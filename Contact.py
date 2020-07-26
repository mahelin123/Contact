from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCantast():
    def setup(self):
        desire_cap = {
            "deviceName": "127.0.0.1:7555",
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset":"True"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

        contast = self.driver.find_element(By.XPATH, '//*[@resource-id="com.tencent.wework:id/dyx" and @text="通讯录"]')
        contast.click()

    def teardown(self):
        self.driver.quit()

    def test_add_contacts(self):
        """
        1、通讯录页面点击添加成员按钮跳转到添加成员页面
        2、添加成员页面点击手动输入添加
        3、输入姓名、手机号，选择部门
        4、点击保存
        :return:
        """
        add_member = self.driver.find_element(By.XPATH, '//*[@text="添加成员"]')
        add_member.click()

        add_manully = self.driver.find_element(By.XPATH, '//*[@text="手动输入添加"]')
        add_manully.click()

        add_name = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText")
        add_name.send_keys("霍格沃兹_5")
        add_mobile = self.driver.find_element_by_id("com.tencent.wework:id/f1e")
        add_mobile.send_keys("14000000005")
        add_department = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[6]/android.widget.RelativeLayout/android.widget.RelativeLayout")
        add_department.click()
        click_ok = self.driver.find_element_by_id("com.tencent.wework:id/g09")
        click_ok.click()

        click_save = self.driver.find_element_by_id("com.tencent.wework:id/h9w")
        click_save.click()
        # 返回到通讯录页面
        locator=(By.ID,"com.tencent.wework:id/h9e")
        el1=WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(locator))
        el1.click()

        name = self.driver.find_element_by_xpath('//*[@text="霍格沃兹_5"]').get_attribute("text")
        assert name == "霍格沃兹_5"

    def test_delete_contacts(self):
        """
        1、先点击要删除的人名，进入到个人信息页面
        2、点击右上角-＞点击编辑成员，进入编辑成员页面
        3、点击删除按钮

        :return:
        """
        name = self.driver.find_element_by_xpath('//*[@text="霍格沃兹_5"]')
        name.click()

        #个人信息页面点击右上角更多按钮
        more_button=self.driver.find_element_by_id("com.tencent.wework:id/h9p")
        more_button.click()

        edit_member=self.driver.find_element_by_xpath('//*[@text="编辑成员"]')
        edit_member.click()

        delete_member=self.driver.find_element_by_xpath('//*[@text="删除成员"]')
        delete_member.click()
        #点击确定按钮
        determine=self.driver.find_element_by_xpath('//*[@text="确定"]')
        determine.click()
        sleep(5)
        # assert "霍格沃兹_5" not in name






