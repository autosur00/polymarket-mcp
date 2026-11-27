"""
[AutoDev Enterprise: Polymarket & Prediction Market Intelligence MCP Server]
Claude Desktop, Cursor, and Antigravity users can query live prediction markets,
whale volumes, and probability shifts through their AI coding assistants.
"""

from fastmcp import FastMCP
import urllib.request
import json
from datetime import datetime
from typing import List, Dict, Any, Optional

mcp = FastMCP("Polymarket Intelligence Engine")

API_BASE = "https://gamma-api.polymarket.com"
HEADERS = {"User-Agent": "PolymarketMCPEngine/1.0"}

def _fetch_markets(limit: int = 20, active: bool = True) -> List[Dict[str, Any]]:
    url = f"{API_BASE}/markets?limit={limit}&active={str(active).lower()}&closed=false"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return []

@mcp.tool()
def get_top_prediction_markets(min_volume_usd: float = 50000.0, limit: int = 10) -> str:
    """Fetch high-liquidity active prediction markets from Polymarket with current odds and volumes."""
    markets = _fetch_markets(limit=30)
    filtered = []
    for m in markets:
        vol = float(m.get("volume", 0) or 0)
        if vol >= min_volume_usd:
            filtered.append({
                "question": m.get("question"),
                "volume_usd": round(vol, 2),
                "liquidity_usd": float(m.get("liquidity", 0) or 0),
                "outcomes": m.get("outcomes", []),
                "prices": m.get("outcomePrices", []),
                "end_date": m.get("endDate")
            })
    
    filtered.sort(key=lambda x: x["volume_usd"], reverse=True)
    top = filtered[:limit]
    
    if not top:
        return "No active markets found matching criteria."
        
    res = [f"📊 Polymarket Intelligence: Top {len(top)} High-Volume Prediction Markets\n"]
    for i, item in enumerate(top, 1):
        res.append(f"{i}. 🎯 **{item['question']}**")
        res.append(f"   • Total Volume: ${item['volume_usd']:,.2f}")
        res.append(f"   • Options: {item['outcomes']}")
        res.append(f"   • Current Probability/Prices: {item['prices']}\n")
        
    return "\n".join(res)

@mcp.tool()
def search_prediction_market_by_topic(keyword: str) -> str:
    """Search Polymarket prediction markets by keyword (e.g. 'crypto', 'election', 'fed', 'rate')."""
    markets = _fetch_markets(limit=50)
    matched = []
    kw = keyword.lower()
    for m in markets:
        q = (m.get("question") or "").lower()
        desc = (m.get("description") or "").lower()
        if kw in q or kw in desc:
            vol = float(m.get("volume", 0) or 0)
            matched.append({
                "question": m.get("question"),
                "volume_usd": round(vol, 2),
                "prices": m.get("outcomePrices", []),
                "outcomes": m.get("outcomes", [])
            })
            
    if not matched:
        return f"No prediction markets found for keyword: '{keyword}'"
        
    matched.sort(key=lambda x: x["volume_usd"], reverse=True)
    out = [f"🔍 Polymarket Search Results for '{keyword}' ({len(matched)} matches):\n"]
    for item in matched[:5]:
        out.append(f"• **{item['question']}** (Volume: ${item['volume_usd']:,.2f})")
        out.append(f"  Odds: {dict(zip(item['outcomes'], item['prices']))}\n")
    return "\n".join(out)

if __name__ == "__main__":
    mcp.run()
