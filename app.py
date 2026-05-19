import streamlit as st
st.set_page_config(page_title="微型 TimeTree",layout="wide")
with st.sidebar:
  st.write("### 行事曆群組")
  st.radio("選擇群組",["業務","行政"])

# =========================
# 頁面設定
# =========================
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
# 左欄：新增行程
# -------------------------
with left_col:

    st.subheader("📝 新增行程")

    # 行程名稱
    event_title = st.text_input(
        "行程名稱",
        placeholder="請輸入行程名稱"
    )

    # 日期選擇
    event_date = st.date_input(
        "選擇日期",
        value=date.today()
    )

    # 顏色選擇
    event_color = st.selectbox(
        "選擇標籤顏色",
        ["🔴 紅色", "🟢 綠色", "🔵 藍色", "🟡 黃色", "🟣 紫色"]
    )

    # 提醒時間
    reminder_time = st.selectbox(
        "提醒時間",
        [
            "15 分鐘前",
            "30 分鐘前",
            "45 分鐘前",
            "60 分鐘前"
        ]
    )

    # 備忘錄
    event_note = st.text_area(
        "備忘錄",
        placeholder="請輸入行程備註..."
    )

    # 新增按鈕
    if st.button("✅ 建立行程"):
        st.success("行程新增成功！")

        st.write("### 已建立的行程")
        st.write(f"📌 行程名稱：{event_title}")
        st.write(f"📅 日期：{event_date}")
        st.write(f"🎨 顏色：{event_color}")
        st.write(f"⏰ 提醒時間：{reminder_time}")
        st.write(f"📝 備忘錄：{event_note}")

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

        # =====================
        # 本月行程
        # =====================
        with tab1:

            st.write("### 本月行程列表")

            st.markdown("""
            <div style="
                padding:10px;
                border-radius:10px;
                background-color:#ffe5e5;
                margin-bottom:10px;
            ">
            🔴 05/20 - 團隊會議（15 分鐘前提醒）
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
                padding:10px;
                border-radius:10px;
                background-color:#e5f0ff;
                margin-bottom:10px;
            ">
            🔵 05/24 - 客戶簡報（30 分鐘前提醒）
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
                padding:10px;
                border-radius:10px;
                background-color:#e5ffe5;
                margin-bottom:10px;
            ">
            🟢 05/28 - 專案驗收（60 分鐘前提醒）
            </div>
            """, unsafe_allow_html=True)

        # =====================
        # 已封存行程
        # =====================
        with tab2:

            st.write("### 已封存行程")

            st.warning("04/10 - 春季活動")
            st.warning("04/18 - 系統維護")

