from playwright.sync_api import Page
import time

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_admin(self):
        print("Navigating to Admin...")
        
        # Language-independent: Use href attribute
        admin_link = self.page.locator('a[href*="admin/viewAdminModule"]')
        
        if admin_link.count() == 0:
            # Fallback: First menu item
            admin_link = self.page.locator('.oxd-main-menu-item-wrapper').first.locator('a')
        
        admin_link.click()
        self.page.wait_for_selector('.oxd-table', timeout=10000)
        print("✅ Admin page loaded")

    def add_user(self, username):
        print("Adding user...")
        
        # Add button
        self.page.click('//button[normalize-space()="Add"]')
        self.page.wait_for_selector('//label[text()="Username"]', timeout=10000)
        
        # Employee field
        emp = self.page.locator('//input[@placeholder="Type for hints..."]')
        emp.click()
        emp.fill("s")
        self.page.wait_for_timeout(3000)
        self.page.wait_for_selector('//div[@role="option"]', timeout=10000)
        self.page.locator('//div[@role="option"]').first.click()
        print("Employee selected ✅")
        
        # Fill form
        self.page.locator('.oxd-select-wrapper').nth(0).click()
        self.page.click('//span[text()="ESS"]')
        self.page.fill('//label[text()="Username"]/following::input[1]', username)
        self.page.locator('.oxd-select-wrapper').nth(1).click()
        self.page.click('//span[text()="Enabled"]')
        self.page.fill('(//input[@type="password"])[1]', "Test@1234")
        self.page.fill('(//input[@type="password"])[2]', "Test@1234")
        
        # Submit
        self.page.click('//button[@type="submit"]')
        
        # Wait for success toast OR table
        try:
            self.page.wait_for_selector('//p[contains(@class, "oxd-text--toast-message")]', timeout=5000)
            print("✅ Success toast detected")
            self.page.wait_for_timeout(2000)
        except:
            print("ℹ️ No toast, waiting for table...")
        
        # Wait for table
        self.page.wait_for_selector('.oxd-table', timeout=15000)
        print("User created ✅")

    def search_user(self, username):
        print(f"🔍 Searching user: {username}...")
        self.page.wait_for_selector('.oxd-table', timeout=10000)
        
        # Reset button
        try:
            reset_btn = self.page.locator('//button[normalize-space()="Reset"]')
            if reset_btn.is_visible():
                reset_btn.click()
                self.page.wait_for_timeout(1000)
                print("Reset clicked")
        except:
            pass
        
        # Username search field
        search_input = self.page.locator('input.oxd-input').nth(1)
        if search_input.count() == 0:
            search_input = self.page.get_by_placeholder("Type for hints...").first
        
        search_input.wait_for(state="visible", timeout=5000)
        search_input.click()
        search_input.fill(username)
        print(f"✅ Username '{username}' entered")
        
        # Search button
        search_button = self.page.locator('button[type="submit"]').first
        if search_button.count() == 0:
            search_button = self.page.locator('button.oxd-button--secondary').first
        
        search_button.wait_for(state="visible", timeout=5000)
        search_button.click()
        print("✅ Search button clicked")
        
        self.page.wait_for_timeout(2000)
        print(f"🔍 Search executed for: {username}")

    def verify_user_exists_qa(self, username, should_exist=True):
        print("\n" + "="*60)
        print(f"🔎 QA VERIFICATION: Checking if user '{username}' exists")
        print("="*60)
        
        try:
            self.page.wait_for_selector('.oxd-table-body', timeout=5000)
        except:
            print(f"ℹ️ INFO: Table body not found")
            user_found = False
        else:
            rows = self.page.locator('.oxd-table-body .oxd-table-row')
            count = rows.count()
            
            if count == 0:
                print(f"ℹ️ INFO: No records found in table")
                user_found = False
            else:
                user_found = False
                for i in range(count):
                    row_text = rows.nth(i).inner_text()
                    if username in row_text:
                        user_found = True
                        print(f"ℹ️ INFO: User '{username}' found in row {i+1}")
                        break
        
        if should_exist:
            if user_found:
                print(f"✅✅✅ PASS: User '{username}' FOUND successfully!")
                print("="*60)
                return True
            else:
                print(f"❌❌❌ FAIL: User '{username}' NOT FOUND!")
                print("="*60)
                return False
        else:
            if not user_found:
                print(f"✅✅✅ PASS: User '{username}' NOT FOUND (Deleted successfully)!")
                print("="*60)
                return True
            else:
                print(f"❌❌❌ FAIL: User '{username}' STILL EXISTS (Should be deleted)!")
                print("="*60)
                return False

    def edit_user_qa(self, username, new_status="Enabled", new_password="Updated@1234"):
        print("\n" + "="*60)
        print(f"✏️ QA EDIT: Updating user '{username}'")
        print("="*60)
        
        print(f"🔍 Step 1: Searching user before edit...")
        self.search_user(username)
        self.page.wait_for_timeout(2000)
        
        if not self.user_exists(username):
            print(f"❌ FAIL: User '{username}' not found for editing!")
            return False
        
        print(f"✏️ Step 2: Clicking pencil/edit icon...")
        rows = self.page.locator('.oxd-table-body .oxd-table-row')
        count = rows.count()
        
        edit_clicked = False
        for i in range(count):
            row_text = rows.nth(i).inner_text()
            if username in row_text:
                buttons = rows.nth(i).locator('button')
                if buttons.count() >= 2:
                    buttons.nth(1).click()
                    edit_clicked = True
                    print(f"✅ Pencil icon clicked for row {i+1}")
                break
        
        if not edit_clicked:
            print(f"❌ FAIL: Could not find pencil/edit icon!")
            return False
        
        self.page.wait_for_selector('//h6[text()="Edit User"]', timeout=10000)
        print(f"✅ Edit form loaded")
        
        print(f"📝 Step 3: Changing status to '{new_status}'...")
        self.page.locator('.oxd-select-wrapper').nth(1).click()
        self.page.click(f'//span[text()="{new_status}"]')
        print(f"✅ Status updated")
        
        print(f"🔐 Step 4: Handling password change...")
        try:
            change_password_checkbox = self.page.locator('//input[@type="checkbox"]')
            if change_password_checkbox.count() > 0:
                if not change_password_checkbox.is_checked():
                    change_password_checkbox.click()
                    print("✅ 'Change Password' checkbox checked")
                    self.page.wait_for_timeout(500)
                
                password_fields = self.page.locator('//input[@type="password"]')
                if password_fields.count() >= 2:
                    password_fields.nth(0).fill(new_password)
                    password_fields.nth(1).fill(new_password)
                    print(f"✅ Password updated to: {new_password}")
                else:
                    print("ℹ️ Password fields not found, skipping password update")
            else:
                print("ℹ️ 'Change Password' checkbox not found, skipping password update")
        except Exception as e:
            print(f"⚠️ Could not update password: {e}")
        
        print(f"💾 Step 5: Saving changes...")
        save_button = self.page.locator('//button[@type="submit"]').first
        save_button.wait_for(state="visible", timeout=5000)
        save_button.click()
        
        try:
            self.page.wait_for_selector('//p[contains(@class, "oxd-text--toast-message")]', timeout=10000)
        except:
            pass
        
        self.page.wait_for_selector('.oxd-table', timeout=15000)
        self.page.wait_for_timeout(2000)
        
        print(f"✅✅✅ User '{username}' updated successfully!")
        print("="*60)
        return True

    def delete_user_qa(self, username):
        print("\n" + "="*60)
        print(f"🗑️ QA DELETE: Removing user '{username}'")
        print("="*60)
        
        print(f"🔍 Step 1: Searching user before delete...")
        self.search_user(username)
        self.page.wait_for_timeout(2000)
        
        if not self.user_exists(username):
            print(f"❌ FAIL: User '{username}' not found for deletion!")
            return False
        
        print(f"🗑️ Step 2: Clicking dustbin/delete icon...")
        rows = self.page.locator('.oxd-table-body .oxd-table-row')
        count = rows.count()
        
        delete_clicked = False
        for i in range(count):
            row_text = rows.nth(i).inner_text()
            if username in row_text:
                buttons = rows.nth(i).locator('button')
                if buttons.count() >= 1:
                    buttons.nth(0).click()
                    delete_clicked = True
                    print(f"✅ Dustbin icon clicked for row {i+1}")
                break
        
        if not delete_clicked:
            print(f"❌ FAIL: Could not find dustbin/delete icon!")
            return False
        
        print(f"⚠️ Step 3: Confirmation popup appeared")
        confirm_btn = self.page.locator('//button[normalize-space()="Yes, Delete"]')
        confirm_btn.wait_for(state="visible", timeout=5000)
        print(f"👉 Clicking 'Yes, Delete' button...")
        confirm_btn.click()
        
        # Wait for success toast
        try:
            self.page.wait_for_selector('//p[contains(@class, "oxd-text--toast-message")]', timeout=5000)
            self.page.wait_for_timeout(1000)
        except:
            pass
        
        self.page.wait_for_selector('.oxd-table', timeout=15000)
        self.page.wait_for_timeout(2000)
        
        print(f"✅✅✅ User '{username}' deleted successfully!")
        print("="*60)
        return True

    def user_exists(self, username):
        try:
            self.page.wait_for_selector('.oxd-table-body', timeout=5000)
        except:
            return False
        
        rows = self.page.locator('.oxd-table-body .oxd-table-row')
        count = rows.count()
        
        if count == 0:
            return False
        
        for i in range(count):
            row_text = rows.nth(i).inner_text()
            if username in row_text:
                print(f"User found in row {i+1}")
                return True
        
        print("User not found")
        return False
    