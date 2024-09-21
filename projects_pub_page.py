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

    st.title("Notable Projects")

    def my_on_click():
        st.write("")

    # Create a 2x2 grid layout for project videos
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
        """
        <div class="project-description">
            <strong>Identifying Economically Backward Countries in accordance with the Multi-Dimensional Poverty Index using Unsupervised Machine Learning</strong><br>
            <em>Thesis Project, Department of Statistics and Data Science, Jahangirnagar University</em><br>
            <strong>Role:</strong> Lead Researcher<br>
            <strong>Duration:</strong> June 2022 – December 2022<br><br>
            The project aimed to classify countries by socio-economic and health indicators to uncover economic disparities. I started with <strong>K-Means clustering</strong> but noted significant overlap between clusters, leading to the integration of the <strong>Multidimensional Poverty Index (MPI)</strong> for enhanced analysis. To address multicollinearity, I performed <strong>Variance Inflation Factor (VIF)</strong> analysis and condition number checks, removing problematic variables to reduce numerical instability. The model was refined using <strong>Principal Component Analysis (PCA)</strong> and regularization techniques like <strong>Ridge</strong> and <strong>Lasso</strong> to retain key features and minimize redundancy. <strong>Weighted Least Squares (WLS)</strong> regression was applied to manage heteroscedasticity, while <strong>DBSCAN</strong> was used to handle outliers and preserve critical anomalies. <strong>Gaussian Mixture Models (GMM)</strong> validated clusters by identifying normally distributed subpopulations. The final analysis identified common countries across K-Means, DBSCAN, and GMM results, providing a robust basis for actionable, data-driven recommendations for fund allocation.
        </div>
        """,
        unsafe_allow_html=True
    )
        
    with col1:
        st.video("https://youtu.be/Cqcx3R3xZxs?si=NY5wd5zdMt4pdRwx")
        st.markdown(
        """
        <div class="project-description">
            <strong>JustTune.AI — AI-Driven Music Generation, Spectrogram Analysis, and MIDI Conversion</strong><br>
            <strong>Role:</strong> AI Engineer<br>
            <strong>Duration:</strong> October 2023<br><br>
            The <strong>JustTune.AI</strong> project merges cutting-edge AI and audio processing technologies to create music, analyze spectrograms, and convert audio to MIDI. Leveraging <strong>MusicGen (AudioCraft — Facebook)</strong>, I generated music from user text prompts, adjusting parameters like sampling temperature and CFG coefficients. The resulting audio was processed with <strong>librosa</strong> for spectrogram visualization, utilizing Short-Time Fourier Transform (STFT) for detailed frequency analysis. Pitch detection was executed using <strong>aubio</strong>, with notes mapped to MIDI events and managed via <strong>mido</strong>. This solution facilitates a smooth transition from music generation to MIDI export, ideal for real-time composition and sound engineering.<br><br>
            <strong>Tools & Techniques:</strong> MusicGen (AudioCraft — Facebook), librosa, aubio, mido, Python
        </div>
        """,
        unsafe_allow_html=True
    )
    with col1:
        st.markdown(
        """
        <div class="project-description">
            <strong>Sonar Bangla — Krishok Bondhu</strong><br>
            <strong>Role:</strong> Android Developer<br>
            <strong>Achievement:</strong> 2nd Runner-up, National Hackathon - 2016<br>
            <strong>Duration:</strong> 6 - 7 April, 2016<br><br>
            The <strong>Sonar Bangla — Krishok Bondhu</strong> project aimed to support Bangladeshi farmers by providing an Android mobile application that facilitates access to agricultural experts, market prices, and the latest updates on agricultural innovations. The app featured voice assistance for ease of use and conducted surveys based on data stored on a server. As part of the development team, I focused on image-based detection and classification of plant diseases, leveraging <strong>TensorFlow</strong> for its powerful machine learning capabilities, which were essential for analyzing plant diseases from live images. Additionally, I contributed to the development of user-friendly surveys, designing and preparing questionnaires to enable data collection and analysis, ultimately enhancing the app's capacity to support the agricultural community.<br><br>
            <strong>Tools & Techniques:</strong> Java, Retrofit, TensorFlow, OpenCV, SQLite
        </div>
        """,
        unsafe_allow_html=True
    )
   
    with col2:
        st.video("https://www.youtube.com/watch?v=Ds8k-aPHVKk")
        st.markdown(
        """
        <div class="project-description">
            <strong>Computer Vision-based Street-width Measurement for Urban Aesthetics Identification</strong><br>
            <em>Thesis Project, Department of Computer Science and Engineering, Daffodil International University</em><br>
            <strong>Role:</strong> Lead Researcher<br>
            <strong>November, 2017 – July, 2018</strong><br><br>
            This project aimed to accurately measure road widths from 2D images using advanced image processing techniques. I utilized <strong>OpenCV</strong> for image acquisition, capturing road images from various distances. Image preprocessing included downscaling for computational efficiency and grayscale filtering. <strong>Canny edge detection</strong> was employed to delineate object boundaries, while morphological operations like erosion and dilation closed gaps in edge lines. Pixel-to-object mapping was calibrated with a reference object to ensure precise width measurement.To classify road conditions, real data from Dhaka city was analyzed using <strong>Naive Bayes</strong>, categorizing road widths based on predefined thresholds. Despite challenges with calibration, camera angles, and manual capture, the project achieved a 96% accuracy rate. This low-cost solution for urban road analysis sets the stage for future advancements from 2D to 3D image analysis.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with col2:
        st.video("https://www.youtube.com/watch?v=OCxz-BOBHQ8")
        st.markdown(
        """
        <div class="project-description">
            <strong>Arannya Bengali Web Browser</strong><br>
            <em>Achievement: DIU Innovation Award - Daffodil ICT Carnival 2018</em><br>
            <strong>Role:</strong> Software Developer<br>
            <strong>Duration:</strong> August 2017 – February 2018<br><br>
            The <strong>Arannya Bengali Web Browser</strong> was designed to enhance web accessibility for low-literacy users in Bangladesh, enabling navigation through voice commands in Bengali. Developed initially in <strong>VB.NET</strong>, the project faced limitations with the WebBrowser Control’s outdated Internet Explorer rendering engine. To resolve this, I integrated the <strong>Chromium Browser Engine</strong>, ensuring full support for modern web standards like HTML5, CSS3, and JavaScript. For voice recognition, I utilized <strong>Microsoft SAPI</strong> to process Bengali commands. Addressing challenges with tone detection and native Bengali phonetics, I advanced the project by developing an acoustic language model with <strong>CMUSphinx</strong>, significantly improving the browser’s responsiveness to native Bengali speech patterns.<br><br>
            <strong>Tools & Techniques:</strong> VB.NET, Chromium Browser Engine, Microsoft SAPI, CMUSphinx
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
