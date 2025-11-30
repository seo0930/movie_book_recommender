import streamlit as st
import random

st.set_page_config(page_title="영화 & 책 추천 앱", page_icon="🎬")
st.title("🎬📚 영화 & 책 추천 웹앱")
st.write("간단한 질문에 답하면 나에게 맞는 콘텐츠를 추천받을 수 있어요!")

menu = st.sidebar.selectbox("메뉴 선택", ["영화 추천", "책 추천"])

movies = {
    "로맨스": ["어바웃 타임", "라라랜드", "노트북"],
    "코미디": ["극한직업", "써니", "트루먼 쇼"],
    "스릴러": ["기생충", "세븐", "셔터 아일랜드"],
    "공포": ["컨저링", "겟 아웃", "곡성"],
    "판타지": ["해리포터", "반지의 제왕", "나니아 연대기"],
}

mood_bonus = {
    "힐링하고 싶어요": "따뜻하고 감동적인 작품을 추천드려요!",
    "몰입감 있는 게 좋아요": "긴장감 넘치고 집중되는 작품이 잘 맞아요!",
    "웃고 싶어요": "가벼운 분위기의 코미디 작품들이 좋아요!",
}

books = {
    "감성/에세이": ["하마터면 열심히 살 뻔했다", "죽고 싶지만 떡볶이는 먹고 싶어"],
    "자기계발": ["아주 작은 습관의 힘", "부의 추월차선"],
    "소설": ["데미안", "해리 포터", "1984"],
    "심리학": ["욱하는 마음 다스리기", "미움받을 용기"],
}

book_moods = {
    "차분하게 읽고 싶어요": "잔잔하고 감성이 풍부한 책을 추천드릴게요.",
    "동기부여 받고 싶어요": "의지가 생기고 도전하게 만드는 책이 잘 맞아요!",
    "몰입감 있는 스토리가 좋아요": "소설이나 스토리 중심 책이 좋아요!",
}

if menu == "영화 추천":
    st.header("🎬 영화 추천")
    st.write("아래 질문에 체크하고 ‘추천 버튼’을 눌러보세요!")
    genre = st.radio("어떤 장르가 좋아요?", list(movies.keys()))
    mood = st.radio("오늘 기분은 어때요?", list(mood_bonus.keys()))
    length = st.radio("선호하는 영화 길이는?", ["짧은 영화(110분 이하)", "보통", "긴 영화(140분 이상)"])
    if st.button("🎞 영화 추천 받기"):
        st.subheader("✨ 추천 결과")
        pick = random.choice(movies[genre])
        st.write(f"**🎬 추천 영화: {pick}**")
        st.write(f"✔️ 추천 이유: {mood_bonus[mood]}")
        st.write(f"✔️ 장르 기준 추천: {genre}")
        st.write(f"✔️ 길이 취향: {length}")
else:
    st.header("📚 책 추천")
    st.write("아래 질문에 대답하면 책을 추천해드릴게요!")
    book_type = st.radio("읽고 싶은 책 종류는?", list(books.keys()))
    mood_b = st.radio("오늘의 독서 분위기는?", list(book_moods.keys()))
    if st.button("📖 책 추천 받기"):
        st.subheader("✨ 추천 결과")
        pick = random.choice(books[book_type])
        st.write(f"**📘 추천 도서: {pick}**")
        st.write(f"✔️ 선택한 분야: {book_type}")
        st.write(f"✔️ 분위기 기반 추천: {book_moods[mood_b]}")
