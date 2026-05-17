import streamlit as st
import os
# from dotenv import load_dotenv

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="EcoHarvest AI Login",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- LOAD ENVIRONMENT VARIABLES ---
# It's good practice to load environment variables at the start.
# load_dotenv()

# --- AUTHENTICATION LOGIC ---
def check_password():
    """Returns `True` if the user has entered the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        # Hardcoded credentials for this example
        # In a real-world scenario, use st.secrets or a secure authentication service
        if st.session_state["username"] in ["admin"] and st.session_state["password"] in ["12345"]:
            st.session_state["authenticated"] = True
            del st.session_state["password"]  # clear password from memory
            del st.session_state["username"]
        else:
            st.session_state["authenticated"] = False

    # Initialize session state for authentication if it doesn't exist
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # Show login form if not authenticated
    if not st.session_state["authenticated"]:
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        if st.button("Login"):
            password_entered()
            # Rerun to update the page state after login attempt
            st.rerun()
    
    # Return authentication status
    return st.session_state["authenticated"]

# --- MAIN APP LOGIC ---
def main():
    """Main function to run the Streamlit app."""
    
    st.title("Welcome to EcoHarvest AI 🌾")
    st.write("---")

    if check_password():
        # --- SIDEBAR ---
        with st.sidebar:
            st.title("EcoHarvest AI")
            # st.image("./assets/logo.png", width=150) # Optional: Add a logo image in an assets folder
            st.write("Your AI-powered agricultural assistant.")
            st.write("---")

            if st.button("Logout"):
                st.session_state["authenticated"] = False
                st.rerun()

        # --- HOME PAGE CONTENT ---
        st.header("🏠 Home")
        st.write("You are successfully logged in.")
        st.info("Please select a feature from the sidebar to begin.")
        
        st.subheader("About EcoHarvest AI")
        st.markdown("""
        **EcoHarvest AI** is a comprehensive tool designed to empower farmers with data-driven insights. 
        Leveraging state-of-the-art AI, this application provides tailored recommendations to enhance agricultural productivity and sustainability.

        **Features:**
        - **🌿 Crop Recommendation:** Get suggestions for the best crops to plant based on your location's real-time weather and seasonal data.
        - **💰 Cost & Yield Optimization:** Receive actionable strategies to reduce farming costs and maximize your harvest.
        - **🐞 Pest & Disease Detection:** Upload an image or describe symptoms to identify potential threats and get effective treatment plans.

        Navigate to the desired page using the links in the sidebar.
        """)
    else:
        st.warning("Please enter your username and password to proceed.")
        st.stop()


if __name__ == "__main__":
    main()