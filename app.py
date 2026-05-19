import streamlit as st
st.set_page_config(page_title="微型 TimeTree",layout="wide")
with st.sidebar:
  st.write("### 行事曆群組")
  st.radio("選擇群組",["業務","行政"])


```python
import pandas as pd
import streamlit as st

# =========================
# 頁面設定
# =========================
st.set_page_config(
    page_title="階段實作練習四",
    page_icon="📅",
    layout="wide"
)

# =========================
# 標題區
# =========================
st.title("階段實作練習四")

st.badge("練習四")

st.header("進階備忘錄與自動化通知設定")

st.markdown("""
建立參數設定區：

- 左邊：藥丸標籤（pills）+ 多行備忘錄（text_area）
- 右邊：滑動開關（toggle），開啟時顯示數字計數器（number_input）
- 最下方：st.dataframe 展示模擬歷史設定報表
""")

st.divider()

# =========================
# 參數設定區
# =========================
left_col, right_col = st.columns(2)

# -------------------------
# 左邊欄位
# -------------------------
with left_col:

    st.subheader("🏷️ 行程標籤")

    # 如果你的 streamlit 版本太舊
    # 可改成 st.multiselect()
    tags = st.pills(
        "選擇分類",
        ["工作", "會議", "學習", "旅遊", "私人"],
        selection_mode="multi"
    )

    st.write("目前選擇：", tags)

    st.subheader("📝 備忘錄")

    memo = st.text_area(
        "請輸入備忘內容",
        placeholder="例如：記得準備簡報、確認會議時間...",
        height=200
    )

# -------------------------
# 右邊欄位
# -------------------------
with right_col:

    st.subheader("🔔 通知設定")

    enable_notice = st.toggle("啟用自動通知")

    if enable_notice:

        notice_count = st.number_input(
            "通知次數",
            min_value=1,
            max_value=10,
            value=3,
            step=1
        )

        st.success(f"目前通知次數：{notice_count}")

    else:
        st.info("目前未啟用通知功能")

# =========================
# 模擬歷史設定報表
# =========================
st.divider()

st.subheader("📊 歷史設定報表")

history_df = pd.DataFrame({
    "日期": [
        "2026-05-01",
        "2026-05-05",
        "2026-05-10",
        "2026-05-15"
    ],
    "分類": [
        "工作",
        "私人",
        "會議",
        "學習"
    ],
    "備忘錄": [
        "完成專案排程",
        "安排家庭聚餐",
        "客戶需求確認",
        "Python 課程複習"
    ],
    "通知次數": [
        2,
        1,
        3,
        5
    ]
})

st.dataframe(
    history_df,
    use_container_width=True,
    hide_index=True
)
```

    use_container_width=True,
    hide_index=True
)

