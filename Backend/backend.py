from flask import Flask, request, jsonify
from SQL import SQL

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
def home():
    return "Hello My Home!"

@app.route("/regis", methods=['POST'])
def regis():
    json_body = request.json
    name = json_body["name"]
    surname = json_body["surname"]
    username = json_body["username"]
    password = json_body["password"]
    agent.register(name, surname, username, password, 2)
    '''
    Your Database Query
    '''
    return {
        "name" : name,
        "surname" : surname,
        "username" : username,
        "password" : password 
    }

@app.route("/login", methods=['GET'])
# for example path /login?username=xxx&password=yyy
def get_user():
    username = request.args.get('username')
    password = request.args.get('password')
    try: 
        success = agent.login(username, password, 2)
        if success:
            return jsonify({"message": "Successful"}), 200
        else:
            return jsonify({"message": "Failed"}), 401
    except:
        return jsonify({"message": "Failed"}), 401
    '''
    Your Database Query
    '''

@app.route("/report", methods=['GET'])
def report():
    '''
    Your Database Query
    '''
    return {
        "status" : True,
        "content" : "Report"
    }

@app.route("/all_student", methods=['GET'])
def all_student():
    '''
    Your Database Query
    '''
    return {
        "status" : True,
        "content" : "All Student"
    }
@app.route("/personal_student", methods=['GET'])
def personal_student():
    '''
    Your Database Query
    '''
    return {
        "status" : True,
        "content" : "Personal Student"
    }
@app.route("/avg", methods=['POST'])
def average_number():
    json_body = request.json
    
    """
    Your AI Model
    """
    
    if "data" in json_body:
    
        return { 
            "status": True,
            "result": sum(json_body["data"])
        }
    
    else:
        return {
            "status": False,
            "content": "Wrong Format"
        }
@app.route("/question_id", methods=['GET'])
def question_id():
    q_tyoe = request.args.get('q_type')
    '''
    Your Database Query
    '''
    return jsonify({"message": "question_id"}), 200

@app.route("/question", methods=['GET'])
def question():
    q_type = request.args.get('q_type')
    '''
    Your Database Query
    '''
    questions = agent.get_question(q_type)
    return jsonify({"message": questions}), 200

@app.route("/student_answer", methods=['POST'])
def student_answer():
    json_body = request.json
    QID = json_body["QID"]
    SID = json_body["SID"]
    answer = json_body["answer"]
    agent.query_answer(QID, SID, answer)
    '''
    Your Database Query
    '''
    return jsonify({"message": "Successfully answering"}), 200

@app.route("/answer", methods=['GET'])
def answer():
    SID = request.args.get('SID')
    QID = request.args.get('QID')
    ans = agent.get_answer(QID, SID)
    '''
    Your Database Query
    '''
    
    return jsonify({"message": ans}), 200
    
if __name__ =="__main__":
    agent = SQL()
    app.run(host='0.0.0.0', port=8000)
    
    