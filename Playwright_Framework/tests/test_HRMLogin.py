from pages.HRM_LoginPage import Login_Page
from playwright.sync_api import Page

def test_hrm_Login(page:Page)-> None:
    login_obj = Login_Page(page)

    login_obj.login_application("Admin","admin123")