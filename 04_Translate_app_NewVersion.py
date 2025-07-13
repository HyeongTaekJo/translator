##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키지 추가
import openai
# Deepl 번역 패키지 추가
import deepl


##### 기능 구현 함수 #####
# ChatGPT 번역
def gpt_translate(messages, apikey):
    client = openai.OpenAI(api_key=apikey)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a translator that translates English into Korean."},
            {"role": "user", "content": messages}
        ]
    )

    return response.choices[0].message.content

# 디플 번역
def deepl_translate(text, deeplAPI):
    translator = deepl.Translator(deeplAPI)
    result = translator.translate_text(text, target_lang="KO")
    return result.text

##### 메인 함수 #####
def main():
    # 기본 설정
    st.set_page_config(
        page_title="번역 플랫폼 모음",
        layout="wide")

    # session state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    if "DeeplAPI" not in st.session_state:
        st.session_state["DeeplAPI"] = ""


    # 사이드바 바 생성
    with st.sidebar:

        # Open AI API 키 입력받기
        st.session_state["OPENAI_API"] = st.text_input(label='OPENAI API 키', placeholder='Enter Your OpenAI API Key', value='',type='password')

        st.markdown('---')


        # DeeplAPI API  입력받기
        st.session_state["DeeplAPI"] = st.text_input(label='Deepl API 키', placeholder='Enter Your Deepl API API Key', value='',type='password')
    
        st.markdown('---')

    # 제목 
    st.header('번역 플랫폼 비교하기 프로그램')
    # 구분선
    st.markdown('---')
    st.subheader("번역을 하고자 하는 텍스트를 입력하세요")
    txt = st.text_area(label="",placeholder="input English..", height=200)
    st.markdown('---')

    st.subheader("ChatGPT 번역 결과")
    st.text("https://openai.com/blog/chatgpt")
    if st.session_state["OPENAI_API"] and txt:
        result = gpt_translate(txt,st.session_state["OPENAI_API"])
        st.info(result)
    else:
        st.info('API 키를 넣으세요')
    st.markdown('---')

    st.subheader("Deepl 번역 결과")
    st.text("https://www.deepl.com/translator")
    if st.session_state["DeeplAPI"] and txt:
        result = deepl_translate(txt,st.session_state["DeeplAPI"])
        st.info(result)
    else:
        st.info('API 키를 넣으세요')

if __name__=="__main__":
    main()
