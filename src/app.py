import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Stock Short Finder", page_icon="🧠", layout="wide")

# Header
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 40px; border-radius: 15px; margin-bottom: 30px; text-align: center;'>
    <h1 style='color: white; font-size: 48px; margin: 0;'>🧠 AI Stock Short Finder</h1>
    <p style='color: white; font-size: 20px; margin-top: 10px;'>Multi-Agent Analysis with Vector Search</p>
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    picks = pd.read_csv('picks.csv')
    
    # Load metrics - fix the column reference
    metrics_df = pd.read_csv('metrics.csv', header=None, index_col=0)
    # Use .iloc to get the first column by position
    metrics = {k: float(v) for k, v in metrics_df.iloc[:, 0].items()}
    
    try:
        equity = pd.read_csv('equity_curve.csv')
    except:
        equity = pd.DataFrame()
    
    try:
        with open('narrative.txt') as f:
            narrative = f.read()
    except:
        narrative = "Not available"
    
    return picks, metrics, equity, narrative

picks, metrics, equity, narrative = load_data()

# Metrics
st.subheader("📊 Model Performance")
col1, col2, col3, col4 = st.columns(4)
col1.metric("AUROC", f"{metrics.get('auroc', 0):.3f}")
col2.metric("PR-AUC", f"{metrics.get('pr_auc', 0):.3f}")
col3.metric("Best Threshold", f"{metrics.get('best_thr', 0):.2f}")
col4.metric("Precision@10", f"{metrics.get('precision@10', 0):.1%}")

st.markdown("---")

# Chart
st.subheader("🎯 Top 10 Short Candidates")
fig = px.bar(picks, x='ticker', y='prob', color='prob',
             color_continuous_scale='Reds',
             title='Short Probability by Stock',
             text=[f"{p:.1%}" for p in picks['prob']])
fig.update_traces(textposition='outside')
fig.update_layout(height=500, showlegend=False, xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# Table
st.subheader("📋 Detailed Analysis")
display_df = picks[['ticker', 'prob', 'rsi14', 'ma_ratio', 'rvol20']].copy()
st.dataframe(
    display_df.style.format({
        'prob': '{:.2%}',
        'rsi14': '{:.2f}',
        'ma_ratio': '{:.3f}',
        'rvol20': '{:.4f}'
    }),
    use_container_width=True
)

# Narrative
with st.expander("🤖 AI Agent Analysis Narrative"):
    st.text(narrative)

# Backtest
if not equity.empty and 'equity' in equity.columns:
    st.subheader("📈 Backtest Performance")
    
    final_return = (equity['equity'].iloc[-1] - 1) * 100
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=equity['step'], 
        y=equity['equity'],
        mode='lines', 
        fill='tozeroy',
        line=dict(color='#667eea', width=3)
    ))
    fig.add_hline(y=1.0, line_dash="dash", line_color="gray")
    fig.update_layout(
        title=f'Equity Curve - Return: {final_return:+.2f}%',
        xaxis_title='Trading Day',
        yaxis_title='Equity Multiple',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Tech Stack:</strong> LangGraph • Qdrant • Scikit-learn • Plotly</p>
</div>
""", unsafe_allow_html=True)
