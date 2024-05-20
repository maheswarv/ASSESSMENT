from SCRIPTS.UI_COMMON.assessment_ui_common_v2 import *
from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.write_excel_new import *
from SCRIPTS.COMMON.io_path import *
from SCRIPTS.CRPO_COMMON.crpo_common import *
from SCRIPTS.CRPO_COMMON.credentials import *


class QPVerification:

    def __init__(self):
        self.row = 1
        write_excel_object.save_result(output_path_ui_mcqww_client_section_random)
        header = ['QP_Verification']
        write_excel_object.write_headers_for_scripts(0, 0, header, write_excel_object.black_color_bold)
        header = ['Test Cases', 'Status', 'Test Id', 'Candidate Id', 'Testuser ID', 'User Name', 'Password',
                  'mismatched questions(in QP) - question out of the QP', "Mismatched S1G1 if any",
                  "Mismatched S2G1 if any", "Mismatched S1G2 if any", "Mismatched S2G2 if any",
                  "Expected Overall Randomization",
                  "Actual Overall Randomization", "Expected S1G1 Randomization", "Actual S1G1 Randomization",
                  "Expected S2G1 Randomization", "Actual S2G1 Randomization", "Expected S1G2 Randomization",
                  "Actual S1G2 Randomization", "Expected S2G2 Randomization", "Actual S2G2 Randomization",
                  '1st login Q1', '2nd login Q1', '1st login Q2', '2nd login Q2', '1st login Q3', '2nd login Q3',
                  '1st login Q4', '2nd login Q4', '1st login Q5', '2nd login Q5', '1st login Q6', '2nd login Q6',
                  '1st login Q7', '2nd login Q7', '1st login Q8', '2nd login Q8', '1st login Q9', '2nd login Q9',
                  '1st login Q10', '2nd login Q10', '1st login Q11', '2nd login Q11', '1st login Q12', '2nd login Q12',
                  '1st login Q13', '2nd login Q13', '1st login Q14', '2nd login Q14', '1st login Q15', '2nd login Q15',
                  '1st login Q16', '2nd login Q16', '1st login Q17', '2nd login Q17', '1st login Q18', '2nd login Q18',
                  '1st login Q19', '2nd login Q19', '1st login Q20', '2nd login Q20', '1st login Q21', '2nd login Q21',
                  '1st login Q22', '2nd login Q22', '1st login Q23', '2nd login Q23', '1st login Q24', '2nd login Q24',
                  '1st login Q25', '2nd login Q25', '1st login Q26', '2nd login Q26', '1st login Q26', '2nd login Q26',
                  '1st login Q28', '2nd login Q28', '1st login Q29', '2nd login Q29', '1st login Q30', '2nd login Q30',
                  '1st login Q31', '2nd login Q31', '1st login Q32', '2nd login Q32', '1st login Q33', '2nd login Q33',
                  '1st login Q34', '2nd login Q34', '1st login Q35', '2nd login Q35', '1st login Q36', '2nd login Q36',
                  '1st login Q37', '2nd login Q37', '1st login Q38', '2nd login Q38', '1st login Q39', '2nd login Q39',
                  '1st login Q40', '2nd login Q40']
        write_excel_object.write_headers_for_scripts(1, 0, header, write_excel_object.black_color_bold)
        self.expected_questions = []

        self.qp_qn_index = [{"qn": "MS Client Random MCQWW G1S1QN1", "index": 1},
                            {"qn": "MS Client Random MCQWW G1S1QN2", "index": 2},
                            {"qn": "MS Client Random MCQWW G1S1QN3", "index": 3},
                            {"qn": "MS Client Random MCQWW G1S1QN4", "index": 4},
                            {"qn": "MS Client Random MCQWW G1S1QN5", "index": 5},
                            {"qn": "MS Client Random MCQWW G1S1QN6", "index": 6},
                            {"qn": "MS Client Random MCQWW G1S1QN7", "index": 7},
                            {"qn": "MS Client Random MCQWW G1S1QN8", "index": 8},
                            {"qn": "MS Client Random MCQWW G1S1QN9", "index": 9},
                            {"qn": "MS Client Random MCQWW G1S1QN10", "index": 10},
                            {"qn": "MS Client Random MCQWW G1S2QN11", "index": 11},
                            {"qn": "MS Client Random MCQWW G1S2QN12", "index": 12},
                            {"qn": "MS Client Random MCQWW G1S2QN13", "index": 13},
                            {"qn": "MS Client Random MCQWW G1S2QN14", "index": 14},
                            {"qn": "MS Client Random MCQWW G1S2QN15", "index": 15},
                            {"qn": "MS Client Random MCQWW G1S2QN16", "index": 16},
                            {"qn": "MS Client Random MCQWW G1S2QN17", "index": 17},
                            {"qn": "MS Client Random MCQWW G1S2QN18", "index": 18},
                            {"qn": "MS Client Random MCQWW G1S2QN19", "index": 19},
                            {"qn": "MS Client Random MCQWW G1S2QN20", "index": 20},
                            {"qn": "MS Client Random MCQWW G2S1QN21", "index": 21},
                            {"qn": "MS Client Random MCQWW G2S1QN22", "index": 22},
                            {"qn": "MS Client Random MCQWW G2S1QN23", "index": 23},
                            {"qn": "MS Client Random MCQWW G2S1QN24", "index": 24},
                            {"qn": "MS Client Random MCQWW G2S1QN25", "index": 25},
                            {"qn": "MS Client Random MCQWW G2S1QN26", "index": 26},
                            {"qn": "MS Client Random MCQWW G2S1QN27", "index": 27},
                            {"qn": "MS Client Random MCQWW G2S1QN28", "index": 28},
                            {"qn": "MS Client Random MCQWW G2S1QN29", "index": 29},
                            {"qn": "MS Client Random MCQWW G2S1QN30", "index": 30},
                            {"qn": "MS Client Random MCQWW G2S2QN31", "index": 31},
                            {"qn": "MS Client Random MCQWW G2S2QN32", "index": 32},
                            {"qn": "MS Client Random MCQWW G2S2QN33", "index": 33},
                            {"qn": "MS Client Random MCQWW G2S2QN34", "index": 34},
                            {"qn": "MS Client Random MCQWW G2S2QN35", "index": 35},
                            {"qn": "MS Client Random MCQWW G2S2QN36", "index": 36},
                            {"qn": "MS Client Random MCQWW G2S2QN37", "index": 37},
                            {"qn": "MS Client Random MCQWW G2S2QN38", "index": 38},
                            {"qn": "MS Client Random MCQWW G2S2QN39", "index": 39},
                            {"qn": "MS Client Random MCQWW G2S2QN40", "index": 40}]

        self.section1_group1_questions = ["MS Client Random MCQWW G1S1QN1",
                                          "MS Client Random MCQWW G1S1QN2",
                                          "MS Client Random MCQWW G1S1QN3",
                                          "MS Client Random MCQWW G1S1QN4",
                                          "MS Client Random MCQWW G1S1QN5",
                                          "MS Client Random MCQWW G1S1QN6",
                                          "MS Client Random MCQWW G1S1QN7",
                                          "MS Client Random MCQWW G1S1QN8",
                                          "MS Client Random MCQWW G1S1QN9",
                                          "MS Client Random MCQWW G1S1QN10"]

        self.section2_group1_questions = ["MS Client Random MCQWW G1S2QN11",
                                          "MS Client Random MCQWW G1S2QN12",
                                          "MS Client Random MCQWW G1S2QN13",
                                          "MS Client Random MCQWW G1S2QN14",
                                          "MS Client Random MCQWW G1S2QN15",
                                          "MS Client Random MCQWW G1S2QN16",
                                          "MS Client Random MCQWW G1S2QN17",
                                          "MS Client Random MCQWW G1S2QN18",
                                          "MS Client Random MCQWW G1S2QN19",
                                          "MS Client Random MCQWW G1S2QN20"]

        self.section1_group2_questions = ["MS Client Random MCQWW G2S1QN21",
                                          "MS Client Random MCQWW G2S1QN22",
                                          "MS Client Random MCQWW G2S1QN23",
                                          "MS Client Random MCQWW G2S1QN24",
                                          "MS Client Random MCQWW G2S1QN25",
                                          "MS Client Random MCQWW G2S1QN26",
                                          "MS Client Random MCQWW G2S1QN27",
                                          "MS Client Random MCQWW G2S1QN28",
                                          "MS Client Random MCQWW G2S1QN29",
                                          "MS Client Random MCQWW G2S1QN30"]

        self.section2_group2_questions = ["MS Client Random MCQWW G2S2QN31",
                                          "MS Client Random MCQWW G2S2QN32",
                                          "MS Client Random MCQWW G2S2QN33",
                                          "MS Client Random MCQWW G2S2QN34",
                                          "MS Client Random MCQWW G2S2QN35",
                                          "MS Client Random MCQWW G2S2QN36",
                                          "MS Client Random MCQWW G2S2QN37",
                                          "MS Client Random MCQWW G2S2QN38",
                                          "MS Client Random MCQWW G2S2QN39",
                                          "MS Client Random MCQWW G2S2QN40"]

        # self.group1_questions = self.section1_group1_questions + self.section2_group1_questions
        # self.group2_questions = self.section1_group2_questions + self.section2_group2_questions

        self.expected_questions = self.section1_group1_questions + self.section2_group1_questions + \
                                  self.section1_group2_questions + self.section2_group2_questions

    def overall_rondomization(self, qn_details):
        for all_qns_with_index in self.qp_qn_index:
            if qn_details.get('question') == all_qns_with_index.get("qn"):
                if qn_details.get('index') != all_qns_with_index.get("index"):
                    self.overall_randomization = "Yes"
                    if 1 <= qn_details.get('index') <= 10:
                        if qn_details.get('question') in self.section1_group1_questions:
                            self.s1g1_randomization = "Yes"
                    elif 11 <= qn_details.get('index') <= 20:
                        if qn_details.get('question') in self.section2_group1_questions:
                            self.s2g1_randomization = "Yes"
                    elif 21 <= qn_details.get('index') <= 30:
                        if qn_details.get('question') in self.section1_group2_questions:
                            self.s1g2_randomization = "Yes"
                    elif 31 <= qn_details.get('index') <= 40:
                        if qn_details.get('question') in self.section2_group2_questions:
                            self.s2g2_randomization = "Yes"
                break

    def verify_group_and_section(self, question_details):
        if question_details.get('group') == 'Group1':
            if question_details.get('section') == "Group1Section1":
                self.actual_s1g1_questions.append(question_details.get('question'))
            elif question_details.get('section') == "Group1Section2":
                self.actual_s2g1_questions.append(question_details.get('question'))
            else:
                print("Question is out of Group1 Section")

        elif question_details.get('group') == 'Group2':
            if question_details.get('section') == "Group2Section1":
                self.actual_s1g2_questions.append(question_details.get('question'))
            elif question_details.get('section') == "Group2Section2":
                self.actual_s2g2_questions.append(question_details.get('question'))
            else:
                print("Question is out of Group2 Section")

    def verify_questions(self, tu_details, login_user, login_pass, candidate_id, tu_id):
        self.overall_randomization = "No"
        self.s1g1_randomization = "No"
        self.s2g1_randomization = "No"
        self.s1g2_randomization = "No"
        self.s2g2_randomization = "No"
        self.color = write_excel_object.green_color
        self.status = 'pass'
        self.row = self.row + 1
        self.delivered_questions = []
        self.relogin_questions = []
        self.actual_s1g1_questions = []
        self.actual_s2g1_questions = []
        self.actual_s1g2_questions = []
        self.actual_s2g2_questions = []
        self.browser = assess_ui_common_obj.initiate_browser(amsin_automation_assessment_url, chrome_driver_path)
        login_details = assess_ui_common_obj.ui_login_to_test(login_user, login_pass)
        if login_details == 'SUCCESS':
            i_agreed = assess_ui_common_obj.select_i_agree()
            if i_agreed:
                start_test_status = assess_ui_common_obj.start_test_button_status()
                assess_ui_common_obj.start_test()
                for question_index in range(1, int(tu_details.get('expectedTotalQuestionsCount') + 1)):
                    assess_ui_common_obj.next_question(question_index)
                    qn_string = assess_ui_common_obj.find_question_string_v2()
                    print(qn_string)
                    self.delivered_questions.append(qn_string[0])
                    self.qn_details = {'question': qn_string[0], 'group': qn_string[1], 'section': qn_string[2],
                                       'index': question_index}
                    client_side_randomization.overall_rondomization(self.qn_details)
                    client_side_randomization.verify_group_and_section(self.qn_details)
                self.overall_randomization_status = client_side_randomization.overall_rondomization(self.qn_details)
                print("1st Login")
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])
                time.sleep(1)
                self.browser.execute_script(
                    '''window.open("https://amsin.hirepro.in/assessment/#/assess/login/eyJhbGlhcyI6ImF1dG9tYXRpb24ifQ%3D%3D", "_blank");''')
                time.sleep(2)
                self.browser.switch_to.window(self.browser.window_handles[1])
                login_details = assess_ui_common_obj.ui_login_to_test(login_user, login_pass)
                if login_details == 'SUCCESS':
                    i_agreed = assess_ui_common_obj.select_i_agree()
                    if i_agreed:
                        start_test_status = assess_ui_common_obj.start_test_button_status()
                        assess_ui_common_obj.start_test()
                        for question_index in range(1, int(tu_details.get('expectedTotalQuestionsCount') + 1)):
                            assess_ui_common_obj.next_question(question_index)
                            qn_string = assess_ui_common_obj.find_question_string_v2()
                            self.relogin_questions.append(qn_string[0])
                            # self.relogin_qn_details = {'question': qn_string[0], 'group': qn_string[1],
                            #                            'section': qn_string[2], "index": question_index}
                self.browser.quit()
                write_excel_object.compare_results_and_write_vertically(tu_details.get('testCases'), None, self.row, 0)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('testID'), None, self.row, 2)
                write_excel_object.compare_results_and_write_vertically(candidate_id, None, self.row, 3)
                write_excel_object.compare_results_and_write_vertically(tu_id, None, self.row, 4)
                write_excel_object.compare_results_and_write_vertically(login_user, None, self.row, 5)
                write_excel_object.compare_results_and_write_vertically(login_pass, None, self.row, 6)

                mismatched_questions = set(self.delivered_questions) - set(self.expected_questions)
                if len(mismatched_questions) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    mismatched_questions = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 7, str(mismatched_questions),
                                            write_excel_object.current_status_color)

                print(self.actual_s1g1_questions)
                s1g1_mismatched = set(self.section1_group1_questions) - set(self.actual_s1g1_questions)
                if len(s1g1_mismatched) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    s1g1_mismatched = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 8, str(s1g1_mismatched),
                                            write_excel_object.current_status_color)

                s2g1_mismatched = set(self.section2_group1_questions) - set(self.actual_s2g1_questions)
                print(self.actual_s2g1_questions)
                if len(s2g1_mismatched) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    s2g1_mismatched = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 9, str(s2g1_mismatched),
                                            write_excel_object.current_status_color)

                s1g2_mismatched = set(self.section1_group2_questions) - set(self.actual_s1g2_questions)
                print(self.actual_s1g2_questions)
                if len(s1g2_mismatched) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    s1g2_mismatched = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 10, str(s1g2_mismatched), write_excel_object.current_status_color)

                s2g2_mismatched = set(self.section2_group2_questions) - set(self.actual_s2g2_questions)
                print(self.actual_s2g2_questions)
                if len(s2g2_mismatched) >= 1:
                    write_excel_object.current_status = 'Fail'
                    write_excel_object.overall_status = 'Fail'
                    write_excel_object.current_status_color = write_excel_object.red_color
                    write_excel_object.overall_status_color = write_excel_object.red_color
                else:
                    s2g2_mismatched = 'No Mismatch - Expected delivery'
                write_excel_object.ws.write(self.row, 11, str(s2g2_mismatched), write_excel_object.current_status_color)

                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedOverallRandomization'),
                                                                        self.overall_randomization, self.row, 12)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedS1G1Randomization'),
                                                                        self.s1g1_randomization, self.row, 14)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedS2G1Randomization'),
                                                                        self.s2g1_randomization, self.row, 16)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedS1G2Randomization'),
                                                                        self.s1g2_randomization, self.row, 18)
                write_excel_object.compare_results_and_write_vertically(tu_details.get('expectedS2G2Randomization'),
                                                                        self.s2g2_randomization, self.row, 20)

                col = 22
                for index in range(0, int(tu_details.get('expectedTotalQuestionsCount'))):
                    print(index)
                    write_excel_object.compare_results_and_write_vertically(self.delivered_questions[index],
                                                                            self.relogin_questions[index], self.row,
                                                                            col)
                    col = col + 2
                write_excel_object.compare_results_and_write_vertically(write_excel_object.current_status, None,
                                                                        self.row, 1)


client_side_randomization = QPVerification()
excel_read_obj.excel_read(input_path_ui_mcq_client_section_random, 9)
candidate_details = excel_read_obj.details
token = crpo_common_obj.login_to_crpo(cred_crpo_admin.get('user'), cred_crpo_admin.get('password'),
                                      cred_crpo_admin.get('tenant'))
test_id = 15685
event_id = 11625
jobrole_id = 30439
sprint_id = input('Enter Sprint ID ')
next_cand = 2000
for current_excel_row in candidate_details:
    next_cand = next_cand + 1
    sprint_id = sprint_id + str(next_cand)
    print(sprint_id)
    candidate_id = crpo_common_obj.create_candidate(token, sprint_id)
    tag_candidate = crpo_common_obj.tag_candidate_to_test(token, candidate_id, test_id, event_id, jobrole_id)
    time.sleep(5)
    test_userid = crpo_common_obj.get_all_test_user(token, candidate_id)
    print(test_userid)
    tu_cred = crpo_common_obj.test_user_credentials(token, test_userid)
    login_id = tu_cred['data']['testUserCredential']['loginId']
    password = tu_cred['data']['testUserCredential']['password']
    # print(login_id)
    # print(password)
    client_side_randomization.verify_questions(current_excel_row, login_id, password, candidate_id, test_userid)
write_excel_object.write_overall_status(1)
