# 🏦 Synapse Street — AI Multi-Agent Stock Analysis System

AI multi-agent platform that detects **short-selling opportunities in the U.S. stock market** using LangGraph agents, vector search, and financial ML models.

Built during **UB Hacking 2024 Hackathon**.

**Key Result**

• 18% backtest return improvement  
• Multi-agent consensus system  
• Vector memory using Qdrant  

---

# 🎯 Overview

Synapse Street is an AI-powered market intelligence system that combines:

• Machine learning  
• large language models  
• vector databases  
• distributed data pipelines  

The system identifies **high-probability short opportunities** across U.S. equities by analyzing:

• price movements  
• volatility signals  
• financial indicators  
• market sentiment  

Inspired by *The Big Short*, the platform autonomously analyzes financial markets and presents results through dashboards.

---

# 🧠 Multi-Agent System

The system uses **three collaborative AI agents**.

### Analyst Agent
Detects volatility spikes and overbought conditions using technical indicators.

### Model Agent
Evaluates short probability using ML models and generates ranking scores.

### Risk Agent
Assesses exposure and generates explainable narratives for decisions.

Agents communicate using **LangGraph state machines and shared vector memory**.

---

# 🏗 System Architecture

```
Market Data
    │
    ▼
Feature Engineering
(Pandas + Technical Indicators)
    │
    ▼
ML Model Pipeline
(Logistic Regression + LightGBM)
    │
    ▼
Vector Encoding
(Qdrant)
    │
    ▼
Multi-Agent Reasoning
(LangGraph Agents)
    │
    ▼
Trading Signals
```

---

# 🔧 My Contributions

## Vector Search System (Qdrant)

• Built semantic vector search pipeline  
• Encoded financial signals as embeddings  
• Implemented similarity retrieval for market pattern detection  
• Optimized query latency for agent decision workflows  

---

## Data Engineering Pipeline

Processed **~5GB stock dataset from Kaggle**

Implemented:

• OHLCV feature engineering  
• technical indicators (RSI, MA ratios, volatility)  
• data cleaning and validation  

Integrated **Hadoop HDFS distributed storage** on a **2-node Vultr cluster**.

---

## Multi-Agent Architecture

Designed and implemented **LangGraph StateGraph workflow**.

Agents:

Analyst Agent  
Model Agent  
Risk Agent  

Implemented inter-agent communication and state management.

---

# 📊 Key Results

| Metric | Value |
|------|------|
AUROC | 0.642  
Precision@10 | 0.60  
Backtest Return | **18%**  
Top Candidate | CMAX (94.5%)  
Dataset Size | ~5GB  

---

# 🛠 Tech Stack

| Component | Technology |
|------|------|
Agent Framework | LangGraph  
Vector Database | Qdrant  
Machine Learning | Logistic Regression + LightGBM  
Data Processing | Pandas  
Distributed Storage | Hadoop HDFS  
Visualization | Streamlit + Tableau  
Infrastructure | Vultr Cloud  

---

# 🚀 Quick Start

Clone repository

```
git clone https://github.com/mrudula1501/Synapse-Street.git
cd Synapse-Street
```

Install dependencies

```
pip install -r requirements.txt
```

Run dashboard

```
streamlit run app.py
```

Dashboard will open at

```
http://localhost:8501
```

---

# 📁 Repository Structure

```
Synapse-Street
│
├── app.py
├── hackathon_stock.ipynb
├── model_pipeline.pkl
├── requirements.txt
│
├── data
│   ├── picks.csv
│   ├── today_scores.csv
│   ├── metrics.csv
│   └── equity_curve.csv
│
├── artifacts
│   └── narrative.txt
│
├── dashboards
│   └── Tableau Dashboard.pdf
│
└── presentation
    └── SYNAPSE_STREET.pptx
```

---

# 📈 Model Pipeline

1️⃣ Load historical stock data  
2️⃣ Compute technical indicators  
3️⃣ Train logistic regression model  
4️⃣ Convert signals to embeddings  
5️⃣ Retrieve similar market patterns  
6️⃣ Run multi-agent reasoning  
7️⃣ Output ranked short opportunities

---

# 💡 Key Learnings

• Multi-agent reasoning improves decision quality  
• Vector search enables fast pattern retrieval  
• Distributed data pipelines scale financial datasets  
• Explainable outputs improve trust in AI trading systems

---

# 🔮 Future Work

• Real-time market data APIs  
• Reinforcement learning trading agents  
• Portfolio optimization models  
• risk-adjusted performance metrics  
• live deployment on HuggingFace Spaces  

---

# 👥 Team

| Name | Role |
|------|------|
Siddharth Adhikari | ML & Agent Framework  
Sathwick Kiran M S | Infrastructure  
Kundan Satkar | Data Processing  
Mrudula Deshmukh | Vector Search & Data Engineering  

---

# 📄 License

This project builds on the original **UB Hacking 2024 repository**.

See original repo for license details.
