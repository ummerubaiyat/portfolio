import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

def education_skill_page():
    # Title for the Educational Background section
    st.title("Educational Background")

    # Create a DataFrame to hold educational data
    data_education = {
        'Institution': ["Daffodil International University", "Jahangirnagar University"],
        'Degree': ["B.Sc. in Computer Science and Engineering", "Masters in Applied Statistics & Data Science"],
        'Department': ["Computer Science and Engineering", "Applied Statistics & Data Science"],
        'Graduation Year': [2018, 2022],
        'CGPA': [3.62, 3.71]
    }

    df_education = pd.DataFrame(data_education)

    # Create a scatter plot for educational data
    scatter_education = go.Figure(data=[
        go.Scatter(
            x=df_education['CGPA'],
            y=df_education['Institution'],
            text=[
                f"Degree: {row['Degree']}<br>"
                f"Institution: {row['Institution']}<br>"
                f"Graduation Year: {row['Graduation Year']}<br>"
                f"CGPA: {row['CGPA']} / 4"
                for _, row in df_education.iterrows()
            ],
            mode='markers',
            marker=dict(
                color=df_education['Degree'].astype('category').cat.codes,
                showscale=True,
                colorscale='Viridis',
                colorbar=dict(
                    title='',  # Remove the colorbar title
                    tickvals=[],  # Remove all tick values from the colorbar
                ),
                size=35,
                opacity=0.9,
            ),
            hoverinfo='text',
            hovertemplate='%{text}',
        )
    ])

    # Layout settings for the educational scatter plot
    layout_education = go.Layout(
        xaxis=dict(title='CGPA (out of 4.0)'),
        yaxis=dict(title='Institution'),
    )

    # Add custom annotations for CGPA percentages and Degree names
    annotations_education = []

    for index, row in df_education.iterrows():
        annotations_education.append(dict(
            x=row['CGPA'],
            y=str(row['Institution']) + " (30px)",
            text=f"CGPA: {row['CGPA'] / 4 * 100:.2f}%<br>{row['Degree']}",
            showarrow=False,
            font=dict(size=11),
        ))

    layout_education['annotations'] = annotations_education
    scatter_education.update_layout(layout_education)

    # Display the educational chart
    st.plotly_chart(scatter_education)

    # Title for the Skills section
    st.title("My Skills")

    # Define skills and their respective scores (out of 10)
    skills = [
        "Python",
        "Statistical Analysis",
        "Deep Learning",
        "Machine Learning",
        "SQL",
        "R",
        "Cloud Computing",
        "Quantum Computing",
    ]

    skill_scores = [9, 9, 8, 8, 7, 6, 8, 2]  # You can adjust the scores accordingly

    # Create a radar chart for skills
    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=skill_scores,
        theta=skills,
        fill='toself',
        name='Skills',
    ))

    radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=False,
                range=[0, 10]  # Adjust the range as needed
            )
        ),
        showlegend=False,
    )

    # Increase the font size of radar chart annotations
    radar.update_layout(
        annotations=[
            dict(
                x=0.5,
                y=0.5,
                xref='paper',
                yref='paper',
                text='Skills',
                showarrow=False,
                font=dict(size=16)  # Adjust the font size as needed
            )
        ]
    )

    # Display the skills radar chart
    st.write(radar)

    # Title for the Featured Courses section
    st.title("Featured Courses")

    # Define course data for the Treemap
    course_data = {
        'Course Category': ["Data Science", "Data Science", "Data Science", "Data Science", "Programming", "AI", "AI",
                            "Data Science", "Leadership", "Business", "Business"],
        'Course Name': ["Data Science (Specialization)", "Data Mining (Specialization)",
                        "Data Analysis and Interpretation (Specialization)",
                        "Data Science: Statistics and Machine Learning (Specialization)",
                        "Python 3 Programming (Specialization)", "Deep Learning (Specialization)",
                        "Machine Learning (Specialization)", "Data Science Professional",
                        "WEDU Global - Leadership Program", "Basic of Social Business", "Business Communication"],
        'Provider': ["Johns Hopkins University", "University of Illinois at Urbana-Champaign", "Wesleyan University",
                     "Johns Hopkins University", "University of Michigan", "DeepLearning.AI", "University of Washington",
                     "Odin School", "WEDU Global", "Global Access Asia", "Global Access Asia"],
        'Platform': ["Coursera", "Coursera", "Coursera", "Coursera", "Coursera", "Coursera", "Coursera",
                     "Odin School (Online)", "WEDU Global (Online)", "Global Access Asia (Online)", "Global Access Asia (Online)"],
        'Credential URL': [
            "https://www.coursera.org/account/accomplishments/specialization/89JEM8LK9Y6V?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://www.coursera.org/account/accomplishments/specialization/BQAJMQRNY7PB?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://www.coursera.org/account/accomplishments/specialization/UNMYW8HX5Q39?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://www.coursera.org/account/accomplishments/specialization/N54CG2P3DDK5?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://www.coursera.org/account/accomplishments/specialization/55BUEDDL4PK3?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://www.coursera.org/account/accomplishments/specialization/XY5RU7QF9FP5?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://www.coursera.org/account/accomplishments/specialization/8C9R8X27DY9E?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n",
            "https://learn.odinschool.com/verify-certificate?serialno=CT3KN5AW", "", "", ""]
    }

    df_courses = pd.DataFrame(course_data)

    # Create an interactive Treemap
    df_courses['Label'] = df_courses['Course Name'] + '<br>' + df_courses['Provider'] + '<br>' + df_courses['Platform']

    fig = px.treemap(df_courses, path=['Course Category', 'Label'],
                     values=[1] * len(df_courses),
                     color_discrete_sequence=['#BED3D4', '#E8CAA4', '#A1B872', '#E5D67B', '#DCC1B0'],
                     hover_data=df_courses[["Platform", "Credential URL"]])

    fig.update_layout(
        width=950,
        height=750,
    )

    # Customize hover template
    hover_template = "<b>Course:</b> %{label}<br><b>Platform:</b> %{customdata[0]}<br><b>Credential URL:</b> <a href='%{customdata[1]}' target='_blank'>Link</a>"
    fig.update_traces(hovertemplate=hover_template)

    # Display the Treemap chart
    st.plotly_chart(fig)

# Call the function to display the page
education_skill_page()
