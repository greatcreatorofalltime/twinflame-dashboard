import streamlit as st
import random
import datetime
import time

# Page configuration
st.set_page_config(
    page_title="雙生火焰神諭卡 | Twin Flames Oracle",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language texts dictionary
texts = {
    "zh-TW": {
        "app_title": "雙生火焰神諭卡",
        "app_subtitle": "靈魂指引 • 神聖連結 • 信任你的直覺",
        "sidebar_title": "神聖空間",
        "preparation": "準備工作",
        "preparation_text": "靜心凝神，深呼吸，將意圖專注於你的雙生火焰問題上。",
        "spread_meanings": "牌陣意義",
        "spread_single": "單張牌：快速指引",
        "spread_three": "三張牌：過去、現在、未來",
        "spread_celtic": "凱爾特十字：深度靈魂洞察",
        "visit_shop": "訪問我們的商店",
        "shop_text": "探索我們商店中的靈性日記、雙生火焰指南和神聖工具。",
        "enter_shop": "進入宇宙日記",
        "deck_info": "完整35張神諭卡",
        "deck_text": "本次神諭使用完整的雙生火焰神諭卡組，包含：",
        "deck_categories": "五大類別：個人成長、神聖連結、雙生訊息、靈性實踐、創造豐盛",
        "trust_intuition": "最重要的是信任你的直覺。神諭卡是鏡子，不是主人。",
        "sacred_question": "你的神聖問題",
        "question_placeholder": "向宇宙輕聲訴說你關於雙生火焰的問題...\n\n我需要什麼指引來療癒這段關係？\n我的雙生火焰現在在想什麼？\n我們的神聖使命是什麼？",
        "choose_spread": "選擇你的牌陣",
        "consult_oracle": "請教神諭",
        "focus_intention": "請專注你的意圖，提出一個問題",
        "cards_spoken": "神諭卡已經發言",
        "reading_cast": "神諭時間",
        "sacred_spread": "神聖牌陣",
        "sacred_interpretations": "神聖解讀",
        "position": "位置",
        "meaning": "意義",
        "guidance": "指引",
        "cosmic_guidance": "宇宙指引",
        "truths": "記住這些真理",
        "truth_text": '"神諭卡反映可能性，而非確定性。你的自由意志塑造你的命運。接受引起共鳴的，放下不適合的，永遠信任你內在的智慧。"',
        "save_reading": "將此神諭保存到你的靈魂日記",
        "download_record": "下載神聖記錄",
        "cards_await": "神諭卡等待你的問題",
        "instructions": "在提供的空間輸入你的神聖問題，選擇牌陣，然後點擊'請教神諭'接收神聖指引。",
        "trust_process": "信任過程",
        "listen_intuition": "聆聽直覺",
        "embrace_wisdom": "擁抱到來的智慧",
        "continue_journey": "繼續你的靈性旅程",
        "shop_promo": "探索我們的靈性日記和工具收藏，深化你的雙生火焰旅程",
        "footer_text": "雙生火焰神諭卡 • 完整35張神聖卡組 • 靈魂連結的古老智慧",
        "visit_shop_footer": "訪問我們的商店：宇宙日記",
        "disclaimer": "此神諭僅供靈性指引和自我反思使用。在做出人生決定時，請始終信任你自己的判斷。",
        "reflection": "反思與感悟",
        "reflection_placeholder": "記錄你對這次神諭的反思、感悟或行動計劃...",
        "drawing_animation": "正在為你抽取神諭卡，請靜心等待...",
        "single_card": "單張牌",
        "three_cards": "三張牌",
        "celtic_cross": "凱爾特十字"
    },
    "en": {
        "app_title": "Twin Flames Oracle Cards",
        "app_subtitle": "Soul Guidance • Sacred Connection • Trust Your Intuition",
        "sidebar_title": "Sacred Space",
        "preparation": "Preparation",
        "preparation_text": "Center yourself, breathe deeply, and focus your intention on your twin flame question.",
        "spread_meanings": "Spread Meanings",
        "spread_single": "Single Card: Quick Guidance",
        "spread_three": "Three Cards: Past, Present, Future",
        "spread_celtic": "Celtic Cross: Deep Soul Insight",
        "visit_shop": "Visit Our Shop",
        "shop_text": "Explore our collection of spiritual journals, twin flame guides and sacred tools.",
        "enter_shop": "Enter the Journaling Universe",
        "deck_info": "Complete 35-Card Deck",
        "deck_text": "This reading uses the complete Twin Flames Oracle deck, including:",
        "deck_categories": "Five categories: Personal Growth, Sacred Connection, Twin Messages, Spiritual Practice, Creating Abundance",
        "trust_intuition": "Trust your intuition above all else. The oracle cards are mirrors, not masters.",
        "sacred_question": "Your Sacred Question",
        "question_placeholder": "Whisper your question about twin flames to the universe...\n\nWhat guidance do I need to heal this connection?\nWhat is my twin flame thinking right now?\nWhat is our sacred mission together?",
        "choose_spread": "Choose Your Spread",
        "consult_oracle": "CONSULT THE ORACLE",
        "focus_intention": "Please focus your intention with a question",
        "cards_spoken": "The Cards Have Spoken",
        "reading_cast": "Reading cast on",
        "sacred_spread": "The Sacred Spread",
        "sacred_interpretations": "Sacred Interpretations",
        "position": "Position",
        "meaning": "Meaning",
        "guidance": "Guidance",
        "cosmic_guidance": "Cosmic Guidance",
        "truths": "Remember These Truths",
        "truth_text": '"The oracle cards reflect possibilities, not certainties. Your free will shapes your destiny. Take what resonates, release what does not, and always trust your inner wisdom above all else."',
        "save_reading": "Save This Reading to Your Soul Journal",
        "download_record": "Download Sacred Record",
        "cards_await": "The Cards Await Your Question",
        "instructions": "Enter your sacred question in the space provided, choose your spread, and click 'Consult the Oracle' to receive divine guidance.",
        "trust_process": "Trust the process",
        "listen_intuition": "Listen to your intuition",
        "embrace_wisdom": "Embrace the wisdom that comes",
        "continue_journey": "Continue Your Spiritual Journey",
        "shop_promo": "Explore our collection of spiritual journals and tools to deepen your twin flame journey",
        "footer_text": "Twin Flames Oracle Cards • Complete 35-Card Sacred Deck • Ancient Wisdom for Soul Connections",
        "visit_shop_footer": "Visit Our Shop: Journaling The Universe",
        "disclaimer": "This reading is for spiritual guidance and self-reflection only. Always trust your own judgment in making life decisions.",
        "reflection": "Reflection & Insights",
        "reflection_placeholder": "Record your reflections, insights or action plans...",
        "drawing_animation": "Drawing your oracle cards, please wait...",
        "single_card": "Single Card",
        "three_cards": "Three Cards",
        "celtic_cross": "Celtic Cross"
    }
}

# 神諭牌數據 - 繁體中文和英文，包含對應的emoji
oracle_cards = {
    'zh-TW': [
        {"text": "陰陽平衡", "emoji": "⚖️"},
        {"text": "情緒淨化", "emoji": "🛁"},
        {"text": "高我保護", "emoji": "👼"},
        {"text": "命中注定", "emoji": "💫"},
        {"text": "療癒", "emoji": "💖"},
        {"text": "學習", "emoji": "📚"},
        {"text": "放下我執", "emoji": "🕊️"},
        {"text": "先愛自己", "emoji": "🤱"},
        {"text": "堅守界線", "emoji": "🚧"},
        {"text": "冥想", "emoji": "🧘"},
        {"text": "勇敢前進", "emoji": "🦸"},
        {"text": "休息", "emoji": "🛌"},
        {"text": "安靜", "emoji": "🤫"},
        {"text": "顯化", "emoji": "🌟"},
        {"text": "專注在其他事情上", "emoji": "🔍"},
        {"text": "瞭解對方", "emoji": "👀"},
        {"text": "溝通", "emoji": "🗣️"},
        {"text": "請求揚升大師或天使援助", "emoji": "👼"},
        {"text": "與大自然連結", "emoji": "🌳"},
        {"text": "與人連結", "emoji": "👥"},
        {"text": "與社會連結", "emoji": "🌐"},
        {"text": "藝術創作", "emoji": "🎨"},
        {"text": "文字創作", "emoji": "✍️"},
        {"text": "創造豐盛", "emoji": "💰"},
        {"text": "尋找神聖男性幫助（現實生活行動力）", "emoji": "🦸‍♂️"},
        {"text": "與神聖女性連結（被動，內在豐盛，慈悲，美）", "emoji": "🦸‍♀️"},
        {"text": "與野性女性連結（對潛/無意識世界的感知力）", "emoji": "🐺"},
        {"text": "與神聖男性連結（把潛/無意識世界的智慧帶上去現實世界）", "emoji": "🧙‍♂️"},
        {"text": "雙生需要時間處理他她的課題", "emoji": "⏳"},
        {"text": "雙生尚未準備好進行下一次的相遇", "emoji": "❌"},
        {"text": "雙生暫時無法承擔作為你的伴侶", "emoji": "🚫"},
        {"text": "雙生想跟你說，他她很愛你", "emoji": "💌"},
        {"text": "雙生想跟你說，他她無論如何都會深深支持你", "emoji": "💪"},
        {"text": "雙生想跟你說，他她一直都在你身邊", "emoji": "👫"},
        {"text": "雙生想跟你說，他她在未來等你", "emoji": "🕰️"}
    ],
    'en': [
        {"text": "Yin Yang Balance", "emoji": "⚖️"},
        {"text": "Emotional Purification", "emoji": "🛁"},
        {"text": "Higher Self Protection", "emoji": "👼"},
        {"text": "Destiny", "emoji": "💫"},
        {"text": "Healing", "emoji": "💖"},
        {"text": "Learning", "emoji": "📚"},
        {"text": "Letting Go of Ego", "emoji": "🕊️"},
        {"text": "Love Yourself First", "emoji": "🤱"},
        {"text": "Set Boundaries", "emoji": "🚧"},
        {"text": "Meditation", "emoji": "🧘"},
        {"text": "Move Forward Bravely", "emoji": "🦸"},
        {"text": "Rest", "emoji": "🛌"},
        {"text": "Silence", "emoji": "🤫"},
        {"text": "Manifestation", "emoji": "🌟"},
        {"text": "Focus on Other Things", "emoji": "🔍"},
        {"text": "Understand Each Other", "emoji": "👀"},
        {"text": "Communication", "emoji": "🗣️"},
        {"text": "Ask for Ascended Masters or Angel Assistance", "emoji": "👼"},
        {"text": "Connect with Nature", "emoji": "🌳"},
        {"text": "Connect with People", "emoji": "👥"},
        {"text": "Connect with Society", "emoji": "🌐"},
        {"text": "Artistic Creation", "emoji": "🎨"},
        {"text": "Writing Creation", "emoji": "✍️"},
        {"text": "Create Abundance", "emoji": "💰"},
        {"text": "Seek Divine Masculine Help (Practical Action)", "emoji": "🦸‍♂️"},
        {"text": "Connect with Divine Feminine (Passive, Inner Abundance, Compassion, Beauty)", "emoji": "🦸‍♀️"},
        {"text": "Connect with Wild Feminine (Perception of Subconscious/Unconscious World)", "emoji": "🐺"},
        {"text": "Connect with Divine Masculine (Bring Wisdom from Subconscious to Reality)", "emoji": "🧙‍♂️"},
        {"text": "Twin Needs Time to Handle Their Lessons", "emoji": "⏳"},
        {"text": "Twin is Not Ready for the Next Meeting", "emoji": "❌"},
        {"text": "Twin Cannot Be Your Partner Temporarily", "emoji": "🚫"},
        {"text": "Twin Wants to Tell You: They Love You Very Much", "emoji": "💌"},
        {"text": "Twin Wants to Tell You: They Deeply Support You No Matter What", "emoji": "💪"},
        {"text": "Twin Wants to Tell You: They Are Always By Your Side", "emoji": "👫"},
        {"text": "Twin Wants to Tell You: They Are Waiting for You in the Future", "emoji": "🕰️"}
    ]
}

# 凱爾特十字牌陣位置說明
celtic_cross_positions = {
    'zh-TW': [
        "1. 現狀 - 當前情況的核心",
        "2. 挑戰 - 橫跨在前的障礙",
        "3. 基礎 - 問題的根源",
        "4. 過去 - 最近的過去影響",
        "5. 目標 - 可能的最佳結果",
        "6. 近期未來 - 即將發生的事",
        "7. 自我態度 - 你的觀點和態度",
        "8. 環境 - 外部影響和人際關係",
        "9. 希望與恐懼 - 內在的期望與擔憂",
        "10. 最終結果 - 長期發展"
    ],
    'en': [
        "1. Present - Core of current situation",
        "2. Challenge - Obstacle crossing your path",
        "3. Foundation - Root of the matter",
        "4. Past - Recent past influences",
        "5. Goal - Best possible outcome",
        "6. Near Future - What's coming soon",
        "7. Self Attitude - Your perspective and attitude",
        "8. Environment - External influences and relationships",
        "9. Hopes & Fears - Inner expectations and worries",
        "10. Final Outcome - Long-term development"
    ]
}

# Custom CSS with deep purple theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Noto+Sans+TC:wght@400;500;700&display=swap');
    
    .main-header {
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        font-size: 3.5rem;
        background: linear-gradient(45deg, #8A2BE2, #9370DB, #8A2BE2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(138, 43, 226, 0.3);
        padding-top: 1rem;
    }
    .subtitle {
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        text-align: center;
        color: #D8BFD8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        letter-spacing: 2px;
    }
    .oracle-card {
        background: linear-gradient(145deg, #2D1B69, #3D2A7A);
        border: 2px solid #9370DB;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .oracle-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(147, 112, 219, 0.2);
    }
    .card-image {
        font-size: 4rem;
        margin-bottom: 15px;
        filter: drop-shadow(0 0 10px rgba(147, 112, 219, 0.5));
    }
    .card-name {
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        color: #9370DB;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 10px 0;
    }
    .interpretation-box {
        background: rgba(45, 27, 105, 0.8);
        border: 1px solid #444;
        border-radius: 12px;
        padding: 25px;
        margin: 15px 0;
        backdrop-filter: blur(10px);
        border-left: 4px solid #9370DB;
    }
    .question-box {
        background: rgba(45, 27, 105, 0.6);
        border: 1px solid #444;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        border-top: 2px solid #9370DB;
    }
    .purple-text {
        color: #9370DB;
        font-family: 'Cinzel', 'Noto Sans TC', serif;
    }
    .light-purple-text {
        color: #D8BFD8;
    }
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #9370DB, transparent);
        margin: 30px 0;
    }
    .spread-title {
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        text-align: center;
        color: #9370DB;
        margin: 25px 0;
        font-size: 1.8rem;
    }
    .stButton button {
        background: linear-gradient(45deg, #8A2BE2, #9370DB);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(138, 43, 226, 0.3);
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(138, 43, 226, 0.4);
        background: linear-gradient(45deg, #9370DB, #8A2BE2);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2A1B52 0%, #1A1033 100%);
    }
    
    /* Main background styling */
    .stApp {
        background: linear-gradient(135deg, #1A1033 0%, #2D1B69 50%, #1A1033 100%);
        color: #E6E6FA;
    }
    
    /* Fix the main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Custom link styling */
    .store-link {
        display: inline-block;
        background: linear-gradient(45deg, #8A2BE2, #9370DB);
        color: white !important;
        padding: 10px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        font-weight: 600;
        margin: 10px 0;
        transition: all 0.3s ease;
        text-align: center;
    }
    .store-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(138, 43, 226, 0.4);
        background: linear-gradient(45deg, #9370DB, #8A2BE2);
        color: white;
        text-decoration: none;
    }
    
    /* Shop promotion styling */
    .shop-promotion {
        background: rgba(45, 27, 105, 0.7) !important;
        border: 1px solid #444 !important;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        border-left: 4px solid #9370DB !important;
    }
    
    /* Drawing animation */
    .drawing-animation {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 60px 40px;
        text-align: center;
        background: rgba(45, 27, 105, 0.5);
        border-radius: 20px;
        border: 1px solid rgba(147, 112, 219, 0.3);
        min-height: 400px;
    }
    
    .spinning-card {
        font-size: 5rem;
        animation: spin 2s ease-in-out infinite;
        margin-bottom: 30px;
        filter: drop-shadow(0 0 15px rgba(147, 112, 219, 0.6));
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.2); }
        100% { transform: rotate(360deg) scale(1); }
    }
    
    .pulsing-text {
        animation: pulse 1.5s ease-in-out infinite;
        color: #D8BFD8;
        font-size: 1.3rem;
        margin-top: 20px;
    }
    
    @keyframes pulse {
        0% { opacity: 0.7; }
        50% { opacity: 1; }
        100% { opacity: 0.7; }
    }
    
    /* Fix column alignment to ensure both columns start at the same top position */
    .main .block-container {
        padding-top: 1rem;
    }
    
    .column-container {
        display: flex;
        align-items: flex-start;
        gap: 20px;
    }
    
    .left-column, .right-column {
        flex: 1;
        min-height: 600px;
    }
    
    /* Ensure both columns start at the same vertical position */
    div[data-testid="column"] {
        align-self: flex-start;
    }
    
    /* Spread button styling */
    .spread-option {
        background: rgba(45, 27, 105, 0.6);
        border: 1px solid rgba(147, 112, 219, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        transition: all 0.3s ease;
        cursor: pointer;
        text-align: center;
    }
    .spread-option:hover {
        background: rgba(147, 112, 219, 0.2);
        transform: translateY(-3px);
    }
    .spread-option.selected {
        background: rgba(147, 112, 219, 0.3);
        border: 1px solid #9370DB;
        box-shadow: 0 0 20px rgba(147, 112, 219, 0.3);
    }
</style>
""", unsafe_allow_html=True)

def draw_cards(num_cards, language):
    """抽取指定數量的牌"""
    cards = random.sample(oracle_cards[language], num_cards)
    return cards

def create_download_content(question, cards, spread_type, language, reflection, positions=None):
    """創建下載內容"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if language == 'zh-TW':
        content = f"雙生火焰神諭卡抽牌記錄\n"
        content += f"抽牌時間: {timestamp}\n"
        content += f"問題: {question}\n"
        content += f"牌陣類型: {spread_type}\n"
        content += "=" * 40 + "\n\n"
        
        if spread_type == "凱爾特十字" and positions:
            for i, (position, card) in enumerate(zip(positions, cards)):
                content += f"{position}\n"
                content += f"神諭卡: {card['emoji']} {card['text']}\n\n"
        else:
            for i, card in enumerate(cards, 1):
                content += f"第{i}張牌: {card['emoji']} {card['text']}\n"
        
        content += "\n" + "=" * 40 + "\n"
        content += "我的反思:\n"
        content += reflection + "\n"
        content += "=" * 40 + "\n\n"
        
        content += "來自 @journaling_the_universe 雙生火焰神諭卡\n"
        content += "願這份指引為你帶來光明與力量✨"
        
    else:  # English
        content = f"Twin Flames Oracle Card Reading\n"
        content += f"Reading Time: {timestamp}\n"
        content += f"Question: {question}\n"
        content += f"Spread Type: {spread_type}\n"
        content += "=" * 40 + "\n\n"
        
        if spread_type == "Celtic Cross" and positions:
            for i, (position, card) in enumerate(zip(positions, cards)):
                content += f"{position}\n"
                content += f"Oracle Card: {card['emoji']} {card['text']}\n\n"
        else:
            for i, card in enumerate(cards, 1):
                content += f"Card {i}: {card['emoji']} {card['text']}\n"
        
        content += "\n" + "=" * 40 + "\n"
        content += "My Reflection:\n"
        content += reflection + "\n"
        content += "=" * 40 + "\n\n"
        
        content += "From @journaling_the_universe Twin Flames Oracle Cards\n"
        content += "May this guidance bring you light and strength✨"
    
    return content

def main():
    # Initialize session state for language
    if 'language' not in st.session_state:
        st.session_state.language = 'zh-TW'
    
    # Language selector in sidebar
    with st.sidebar:
        lang = st.selectbox("🌐 語言 / Language", ["繁體中文", "English"], 
                           index=0 if st.session_state.language == 'zh-TW' else 1)
        st.session_state.language = 'zh-TW' if lang == "繁體中文" else 'en'
    
    # Get current language texts
    t = texts[st.session_state.language]
    
    # Elegant header
    st.markdown(f'<h1 class="main-header">{t["app_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{t["app_subtitle"]}</p>', unsafe_allow_html=True)
    
    # Sidebar with elegant design
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px 0;'>
            <div style='font-size: 3rem; margin-bottom: 10px;'>🌙</div>
            <h2 style='font-family: Cinzel, serif; color: #9370DB;'>{t["sidebar_title"]}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(147, 112, 219, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #9370DB; font-family: Cinzel, serif;'>✨ {t["preparation"]}</h4>
            <p style='font-size: 0.9rem;'>{t["preparation_text"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(147, 112, 219, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #9370DB; font-family: Cinzel, serif;'>📜 {t["spread_meanings"]}</h4>
            <ul style='font-size: 0.9rem; padding-left: 20px;'>
                <li><strong>{t["spread_single"]}</strong></li>
                <li><strong>{t["spread_three"]}</strong></li>
                <li><strong>{t["spread_celtic"]}</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Shop link in sidebar
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(147, 112, 219, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #9370DB; font-family: Cinzel, serif;'>🛍️ {t["visit_shop"]}</h4>
            <p style='font-size: 0.9rem;'>{t["shop_text"]}</p>
            <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
               target="_blank" class="store-link" style='display: block; text-align: center;'>
               🌟 {t["enter_shop"]}
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Deck information
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(147, 112, 219, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #9370DB; font-family: Cinzel, serif;'>🃏 {t["deck_info"]}</h4>
            <p style='font-size: 0.9rem;'>{t["deck_text"]}</p>
            <ul style='font-size: 0.8rem; padding-left: 20px;'>
                <li>{t["deck_categories"]}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
        <div style='text-align: center; color: #D8BFD8; font-size: 0.8rem;'>
            <p>{t["trust_intuition"]}</p>
        </div>
        """, unsafe_allow_html=True)

    # Create two column layout with proper alignment
    left_col, right_col = st.columns([1, 1.5], gap="large")
    
    # Left column - Question and spread selection
    with left_col:
        # Question input
        st.markdown(f"### 🌟 {t['sacred_question']}")
        question = st.text_area(
            "",
            placeholder=t["question_placeholder"],
            height=150,
            help=t["preparation_text"],
            key="question_input"
        )
        
        # Spread selection
        st.markdown(f"### 📜 {t['choose_spread']}")
        
        # Spread options as clickable cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"## ✨\n### {t['single_card']}", use_container_width=True, key="single"):
                st.session_state.spread_choice = t['single_card']
        
        with col2:
            if st.button(f"## 🔮\n### {t['three_cards']}", use_container_width=True, key="three"):
                st.session_state.spread_choice = t['three_cards']
        
        with col3:
            if st.button(f"## ♱\n### {t['celtic_cross']}", use_container_width=True, key="celtic"):
                st.session_state.spread_choice = t['celtic_cross']
        
        # Initialize spread choice
        if 'spread_choice' not in st.session_state:
            st.session_state.spread_choice = None
        
        # Show selected spread
        if st.session_state.spread_choice:
            st.markdown(f"### 🎯 {t['position']}: {st.session_state.spread_choice}")
        
        # Consult oracle button
        st.markdown("---")
        draw_disabled = not (question and st.session_state.spread_choice)
        draw_button = st.button(f"🌀 {t['consult_oracle']}", 
                              use_container_width=True, 
                              disabled=draw_disabled,
                              type="primary")

    # Right column - Results and animation
    with right_col:
        # Handle drawing animation and results
        if draw_button and question and st.session_state.spread_choice:
            # Show drawing animation
            st.markdown(f"""
            <div class="drawing-animation">
                <div class="spinning-card">🔮</div>
                <div class="pulsing-text">{t['drawing_animation']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Wait for 2.5 seconds
            time.sleep(2.5)
            
            # Determine number of cards based on spread choice
            if st.session_state.spread_choice == t['single_card']:
                num_cards = 1
                spread_type = t['single_card']
            elif st.session_state.spread_choice == t['three_cards']:
                num_cards = 3
                spread_type = t['three_cards']
            else:  # Celtic Cross
                num_cards = 10
                spread_type = t['celtic_cross']
            
            # Draw cards
            cards = draw_cards(num_cards, st.session_state.language)
            
            # Store in session state
            st.session_state.cards = cards
            st.session_state.question = question
            st.session_state.spread_type = spread_type
            st.session_state.timestamp = datetime.datetime.now()
            st.session_state.show_results = True
            
            # Rerun to show results
            st.rerun()
        
        # Display results if available
        if 'show_results' in st.session_state and st.session_state.show_results:
            cards = st.session_state.cards
            question = st.session_state.question
            spread_type = st.session_state.spread_type
            
            # Display reading with elegant layout
            st.markdown(f"## 🔮 {t['cards_spoken']}")
            
            # Question and timestamp in elegant box
            st.markdown(f"""
            <div class="question-box">
                <h4 class="purple-text">{t['sacred_question']}</h4>
                <p style='font-size: 1.1rem; font-style: italic;'>"{question}"</p>
                <p class="light-purple-text" style='font-size: 0.9rem; margin-top: 10px;'>
                {t['reading_cast']} {st.session_state.timestamp.strftime("%Y-%m-%d %H:%M")}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Cards display
            st.markdown(f'<div class="spread-title">{t["sacred_spread"]}</div>', unsafe_allow_html=True)
            
            # Create columns for cards based on spread type
            if len(cards) == 1:
                # Single card
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    card = cards[0]
                    st.markdown(f"""
                    <div class="oracle-card">
                        <div class="card-image">{card['emoji']}</div>
                        <div class="card-name">{card['text']}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            elif len(cards) == 3:
                # Three cards
                cols = st.columns(3)
                positions = ["過去/基礎", "現在/挑戰", "未來/指引"] if st.session_state.language == 'zh-TW' else ["Past/Foundation", "Present/Challenge", "Future/Guidance"]
                
                for i, (col, card) in enumerate(zip(cols, cards)):
                    with col:
                        st.markdown(f"""
                        <div class="oracle-card">
                            <div class="card-image">{card['emoji']}</div>
                            <div class="card-name">{card['text']}</div>
                            <div style='color: #D8BFD8; font-size: 0.9rem; margin: 5px 0;'>{positions[i]}</div>
                        </div>
                        """, unsafe_allow_html=True)
            
            else:  # Celtic Cross (10 cards)
                # First row: positions 1-3
                cols = st.columns(3)
                positions = celtic_cross_positions[st.session_state.language]
                
                for i in range(3):
                    with cols[i]:
                        card = cards[i]
                        st.markdown(f"""
                        <div class="oracle-card">
                            <div class="card-image">{card['emoji']}</div>
                            <div class="card-name">{card['text']}</div>
                            <div style='color: #D8BFD8; font-size: 0.8rem; margin: 5px 0;'>{positions[i]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Second row: positions 4-6
                cols = st.columns(3)
                for i in range(3, 6):
                    with cols[i-3]:
                        card = cards[i]
                        st.markdown(f"""
                        <div class="oracle-card">
                            <div class="card-image">{card['emoji']}</div>
                            <div class="card-name">{card['text']}</div>
                            <div style='color: #D8BFD8; font-size: 0.8rem; margin: 5px 0;'>{positions[i]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Third row: positions 7-10
                cols = st.columns(4)
                for i in range(6, 10):
                    with cols[i-6]:
                        card = cards[i]
                        st.markdown(f"""
                        <div class="oracle-card">
                            <div class="card-image">{card['emoji']}</div>
                            <div class="card-name">{card['text']}</div>
                            <div style='color: #D8BFD8; font-size: 0.8rem; margin: 5px 0;'>{positions[i]}</div>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Divider
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            # Reflection area
            st.markdown(f"## 📝 {t['reflection']}")
            reflection = st.text_area(
                "",
                placeholder=t["reflection_placeholder"],
                height=150,
                key="reflection"
            )
            
            # Download button
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                # Create download content
                positions_to_use = None
                if spread_type == t['celtic_cross']:
                    positions_to_use = celtic_cross_positions[st.session_state.language]
                
                download_content = create_download_content(
                    question,
                    cards, 
                    spread_type, 
                    st.session_state.language, 
                    reflection if reflection else ("(未填寫反思)" if st.session_state.language == 'zh-TW' else "(No reflection)"),
                    positions_to_use
                )
                
                # Download button
                st.download_button(
                    label=f"📥 {t['download_record']}",
                    data=download_content,
                    file_name=f"雙生火焰神諭卡_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        
        else:
            # Initial state when no reading has been done
            st.markdown(f"""
            <div style='text-align: center; padding: 40px 20px;'>
                <div style='font-size: 5rem; margin-bottom: 20px;'>🔮</div>
                <h2 style='color: #9370DB; font-family: Cinzel, serif;'>{t['cards_await']}</h2>
                <p style='color: #D8BFD8; font-size: 1.1rem; margin: 20px 0;'>
                {t['instructions']}
                </p>
                <div style='color: #9370DB; font-style: italic; margin-top: 30px;'>
                <p>✨ {t['trust_process']} ✨</p>
                <p>✨ {t['listen_intuition']} ✨</p>
                <p>✨ {t['embrace_wisdom']} ✨</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Shop promotion
            st.markdown(f"""
            <div class="shop-promotion">
                <h4 style='color: #9370DB; font-family: Cinzel, serif; text-align: center;'>📓 {t['continue_journey']}</h4>
                <p style='color: #D8BFD8; text-align: center;'>{t['shop_promo']}</p>
                <div style='text-align: center;'>
                    <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
                       target="_blank" class="store-link">
                       🛍️ {t['enter_shop']}
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Show warnings if needed
    if draw_button and not question:
        st.warning(f"⚠️ {t['focus_intention']}")

    if draw_button and not st.session_state.spread_choice:
        st.warning("⚠️ 請先選擇牌陣" if st.session_state.language == 'zh-TW' else "⚠️ Please select a spread first")

    # Elegant footer with shop link
    st.markdown(f"""
    <div style='text-align: center; margin-top: 50px; padding: 20px; color: #9370DB; border-top: 1px solid #333;'>
        <p>{t['footer_text']}</p>
        <p style='font-size: 0.9rem; margin: 15px 0;'>
            <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
               target="_blank" style='color: #9370DB; text-decoration: none; font-family: Cinzel, serif;'>
               🌟 {t['visit_shop_footer']}
            </a>
        </p>
        <p style='font-size: 0.8rem; color: #D8BFD8;'>{t['disclaimer']}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
