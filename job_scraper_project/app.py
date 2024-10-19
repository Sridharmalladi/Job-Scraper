from flask import Flask, render_template_string
from models import Job, session

app = Flask(__name__)

@app.route('/')
def index():
    jobs = session.query(Job).all()
    # Simple HTML with job listings
    html = """
    <h1>Job Listings</h1>
    <table border="1">
        <tr>
            <th>Title</th>
            <th>Company</th>
            <th>Recruiter Email</th>
        </tr>
        {% for job in jobs %}
        <tr>
            <td>{{ job.title }}</td>
            <td>{{ job.company }}</td>
            <td>{{ job.recruiter_email }}</td>
        </tr>
        {% endfor %}
    </table>
    """
    return render_template_string(html, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
