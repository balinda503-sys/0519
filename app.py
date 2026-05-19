import streamlit as st
st.set_page_config(page_title="微型 TimeTree",layout="wide")
with st.sidebar:
  st.write("### 行事曆群組")
  st.radio("選擇群組",["業務","行政"])


# 頁面設定
st.set_page_config(
    page_title="行事曆管理",
    page_icon="📅",
    layout="wide"
)

# =========================
# 側邊欄
# =========================
with st.sidebar:
    st.title("📌 功能選單")

    st.markdown("### 使用者資訊")
    st.write("歡迎回來，使用者！")

    st.markdown("### 快速功能")
    st.button("➕ 新增行程")
    st.button("📂 查看封存")

# =========================
# 主畫面
# =========================
left_col, right_col = st.columns([1, 3])

# -------------------------
# 左欄：新增行程提示
# -------------------------
with left_col:
    st.subheader("📝 新增行程")

    st.info(
        "請點選側邊欄的「新增行程」按鈕，"
        "即可建立新的行程內容。"
    )

# -------------------------
# 右欄：行程內容
# -------------------------
with right_col:
    with st.container(border=True):

        st.subheader("📅 行程管理")

        tab1, tab2 = st.tabs([
            "本月行程",
            "已封存行程"
        ])

        # 本月行程
        with tab1:
            st.write("### 本月行程列表")

            st.success("05/20 - 團隊會議")
            st.success("05/24 - 客戶簡報")
            st.success("05/28 - 專案驗收")

        # 已封存行程
        with tab2:
            st.write("### 已封存行程")

            st.warning("04/10 - 春季活動")
            st.warning("04/18 - 系統維護")
