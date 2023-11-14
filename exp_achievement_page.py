import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Tree
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import random

def exp_achievement_page():
    # Define your achievements data
    achievements = [
        {"title": "Mentee @ SDG AI Lab Frontier Technologies Learning Collaborative", "start_date": "February 2023"},
        {"title": "Data Science Scholar @ Data Insight Career Program", "start_date": "August 2021"},
        {"title": "Data Science Scholar @ GreyCampus Career Program (Major on AI & ML)", "start_date": "March 2021"},
        {"title": "Learn IT, Girl (Best Project Award) 4th edition 2019", "start_date": "August 2019"},
        {"title": "Daffodil ICT Carnival 2018 (DIU Innovation Award)", "start_date": "December 2018"},
        {"title": "Fellow, Wi-STEM Bangladesh", "start_date": "September 2016"},
        {"title": "Rising Star, Facilitator WEDU", "start_date": "January 2017"},
        {"title": "National Hackathon 2016- 2nd Runner’s Up", "start_date": "October 2016"},
        {"title": "Electric Solar Vehicle Championship- Future Award 2014-2015", "start_date": "June 2014"},
    ]

    # Define custom markers for data points (replace 'A' with desired icons)
    markers = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

    # Convert date strings to datetime objects
    for achievement in achievements:
        achievement["start_date"] = datetime.strptime(achievement["start_date"], "%B %Y")

    # Generate random dates within the same month for each achievement
    for achievement in achievements:
        random_day = random.randint(1, 28)  # Random day in the month
        achievement["start_date"] = achievement["start_date"].replace(day=random_day)

    # Sort achievements by start date
    achievements.sort(key=lambda x: x["start_date"])

    # Extract dates and names from achievements data
    dates = [achievement["start_date"] for achievement in achievements]
    names = [achievement["title"] for achievement in achievements]

    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates) / 6)))[:len(dates)]

    # Create a larger figure and plot a stem plot with the date
    st.title("Achievement Timeline")
    
    fig, ax = plt.subplots(figsize=(10, 15))  # Increase the figure size

    gradient_fill = lambda x: 'gold' if x < 0 else 'yellow'
    colors = [gradient_fill(level) for level in levels]

    # The vertical stems
    ax.vlines(dates, 0, levels, color="tab:green")

    # Larger data points with gradient fill
    ax.scatter(dates, np.zeros_like(dates), c=colors, s=4000, marker="*", edgecolor='black')

    # Annotate lines with improved spacing and custom font size
    for d, l, r, m in zip(dates, levels, names, markers):
        va = "bottom" if l > 0 else "top"
        ax.annotate(r, xy=(d, l), xytext=(5, -15 if va == "bottom" else 10),
                    textcoords="offset points", horizontalalignment="left",
                    verticalalignment=va, fontsize=11, fontweight='bold')

    # Format x-axis with 36-month intervals
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=36))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

    # Remove y-axis and spines
    ax.yaxis.set_visible(False)
    ax.spines[["left", "top", "right"]].set_visible(False)

    # Set margins
    ax.margins(y=0.1)

    # Display the Matplotlib plot using Streamlit
    st.pyplot(fig)
    
    st.title("Job Experience Timeline")

    # Define your data for the Experience graph
    data = {
        "name": "Job Experience",
        "children": [
            {
                "name": "Huawei Technologies (Bangladesh) Ltd.",
                "children": [
                    {"name": "Solution Engineer", "children": [{"name": "Responsibilities", "children": []},
                                                               {"name": "Duration: December 2023 to Continuing", "collapse": True}]},
                    {"name": "Solution Architect (Cloud)", "children": [{"name": "Responsibilities", "children": [
                        {"name": "Cloud Solutions Design and Development "},
                        {"name": "Assessment Conduction of Customer Environments"},
                        {"name": "Mentoring Partner Representatives"}]},
                                                                       {"name": "Duration: March 2023 to August 2023", "collapse": True}]},
                ],
            },
            {
                "name": "Radisson Digital Technologies Limited.",
                "children": [
                    {"name": "Software Developer", "children": [{"name": "Responsibilities", "children": [
                        {"name": "Required Dependencies gathering and Resource Collection to design and develop Android Applications"},
                        {"name": "AI and data driven Mobile App Data model design and development (Category - Children and Financial)"},
                        {"name": "Survey questionnaires generation and analysis for 'Effect of Training on Employee Performance'"}]},
                                                               {"name": "Duration: August 2022 to February 2023", "collapse": True}]},
                ],
            },
            {
                "name": "InsideMaps Inc.",
                "children": [
                    {"name": "Quality Control Analyst", "children": [{"name": "Responsibilities", "children": [
                        {"name": "Data Quality Evaluation"},
                        {"name": "Record and Maintain Documentation"},
                        {"name": "Providing support to Data-Driven decisions"}]},
                                                                   {"name": "Duration: October 2021 to November 2021", "collapse": True}]},
                ],
            },
            {
                "name": "Monos Works International",
                "children": [
                    {"name": "AI Engineer", "children": [{"name": "Responsibilities", "children": [
                        {"name": "Research about AI enabled Anomaly Detection System and Prototype Development"},
                        {"name": "Face Recognition, Pose Estimation from live feeds"},
                        {"name": "Data Analysis during Preprocessing and improved prediction accuracy of model"}]},
                                                          {"name": "January 2019 to June 2020", "collapse": True}]},
                ],
            },
            {
                "name": "Multimedia Content & Communications (MCC)",
                "children": [
                    {"name": "Trainer (App Development)", "children": [{"name": "Responsibilities", "children": [
                        {"name": "Conduction of technical sessions on Object-Oriented Programming and Android app development"},
                        {"name": "Maintaining design principles and best practices for user-friendly system development"},
                        {"name": "Providing guidance and motivational support to mentees"}]},
                                                                      {"name": "Duration: May 2018 to November 2018", "collapse": True}]},
                ],
            },
        ],
    }

    # Create a Pyecharts tree chart for the Experience graph
    tree = Tree()
    tree.add(
        "job_experience",
        [data],
        symbol="emptyCircle",
        pos_top="1%",
        pos_left="5%",
        pos_bottom="1%",
        pos_right="15%",
        symbol_size=15,
        initial_tree_depth=3,  # Set the initial depth to 2 to only display the first children's data
    )
    tree.set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{b} {c}",  # Customize the tooltip to display the name and value
        ),
    )

    # Add some design customizations
    tree.set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            vertical_align="bottom",
            horizontal_align="bottom",
            font_size=10,
        ),
        itemstyle_opts=opts.ItemStyleOpts(
            color="#19AAF8",  # Customize node color
            border_color="blue",  # Customize border color
        ),
    )

    st_pyecharts = st.components.v1.html(tree.render_embed(), width=900, height=500)

# Run the page
exp_achievement_page()
