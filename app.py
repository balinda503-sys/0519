import streamlit as st
st.set_page_config(page_title="微型 TimeTree",layout="wide")
with st.sidebar:
  st.write("### 行事曆群組")
  st.radio("選擇群組",["業務","行政"])

# 1. 初始化 Session State（用來暫存行程資料）
if "events" not in st.session_state:
    st.session_state.events = [
        {"日期": "2026-05-01", "事項": "勞動節放假", "狀態": "本月行程"},
        {"日期": "2026-04-15", "事項": "4月份財務對帳", "狀態": "已封存行程"},
    ]

# 2. 設定網頁標題與主頁面寬度
st.set_page_config(page_title="個人行事曆網頁", layout="wide")
st.title("📅 我的工作行事曆")

# --- 側邊欄 (st.sidebar) ---
with st.sidebar:
    st.header("⚙️ 功能選單")
    st.write("歡迎使用行事曆系統")
    
    # 側邊欄工具範例
    filter_cate = st.selectbox("篩選行程類別", ["全部", "工作", "個人", "緊急"])
    st.info("提示：點擊右側分頁可切換查看不同的行程狀態。")

# --- 主畫面佈局 (st.columns) ---
# 使用 1:3 的比例切分成左右兩欄
col1, col2 = st.columns([1, 3])

# --- 左欄：新增行程提示與表單 ---
with col1:
    st.subheader("➕ 新增行程")
    
    # 使用 Form 讓使用者輸入資料
    with st.form("add_event_form", clear_on_submit=True):
        event_date = st.date_input("選擇日期", datetime.now())
        event_text = st.text_input("行程內容描述", placeholder="例如：下午 2:00 線上會議")
        event_status = st.selectbox("歸類分頁", ["本月行程", "已封存行程"])
        
        submit_btn = st.form_submit_button("確認新增")
        
        if submit_btn:
            if event_text.strip() == "":
                st.error("請輸入行程內容！")
            else:
                # 將新行程加入暫存
                new_event = {
                    "日期": str(event_date),
                    "事項": event_text,
                    "狀態": event_status
                }
                st.session_state.events.append(new_event)
                st.success(f"成功新增至【{event_status}】！")

# --- 右欄：外框容器與分頁頁籤 ---
with col2:
    st.subheader("📋 行程總覽")
    
    # 建立帶有外框的容器
    with st.container(border=True):
        
        # 在容器內部嵌入一組分頁頁籤
        tab1, tab2 = st.tabs(["📅 本月行程", "🗄️ 已封存行程"])
        
        # 將行程資料轉換為 DataFrame 方便篩選與呈現
        df_events = pd.DataFrame(st.session_state.events)
        
        # 分頁 1：本月行程
        with tab1:
            st.markdown("### 📌 本月待辦與規劃")
            current_events = df_events[df_events["狀態"] == "本月行程"]
            
            if not current_events.empty:
                st.dataframe(current_events[["日期", "事項"]], use_container_width=True, hide_index=True)
            else:
                st.caption("目前沒有本月行程。")
                
        # 分頁 2：已封存行程
        with tab2:
            st.markdown("### 📁 歷史紀錄封存")
            archived_events = df_events[df_events["狀態"] == "已封存行程"]
            
            if not archived_events.empty:
                st.dataframe(archived_events[["日期", "事項"]], use_container_width=True, hide_index=True)
            else:
                st.caption("目前沒有已封存的行程。")
