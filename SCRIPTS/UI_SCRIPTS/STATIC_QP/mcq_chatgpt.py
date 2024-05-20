from SCRIPTS.UI_COMMON.assessment_ui_common_v2 import *
import time
from SCRIPTS.UI_SCRIPTS.assessment_data_verification import *
from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.io_path import *


class OnlineAssessment:
    def __init__(self):
        # URL for the assessment
        self.url = amsin_at_assessment_url
        # Path for Chrome webdriver
        self.path = r"F:\qa_automation\chromedriver.exe"

    def mcq_assessment(self, current_excel_data):
        # Initiating the browser for assessment
        self.browser = assess_ui_common_obj.initiate_browser(self.url, self.path)
        # Logging in to the assessment platform
        login_details = assess_ui_common_obj.ui_login_to_test(current_excel_data.get('loginName'),
                                                              (current_excel_data.get('password')))
        if login_details == 'SUCCESS':
            # Selecting 'I Agree' checkbox
            i_agreed = assess_ui_common_obj.select_i_agree()
            if i_agreed:
                # Checking start test button status
                start_test_status = assess_ui_common_obj.start_test_button_status()
                # Starting the test
                assess_ui_common_obj.start_test()
                if current_excel_data.get('skipRquired') == 'Yes':
                    # Skipping questions
                    assess_ui_common_obj.next_question(5)
                    # Ending the test
                    assess_ui_common_obj.end_test()
                    # Confirming the end of the test
                    assess_ui_common_obj.end_test_confirmation()
                    time.sleep(3)
                    self.browser.quit()

                elif current_excel_data.get('reloginRequird') == 'Yes':
                    # Selecting answers for questions after relogin
                    self.relogin_and_answer_questions(current_excel_data)

                else:
                    # Selecting answers for questions
                    self.select_answers(current_excel_data)

        else:
            print("login failed due to below reason")
            print(login_details)

    def relogin_and_answer_questions(self, current_excel_data):
        # Selecting answers for questions after relogin
        assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid1'))
        assess_ui_common_obj.next_question(2)
        assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid2'))
        assess_ui_common_obj.next_question(3)
        assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid3'))
        assess_ui_common_obj.next_question(4)
        assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid4'))
        assess_ui_common_obj.next_question(5)
        assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid5'))
        assess_ui_common_obj.end_test()
        assess_ui_common_obj.end_test_confirmation()
        time.sleep(5)
        self.browser.quit()

    def select_answers(self, current_excel_data):
        # Selecting answers for questions
        if current_excel_data.get('unAnswerRequired') == 'No':
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid1'))
            assess_ui_common_obj.next_question(2)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid2'))
            assess_ui_common_obj.next_question(3)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid3'))
            assess_ui_common_obj.next_question(4)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid4'))
            assess_ui_common_obj.next_question(5)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid5'))
            assess_ui_common_obj.end_test()
            assess_ui_common_obj.end_test_confirmation()
            time.sleep(5)
            self.browser.quit()
        else:
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid1'))
            assess_ui_common_obj.unanswer_question()
            assess_ui_common_obj.next_question(2)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid2'))
            assess_ui_common_obj.unanswer_question()
            assess_ui_common_obj.next_question(3)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid3'))
            assess_ui_common_obj.unanswer_question()
            assess_ui_common_obj.next_question(4)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid4'))
            assess_ui_common_obj.unanswer_question()
            assess_ui_common_obj.next_question(5)
            assess_ui_common_obj.select_answer_for_the_question(current_excel_data.get('ans_qid5'))
            assess_ui_common_obj.unanswer_question()
            assess_ui_common_obj.end_test()
            assess_ui_common_obj.end_test_confirmation()
            time.sleep(5)
            self.browser.quit()

print(datetime.datetime.now())
assessment_obj = OnlineAssessment()
input_file_path = r"F:\qa_automation\PythonWorkingScripts_InputData\UI\Assessment\ui_relogin.xls"
excel_read_obj.excel_read(input_file_path, 0)
excel_data = excel_read_obj.details
for current_excel_row in excel_data:
    print(current_excel_row)
    assessment_obj.mcq_assessment(current_excel_row)
crpo_token = crpo_common_obj.login_to_crpo('admin', 'At@2023$$', 'AT')
print(crpo_token)
obj_assessment_data_verification.assessment_data_report(crpo_token, excel_data)
obj_assessment_data_verification.write_excel.close()
print(datetime.datetime.now())