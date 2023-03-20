# import sys
# import os
#sys.path.insert(0, "/home/bence/code/FocusFactor/FocusFactor/")
import streamlit as st
import datetime
#import numpy as np
import pandas as pd
#mahar functions that are now in the master
#import aggredesstat as aads
from PIL import Image


# ######Have all your data in your raw data folder!!!!###########


st.set_page_config(
        layout="wide",
        page_title= "Topic Modelling",
        page_icon="📁")

#path with twitter data needed to use mahar's function
#path = "/home/bence/code/FocusFactor/FocusFactor/raw_data/wcup-tweets.csv"
#also for mahar's function
#interval = "1D"

tab1, tab2, tab3 = st.tabs(["Home", "Model", "Team"])
# headline in markdown logic
from streamlit import components
#mahar's function that transforms data into a daywise tweet-count and impact-sum
# depiction

# @st.cache  # 👈 Add the caching decorator
# def create_path_tuple():
#     return aads.create_path_tuple()

# @st.cache  # 👈 Add the caching decorator
# def upload_and_clean_data_2_topic():
#     return aads.upload_and_clean_data_2_topic(path_ls)

# @st.cache  # 👈 Add the caching decorator
# def count_tweet_intervalbased():
#     pa = aads.create_path_tuple()
#     dfa = aads.upload_and_clean_data_2_topic(pa)
#     return aads.count_tweet_intervalbased(dfa)



# path_ls = create_path_tuple()
# df_all = upload_and_clean_data_2_topic()
# df = count_tweet_intervalbased()
df = pd.read_csv("raw_data/FocusFactor-streamlit_test.csv")
df.index = df["Date"].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))
# path_ls = aads.create_path_tuple()
# df_all = aads.upload_and_clean_data_2_topic(path_ls)
# df = aads.count_tweet_intervalbased(df_all)
#df.Date = df.Date.date
# st.write(df.head())
# st.write(df.dtypes)
#t.write(df)
#column-based slider for date range and two radios for chart-type and
#content-selecter
with tab1:
    st.markdown("## Our findings regarding the impact of all tweets per day tweeted \
    on the war in Ukraine compared to those about the World Cup")
    col99, col98, col2, col3 = st.columns(4)
    with col99:
        d1 = st.date_input(
            "From when",
            datetime.datetime(2022, 10, 1))

    with col98:
        d2 = st.date_input(
            "To when",
            datetime.datetime(2023, 1, 31))
    
    # with col1:
    #     option = st.slider('Select a date range', 1, 31, (1, 31))
    with col2:
        chart_choice =  st.radio('Select a type the event to focus on',
                                 ('Ukraine','World Cup', 'Both'))
    #st.write(type(d1))
    # this is organizing the data from one selected date to the other
    # filtered_df = df[df.index > f"{d1} 00:00:00+00:00"][df.Date <= f"{d2} 00:00:00+00:00"]
    # filtered_df = df[df.Date > f"{d1}"][df.Date <= f"{d2}"]
    filtered_df = df[df.index >= pd.Timestamp(d1)]
    filtered_df = filtered_df[filtered_df.index <= pd.Timestamp(d2)]
    #st.write(filtered_df.head())
    #leave it here but delete it at the end if of no use
    #filtered_df = timeframe.iloc[:, 1:]
    #filtered_df = df.iloc[:, 1:].iloc[option[0]-1:option[1]+1]

    #selection of content
    with col3:
        rep_choice =  st.radio('Tweet count or impact score?',
                            ('Count', 'Score', "Both"))

    # this makes the ukr charts
    if chart_choice == 'Ukraine':
        if rep_choice == "Count":
            st.markdown(f" ### Daily tweet counts from {d1} to {d2}\
                regarding twitter discussions on the war in Ukraine")
            st.line_chart(filtered_df["UKR_Daily_Tweet_Count"])#,x="Date",y="Tweet_count")
        elif rep_choice == "Score":
            st.markdown(f"### Daily sum of the total impact score from  **{d1}** \
                to **{d2}** regarding twitter discussions on the war in Ukraine")
            st.line_chart(filtered_df["UKR_Daily_Relative_Impact_score"])
        else:
            st.markdown(f"### Daily total impact scores and tweet counts from {d1} \
                to {d2} regarding twitter discussions on the war in Ukraine")
            # this gets both impact sum and tweetcount next to each other
            col4, col5 = st.columns(2)
            col5.line_chart(filtered_df["UKR_Daily_Tweet_Count"])
            col4.line_chart(filtered_df["UKR_Daily_Relative_Impact_score"])

    #this ones gets the wc charts
    elif chart_choice == 'World Cup':
        if rep_choice == "Count":
            st.markdown(f" ### Daily tweet counts from {d1} to {d2} \
                regarding twitter discussions on the World Cup")
            st.line_chart(filtered_df["WC_Daily_Tweet_Count"])#,x="Date",y="Tweet_count")
        elif rep_choice == "Score":
            st.markdown(f"### Daily sum of the total impact score from  **{d1}** \
                to **{d2}** regarding twitter discussions on the World Cup")
            st.line_chart(filtered_df["WC_Daily_Relative_Impact_score"])
        else:
            st.markdown(f"### Daily total impact scores and tweet counts from {d1} \
                to {d2} regarding twitter discussions on the World Cup")
            # this gets both impact sum and tweetcount next to each other
            col4, col5 = st.columns(2)
            col5.line_chart(filtered_df["WC_Daily_Tweet_Count"])
            col4.line_chart(filtered_df["WC_Daily_Relative_Impact_score"])

    else:
        if rep_choice == "Count":
            st.markdown(f" ### Daily tweet counts from {d1} to {d2}")
            col77, col78 = st.columns(2)
            col77.line_chart(filtered_df["WC_Daily_Tweet_Count"])
            col78.line_chart(filtered_df["UKR_Daily_Tweet_Count"])
        elif rep_choice == "Score":
            st.markdown(f"### Daily sum of the total impact score from {d1} to {d2}")
            col79, col80 = st.columns(2)
            col79.line_chart(filtered_df["WC_Daily_Relative_Impact_score"])
            col80.line_chart(filtered_df["WC_Daily_Relative_Impact_score"])
        else:
            st.markdown(f"### Daily total impact scores and tweet counts from {d1} \
                to {d2}")
            col81, col82 = st.columns(2)
            # this gets both impact sum and tweetcount next to each other
            with col81:
                st.line_chart(filtered_df["WC_Daily_Tweet_Count"])
                st.line_chart(filtered_df["UKR_Daily_Tweet_Count"])
            with col82:
                st.line_chart(filtered_df["WC_Daily_Relative_Impact_score"])
                st.line_chart(filtered_df["UKR_Daily_Relative_Impact_score"])
            # col6, col7 = st.columns(2)
            # col6.bar_chart(filtered_df,x="Date", y="Tweet_count")
            # col7.bar_chart(filtered_df,x="Date", y="Sum_impact_score")

with tab2:
    #Here we will have Daiana's streamlit page


    st.markdown("# Our findings regarding the most talked about topics regarding the war in Ukraine")

    # Customization for sidebar
    st.markdown('<style>div[class="css-6qob1r e1fqkh3o3"] { background: url("https://media2.giphy.com/media/46hpy8xB3MiHfruixn/giphy.gif");background-repeat: no-repeat;background-size:350%;border:1px solid #36454F; border-top:none;} </style>', unsafe_allow_html=True)

    # Hiding the Footer
    hide_st_style =" <style>footer {visibility: hidden;}</style>"
    st.markdown(hide_st_style, unsafe_allow_html=True)

    ########### pyLDAvis Plot



    with open('raw_data/model_plot_cleaned_2.html', 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1300,  height=800, scrolling=False)

with tab3:

    st.title('Meet the Team')

    col33, col1, col2, col34 = st.columns(4)

    col33.markdown("")

    with col1:
        st.subheader("Antonella Navarro")
        #st.write(os.getcwd())
        image_antonella = Image.open('raw_data/Antonella.jpg')
        st.image(image_antonella, width=250)
        st.markdown('''

                    ''')
        st.subheader("Mahar Albaher Ali")
        image_mahar = Image.open('raw_data/Mahar.jpg')
        st.image(image_mahar, width=250)

    with col2:
        st.subheader("Daiana Rinja")
        image_daiana = Image.open('raw_data/Daiana.png')
        st.image(image_daiana, width=250)
        st.markdown('''

                    ''')
        st.subheader("Bence Tóth")
        image_bence = Image.open('raw_data/Bence.jpg')
        st.image(image_bence, width=250)

    col34.markdown("")
hide_st_style =" <style>footer {visibility: hidden;}</style>"
st.markdown(hide_st_style, unsafe_allow_html=True)

#this is left from bokeh-attempts
# df_interval = df
# df_interval['day_number'] = (df_interval['Date'] - df_interval['Date'].min()).dt.days +1
# idf = df_interval.interactive()
# # Define year slider
# day_slider = pn.widgets.IntSlider(name='Select Day', start=1,
#                                 end=df_interval.day_number.max(), step=1, value=df_interval.day_number.max(),
#                                 height=56)

# # Radio buttons for measuers/ impact score and tweet count
# tweet_axis = pn.widgets.RadioButtonGroup(
#             name='Y-axis',
#             options=['Tweet_count', 'Sum_impact_score'],
#             value='Tweet_count',
#             button_type='success')
# print(tweet_axis)

# tweet_pipeline = idf[(idf.day_number <= day_slider)][tweet_axis]

#     # #Defining the pipeline
# tweet_plot = tweet_pipeline.hvplot.bar(x='day_number', y=tweet_axis,
#                                 line_width=3, title='tweet count and impact score per day').opts(backend='bokeh')
# bokeh
#st.bokeh_chart(tweet_plot, use_container_width=True)
