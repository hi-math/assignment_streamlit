import streamlit as st
import os
import openai
from dotenv import load_dotenv

st.set_page_config(
    page_title="진로탐색 프로젝트",
    page_icon=":seedling:",
    layout="wide"
)

st.subheader(":seedling:**직업 선택 시 나에게 더 중요한 것은?**", divider="rainbow")

# .env 파일 로드
load_dotenv()

# API 키 읽기
api_key = os.getenv("OPENAI_API_KEY")

# 항목 리스트
items = ["안정성", "일과 삶의 균형", "사회적 평판", "연봉", "자기 계발", "사회적 기여"]

# 선택된 순위를 저장할 딕셔너리 초기화
rankings = {item: None for item in items}

# 6개의 열 생성
col1, col2, col3, col4, col5, col6 = st.columns(6)

# 각 항목에 대해 라디오 버튼 생성
for i, item in enumerate(items):
    with col1 if i == 0 else col2 if i == 1 else col3 if i == 2 else col4 if i == 3 else col5 if i == 4 else col6:
        st.write(f"**{item}**")

        # 라디오 버튼을 통해 1부터 6까지의 순위 선택
        ranking = st.radio("순위 선택", [1, 2, 3, 4, 5, 6], index=i, key=item)

        # 전체 선택된 순위를 확인하여 중복 선택 여부 확인
        selected_rankings = [rank for selected_item, rank in rankings.items() if rank is not None]
        if ranking in selected_rankings:
            st.warning("이미 선택한 순위입니다. 다른 순위를 선택하세요.")
        else:
            rankings[item] = ranking

# 선택된 순위 출력
success_message = "**나의 우선순위는!**\n"
rankings_sorted = sorted(rankings.items(), key=lambda x: x[1])  # 우선순위 기준으로 정렬
for rank, (item, ranking) in enumerate(rankings_sorted, start=1):
    success_message += f"\n{rank}순위: {item}  \n"

# 메시지 출력
st.info(success_message)

# GPT API에 전달할 질문 생성
question = f"나의 우선순위는 {', '.join([f'{rank}순위: {item}' for rank, (item, _) in enumerate(rankings_sorted, start=1)])} 어떤 직업 분야가 어울릴까요? 순위를 종합적으로 고려해서 한 분야만 추천해주면 좋겠어요."

# GPT API 호출
openai.api_key = api_key
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}
]

result = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.4, max_tokens=400)

response = result['choices'][0]['message']['content']

# GPT API의 응답을 출력
st.success("GPT API로부터 받은 직업 추천:\n" + response)