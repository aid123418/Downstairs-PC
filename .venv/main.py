import streamlit as st

st.title("Welcome to my favorite roblox games:")
st.write("These are my favorite ROBLOX games, link and short description will be provided!")

col1, col2 = st.columns(2)


with col1:
    st.image("images/image.png")
    st.info("SCP roleplay is basically a scuffed roleplay game from the SCP universe. its combat system is pretty clean and nice. The teams require lots of EXP to max, and about 1 minute = 1 exp (like 1200 exp to max security)")
    st.link_button(url="https://www.roblox.com/games/5041144419/SCP-Roleplay", label="SCP Roleplay link")

    st.image("images/Deathball.png")
    st.info("Death Ball is a very good game, you may play blade ball but i think this will impress you. It has many champions, each with 4 abilities that help you in some way. Just like blade ball, there is an highly dangerous ball randmly speedng towards people, get hit and you loose one of your three given lives. Find out more by playing!")
    st.link_button(url="https://www.roblox.com/games/15002061926/Death-Ball-UPD", label="Death Ball link")






with col2:
    st.image("images/Beeswarm.png")
    st.info('Bee swarm simulator is just built different... Litteraly. Bee swarm, or "bee game" is not pay to win like other games. It has a nice progression system and rewarding sounds. You should try bee game NOW! ')
    st.link_button(url="https://www.roblox.com/games/1537690962/Bee-Swarm-Simulator", label="Bee Swarm Simulator link")

    st.image("images/Asylumroleplay.png")
    st.info("Asylum roleplay is a small game with a small comunity. However, it is a great game that is entertaining with its many teams. Some teams are paid, but it does not stop it being great. Try it and see!")
    st.link_button(url="https://www.roblox.com/games/4805760032/Asylum-Roleplay", label="Asylum Roleplay link")