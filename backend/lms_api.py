import requests

LMS_API_URL = "https://moodle.youruniversity.edu/webservice/rest/server.php"
LMS_TOKEN = "YOUR_LMS_TOKEN"

def get_file_from_lms(query):
    if "algorithms" in query:
        params = {
            'wstoken': LMS_TOKEN,
            'wsfunction': 'core_course_get_contents',
            'moodlewsrestformat': 'json',
            'courseid': 12
        }
        response = requests.get(LMS_API_URL, params=params)
        return f"Here's your Algorithms PDF: [link]"
    return "No matching file found."