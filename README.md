# Synapse Street
**AI multi-agent system detecting stock market short opportunities using LangGraph agents, Qdrant vector search, and HDFS pipelines.**

> **Original Project**: UB Hacking 2024 | **Contributors**: Siddharth Adhikari, Sathwick Kiran M S, Kundan Satkar, Mrudula Deshmukh

---

## 🎯 Overview

Synapse Street is an AI-powered multi-agent system that detects potential short-selling opportunities in the U.S. stock market by combining machine learning, large language models, and vector databases.

Inspired by *The Big Short*, this project autonomously analyzes market data and delivers interpretable results through interactive dashboards. **Achieved 18% backtest returns** over the evaluation period.

---

## 🔧 My Core Contributions

### **Vector Search & Semantic Retrieval (Qdrant)**
- Designed and implemented vector database architecture using Qdrant for contextual market signal retrieval
- Engineered embedding pipeline to encode financial metrics (RSI, Moving Average ratios, volatility signals)
- Built semantic search queries to find similar market conditions across historical data
- Optimized query latency for real-time agent decision-making

### **Data Engineering Pipeline (Pandas + Hadoop HDFS)**
- Architected ETL pipeline to process ~5GB U.S. stock market dataset from Kaggle
- Implemented feature engineering workflows with Pandas (OHLCV normalization, technical indicators)
- Integrated Hadoop HDFS distributed storage on 2-node Vultr cluster for scalable data management
- Performed data validation, deduplication, and quality assurance on millions of records

### **Multi-Agent Orchestration (LangGraph)**
- Collaborated on designing StateGraph architecture for 3 autonomous AI agents:
  - **Analyst Agent**: Detects volatility spikes and overbought market conditions
  - **Model Agent**: Evaluates short probabilities from ML pipeline and generates risk scores
  - **Risk Agent**: Assesses portfolio exposure and creates human-readable narratives
- Implemented inter-agent communication patterns and state management

---

## 📊 Key Results & Metrics

| Metric | Value |
|--------|-------|
| **AUROC** | 0.642 |
| **Precision@10** | 0.60 |
| **Backtest Returns** | 18% |
| **Top Short Candidate** | CMAX (94.5% probability) |
| **Data Processed** | ~5GB (50K+ stocks) |

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Multi-Agent Framework** | LangGraph |
| **Vector Database** | Qdrant |
| **Machine Learning** | Scikit-learn (Logistic Regression), LightGBM |
| **Data Processing** | Pandas |
| **Big Data Storage** | Hadoop HDFS |
| **Visualization** | Streamlit, Tableau |
| **Cloud Infrastructure** | Vultr (2-node cluster) |
| **Deployment** | HuggingFace Spaces |

---

## 📁 Project Structure

```
Synapse-Street/
├── app.py                      # Streamlit dashboard application
├── hackathon_stock.ipynb       # Data processing & ML pipeline notebook
├── model_pipeline.pkl          # Trained Logistic Regression model
├── requirement.txt             # Python dependencies
│
├── Data Artifacts/
│   ├── picks.csv               # Top 10 short candidates
│   ├── today_scores.csv        # All analyzed tickers with probabilities
│   ├── metrics.csv             # Model evaluation metrics
│   ├── equity_curve.csv        # Backtest performance curve
│   └── narrative.txt           # AI-agent reasoning summary
│
└── Presentations/
    ├── SYNAPSE_STREET.pptx     # Project presentation
    └── Tableau Dashboard.pdf   # Performance analytics dashboard
```

---

## 🚀 How to Run Locally

### **1. Clone the Repository**
```bash
git clone https://github.com/mrudula1501/Synapse-Street.git
cd Synapse-Street
```

### **2. Install Dependencies**
```bash
pip install -r requirement.txt
```

### **3. Run Streamlit Dashboard**
```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

### **4. View Results**
- **picks.csv** - Top 10 short opportunities
- **today_scores.csv** - Full analysis results
- **Tableau Dashboard.pdf** - Visual analytics

---

## 📈 Model Pipeline

1. **Data Ingestion**: Load historical OHLCV data from Kaggle
2. **Feature Engineering**: Calculate technical indicators (RSI, MA, volatility)
3. **Model Training**: Logistic Regression on normalized features
4. **Vector Encoding**: Convert signals to embeddings for semantic search
5. **Agent Analysis**: 
   - Analyst identifies high-volatility candidates
   - Model scores short probabilities
   - Risk agent validates exposure
6. **Output**: Rankings and narratives for top opportunities

---

## 💡 Key Insights & Learnings

- **Multi-Agent Design**: Successfully orchestrated 3 LLM agents to reason about financial data collaboratively
- **Vector Search in Finance**: Qdrant embeddings enabled fast retrieval of similar market patterns
- **Scalable Data Pipeline**: HDFS integration demonstrated handling 5GB+ datasets in production workflows
- **Speed vs. Interpretability**: Balanced rapid prototyping with explainable AI outputs during 15-hour hackathon
- **Full-Stack Development**: Integrated ML pipeline, vector DB, agent framework, and dashboards into one cohesive system

---

## 🎯 Future Enhancements

- [ ] Real-time stock APIs (Polygon, Alpha Vantage, IEX Cloud)
- [ ] Expand to 5+ agents (News Sentiment, Portfolio Optimization, Risk Management)
- [ ] LLM commentary generation (GPT-4/Claude API for market summaries)
- [ ] Risk-adjusted metrics (Sharpe Ratio, Maximum Drawdown, Sortino Ratio)
- [ ] Live Streamlit deployment on HuggingFace Spaces
- [ ] Backtesting framework (Backtrader/VectorBT)
- [ ] Database integration (PostgreSQL for historical tracking)

---

## 📚 External Resources

- **Dataset**: [Kaggle - U.S. Stock Market History](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)
- **Tableau Dashboard**: [Public Link](https://public.tableau.com/views/Book1_17626741383510/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)
- **Original Repository**: [Sathwick17/ub_hackers](https://github.com/Sathwick17/ub_hackers)

---

## 👥 Team

| Name | Role | GitHub |
|------|------|--------|
| **Siddharth Adhikari** | ML & Agent Framework | [@siddhyaaddy](https://github.com/siddhyaaddy) |
| **Sathwick Kiran M S** | Lead & Infrastructure | [@Sathwick17](https://github.com/Sathwick17) |
| **Kundan Satkar** | Data Processing | [@KundanS18](https://github.com/KundanS18) |
| **Mrudula Deshmukh** | Vector Search & Data Engineering | [@mrudula1501](https://github.com/mrudula1501) |

---

## 📄 License

This project builds on the original UB Hacking 2024 project. Please see the original repository for licensing details.

---

**Last Updated**: January 2026 | **Status**: Complete & Documented
