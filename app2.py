import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="공지천 수질 데이터 분석",
    layout="wide"
)

# ----------------------------------------------------------
# 1. 최상단: 프로젝트 소개
# ----------------------------------------------------------

st.title("공지천 수질 측정 데이터 분석 보고서")
st.subheader("우리가 쓰는 물은 안전할까?")
st.markdown("---")

left, middle, right = st.columns(3)
if left.button("용존산소"):
    left.markdown("물속에 녹아 있는 산소의 양")
if middle.button("총질소"):
    middle.markdown("물속에 존재하는 모든 형태의 질소 화합물(무기성 질소 + 유기성 질소)의 총량")
if right.button("총유기탄소"):
    right.markdown("물속에 녹아 있거나 떠 있는 모든 유기물을 구성하는 탄소의 총량")
st.markdown("---")
    
# ----------------------------------------------------------
# 2. 데이터셋 소개 (텍스트, 사진, 링크, 영상)
# ----------------------------------------------------------

col1, col2 = st.columns([1, 1])

with col1: #왼쪽 화면
    st.info("사용된 데이터 정보")
    st.write("**데이터 파일명:** 공지천3_수질측정망.csv")
    st.write("**데이터 출처:** 국가 통합물관리정보플랫폼(https://www.mulmoa.go.kr/web/gDashBoard)")
    try:
        st.image("공지천 사진.jpg", caption="공지천의 모습")
    except:
        st.write("이미지를 불러올 수 없습니다.")

with col2:
    st.warning("우리의 실천 방안")
    st.video("https://www.youtube.com/watch?v=6s7vo55ekFA")

st.markdown("---")

# ----------------------------------------------------------
# 3. 데이터 로드 및 전처리
# ----------------------------------------------------------

st.header("1. 데이터 로드 및 전처리")
data = pd.read_csv("공지천3_수질측정망.csv", encoding='utf-8')
st.dataframe(data)

st.subheader("용존산소와 총질소(전처리)")
data2 = data[['용존산소','총질소']]
st.line_chart(data2)

data3 = data2.dropna()
st.header("2. 결측치 제거 후 데이터")
st.dataframe(data3)

# ----------------------------------------------------------
# 4. 데이터 분석 및 시각화
# ----------------------------------------------------------

st.header("3. 데이터 분석 및 시각화")
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig1, ax1 = plt.subplots()
    st.subheader(" 시각화 1: 선그래프")
    sns.lineplot(data=data3, x='용존산소', y='총질소', ax=ax1)
    ax1.set_title('용존산소와 총질소의 관계')
    ax1.set_xlabel('용존 산소 (mg/L)')
    ax1.set_ylabel('총질소 (mg/L)')
    st.pyplot(fig1)

with chart_col2:
    fig2, ax2 = plt.subplots()
    st.subheader(" 시각화 2: 막대그래프")
    sns.barplot(data=data3, x='용존산소', y='총질소', ax=ax2)
    ax2.set_title('용존산소와 총질소의 관계')
    ax2.set_xlabel('용존 산소 (mg/L)')
    ax2.set_ylabel('총질소 (mg/L)')
    ax2.set_xticks(ax2.get_xticks()[::1])  # x축 눈금 간격 조정
    st.pyplot(fig2)

# ----------------------------------------------------------
# 5. 결론 및 인사이트
# ----------------------------------------------------------

st.markdown("---")
st.header("4. 분석 결과 및 인사이트")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:
    st.info("데이터 분석 요약")
    st.write("1. 용존산소(DO)와 총질소(TN)는 대체로 **반비례/정비례** 관계를 보임.")
    st.write("2. 특정 시기(또는 지점)에서 수질 수치가 급격히 변하는 구간 발견.")

with summary_col2:
    st.warning("환경적 제언")
    st.write("- 총질소 농도가 높은 구간은 인근 농경지나 생활 하수의 유입이 의심됨.")
    st.write("- 지속적인 모니터링을 통해 공지천의 자정 작용을 도와야 함.")

st.success("이번 프로젝트를 통해 데이터가 단순한 숫자가 아니라 우리 동네의 환경 상태를 알려주는 중요한 지표임을 깨달았습니다.")