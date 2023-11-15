
from flask import Flask

app = Flask(__name__)


@app.route('/')
def CGPA():
    {cc=input("Enter cloud computing grade")
    ml=input("Enter machine learning grade")
    cns=input("Enter cybersecurity grade")
    pom=input("Enter principles of management grade")
    cgpa=0
    j=cc
    if(j==O):
        cgpa=cgpa+10
    elif(j==A):
        cgpa=cgpa+9
    else:
        cgpa=cgpa+8

     j=ml
    if(j==O):
        cgpa=cgpa+10
    elif(j==A):
        cgpa=cgpa+9
    else:
        cgpa=cgpa+8

     j=cns
    if(j==O):
        cgpa=cgpa+10
    elif(j==A):
        cgpa=cgpa+9
    else:
        cgpa=cgpa+8

     j=pom
    if(j==O):
        cgpa=cgpa+10
    elif(j==A):
        cgpa=cgpa+9
    else:
        cgpa=cgpa+8

    print(cgpa)}


if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=8080, debug=True)

