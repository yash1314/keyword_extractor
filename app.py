import streamlit as st
from src.prediction_pipeline import keywords
import pandas as pd

keyword_extractor = keywords()

st.title('***Words Extractor***')
st.markdown("-------------------")
st.markdown('###### This webapp can extract relevant keywords from the user input. For this purpose it uses the frequency of the words inside the corpus')


st.markdown('')
user_input = st.text_area('Enter you text here')

final_keywords = keyword_extractor.word_extractor(user_input)
results = [(key, value) for i in final_keywords for key, value in i.items()]
result = pd.DataFrame(results, columns = ['Words', 'Frequency'])
button = st.button('Process')

cols1, cols2 = st.columns(2)

with cols1:
    if button:
        if user_input[:] == "":
            st.warning("Please enter a message.")
        else:
            st.dataframe(result)

with cols2:
    if button:
        st.bar_chart(data = result, x = 'Words', y = 'Frequency', color='#00FFFF', use_container_width=True)





