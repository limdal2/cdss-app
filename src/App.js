// src/App.js
import React, { useState } from 'react';
import './App.css';

const symptomList = [
  '두통', '발열', '기침', '콧물', '인후통', '속쓰림', '소화불량'
];

function App() {
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [medications, setMedications] = useState([]);

  const toggleSymptom = (symptom) => {
    setSelectedSymptoms(prev =>
      prev.includes(symptom)
        ? prev.filter(s => s !== symptom)
        : [...prev, symptom]
    );
  };

  const handleRecommend = async () => {
    const res = await fetch('http://localhost:5000/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symptoms: selectedSymptoms })
    });
    const data = await res.json();
    setMedications(data);
  };

  return (
    <div className="App">
      <h1>증상 선택</h1>
      {symptomList.map(symptom => (
        <label key={symptom}>
          <input
            type="checkbox"
            checked={selectedSymptoms.includes(symptom)}
            onChange={() => toggleSymptom(symptom)}
          />
          {symptom}
        </label>
      ))}
      <br />
      <button onClick={handleRecommend}>약 추천받기</button>

      <h2>추천 약 목록</h2>
      {medications.map((med, index) => (
        <div key={index}>
          <strong>{med.name}</strong> ({med.for})<br />
          <em>{med.description}</em><br />
          {med.prescription ? '🔒 처방 필요' : '✅ 일반 의약품'}
          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;




