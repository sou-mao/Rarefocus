"""Frozen diagnosis-name matching prompt and response parser used for evaluation."""

from __future__ import annotations

import re
from collections.abc import Sequence


SYSTEM_PROMPT = "You are a specialist in the field of rare diseases."
INSTRUCTION = (
    "I will now give you five predicted diseases if the predicted diagnosis is in the standard diagnosis. "
    'Please output the predicted rank, otherwise output "No", only output "No" or "1-5" numbers, '
    "if the predicted disease has multiple conditions, only output the top rank. "
    'Output only "No" or one number, no additional output.'
)


def build_prediction_text(candidates: Sequence[str]) -> str:
    """Number the frozen candidates without adding, removing or reordering them."""
    return "\n".join(
        f"{index}. {disease}" for index, disease in enumerate(candidates, start=1)
    )


def build_user_prompt(candidates: Sequence[str], standard_diagnosis: str) -> str:
    """Build the exact user-prompt structure used in the frozen evaluation."""
    prediction_text = build_prediction_text(candidates)
    return (
        INSTRUCTION
        + f"Predicted diseases: {prediction_text}\n"
        + f"Standard diagnosis: {standard_diagnosis}\n"
    )


def parse_rank(raw_response: str | None) -> int | None:
    """Map a valid returned position to 1-5 and an unmatched result to 11."""
    if raw_response is None:
        return None
    compact = raw_response.replace("\n", "").strip()
    if "否" in compact or "No" in compact:
        return 11
    numbers = re.findall(r"\b(?:10|[1-9])\b", compact)
    if not numbers or numbers[0] not in {"1", "2", "3", "4", "5"}:
        return None
    return int(numbers[0])
