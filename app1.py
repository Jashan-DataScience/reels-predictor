import random
import streamlit as st

st.set_page_config(
    page_title="Reels Time Waster Predictor", page_icon="📱", layout="centered"
)

st.title("📱 Instagram Reels & Social Media 'Time Waster' Predictor")
st.write(
    "Unmai-ah sollu, inniki unga life-ah antha algorithm-ku evlo neram gift panna"
    " poreenga? Intha app check pannum!"
)

# Sidebar or main inputs
st.header("🔍 Ungaloda Daily Scrolling Habits:")

reels_hours = st.slider(
    "Daily evlo hours Reels / Shorts pakkeenga?", 0.0, 12.0, 3.5
)

night_scroll = st.selectbox(
    "Thungura munnaadi bed-la phone use panreengala?",
    [
        "Kandippa, 2-3 hours over-ah scroll panruven!",
        "Konjam neram pakki thungiruven",
        "Illave illa, romba good boy/girl",
    ],
)

boredom_trigger = st.selectbox(
    "Bore adikumbothu ungaloda instant reaction enna?",
    [
        "Oru second kooda yosikkama Insta-va open panruven",
        "Gallery-la irukura old screenshots-ah pakka aarambichiduven",
        "Real-world-la yaarachu irukangala nu pakkuven",
    ],
)

# Button to calculate result
if st.button("Calculate My Wasted Life 💀"):
  # Score calculation logic
  score = reels_hours * 12
  if "over-ah" in night_scroll:
    score += 40
  if "open panruven" in boredom_trigger:
    score += 20

  st.markdown("---")
  st.subheader("📊 Ungaloda Result:")

  if score < 30:
    st.success(
        "🟢 **Status: Normal Human!** Ungalukku innum real-world friends irukanga."
        " Super!"
    )
  elif score < 70:
    st.warning(
        "🟡 **Status: Moderate Scroller!** Unga screen time-ah konjam"
        " kammi pannunga, illana battery-um data-um theernthudum!"
    )
  else:
    st.error(
        "🔴 **Status: 🧟‍♂️ Zombie Scroll Master!** Unga brain ippo oru AI"
        " recommendation engine mathiri maariduchu! Ungalukku 'Disconnect'"
        " button work aagathu!"
    )

  # Random funny quotes
  funny_quotes = [
      (
          "Warning: Ungala pathu antha Insta algorithm-kku romba santhosham"
          " aagiruchu!"
      ),
      (
          "Unga frnds ellam ungaloda Insta Broadcast Channel-ah pathu thaan neenga"
          " uyiroda irukeenga nu confirm panranga!"
      ),
      (
          "Next birth-la neenga oru Wi-Fi Router-ah thaan porakka poreenga!"
      ),
      "Oru 10 reels kku oru murai, romba mukkiyam-ana 'touch grass' pannunga!",
  ]
  st.info(f"💡 **Algorithm Verdict:** {random.choice(funny_quotes)}")