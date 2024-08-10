import streamlit as st
import pandas as pd
import base64

# Function to read and process the Excel file
@st.cache_data
def load_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    courses = {}
    
    for _, row in df.iterrows():
        course = row['Course Name']
        subject = row['Subject Name']
        chapter = row['Chapter Number']
        pdf_name = row['PDF Name']
        pdf_link = row['PDF Link']
        
        if course not in courses:
            courses[course] = {}
        if subject not in courses[course]:
            courses[course][subject] = []
        
        # Find if the chapter already exists
        chapter_entry = next((item for item in courses[course][subject] if item['title'] == chapter), None)
        if chapter_entry:
            chapter_entry['pdf_links'].append({'name': pdf_name, 'url': pdf_link})
        else:
            courses[course][subject].append({
                'title': chapter,
                'pdf_links': [{'name': pdf_name, 'url': pdf_link}]
            })
    
    return courses

# Function to set background image with gradient overlay
def set_background_image_with_gradient(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                position: relative;
                overflow: hidden;
                height: 100vh;
                background-image: url("data:image/jpeg;base64,{encoded_string}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            .stApp::before {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8); /* Adjust the color and opacity for gradient effect */
                pointer-events: none; /* Allow clicks to pass through */
            }}
            .main-container {{
                position: relative;
                padding: 20px;
                border-radius: 10px;
            }}
            .navbar {{
                display: flex;
                align-items: center;
                background-color: rgba(40, 100, 100, 0.7);
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                position: absolute;
                width: 100%;
                top: 0;
                left: 0;
                z-index: 2; /* Ensure navbar is on top */
            }}
            .navbar img {{
                height: 40px; /* Adjust height for logo size */
                margin-right: 20px;
            }}
            .navbar a {{
                color: white;
                text-decoration: none;
                padding: 0 15px;
                font-size: 16px;
            }}
            .navbar a:hover {{
                text-decoration: underline;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"Image file not found: {image_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app
def main():
    # Set the background image with gradient overlay
    image_path = "public/images/lpu_image.jpeg"  # Adjust relative path as needed
    set_background_image_with_gradient(image_path)

    st.header("Welcome to Lovely Professional University")
    st.title("Course Selection")

    # Specify the local path to your Excel file
    excel_file_path = "Book1.xlsx"  # Adjust this path as needed

    # Load data from the Excel file
    courses = load_data_from_excel(excel_file_path)

    # Add navigation bar with logo and links
    logo_path = "public/images/logo.png"  # Adjust relative path as needed
    st.markdown(f"""
        <div class="navbar">
            <img src="data:image/png;base64,{base64.b64encode(open(logo_path, "rb").read()).decode()}" alt="Logo">
            <div>
                <a href="#">Home</a>
                <a href="#">Who We Are</a>
                <a href="#">Contact Us</a>
                <a href="#">Explore More</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Create a container for the main content to overlay on the background
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)

        # Sidebar for course selection
        course_name = st.sidebar.selectbox("Select a Course", list(courses.keys()))

        # Display selected course subjects
        if course_name:
            st.sidebar.subheader("Subjects")
            subjects = courses[course_name]
            subject_name = st.sidebar.selectbox("Select a Subject", list(subjects.keys()))
            
            # Display topics under the selected subject
            if subject_name:
                st.subheader(f"Topics in {subject_name}")
                topics = subjects[subject_name]
                for topic in topics:
                    with st.expander(topic["title"]):
                        for pdf in topic["pdf_links"]:
                            st.markdown(f"[{pdf['name']}]({pdf['url']})")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
