from app.cafe import Cafe

from app.errors import VaccineError, NotWearingMaskError

from typing import List


def go_to_cafe(friends: List[dict], cafe: Cafe) -> str:
    masks_needed = sum(1 for friend in friends if not friend.get("wearing_a_mask", False))
    unvaccinated = any("vaccine" not in friend or friend["vaccine"].get("expiration_date", date.min) < date.today() for friend in friends)

    if unvaccinated:
        return "All friends should be vaccinated"

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"