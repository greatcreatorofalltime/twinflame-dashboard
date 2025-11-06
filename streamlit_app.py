import streamlit as st
import random
import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Twin Flame Oracle",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language texts dictionary
texts = {
    "en": {
        "app_title": "TWIN FLAME ORACLE",
        "app_subtitle": "Divine Guidance • Soul Connection • Spiritual Awakening",
        "sidebar_title": "Sacred Space",
        "preparation": "Preparation",
        "preparation_text": "Center yourself, breathe deeply, and focus your intention on your twin flame journey.",
        "spread_meanings": "Spread Meanings",
        "spread_single": "Single Card: Daily guidance",
        "spread_three": "Three Cards: Situation, Action, Outcome",
        "spread_celtic": "Celtic Cross: Deep soul insight",
        "visit_shop": "Visit Our Shop",
        "shop_text": "Explore spiritual journals, oracle guides, and mystical tools in our store.",
        "enter_shop": "Enter the Cosmic Journal",
        "deck_info": "Complete Twin Flame Oracle Deck",
        "deck_text": "This reading uses the specially designed twin flame oracle deck including:",
        "deck_categories": "Divine guidance, healing, connection, and messages",
        "trust_intuition": "Trust your intuition above all else. The cards are mirrors, not masters.",
        "sacred_question": "Your Sacred Question",
        "question_placeholder": "Whisper your question to the universe about your twin flame journey...\n\nWhat guidance do I need for our connection?\nWhat is the next step in our journey?\nWhat do I need to understand about this situation?",
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
        "category": "Category",
        "cosmic_guidance": "Cosmic Guidance",
        "truths": "Remember These Truths",
        "truth_text": '"The cards reflect possibilities, not certainties. Your free will shapes your destiny. Take what resonates, release what does not, and always trust your inner wisdom above all else."',
        "save_reading": "Save This Reading to Your Spiritual Journal",
        "download_record": "Download Sacred Record",
        "cards_await": "The Cards Await Your Question",
        "instructions": "Enter your sacred question in the space provided, choose your spread, and click 'Consult the Oracle' to receive divine guidance.",
        "trust_process": "Trust the process",
        "listen_intuition": "Listen to your intuition",
        "embrace_wisdom": "Embrace the wisdom that comes",
        "continue_journey": "Continue Your Spiritual Journey",
        "shop_promo": "Explore our collection of spiritual journals and tools to deepen your practice",
        "footer_text": "Twin Flame Oracle • Specially Designed Deck • Divine Guidance for Soul Connections",
        "visit_shop_footer": "Visit Our Shop: Cosmic Journal",
        "disclaimer": "This reading is for spiritual guidance and self-reflection only. Always trust your own judgment in making life decisions.",
        # Spread options for dropdown
        "spread_single_option": "Single Card • Daily Guidance",
        "spread_three_option": "Three Cards • Situation, Action, Outcome", 
        "spread_celtic_option": "Celtic Cross • Comprehensive Insight",
        # Position names for spreads
        "position_single": ["Current Guidance"],
        "position_three": ["Situation", "Action Needed", "Outcome"],
        "position_celtic": ["Present Situation", "Immediate Challenge", "Distant Past", "Recent Past", "Higher Self", "Near Future", "Your Approach", "External Influences", "Hopes & Fears", "Final Outcome"]
    },
    "zh": {
        "app_title": "雙生火焰神諭卡",
        "app_subtitle": "神聖指引 • 靈魂連結 • 靈性覺醒",
        "sidebar_title": "神聖空間",
        "preparation": "準備工作",
        "preparation_text": "靜心凝神，深呼吸，將意圖專注於你的雙生火焰旅程上。",
        "spread_meanings": "牌陣意義",
        "spread_single": "單張牌：每日指引",
        "spread_three": "三張牌：情況、行動、結果",
        "spread_celtic": "凱爾特十字：深度靈魂洞察",
        "visit_shop": "訪問我們的商店",
        "shop_text": "探索我們商店中的靈性日記、神諭卡指南和神秘工具。",
        "enter_shop": "進入宇宙日記",
        "deck_info": "完整雙生火焰神諭卡牌組",
        "deck_text": "本次占卜使用特別設計的雙生火焰神諭卡牌組，包括：",
        "deck_categories": "神聖指引、療癒、連結和訊息",
        "trust_intuition": "最重要的是信任你的直覺。神諭卡是鏡子，不是主人。",
        "sacred_question": "你的神聖問題",
        "question_placeholder": "向宇宙輕聲訴說你關於雙生火焰旅程的問題...\n\n我們的連結需要什麼指引？\n我們旅程的下一步是什麼？\n關於這個情況我需要理解什麼？",
        "choose_spread": "選擇你的牌陣",
        "consult_oracle": "請教神諭",
        "focus_intention": "請專注你的意圖，提出一個問題",
        "cards_spoken": "神諭卡已經發言",
        "reading_cast": "占卜時間",
        "sacred_spread": "神聖牌陣",
        "sacred_interpretations": "神聖解讀",
        "position": "位置",
        "meaning": "意義",
        "guidance": "指引",
        "category": "類別",
        "cosmic_guidance": "宇宙指引",
        "truths": "記住這些真理",
        "truth_text": '"神諭卡反映可能性，而非確定性。你的自由意志塑造你的命運。接受引起共鳴的，放下不適合的，永遠信任你內在的智慧。"',
        "save_reading": "將此占卜保存到你的靈性日記",
        "download_record": "下載神聖記錄",
        "cards_await": "神諭卡等待你的問題",
        "instructions": "在提供的空間輸入你的神聖問題，選擇牌陣，然後點擊'請教神諭'接收神聖指引。",
        "trust_process": "信任過程",
        "listen_intuition": "聆聽直覺",
        "embrace_wisdom": "擁抱到來的智慧",
        "continue_journey": "繼續你的靈性旅程",
        "shop_promo": "探索我們的靈性日記和工具收藏，深化你的修行",
        "footer_text": "雙生火焰神諭卡 • 特別設計牌組 • 靈魂連結的神聖指引",
        "visit_shop_footer": "訪問我們的商店：宇宙日記",
        "disclaimer": "此占卜僅供靈性指引和自我反思使用。在做出人生決定時，請始終信任你自己的判斷。",
        # Spread options for dropdown
        "spread_single_option": "單張牌 • 每日指引",
        "spread_three_option": "三張牌 • 情況、行動、結果", 
        "spread_celtic_option": "凱爾特十字 • 深度靈魂洞察",
        # Position names for spreads
        "position_single": ["當前指引"],
        "position_three": ["情況", "需要採取的行動", "結果"],
        "position_celtic": ["當前狀況", "立即挑戰", "遙遠過去", "近期過去", "高我指引", "近期未來", "你的態度", "外部影響", "希望與恐懼", "最終結果"]
    }
}

# Custom CSS with deep purple theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=MedievalSharp&family=Noto+Sans+TC:wght@400;500;700&display=swap');
    
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
        color: #d8d8d8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        letter-spacing: 2px;
    }
    .oracle-card {
        background: linear-gradient(145deg, #2d1b4e, #3d2963);
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
        background: rgba(45, 27, 78, 0.8);
        border: 1px solid #555;
        border-radius: 12px;
        padding: 25px;
        margin: 15px 0;
        backdrop-filter: blur(10px);
        border-left: 4px solid #9370DB;
    }
    .question-box {
        background: rgba(45, 27, 78, 0.6);
        border: 1px solid #555;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        border-top: 2px solid #9370DB;
    }
    .purple-text {
        color: #9370DB;
        font-family: 'Cinzel', 'Noto Sans TC', serif;
    }
    .silver-text {
        color: #d8d8d8;
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
        color: #1a1a2e;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-family: 'Cinzel', 'Noto Sans TC', serif;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(147, 112, 219, 0.3);
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(147, 112, 219, 0.4);
        background: linear-gradient(45deg, #9370DB, #8A2BE2);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1a1a2e 0%, #2d1b4e 100%);
    }
    
    /* Main background styling */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #2d1b4e 100%);
        color: #e6e6e6;
    }
    
    /* Fix the main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Ensure proper spacing */
    .css-1d391kg {
        padding-top: 0rem;
    }
    
    /* Custom link styling */
    .store-link {
        display: inline-block;
        background: linear-gradient(45deg, #8A2BE2, #9370DB);
        color: #1a1a2e !important;
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
        box-shadow: 0 6px 20px rgba(147, 112, 219, 0.4);
        background: linear-gradient(45deg, #9370DB, #8A2BE2);
        color: #1a1a2e;
        text-decoration: none;
    }
    
    /* Shop promotion styling that blends with theme */
    .shop-promotion {
        background: rgba(45, 27, 78, 0.7) !important;
        border: 1px solid #555 !important;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        border-left: 4px solid #9370DB !important;
    }
</style>
""", unsafe_allow_html=True)

# Twin Flame Oracle Cards Database
twin_flame_cards = {
    "陰陽平衡": {
        "name_en": "Yin Yang Balance", 
        "meaning": "Harmony between masculine and feminine energies within and in your connection.", 
        "meaning_zh": "內在與連結中男性能量與女性能量的和諧平衡。",
        "advice": "Focus on balancing your own inner energies before seeking balance in the connection.",
        "advice_zh": "在尋求連結中的平衡之前，先專注於平衡你自己的內在能量。",
        "image": "⚖️", 
        "category": "Balance",
        "category_zh": "平衡"
    },
    "情緒淨化": {
        "name_en": "Emotional Purification", 
        "meaning": "Release old emotional patterns and cleanse your emotional body.", 
        "meaning_zh": "釋放舊有情緒模式，淨化你的情緒體。",
        "advice": "Allow yourself to feel and release emotions without judgment.",
        "advice_zh": "允許自己感受並釋放情緒，不加評判。",
        "image": "💧", 
        "category": "Healing",
        "category_zh": "療癒"
    },
    "高我保護": {
        "name_en": "Higher Self Protection", 
        "meaning": "Your higher self is protecting you and guiding you on this journey.", 
        "meaning_zh": "你的高我正在保護你並引導你走這段旅程。",
        "advice": "Trust that you are always protected on a soul level.",
        "advice_zh": "相信你在靈魂層面上總是受到保護。",
        "image": "🛡️", 
        "category": "Protection",
        "category_zh": "保護"
    },
    "命中注定": {
        "name_en": "Divine Timing", 
        "meaning": "Everything is unfolding according to divine timing and purpose.", 
        "meaning_zh": "一切都在按照神聖時機和目的展開。",
        "advice": "Practice patience and trust in the divine plan.",
        "advice_zh": "練習耐心，信任神聖計劃。",
        "image": "💫", 
        "category": "Divine Order",
        "category_zh": "神聖秩序"
    },
    "療癒": {
        "name_en": "Healing", 
        "meaning": "Deep healing is occurring on multiple levels of your being.", 
        "meaning_zh": "深層療癒正在你存在的多個層面發生。",
        "advice": "Be gentle with yourself during this healing process.",
        "advice_zh": "在這個療癒過程中對自己溫柔一些。",
        "image": "🌿", 
        "category": "Healing",
        "category_zh": "療癒"
    },
    "學習": {
        "name_en": "Learning", 
        "meaning": "Important soul lessons are being presented to you now.", 
        "meaning_zh": "重要的靈魂課題現在正呈現在你面前。",
        "advice": "Embrace the lessons with an open heart and mind.",
        "advice_zh": "以開放的心和思想擁抱這些課題。",
        "image": "📚", 
        "category": "Growth",
        "category_zh": "成長"
    },
    "放下我執": {
        "name_en": "Release Ego", 
        "meaning": "Time to release ego attachments and surrender to higher wisdom.", 
        "meaning_zh": "是時候放下自我執著，臣服於更高智慧。",
        "advice": "Practice humility and surrender control to the universe.",
        "advice_zh": "練習謙卑，將控制權交給宇宙。",
        "image": "🕊️", 
        "category": "Surrender",
        "category_zh": "臣服"
    },
    "先愛自己": {
        "name_en": "Love Yourself First", 
        "meaning": "Your primary relationship must be with yourself before union with another.", 
        "meaning_zh": "在與他人結合之前，你首要的關係必須是與自己的關係。",
        "advice": "Cultivate self-love and self-acceptance daily.",
        "advice_zh": "每天培養自愛和自我接納。",
        "image": "💖", 
        "category": "Self-Love",
        "category_zh": "自愛"
    },
    "堅守界線": {
        "name_en": "Maintain Boundaries", 
        "meaning": "Healthy boundaries are essential for your spiritual growth and wellbeing.", 
        "meaning_zh": "健康的界線對你的靈性成長和幸福至關重要。",
        "advice": "Honor your needs and communicate your boundaries clearly.",
        "advice_zh": "尊重你的需求，清晰溝通你的界線。",
        "image": "🚧", 
        "category": "Boundaries",
        "category_zh": "界線"
    },
    "冥想": {
        "name_en": "Meditation", 
        "meaning": "Regular meditation will bring clarity and connection to your higher guidance.", 
        "meaning_zh": "定期冥想將帶來清晰並連結你的更高指引。",
        "advice": "Create a daily meditation practice, even if brief.",
        "advice_zh": "建立每日冥想練習，即使時間很短。",
        "image": "🧘", 
        "category": "Practice",
        "category_zh": "練習"
    },
    "勇敢前進": {
        "name_en": "Brave Forward", 
        "meaning": "Have courage to move forward on your path, even when it's challenging.", 
        "meaning_zh": "有勇氣在你的道路上向前邁進，即使面臨挑戰。",
        "advice": "Trust that courage comes from taking the first step.",
        "advice_zh": "相信勇氣來自於邁出第一步。",
        "image": "🚀", 
        "category": "Courage",
        "category_zh": "勇氣"
    },
    "休息": {
        "name_en": "Rest", 
        "meaning": "Your soul needs rest and integration time.", 
        "meaning_zh": "你的靈魂需要休息和整合的時間。",
        "advice": "Honor your need for rest without guilt.",
        "advice_zh": "尊重你對休息的需求，不要感到愧疚。",
        "image": "😴", 
        "category": "Self-Care",
        "category_zh": "自我照顧"
    },
    "安靜": {
        "name_en": "Stillness", 
        "meaning": "In the quiet spaces, you will hear your soul's wisdom.", 
        "meaning_zh": "在安靜的空間中，你會聽到你靈魂的智慧。",
        "advice": "Create regular moments of silence in your day.",
        "advice_zh": "在一天中創造規律的靜默時刻。",
        "image": "🤫", 
        "category": "Inner Peace",
        "category_zh": "內在平靜"
    },
    "顯化": {
        "name_en": "Manifestation", 
        "meaning": "Your thoughts and emotions are powerful creators of your reality.", 
        "meaning_zh": "你的思想和情緒是你現實的強大創造者。",
        "advice": "Focus on what you want to create, not what you fear.",
        "advice_zh": "專注於你想要創造的，而不是你害怕的。",
        "image": "✨", 
        "category": "Creation",
        "category_zh": "創造"
    },
    "專注在其他事情上": {
        "name_en": "Focus Elsewhere", 
        "meaning": "Redirect your energy toward your personal growth and life purpose.", 
        "meaning_zh": "將你的能量重新導向你的個人成長和生命目的。",
        "advice": "Invest in yourself and your own journey.",
        "advice_zh": "投資於你自己和你自己的旅程。",
        "image": "🎯", 
        "category": "Focus",
        "category_zh": "專注"
    },
    "瞭解對方": {
        "name_en": "Understand Each Other", 
        "meaning": "Seek to understand your twin's journey and perspective with compassion.", 
        "meaning_zh": "以同情心尋求理解你雙生的旅程和觀點。",
        "advice": "Practice empathy without losing yourself.",
        "advice_zh": "練習同理心，同時不失去自己。",
        "image": "👀", 
        "category": "Understanding",
        "category_zh": "理解"
    },
    "溝通": {
        "name_en": "Communication", 
        "meaning": "Open, honest communication is needed, whether internal or external.", 
        "meaning_zh": "需要開放、誠實的溝通，無論是內在還是外在。",
        "advice": "Speak your truth with love and compassion.",
        "advice_zh": "用愛和同情心說出你的真相。",
        "image": "💬", 
        "category": "Communication",
        "category_zh": "溝通"
    },
    "請求揚升大師或天使援助": {
        "name_en": "Ask for Ascended Masters or Angel Assistance", 
        "meaning": "Divine assistance is available when you ask for it.", 
        "meaning_zh": "當你請求時，神聖援助是可用的。",
        "advice": "Don't hesitate to ask for spiritual support.",
        "advice_zh": "不要猶豫請求靈性支持。",
        "image": "👼", 
        "category": "Divine Assistance",
        "category_zh": "神聖援助"
    },
    "與大自然連結": {
        "name_en": "Connect with Nature", 
        "meaning": "Nature will ground and recharge your energy.", 
        "meaning_zh": "大自然將使你接地並補充你的能量。",
        "advice": "Spend time in nature regularly to reconnect.",
        "advice_zh": "定期花時間在大自然中重新連結。",
        "image": "🌳", 
        "category": "Connection",
        "category_zh": "連結"
    },
    "與人連結": {
        "name_en": "Connect with People", 
        "meaning": "Meaningful connections with others support your journey.", 
        "meaning_zh": "與他人的有意義連結支持你的旅程。",
        "advice": "Nurture supportive relationships in your life.",
        "advice_zh": "培養生活中支持性的關係。",
        "image": "👥", 
        "category": "Connection",
        "category_zh": "連結"
    },
    "與社會連結": {
        "name_en": "Connect with Society", 
        "meaning": "Your journey has purpose within the larger collective.", 
        "meaning_zh": "你的旅程在更大的集體中具有目的。",
        "advice": "Find ways to contribute your gifts to the world.",
        "advice_zh": "找到方法將你的天賦貢獻給世界。",
        "image": "🏙️", 
        "category": "Purpose",
        "category_zh": "目的"
    },
    "藝術創作": {
        "name_en": "Artistic Creation", 
        "meaning": "Creative expression will help process and transmute energy.", 
        "meaning_zh": "創造性表達將幫助處理和轉化能量。",
        "advice": "Express your journey through creative outlets.",
        "advice_zh": "通過創造性出口表達你的旅程。",
        "image": "🎨", 
        "category": "Expression",
        "category_zh": "表達"
    },
    "文字創作": {
        "name_en": "Writing", 
        "meaning": "Writing will bring clarity and healing to your journey.", 
        "meaning_zh": "寫作將為你的旅程帶來清晰和療癒。",
        "advice": "Keep a journal of your thoughts and experiences.",
        "advice_zh": "記錄你的思想和經歷日記。",
        "image": "📝", 
        "category": "Expression",
        "category_zh": "表達"
    },
    "創造豐盛": {
        "name_en": "Create Abundance", 
        "meaning": "Your spiritual work creates abundance on all levels.", 
        "meaning_zh": "你的靈性工作在所有層面創造豐盛。",
        "advice": "Trust that your needs will be met as you follow your path.",
        "advice_zh": "相信當你跟隨你的道路時，你的需求將會得到滿足。",
        "image": "💰", 
        "category": "Abundance",
        "category_zh": "豐盛"
    },
    "尋找神聖男性幫助（現實生活行動力）": {
        "name_en": "Seek Divine Masculine Help (Practical Action)", 
        "meaning": "The divine masculine energy supports practical action and manifestation.", 
        "meaning_zh": "神聖男性能量支持實際行動和顯化。",
        "advice": "Take practical steps toward your goals.",
        "advice_zh": "朝著你的目標採取實際步驟。",
        "image": "🦸‍♂️", 
        "category": "Action",
        "category_zh": "行動"
    },
    "與神聖女性連結（被動，內在豐盛，慈悲，美）": {
        "name_en": "Connect with Divine Feminine (Receptivity, Inner Abundance, Compassion, Beauty)", 
        "meaning": "The divine feminine brings receptivity, inner abundance, compassion and beauty.", 
        "meaning_zh": "神聖女性帶來接納性、內在豐盛、同情心和美麗。",
        "advice": "Cultivate receptivity and self-compassion.",
        "advice_zh": "培養接納性和自我同情。",
        "image": "🦸‍♀️", 
        "category": "Receptivity",
        "category_zh": "接納"
    },
    "與野性女性連結（對潛/無意識世界的感知力）": {
        "name_en": "Connect with Wild Feminine (Perception of Subconscious/Unconscious World)", 
        "meaning": "The wild feminine connects you to intuitive wisdom and subconscious realms.", 
        "meaning_zh": "野性女性將你連結到直覺智慧和潛意識領域。",
        "advice": "Trust your dreams, intuition, and inner knowing.",
        "advice_zh": "信任你的夢境、直覺和內在知曉。",
        "image": "🐺", 
        "category": "Intuition",
        "category_zh": "直覺"
    },
    "與神聖男性連結（把潛/無意識世界的智慧帶上去現實世界）": {
        "name_en": "Connect with Divine Masculine (Bring Subconscious Wisdom to Reality)", 
        "meaning": "The divine masculine helps bring subconscious wisdom into practical reality.", 
        "meaning_zh": "神聖男性幫助將潛意識智慧帶入實際現實。",
        "advice": "Ground your spiritual insights into daily life.",
        "advice_zh": "將你的靈性洞察落地到日常生活中。",
        "image": "🧙‍♂️", 
        "category": "Integration",
        "category_zh": "整合"
    },
    "雙生需要時間處理他她的課題": {
        "name_en": "Twin Needs Time to Process Their Lessons", 
        "meaning": "Your twin flame needs time and space for their own soul growth.", 
        "meaning_zh": "你的雙生火焰需要時間和空間進行他們自己的靈魂成長。",
        "advice": "Respect their journey and focus on your own growth.",
        "advice_zh": "尊重他們的旅程，專注於你自己的成長。",
        "image": "⏳", 
        "category": "Patience",
        "category_zh": "耐心"
    },
    "雙生尚未準備好進行下一次的相遇": {
        "name_en": "Twin Isn't Ready for Next Meeting", 
        "meaning": "Your twin flame is not yet ready for the next phase of connection.", 
        "meaning_zh": "你的雙生火焰尚未準備好進入連結的下一個階段。",
        "advice": "Trust divine timing and continue your own preparation.",
        "advice_zh": "信任神聖時機，繼續你自己的準備。",
        "image": "❌", 
        "category": "Timing",
        "category_zh": "時機"
    },
    "雙生暫時無法承擔作為你的伴侶": {
        "name_en": "Twin Temporarily Cannot Be Your Partner", 
        "meaning": "Your twin flame currently cannot fulfill the role of partner in your life.", 
        "meaning_zh": "你的雙生火焰目前無法在你生活中承擔伴侶的角色。",
        "advice": "Find completeness within yourself rather than seeking it externally.",
        "advice_zh": "在你內在找到完整，而不是向外尋求。",
        "image": "💔", 
        "category": "Independence",
        "category_zh": "獨立"
    },
    "雙生想跟你說，他她很愛你": {
        "name_en": "Twin Wants to Tell You They Love You", 
        "meaning": "Your twin flame holds deep love for you in their heart.", 
        "meaning_zh": "你的雙生火焰在心中對你懷有深深的愛。",
        "advice": "Feel this love energetically without needing external validation.",
        "advice_zh": "在能量上感受這份愛，不需要外部確認。",
        "image": "💕", 
        "category": "Love",
        "category_zh": "愛"
    },
    "雙生想跟你說，他她無論如何都會深深支持你": {
        "name_en": "Twin Wants to Tell You They Deeply Support You", 
        "meaning": "Your twin flame offers unconditional support for your journey.", 
        "meaning_zh": "你的雙生火焰為你的旅程提供無條件的支持。",
        "advice": "Feel supported on a soul level, regardless of physical circumstances.",
        "advice_zh": "在靈魂層面上感受支持，無論物理情況如何。",
        "image": "💞", 
        "category": "Support",
        "category_zh": "支持"
    },
    "雙生想跟你說，他她一直都在你身邊": {
        "name_en": "Twin Wants to Tell You They're Always With You", 
        "meaning": "Your twin flame is always connected to you on a soul level.", 
        "meaning_zh": "你的雙生火焰在靈魂層面上總是與你連結。",
        "advice": "Feel their presence in your heart and in quiet moments.",
        "advice_zh": "在你的心中和安靜時刻感受他們的存在。",
        "image": "👥", 
        "category": "Connection",
        "category_zh": "連結"
    },
    "雙生想跟你說，他她在未來等你。": {
        "name_en": "Twin Wants to Tell You They're Waiting for You in the Future", 
        "meaning": "Your reunion is destined in divine timing when you're both ready.", 
        "meaning_zh": "當你們都準備好時，你們的重聚在神聖時機中是注定的。",
        "advice": "Focus on becoming the version of yourself ready for union.",
        "advice_zh": "專注於成為準備好結合的那個版本的自己。",
        "image": "🔮", 
        "category": "Future",
        "category_zh": "未來"
    }
}

def get_oracle_reading(question, spread_type, language):
    """Generate an oracle reading based on question and spread type"""
    cards = random.sample(list(twin_flame_cards.items()), spread_type)
    reading = []
    
    for i, (card_name, card_data) in enumerate(cards):
        # Choose language-specific content
        if language == 'zh':
            card_display_name = card_name
            meaning = card_data["meaning_zh"]
            advice = card_data["advice_zh"]
            category = card_data["category_zh"]
        else:
            card_display_name = card_data["name_en"]
            meaning = card_data["meaning"]
            advice = card_data["advice"]
            category = card_data["category"]
        
        reading.append({
            "card": card_display_name,
            "original_name": card_name,
            "meaning": meaning,
            "advice": advice,
            "image": card_data["image"],
            "position": i + 1,
            "category": category
        })
    
    return reading

def main():
    # Initialize session state for language
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    # Language selector in sidebar
    with st.sidebar:
        st.markdown("### 🌐 Language / 語言")
        lang = st.radio("", ["English", "中文"], index=0 if st.session_state.language == 'en' else 1, label_visibility="collapsed")
        st.session_state.language = 'en' if lang == "English" else 'zh'
    
    # Get current language texts
    t = texts[st.session_state.language]
    
    # Elegant header
    st.markdown(f'<h1 class="main-header">{t["app_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{t["app_subtitle"]}</p>', unsafe_allow_html=True)
    
    # Sidebar with elegant design
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px 0;'>
            <div style='font-size: 3rem; margin-bottom: 10px;'>🔥</div>
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
        <div style='text-align: center; color: #d8d8d8; font-size: 0.8rem;'>
            <p>{t["trust_intuition"]}</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content area
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"### 🌟 {t['sacred_question']}")
        
        # Question input with elegant styling
        question = st.text_area(
            "",
            placeholder=t["question_placeholder"],
            height=150,
            help=t["preparation_text"],
            label_visibility="collapsed"
        )
        
        # Spread selection with custom styling
        st.markdown(f"### 📜 {t['choose_spread']}")
        
        # Define spread options
        spread_options = [
            (t["spread_single_option"], 1),
            (t["spread_three_option"], 3),
            (t["spread_celtic_option"], 10)
        ]
        
        spread_type = st.selectbox(
            "",
            spread_options,
            format_func=lambda x: x[0],
            label_visibility="collapsed"
        )[1]
        
        # Elegant button
        if st.button(f"🌀 {t['consult_oracle']}", use_container_width=True):
            if question.strip():
                with st.spinner("🌀 The veil parts... wisdom emerges..." if st.session_state.language == 'en' else "🌀 帷幕分開...智慧顯現..."):
                    # Add a small delay for dramatic effect
                    import time
                    time.sleep(2)
                    # Generate reading
                    reading = get_oracle_reading(question, spread_type, st.session_state.language)
                    st.session_state.reading = reading
                    st.session_state.question = question
                    st.session_state.timestamp = datetime.datetime.now()
                    st.rerun()
            else:
                st.warning(f"💫 {t['focus_intention']}")
    
    with col2:
        if 'reading' in st.session_state:
            # Display reading with elegant layout
            st.markdown(f"## 🔮 {t['cards_spoken']}")
            
            # Question and timestamp in elegant box
            st.markdown(f"""
            <div class="question-box">
                <h4 class="purple-text">{t['sacred_question']}</h4>
                <p style='font-size: 1.1rem; font-style: italic;'>"{st.session_state.question}"</p>
                <p class="silver-text" style='font-size: 0.9rem; margin-top: 10px;'>
                {t['reading_cast']} {st.session_state.timestamp.strftime("%Y-%m-%d %H:%M")}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Cards display
            st.markdown(f'<div class="spread-title">{t["sacred_spread"]}</div>', unsafe_allow_html=True)
            
            # Create columns for cards
            cols = st.columns(len(st.session_state.reading))
            
            # Position names based on spread type
            if len(st.session_state.reading) == 1:
                position_names = t["position_single"]
            elif len(st.session_state.reading) == 3:
                position_names = t["position_three"]
            else:  # 10 cards
                position_names = t["position_celtic"]
            
            for i, (col, card) in enumerate(zip(cols, st.session_state.reading)):
                with col:
                    position_name = position_names[i] if i < len(position_names) else f"{t['position']} {i+1}"
                    
                    st.markdown(f"""
                    <div class="oracle-card">
                        <div class="card-image">{card['image']}</div>
                        <div class="card-name">{card['card']}</div>
                        <div style='color: #d8d8d8; font-size: 0.9rem; margin: 5px 0;'>{position_name}</div>
                        <div style='color: #888; font-size: 0.8rem; margin-top: 8px;'>
                        {t['category']}: {card['category']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Divider
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            # Detailed interpretations
            st.markdown(f"## 📖 {t['sacred_interpretations']}")
            
            for i, card in enumerate(st.session_state.reading):
                position_name = position_names[i] if i < len(position_names) else f"{t['position']} {i+1}"
                
                st.markdown(f"""
                <div class="interpretation-box">
                    <h4 class="purple-text">#{i+1} • {position_name}</h4>
                    <h3 style='color: #9370DB; margin: 10px 0;'>{card['image']} {card['card']}</h3>
                    <p><strong class="purple-text">{t['category']}:</strong> {card['category']}</p>
                    <p><strong class="purple-text">{t['meaning']}:</strong> {card['meaning']}</p>
                    <p><strong class="purple-text">{t['guidance']}:</strong> {card['advice']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Final guidance
            st.markdown(f"## 💫 {t['cosmic_guidance']}")
            st.markdown(f"""
            <div style='background: rgba(147, 112, 219, 0.1); padding: 25px; border-radius: 12px; border: 1px solid #9370DB;'>
                <h4 style='color: #9370DB; text-align: center; font-family: Cinzel, serif;'>
                🌟 {t['truths']} 🌟
                </h4>
                <p style='text-align: center; font-style: italic; margin: 15px 0;'>
                {t['truth_text']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Download button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                # Create reading text for download
                reading_text = f"""
{t['app_title']}
{'='*len(t['app_title'])}

{t['reading_cast']}: {st.session_state.timestamp.strftime("%Y-%m-%d %H:%M")}
{t['sacred_question']}: {st.session_state.question}

{t['cards_spoken']}:
"""
                for i, card in enumerate(st.session_state.reading):
                    position_name = position_names[i] if i < len(position_names) else f"{t['position']} {i+1}"
                    reading_text += f"""
{i+1}. {card['card']}
   {t['position']}: {position_name}
   {t['category']}: {card['category']}
   {t['meaning']}: {card['meaning']}
   {t['guidance']}: {card['advice']}
"""

                reading_text += f"""

{t['cosmic_guidance']}:
{t['truth_text']}

{t['disclaimer']}
"""
                
                st.download_button(
                    label=f"📥 {t['download_record']}",
                    data=reading_text,
                    file_name=f"twin_flame_reading_{st.session_state.timestamp.strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        
        else:
            # Beautiful initial state with properly styled shop promotion
            st.markdown(f"""
            <div style='text-align: center; padding: 40px 20px;'>
                <div style='font-size: 5rem; margin-bottom: 20px;'>🔥</div>
                <h2 style='color: #9370DB; font-family: Cinzel, serif;'>{t['cards_await']}</h2>
                <p style='color: #d8d8d8; font-size: 1.1rem; margin: 20px 0;'>
                {t['instructions']}
                </p>
                <div style='color: #888; font-style: italic; margin-top: 30px;'>
                <p>✨ {t['trust_process']} ✨</p>
                <p>✨ {t['listen_intuition']} ✨</p>
                <p>✨ {t['embrace_wisdom']} ✨</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Properly integrated shop promotion
            st.markdown(f"""
            <div class="shop-promotion">
                <h4 style='color: #9370DB; font-family: Cinzel, serif; text-align: center;'>📓 {t['continue_journey']}</h4>
                <p style='color: #d8d8d8; text-align: center;'>{t['shop_promo']}</p>
                <div style='text-align: center;'>
                    <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
                       target="_blank" class="store-link">
                       🛍️ {t['enter_shop']}
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Elegant footer with shop link
    st.markdown(f"""
    <div style='text-align: center; margin-top: 50px; padding: 20px; color: #888; border-top: 1px solid #444;'>
        <p>{t['footer_text']}</p>
        <p style='font-size: 0.9rem; margin: 15px 0;'>
            <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
               target="_blank" style='color: #9370DB; text-decoration: none; font-family: Cinzel, serif;'>
               🌟 {t['visit_shop_footer']}
            </a>
        </p>
        <p style='font-size: 0.8rem;'>{t['disclaimer']}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
