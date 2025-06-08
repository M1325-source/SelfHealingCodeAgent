import streamlit as st
from monitor.anomaly_detector import detect_anomaly
from agent.llm_fix_agent import suggest_fix
from cicd.create_pr import create_pull_request

st.set_page_config(page_title="🛠️ Self-Healing Code Agent", layout="centered")

st.title("🤖 Self-Healing Code Agent for DevOps")

if st.button("Start Log Monitoring"):
    error = detect_anomaly("logs/sample_log.txt")
    if error:
        st.error(f"🚨 Anomaly Detected:\n\n{error}")
        fix = suggest_fix(error)
        st.success("✅ Suggested Fix:")
        st.code(fix, language="python")
        st.info("Creating Pull Request...")
        create_pull_request(fix)
    else:
        st.success("✅ No anomalies found.")
