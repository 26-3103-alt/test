import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="문화재 훼손"
)

st.title("문화재 훼손 예측")
st.divider()

df = pd.read_csv("data/yc_heritage_detail_enriched.csv")
st.dataframe(df)


sido_map = {
    11: "서울특별시",
    21: "부산광역시",
    22: "대구광역시",
    23: "인천광역시",
    24: "광주광역시",
    25: "대전광역시",
    26: "울산광역시",
    31: "경기도",
    32: "강원도",
    33: "충청북도",
    34: "충청남도",
    35: "전라북도",
    36: "전라남도",
    37: "경상북도",
    38: "경상남도",
    39: "제주특별자치도"
}

df["시도명"] = df["시도코드"].map(sido_map)

# 필터
selected_sido = st.sidebar.selectbox(
    "지역 선택",
    ["전체"] + sorted(df["시도명"].dropna().unique())
)

filtered_df = df.copy()

if selected_sido != "전체":
    filtered_df = filtered_df[
        filtered_df["시도명"] == selected_sido
    ]

st.dataframe(filtered_df)

st.sidebar.header("필터")

# 시도코드 선택
sido_list = ["전체"] + sorted(df["시도코드"].unique().tolist())
selected_sido = st.sidebar.selectbox(
    "시도코드 선택",
    sido_list
)

# 국가유산종목 선택
heritage_type_list = ["전체"] + sorted(df["국가유산종목"].unique().tolist())
selected_type = st.sidebar.selectbox(
    "국가유산종목 선택",
    heritage_type_list
)

# ===== 필터 적용 =====
filtered_df = df.copy()

if selected_sido != "전체":
    filtered_df = filtered_df[
        filtered_df["시도코드"] == selected_sido
    ]

if selected_type != "전체":
    filtered_df = filtered_df[
        filtered_df["국가유산종목"] == selected_type
    ]

# 결과 출력
st.dataframe(filtered_df)
