import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

function NutrientChart({ nitrogen }) {
  const valueMap = {
    low: 30,
    medium: 65,
    high: 90
  };

  const data = {
    labels: ["Nitrogen"],
    datasets: [
      {
        label: "Nutrient Level",
        data: [valueMap[nitrogen.toLowerCase()]],
        backgroundColor: "#81c784",
        borderRadius: 8,
      }
    ]
  };

  const options = {
    responsive: true,
    scales: {
      y: {
        min: 0,
        max: 100
      }
    },
    plugins: {
      legend: { display: false }
    }
  };

  return (
    <div style={{ marginTop: "25px" }}>
      <h3>Nutrient Status</h3>
      <Bar data={data} options={options} />
    </div>
  );
}

export default NutrientChart;
