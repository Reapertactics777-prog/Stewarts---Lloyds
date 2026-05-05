import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Stewarts & Lloyds Manufacturing",
    page_icon="🏗️",
    layout="wide"
)

# --- CORPORATE BRANDING CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Custom Header */
    .brand-header {
        background-color: #003366; /* S&L Deep Blue */
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Product Cards */
    .product-box {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        background-color: #fcfcfc;
        transition: transform 0.2s;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.02);
    }
    
    .product-box:hover {
        border-color: #003366;
        transform: translateY(-5px);
    }

    .price-text {
        color: #003366;
        font-size: 1.4rem;
        font-weight: 800;
        margin-top: 10px;
    }
    
    .dept-title {
        color: #003366;
        font-weight: 700;
        border-left: 5px solid #003366;
        padding-left: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
# Using a dictionary to keep departments separate as requested
DEPT_DATA = {
    "ICU Fencing": {
        "subtitle": "Clearview & High Security Fencing",
        "products": [["Clearview Panel 2.1m", "R 1,250.00"], ["Post & Fixings Kit", "R 450.00"], ["Security Mesh 3.0m", "R 1,800.00"]]
    },
    "Open Sections": {
        "subtitle": "Lip Channels & Structural Purlins",
        "products": [["Lip Channel 100x50x20x2mm", "R 165.00/m"], ["Lip Channel 125x50x20x2mm", "R 195.00/m"], ["Purlins Black Steel", "Request Quote"]]
    },
    "Roofing": {
        "subtitle": "IBR & Corrugated Roofing Solutions",
        "products": [["IBR Sheet 0.47mm Zincalume", "R 115.00/m"], ["Corrugated 0.5mm Galv", "R 108.00/m"], ["Cranked Sheets", "Quote Required"]]
    },
    "Fencing": {
        "subtitle": "Industrial Palisade Fencing",
        "products": [["Palisade Panel 3m x 1.8m", "R 980.00"], ["Palisade Bolt-on Pale", "R 42.00"], ["Angle Iron Post", "R 210.00"]]
    },
    "Hardware": {
        "subtitle": "Steel Components & Accessories",
        "products": [["Pole Caps 50mm", "R 12.50"], ["Heavy Duty Hinges", "R 55.00"], ["Wall Spikes (1.5m)", "R 89.00"], ["Weaving Coil (50kg)", "R 1,100.00"], ["Lugs & Base Plates", "R 15.00"]]
    },
    "Plasma": {
        "subtitle": "CNC Precision Plasma Cutting",
        "products": [["Custom Base Plates", "Market Price"], ["Plasma Cut to Size", "Per kg/min"], ["Profiling Service", "Request Quote"]]
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://www.stewartsandlloyds.co.za/wp-content/uploads/2023/04/Stewarts-and-Lloyds-Logo.png", width=200) # Fallback to text if URL fails
    st.markdown("---")
    st.title("Navigation")
    selection = st.radio("Select Department:", list(DEPT_DATA.keys()))
    st.markdown("---")
    st.info("Contact Head Office: \n\n 📞 +27 (0)11 XXX XXXX")

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

# Display Products in a Responsive Grid
items = DEPT_DATA[selection]['products']
cols = st.columns(3)

for i, item in enumerate(items):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="product-box">
                <div>
                    <span style="color: #666; font-size: 0.8rem; text-transform: uppercase;">Product Code: SL-{i+100}</span>
                    <h3 style="margin: 5px 0;">{item[0]}</h3>
                </div>
                <div class="price-text">{item[1]}</div>
            </div>
            """, unsafe_allow_html=True)
        st.button(f"Enquire About {item[0]}", key=f"btn_{selection}_{i}")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Stewarts & Lloyds Manufacturing | Built for Excellence</p>", unsafe_allow_html=True)
