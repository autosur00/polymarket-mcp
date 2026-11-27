# Polymarket Intelligence MCP Server

> Query real-time prediction market odds, whale volume metrics, and probability shifts directly inside **Claude Desktop**, **Cursor**, and **Antigravity**.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/built%20with-FastMCP-green.svg)](https://github.com/jlowin/fastmcp)

---

## ⚡ What is this?
An open-source Model Context Protocol (MCP) server that connects your AI coding assistant to **Polymarket**, the world's largest prediction market ($50M+ daily volume).

Ask Claude or Cursor:
- *"What are the top 5 high-volume political prediction markets right now?"*
- *"Check the current odds and probability shifts on the 2028 elections."*
- *"Search prediction markets related to Ethereum ETF or interest rate cuts."*

---

## 🚀 Quick Setup

### 1. Installation
```bash
git clone https://github.com/autosur00/polymarket-mcp.git
cd polymarket-mcp
pip install fastmcp
```

### 2. Configure Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "polymarket": {
      "command": "python",
      "args": ["/path/to/polymarket-mcp/server.py"]
    }
  }
}
```

### 3. Configure Antigravity / Cursor
Add to your MCP settings:
```json
{
  "mcpServers": {
    "polymarket": {
      "command": "python",
      "args": ["c:/autodev/products/polymarket_mcp/server.py"]
    }
  }
}
```

---

## 🛠️ Available MCP Tools
- `get_top_prediction_markets(min_volume_usd, limit)`: Fetch the highest-liquidity prediction markets with real-time probability distributions.
- `search_prediction_market_by_topic(keyword)`: Query live markets by topics like crypto, geopolitics, elections, and macro economy.

---

## 💳 Commercial & Pro Version
Looking for automated probability arbitrage signals, whale wallet alerts, and private Discord/Telegram webhooks?
👉 **Get the Pro Intelligence Feed on Gumroad**: [https://gumroad.com](https://gumroad.com)

---

## 📜 License
MIT © autosur00
