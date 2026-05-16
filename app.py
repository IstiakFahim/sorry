import streamlit as st

st.set_page_config(
    page_title="Sorry Heeya ❤️",
    page_icon="🥺",
    layout="wide"
)

# SESSION STATE
if "show_buttons" not in st.session_state:
    st.session_state.show_buttons = False
if "forgiven" not in st.session_state:
    st.session_state.forgiven = False

# CSS
st.markdown("""
<style>
/* Import cute Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Nunito:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ffe4e1);
    font-family: 'Nunito', sans-serif;
}

/* Hide streamlit menu */
header, footer, #MainMenu {
    visibility: hidden;
}

/* Main content */
.main {
    text-align: center;
    padding-top: 40px;
    color: #d81b60; /* Darker, softer pink for readability */
}

/* Title with floating animation */
.title {
    font-family: 'Caveat', cursive;
    font-size: 80px;
    font-weight: bold;
    color: #ff4081;
    text-shadow: 2px 2px 10px rgba(255, 64, 129, 0.3);
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* Message */
.message {
    font-size: 26px;
    line-height: 1.8;
    margin-top: 20px;
    color: #5a2a3b;
    font-weight: 600;
}

/* Footer */
.footer {
    margin-top: 80px;
    font-size: 20px;
    opacity: 0.8;
    text-align: center;
    color: #d81b60;
    font-family: 'Caveat', cursive;
}

/* Button styling */
div.stButton > button:first-child {
    background: linear-gradient(45deg, #ff4081, #ff79b0);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 15px 30px;
    font-size: 24px;
    font-family: 'Nunito', sans-serif;
    font-weight: bold;
    box-shadow: 0px 5px 15px rgba(255, 64, 129, 0.4);
    transition: all 0.3s ease;
}

/* Bouncy hover effect */
div.stButton > button:first-child:hover {
    transform: scale(1.1) translateY(-2px);
    box-shadow: 0px 8px 20px rgba(255, 64, 129, 0.6);
    color: white;
}

/* Custom Success Message Box */
.success-text {
    text-align: center;
    font-family: 'Caveat', cursive;
    font-size: 55px;
    color: #d81b60;
    background: rgba(255, 255, 255, 0.6);
    padding: 20px;
    border-radius: 30px;
    margin-top: 30px;
    box-shadow: 0px 10px 30px rgba(255, 182, 193, 0.8);
    animation: pop 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes pop {
    0% { transform: scale(0.5); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
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

# OPEN BUTTON
if not st.session_state.show_buttons:
    col1, col2, col3 = st.columns([3, 2, 3])
    
    with col2:
        if st.button("Open My Heart 🌸", use_container_width=True):
            st.session_state.show_buttons = True
            st.rerun()

# YES / NO BUTTONS
if st.session_state.show_buttons and not st.session_state.forgiven:

    st.markdown(
        "<h1 style='text-align:center;color:#d81b60;font-family:\"Nunito\", sans-serif;'>Will you forgive me? 🥺</h1>",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns([2, 1, 1, 2])

    with col2:
        # If Yes is clicked, update the session state
        if st.button("Yes ❤️", use_container_width=True):
            st.session_state.forgiven = True
            st.rerun()

    with col3:
        if st.button("No 💔", use_container_width=True):
            # Cute little popup if she clicks No
            st.toast("Please? 🥺", icon="😭") 

# PERFECTLY CENTERED SUCCESS MESSAGE
if st.session_state.forgiven:
    st.balloons()
    
    # Empty columns just to squeeze the width of the success box slightly
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("""
        <div class="success-text">
        YAYYYY 😭❤️ Heeya forgave Meeeeeeeeeeeeeeeeeeee! 🎉💕<br>
        <span style="font-size:35px; color:#ff4081;">I promise to be better! 🌸</span>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
Made with love, regret & overthinking by Fahim Istiak 💖
</div>
""", unsafe_allow_html=True)
