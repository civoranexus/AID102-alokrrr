function SoilHealthBar({ score }) {
  return (
    <div style={{ marginTop: "20px" }}>
      <p><strong>Soil Health Index</strong></p>

      <div style={{
        background: "rgba(255,255,255,0.2)",
        borderRadius: "12px",
        overflow: "hidden",
        height: "18px"
      }}>
        <div
          style={{
            width: `${score}%`,
            height: "100%",
            background:
              score > 70 ? "#66bb6a" :
              score > 40 ? "#ffb74d" :
              "#e57373",
            transition: "width 0.6s ease"
          }}
        />
      </div>

      <small>{score}% overall soil suitability</small>
    </div>
  );
}

export default SoilHealthBar;
