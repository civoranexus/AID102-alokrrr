import { useState } from "react";
import SoilForm from "../components/SoilForm.jsx";
import AnalysisResult from "../components/AnalysisResult.jsx";
import AlertBox from "../components/AlertBox.jsx";

function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <main className="container">
      {/* HERO */}
      <section className="hero">
        <h1>SoilSense AI</h1>
        <p>
          Intelligent soil health analysis using AI-driven agronomic rules
        </p>
      </section>

      {/* INPUT CARD */}
      <section className="card lift">
        <SoilForm onResult={setResult} />
      </section>

      {/* ALERT */}
      <AlertBox risk={result?.risk_level} />

      {/* RESULT */}
      {result && (
        <section className="card lift">
          <AnalysisResult result={result} />
        </section>
      )}
    </main>
  );
}

export default Dashboard;
