import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from src.advisor_engine import DisasterResponseAdvisor # type: ignore
from src.rules import Disaster # type: ignore

def run_advisor():
    engine = DisasterResponseAdvisor()
    engine.reset()
    print("=== 🧠 Disaster Response Advisor ===")
    print("Disasters: earthquake, flood, fire, cyclone, tsunami, landslide, drought, pandemic")

    disaster_type = input("Enter disaster type: ").lower()
    engine.declare(Disaster(type=disaster_type))
    engine.run()

if __name__ == "__main__":
    run_advisor()