
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # استلام البيانات من المستخدم
    input_text = request.form["input_text"]
    start_index = int(request.form["start_index"])
    end_index = int(request.form["end_index"])
    
    # معالجة القائمة
    lines = input_text.splitlines()
    processed_lines = [line[:start_index] + line[end_index:] for line in lines if len(line) > end_index]

    # تحويل النتيجة إلى نص
    result = "\n".join(processed_lines)
    return render_template("index.html", input_text=input_text, result=result)

if __name__ == "__main__":
    app.run(debug=True)
