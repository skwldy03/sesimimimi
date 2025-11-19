import streamlit as st
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="세심제 - 강원사대부고 축제",
    layout="centered",
)

# CSS 스타일
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'NanumSquare', sans-serif;
}

.main {
    max-width: 480px;
    margin: 0 auto;
}

.header-box {
    text-align: center;
    padding: 20px 10px;
    background: linear-gradient(135deg, #8d5fe7, #b77bff);
    color: white;
    border-radius: 16px;
    margin-bottom: 20px;
}

.card {
    background: #ffffff;
    padding: 18px 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.tab-box {
    display: flex;
    justify-content: space-between;
    margin: 5px 0 20px 0;
}

.tab-btn {
    flex: 1;
    background: #f7f2ff;
    padding: 12px;
    margin: 0 4px;
    text-align: center;
    border-radius: 12px;
    font-weight: bold;
    color: #6d36c9;
    border: 1.5px solid #d8c9ff;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------
# 페이지 상태 (초기값은 home)
# -------------------------------------------
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# -------------------------------------------
# 상단 헤더
# -------------------------------------------
st.markdown("""
<div class="header-box">
    <h1>🎉 세심제 2025 🎉</h1>
    <h4>강원사대부고 학교축제</h4>
    <p>12월 29일 ~ 12월 30일</p>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------
# 탭 메뉴 (Streamlit 버튼으로 전환)
# -------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 홈"):
        