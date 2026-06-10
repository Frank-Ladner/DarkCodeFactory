import streamlit as st

from bmi import calculate_bmi, classify_bmi


st.set_page_config(
    page_title="Dark Code Factory - BMI-Rechner",
    page_icon="Y",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --syzygy-green: #00EE4D;
        --milky-way-white: #FFFFFF;
        --galaxy-black: #000000;
        --not-quite-black: #1D1D1D;
        --moon-grey: #F6F6F4;
        --border-grey: #DBD9D6;
    }

    html, body, [class*="css"] {
        font-family: "ProximaNovaA-Light", Arial, sans-serif;
        color: var(--not-quite-black);
        letter-spacing: 0;
    }

    .stApp {
        background: var(--milky-way-white);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stAppViewContainer"] > .main {
        background:
            linear-gradient(var(--syzygy-green), var(--syzygy-green)) 0 0 / 100% 6px no-repeat,
            var(--milky-way-white);
    }

    .block-container {
        max-width: 1120px;
        padding-top: 3.5rem;
        padding-bottom: 4rem;
    }

    .brand-line {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin-bottom: 4.5rem;
        color: var(--not-quite-black);
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
        line-height: 1;
    }

    .brand-mark {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 2.4rem;
        height: 2.4rem;
        background: var(--syzygy-green);
        color: var(--galaxy-black);
        font-size: 1.1rem;
        font-weight: 600;
    }

    .brand-divider {
        width: 2.8rem;
        height: 1px;
        background: var(--not-quite-black);
    }

    .eyebrow {
        margin: 0 0 1rem;
        color: var(--not-quite-black);
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
    }

    .eyebrow-slash {
        color: var(--syzygy-green);
        font-size: 1.15rem;
        margin-right: 0.45rem;
    }

    .hero-title {
        max-width: 760px;
        margin: 0;
        color: var(--not-quite-black);
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-size: clamp(2.8rem, 6vw, 5.4rem);
        font-weight: 600;
        line-height: 1.02;
        letter-spacing: 0;
    }

    .hero-copy {
        max-width: 590px;
        margin: 1.5rem 0 4rem;
        color: var(--not-quite-black);
        font-size: 1.14rem;
        font-weight: 300;
        line-height: 1.5;
    }

    .section-label {
        display: flex;
        align-items: center;
        gap: 0.65rem;
        margin-bottom: 1.2rem;
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-size: 1rem;
        font-weight: 600;
    }

    .section-label::before {
        content: "/";
        color: var(--syzygy-green);
        font-size: 1.35rem;
    }

    [data-testid="stNumberInput"] label {
        color: var(--not-quite-black) !important;
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif !important;
        font-weight: 600 !important;
    }

    [data-testid="stNumberInput"] input {
        min-height: 3.25rem;
        border-color: var(--border-grey);
        border-radius: 0;
        background: var(--milky-way-white);
        color: var(--not-quite-black);
        font-size: 1.05rem;
    }

    [data-testid="stNumberInput"] input:focus {
        border-color: var(--not-quite-black);
        box-shadow: 0 0 0 2px var(--syzygy-green);
    }

    .stButton > button {
        min-height: 3.25rem;
        margin-top: 1rem;
        padding: 0.75rem 1.5rem;
        border: 2px solid var(--galaxy-black);
        border-radius: 0;
        background: var(--syzygy-green);
        color: var(--galaxy-black);
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-weight: 600;
    }

    .stButton > button:hover {
        border-color: var(--galaxy-black);
        background: var(--galaxy-black);
        color: var(--milky-way-white);
    }

    .stButton > button:focus {
        box-shadow: 0 0 0 3px var(--syzygy-green);
    }

    .result-panel {
        margin-top: 3rem;
        padding: 2rem 0;
        border-top: 1px solid var(--not-quite-black);
        border-bottom: 1px solid var(--border-grey);
    }

    .result-kicker {
        margin-bottom: 0.45rem;
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-size: 0.82rem;
        font-weight: 600;
    }

    .result-value {
        color: var(--not-quite-black);
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-size: 4rem;
        font-weight: 600;
        line-height: 1;
    }

    .result-category {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.55rem 0.8rem;
        background: var(--syzygy-green);
        color: var(--galaxy-black);
        font-family: "ProximaNovaA-Semibold", Arial, sans-serif;
        font-weight: 600;
    }

    .space-pattern {
        position: relative;
        min-height: 18rem;
        margin-top: 1rem;
        overflow: hidden;
        background: var(--moon-grey);
    }

    .space-pattern::before,
    .space-pattern::after {
        content: "";
        position: absolute;
        border: 2px solid var(--not-quite-black);
        border-radius: 50%;
    }

    .space-pattern::before {
        width: 10rem;
        height: 10rem;
        right: 14%;
        top: 3rem;
        border-right-color: transparent;
    }

    .space-pattern::after {
        width: 1.1rem;
        height: 1.1rem;
        right: 12%;
        top: 2.2rem;
        border: 0;
        background: var(--syzygy-green);
    }

    .orbit-slash {
        position: absolute;
        right: 36%;
        bottom: 4rem;
        width: 5rem;
        height: 0.75rem;
        background: var(--galaxy-black);
        transform: rotate(-48deg);
    }

    .orbit-dot {
        position: absolute;
        right: 48%;
        top: 4rem;
        width: 0.7rem;
        height: 0.7rem;
        background: var(--syzygy-green);
        border-radius: 50%;
    }

    .orbit-line {
        position: absolute;
        right: 25%;
        bottom: 3.5rem;
        width: 8rem;
        height: 1px;
        background: var(--not-quite-black);
        transform: rotate(22deg);
        transform-origin: left center;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-top: 2rem;
        }

        .brand-line {
            margin-bottom: 3rem;
        }

        .hero-title {
            font-size: 3rem;
        }

        .hero-copy {
            margin-bottom: 3rem;
        }

        .space-pattern {
            min-height: 11rem;
            margin-top: 2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="brand-line">
        <span class="brand-mark">Y</span>
        <span>Dark Code Factory</span>
        <span class="brand-divider"></span>
        <span>Human centered tools</span>
    </div>
    <p class="eyebrow"><span class="eyebrow-slash">/</span>BMI-Rechner</p>
    <h1 class="hero-title">Klarheit für deine Gesundheit.</h1>
    <p class="hero-copy">
        Berechne deinen Body-Mass-Index. Schnell, einfach und ohne Umwege.
    </p>
    """,
    unsafe_allow_html=True,
)

form_column, visual_column = st.columns([1.15, 0.85], gap="large")

with form_column:
    st.markdown('<div class="section-label">Deine Werte</div>', unsafe_allow_html=True)

    input_left, input_right = st.columns(2, gap="medium")

    with input_left:
        height_cm = st.number_input(
            "Körpergröße (cm)",
            min_value=50,
            max_value=250,
            value=170,
            step=1,
        )

    with input_right:
        weight_kg = st.number_input(
            "Gewicht (kg)",
            min_value=10.0,
            max_value=500.0,
            value=70.0,
            step=0.1,
        )

    calculate = st.button("BMI berechnen", type="primary", use_container_width=True)

with visual_column:
    st.markdown(
        """
        <div class="space-pattern" aria-hidden="true">
            <span class="orbit-slash"></span>
            <span class="orbit-dot"></span>
            <span class="orbit-line"></span>
        </div>
        """,
        unsafe_allow_html=True,
    )

if calculate:
    bmi = calculate_bmi(height_cm, weight_kg)
    category, color = classify_bmi(bmi)

    st.markdown(
        f"""
        <div class="result-panel" data-category-color="{color}">
            <div class="result-kicker">Dein Ergebnis</div>
            <div class="result-value">{bmi:.1f}</div>
            <div class="result-category">{category}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
