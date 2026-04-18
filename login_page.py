from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = 'input[name="username"]'
        self.password = 'input[name="password"]'
        self.login_btn = 'button[type="submit"]'

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self):
        self.page.fill(self.username, "Admin")
        self.page.fill(self.password, "admin123")
        self.page.click(self.login_btn)
        
        # Wait for dashboard
        self.page.wait_for_selector('//h6[text()="Dashboard"]')
        print("✅ Login successful")