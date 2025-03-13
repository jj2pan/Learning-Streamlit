import streamlit as st
import pandas as pd
import time

@st.dialog("User Details")
def user_details():
    username = st.text_input("Enter your username : ")
    email = st.text_input("Enter your email : ")

    if st.button("Login"):
        st.write(f"{username} logged in")

def main():
    st.title("This is a Title")
    st.header("This is a Header")
    st.subheader("This is a Subheader")
    st.write("Welcome to my streamlit application")
    st.caption("This is a Caption")

    st.code("""
    st.title("This is a Title")
    st.header("This is a Header")
    st.subheader("This is a Subheader")
    st.write("Welcome to my streamlit application")
    st.caption("This is a Caption")
    """)

    with st.echo():
        st.write("This code will be executed")
        st.write("This code will be executed")

    st.divider()
    # st.write("---")

    df = pd.read_csv("/Users/kiman/Documents/data.csv")
    st.dataframe(df)

    st.table(df.head())

    edited_df = st.data_editor(df)

    st.metric("Temperature in °C", 26, 2)
    st.metric("Rainfall in mm", 1400, -350)

    # submit_button = st.button("Submit")
    # if submit_button:
    #     st.write("The button was clicked")

    if st.button("Submit"):
        st.write("The button has been clicked!")

    like_dislike = st.feedback()
    if like_dislike == 0:
        st.write("You've disliked the content")
    else:
        st.write("You've liked the content")

    rating = st.feedback("stars")
    if rating or rating == 0:
        if rating < 3:
            st.write("Thank you for your feedback. We are working to improve.")
        elif rating == 3:
            st.write("We are glad you are enjoying our service.")
        elif rating == 4:
            st.write("Excellent! Thank you for choosing us.")

    st.toggle("Dark mode")

    terms = st.checkbox("I have read the terms and conditions.")
    if terms:
        st.write("The user has agreed to the above terms and conditions.")

    gender = st.radio("Select your gender", ["Male", "Female", "Other"])
    if gender == "Male":
        st.write("Hu!")
    elif gender == "Female":
        st.write("Haii!")

    team = st.selectbox("Select your favourite team: ", ["Liverpool", "Arsenal", "Nottingham", "Chelsea"])

    breakfast = st.multiselect("What did you have for breakfast?", ["Tea", "Bacon", "Eggs", "Milk", "Sweet potatoes", "Cassava", "Latte", "Sausages", "Croissant"])
    st.write(breakfast)

    st.select_slider("Sizes : ", ["XS", "S", "M", "L", "XL", "XXL", "XXXL"])

    st.number_input("Enter a number here : ", 0, 100)

    st.slider("Enter you age here : ", 18, 60, value=25)

    st.date_input("Enter the appointment date : ")

    st.time_input("Enter the time you want to schedule the appointment : ")

    first_name = st.text_input("Enter your first name : ")
    second_name = st.text_input("Enter your second name : ")

    st.write(f"Your name is {first_name} {second_name}")

    st.text_area("Write a 1000 word essay on social justice : ")

    st.file_uploader("Upload a file : ")

    # st.camera_input("Take your portrait : ")

    st.image("img/_DSC0055.JPG", width=250)

    cl1, cl2, cl3 = st.columns(3)
    with cl1:
        st.image("img/codecamp.png", width=200)
    with cl2:
        st.image("img/git.png", width=200)
    with cl3:
        st.image("img/dp.jpg", width=200)

    if st.button("Sign in"):
        user_details()

    with st.expander("Click to see more details : "):
        st.write("This is the first statement")
        st.write("This is the second statement")
        st.write("This is the third statement")
        st.write("This is the fourth statement")

    # with st.sidebar:
    #     st.write("This is in a sidebar")

    if st.button("Start"):
        with st.spinner("Loading content"):
            time.sleep(3)

        progress_text = "Processing..."
        bar = st.progress(0, text=progress_text)

        for i in range(100):
            time.sleep(0.05)
            bar.progress(i + 1, text=progress_text)

        time.sleep(2)
        bar.empty()
        st.write("Ready")

    if st.button("log in"):
        st.toast("User logging in", icon="👍")

    st.write("This is a joy emoji :joy: :joy: :joy:")

    if st.button("Balloons"):
        st.balloons()

    st.success("You have successfully logged in")
    st.info("Upload a .csv file")
    st.warning("The directory you are trying to save to does not exist")
    st.error("Failed to load image")

if __name__ == "__main__":
    main()