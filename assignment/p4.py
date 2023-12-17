import streamlit as st

st.set_page_config(
    page_title="진로탐색 프로젝트",
    page_icon=":seedling:",
    layout="wide"
)

st.subheader(":seedling:**친구 직업 추천해주기**", divider="rainbow")
st.markdown("**:one:친구의 우선순위**")

# '친구이름' 입력 받기 (기본값: "수진")
friend_name = st.text_input("친구 이름을 입력하세요:", value="수진")

# 항목 리스트
items = [
    "안정성",
    "일과 삶의 균형",
    "사회적 평판",
    "연봉",
    "자기 계발",
    "사회적 기여"
]

# 선택된 순위를 저장할 딕셔너리 초기화
rankings = {}

# 6개의 열 생성
col1, col2, col3, col4, col5, col6 = st.columns(6)

# 각 col에 대해 기본값 설정
default_values = ["안정성", "일과 삶의 균형", "사회적 평판", "연봉", "자기 계발", "사회적 기여"]

# 순위 선택
for i, (col, default_value) in enumerate(zip([col1, col2, col3, col4, col5, col6], default_values), start=1):
    with col:
        # index 매개변수를 사용하여 기본으로 선택되는 값을 설정
        option = st.selectbox(
            f'{i}순위는?',
            items,
            index=items.index(default_value)  # 각 col에 대한 기본값 설정
        )
        rankings[f"{i}순위"] = option

# 선택된 순위 출력
success_message = f"**{friend_name}의 순위는!**\n"
for rank, (item, ranking) in enumerate(rankings.items(), start=1):
    success_message += f"\n{item} - {ranking}\n"

# 메시지 출력
st.warning(success_message)

# 친구 직업 분야 추천
st.markdown("**:two:친구에게 어울리는 직업 분야 추천**")
st.write("직업 특성에서 살펴본 데이터들을 떠올리며, 앞서 gpt가 나에게 직업 분야를 추천해준 것처럼 친구에게 어울릴 것 같은 직업 분야를 추천해주고 이유를 적어보자.")
jobs = ["경영, 사무, 금융, 보험직", "연구직, 공학, 기술직", "교육, 법률, 사회복지, 경찰, 소방직, 군인", "보건, 의료직", "예술, 디자인, 방송, 스포츠직", "미용, 여행, 숙박, 음식, 경비, 청소직", "영업, 판매, 운전, 운송직", "건설, 채굴직", "설치, 정비, 생산직", "농림, 어업직"]
option = st.selectbox(
            f'{friend_name}(이)에게 어울릴 것 같은 직업 분야는',
            jobs
        )

st.text_area(
    "이유를 적어봅시다",
    "수진이는 안정성 및 일과 삶을 균형을 가장 중요하게 고려하므로, 안정성이 높고 근로시간이 비교적 짧은 연구직, 공학, 기술직이 가장 적합할 것으로 생각된다.",
    )

st.subheader(":seedling:**나가며**", divider="rainbow")
st.write("직업에 대한 다양한 정보는 커리어넷 참고!")

# 버튼을 누르면 이동할 링크
link = "https://www.career.go.kr/cnet/front/main/main.do"

# 버튼을 만들어서 누를 때 링크로 이동하도록 함
if st.button("커리어넷 바로가기"):
    st.markdown(f"[커리어넷 바로가기]({link})")