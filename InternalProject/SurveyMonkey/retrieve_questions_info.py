import json
import pathlib
import unicodedata

from write_to_file import Write_To_File
import family_id_transfer as fit
from surveys import Surveys


class Retrieve_Questions_Info:

    def __init__(self):
        self.append_json_to_file = Write_To_File().append_json_to_file
        self.clear_file = Write_To_File().clear_file
        self.new_questions_data_path = '%s/output/03s3_new_questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.questions_info_path = '%s/output/04questions_info.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_questions_info_path = '%s/output/04new_questions_info.json' % pathlib.Path(
            __file__).parent.resolve()

    # Retrieve all required question info in a specificed survey
    def retrieve_question_info(self, survey_id: int) -> dict:

        survey_data = ''

        # Initialize required question info dictionary
        qtn_info = {'sid': survey_id,  # sid refers to survey_id
                    "pos": '',  # pos refers to position
                    'qid': '',  # qid refers to question_id
                    'question': '',
                    'fid': '', ''  # fid refers to family_id
                    'stid': ''  # stid refers to subtype_id
                    }

        # Extract corresponding data set as survey_data
        with open(self.new_questions_data_path) as f:
            for line in f:
                survey_data0 = json.loads(line)
                if int(survey_data0['id']) == survey_id:
                    survey_data = survey_data0
                    break

        pages = survey_data['pages']
        # Question position starts from 1 on each page
        # Add question_count to the subsequent page's
        # question position to get the corrent position
        question_count = 0

        for page in pages:
            qtns = page['questions']
            if not qtns:  # qtns is empty
                self.append_json_to_file(self.questions_info_path, qtn_info)
                self.append_json_to_file(
                    self.new_questions_info_path, qtn_info)

            for qtn in qtns:
                qtn_info['pos'] = qtn['position'] + question_count
                qtn_info['qid'] = int(qtn['id'])
                qtn_info["question"] = unicodedata.normalize(
                    'NFKD', qtn['headings'][0]['heading'])
                qtn_info['fid'] = fit.family_table[qtn['family']]

                # Check family_id_transfer.py for the corresponding family
                # Check by the order of the frequency of the occurence of
                # the questions to speed up the program
                if qtn_info['fid'] == 2:
                    qtn_info['stid'] = fit.matrix_subtype_table[qtn['subtype']]
                elif qtn_info['fid'] == 3:
                    qtn_info['stid'] = fit.open_ended_subtype_table[qtn['subtype']]
                elif qtn_info['fid'] == 1:
                    qtn_info['stid'] = fit.single_choice_subtype_table[qtn['subtype']]
                elif qtn_info['fid'] == 6:
                    qtn_info['stid'] = fit.multiple_choice_subtype_table[qtn['subtype']]
                elif qtn_info['fid'] == 4:
                    qtn_info['stid'] = fit.demographic_subtype_table[qtn['subtype']]
                elif qtn_info['fid'] == 5:
                    qtn_info['stid'] = fit.datetime_subtype_table[qtn['subtype']]
                elif qtn_info['fid'] == 7:
                    qtn_info['stid'] = fit.presentation_subtype_table[qtn['subtype']]

                temp_qtn_info = qtn_info.copy()
                self.append_json_to_file(
                    self.questions_info_path, temp_qtn_info)
                self.append_json_to_file(
                    self.new_questions_info_path, temp_qtn_info)

            # Update question_count
            question_count += page['question_count']

    # Check question family id with given survey_id and question_id
    def family_id(self, survey_id: int, question_id: int):
        with open(self.questions_info_path) as f:
            for line in f:
                if int(json.loads(line)['sid']) == survey_id and int(json.loads(line)['qid']) == question_id:
                    return json.loads(line)['fid']

    # Retrieve all required question info from all surveys
    def retrieve_questions_info(self):
        # Find recent added surveys
        survey_ids = Surveys().new_survey_ids()

        self.clear_file(self.new_questions_info_path)

        for survey_id in survey_ids:
            self.retrieve_question_info(int(survey_id))
