import streamlit as st
from PIL import Image, ImageDraw
import io
from streamlit_lottie import st_lottie
import requests
from education_skill_page import education_skill_page
from exp_achievement_page import exp_achievement_page
from projects_pub_page import projects_pub_page
from social_act_page import social_act_page
from st_clickable_images import clickable_images

# Function to create a circular image
def create_circular_image(image_path, size):
    """
    Create a circular image from the provided image path.

    Parameters:
    - image_path (str): Path to the image file.
    - size (int): Size of the circular image.

    Returns:
    - io.BytesIO: Circular image data as bytes.
    """
    image = Image.open(image_path)
    size = min(image.size)
    image = image.crop((0, 0, size, size))
    circular_mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(circular_mask).ellipse((0, 0, size, size), fill=255)
    circular_image = Image.new("RGBA", (size, size))
    circular_image.paste(image, mask=circular_mask)
    circular_image_bytes = io.BytesIO()
    circular_image.save(circular_image_bytes, format="PNG")
    return circular_image_bytes

# Page content for the Home tab
def home_page():
    # Center-align the content with custom CSS
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .pro-text {
            font-size: 18px;
            font-weight: normal;
            text-align: justify;
            line-height: 1.6;
        }

        .pro-text .first-letter {
            font-size: 48px;
            font-weight: bold;
            float: left;
            margin-right: 10px;
            margin-top: 3px;
            line-height: 0.8;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Set the background color to white
    st.markdown(
        """
        <style>
        body {
            background-color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create a layout with one row
    row1 = st.columns(2)

    # Row 1, Column 1
    with row1[0]:
        # Add the name with a large fantasy font
        st.header("Umme Rubaiyat Chowdhury")
        # Add your position with a briefcase emoji
        st.markdown(":briefcase:  Solution Engineer")
        # Add the company with a company emoji
        st.markdown(":office:  Huawei Technologies (Bangladesh) Ltd. ")
        # Add your email with an email emoji
        st.markdown(":email: Email:  rubaiyat4305 [at] diu [dot] edu [dot] bd ")

    # Row 1, Column 2
    with row1[1]:
        image_size = 200  # Adjust the size as needed
        # Load the image using PIL
        image_url = "https://i.imgur.com/4Wv0P4y.jpg"
        image = Image.open(requests.get(image_url, stream=True).raw)

        # Ensure the image is square
        size = min(image.size)
        image = image.crop((0, 0, size, size))

        # Create a circular mask
        circular_mask = Image.new("L", (size, size), 0)
        ImageDraw.Draw(circular_mask).ellipse((0, 0, size, size), fill=255)

        # Apply the circular mask to the image
        circular_image = Image.new("RGBA", (size, size))
        circular_image.paste(image, mask=circular_mask)

        # Convert the circular image to bytes with a transparent background
        circular_image_bytes = io.BytesIO()
        circular_image.save(circular_image_bytes, format="PNG")

        # Display the circular image with the fixed size
        st.image(circular_image_bytes, width=image_size)

    # Create a layout with one row for the second row
    row2 = st.columns((3, 1))  # Specify the width ratios here (3 for three-thirds, 1 for one-third)

    # Row 2, Column 1 (Three-thirds of the row)
    with row2[0]:
        # Add the text in the left column
        st.markdown(
            """
            <p class='pro-text'>
                <span class='first-letter'>A</span> proactive AI enthusiast, equipped with precise skills in Data Analytics, Cloud Architecture, and Deep Learning. With a fervent dedication to harnessing the power of data for innovative solutions, I am unwavering in my commitment to pushing the boundaries of what's achievable in the dynamic realm of data science. My approach is underpinned by a collaborative and innovative mindset, making interdisciplinary collaboration a cornerstone of my work. I firmly believe that data science's true potential lies in its capacity to bridge domains and ignite positive transformation. Committed to ongoing learning and staying abreast of the latest advancements in data science and AI, my aim is to apply my expertise and enthusiasm to projects that generate a substantial impact on society. My excitement extends to the prospect of engaging with like-minded professionals who share a vision for data-driven innovation and forging new paths in the field of data science.
            </p>
            """,
            unsafe_allow_html=True,
        )

    # Row 2, Column 2 (One-third of the row)
    with row2[1]:
        # Add the Lottie image in the right column
        st.markdown(
            """
            <div style="padding: 20px;">
            <style>
                .lottie-container {
                    display: flex;
                    justify-content: center;
                }
            </style>
            <div class="lottie-container">
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_about_me = load_lottieurl(
            "https://lottie.host/17c58954-51ce-4202-a777-b1a8f82b0f33/5FAM4KpSJX.json"
        )

        st_lottie(lottie_about_me, speed=1, width=210, height=210)

    st.title("Highlights")

    clicked = clickable_images(
        [
            "https://i.imgur.com/IDPZTKe.jpeg?w=700",
            "https://i.imgur.com/lz4VJzH.jpeg?w=700",
            "https://i.imgur.com/r2Gy9W0.jpeg?w=700",
            "https://i.imgur.com/j2FSdJx.jpeg?w=700",
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "5px", "height": "200px"},
    )


# Create a sidebar navigation
with st.sidebar:
    st.markdown("## Navigation")

    # Define the navigation items with icons
    navigation_items = {
        "Home": "🏠",
        "Education and Skills": "📚",
        "Experience and Achievements": "🏆",
        "Projects and Publications": "🚀",
        "Activities": "🎉",
    }

    # Get the selected page
    page = st.selectbox("", list(navigation_items.keys()))

    # Apply CSS styles for the navigation items
    st.markdown(
        """
        <style>
        .sidebar-content {
            padding: 10px;
            background-color: #262730;
            border-radius: 8px;
        }
        .nav-item {
            padding: 10px;
            margin: 5px 0;
            background: #1E2126;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .nav-item:hover {
            background: #43454D;
        }
        .nav-icon {
            margin-right: 10px;
            color: #ffffff;
        }
        .selectbox {
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display the navigation items
    for item, icon in navigation_items.items():
        if page == item:
            background_color = "#43454D"  # Highlight the selected page
        else:
            background_color = "#1E2126"

        # Create a clickable navigation item
        # clicked = st.button(
        #     f'<div class="nav-item" style="background: {background_color};"><div class="nav-icon">{icon}</div>{item}</div>',
        #     key=item,
        # )
        # if clicked:
        #     page = item  # Update the selected page


# Load and display the selected page
if page == "Home":
    home_page()
elif page == "Education and Skills":
    education_skill_page()
elif page == "Experience and Achievements":
    exp_achievement_page()
elif page == "Projects and Publications":
    projects_pub_page()
else:
    social_act_page()
