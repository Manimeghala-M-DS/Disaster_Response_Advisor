"""
advisor_engine.py
Implements the DisasterResponseAdvisor KnowledgeEngine with rules.
"""

from experta import KnowledgeEngine, Rule, MATCH
from src.rules import Disaster, SAFETY_CONTACTS, GENERAL_SAFETY


class DisasterResponseAdvisor(KnowledgeEngine):
    """
    Rule-based Expert System for disaster safety recommendations.
    """

    # ---------- EARTHQUAKE ----------
    @Rule(Disaster(type="earthquake"))
    def earthquake_basic(self):
        print("\n🪨 EARTHQUAKE — Basic Safety:")
        print("- Drop, Cover, and Hold On.")
        print("- Stay away from windows, mirrors, and heavy furniture.")
        print("- If outdoors, move to open areas away from buildings.")
        print("- After shaking stops, check for injuries and gas leaks.")
        print("Emergency contact:", SAFETY_CONTACTS.get("earthquake"))

    @Rule(Disaster(type="earthquake", injured_people=True))
    def earthquake_injured(self):
        print("\n⚕️ Earthquake + Injuries:")
        print("- Provide first aid if trained.")
        print("- Move injured people only if absolutely necessary.")
        print("- Contact emergency services immediately.")

    # ---------- FLOOD ----------
    @Rule(Disaster(type="flood"))
    def flood_basic(self):
        print("\n🌊 FLOOD — Basic Safety:")
        print("- Move to higher ground immediately.")
        print("- Avoid walking or driving through floodwaters.")
        print("- Boil or purify water before drinking.")
        print("- Turn off gas and electricity if instructed.")
        print("Emergency contact:", SAFETY_CONTACTS.get("flood"))

    @Rule(Disaster(type="flood", has_clean_water=False))
    def flood_no_clean_water(self):
        print("\n⚠️ Flood + No Clean Water:")
        print("- Boil water for at least 1 minute or use purification tablets.")
        print("- Collect rainwater if safe and store it properly.")

    # ---------- FIRE ----------
    @Rule(Disaster(type="fire"))
    def fire_basic(self):
        print("\n🔥 FIRE — Basic Safety:")
        print("- Crawl low under smoke; exit using stairs.")
        print("- Use a wet cloth to cover mouth and nose.")
        print("- Never use elevators during fire evacuation.")
        print("- Signal rescuers from windows if trapped.")
        print("Emergency contact:", SAFETY_CONTACTS.get("fire"))

    @Rule(Disaster(type="fire", is_indoor=True))
    def indoor_fire(self):
        print("\n⚠️ Indoor Fire:")
        print("- Close doors behind you to slow down fire spread.")
        print("- Seal door gaps with wet cloth and signal rescuers.")
        print("- Stay low and head toward the nearest safe exit.")

    # ---------- CYCLONE ----------
    @Rule(Disaster(type="cyclone"))
    def cyclone_basic(self):
        print("\n🌪️ CYCLONE — Basic Safety:")
        print("- Secure windows, doors, and outdoor objects.")
        print("- Keep an emergency kit (water, flashlight, medicines).")
        print("- Stay indoors in a safe room away from windows.")
        print("- Listen to official updates via radio or phone.")
        print("Emergency contact:", SAFETY_CONTACTS.get("cyclone"))

    # ---------- TSUNAMI ----------
    @Rule(Disaster(type="tsunami"))
    def tsunami_basic(self):
        print("\n🌊 TSUNAMI — Basic Safety:")
        print("- If near the coast and feel an earthquake, move inland or to higher ground immediately.")
        print("- Never go to the shore to watch the waves.")
        print("- Stay away until authorities declare it safe.")
        print("Emergency contact:", SAFETY_CONTACTS.get("tsunami"))

    @Rule(Disaster(type="tsunami", is_coastal=True))
    def coastal_tsunami(self):
        print("\n⚠️ Coastal Area + Tsunami Risk:")
        print("- Move to high ground immediately after strong shaking.")
        print("- Follow official evacuation routes and alerts.")

    # ---------- LANDSLIDE ----------
    @Rule(Disaster(type="landslide"))
    def landslide_basic(self):
        print("\n🏔️ LANDSLIDE — Basic Safety:")
        print("- Move away from slopes or steep terrain immediately.")
        print("- Watch for cracks, leaning trees, and unusual sounds.")
        print("- Avoid river valleys and low-lying areas.")
        print("- Stay tuned for weather warnings and updates.")
        print("Emergency contact:", SAFETY_CONTACTS.get("landslide"))

    # ---------- DROUGHT ----------
    @Rule(Disaster(type="drought"))
    def drought_basic(self):
        print("\n☀️ DROUGHT — Water Conservation:")
        print("- Conserve water: fix leaks, minimize outdoor use.")
        print("- Store clean drinking water in sealed containers.")
        print("- Support community water-saving measures.")
        print("Emergency contact:", SAFETY_CONTACTS.get("drought"))

    # ---------- PANDEMIC ----------
    @Rule(Disaster(type="pandemic"))
    def pandemic_basic(self):
        print("\n🧫 PANDEMIC — Health Safety:")
        print("- Maintain hygiene; wash hands frequently with soap.")
        print("- Wear masks in crowded or indoor areas.")
        print("- Avoid unnecessary travel or gatherings.")
        print("- Isolate and seek medical help if symptomatic.")
        print("Emergency contact:", SAFETY_CONTACTS.get("pandemic"))

    # ---------- UNKNOWN / GENERAL ----------
    @Rule(Disaster(type=MATCH.t))
    def unknown_disaster(self, t):
        known = [
            "earthquake", "flood", "fire", "cyclone",
            "tsunami", "landslide", "drought", "pandemic"
        ]
        if t not in known:
            print(f"\n❓ Unknown disaster type '{t}'. Showing general safety tips:")
            for msg in GENERAL_SAFETY:
                print("-", msg)


# ✅ Quick test mode (optional)
if __name__ == "__main__":
    # Run the engine standalone to verify rules
    print("Running Disaster Advisor test:")
    engine = DisasterResponseAdvisor()
    engine.reset()
    engine.declare(Disaster(type="earthquake", is_indoor=True))
    engine.run()

