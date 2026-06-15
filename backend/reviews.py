from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from typing import Any
from uuid import uuid4

from backend.config import Settings


class ReviewValidationError(ValueError):
    pass


@dataclass(frozen=True)
class Review:
    id: str
    name: str
    rating: int
    comment: str
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def public_dict(self) -> dict[str, Any]:
        return asdict(self)


def create_review(payload: dict[str, Any], settings: Settings) -> Review:
    review = _parse_review(payload)
    _save_review(review, settings)
    return review


def list_reviews(settings: Settings) -> list[Review]:
    if not settings.review_storage_path.exists():
        return []

    reviews: list[Review] = []
    with settings.review_storage_path.open(encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue
            data = json.loads(line)
            reviews.append(
                Review(
                    id=str(data["id"]),
                    name=str(data["name"]),
                    rating=int(data["rating"]),
                    comment=str(data["comment"]),
                    created_at=str(data["created_at"]),
                )
            )
    return sorted(reviews, key=lambda review: review.created_at, reverse=True)


def _parse_review(payload: dict[str, Any]) -> Review:
    name = _required_text(payload, "name", "nombre")
    comment = _required_text(payload, "comment", "comentario")
    rating = _parse_rating(payload.get("rating"))

    return Review(id=uuid4().hex, name=name, rating=rating, comment=comment)


def _parse_rating(value: Any) -> int:
    try:
        rating = int(value)
    except (TypeError, ValueError):
        raise ReviewValidationError("La calificacion debe estar entre 1 y 5.")

    if rating < 1 or rating > 5:
        raise ReviewValidationError("La calificacion debe estar entre 1 y 5.")
    return rating


def _required_text(payload: dict[str, Any], field_name: str, label: str) -> str:
    value = payload.get(field_name, "")
    if value is None:
        value = ""
    text = str(value).strip()
    if not text:
        raise ReviewValidationError(f"El campo {label} es obligatorio.")
    return text


def _save_review(review: Review, settings: Settings) -> None:
    settings.review_storage_path.parent.mkdir(parents=True, exist_ok=True)
    with settings.review_storage_path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(asdict(review), ensure_ascii=True) + "\n")
