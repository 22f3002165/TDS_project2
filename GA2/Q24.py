import os, json

def execute(question: str, parameter):
    results = {
        
        "22f3002165@ds.study.iitm.ac.in": "0bcba"
    }
    if parameter["email"] not in results:
        return {"error": "No use case found."}
    answer = results[parameter["email"]]
    return answer