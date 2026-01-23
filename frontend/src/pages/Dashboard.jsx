import { useState } from "react";
import SoilForm from "../components/SoilForm.jsx";
import AnalysisResult from "../components/AnalysisResult.jsx";
import AlertBox from "../components/AlertBox.jsx";

function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <main className="container">
      <h1 style={{ color: "black" }}>SoilSense Dashboard</h1>
      <p style={{ textAlign: "center", marginBottom: "30px", opacity: 0.85 }}>
        AI-powered soil health analysis & crop-specific recommendations
      </p>


      <SoilForm onResult={setResult} />

      <AlertBox risk={result?.risk_level} />

      <AnalysisResult result={result} />
    </main>
  );
}

export default Dashboard;
