from flask import Flask, render_template
import requests
import config
app = Flask(__name__)
def get_github_data():
    url = f"https://api.github.com/users/{config.STUDENT_GITHUB_USERNAME}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
@app.route('/')
def resume():
    github_data = get_github_data()
    return render_template(
        'resume.html',
        name=config.STUDENT_NAME,
        email=config.STUDENT_EMAIL,
        github=config.STUDENT_GITHUB,
        achievements=config.ACHIEVEMENTS,
        github_data=github_data
    )
@app.route('/refresh')
def refresh():
    github_data = get_github_data()
    return render_template(
        'resume.html',
        name=config.STUDENT_NAME,
        email=config.STUDENT_EMAIL,
        github=config.STUDENT_GITHUB,
        achievements=config.ACHIEVEMENTS,
        github_data=github_data
    )
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
