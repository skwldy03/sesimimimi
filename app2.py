import streamlit as st
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="세심제 - 강원사대부고 축제",
    layout="centered",
)

# -------------------------
# 스타일 (CSS) 적용
# -------------------------
st.markdown("""
<style>

/* 전체 글꼴, 센터 정렬 */
html, body, [class*="css"]  {
    font-family: 'NanumSquare', sans-serif;
}

/* 모바일 기준 폭 조정 */
.main {
    max-width: 480px;
    margin: 0 auto;
}

/* 상단 헤더 중심 */
.header-box {
    text-align: center;
    padding: 20px 10px;
    background: linear-gradient(135deg, #8d5fe7, #b77bff);
    color: white;
    border-radius: 16px;
    margin-bottom: 20px;
}

/* 카드 디자인 */
.card {
    background: #ffffff;
    padding: 18px 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

/* 상단 탭 메뉴 */
.tab-box {
    display: flex;
    justify-content: space-between;
    margin: 10px 0 25px 0;
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
    cursor: pointer;
    transition: 0.2s;
}

.tab-btn:hover {
    background: #ece3ff;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------
# 🎪 세심제 상단 헤더
# -------------------------------------------
st.markdown("""
<div class="header-box">
    <h1>🎉 세심제 2025 🎉</h1>
    <h4>강원사대부고 학교축제</h4>
    <p>12월 29일 ~ 12월 30일</p>
</div>
""", unsafe_allow_html=True)


# -------------------------
# 상단 탭 메뉴
# -------------------------
st.markdown("""
<div class="tab-box">
    <div class="tab-btn" onclick="window.location.href='/?page=home'">🏠 홈</div>
    <div class="tab-btn" onclick="window.location.href='/?page=schedule'">📅 일정</div>
    <div class="tab-btn" onclick="window.location.href='/?page=booth'">🎪 부스</div>
    <div class="tab-btn" onclick="window.location.href='/?page=notice'">📢 안내</div>
</div>
""", unsafe_allow_html=True)


# 현재 페이지 값 확인
page = st.query_params.get("page", ["home"])[0]


# -------------------------------------------------------
# 페이지 : 홈
# -------------------------------------------------------
if page == "home":
    st.image("https://picsum.photos/500/250", caption="세심제 분위기 미리보기", use_column_width=True)

    # 타이머 카드
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⏰ 축제 시작까지 남은 시간")

    festival_start = datetime(2025, 12, 29, 10, 0)
    now = datetime.now()
    rest = festival_start - now

    if rest.total_seconds() > 0:
        d = rest.days
        h = rest.seconds // 3600
        m = (rest.seconds % 3600) // 60
        st.write(f"**{d}일 {h}시간 {m}분 남았습니다!**")
    else:
        st.write("🎉 지금 축제가 진행 중입니다!")
    st.markdown('</div>', unsafe_allow_html=True)


    # 소개 카드
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎈 세심제란?")
    st.write("강원사대부고의 연말 대표 축제로, 학생들이 직접 준비한 공연, 부스, 이벤트가 가득합니다!")
    st.markdown('</div>', unsafe_allow_html=True)



# -------------------------------------------------------
# 페이지 : 일정
# -------------------------------------------------------
elif page == "schedule":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📅 세심제 일정")
    st.write("### ✔ 12월 29일 (1일차)")
    st.write("""
    - 10:00 ▸ 개막식  
    - 11:00 ▸ 밴드 공연  
    - 13:00 ▸ 댄스 동아리  
    - 15:00 ▸ 랩 경연  
    - 16:30 ▸ 포토존 이벤트  
    """)
    st.write("### ✔ 12월 30일 (2일차)")
    st.write("""
    - 10:00 ▸ 학생 DJ 오프닝  
    - 12:00 ▸ 장기자랑  
    - 14:00 ▸ e스포츠 대회  
    - 16:00 ▸ 폐막식  
    """)
    st.markdown('</div>', unsafe_allow_html=True)



# -------------------------------------------------------
# 페이지 : 부스
# -------------------------------------------------------
elif page == "booth":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎪 부스 안내")

    st.write("""
    - 🍔 **먹거리 부스** → 떡볶이, 어묵, 타코야끼  
    - 🎯 **게임 부스** → 다트, 룰렛, 농구 던지기  
    - 📸 **포토존** → 즉석사진, 폴라로이드  
    - 🎨 **체험 부스** → 페이스페인팅, 캘리그라피  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🗳️ 부스 인기 투표")
    pick = st.selectbox("가장 기대되는 부스는?", 
                        ["먹거리", "게임", "포토존", "체험"])
    st.write("✔ 선택됨:", pick)
    st.markdown('</div>', unsafe_allow_html=True)



# -------------------------------------------------------
# 페이지 : 안내
# -------------------------------------------------------
elif page == "notice":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📢 안내 사항")
    st.write("""
    - 학생증 필수 지참  
    - 쓰레기 분리수거 철저히  
    - 위험 물품 반입 금지  
    - 이동 시 안전 주의  
    - 타 학교 학생도 입장 가능  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

