"""
rules.py
Defines the Disaster Fact and supporting data for the Disaster Response Advisor Expert System.
"""

from experta import Fact


class Disaster(Fact):
    """
    Fact representing the current disaster situation.
    Each instance of this fact contains the environmental and situational data 
    that the rule engine uses to provide context-aware advice.

    Example attributes:
        - type (str): disaster type (e.g., earthquake, flood, fire, cyclone, etc.)
        - is_indoor (bool): whether the person is indoors
        - has_first_aid (bool): whether a first-aid kit is available
        - has_clean_water (bool): whether clean water is accessible
        - is_coastal (bool): whether the person is in a coastal area
        - injured_people (bool): whether there are injured people nearby
    """
    pass


# 📞 Emergency contact details — customize based on your country
SAFETY_CONTACTS = {
    "earthquake": "Emergency Services: 112 or local disaster helpline",
    "flood": "Flood Rescue / Disaster Management Unit: Contact local authority",
    "fire": "Fire Department: Dial 101 (India) or your local emergency number",
    "cyclone": "State Disaster Management Control Room / Weather Dept Helpline",
    "tsunami": "Coastal Emergency Response Center or local evacuation team",
    "landslide": "District Disaster Response Force or local rescue authority",
    "drought": "Municipal Water Resource and Rural Relief Helpline",
    "pandemic": "Public Health Hotline / Hospital Emergency Desk",
}


# 💡 General safety recommendations — used for unknown or undefined disasters
GENERAL_SAFETY = [
    "Stay calm and avoid panic.",
    "Follow official instructions from disaster authorities.",
    "Contact emergency services immediately if there are injuries.",
    "Keep emergency supplies ready — first aid, flashlight, water, and non-perishable food.",
    "If safe, assist neighbors or vulnerable individuals nearby.",
    "Stay updated using verified radio, TV, or mobile alerts.",
]
