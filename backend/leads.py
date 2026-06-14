from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from typing import Any
from urllib.parse import quote
from uuid import uuid4

from backend.config import Settings


class LeadValidationError(ValueError):
    pass


@dataclass(frozen=True)
class Lead:
    id: str
    name: str
    contact: str
    message: str
    event_type: str = ""
    event_date: str = ""
    location: str = ""
    services: list[str] = field(default_factory=list)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def public_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data.pop("message")
        return data


def create_lead(payload: dict[str, Any], settings: Settings) -> Lead:
    lead = _parse_lead(payload)
    _save_lead(lead, settings)
    return lead


def lead_to_whatsapp_url(lead: Lead, settings: Settings) -> str:
    lines = [
        f"Hola, soy {lead.name}.",
        f"Contacto: {lead.contact}",
    ]

    if lead.event_type:
        lines.append(f"Tipo de evento: {lead.event_type}")
    if lead.event_date:
        lines.append(f"Fecha: {lead.event_date}")
    if lead.location:
        lines.append(f"Lugar: {lead.location}")
    if lead.services:
        lines.append(f"Servicios: {', '.join(lead.services)}")

    lines.append(f"Mensaje: {lead.message}")
    return f"https://wa.me/{settings.whatsapp_number}?text={quote(chr(10).join(lines))}"


def _parse_lead(payload: dict[str, Any]) -> Lead:
    name = _required_text(payload, "name", "nombre")
    contact = _required_text(payload, "contact", "contacto")
    message = _required_text(payload, "message", "mensaje")

    return Lead(
        id=uuid4().hex,
        name=name,
        contact=contact,
        message=message,
        event_type=_optional_text(payload, "event_type"),
        event_date=_optional_text(payload, "event_date"),
        location=_optional_text(payload, "location"),
        services=_parse_services(payload.get("services", [])),
    )


def _required_text(payload: dict[str, Any], field_name: str, label: str) -> str:
    value = _optional_text(payload, field_name)
    if not value:
        raise LeadValidationError(f"El campo {label} es obligatorio.")
    return value


def _optional_text(payload: dict[str, Any], field_name: str) -> str:
    value = payload.get(field_name, "")
    if value is None:
        return ""
    return str(value).strip()


def _parse_services(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def _save_lead(lead: Lead, settings: Settings) -> None:
    settings.lead_storage_path.parent.mkdir(parents=True, exist_ok=True)
    with settings.lead_storage_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(asdict(lead), ensure_ascii=True) + "\n")
