# Scaled Price Breakout Strategy

A professional, systematic price normalization and breakout framework built in Python using Yahoo Finance data and Plotly visualization.

This project generates institutional-quality charts that combine rolling price channels with a normalized scaled-price oscillator to identify breakouts, compressions, and potential mean-reversion zones across global markets.

## Strategy Overview

The Scaled Price Breakout Strategy transforms raw price action into a **dimensionless oscillator** by scaling price relative to its recent trading range:

- Rolling High (20-day)
- Rolling Low (20-day)
- Rolling Average (20-day)

Price is then expressed as a deviation from the rolling mean, normalized by the rolling range. This removes unit bias and allows signals to be compared across:

- Futures
- Equities
- Indices
- Crypto
- FX
---

## Core Concepts

### 1. Rolling Price Channel
A dynamic 20-day channel captures the market’s current volatility regime:
- Upper bound: Rolling High
- Lower bound: Rolling Low
- Midline: Rolling Average

### 2. Scaled Price Oscillator
The scaled price is calculated as:

Scaled Price = (Close − Rolling Average) / (Rolling High − Rolling Low)

This produces a normalized oscillator where:
- `+1 or +0.5` and above → upside breakout / extension
- `0` → fair value
- `−1 or -0.5` and below → downside breakout / compression

### 3. Regime-Aware Interpretation
Because the oscillator adapts to changing volatility, it avoids false signals common in static indicator systems.

## Chart Layout

Each chart includes:

- **Candlestick price chart**
- **Rolling High / Low / Average**
- **Shaded volatility channel**
- **Scaled Price oscillator**
- **Key horizontal levels:** `+1`, `+0.5`, `0`, `−0.5`, `−1`

Charts are exported as high-resolution PNG files suitable for:
- Research reports
- Trading dashboards
- Portfolio reviews



