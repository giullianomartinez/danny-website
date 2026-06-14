from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    whatsapp_number: str
    lead_storage_path: Path

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            whatsapp_number=os.getenv("WHATSAPP_NUMBER", "56953021437"),
            lead_storage_path=Path(
                os.getenv("LEAD_STORAGE_PATH", "instance/contact_leads.jsonl")
            ),
        )
