import psutil
import datetime
import os
import csv

class QuantumFlow:
    def __init__(self):
        self.report_data = []

    def gather_system_processes(self):
        process_info = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time']):
            try:
                with proc.oneshot():
                    pid = proc.info['pid']
                    name = proc.info['name']
                    username = proc.info['username']
                    cpu_percent = proc.info['cpu_percent']
                    memory_info = proc.info['memory_info']
                    create_time = datetime.datetime.fromtimestamp(proc.info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
                    process_info.append((pid, name, username, cpu_percent, memory_info, create_time))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process_info

    def gather_application_activity(self):
        # Placeholder for future implementation
        # To track application-specific activities, external modules or APIs would be needed
        return []

    def generate_report(self):
        self.report_data = self.gather_system_processes()
        self.save_report_to_csv()

    def save_report_to_csv(self):
        report_name = f"QuantumFlow_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(report_name, mode='w', newline='') as report_file:
            report_writer = csv.writer(report_file)
            report_writer.writerow(['PID', 'Process Name', 'Username', 'CPU Usage (%)', 'Memory Usage', 'Start Time'])
            for process in self.report_data:
                report_writer.writerow(process)
        print(f"Report generated: {report_name}")

if __name__ == '__main__':
    qf = QuantumFlow()
    qf.generate_report()