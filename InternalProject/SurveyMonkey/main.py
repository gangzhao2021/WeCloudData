from surveys import Surveys
from surveys_data_collector import Surveys_Data_Collector
from survey_data_transmit import Survey_Data_Transmit
from retrieve_questions_info import Retrieve_Questions_Info
from retrieve_responses_info import Retrieve_Responses_Info


def main():
    
    # 01
    # Call surveys() to generate all_surveys.json and new_surveys.json
    Surveys().surveys()

    # 02
    # Call questions_data() to generate questions_data.json
    Surveys_Data_Collector().questions_data()
    # Call responses_data() to generate responses_data.json
    Surveys_Data_Collector().responses_data()

    # 03
    # Call local_to_s3() to upload 02_questions_data.json
    # , 02_responses_data.json, 02_new_questions_data.json
    # and 02_new_responses_data  to s3 bucket
    Survey_Data_Transmit().local_to_s3('questions_data.json')
    Survey_Data_Transmit().local_to_s3('responses_data.json')
    Survey_Data_Transmit().local_to_s3('new_questions_data.json')
    Survey_Data_Transmit().local_to_s3('new_responses_data.json')

    # Call s3_to_local() to download questions_data.json, 
    # responses_data.json, new_questions_data.json and 
    # new_responses_data.json from s3 bucket to local
    Survey_Data_Transmit().s3_to_local('questions_data.json')
    Survey_Data_Transmit().s3_to_local('responses_data.json')
    Survey_Data_Transmit().s3_to_local('new_questions_data.json')
    Survey_Data_Transmit().s3_to_local('new_responses_data.json')

    # 04
    # Call retrieve_questions_info() to generate questions_info.json
    Retrieve_Questions_Info().retrieve_questions_info()

    # 05
    # Call retrieve_responses_info() to generate different kinds of response.json
    Retrieve_Responses_Info().retrieve_responses_info()


if __name__ == "__main__":
    main()
