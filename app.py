import streamlit as st
import random

st.set_page_config(
    page_title="Sorry Heeya ❤️",
    page_icon="🥺",
    layout="wide"
)

# SESSION
if "show_buttons" not in st.session_state:
    st.session_state.show_buttons = False

if "no_pos" not in st.session_state:
    st.session_state.no_pos = (random.randint(5, 85), random.randint(20, 80))

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ff9ec4, #ffc2d1, #ffd6e7);
    overflow: hidden;
}

/* Hide streamlit stuff */
header, footer, #MainMenu {
    visibility: hidden;
}

/* Main container */
.main-box {
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
    margin-top: 30px;
    font-size: 28px;
    line-height: 1.8;
    text-shadow: 1px 1px 10px rgba(0,0,0,0.15);
}

/* Footer */
.footer {
    margin-top: 80px;
    font-size: 18px;
    opacity: 0.9;
}

/* YES button */
div.stButton > button:first-child {
    background-color: #ff4f81;
    color: white;
    border-radius: 40px;
    border: none;
    height: 3.5em;
    width: 11em;
    font-size: 22px;
    transition: 0.3s;
}

div.stButton > button:first-child:hover {
    transform: scale(1.1);
    background-color: #ff2f68;
    color: white;
}

/* Floating hearts */
.hearts {
    position: fixed;
    font-size: 25px;
    animation: float 6s infinite ease-in-out;
    opacity: 0.6;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}

</style>
""", unsafe_allow_html=True)

# Floating hearts
for i in range(15):
    st.markdown(
        f"""
        <div class="hearts"
        style="
            left:{random.randint(0,100)}%;
            top:{random.randint(0,100)}%;
            animation-delay:{random.uniform(0,5)}s;
        ">
        💖
        </div>
        """,
        unsafe_allow_html=True
    )

# MAIN CONTENT
st.markdown("""
<div class="main-box">

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
    if st.button("Open My Heart 🌸"):
        st.session_state.show_buttons = True
        st.rerun()

# YES / NO
if st.session_state.show_buttons:

    st.markdown(
        "<h1 style='text-align:center;color:white;'>Will you forgive me? 🥺</h1>",
        unsafe_allow_html=True
    )

    # YES BUTTON
    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("Yes ❤️"):
            st.balloons()
            st.success("YAYYYY 😭❤️ Heeya forgave Fahim!")

    # RANDOM MOVING NO BUTTON
    x, y = st.session_state.no_pos

    st.markdown(
        f"""
        <div style="
            position: fixed;
            left: {x}%;
            top: {y}%;
            z-index: 999999;
        ">
        <form action="">
            <button 
            style="
                background:#444;
                color:white;
                border:none;
                padding:12px 24px;
                border-radius:30px;
                font-size:18px;
                cursor:pointer;
            ">
            No 💔
            </button>
        </form>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Invisible button trigger
    if st.button("no_trigger_hidden_button"):
        pass

    # JS trick
    st.markdown(
        """
        <script>
        const buttons = window.parent.document.querySelectorAll('button');

        buttons.forEach(btn => {
            if(btn.innerText.includes('No 💔')) {
                btn.addEventListener('mouseover', () => {
                    window.location.reload();
                });
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )

    # CHANGE POSITION EVERY RERUN
    st.session_state.no_pos = (
        random.randint(5, 85),
        random.randint(15, 85)
    )

# FOOTER
st.markdown("""
<div class="footer" style="text-align:center;color:white;">
Made with love, regret & overthinking by Fahim Istiak 💖
</div>
""", unsafe_allow_html=True)
