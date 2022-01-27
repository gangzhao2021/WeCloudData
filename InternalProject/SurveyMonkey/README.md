## Classes and Functions

Fill the access_token in line 4 in auth.py

Fill aws_access_key_id in line 12 in auth.py

Fill aws_secret_access_key in line 13 in auth.py


Remove all the files in output folder.

Run the main() function in main.py

The following is the order of files

01 surveys.py

02 surveys_data_collector.py

03 survey_data_transmit.py

04 retrieve_questions_info.py

05 retrieve_responses_info.py

The rest are helper functions

## Output

01all_surveys.json contains all surveys' ids and titles.

01new_surveys.json contains recent added surveys' id and titles.

02questions_data.json contains all survey data about the questions. This data set would be uploaded to the s3 bucket.

02responses_data.json contains all survey data about the responses. This data set would be uploaded to the s3 bucket.

02new_questions_data.json contains recent added surveys' data about the questions. This data set would be uploaded to the s3 bucket.

02new_responses_data.json contains recent added surveys' data about the responses. This data set would be uploaded to the s3 bucket.

03s3_questions_data.json is the data set download from the s3 bucket, which is the same as 02questions_data.json.

03s3_responses_data.json is the data set download from the s3 bucket, which is the same as 02responses_data.json.

03s3_new_questions_data.json is the data set download from the s3 bucket, which is the same as 02new_questions_data.json.

03s3_new_responses_data.json is the data set download from the s3 bucket, which is the same as 02new_responses_data.json.

04questions_info.json contains the required question information from all surveys.

04new_questions_info.json contains the required question information from recent added surveys.

05_ contains different families of responses from all participants from all surveys.

05new_ contains different families of responses from all participants from recent added surveys.