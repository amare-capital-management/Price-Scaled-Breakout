import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from datetime import datetime

# -------------------------------------
# CONFIG
# -------------------------------------
tickers = ["ABN.AS", "ADYEN.AS", "ASML.AS", "HEIA.AS", "JDEP.AS", "PHIA.AS", "RAND.AS", "SHELL.AS", "TKWY.AS", "UNA.AS", "WKL.AS", "ACR1.F", 
           "XCA.F", "AIR.F", "AXA.F", "BSN.F", "BNP.F", "CAR1.F", "CAJ1.F", "GZFB.F", "76B.F", "LOR.F", "LVMHF", "MCHA.F", "MOS.F", "RNL.F", 
           "TH1.F", "VACE.F", "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CBK.DE", "CON.DE", "1CO.DE", "DBK.DE", "DB1.DE", 
           "DHL.DE", "DTE.DE", "EOAN.DE", "FME.DE", "HEI.DE", "IFX.DE", "LHA.DE", "PAH3.DE", "PUM.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", 
           "VNA.DE", "ACB.TO", "CM.TO", "BMO.TO", "ABX.TO", "BCE.TO", "BNS.TO", "CNR.TO", "WEED.TO", "ENB.TO", "GWO.TO", "MFC.TO", "CNQ.TO",
           "NTR.TO", "CP.TO", "RY.TO", "SHOP.TO", "SU.TO", "TRP.TO", "TD.TO", "T.TO", "WCN.TO", "MMM", "ABT", "ABBV", "ABC", "ABMD", "ACN",
           "ADM", "ADBE", "ADP", "AAP", "AEP", "AES", "AFL", "AIG", "ABNB", "AIV", "AJG", "ALK", "BABA", "ALGN", "ALLE", "LNT", "ALL", "MO",
           "AMAT", "AMZN", "AMC", "AMD", "DOX", "AEE", "AAL", "AMT", "EXP", "AME", "AMG", "AMGN", "AMP", "APH", "ADI", "ANSS", "AON", "APA",
           "APD", "AAPL", "APTV", "ARNC", "ARE", "ANET", "ARM", "ASML", "AIZ", "T", "ATO", "ADSK", "AZO", "AVB", "AVY", "AWK", "BIDU", "BHGE",
           "USB", "BHC", "BAX", "BDX", "BRK-B", "BBY", "BYND", "BILI", "BIIB", "BMRN", "BLK", "BK", "BAC", "BA", "BKNG", "BWA", "BXP", "BSX",
           "BMY", "AVGO", "BR", "CDNS", "CCJ", "CPB", "CGC", "COF", "CPRI", "CAH", "KMX", "CCL", "CAT", "CBOE", "CBRE", "CE", "CNC", "CNP",
           "CF", "SCHW", "CHTR", "CHD", "CVX", "LFC", "ZNH", "CMG", "CHRW", "CB", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CLX", 
           "CME", "CMS", "CCE", "COIN", "CL", "CMCSA", "CMA", "CAG", "COP", "COO", "CPRT", "GLW", "COST", "COTY", "CCI", "CSX", "CVS", "DHR",
           "DRI", "DVA", "DAL", "DVN", "DFS", "FANG", "WBD", "DISH", "DIS", "DLR", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DHI", "DUK", "DRE",
           "DXC", "DVAX", "EA", "EMN", "ETN", "EBAY", "ECL", "ED", "EW", "LLY", "EMR", "ETR", "EOG", "EQR", "EFX", "EQIX", "ESS", "EL", "EVRG",
           "ES", "EXC", "EXPD", "EXPE", "EXR", "XOM", "META", "FAST", "FDX", "FFIV", "FIS", "FE", "FISV", "FITB", "FLT", "FLS", "FLR", "FMX",
           "F", "FWONA", "FTNT", "FBHS", "FOXA", "BEN", "FCX", "FRT", "GRMN", "IT", "GD", "GDS", "GE", "GIS", "GMAB", "GPC", "GILD", "GPN",
           "GM", "GOOG", "GRPN", "GS", "HAL", "HBI", "HOG", "LHX", "HAS", "HBAN", "HCA", "PEAK", "HP", "HSCI", "HSY", "HES", "HPE", "HIG", 
           "HLT", "HOLX", "HD", "HON", "HRL", "HPQ", "HRB", "HST", "HTHT", "HUM", "IBM", "ICE", "IDXX", "IFF", "ILMN", "INCY", "INO", "INTC",
           "IP", "IPG", "INTU", "ISRG", "IVZ", "NVTA", "IPGP", "IQV", "IRM", "ITW", "JKHY", "JD", "JEF", "SJM", "JNJ", "DE", "YY", "JPM", "JNPR",
           "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC", "KSS", "KHC", "KR", "LW", "LEG", "LEN", "LEVI", "LBTY", "LNC", "LIN", "LKQ", "LMT",
           "LOW", "LRCX", "LULU", "LYFT", "MAA", "MAC", "M", "MANU", "MPC", "MRO", "MAR", "MAS", "MA", "MAT", "MKC", "MCD", "MCK", "MDT", "MELI",
           "MRK", "META", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MLM", "MMC", "MRNA", "MHK", "TAP", "MOMO", "MDLZ", "MNST", "MCO", "MS",
           "MOS", "MSI", "MSCI", "MTB", "NDAQ", "NOV", "NKTR", "NTAP", "NTES", "NFLX", "NWL", "NEM", "EDU", "NWSA", "NEE", "NLSN", "NKE", "NIO",
           "NI", "JWN", "NSC", "NTRS", "NOC", "NLOC", "NCLH", "NVO", "NRG", "NUE", "NVDA", "OXY", "OMC", "OKE", "ORCL", "ORLY", "PCAR", "PZZA",
           "PH", "PAYX", "PYPL", "PEG", "PTON", "PNR", "PEP", "PKI", "PFG", "PFE", "PG", "PM", "PSX", "PDD", "PNW", "PINS", "PKG", "PNC", "PPG",
           "PPL", "PGR", "PLD", "PRU", "PHM", "PVH", "PXD", "QRVO", "QCOM", "PWR", "DGX", "RL", "RJF", "RTX", "O", "RDDT", "REG", "REGN", "RMD",
           "RF", "RHI", "HOOD", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "SHAK", "SHW", "SPG",
           "SIRI", "XRAY", "SWKS", "SLG", "AOS", "SNAP", "SONY", "SO", "LUV", "SWK", "SBUX", "STT", "SYK", "SIVB", "SYF", "SNPS", "SYY", "TMUS",
           "TTWO", "TAL", "TPR", "TGT", "FTI", "TEL", "TFX", "TME", "TSLA", "TEVA", "TXN", "TXT", "GAP", "TMO", "TJX", "TKO", "TSCO", "TDG", "TRV",
           "TCOM", "TRIP", "TROW", "TFC", "TSN", "UBER", "UDR", "ULTA", "UUA", "UNP", "UAL", "UNH", "UPS", "URI", "UNM", "VLO", "VTR", "VRSK", 
           "VZ", "VRSN", "VRTX", "VFC", "VIPS", "VIR", "SPCE", "V", "VNO", "VMC", "WAB", "WMT", "WM", "WAT", "WEC", "WB", "WFC", "WELL", "WDC",
           "WU", "WRK", "WY", "WHR", "WMB", "WDAY", "WWE", "GWW", "WYNN", "XEL", "XRX", "XYL", "YUM", "YUMC", "ZBH", "ZION", "ZTS", "ZM", "ZTO"]

start_date = "2025-01-01"
end_date = datetime.today().strftime("%Y-%m-%d")
output_dir = "breakout_plots_pro"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------
# FUNCTIONS
# -------------------------------------
def download_and_clean(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
    if df.empty:
        return None
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
    df.dropna(inplace=True)
    return df


def add_scaled_price_features(df, window=20):
    close = df["Close"]
    df["RollingMax"] = close.rolling(window).max()
    df["RollingMin"] = close.rolling(window).min()
    df["RollingAvg"] = close.rolling(window).mean()
    df["Range"] = df["RollingMax"] - df["RollingMin"]
    df["ScaledPrice"] = (close - df["RollingAvg"]) / (df["Range"] + 1e-8)
    return df


def build_pro_chart(df, ticker):
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.7, 0.3]
    )

    # Candlestick
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"],
        name="OHLC",
        increasing_line_color="#26a69a", decreasing_line_color="#ef5350",
        showlegend=False
    ), row=1, col=1)

    # Rolling lines
    fig.add_trace(go.Scatter(x=df.index, y=df["RollingMax"], name="20D High", line=dict(color="#ff4444", width=2)), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df["RollingMin"], name="20D Low",  line=dict(color="#00ccff", width=2)), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df["RollingAvg"], name="20D Avg",  line=dict(color="#ffbb33", width=2)), row=1, col=1)

    # Shaded channel – works on all Plotly versions
    fig.add_trace(go.Scatter(
        x=np.concatenate([df.index, df.index[::-1]]),
        y=np.concatenate([df["RollingMax"].values, df["RollingMin"][::-1].values]),
        fill='toself',
        fillcolor='rgba(180,180,180,0.12)',
        line=dict(color="rgba(0,0,0,0)"),
        hoverinfo="skip",
        showlegend=False
    ), row=1, col=1)

    # Scaled Price oscillator
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["ScaledPrice"],
        name="Scaled Price",
        line=dict(color="#e91e63", width=3),
        fill='tozeroy',
        fillcolor='rgba(233,30,99,0.2)'
    ), row=2, col=1)

    # Horizontal levels
    for lvl in [1.0, 0.5, 0, -0.5, -1.0]:
        fig.add_hline(y=lvl, line_dash="dot", line_color="gray", opacity=0.6, row=2, col=1)

    # Layout
    pretty_name = ticker.replace("=F", " Futures").replace("-", "/")
    fig.update_layout(
        title=dict(text=f"<b>{pretty_name}</b><br>Scaled Price Breakout Strategy", x=0.5, font_size=22),
        template="plotly_dark",
        height=900,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis_rangeslider_visible=False,
        margin=dict(l=60, r=60, t=100, b=60)
    )

    fig.update_yaxes(title_text="Price (USD)", row=1, col=1)
    fig.update_yaxes(title_text="Scaled Price", range=[-2.2, 2.2], row=2, col=1)

    return fig


# -------------------------------------
# MAIN LOOP
# -------------------------------------
print("Starting professional Scaled Price Breakout charts...\n")

for ticker in tickers:
    print(f"Processing {ticker}...")

    df = download_and_clean(ticker, start_date, end_date)

    if df is None or len(df) < 50:
        print(f"  → Not enough data for {ticker}\n")
        continue

    df = add_scaled_price_features(df, window=20)
    df = df.dropna()

    fig = build_pro_chart(df, ticker)

    filename = f"{ticker.replace('=', '').replace('-', '')}_ScaledPrice_Pro.png"
    path = os.path.join(output_dir, filename)

    fig.write_image(path, width=1920, height=1080, scale=3)
    print(f"  → Saved {filename}\n")

print("All charts generated successfully!")

print(f"Folder: {os.path.abspath(output_dir)}")
