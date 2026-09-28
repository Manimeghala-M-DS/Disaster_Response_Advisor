"""
app.py
Streamlit web interface for the Disaster Response Advisor Expert System.
"""

import io
import sys
import streamlit as st

from src.advisor_engine import DisasterResponseAdvisor # type: ignore
from src.rules import Disaster # pyright: ignore[reportMissingImports]


def run_engine_and_capture(disaster_kwargs):
    """
    Runs the Expert System and captures printed recommendations as text output.
    """
    engine = DisasterResponseAdvisor()
    engine.reset()

    # Declare the fact (user situation)
    engine.declare(Disaster(**disaster_kwargs))

    # Redirect stdout to capture Experta's printed output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        engine.run()
        sys.stdout.flush()
    except Exception as e:
        print("⚠️ Error running inference engine:", e)
    finally:
        sys.stdout = old_stdout

    # Collect advice text
    output = buffer.getvalue().strip()
    if not output:
        output = "⚠️ No advice generated — please check your selections or rules."
    return output


def main():
    # Streamlit UI configuration
    st.set_page_config(page_title="Disaster Response Advisor", layout="centered")
    st.title("🧠 Disaster Response Advisor")
    st.write("Select a disaster type and your situation to get AI-powered safety advice.")

    # Disaster selection dropdown
    disaster_type = st.selectbox(
        "Choose a disaster:",
        [
            "earthquake",
            "flood",
            "fire",
            "cyclone",
            "tsunami",
            "landslide",
            "drought",
            "pandemic",
        ],
    )

    # Collect user input via checkboxes
    st.markdown("### Situation Details")
    col1, col2 = st.columns(2)
    with col1:
        is_indoor = st.checkbox("Are you indoors?")
        has_first_aid = st.checkbox("Do you have a first aid kit?")
    with col2:
        has_clean_water = st.checkbox("Do you have clean water?")
        is_coastal = st.checkbox("Are you in a coastal area?")
    injured_people = st.checkbox("Are there injured people nearby?")

    # When button pressed — run expert system
    if st.button("Get Advice"):
        disaster_kwargs = {
            "type": disaster_type,
            "is_indoor": is_indoor,
            "has_first_aid": has_first_aid,
            "has_clean_water": has_clean_water,
            "is_coastal": is_coastal,
            "injured_people": injured_people,
        }

        st.success("✅ Safety Recommendations:")
        output = run_engine_and_capture(disaster_kwargs)

        # Display advice neatly
        st.code(output, language="text")

        # Optional: allow user to download advice
        st.download_button(
            label="📥 Download Advice as Text",
            data=output,
            file_name=f"{disaster_type}_safety_advice.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    main()
