import streamlit as st
import sqlite3
import os
from database import create_user, check_user, create_car, list_cars, search_cars, update_car, delete_car, create_tables

# Initialize the database
create_tables()

# Define the directory to save images
IMAGE_DIR = 'images/'

# Ensure the directory exists
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# Function to handle image upload and save it
def save_uploaded_image(uploaded_file):
    """Saves the uploaded image to the 'images' folder and returns the file path."""
    file_path = os.path.join(IMAGE_DIR, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    return file_path

# Streamlit page title
st.title("Car Management Application")

# User Authentication
def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login"):
        user = check_user(username)
        if user and user[2] == password:
            st.session_state.user_id = user[0]
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.session_state.page = "Car List"  # Set the page to "Car List"
            st.experimental_rerun()  # Automatically reload to show car list page
        else:
            st.error("Invalid credentials")
            st.session_state.username = ""
            st.session_state.password = ""

def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type="password", key="signup_password")
    
    if st.button("Sign Up"):
        if check_user(username):
            st.error("Username already exists!")
        else:
            create_user(username, password)
            st.success("User created successfully! Kindly login now.")
            st.session_state.username = ""
            st.session_state.password = ""
            
            # Show a button to redirect to the login page
            if st.button("Go to Login"):
                st.session_state.page = "Login"  # Redirect to the login page
                st.experimental_rerun()  # Automatically reload to show login page

# Page Logic
if 'user_id' not in st.session_state:
    # Show Login or Sign Up page based on user choice
    page = st.selectbox("Select Page", ["Login", "Sign Up"], key="auth_page")
    
    if page == "Login":
        login()
    elif page == "Sign Up":
        signup()
else:
    # If the user is logged in, show the main menu
    st.sidebar.subheader(f"Hello {st.session_state.username}")
    page = st.selectbox("Select Page", ["Car List", "Add Car", "Search Cars"])

    # Car List Page
    if page == "Car List":
        cars = list_cars(st.session_state.user_id)
        if cars:
            for car in cars:
                st.write(f"**{car[2]}**")  # Title
                st.write(car[3])  # Description
                st.write("Tags:", car[4])  # Tags
                st.image(car[5])  # Car Images
                
                # Only allow the user who added the car to delete it
                if car[1] == st.session_state.user_id:  # Check if user_id matches
                    if st.button(f"Delete {car[2]}", key=car[0]):
                        delete_car(car[0])  # Delete the car
                        st.success(f"Car '{car[2]}' deleted successfully!")
                        st.experimental_rerun()  # Refresh to update the list
                else:
                    st.write("You can only delete your own cars.")  # Message if not the owner

    # Add Car Page
    if page == "Add Car":
        st.subheader("Add New Car")
        title = st.text_input("Car Title")
        description = st.text_area("Car Description")
        tags = st.text_input("Tags (comma separated)")

        images = []  # List to store the image paths
        uploaded_images = 0  # Track the number of uploaded images

        # Upload the first image
        img = st.file_uploader("Upload Image 1", type=["jpg", "jpeg", "png"], key="img_1")
        if img:
            with st.spinner("Uploading image..."):
                img_path = save_uploaded_image(img)
                images.append(img_path)
                uploaded_images += 1

        # Allow adding more images
        add_more = st.button("Add More Pictures")
        if add_more:
            img = st.file_uploader("Upload Another Image", type=["jpg", "jpeg", "png"], key="img_2")
            if img:
                with st.spinner("Uploading image..."):
                    img_path = save_uploaded_image(img)
                    images.append(img_path)
                    uploaded_images += 1

        # Once images are uploaded, allow user to submit the car details
        if st.button("Add Car") and uploaded_images > 0:
            # Save car data
            create_car(st.session_state.user_id, title, description, tags, ", ".join(images))
            st.success("Car added successfully!")
            # Clear the input fields
            title = ""
            description = ""
            tags = ""
            images = []
            uploaded_images = 0
            st.experimental_rerun()  # Redirect to a fresh state, clearing the form

        elif uploaded_images == 0:
            st.error("Please upload at least one image!")

    # Search Cars Page
    if page == "Search Cars":
        keyword = st.text_input("Search by title, description, or tags")
        if keyword:
            cars = search_cars(st.session_state.user_id, keyword)
            if cars:
                for car in cars:
                    st.write(f"**{car[2]}**")  # Title
                    st.write(car[3])  # Description
                    st.write("Tags:", car[4])  # Tags
                    st.image(car[5])  # Car Images
            else:
                st.write("No cars found")
