import streamlit as st
import random

st.set_page_config(
    page_title="Sorry Heeya ❤️",
    page_icon="🥺",
    layout="wide"
)

# Session state
if "show_question" not in st.session_state:
    st.session_state.show_question = False

if "no_x" not in st.session_state:
    st.session_state.no_x = random.randint(5, 85)

if "no_y" not in st.session_state:
    st.session_state.no_y = random.randint(20, 80)

# Background + styling
st.markdown(
    f"""
    <style>

    .stApp {{
        background: linear-gradient(135deg, #ff9ec4, #ffd6e7, #ffc2d1);
        overflow: hidden;
    }}

    /* Hide ugly streamlit stuff */
    header {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    .main-text {{
        text-align: center;
        padding-top: 80px;
    }}

    .title {{
        font-size: 60px;
        color: white;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }}

    .message {{
        font-size: 26px;
        color: white;
        line-height: 1.8;
        max-width: 900px;
        margin: auto;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.15);
    }}

    .footer {{
        text-align: center;
        margin-top: 50px;
        color: white;
        font-size: 18px;
    }}

    .yes-btn button {{
        background-color: #ff4f81 !important;
        color: white !important;
        border-radius: 40px !important;
        height: 3.5em;
        width: 10em;
        font-size: 20px !important;
        border: none !important;
    }}

    .yes-btn button:hover {{
        transform: scale(1.08);
        transition: 0.2s;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.markdown(
    """
    <div class="main-text">
        <div class="title">🥺 I'm Really Sorry Heeya 💌</div>

        <br>

        <div class="message">
            Saima Ekram Heeya,<br><br>

            I know I messed up and hurt you.<br>
            That was never my intention.<br><br>

            You genuinely mean a lot to me,
            and seeing you upset because of me hurts deeply.<br><br>

            I never wanted to make you sad.<br>
            Please forgive this dumb human named Fahim Istiak ❤️
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Open heart button
if not st.session_state.show_question:
    if st.button("Open My Heart 🌸"):
        st.session_state.show_question = True
        st.rerun()

# Yes/No buttons
if st.session_state.show_question:

    st.markdown(
        "<h1 style='text-align:center; color:white;'>Will you forgive me? 🥺</h1>",
        unsafe_allow_html=True
    )

    # YES BUTTON CENTER
    st.markdown("<div class='yes-btn'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("Yes ❤️"):
            st.balloons()
            st.success("YAYYY 😭❤️ Heeya forgave Fahim!")

    st.markdown("</div>", unsafe_allow_html=True)

    # MOVING NO BUTTON
    no_placeholder = st.empty()

    with no_placeholder.container():

        st.markdown(
            f'''
            <div style="
                position: fixed;
                left: {st.session_state.no_x}%;
                top: {st.session_state.no_y}%;
                z-index: 999;
            ">
            ''',
            unsafe_allow_html=True
        )

        if st.button("No 💔"):
            st.session_state.no_x = random.randint(0, 90)
            st.session_state.no_y = random.randint(10, 90)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        Made with love, regret & overthinking by Fahim Istiak 💖
    </div>
    """,
    unsafe_allow_html=True
)
