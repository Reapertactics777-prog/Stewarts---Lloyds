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
    
    .product-box {
        border: 1px solid #e0e0e0;
        border-radius: 8px 8px 0 0; /* Rounded top only to sit on button */
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
    
    .dept-title {
        color: #003366;
        font-weight: 700;
        border-left: 5px solid #003366;
        padding-left: 15px;
    }

    /* Professional WhatsApp Button Style */
    .whatsapp-btn {
        background-color: #25D366;
        color: white !important;
        text-decoration: none;
        padding: 12px;
        display: block;
        text-align: center;
        border-radius: 0 0 8px 8px; /* Rounded bottom to match card */
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 25px;
        transition: 0.3s;
    }
    .whatsapp-btn:hover {
        background-color: #128C7E;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
# Add your specific WhatsApp numbers here (Use international format: 2782...)
DEPT_CONTACTS = {
    "ICU Fencing": "27821234567",
    "Open Sections": "27821234567",
    "Roofing": "27821234567",
    "Fencing": "27821234567",
    "Hardware": "27821234567",
    "Plasma": "27821234567"
}

DEPT_DATA = {
    "ICU Fencing": {
        "subtitle": "Clearview & High Security Fencing",
        "products": [["Clearview Panel 2.1m", "R 1,250.00"], ["Post & Fixings Kit", "R 450.00"], ["Security Mesh 3.0m", "R 1,800.00"]]
    },
    "Open Sections": {
        "subtitle": "Lip Channels & Structural Purlins",
        "products": [["Lip Channel 100x50x20x2mm", "R 165.00/m"], ["Lip Channel 125x50x20x2mm", "R 195.00/m"]]
    },
    "Roofing": {
        "subtitle": "IBR & Corrugated Roofing Solutions",
        "products": [["IBR Sheet 0.47mm Zincalume", "R 115.00/m"], ["Corrugated 0.5mm Galv", "R 108.00/m"]]
    },
    "Fencing": {
        "subtitle": "Industrial Palisade Fencing",
        "products": [["Palisade Panel 3m x 1.8m", "R 980.00"], ["Palisade Bolt-on Pale", "R 42.00"]]
    },
    "Hardware": {
        "subtitle": "Steel Components & Accessories",
        "products": [["Pole Caps 50mm", "R 12.50"], ["Heavy Duty Hinges", "R 55.00"], ["Wall Spikes (1.5m)", "R 89.00"], ["Weaving Coil (50kg)", "R 1,100.00"]]
    },
    "Plasma": {
        "subtitle": "CNC Precision Plasma Cutting",
        "products": [["Custom Base Plates", "Market Price"], ["Plasma Cut to Size", "Per kg/min"]]
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://www.stewartsandlloyds.co.za/wp-content/uploads/2023/04/Stewarts-and-Lloyds-Logo.png", width=200)
    st.markdown("---")
    st.title("Navigation")
    selection = st.radio("Select Department:", list(DEPT_DATA.keys()))
    st.markdown("---")
    st.info(f"**Direct WhatsApp:**\n\n+{DEPT_CONTACTS[selection]}")

# --- MAIN PAGE CONTENT ---
st.markdown(f"""
    <div class="brand-header">
        <h1>Stewarts & Lloyds Manufacturing</h1>
        <p>Quality Steel & Trusted Value Since 1903</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"<h2 class='dept-title'>{selection}</h2>", unsafe_allow_html=True)
st.write(f"Displaying catalog for: **{DEPT_DATA[selection]['subtitle']}**")
st.markdown("---")

# Display Products
items = DEPT_DATA[selection]['products']
cols = st.columns(3)

for i, item in enumerate(items):
    prod_name = item[0]
    prod_price = item[1]
    phone = DEPT_CONTACTS[selection]
    
    # Create the WhatsApp message link
    msg = f"Hi S&L Manufacturing, I'm interested in: {prod_name} (Price: {prod_price}) from the {selection} department."
    wa_url = f"https://wa.me/{phone}?text={urllib.parse.quote(msg)}"
    
    with cols[i % 3]:
        # Product Info
        st.markdown(f"""
            <div class="product-box">
                <div>
                    <span style="color: #666; font-size: 0.8rem; text-transform: uppercase;">Product Code: SL-{i+100}</span>
                    <h3 style="margin: 5px 0;">{prod_name}</h3>
                </div>
                <div class="price-text">{prod_price}</div>
            </div>
            <a href="{wa_url}" class="whatsapp-btn" target="_blank">
                💬 ENQUIRE ON WHATSAPP
            </a>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Stewarts & Lloyds Manufacturing | Built for Excellence</p>", unsafe_allow_html=True)
