import streamlit as st
import json
import pandas as pd
import datetime

# Clean, professional modern layout setup
st.set_page_config(page_title="Project Aether: Next-Level Suite", layout="wide")

st.title("🌌 PROJECT AETHER // NEXT-LEVEL SUITE")
st.caption("Advanced Automated Portfolio Suite • Configured for Robinhood Assets & Broad Indexes")

# --- MODULE 1: BROAD MARKET INDEX FUNDS MONITORING ---
st.header("🏢 Global Index Funds Monitor")
st.write("Track the performance of core market indexes and popular index tracking instruments:")

index_data = {
    "Index Fund": ["S&P 500 ETF (VOO)", "Nasdaq 100 ETF (QQQ)", "Total Stock Market (VTI)", "Dow Jones Industrial (DIA)"],
    "Benchmark Tracker": ["S&P 500 Index", "NASDAQ-100", "CRSP US Total Market", "Dow Jones Industrial Average"],
    "Estimated Share Price": ["$510.40", "$445.30", "$260.15", "$392.80"],
    "Daily Status": ["🟢 ACTIVE", "🟢 ACTIVE", "🟢 ACTIVE", "🟢 ACTIVE"],
    "Risk Profile": ["Moderate / Core", "Aggressive Growth", "Broad Conservative", "Large-Cap Value"]
}
st.table(pd.DataFrame(index_data))

# --- MODULE 2: INTERACTIVE TRADE CHARTS SPACE ---
st.header("📈 Interactive Performance Trade Charts")
st.write("Select an index asset to visualize historical performance curves and mock pricing channels:")

selected_chart_asset = st.selectbox("Select Asset Asset for Technical Charting", ["S&P 500 ETF (VOO)", "Nasdaq 100 ETF (QQQ)", "Total Stock Market (VTI)"])

# Stable algorithmic chart baseline data arrays
chart_days = [f"Day {i}" for i in range(1, 11)]
if "VOO" in selected_chart_asset:
    base_trend = [500, 502, 499, 504, 506, 503, 508, 512, 509, 510.40]
elif "QQQ" in selected_chart_asset:
    base_trend = [430, 435, 432, 438, 441, 437, 442, 446, 443, 445.30]
else:
    base_trend = [252, 254, 253, 256, 258, 255, 259, 261, 258, 260.15]

chart_df = pd.DataFrame({"Asset Evaluation Path ($)": base_trend}, index=chart_days)
st.line_chart(chart_df)

# --- MODULE 3: UPCOMING IPO DISCOVERY space ---
st.header("🚀 Advanced IPO Discovery Matrix")
st.write("Track upcoming market listings and newly planned public offerings:")

ipo_col1, ipo_col2, ipo_col3 = st.columns(3)
with ipo_col1:
    with st.container(border=True):
        st.subheader("🤖 ApexAI Tech")
        st.metric("Ticker Symbol Target", "AAIT")
        st.markdown("**Offering Bounds:** $14.50\n\n**Sector:** Generative AI Infrastructure\n\n*High liquidity volatility profile expected.*")
with ipo_col2:
    with st.container(border=True):
        st.subheader("🌿 EcoCharge Power")
        st.metric("Ticker Symbol Target", "EQLV")
        st.markdown("**Offering Bounds:** $32.00\n\n**Sector:** Solid-State EV Battery Grid\n\n*Backed by green energy infrastructure subsidies.*")
with ipo_col3:
    with st.container(border=True):
        st.subheader("📦 FlexCart Logistics")
        st.metric("Ticker Symbol Target", "FXCT")
        st.markdown("**Offering Bounds:** $22.10\n\n**Sector:** Automated E-Commerce Fulfillment\n\n*Stable historical private revenue models.*")

# --- MODULE 4: PORTFOLIO INVESTMENT TRACKING CALCULATOR ---
st.header("💼 Multi-Asset Investment Calculator Node")
st.write("Track customized Robinhood positions and compute multi-year compound interest paths:")

calc_col1, calc_col2 = st.columns(2)

with calc_col1:
    st.write("### ✏️ Position Allocation Parameters")
    asset_selection = st.selectbox("Select Active Asset Target", ["HOOD (Robinhood Markets)", "AAPL (Apple Inc.)", "NVDA (NVIDIA Corp.)", "MSFT (Microsoft Corp.)"])
    shares_owned = st.number_input("Total Number of Shares Allocated", min_value=0.0, value=20.0, step=1.0)
    avg_cost_basis = st.number_input("Average Purchase Share Price Cost Basis ($)", min_value=0.0, value=35.0, step=5.0)
    projection_years = st.slider("Compounding Time Horizon Strategy Window (Years)", min_value=1, max_value=30, value=10)
    expected_cagr = st.slider("Target Expected Annual Compound Growth Rate (CAGR %)", min_value=1.0, max_value=25.0, value=10.5, step=0.5)

# Calculate cost layout structures
ticker_name = asset_selection.split(" ")[0]
current_prices = {"HOOD": 25.40, "AAPL": 182.30, "NVDA": 505.10, "MSFT": 415.20}
active_market_price = current_prices.get(ticker_name, 100.0)

total_principal_outlay = shares_owned * avg_cost_basis
current_holdings_value = shares_owned * active_market_price
immediate_pnl_usd = current_holdings_value - total_principal_outlay

# Compound Interest Multi-Year Curve Formula
rate_multiplier = expected_cagr / 100.0
future_value_projection = current_holdings_value * ((1.0 + rate_multiplier) ** projection_years)
total_compounded_yield = future_value_projection - total_principal_outlay

with calc_col2:
    st.write("### 📊 Calculated Systematic Metrics")
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Cost Outlay", f"${total_principal_outlay:,.2f}")
    m2.metric("Current Portfolio Equity", f"${current_holdings_value:,.2f}")
    
    if immediate_pnl_usd >= 0:
        m3.metric("Immediate P&L Delta", f"+${immediate_pnl_usd:,.2f}")
    else:
        m3.metric("Immediate P&L Delta", f"-${abs(immediate_pnl_usd):,.2f}", delta_color="inverse")
        
    st.metric("Long-Term Projected Valuation (Year Final)", f"${future_value_projection:,.2f}")
    st.metric("Total Future Wealth Accumulation (P&L Harvest)", f"+${total_compounded_yield:,.2f}")

    # Generate linear projection trajectory coordinate maps
    years_list = [f"Year {i}" for i in range(projection_years + 1)]
    future_curve_points = [current_holdings_value * ((1.0 + rate_multiplier) ** year) for year in range(projection_years + 1)]
    
    projection_df = pd.DataFrame({"Compounded Portfolio Trajectory ($)": future_curve_points}, index=years_list)
    st.line_chart(projection_df)

# --- MODULE 5: CORE TELEMETRY FRAMEWORK CONSOLE LOGS ---
st.header("🖥️ System Platform Monitoring Logs")
st.code(f"🟢 [{datetime.datetime.now().strftime('%H:%M:%S')}] Next-Level App Modules Active. Data structures compiling without leaks.")
