from monitor.anomaly_detector import detect_anomaly
from agent.llm_fix_agent import suggest_fix
from cicd.create_pr import create_pull_request

def main():
    print("📊 Monitoring Logs...")
    error = detect_anomaly("logs/sample_log.txt")
    if error:
        print(f"\n🚨 Anomaly Detected: {error}")
        fix = suggest_fix(error)
        create_pull_request(fix)
    else:
        print("✅ No anomalies found.")

if __name__ == "__main__":
    main()
