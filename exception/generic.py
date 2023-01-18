import json
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ExceptionError(Exception):
    message: str
    payload: Any = None

    def __post_init__(self):

        if self.payload and isinstance(self.payload, Dict):
            self.payload = json.dumps(self.payload)

    def __str__(self):
        return '\n'.join([self.message, self.payload or ''])


class GErrorValue(ExceptionError):

    message: str = "Failed to update!"
