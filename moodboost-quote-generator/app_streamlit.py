import streamlit as st
from emotion_analysis import detect_emotions
from quote_selector import get_quotes_for_emotions

# -------------------- Setup --------------------
st.set_page_config(page_title="MoodBoost Quotes", page_icon="💬")
st.title("💬 MoodBoost Quote Generator")
st.write("Tell me how you're feeling and click **Show me quotes!** for a lift.")
st.markdown("Type **`quit`**, **`exit`**, or **`q`** to close the app anytime.")

# -------------------- Session-state defaults --------------------
DEFAULTS = {
    "emotions"     : [],
    "quotes"       : [],          # <-- ensure key exists
    "show_more"    : False,
    "more_choice"  : None,
    "typed_text"   : ""
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -------------------- Text input --------------------
user_input = st.text_area(
    "How are you feeling today?",
    placeholder="e.g. I'm feeling really overwhelmed and anxious",
    value=st.session_state.get("typed_text", "")
)

# -------------------- Main logic --------------------
if user_input:
    txt = user_input.strip()
    st.session_state.typed_text = user_input  # remember text

    # Quit commands
    if txt.lower() in {"quit", "exit", "q", "e"}:
        st.warning("👋 Take care. See you next time.")
        st.stop()

    # Detect emotions immediately
    st.session_state.emotions = detect_emotions(txt)
    if not st.session_state.emotions:
        st.error("🤔 Hmm, I'm not sure how you're feeling. Did you spell it correctly? Refresh and try again.")
        st.stop()

    st.markdown(f"**Detected emotions:** {', '.join(st.session_state.emotions)}")

    # Show-quotes button
    if st.button("✨ Show me quotes!"):
        st.session_state.quotes = get_quotes_for_emotions(st.session_state.emotions)
        st.session_state.show_more = False
        st.experimental_rerun()

# -------------------- Display quotes --------------------
if st.session_state.get("quotes"):
    st.markdown("---")
    for q in st.session_state.quotes:
        st.success(f"“{q}”")

    st.session_state.more_choice = st.radio(
        "Would you like more quotes?",
        ["No", "Yes"],
        index=0,
        key="more_radio"
    )

    if st.session_state.more_choice == "Yes" and not st.session_state.show_more:
        st.session_state.quotes = get_quotes_for_emotions(st.session_state.emotions)
        st.session_state.show_more = True
        st.experimental_rerun()

    if st.session_state.more_choice == "No" and st.session_state.show_more:
        st.info("❤️ Glad I could help. Take care!")
