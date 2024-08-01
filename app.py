import streamlit as st

st.title("Challenge Yourself")

challenges = ['FAP', 'No Productivity']
total_penalty = 0

challenge_penalties = [10,10]

new_challenge = st.text_input("Enter your new Challenge")
if new_challenge:
    penalty_value = st.number_input("Pick Your Penalty Points",5,20)

if st.button("Add New Challenge"):
    if new_challenge and penalty_value:    
        challenges.append(new_challenge)
        challenge_penalties.append(penalty_value)
    else:
        st.error("Enter Both Challenge and Penalty")


challenge , penalty = st.columns(2)

with challenge:
    for challenge_name in challenges:
        st.markdown(f"### {challenge_name}")


with penalty:
    index = 0
    for penalty in challenge_penalties:
        if st.button("Add penalty",key = f"Penalty{index}"):
            total_penalty += penalty
        index+=1

#st.write(challenge_penalties)
#st.write(challenges)