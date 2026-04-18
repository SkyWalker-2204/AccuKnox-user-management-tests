import time
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

class TestUserManagement:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.admin = AdminPage(page)
        
        # Login
        self.login_page.navigate()
        self.login_page.login()
        
        yield

    def test_complete_qa_flow(self, page: Page):
        username = f"qauser_{int(time.time())}"
        
        print("\n" + "🧪" * 30)
        print("QA TEST EXECUTION STARTED")
        print("🧪" * 30)
        
        # Step 1: Go to Admin
        print("\n[STEP 1] Navigating to Admin page...")
        self.admin.go_to_admin()
        
        # Step 2: Create user
        print(f"\n[STEP 2] Creating new user: {username}")
        self.admin.add_user(username)
        time.sleep(2)
        
        # Step 3: Search & Verify
        print(f"\n[STEP 3] Search & Verify created user")
        self.admin.search_user(username)
        assert self.admin.verify_user_exists_qa(username, should_exist=True)
        
        # Step 4: Edit user
        print(f"\n[STEP 4] Edit user")
        assert self.admin.edit_user_qa(username, new_status="Enabled")
        
        # Step 5: Search after edit
        print(f"\n[STEP 5] Search after edit")
        self.admin.search_user(username)
        assert self.admin.verify_user_exists_qa(username, should_exist=True)
        
        # Step 6: Delete user
        print(f"\n[STEP 6] Delete user")
        assert self.admin.delete_user_qa(username)
        
        # Step 7: Verify deletion
        print(f"\n[STEP 7] Verify deletion")
        self.admin.search_user(username)
        assert self.admin.verify_user_exists_qa(username, should_exist=False)
        
        print("\n" + "🎉" * 30)
        print("🎉 ALL QA TESTS PASSED! 🎉")
        print("🎉" * 30)