import streamlit as st
import pandas as pd

# st.title("RAG 챗봇 개발을 위한")

# st.header("streamlit")

# st.write("안녕하세요")

# st.image("samsung.png")

# st.link_button("삼성 홈페이지 링크","https://www.samsung.com/sec/")

# df = pd.read_csv("InkjetDB_preprocessing.csv")

# st.line_chart(df, x="Viscosity", y="Velocity")

# st.scatter_chart(df, x="Viscosity", y="Velocity")

# #데이터 프레임 가져오기​

# import pandas as pd

# # Read the dataset
# df = pd.read_csv("InkjetDB_preprocessing.csv")

# # Display the dataframe
# st.write(df)
##################################################################################################################
# 챗봇 가져오기
from openai import OpenAI
import streamlit as st

st.title("챗봇과 대화를 해보세요.")

openai_api_key = st.text_input("Enter your OpenAI API key")

client = OpenAI(api_key=openai_api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
    