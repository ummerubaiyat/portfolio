import streamlit as st
from streamlit_sortables import sort_items

def social_act_page():
    st.title("Leadership Experience")

    data_leadership = [
        'Campus Ambassador (DIU),\n Google Developer Group Sonargaon\n (April 2, 2018 – Dec 30, 2018)',
        'Vice President,\n DIU Girls Programming Club\n (2017 – 2018)',
        'Campus Ambassador (DIU), \n BRAC (Urban Innovation Challenge 2016)',
        'Campus Ambassador (DIU), \n Take Back the Tech Bangladesh \n November 2, 2017, to Dec 30, 2018',
    ]

    # sorted_data_leadership = sort_items(data_leadership, "")
    
    # Display sorted items with custom styling
    for item in data_leadership:
        st.markdown(f'<div style="background-color: #DB9F92; padding: 10px; margin: 5px;">{item}</div>', unsafe_allow_html=True)

    st.title("Volunteer Experience")

    data_volunteer = [
        'Volunteer,\n ICCIT 2014\n',
        'Volunteer, \n BRAC (Urban Innovation Challenge 2016)',
        'Volunteer, \n Google Developer Group Sonargaon\n (2016-2019)',
        'Volunteer, \n Wi-STEM Bangladesh\n (2016-2017)',
        'Volunteer, \n WEDU Global\n (2017-2020)',
    ]

    # sorted_data_volunteer = sort_items(data_volunteer, "")
    
    # Display sorted items with custom styling
    for item in data_volunteer:
        st.markdown(f'<div style="background-color:#DB9F92; padding: 10px; margin: 5px;">{item}</div>', unsafe_allow_html=True)


    def image_gallery():
        st.title("Activities")

        # Image URLs
        image_urls = [
            "https://i.imgur.com/hbcMHOt.jpeg",
            "https://i.imgur.com/SupTGWZ.jpeg",
            "https://i.imgur.com/Mh5vrhi.jpeg",
            "https://i.imgur.com/cS2UoJf.jpeg",
            "https://i.imgur.com/pZJoHpN.jpeg",
            "https://i.imgur.com/IDPZTKe.jpeg",
            "https://i.imgur.com/PtNfpDU.jpeg",
            "https://i.imgur.com/0A9dNx3.jpeg",
            "https://i.imgur.com/r2Gy9W0.jpeg",
            "https://i.imgur.com/pUm7xLF.jpeg",
            "https://i.imgur.com/lz4VJzH.jpeg",
            "https://i.imgur.com/y8DcH5e.jpeg",
        ]

        # List of captions for each image
        captions = [
            "#KolpoKoushol #ai_music #nlp #recurrent_neural_network",
            "#huawei #hard_work #dedication #team_recognition",
            "#women_techmakers #google #public_speaking",
            "#national_hackathon_2016 #runner_up",
            "#solar_car #daffodil_international_university #solar_vehicle_competition",
            "#microsoft #ai #dl #cv #cnn #ml #guest_speaker #technical_trainning",
            "#microsoft #ai #ml #guest_speaker #public_speaking",
            "#diu_innovation_reward_2018 #nlp #speech_recognition #corpus",
            "#vice_president #cultural_club_diu #DIU Girls Computer Programming Club",
            "#national_hackathon_2016 #runner_up #prize_giving_ceremony",
            "#google #mcite_certified_developer",
            "#diu_innovation_reward_2018 #nlp #speech_recognition #corpus",
        ]

        # Calculate the number of rows and columns
        num_rows = 4
        num_columns = 3

        # Specify the width of each image
        image_width = 210

        # Specify the border style
        border_style = "2px solid #ddd"  # You can customize the border style

        # Iterate through the image URLs and display them in the grid
        for i in range(num_rows):
            # Create a row with separate columns for each image and caption
            row = st.columns(num_columns)
            for j in range(num_columns):
                index = i * num_columns + j
                if index < len(image_urls):
                    # Display image with Markdown caption
                    with row[j]:
                        st.image(image_urls[index], caption=f"**{captions[index]}**", width=image_width, output_format="auto")

    image_gallery()

# Call the social_act_page function to display the content
social_act_page()
