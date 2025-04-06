import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests 


#image = Image.open ("IMG_7251.jpeg")
#st.image(image, caption="my portfolio", use_column_width=True)

st.set_page_config(
              page_title = "Oluwaseun Emmanuel Web App Portfolio",
              layout = "wide",
             initial_sidebar_state = "expanded"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_code = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tfb3estd.json")

col1, col2 = st.columns([3,1])
with col1:
    st.write("##")
    st.subheader("Welcome to my app!")
    st.markdown("Data analysis is both art and science, Oluwaseun Emmanuel is a computer science graduate with a passion for doing data analysis and visualization.")
    st.write("[Read more](https://github.com/SeunBoyy)")

if lottie_code:
    with col2:
        st_lottie(lottie_code, height=300, width=300, key="lottie_animation")

#with col2:
    #st.header("Image")
    #st.image(image, use_column_width=True)

st.write('----')


selected = option_menu(
    menu_title="Main Menu",  # Title for the menu
    options=["About Me", "Projects", "Contact Me"],  # List of options in the menu
    icons=["house", "book", "envelope"],  # Icons for each option (can be left empty)
    orientation="horizontal"  # Menu orientation (can be "horizontal" or "vertical")
)


if selected == "About Me":
        st.title("About Me")
        st.write("Welcome to the About Me section!")
        st.markdown("""
        Oluwaseun Emmanuel is a computer science graduate with a passion for data analysis and visualization.
        Data analysis is both an art and a science, and I enjoy exploring insights from data.
 """) 

elif selected == "Projects":
    st.title("Projects")
    st.write("Here are some of my projects:")
    st.markdown("""
        - **Project 1**: Data visualization dashboard for sales analysis.
        - **Project 2**: leveraging sql queries  to uncover patterns, identify key metrics by enhancing business operations.
        - **project 3**: Data loading and inspection, handling inconsistent values doing EDA with Excel.
""")
    
elif selected == "Contact Me":
    st.title("Contact Me")
    st.write("Feel free to reach out to me!")
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("send")
        if submit_button:
         st.success("Message sent!")

    st.markdown("""
        - **Email**: seunemmanuel03@gmail.com
        - **LinkedIn**: [Oluwaseun Emmanuel](https://linkedin.com/in/example)
        - **GitHub**: [SeunBoyy](https://github.com/SeunBoyy)
    """)

    st.markdown("""
        <style>
        .contact-container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .contact-form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .contact-form button[type="submit"] {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .contact-form button[type="submit"]:hover {
            background-color: #3e8e41;
        }
        </style>
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.write("Thank you for visiting my portfolio!")