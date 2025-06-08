import os

project_files = {
    "app.py": '''from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
''',

    "requirements.txt": "flask\n",

    "Dockerfile": '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
''',

    "templates/index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Flask Splash</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white flex items-center justify-center h-screen">
  <div class="text-center">
    <img src="/static/logo.png" alt="Logo" class="mx-auto w-32 h-32 mb-4">
    <h1 class="text-4xl font-bold">Flask Splash Docker</h1>
  </div>
</body>
</html>
'''
}

os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Dummy placeholder logo
with open("static/logo.png", "wb") as f:
    f.write(b"\x89PNG\r\n\x1a\n")  # tiny empty PNG to avoid 404

for path, content in project_files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Project scaffolded. To run:\n")
print("  docker build -t flask-splash .")
print("  docker run -p 5000:5000 flask-splash")
