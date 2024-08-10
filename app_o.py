import streamlit as st

# Page configuration
st.set_page_config(page_title="Front Page", layout="centered")

# CSS for background image and gradient
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://example.com/your-background-image.jpg');
        background-size: cover;
        background-position: center;
    }
    .header {
        text-align: center;
        padding: 50px;
        color: white;
    }
    .navbar {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    .navbar button {
        margin: 0 10px;
        padding: 10px 20px;
        font-size: 16px;
        color: white;
        background-color: #007bff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .navbar button:hover {
        background-color: #0056b3;
    }
    .button-container {
        text-align: center;
        margin-top: 200px;
    }
    .button-container button {
        margin: 0 10px;
        padding: 15px 30px;
        font-size: 18px;
        color: white;
        background-color: #28a745;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .button-container button:hover {
        background-color: #218838;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header">Welcome to Our App</h1>', unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <div class="navbar">
        <button onclick="window.location.href='/page1'">Page 1</button>
        <button onclick="window.location.href='/page2'">Page 2</button>
    </div>
""", unsafe_allow_html=True)

# Buttons in the middle
st.markdown("""
    <div class="button-container">
        <button onclick="window.location.href='/app'">Go to App</button>
        <button onclick="window.location.href='/page2'">Go to Page 2</button>
    </div>
""", unsafe_allow_html=True)

# Handling Streamlit routing
page = st.query_params.get('page', ['main'])[0]

if page == 'app':
    st.experimental_rerun()
elif page == 'page2':
    st.experimental_rerun()
