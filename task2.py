# =================================================================
# PROJECT: Cloud Monitoring & Alerting System
# DESCRIPTION: Configuring CloudWatch metrics, Dashboards, and Alarms.
# DELIVERABLE: A monitoring engine with threshold-based alerts.
# =================================================================

import time
import random

class CloudWatchMonitor:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.threshold = 85.0  # Alert if CPU > 85%
        self.metrics_history = []
        print(f"📡 Monitoring Started for Instance: {self.instance_id}")

    def get_cpu_utilization(self):
        """Simulates fetching real-time CPU metrics from the cloud."""
        return round(random.uniform(10.0, 95.0), 2)

    def create_dashboard(self):
        """Simulates generating a CloudWatch Dashboard view."""
        print("\n" + "="*45)
        print(f"📊 CLOUD MONITORING DASHBOARD: {self.instance_id}")
        print("="*45)
        print(f"{'TIMESTAMP':<20} | {'CPU %':<10} | {'STATUS'}")
        print("-" * 45)
        
        for metric in self.metrics_history[-5:]: # Show last 5 metrics
            status = "🔴 ALARM" if metric['value'] > self.threshold else "🟢 OK"
            print(f"{metric['time']:<20} | {metric['value']:<10} | {status}")
        print("="*45)

    def trigger_alert(self, value):
        """Simulates SNS (Simple Notification Service) Alert."""
        print(f"\n🚨 [CRITICAL ALERT] CPU Utilization is {value}%!")
        print(f"📧 Sending Notification to Administrator (aditya@soit.edu)...")
        print(f"📟 Status: AUTO-SCALING TRIGGERED to handle load.")

    def run_monitor_cycle(self):
        """Main monitoring loop."""
        current_val = self.get_cpu_utilization()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        self.metrics_history.append({"time": timestamp, "value": current_val})
        
        # Check for Alarm Threshold
        if current_val > self.threshold:
            self.trigger_alert(current_val)
        else:
            print(f"ℹ️ Metric Logged: {current_val}% (Healthy)")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Initialize Monitor for our App Server
    monitor = CloudWatchMonitor("i-0abc123def456")

    # 2. Simulate 5 monitoring cycles (Checking metrics every 'pulse')
    print("🔄 Running real-time cloud health checks...")
    for _
