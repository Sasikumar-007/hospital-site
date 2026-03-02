SYMPTOM_WEIGHTS = {
    "dry_skin": {"vata": 3, "pitta": 0, "kapha": 0},
    "anxiety": {"vata": 2, "pitta": 1, "kapha": 0},
    "acidity": {"vata": 0, "pitta": 3, "kapha": 0},
    "irritability": {"vata": 0, "pitta": 2, "kapha": 0},
    "lethargy": {"vata": 0, "pitta": 0, "kapha": 3},
    "weight_gain": {"vata": 0, "pitta": 0, "kapha": 2}
}

THERAPY_MAP = {
    "vata": {
        "therapy": "Abhyanga + Basti",
        "medicines": ["Ashwagandha", "Dashamoola"],
        "diet": "Warm, unctuous meals and regular routine."
    },
    "pitta": {
        "therapy": "Virechana + Shirodhara",
        "medicines": ["Guduchi", "Amalaki"],
        "diet": "Cooling foods, avoid excess spice and oil."
    },
    "kapha": {
        "therapy": "Udvartana + Vamana",
        "medicines": ["Trikatu", "Guggulu"],
        "diet": "Light warm meals and active daily routine."
    }
}


def run_dosha_analysis(symptoms: list[str]) -> dict:
    scores = {"vata": 0, "pitta": 0, "kapha": 0}
    for symptom in symptoms:
        weights = SYMPTOM_WEIGHTS.get(symptom, {})
        for dosha in scores:
            scores[dosha] += weights.get(dosha, 0)

    dominant = max(scores, key=scores.get)
    total = sum(scores.values()) or 1
    confidence = round((scores[dominant] / total) * 100, 2)

    recommendation = THERAPY_MAP[dominant]
    return {
        "dominant_dosha": dominant,
        "confidence": confidence,
        "scores": scores,
        "recommended_therapy": recommendation["therapy"],
        "suggested_medicines": recommendation["medicines"],
        "diet_advice": recommendation["diet"]
    }
