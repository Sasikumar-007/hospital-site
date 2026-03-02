from flask import Blueprint, jsonify, request
from middleware.auth_middleware import jwt_required
from services.ai_engine import run_dosha_analysis
from services.therapist_service import suggest_therapist

api = Blueprint("api", __name__)


@api.post("/appointments")
@jwt_required(["admin", "doctor", "patient"])
def create_appointment():
    payload = request.json or {}
    return jsonify({"message": "Appointment created", "data": payload}), 201


@api.post("/ai-dosha-analysis")
@jwt_required(["admin", "doctor", "patient"])
def ai_dosha_analysis():
    symptoms = (request.json or {}).get("symptoms", [])
    result = run_dosha_analysis(symptoms)
    return jsonify({"message": "Analysis complete", "data": result})


@api.post("/suggest-therapist")
@jwt_required(["admin", "doctor"])
def therapist_suggestion():
    payload = request.json or {}
    therapist = suggest_therapist(payload.get("therapists", []), payload.get("therapy_needed", ""))
    if therapist is None:
        return jsonify({"message": "No therapist available"}), 404
    return jsonify({"message": "Therapist suggested", "data": therapist})


@api.post("/generate-prescription")
@jwt_required(["admin", "doctor"])
def generate_prescription():
    payload = request.json or {}
    return jsonify({"message": "Prescription generated", "data": payload}), 201


@api.post("/assign-therapy")
@jwt_required(["admin", "doctor"])
def assign_therapy():
    payload = request.json or {}
    return jsonify({"message": "Therapy assigned", "data": payload}), 201


@api.get("/dashboard-data")
@jwt_required(["admin", "doctor", "therapist"])
def dashboard_data():
    return jsonify(
        {
            "total_patients": 1204,
            "total_doctors": 34,
            "total_therapists": 57,
            "total_appointments": 2489,
            "therapy_distribution": {"Vata": 41, "Pitta": 34, "Kapha": 25},
            "monthly_trends": [120, 155, 180, 210, 240, 270]
        }
    )
