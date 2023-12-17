import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="진로탐색 프로젝트",
    page_icon=":seedling:",
    layout="wide"
)

st.subheader(":seedling:**데이터를 통해 직업을 비교해보자**", divider="rainbow")
st.caption("**모든 데이터는 한국고용노동원(2021 한국의 직업정보 - 2021 KNOW 연구보고서)를 기반으로 한 것입니다.")

# CSV 파일을 Pandas DataFrame으로 읽어오기
file_path = "occupational_factor.csv"
data = pd.read_csv(file_path)

# 3행 2열의 colume 생성
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

# 함수
def plot_bar_chart(data, x_col, y_col, ylabel, title, colors, average_color, body):
    selected_data = data[[x_col, y_col]].sort_values(by=y_col, ascending=False)

    fig, ax = plt.subplots()
    sns.barplot(data=selected_data, x=x_col, y=y_col, palette=colors)

    ax.set(xlabel="직업", ylabel=f"[{ylabel}]")

    for bar in ax.patches:
        bar.set_linewidth(5)

    average_category = "전체\n평균"
    average_bar = ax.patches[selected_data[x_col].str.strip().tolist().index(average_category.strip())]
    average_bar.set_color(average_color)

    if ylabel == "평균소득(연봉)":
        ax.set_ylabel("평균소득(연봉)")
    elif ylabel == "주당 근로시간":
        ax.set_ylabel("주당 근로시간")
    else:
        ax.set_ylabel(f'{ylabel} 설문 점수')

    st.subheader(title)
    st.caption(body)
    st.pyplot(fig)

    # 텍스트 영역 추가
    if title == "근무조건":
        st.text_area(f"{title}이 가장 좋은 직업 분야는?", value="", height=100)
    elif title == "주당 근로시간":
        st.text_area(f"{title}이 가장 짧은 직업 분야는?", value="", height=100)
    else:
        st.text_area(f"{title}이 가장 높은 직업 분야는?", value="", height=100)
    
# 항목 리스트
items = [
    ("직업 안정성", col1, "#EDBB99", "#F5CBA7", "귀하의 현재 직업이 나이가 들어서도 계속 동일한 일을 할 수 있는 직업이라고 생각하십니까? (5점 만점)"),
    ("근무조건", col2, "#D2B4DE", "#E8DAEF", "귀하의 현재 업무는 업무환경이 쾌적하고 다른 여가를 즐길 수 있는 시간적 여유로움이 있다고 생각하십니까? (5점 만점)"),
    ("사회적 평판", col3, "#AED6F1", "#D6EAF8", "귀하가 현재 수행하고 있는 일이 사회적으로 기여하고 타인의 인정을 받을 수 있다고 생각하십니까? (5점 만점)"),
    ("주당 근로시간", col4, "#ABEBC6", "#D5F5E3", "귀하는 보통 일주일에 실제로 몇 시간 일하십니까?"),
    ("평균소득(연봉)", col5, "#F5B7B1", "#FADBD8", "세금, 상여금 등을 모두 포함한 근로소득은 얼마입니까?"),
    ("발전 가능성", col6, "#F9E79F", "#FCF3CF", "귀하가 현재 수행하고 있는 일을 통해 계속 자신의 전문성을 향상시킬 수 있으며 더 발전할 수 있다고 생각하십니까?(5점 만점)")
]

# 반복문으로 각 항목에 대한 차트 그리기
for item in items:
    title, col, color, average_color, body = item
    with col:
        colors = [color] * len(data["직업대분류"])
        plot_bar_chart(data, "직업대분류", title, title, title, colors, average_color, body)