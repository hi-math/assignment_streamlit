import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
    page_title="진로탐색 프로젝트",
    page_icon=":seedling:",
    layout="wide"
)

# 페이지 정의
pages = [
    Page("p1.py", "들어가기", ":cactus:"),
    Page("p2.py", "직업 특성", ":palm_tree:"),
    Page("p3.py", "나의 가치관", ":evergreen_tree:"),
    Page("p4.py", "직업 추천", ":deciduous_tree:")
]

# 페이지 표시
show_pages(pages)

# 진로탐색프로젝트
st.title(":sunflower:진로탐색 프로젝트:sunflower:")
st.subheader("뭘 할 지 모르겠어? 오늘 같이 고민해보자!")

image_path = "./img1.jpg"
st.image(image_path, caption="출처:https://www.ytn.co.kr/_ln/0103_202212200127267290", use_column_width=True)

st.subheader(":seedling:**오늘의 목표**", divider="rainbow")
text = (
    "1. **데이터로** 직업 특성 살펴보기\n"
    "2. 나의 직업 **가치관** 모색하기\n"
    "3. 나에게 **적합한 직업** 고민하기\n"
    "4. 친구에게 **적합한 직업 추천**해주기"
)
st.write(text)

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

# 직업 선택 워드 클라우드
st.subheader(":seedling:**직업 선택 시 중요한 것은?**", divider="rainbow")

# 텍스트 입력을 받습니다.
user_input = st.text_input("답변을 입력하세요:")

# 파일에 저장된 이전 답변을 불러오기
filename = 'previous_responses.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        previous_responses = file.read().splitlines()
except FileNotFoundError:
    previous_responses = []

# 사용자가 입력한 텍스트가 있거나 이전 답변이 있으면 Word Cloud를 표시합니다.
if user_input or previous_responses:
    # 이전 답변에 현재 답변을 추가
    if user_input:
        previous_responses.append(user_input)

        # 모든 답변을 파일에 저장
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(previous_responses))

    # 모든 답변을 합쳐서 하나의 텍스트로 만듭니다.
    all_responses_text = ' '.join(previous_responses)

    # Word Cloud 생성
    wordcloud = WordCloud(
        font_path='./NanumGothic.ttf',
        background_color='white'  # 배경색을 흰색으로 지정
    ).generate(all_responses_text)

    # Matplotlib figure 생성
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    # BytesIO에 저장
    image_stream = BytesIO()
    plt.savefig(image_stream, format="png")
    plt.close(fig)

    # 결과를 세션 상태에 추가
    st.image(image_stream, caption="Word Cloud", width=None)

# # 초기화 버튼
# if st.button("초기화"):
#     # 이전 답변 초기화
#     previous_responses = []
#     # 파일에도 초기화된 상태 저장
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write('')
#     # 메시지 출력
#     st.success("이전 답변이 초기화되었습니다.")


