from playwright.sync_api import Playwright, Page, expect

class Login_Page:
    
    def __init__(self, page:Page):
        self.page = page

        self.userName = page.get_by_role("textbox", name= "username")
        self.password = page.get_by_role("textbox", name= "password")
        self.loginBtn = page.get_by_role("button", name= "Login")
    
    def login_application(self,username:str,password:str) -> None:
        self.userName.fill(username)
        self.password.fill(password)
        self.loginBtn.click
    





   