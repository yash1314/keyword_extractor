import streamlit as st
from src.prediction_pipeline import keywords
from src.utils import utilities
import pandas as pd

keyword_extractor = keywords()
utilities = utilities()

st.title('*:rainbow[Word Extractor]*')
st.subheader("",divider='rainbow')
st.markdown("""#### This webapp can extract top 10 relevant keywords and perform Word analysis on the user input.""")


st.markdown('')
user_input = st.text_area('Enter you text here')

final_keywords = keyword_extractor.word_extractor(user_input)
results = [(key, value) for i in final_keywords for key, value in i.items()]
result = pd.DataFrame(results, columns = ['Words', 'Frequency'])
button = st.button('Process')

cols1, cols2, cols3 = st.columns([2.2,3,0.3], gap = 'large')

with cols1:
    if button:
        if user_input[:] == "":
            st.warning("Please enter a message.")
        else:
            st.markdown("### :green[Table] ###")
            st.dataframe(result)

with cols2:
    if button:
        if user_input[:] == "":
            pass
        else:
            st.markdown("### :green[Chart] ###")
            st.bar_chart(data = result, x = 'Words', y = 'Frequency', color='#A6B1F7', use_container_width=True)


with cols3:
    if button:
        if user_input[:] == "":
            pass
        else:
            st.markdown("### :green[Words] ###")
            st.markdown(f"#### {utilities.word_count(user_input)} ####")

            st.markdown("### :green[Sentences] ###")
            st.markdown(f"#### {utilities.sentence_count(user_input)} ####")

            st.markdown("### :green[Paragraphs] ###")
            st.markdown(f"#### {utilities.paragraph_count(user_input)} ####")




