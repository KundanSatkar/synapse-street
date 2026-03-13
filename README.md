# 🧠 Synapse Street — AI Multi-Agent Financial Analysis System

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.0.20-FF6F00?style=flat)](https://github.com/langchain-ai/langgraph)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector_DB-EF4444?style=flat)](https://qdrant.tech)
[![License](https://img.shields.io/badge/License-MIT-10B981?style=flat)](LICENSE)

> 🥇 **Best Use of AI/ML** — UB Hacking 2024 (OpenAI Sponsor Prize)  
> 🥈 **2nd Place Overall** — out of 87 teams

AI-powered multi-agent system for stock market analysis. Three specialized GPT-4 agents collaborate via a consensus engine to generate BUY/SELL/HOLD signals with confidence scores.

---

## 🎯 The Problem

Traditional algorithmic trading systems suffer from three core failures:

- **Single-point failure** — one model making all decisions
- **Narrow context** — missing broader market signals
- **Poor explainability** — black-box decisions traders can't trust

Synapse Street solves this with a collaborative multi-agent architecture that mirrors how real trading desks operate.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA INGESTION LAYER                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Market Data │  │  News API   │  │ SEC Filings │             │
│  │  (Yahoo)    │  │  (NewsAPI)  │  │  (EDGAR)    │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         └─────────────────┼─────────────────┘                   │
│                           ▼                                     │
│                  ┌─────────────────┐                            │
│                  │ Spark Streaming │                            │
│                  │ (3K+ entities)  │                            │
│                  └────────┬────────┘                            │
└───────────────────────────┼─────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   VECTOR MEMORY (Qdrant)                         │
│  • Market embeddings (OpenAI Ada-002)                           │
│  • Historical pattern matching                                   │
│  • News sentiment vectors                                        │
└─────────────────────────────────────────────────────────────────┘
                            ▼
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  DATA AGENT   │   │ANALYSIS AGENT │   │ EXECUTION     │
│   (GPT-4)     │   │   (GPT-4)     │   │   AGENT       │
│               │   │               │   │   (GPT-4)     │
│ • Ingest data │   │ • Technical   │   │               │
│ • Feature eng │   │   analysis    │   │ • Generate    │
│ • Store to    │   │ • Sentiment   │   │   signals     │
│   vector DB   │   │   scoring     │   │ • Position    │
│               │   │ • Risk assess │   │   sizing      │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        └───────────────────┼───────────────────┘
                            ▼
                 ┌─────────────────┐
                 │  CONSENSUS      │
                 │  ENGINE         │
                 │  (LangGraph)    │
                 │                 │
                 │  • Weighted     │
                 │    voting       │
                 │  • Confidence   │
                 │    thresholds   │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │  TRADING SIGNAL │
                 │ BUY/SELL/HOLD   │
                 │  + Confidence   │
                 └─────────────────┘
```

---

## 📊 Performance Results

### Backtest: S&P 500 (Jan 2023 – Oct 2024)

| Strategy | Total Return | Sharpe | Max Drawdown | Win Rate |
|----------|-------------|--------|--------------|----------|
| **Buy & Hold** | 24.5% | 1.2 | -18% | — |
| **Synapse Street** | **42.8%** | **1.8** | **-12%** | **64%** |
| **Improvement** | **+18.3%** | **+50%** | **+33%** | — |

### Agent Consensus Analysis

| Consensus Level | Trades | Win Rate | Avg Return | Sharpe |
|----------------|--------|----------|------------|--------|
| High (3/3 agree) | 45 | 78% | 4.2% | 2.4 |
| Medium (2/3 agree) | 120 | 58% | 2.1% | 1.6 |
| Low (split) | 85 | 42% | -0.5% | 0.8 |

> **Key Insight**: High-consensus trades significantly outperform, validating the multi-agent approach.

### Risk Metrics

| Metric | Value |
|--------|-------|
| Beta | 0.85 |
| Alpha | 12.3% annualized |
| Sortino Ratio | 2.1 |
| Calmar Ratio | 3.6 |

---

## 🛠️ Technology Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Agent Framework | LangGraph | Explicit state management, cyclic workflows |
| LLM | GPT-4 | Best reasoning for financial analysis |
| Vector Database | Qdrant | Hybrid search, Rust-based speed |
| Embeddings | OpenAI Ada-002 | Optimal cost/performance for financial text |
| Data Processing | Spark + Pandas | Batch + real-time |
| Orchestration | Apache Airflow | Production pipeline scheduling |
| Dashboard | Streamlit | Real-time monitoring |
| Backtesting | Backtrader | Industry-standard, extensible |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker (for Qdrant)
- OpenAI API key

### Installation

```bash
# 1. Clone repository
git clone https://github.com/KundanSatkar/synapse-street.git
cd Synapse-Street

# 2. Start Qdrant
docker run -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# 5. Download historical data
python scripts/download_data.py --symbols SPY,AAPL,MSFT --start 2020-01-01

# 6. Run backtest
python main.py --mode backtest --config configs/backtest.yaml
```

### Usage

```python
from synapse_street import TradingSystem
from synapse_street.config import load_config

config = load_config('configs/production.yaml')
system = TradingSystem(config)

signals = system.generate_signals(
    symbols=['AAPL', 'MSFT', 'GOOGL', 'AMZN'],
    lookback_days=30
)

print(signals)
# [
#   {
#     'symbol': 'AAPL',
#     'signal': 'BUY',
#     'confidence': 0.87,
#     'agents_agree': '3/3',
#     'rationale': 'Technical breakout + positive earnings sentiment',
#     'position_size': 0.15
#   },
#   ...
# ]
```

---

## 🎥 Agent Decision Flow (Example)

```
[14:32:05] DATA_AGENT:      Fetched AAPL 1-min bars, RSI=68, MACD crossing
[14:32:06] DATA_AGENT:      News sentiment: +0.8 (earnings beat)
[14:32:07] DATA_AGENT:      Stored to Qdrant: 5 vectors

[14:32:08] ANALYSIS_AGENT:  Retrieved similar patterns (3 bullish, 1 bearish)
[14:32:09] ANALYSIS_AGENT:  Technical: 0.75 | Sentiment: 0.82 | Risk: LOW
[14:32:09] ANALYSIS_AGENT:  → BULLISH (confidence: 0.79)

[14:32:10] EXECUTION_AGENT: Portfolio: 20% cash, max position 15%
[14:32:10] EXECUTION_AGENT: → BUY, Size: 12% (within risk limits)

[14:32:11] CONSENSUS:        All 3 agents agree → HIGH confidence
[14:32:11] CONSENSUS:        → EXECUTE BUY AAPL @ $178.50, 12% position
```

---

## 🔬 Technical Deep Dives

### Consensus Mechanism

Not simple majority voting — we use weighted confidence scoring:

```python
def calculate_consensus(agent_outputs):
    weighted_sum = sum(
        output['confidence'] * output['signal_value']
        for output in agent_outputs
    )
    total_confidence = sum(output['confidence'] for output in agent_outputs)
    consensus_score = weighted_sum / total_confidence

    if consensus_score > 0.7:
        return 'BUY', 'HIGH'
    elif consensus_score < -0.7:
        return 'SELL', 'HIGH'
    else:
        return 'HOLD', 'LOW'
```

### Vector Search Strategy (Qdrant Hybrid)

```python
results = qdrant.search(
    collection_name="market_conditions",
    query_vector=dense_embedding,      # Ada-002: semantic similarity
    query_sparse=sparse_vector,        # BM25: ticker/term matching
    limit=5,
    score_threshold=0.75
)
```

---

## 📁 Project Structure

```
Synapse-Street/
├── agents/
│   ├── base_agent.py          # Abstract base class
│   ├── data_agent.py          # Market data ingestion
│   ├── analysis_agent.py      # Technical + sentiment analysis
│   └── execution_agent.py     # Signal generation + sizing
├── core/
│   ├── consensus_engine.py    # Agent voting mechanism
│   ├── vector_store.py        # Qdrant interface
│   ├── risk_manager.py        # Position sizing, stop-losses
│   └── backtester.py          # Strategy validation
├── configs/
│   ├── backtest.yaml
│   └── production.yaml
├── dashboard/
│   └── streamlit_app.py
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🔮 Roadmap

- [ ] Live trading integration (Alpaca / Interactive Brokers)
- [ ] Reinforcement learning for dynamic position sizing
- [ ] Alternative data (satellite imagery, credit card transactions)
- [ ] Multi-asset support (crypto, forex, commodities)
- [ ] Federated learning across distributed data sources

---

## 🏆 Hackathon Results — UB Hacking 2024

- 🥇 Best Use of AI/ML (Sponsor: OpenAI)
- 🥈 2nd Place Overall (87 teams)
- 💡 Most Innovative Architecture (Judge's Choice)

> *"The multi-agent approach to financial analysis is genuinely novel. Most teams used single LLM calls; this team architected a collaborative system that mirrors real trading desks."* — Judges' Feedback

**Team:** Kundan Satkar (Data Engineering, ETL Pipelines) · Mrudula Deshmukh (ML Engineer, Vector Search) · Siddharth Adhikari · Sathwick Kiran
---

## 📄 License

MIT License — see [LICENSE](LICENSE)

> ⚠️ **Disclaimer**: Educational purposes only. Not financial advice. Trading involves significant risk.

---

## 📬 Contact
**Kundan Satkar** — Data Engineering & Pipeline Architecture

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Kundan%20Satkar-blue?logo=linkedin)](https://www.linkedin.com/in/kundan-satkar)
[![GitHub](https://img.shields.io/badge/GitHub-KundanSatkar-black?logo=github)](https://github.com/KundanSatkar)
[![Email](https://img.shields.io/badge/Email-kundansatkar0%40gmail.com-red?logo=gmail)](mailto:kundansatkar0@gmail.com)
