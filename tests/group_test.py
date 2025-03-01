import unittest
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from base_test_class import BaseTestCase
from user_test import UserTest


class GroupTest(BaseTestCase):

    def test_create_group(self):
        # Login to the site.
        driver = self.driver
        # Navigate to the Group managegement page
        driver.get(self.base_url + "group")
        # "Click" the dropdown button to see options
        driver.find_element_by_id("dropdownMenu1").click()
        # "Click" the add group button
        driver.find_element_by_link_text("New Group").click()
        # Fill in the Necessary group Details
        # name
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Group Name")
        # "Click" the submit button to complete the transaction
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # Assert status is success
        self.assertTrue(self.is_success_message_present(text='Group was added successfully.'))

    def test_group_edit_name_and_global_role(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to Group Management page
        driver.get(self.base_url + "group")
        # Select the previously created group to edit
        # The name is not clickable
        # so we would have to select specific group by filtering list of groups
        driver.find_element_by_id("show-filters").click()
        # Insert name to filter by into name box
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Group Name")
        # click on 'apply filter' button
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        # only the needed group is now available, proceed with opening the context menu and clicking 'Edit' button
        driver.find_element_by_id("dropdownMenuGroup").click()
        driver.find_element_by_id("editGroup").click()
        # Edit name
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Another Name")
        # Select the role 'Reader'
        Select(driver.find_element_by_id("id_role")).select_by_visible_text("Reader")
        # "Click" the submit button to complete the transaction
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

        # Assert status is success
        self.assertTrue(self.is_success_message_present(text='Group saved successfully.'))

    def test_add_group_member(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to Group Management page
        driver.get(self.base_url + "group")
        # Select and click on the particular group to view
        driver.find_element_by_link_text("Another Name").click()
        # Open the menu to add users and click the 'Add' button
        driver.find_element_by_id("dropdownMenuAddGroupMember").click()
        driver.find_element_by_id("addGroupMember").click()
        # Select the user 'propersahm'
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'id_users_chosen')))
        except TimeoutException:
            self.fail('Timed out waiting for products dropdown to initialize ')
        driver.execute_script("document.getElementsByName('users')[0].style.display = 'inline'")
        element = driver.find_element_by_xpath("//select[@name='users']")
        user_option = element.find_elements_by_tag_name('option')[0]
        Select(element).select_by_value(user_option.get_attribute("value"))
        # Select the role 'Reader'
        Select(driver.find_element_by_id("id_role")).select_by_visible_text("Reader")
        # "Click" the submit button to complete the transaction
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text='Group members added successfully.'))
        # Query the site to determine if the member has been added
        self.assertEqual(driver.find_elements_by_name("member_user")[1].text, "Proper Samuel (propersahm)")
        self.assertEqual(driver.find_elements_by_name("member_role")[1].text, "Reader")

    def test_edit_group_member(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to Group Management page
        driver.get(self.base_url + "group")
        # Select and click on the particular group to view
        driver.find_element_by_link_text("Another Name").click()
        # Open the menu to manage members and click the 'Edit' button
        driver.find_elements_by_name("dropdownManageGroupMembers")[1].click()
        driver.find_elements_by_name("editGroupMember")[1].click()
        # Select the role 'Maintainer'
        Select(driver.find_element_by_id("id_role")).select_by_visible_text("Maintainer")
        # "Click" the submit button to complete the transaction
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text='Group member updated successfully'))
        # Query the site to determine if the member has been edited
        self.assertEqual(driver.find_elements_by_name("member_user")[1].text, "Proper Samuel (propersahm)")
        self.assertEqual(driver.find_elements_by_name("member_role")[1].text, "Maintainer")

    def test_delete_group_member(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to Group Management page
        driver.get(self.base_url + "group")
        # Select and click on the particular group to view
        driver.find_element_by_link_text("Another Name").click()
        # Open the menu to manage members and click the 'Delete' button
        driver.find_elements_by_name("dropdownManageGroupMembers")[1].click()
        driver.find_elements_by_name("deleteGroupMember")[1].click()
        # "Click" the submit button to complete the transaction
        driver.find_element_by_css_selector("input.btn.btn-danger").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text='Group member deleted successfully.'))

    def test_group_delete(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to the Group management page
        driver.get(self.base_url + "group")
        # Select the previously created group to edit
        # The name is not clickable
        # so we would have to select specific group by filtering list of groups
        driver.find_element_by_id("show-filters").click()
        # Insert name to filter by into name box
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Another Name")
        # click on 'apply filter' button
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        # only the needed group is now available, proceed with clicking 'Delete' button
        driver.find_element_by_id("dropdownMenuGroup").click()
        driver.find_element_by_id("deleteGroup").click()
        # confirm deletion, by clicking delete a second time
        driver.find_element_by_css_selector("button.btn.btn-danger").click()

        # Assert status is success
        self.assertTrue(self.is_success_message_present(text='Group and relationships successfully removed.'))


def suite():
    suite = unittest.TestSuite()
    # Add each test the the suite to be run
    # success and failure is output by the test
    suite.addTest(BaseTestCase('test_login'))
    suite.addTest(UserTest('test_create_user'))
    suite.addTest(GroupTest('test_create_group'))
    suite.addTest(GroupTest('test_group_edit_name_and_global_role'))
    suite.addTest(GroupTest('test_add_group_member'))
    suite.addTest(GroupTest('test_edit_group_member'))
    suite.addTest(GroupTest('test_delete_group_member'))
    suite.addTest(GroupTest('test_group_delete'))
    suite.addTest(UserTest('test_user_delete'))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(descriptions=True, failfast=True, verbosity=2)
    ret = not runner.run(suite()).wasSuccessful()
    BaseTestCase.tearDownDriver()
    sys.exit(ret)
