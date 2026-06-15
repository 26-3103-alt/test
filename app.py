import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="문화재 훼손"
)

st.title("문화재 훼손 예측")
st.divider()

df = pd.read_csv("data/yc_heritage_detail_enriched.csv")
st.dataframe(df)


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
