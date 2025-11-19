import streamlit as st

st.title("🎉 우리 학교 축제 안내 홈페이지")
st.subheader("2025 스쿨 페스티벌")

st.image("https://picsum.photos/900/300", caption="축제 분위기 이미지")

st.header("📅 축제 일정")
st.write("""
- **날짜:** 2025년 5월 27일  
- **시간:** 오전 10시 ~ 오후 5시  
- **장소:** 학교 운동장 및 본관  
""")

st.header("🎤 공연 프로그램")
st.write("""
- 11:00 ▸ 밴드부 공연  
- 13:00 ▸ 댄스동아리  
- 15:00 ▸ 랩 경연  
""")

st.header("🍔 먹거리 부스")
st.write("- 떡볶이\n- 핫도그\n- 타코야끼\n- 아이스크림\n- 츄로스")

st.header("🗳️ 인기 부스 투표")
choice = st.selectbox("가장 기대되는 부스를 선택하세요!", 
                      ["게임부스", "먹거리부스", "포토존", "공연무대"])
st.write("선택:", choice)
