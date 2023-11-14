import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Graph
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from streamlit_card import card
from streamlit_lottie import st_lottie

# Define lottie_research outside of functions
lottie_research = "https://lottie.host/41a217a7-063f-4abb-82e9-f7fa94a718fa/OERRpGG9d9.json"

# Default on_click function to remove any error
default_on_click = lambda: None

def generate_word_cloud(data):
    # Join all words in the data into a single string
    text = ' '.join(data)
    
    # Generate the word cloud with custom parameters
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',  # Set background color to white
        max_font_size=50,  # Adjust the maximum font size
        random_state=95,  # Set a fixed random state
    ).generate(text)
    
    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    
    # Display the Matplotlib figure using st.pyplot()
    st.pyplot(fig)

def projects_pub_page():
    st.title("Research Interest")

    data = [
        "Machine Learning",
        "Quantum Machine Learning",
        "Quasiprobability",
        "Artificial Intelligence",
        "Deep Learning",
        "Applied Statistics",
        "Data Mining",
        "Natural Language Processing",
        "Quantum Superposition",
        "Quantum Error Mitigation",
        "Bayesian Statistics",
        "Generative Quantum Machine Learning",
        "Machine Learning in Drug Discovery",
        "Time Series",
        "Machine Learning in Finance",
        "Computer Vision",
        "Bio-Statistics",
    ]

    # Display the word cloud and Lottie animation
    generate_word_cloud(data)

    st.title("Projects")

    def my_on_click():
        st.write("")

    # Create a 2x2 grid layout
    col1, col2 = st.columns(2)

    # Row 1
    with col1:
        # Project 1
        card(
            title="Arannya Bengali Browser",
            text="Speech Corpus enabled Bengali Web Browser",
            image="https://ct.kidgovernor.org/wp-content/uploads/2018/09/youtube-logo-hd-8-1024x768.png",
            url="https://www.youtube.com/watch?v=OCxz-BOBHQ8",
            on_click=default_on_click,  # Set default on_click function
        )

    with col2:
        # Project 2
        card(
            title="Computer Vision Based Street Width Measurement for Urban Aesthetics Identification",
            text="",
            image="https://ct.kidgovernor.org/wp-content/uploads/2018/09/youtube-logo-hd-8-1024x768.png",
            url="https://www.youtube.com/watch?v=Ds8k-aPHVKk",
            on_click=default_on_click,  # Set default on_click function
        )

    # Row 2
    with col1:
        # Project 3
        card(
            title="JustTune.AI",
            text="Text to Music Generator",
            image="https://scontent.fdac8-1.fna.fbcdn.net/v/t39.30808-6/391652127_3760221387597786_4925828799259193627_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_ohc=DctP4SGN_S4AX9Cb31d&_nc_ht=scontent.fdac8-1.fna&oh=00_AfCSHr4-9UCQfcD1iF2RNiAuFiLup0tO8B5edsj3-yTyiw&oe=65566D9E",
            url="https://youtu.be/Cqcx3R3xZxs?si=NY5wd5zdMt4pdRwx",
            on_click=default_on_click,  # Set default on-click function
        )

    with col2:
        # Project 4
        card(
            title="Github",
            text="ummerubaiyat",
            image="https://repository-images.githubusercontent.com/326435405/9affba00-777d-11eb-9c52-806cbc107892",
            url="https://github.com/ummerubaiyat",
            on_click=default_on_click,  # Set default on-click function
        )

    # Publications Section
    st.title("Publications")
    text_column, image_column = st.columns([3, 1])
    with text_column:
        tab1, tab2 = st.tabs(["1", "2"])
        with tab1:
            st.markdown(
                """
                <div class="stMarkdownContainer">
                    Chapter Title : Computer Vision-Based Street Width Measurement for Urban Aesthetics Identification
                    
                    ISBN : 9780367742515
                    
                    Abstract : This paper presents a computer-vision-based Street-Width measurement system 
                    for Urban Aesthetics identification. In this system, the image is captured using a digital 
                    camera. In the preprocessing section, the image is scaled in high to low resolution. The 
                    method used to identify the object is contour tracing and canny edge detection algorithm. 
                    Then the object is measured by generalizing the pixel mapping. Finally, the finding output 
                    is matched with the Standard Street Measurement. The measurement findings in this 
                    proposed methodology were then analyzed and based on some criteria the street aesthetics 
                    of Dhaka city was provided.
                    
                    Reference Link : [Book Link](https://www.routledge.com/.../Ari.../p/book/9780367742515?fbclid=IwAR0OG4UnZNPur9o3m-h36jUewGDhsKBLmdKBWDhcVaXmav9nJD8sKH-4j_4)
                    
                </div>
                """,
                unsafe_allow_html=True
            )

        with tab2:
            st.markdown(
                """
                <div class="stMarkdownContainer">
                    Student paper published at the 17th International Conference on Computer and Information Technology (ICCIT) 2014
                    
                    Title : Online Medication
                    
                    Abstract : Proper medication is a very common need of daily life. With the improvement of 
                    modern medical science, the maintenance cost of medication has also increased in the same 
                    way. For this, it is becoming a common problem for the citizens of undeveloped countries 
                    to maintain a balanced health care system. This paper highlights the basic need for an 
                    online medication system from the perspective of these undeveloped countries.
                    
                    Reference Link : [Conference Link](www.iccit.org.bd/2014/student-conference-iccit-2014)
                    
                </div>
                """,
                unsafe_allow_html=True
            )
    with image_column:
        # Add images or Lottie animations
        # st.image("image1.png", use_column_width=True)
        st_lottie(lottie_research, height=200, key="research")

    css = '''
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 2rem;
            font-family: Georgia, serif;
            text-align: justify;
        }
    </style>
    '''
    
    st.markdown(css, unsafe_allow_html=True)

# Call the function in your projects_pub_page to display the Research Interest word cloud, project cards, and publications
projects_pub_page()
