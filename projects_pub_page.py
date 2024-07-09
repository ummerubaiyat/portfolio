import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Graph
from wordcloud import WordCloud
import matplotlib.pyplot as plt
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

    # Create a 2x2 grid layout for project videos
    col1, col2 = st.columns(2)

    with col1:
        st.video("https://www.youtube.com/watch?v=OCxz-BOBHQ8")
        st.markdown(
            """
            <div class="project-description">
            **Arannya Bengali Browser**  
            A speech corpus-enabled Bengali web browser designed to enhance accessibility and user experience for Bengali speakers. Features include voice commands and a unique user interface tailored to the Bengali language.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.video("https://www.youtube.com/watch?v=Ds8k-aPHVKk")
        st.markdown(
            """
            <div class="project-description">
            **Computer Vision-Based Street Width Measurement for Urban Aesthetics Identification**  
            It is a system that utilizes computer vision techniques to measure street width as a metric for urban aesthetics. The methodology involved capturing images with a digital camera, preprocessing through scaling resolution, object identification via contour tracing and canny edge detection algorithms, and pixel mapping generalization for measurement. The results were compared with standard street measurements to analyze the aesthetics of Dhaka city streets.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col1:
        st.video("https://youtu.be/Cqcx3R3xZxs?si=NY5wd5zdMt4pdRwx")
        st.markdown(
            """
            <div class="project-description">
            **JustTune.AI**  
            A text-to-music generator that converts written text into musical compositions. This project leverages natural language processing and deep learning to create personalized music based on user inputs.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("https://repository-images.githubusercontent.com/326435405/9affba00-777d-11eb-9c52-806cbc107892", use_column_width=True)
        st.markdown(
            """
            <div class="project-description">
            **Github**  
            [ummerubaiyat's GitHub profile](https://github.com/ummerubaiyat)
            </div>
            """,
            unsafe_allow_html=True
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
        .stMarkdownContainer {
            margin: 20px 0;
        }
        .project-description {
            margin: 20px 0;
            padding: 20px;
            border: 1px solid var(--primary-color);
            border-radius: 8px;
            background-color: var(--background-color);
            color: var(--text-color);
            font-size: 1.1rem;
            text-align: justify;
        }
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 2rem;
            font-family: Georgia, serif;
            text-align: justify;
        }
        :root {
            --primary-color: #ddd;
            --background-color: #f9f9f9;
            --text-color: #000;
        }
        @media (prefers-color-scheme: dark) {
            :root {
                --primary-color: #444;
                --background-color: #333;
                --text-color: #fff;
            }
        }
    </style>
    '''
    
    st.markdown(css, unsafe_allow_html=True)

# Call the function in your projects_pub_page to display the Research Interest word cloud, project videos, and publications
projects_pub_page()
