import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For You My ❤️", page_icon="💖", layout="centered")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = 1
if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False
if "story_done" not in st.session_state:
    st.session_state.story_done = False
if "opened" not in st.session_state:
    st.session_state.opened = False

# query_params = st.query_params
# if "page" in query_params:
#     st.session_state.page = int(query_params["page"])



# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffd6e0, #ff9a9e);
    text-align: center;
    font-family: Georgia, serif;
}
.big-title {
    font-size: 52px;
    color: #b71c1c;
    font-weight: bold;
}
.text {
    font-size: 22px;
    color: #4a0e2e;
    margin-top: 20px;
}
button[kind="primary"] {
    background:linear-gradient(45deg,#ff4d6d,#ff758f);
    color:white !important;
}
div.stButton > button {
    background: linear-gradient(45deg, #ff4d6d, #ff758f) !important;
    color: white !important;
    border-radius: 50px !important;
    border: none !important;
    padding: 0.7em 2.2em !important;
    font-size: 20px !important;
    font-weight: bold;
    box-shadow: 0 8px 22px rgba(0,0,0,0.25);
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: scale(1.07);
    box-shadow: 0 10px 28px rgba(0,0,0,0.35);
}            
button:hover {
    background:#c2185b !important;
    color:white !important;
}
            
.card {
    background: rgba(255,255,255,0.3);
    backdrop-filter: blur(18px);
    padding: 40px;
    border-radius: 28px;
    box-shadow: 0 18px 50px rgba(0,0,0,0.18);
    font-size: 21px;
    line-height: 2;
    color: #4a0e2e;
    max-width: 750px;
    margin: auto;
    text-align: left;
}
#loveLetter {
    animation: fadeInLetter 1.2s ease forwards;
}

@keyframes fadeInLetter {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeText {
    from { opacity: 0.4; }
    to { opacity: 1; }
}
/* Floating Roses */
.rose {
    position: fixed;
    top: -20px;
    font-size: 24px;
    opacity: 0.7;
    animation: fall 14s linear infinite;
}

@keyframes fall {
    from { transform: translateY(0); }
    to { transform: translateY(120vh); }
}
</style>
""", unsafe_allow_html=True)


import time
from pathlib import Path
def type_text(text, delay=0.07):
    placeholder = st.empty()
    typed = ""

    for char in text:
        typed += char
        placeholder.markdown(
            f"<div class='text' style='animation: fadeText 0.3s ease;'>{typed}</div>",
            unsafe_allow_html=True
        )
        time.sleep(delay)
# ---------------- PAGE 1 ----------------
# if st.session_state.page == 1:
#     st.markdown("<div class='big-title'>Hey You ❤️</div>", unsafe_allow_html=True)
#     st.markdown("<div class='text'>I made something just for you...</div>", unsafe_allow_html=True)

#     if not st.session_state.opened:
#         if st.button("Open It 💌"):
#             st.session_state.opened = True
#             st.session_state.page = 2
#             st.rerun()

import streamlit as st
import streamlit.components.v1 as components
import base64




def autoplay_audio(file_path: str):
    if not Path(file_path).exists():
        return
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""<audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>""",
        unsafe_allow_html=True,
    )
if st.session_state.page == 1:

    st.markdown("<div class='big-title'>Ei Ri❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>I made something just for you...</div>", unsafe_allow_html=True)

    # Hidden Streamlit trigger button
    trigger = st.button("hidden", key="trigger_btn")

    # HTML animated button
    components.html("""
    <button id="myBtn" style="
        background:linear-gradient(45deg,#ff4d6d,#ff758f);
        color:white;
        border:none;
        border-radius:50px;
        padding:12px 35px;
        font-size:20px;
        font-weight:bold;
        cursor:pointer;
        box-shadow:0 8px 22px rgba(0,0,0,0.25);
        transition:0.3s;
    ">Open It 💌</button>

    <script>
    const btn = document.getElementById("myBtn");

    btn.addEventListener("click", () => {
        btn.style.opacity = "0";
        btn.style.transform = "scale(0.7)";
        btn.style.pointerEvents = "none";

        setTimeout(() => {
            const streamlitButton = window.parent.document.querySelector('button[kind="secondary"]');
            if(streamlitButton){ streamlitButton.click(); }
        }, 500);
    });
    </script>
    """, height=120)

    # Hide the real button visually
    st.markdown("""
    <style>
    button[kind="secondary"] { display:none !important; }
    </style>
    """, unsafe_allow_html=True)

    # When hidden button is triggered
    if trigger:
        st.session_state.page = 2
        st.rerun()

    st.stop()
      

# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:
    st.empty()
    page2_container = st.container()  # This becomes your "layout"
    with page2_container:
        for i in range(15):
            st.markdown(f"<div class='rose' style='left:{i*8}%; animation-delay:{i}s'>🌹</div>", unsafe_allow_html=True)
        autoplay_audio("love.mp3")
        if not st.session_state.story_done:

            type_text(
                "I know I'm not perfect 💭 "
                "And I know there were moments where I could have been better, calmer, more understanding. "
                "There were times I should have listened more, spoken softer, and shown my love more clearly. "
                "If I ever hurt you, even unknowingly, I'm truly sorry 🤍"
            )

            st.write("")
            type_text(
                "Sometimes I sit and think about everything… about us, about you, about how lucky I am to even have you in my life 💔 "
                "And I feel like I haven't always done enough to show how important you are to me. "
                "Maybe I didn’t always express my love in the ways you deserved. "
                "But please believe me, it was never because I didn't care 🌹 "
                "My heart has always been full of feelings for you, even when I didn't know the right words to say."
            )

            st.write("")
            type_text(
                "The way I look at you… I'm sure no one else sees you the way I do ✨ "
                "Your kindness isn't ordinary 💫 Your heart is rare 💖 "
                "The way you care for people, the way you worry about others before yourself, "
                "the way you stay strong even when you're tired — it’s something truly beautiful."
            )

            st.write("")
            type_text(
                "You have this quiet strength inside you that amazes me every time 🌸 "
                "Your smile feels like warmth on a cold day 🔥 "
                "Your presence feels like comfort when everything else feels heavy ☀️ "
                "Even your silence feels peaceful 🕊️"
            )

            st.write("")
            type_text(
                "You make my world softer, calmer, and brighter just by being in it 🌷 "
                "When my mind is messy, thoughts racing, feelings tangled — just thinking about you makes everything feel okay. "
                "You bring peace to my chaos without even trying."
            )

            st.write("")
            type_text(
                "And I truly hope… I do the same in your life too 🤞 "
                "I want to be your calm when things feel heavy 🌧️ "
                "I want to take your worries, your stress, your chaos, and stand beside you so you never feel alone 🤝 "
                "I want to be someone who adds happiness to your days, not weight to your heart."
            )

            st.write("")
            type_text(
                "I want to be someone you feel safe with. "
                "Someone you can talk to without fear. "
                "Someone who understands your silence and respects your feelings. "
                "Someone who supports your dreams, no matter how big they are."
            )

            st.write("")
            type_text(
                "I may not always be the best, but my feelings for you have always been real ❤️ "
                "Not temporary, not casual, not uncertain — but steady, warm, and sincere 💘 "
                "No matter what happens, my heart keeps choosing you. Every single day 🌅"
            )

            st.session_state.story_done = True

        else:
            st.markdown("""
            <div class='text'>
            I know I'm not perfect 💭 And I know there were moments where I could have been better, calmer, more understanding. There were times I should have listened more, spoken softer, and shown my love more clearly. If I ever hurt you, even unknowingly, I'm truly sorry 🤍<br><br>

            Sometimes I sit and think about everything… about us, about you, about how lucky I am to even have you in my life 💔 And I feel like I haven't always done enough to show how important you are to me. Maybe I didn’t always express my love in the ways you deserved. But please believe me, it was never because I didn't care 🌹 My heart has always been full of feelings for you, even when I didn't know the right words to say.<br><br>

            The way I look at you… I'm sure no one else sees you the way I do ✨ Your kindness isn't ordinary 💫 Your heart is rare 💖 The way you care for people, the way you worry about others before yourself, the way you stay strong even when you're tired — it’s something truly beautiful.<br><br>

            You have this quiet strength inside you that amazes me every time 🌸 Your smile feels like warmth on a cold day 🔥 Your presence feels like comfort when everything else feels heavy ☀️ Even your silence feels peaceful 🕊️<br><br>

            You make my world softer, calmer, and brighter just by being in it 🌷 When my mind is messy, thoughts racing, feelings tangled — just thinking about you makes everything feel okay. You bring peace to my chaos without even trying.<br><br>

            And I truly hope… I do the same in your life too 🤞 I want to be your calm when things feel heavy 🌧️ I want to take your worries, your stress, your chaos, and stand beside you so you never feel alone 🤝 I want to be someone who adds happiness to your days, not weight to your heart.<br><br>

            I want to be someone you feel safe with. Someone you can talk to without fear. Someone who understands your silence and respects your feelings. Someone who supports your dreams, no matter how big they are.<br><br>

            I may not always be the best, but my feelings for you have always been real ❤️ Not temporary, not casual, not uncertain — but steady, warm, and sincere 💘 No matter what happens, my heart keeps choosing you. Every single day 🌅
            </div>
            """, unsafe_allow_html=True)

            st.write("")

        if st.button("That's why... ❤️"):
            st.session_state.page = 3
            st.rerun()



# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:
    for i in range(15):
       st.markdown(f"<div class='rose' style='left:{i*8}%; animation-delay:{i}s'>❤️</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='big-title'>Would You Be My Valentine?💖</div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<div class='btn-center'>", unsafe_allow_html=True)
    if st.button("YES 😍", key="yes_btn"):
        # t=1
        st.session_state.yes_clicked = True
        st.balloons()
        type_text("You know what?🙃")
        type_text("I was hoping you'd say that!🙈")
        type_text("🥰 You just made me the happiest person alive ❤️")
        type_text("So, I want to say that....")
        type_text("👉🏻👈🏻")
        autoplay_audio("lov_Song.mp3")
        st.write("")

    # 💕 SHOW GIF
        st.image(
            "source.gif",   # put your gif file in project folder
            width=700

        )
        
    st.markdown("</div>", unsafe_allow_html=True)
        


    # NO BUTTON only if YES not clicked
    if not st.session_state.yes_clicked:
        import base64
        with open("sed_Song.mp3", "rb") as f:
            base64_audio_string = base64.b64encode(f.read()).decode()

        components.html(f"""
        <style>
        #noBtn {{
            position:fixed;
            background:linear-gradient(45deg,#ff6b81,#ff9a9e);
            color:white;
            border:none;
            border-radius:40px;
            padding:12px 32px;
            font-size:18px;
            cursor:pointer;
            transition: all 0.3s ease;
            z-index:9999;
        }}
        #msg {{
            position:fixed;
            bottom:300px;
            width:100%;
            text-align:center;
            font-size:18px;
            color:#c2185b;
            font-weight:bold;
        }}
        </style>

        <button id="noBtn">NO 😢</button>
        <div id="msg"></div>

        <audio id="sadSong" preload="auto">
            <source src="data:audio/mp3;base64,{base64_audio_string}" type="audio/mp3">
        </audio>

        <script>
        const btn = document.getElementById("noBtn");
        const msg = document.getElementById("msg");
        const song = document.getElementById("sadSong");

        let songStarted = false;

        const lines = [
            "Why are you trying to press NO 😭",
            "That hurts my heart 💔",
            "Please don’t do this to me 🥺",
            "I’ll keep running 😤",
            "YES is the better option 😌"
        ];

        function moveButton() {{
            const maxX = window.innerWidth - btn.offsetWidth;
            const maxY = window.innerHeight - btn.offsetHeight;

            btn.style.left = Math.random() * maxX + "px";
            btn.style.top = Math.random() * maxY + "px";
            btn.style.transform = "scale(0.75)";
            btn.style.opacity = "0.7";

            msg.innerText = lines[Math.floor(Math.random()*lines.length)];

            if (!songStarted) {{
                song.play().then(() => {{
                    songStarted = true;
                }}).catch(() => {{}});
            }}
        }}

        btn.addEventListener("mouseover", moveButton);
        btn.addEventListener("touchstart", e => {{ e.preventDefault(); moveButton(); }});
        btn.addEventListener("click", e => {{ e.preventDefault(); moveButton(); }});
        </script>
        """, height=400)
   


        


