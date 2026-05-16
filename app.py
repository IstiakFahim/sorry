import streamlit as st
import random

st.set_page_config(page_title="Sorry Heeya ❤️", page_icon="🥺")

# Session state
if "show_question" not in st.session_state:
    st.session_state.show_question = False

if "no_x" not in st.session_state:
    st.session_state.no_x = random.randint(10, 80)

if "no_y" not in st.session_state:
    st.session_state.no_y = random.randint(10, 80)

# Background and styling
st.markdown(
    """
    <style>
    .main {
        background-color: #ffd6e7;
    }

    .box {
        background: white;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
    }

    .title {
        color: #ff4f81;
        font-size: 50px;
        font-weight: bold;
    }

    .text {
        color: #555;
        font-size: 22px;
        line-height: 1.7;
    }

    .footer {
        margin-top: 30px;
        color: gray;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='box'>", unsafe_allow_html=True)

st.markdown(
    "<h1 class='title'>🥺 I'm Really Sorry Saima Ekram Heeya 💌</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class='text'>
    I know I messed up and hurt you.<br><br>

    You are genuinely one of the most important people in my life,
    and seeing you upset because of me hurts a lot.<br><br>

    I never wanted to make you sad.<br>
    Please forgive this dumb human named Fahim Istiak ❤️
    </p>
    """,
    unsafe_allow_html=True
)

# First button
if not st.session_state.show_question:
    if st.button("Open My Heart 🌸"):
        st.session_state.show_question = True
        st.rerun()

# Yes/No section
if st.session_state.show_question:

    st.markdown("## Will you forgive me? 🥺")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes ❤️"):
            st.balloons()
            st.success("YAYYY 😭❤️ Thank you Heeya, Fahim loves you so much!")

    with col2:
        # Moving No button
        st.markdown(
            f'''
            <div style="
                position: relative;
                left: {random.randint(-100,100)}px;
                top: {random.randint(-20,20)}px;
            ">
            ''',
            unsafe_allow_html=True
        )

        if st.button("No 💔"):
            st.session_state.no_x = random.randint(10, 80)
            st.session_state.no_y = random.randint(10, 80)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer'>Made with love, regret & overthinking by Fahim Istiak 💖</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
