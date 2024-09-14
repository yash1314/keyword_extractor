import streamlit as st
from streamlit_extras.bottom_container import bottom
from src.prediction_pipeline import keywords
from src.utils import utilities
import pandas as pd

keyword_extractor = keywords()
utilities = utilities()

st.set_page_config(layout='wide')
st.markdown('<style>div.block-container{padding-top:1.3rem;}</style>', unsafe_allow_html=True)
st.title('*:rainbow[Word Extractor]*')
st.markdown("""**This webapp can extract top 10 relevant keywords and perform Word analysis on the user input.**""")
st.markdown("----------------------------------------------------------")


with bottom():
    co1, co2 = st.columns([0.7, 0.1])
    
    with co1:
        user_input = st.text_input('**Enter you text here**')
    with co2:
        button = st.button('Enter Text to Analyze', use_container_width=True)


final_keywords = keyword_extractor.word_extractor(user_input)
results = [(key, value) for i in final_keywords for key, value in i.items()]
result = pd.DataFrame(results, columns = ['Words', 'Frequency'])

cols1, cols2, cols3 = st.columns([2.4,1.8,3.2], gap = 'medium')

with cols1:
    if button:
        if user_input[:] == "":
            st.warning("Please enter a message.")
        else:
            st.markdown("### :green[Table :] ###")
            st.dataframe(result)

with cols3:
    if button:
        if user_input[:] == "":
            pass
        else:
            st.markdown("### :green[Chart :] ###")
            st.bar_chart(data = result, x = 'Words', y = 'Frequency', color='#A6B1F7', use_container_width=True)


with cols2:
    if button:
        if user_input[:] == "":
            pass
        else:
            st.markdown("### :green[Words :] ###")
            st.markdown(f"#### {utilities.word_count(user_input)} ####")

            st.markdown("### :green[Sentences :] ###")
            st.markdown(f"#### {utilities.sentence_count(user_input)} ####")

            st.markdown("### :green[Paragraphs :] ###")
            st.markdown(f"#### {utilities.paragraph_count(user_input)} ####")