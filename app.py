from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 증상별 약 데이터 (설명 추가, 처방 필요 여부 포함)
medications = {
    "두통": [
        {"name": "타이레놀", "description": "경증 두통에 자주 사용됨", "prescription": False},
        {"name": "이부프로펜", "description": "염증성 통증에도 효과적", "prescription": False}
    ],
    "발열": [
        {"name": "타이레놀", "description": "해열에 자주 사용됨", "prescription": False},
        {"name": "이부프로펜", "description": "염증을 동반한 열에 효과적", "prescription": False}
    ],
    "기침": [
        {"name": "덱스트로메토르판", "description": "마른 기침에 효과적", "prescription": False},
        {"name": "구아이페네신", "description": "가래 배출을 돕는 기침약", "prescription": False}
    ],
    "콧물": [
        {"name": "클로르페니라민", "description": "알레르기성 콧물에 효과적", "prescription": False},
        {"name": "로라타딘", "description": "졸림이 적은 항히스타민제", "prescription": False}
    ],
    "인후통": [
        {"name": "아세트아미노펜", "description": "통증 완화용 해열진통제", "prescription": False},
        {"name": "트로키", "description": "목 안 통증 완화용", "prescription": False}
    ],
    "속쓰림": [
        {"name": "오메프라졸", "description": "위산 억제에 사용됨", "prescription": True},
        {"name": "라니티딘", "description": "속쓰림과 위염에 사용됨", "prescription": True}
    ],
    "소화불량": [
        {"name": "베아제", "description": "과식했을 때, 식체, 소화불량", "prescription": False},
        {"name": "훼스탈 플러스", "description": "이유 없는 복부 팽만감, 기능성 소화불량", "prescription": False}
    ]
}

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    symptoms = data.get('symptoms', [])

    recommended = []
    added = set()

    for symptom in symptoms:
        for med in medications.get(symptom, []):
            key = med['name'] + med['description']
            if key not in added:
                recommended.append({
                    "name": med['name'],
                    "description": med['description'],
                    "prescription": med['prescription'],
                    "for": symptom
                })
                added.add(key)

    return jsonify(recommended)

if __name__ == '__main__':
    app.run(debug=True)

