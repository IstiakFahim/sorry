import streamlit as st

st.set_page_config(
    page_title="Sorry Heeya ❤️",
    page_icon="🥺",
    layout="wide"
)

# SESSION STATE
if "show_buttons" not in st.session_state:
    st.session_state.show_buttons = False

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ff9ec4, #ffc2d1, #ffd6e7);
}

/* Hide streamlit menu */
header, footer, #MainMenu {
    visibility: hidden;
}

/* Main content */
.main {
    text-align: center;
    padding-top: 60px;
    color: white;
}

/* Title */
.title {
    font-size: 65px;
    font-weight: bold;
    text-shadow: 2px 2px 15px rgba(0,0,0,0.2);
}

/* Message */
.message {
    font-size: 28px;
    line-height: 1.8;
    margin-top: 30px;
    text-shadow: 1px 1px 10px rgba(0,0,0,0.15);
}

/* Footer */
.footer {
    margin-top: 80px;
    font-size: 18px;
    opacity: 0.9;
    text-align: center;
    color: white;
}

/* Center all buttons inside their containers */
div.stButton {
    display: flex;
    justify-content: center;
}

/* Button styling */
div.stButton > button:first-child {
    background-color: #ff4f81;
    color: white;
    border: none;
    border-radius: 40px;
    padding: 12px 28px;
    font-size: 22px;
    transition: 0.3s;
}

div.stButton > button:first-child:hover {
    background-color: #ff2f68;
    transform: scale(1.08);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# MAIN CONTENT
st.markdown("""
<div class="main">

<div class="title">
🥺 I'm Really Sorry Heeya 💌
</div>

<div class="message">

Saima Ekram Heeya,<br><br>

I know I messed up and hurt you.<br>
That was never my intention.<br><br>

You genuinely mean a lot to me,<br>
and seeing you upset because of me hurts deeply.<br><br>

I never wanted to make you sad.<br>
Please forgive this dumb human named Fahim Istiak ❤️

</div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# OPEN BUTTON (PROPER CENTER FIX)
if not st.session_state.show_buttons:
    # Because of the CSS flexbox, this will now be perfectly centered 
    # without needing column hacks.
    if st.button("Open My Heart 🌸"):
        st.session_state.show_buttons = True
        st.rerun()

# YES / NO BUTTONS
if st.session_state.show_buttons:

    st.markdown(
        "<h1 style='text-align:center;color:white;'>Will you forgive me? 🥺</h1>",
        unsafe_allow_html=True
    )

    # Using 4 columns keeps the buttons clustered tightly in the center
    col1, col2, col3, col4 = st.columns([2, 1, 1, 2])

    with col2:
        if st.button("Yes ❤️", use_container_width=True):
            st.balloons()
            st.success("YAYYYY 😭❤️ Heeya forgave Fahim!")

    with col3:
        st.button("No 💔", use_container_width=True)

# FOOTER
st.markdown("""
<div class="footer">
Made with love, regret & overthinking by Fahim Istiak 💖
</div>
""", unsafe_allow_html=True)
