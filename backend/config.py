from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    whatsapp_number: str
    lead_storage_path: Path
    review_storage_path: Path = Path("instance/reviews.jsonl")

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            whatsapp_number=os.getenv("WHATSAPP_NUMBER", "56953021437"),
            lead_storage_path=Path(
                os.getenv("LEAD_STORAGE_PATH", "instance/contact_leads.jsonl")
            ),
            review_storage_path=Path(
                os.getenv("REVIEW_STORAGE_PATH", "instance/reviews.jsonl")
            ),
        )
