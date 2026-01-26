function PHIndicator({ pH, crop }) {
  const value = Math.max(0, Math.min(14, Number(pH)));
  const position = (value / 14) * 100;

  const idealRanges = {
    wheat: { min: 6.0, max: 7.0 },
    rice: { min: 5.5, max: 6.5 },
    cotton: { min: 6.0, max: 7.5 },
  };

  const range = idealRanges[crop?.toLowerCase()];
  const rangeStart = range ? (range.min / 14) * 100 : 0;
  const rangeWidth = range ? ((range.max - range.min) / 14) * 100 : 0;

  return (
    <div style={{ marginTop: "25px" }}>
      <h3>Soil pH Level</h3>

      <div style={{ position: "relative", marginTop: "12px" }}>
        {/* Base pH scale */}
        <div
          style={{
            height: "16px",
            borderRadius: "10px",
            background:
              "linear-gradient(to right, #e57373, #fff176, #81c784, #64b5f6)",
          }}
        />

        {/* Ideal range overlay */}
        {range && (
          <div
            style={{
              position: "absolute",
              top: 0,
              left: `${rangeStart}%`,
              width: `${rangeWidth}%`,
              height: "16px",
              background: "rgba(255,255,255,0.35)",
              borderRadius: "10px",
            }}
          />
        )}

        {/* Current pH marker */}
        <div
          style={{
            position: "absolute",
            top: "-6px",
            left: `${position}%`,
            transform: "translateX(-50%)",
            width: "4px",
            height: "28px",
            background: "#fff",
            borderRadius: "2px",
          }}
        />
      </div>

      <small>
        pH: <strong>{value}</strong>{" "}
        {range && (
          <>
            | Ideal for {crop}: {range.min} – {range.max}
          </>
        )}
      </small>
    </div>
  );
}

export default PHIndicator;
