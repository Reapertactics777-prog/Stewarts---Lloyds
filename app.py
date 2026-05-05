import streamlit as st
import pandas as pd
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Stewarts & Lloyds Manufacturing",
    page_icon="🏗️",
    layout="wide"
)

# --- CORPORATE BRANDING CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    
    .brand-header {
        background-color: #003366; 
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }

    .promo-banner {
        background: linear-gradient(90deg, #cc0000 0%, #ff4b4b 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .product-box {
        border: 1px solid #e0e0e0;
        border-radius: 8px 8px 0 0;
        padding: 1.5rem;
        background-color: #fcfcfc;
        height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .price-text {
        color: #003366;
        font-size: 1.4rem;
        font-weight: 800;
    }

    .promo-price {
        color: #cc0000;
        font-size: 1.4rem;
        font-weight: 800;
    }

    .old-price {
        text-decoration: line-through;
        color: #999;
        font-size: 0.9rem;
    }
    
    .dept-title {
        color: #003366;
        font-weight: 700;
        border-left: 5px solid #003366;
        padding-left: 15px;
    }

    .whatsapp-btn {
        background-color: #25D366;
        color: white !important;
        text-decoration: none;
        padding: 12px;
        display: block;
        text-align: center;
        border-radius: 0 0 8px 8px;
        font-weight: 700;
        font-size: 0.8rem;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
DEPT_CONTACTS = {
    "Promotions": "27821234567", # General sales line
    "ICU Fencing": "27821234567",
    "Open Sections": "27821234567",
    "Roofing": "27821234567",
    "Fencing": "27821234567",
    "Hardware": "27821234567",
    "Plasma": "27821234567"
}

DEPT_DATA = {
    "Promotions": {
        "subtitle": "Limited Time Manufacturing Specials",
        "products": [
            ["Palisade Panels (Bulk Buy)", "R 850.00", "R 980.00"],
            ["Clearview 2.1m (Off-cuts)", "R 950.00", "R 1,250.00"],
            ["IBR Sheets 6m bundle", "R 550.00", "R 690.00"]
        ]
    },
    "ICU Fencing": {
        "subtitle": "Clearview & High Security Fencing",
        "products": [["Clearview Panel 2.1m", "R 1,250.00"], ["Post & Fixings Kit", "R 450.00"]]
    },
    "Open Sections": {
        "subtitle": "Lip Channels & Structural Purlins",
        "products": [["Lip Channel 100x50x20x2mm", "R 165.00/m"]]
    },
    "Roofing": {
        "subtitle": "IBR & Corrugated Roofing Solutions",
        "products": [["IBR Sheet 0.47mm Zincalume", "R 115.00/m"]]
    },
    "Fencing": {
        "subtitle": "Industrial Palisade Fencing",
        "products": [["Palisade Panel 3m x 1.8m", "R 980.00"]]
    },
    "Hardware": {
        "subtitle": "Steel Components & Accessories",
        "products": [["Pole Caps 50mm", "R 12.50"], ["Wall Spikes (1.5m)", "R 89.00"]]
    },
    "Plasma": {
        "subtitle": "CNC Precision Plasma Cutting",
        "products": [["Custom Base Plates", "Market Price"]]
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://www.stewartsandlloyds.co.za/wp-content/uploads/2023/04/Stewarts-and-Lloyds-Logo.png", width=200)
    st.markdown("---")
    selection = st.radio("Go to Department:", list(DEPT_DATA.keys()))
    st.markdown("---")
    st.info(f"**Contact {selection}:**\n\n+{DEPT_CONTACTS[selection]}")

# --- MAIN PAGE CONTENT ---
st.markdown(f"""
    <div class="brand-header">
        <h1>Stewarts & Lloyds Manufacturing</h1>
        <p>Quality Steel & Trusted Value Since 1903</p>
    </div>
    """, unsafe_allow_html=True)

# Add Promo Banner if on Promotions page
if selection == "Promotions":
    st.markdown('<div class="promo-banner">🔥 MONTHLY MANUFACTURING SPECIALS - WHILE STOCKS LAST 🔥</div>', unsafe_allow_html=True)

st.markdown(f"<h2 class='dept-title'>{selection}</h2>", unsafe_allow_html=True)
st.write(f"Section: **{DEPT_DATA[selection]['subtitle']}**")
st.markdown("---")

# Display Products
items = DEPT_DATA[selection]['products']
cols = st.columns(3)

for i, item in enumerate(items):
    prod_name = item[0]
    is_promo = len(item) > 2
    
    current_price = item[1]
    old_price = item[2] if is_promo else ""
    
    phone = DEPT_CONTACTS[selection]
    msg = f"Hi S&L, I want to claim the special for {prod_name} at {current_price}." if is_promo else f"Hi S&L, I am interested in {prod_name}."
    wa_url = f"https://wa.me/{phone}?text={urllib.parse.quote(msg)}"
    
    with cols[i % 3]:
        # Product Card Logic
        price_display = f'<div class="old-price">{old_price}</div><div class="promo-price">{current_price}</div>' if is_promo else f'<div class="price-text">{current_price}</div>'
        
        st.markdown(f"""
            <div class="product-box">
                <div>
                    <span style="color: {'#cc0000' if is_promo else '#666'}; font-size: 0.8rem; font-weight: bold;">
                        {'⚡ SPECIAL OFFER' if is_promo else f'CODE: SL-{selection[:2].upper()}-{i+100}'}
                    </span>
                    <h3 style="margin: 5px 0; font-size: 1.1rem;">{prod_name}</h3>
                </div>
                {price_display}
            </div>
            <a href="{wa_url}" class="whatsapp-btn" target="_blank">
                {'GET THIS DEAL' if is_promo else 'ENQUIRE ON WHATSAPP'}
            </a>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 Stewarts & Lloyds Manufacturing | Prices subject to steel fluctuations.")
