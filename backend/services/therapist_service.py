def suggest_therapist(therapists: list[dict], therapy_needed: str) -> dict | None:
    eligible = [
        therapist
        for therapist in therapists
        if therapy_needed in therapist.get("specializations", []) and therapist.get("available", False)
    ]
    if not eligible:
        return None

    return sorted(eligible, key=lambda row: row.get("active_cases", 999))[0]
