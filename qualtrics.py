import requests
import zipfile
import io
import os

def get_qualtrics_survey(dir_to_save_survey_in, survey_id):
    """based on: https://www.youtube.com/watch?v=_uhY_a4NgNc"""

    api_token = ""  # TODO
    file_format = "csv"
    data_center = "" # TODO

    request_check_progress = 0.0
    progress_status = "in progress"
    base_url = "https://{0}.qualtrics.com/API/v3/responseexports/".format(data_center)
    headers = {
        "content-type": "application/json",
        "x-api-token:": api_token,
    }

    download_request_url = base_url
    download_request_payload = '{"format":"' + file_format + '","surveyId":"' + survey_id + '"}'
    download_request_response = requests.request("POST", download_request_url, data=download_request_payload, headers=headers)
    progress_id = download_request_response.json()["result"]["id"]

    while request_check_progress < 100 and progress_status != "complete":
        request_check_url = base_url + progress_id
        request_check_response = requests.request("GET", request_check_url, headers=headers)
        request_check_progress = request_check_response.json()["result"]["percentComplete"]
        progress_status = request_check_response.json()["result"]["status"]

    request_download_url = base_url + progress_id + '/file'
    request_download = requests.request("GET", request_download_url, headers=headers, stream=True)

    zipfile.ZipFile(io.BytesIO(request_download.content)).extractall(dir_to_save_survey_in)


if __name__ == "__main__":

    path = "" # TODO
    survey_id = "hello" # TODO: where do we get this from??

    get_qualtrics_survey(dir_to_save_survey_in = path, survey_id = survey_id)