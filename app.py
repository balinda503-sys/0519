import streamlit as st
st.set_page_config(page_title="微型 TimeTree",layout="wide")
with st.sidebar:
  st.write("### 行事曆群組")
  st.radio("選擇群組",["業務","行政"])


# =========================
# 頁面設定
# =========================
st.set_page_config(
    page_title="行事曆設定頁",
    page_icon="📅",
    layout="wide"
)

st.title("📅 行事曆參數設定")

# =========================
# 參數設定區
# =========================
st.subheader("⚙️ 參數設定")

left_col, right_col = st.columns(2)

# -------------------------
# 左邊區塊
# -------------------------
with left_col:

    st.markdown("### 🏷️ 行程分類")

    category = st.pills(
        "選擇標籤",
        ["工作", "會議", "私人", "旅遊", "學習"],
        selection_mode="multi"
    )

    st.markdown("### 📝 備忘錄")

    memo = st.text_area(
        "請輸入備忘內容",
        placeholder="例如：記得準備會議簡報與文件...",
        height=180
    )

# -------------------------
# 右邊區塊
# -------------------------
with right_col:

    st.markdown("### 🔧 進階設定")

    enable_counter = st.toggle("啟用數量限制")

    if enable_counter:
        limit_value = st.number_input(
            "設定最大數量",
            min_value=1,
            max_value=100,
            value=10,
            step=1
        )

        st.success(f"目前限制數量：{limit_value}")

# =========================
# 模擬歷史設定報表
# =========================
st.divider()

st.subheader("📊 歷史設定報表")

history_df = pd.DataFrame({"日期": ["2026-05-01", "2026-05-05", "2026-05-10"],"分類": ["工作", "私人", "會議"],"備忘錄": ["完成專案排程", "安排家庭聚餐","客戶需求確認"], "限制數量": [5, 10, 3]})

st.dataframe(
    history_df,
    use_container_width=True,
    hide_index=True)

