import streamlit as st
import random

st.set_page_config(page_title="영화 & 책 추천 앱", page_icon="🎬📚", layout="centered")

# =============================
#        🌈 CSS 스타일 적용
# =============================
st.markdown("""
    <style>

        /* -------- 배경 파스텔 그라데이션 애니메이션 -------- */
        .main {
            background: linear-gradient(120deg, #E3F2FD, #FFF9C4, #FCE4EC, #EDE7F6, #E1F5FE);
            background-size: 500% 500%;
            animation: pastelMove 16s ease infinite;
        }

        @keyframes pastelMove {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* ---------------- 글자 폰트 부드럽게 ---------------- */
        h1, h2, h3, h4, p, label {
            font-family: 'Pretendard', sans-serif;
        }

        /* ----------- 카드 글래스모피즘 + 팝 애니메이션 ----------- */
        .card {
            background: rgba(255, 255, 255, 0.55);
            backdrop-filter: blur(9px);
            padding: 20px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            margin-bottom: 20px;
            opacity: 0;
            animation: pop 0.6s ease forwards;
        }

        @keyframes pop {
            0%   { opacity: 0; transform: scale(0.92); }
            100% { opacity: 1; transform: scale(1); }
        }

        /* ------------------- 버튼 젤리 효과 ------------------- */
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

        /* --------- 라디오 버튼을 젤리칩 디자인으로 --------- */
        div.row-widget.stRadio > div {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        div.stRadio > label {
            background: rgba(255,255,255,0.6);
            padding: 10px 15px;
            border-radius: 15px;
            border: 2px solid #E1BEE7;
            transition: 0.2s ease;
        }

        div.stRadio > label:hover {
            background: #F3E5F5;
        }

    </style>
""", unsafe_allow_html=True)


# =============================
#          UI 헤더
# =============================
st.title("🎬📚 영화 & 책 추천 웹앱")
st.subheader("✨ 간단한 취향 분석으로 나만의 콘텐츠를 추천해드려요!")


# =============================
#        카드 생성 함수
# =============================
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


# =============================
#       선택 데이터 세트
# =============================
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


# =============================
#          영화 추천
# =============================
if menu == "영화 추천":
    st.header("🎬 영화 추천")
    st.write("아래 질문에 답하면 취향에 맞는 영화를 알려드릴게요!")

    g
