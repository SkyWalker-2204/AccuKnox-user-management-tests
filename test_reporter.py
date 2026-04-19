from datetime import datetime
import json
import os

class QATestReporter:
    def __init__(self, test_name='User Management CRUD Flow'):
        self.test_name = test_name
        self.browser = 'Chromium'
        self.start_time = None
        self.end_time = None
        self.steps = []
        self.status = 'PENDING'
        
    def start_test(self):
        self.start_time = datetime.now()
        self.steps = []
        self.status = 'RUNNING'
        
    def add_step(self, step_num, description, status):
        self.steps.append({
            'step': step_num,
            'description': description,
            'status': status,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
        
    def end_test(self, status='PASSED'):
        self.end_time = datetime.now()
        self.status = status
        
    def get_execution_time(self):
        if self.start_time and self.end_time:
            return round((self.end_time - self.start_time).total_seconds(), 2)
        return 0
    
    def generate_console_report(self):
        print('\n' + '='*50)
        print('🧪 QA TEST EXECUTION REPORT')
        print('='*50)
        print(f'Test Case: {self.test_name}')
        print(f'Browser: {self.browser}')
        print(f'Date: {self.start_time.strftime("%Y-%m-%d %H:%M:%S") if self.start_time else "N/A"}')
        print('\nTest Steps:')
        for step in self.steps:
            icon = '✅' if step['status'] == 'PASS' else '❌'
            print(f"{step['step']}. {icon} {step['description']} -> {step['status']}")
        print('\n' + '-'*50)
        icon = '✅' if self.status == 'PASSED' else '❌'
        print(f'Final Result: {icon} {self.status}')
        print(f'Execution Time: {self.get_execution_time()} seconds')
        print('='*50)
        
    def generate_html_report(self, filename='test_report.html'):
        os.makedirs('reports', exist_ok=True)
        filepath = os.path.join('reports', filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f'<html><body><h1>QA Report - {self.test_name}</h1><p>Status: {self.status}</p></body></html>')
        print(f'\n📄 HTML Report: {filepath}')
        return filepath
    
    def generate_json_report(self, filename='test_report.json'):
        os.makedirs('reports', exist_ok=True)
        filepath = os.path.join('reports', filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({'test_name': self.test_name, 'status': self.status, 'steps': self.steps}, f, indent=2)
        print(f'📄 JSON Report: {filepath}')
        return filepath