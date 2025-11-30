import streamlit as st
import random
import requests

st.set_page_config(page_title="영화 & 책 추천 앱", page_icon="🎬📚", layout="centered")

OMDB_KEY = "1a38fe88"

# -------------------------------------------------
# ⭐ OMDb 포스터 가져오기 함수
# -------------------------------------------------
def get_movie_poster(movie_name):
    url = f"http://www.omdbapi.com/?apikey={OMDB_KEY}&t={movie_name}"
    res = requests.get(url).json()

    if res.get("Response") == "True" and res.get("Poster") != "N/A":
        return res["Poster"]
    else:
        return None

# =============================
#    🌈 CSS 스타일(배경/버튼/카드)
# =============================
st.markdown("""
    <style>

        .main {
            background: linear-gradient(120deg, #E3F2FD, #FFF9C4, #FCE4EC, #EDE7F6, #E1F5FE);
            background-size: 500% 500%;
            animation: pastelMove 16s ease infinite;
        }

        @keyframes pastelMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .card {
            background: rgba(255,255,255,0.55);
            backdrop-filter: blur(9px);
            padding: 20px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            margin-bottom: 20px;
            opacity: 0;
            animation: pop 0.6s ease forwards;
        }

        @keyframes pop {
            0% { opacity: 0; transform: scale(0.92); }
            100% { opacity: 1; transform: scale(1); }
        }

        .stButton>button {
            background: linear-gradient(135deg, #FFB6C1, #CE93D8);
            color: white;
            padding: 12px 20px;
            border-radius: 12px;
            border: none;
            font-size: 17px;
            font-weight: bold;
            transition: 0.25s ease;
        }

        .stButton>button:hover {
            transform: scale(1.07);
            box-shadow: 0 10px 18px rgba(0,0,0,0.15);
        }

    </style>
""", unsafe_allow_html=True)

st.title("🎬📚 영화 & 책 추천 웹앱")
st.subheader("✨ 간단한 취향 분석으로 나만의 콘텐츠를 추천해드려요!")


def card(title, description):
    st.markdown(
        f"""
        <div class="card">
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


movie_info = {
    "어바웃 타임": "시간 여행 능력을 가진 청년이 사랑과 가족을 통해 인생의 소중함을 깨닫는 이야기.",
    "라라랜드": "꿈을 좇는 배우 지망생과 재즈 음악가의 사랑과 성장 이야기.",
    "노트북": "첫사랑의 기억을 회상하며 펼쳐지는 감성적인 로맨스 이야기.",
    "극한직업": "해체 위기의 형사팀이 잠복 수사 중 치킨집을 대박 내며 벌어지는 코미디.",
    "써니": "과거 고등학교 시절 친구들과의 추억을 찾아가는 따뜻한 이야기.",
    "트루먼 쇼": "자신의 일상이 거대한 TV쇼였다는 사실을 깨닫는 남자의 이야기.",
    "기생충": "가난한 가족이 부유층 가정에 점점 스며들며 벌어지는 사건.",
    "세븐": "7가지 죄악을 모티브로 한 잔혹한 연쇄살인범을 추적하는 스릴러.",
    "셔터 아일랜드": "정신병원에서 실종 사건을 조사하던 형사가 진실을 마주하는 이야기.",
    "컨저링": "악령과 싸우는 실존 부부 엑소시스트의 공포 실화 바탕 이야기.",
    "겟 아웃": "남자친구가 여자친구 가족을 만나러 가며 벌어지는 미스터리 공포 영화.",
    "곡성": "작은 마을에 의문의 사건들이 일어나고, 그 배후를 쫓아가는 이야기.",
    "해리포터": "마법 세계에서 성장하는 소년 해리와 친구들의 모험 이야기.",
    "반지의 제왕": "절대반지를 파괴하기 위한 여정에 나선 호빗과 동료들의 판타지 대서사.",
    "나니아 연대기": "옷장 속 판타지 세계를 여행하는 아이들의 모험 이야기."
}

book_info = {
    "하마터면 열심히 살 뻔했다": "일과 삶에 지친 사람들에게 위로와 공감을 주는 에세이.",
    "죽고 싶지만 떡볶이는 먹고 싶어": "우울과 일상을 기록한 화자의 솔직한 심리 에세이.",
    "아주 작은 습관의 힘": "매일 1%씩 성장하는 습관의 과학을 다룬 자기계발서.",
    "부의 추월차선": "부자가 되는 관점을 완전히 바꿔주는 경제 자기계발 책.",
    "데미안": "내면의 나를 찾아가는 청소년의 성장 스토리.",
    "해리 포터": "마법사 소년의 모험과 성장 이야기.",
    "1984": "전체주의 감시사회에 대한 디스토피아 소설.",
    "욱하는 마음 다스리기": "감정 조절과 스트레스 해소를 알려주는 심리학 책.",
    "미움받을 용기": "타인의 시선에서 벗어나 자신의 삶을 살아가는 방법에 대한 철학적 대화."
}

menu = st.sidebar.selectbox("메뉴 선택", ["영화 추천", "책 추천"])

movies = {
    "로맨스": ["어바웃 타임", "라라랜드", "노트북"],
    "코미디": ["극한직업", "써니", "트루먼 쇼"],
    "스릴러": ["기생충", "세븐", "셔터 아일랜드"],
    "공포": ["컨저링", "겟 아웃", "곡성"],
    "판타지": ["해리포터", "반지의 제왕", "나니아 연대기"],
}

mood_bonus = {
    "힐링하고 싶어요": "따뜻하고 감동적인 작품이 오늘 기분에 잘 맞아요!",
    "몰입감 있는 게 좋아요": "집중력 200%로 빠져드는 작품을 추천드릴게요!",
    "웃고 싶어요": "재미있고 가벼운 분위기의 작품이 좋아요!",
}

books = {
    "감성/에세이": ["하마터면 열심히 살 뻔했다", "죽고 싶지만 떡볶이는 먹고 싶어"],
    "자기계발": ["아주 작은 습관의 힘", "부의 추월차선"],
    "소설": ["데미안", "해리 포터", "1984"],
    "심리학": ["욱하는 마음 다스리기", "미움받을 용기"],
}

book_moods = {
    "차분하게 읽고 싶어요": "잔잔하고 감성적인 책이 잘 맞아요.",
    "동기부여 받고 싶어요": "불타오르는 MOTIVATION을 드릴게요!",
    "몰입감 있는 스토리가 좋아요": "빠져드는 스토리 중심의 책을 추천할게요!",
}

# --------------------------------------
# 🎬 영화 추천
# --------------------------------------
if menu == "영화 추천":
    st.header("🎬 영화 추천")

    genre = st.radio("어떤 장르가 좋아요?", list(movies.keys()))
    mood = st.radio("오늘 기분은 어때요?", list(mood_bonus.keys()))
    length = st.radio("선호하는 영화 길이는?", ["짧은 영화", "보통", "긴 영화"])

    if st.button("🎞 영화 추천 받기"):
        pick = random.choice(movies[genre])

        st.subheader("✨ 추천 결과")
        card("🎬 추천 영화", pick)
        card("📖 영화 줄거리", movie_info[pick])
        card("✔️ 추천 이유", mood_bonus[mood])

        poster = get_movie_poster(pick)
        if poster:
            st.image(poster, width=300)
        else:
            st.info("포스터를 찾을 수 없어요 😢")

# --------------------------------------
# 📚 책 추천
# --------------------------------------
else:
    st.header("📚 책 추천")

    book_type = st.radio("읽고 싶은 책 종류는?", list(books.keys()))
    mood_b = st.radio("오늘 독서 분위기는?", list(book_moods.keys()))

    if st.button("📖 책 추천 받기"):
        pick = random.choice(books[book_type])

        st.subheader("✨ 추천 결과")
        card("📘 추천 도서", pick)
        card("📖 책 줄거리", book_info[pick])
