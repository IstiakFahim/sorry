import streamlit as st

st.set_page_config(page_title="I'm Sorry ❤️", page_icon="🥺")

st.markdown(
    """
    <style>
    .main {
        background-color: #ffd6e7;
    }

    .title {
        text-align: center;
        color: #ff4f81;
        font-size: 50px;
        font-weight: bold;
    }

    .text {
        text-align: center;
        color: #555;
        font-size: 22px;
        line-height: 1.6;
    }

    .box {
        background: white;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='box'>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🥺 I’m Really Sorry 💌</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <p class='text'>
    I know I messed up and hurt you.<br>
    That was never my intention.<br><br>

    You mean a lot to me, and I truly regret making you sad.<br>
    I hope you can forgive me ❤️
    </p>
    """,
    unsafe_allow_html=True
)

if st.button("Forgive Me? 🌸"):
    st.balloons()
    st.success("Thank you for hearing me out ❤️")

st.markdown("</div>", unsafe_allow_html=True)