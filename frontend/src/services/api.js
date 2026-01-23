const API_URL = "http://127.0.0.1:8000/analyze-soil";

export async function analyzeSoil(payload) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || "API request failed");
  }

  return response.json();
}
