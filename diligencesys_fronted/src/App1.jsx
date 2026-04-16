import React, { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file first.");
      return;
    }

    setLoading(true);
    setError("");
    setResults([]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", { method: "POST", body: formData, });

      if (!response.ok) {
        throw new Error("Failed to analyze file.");
      }
      const data = await response.json();
      setResults(data);
    } 
    catch (err) {
      setError(err.message || "Something went wrong.");
    } 
    finally {
      setLoading(false);
    }
  };

  const getRiskColor = (score) => {
    if (score>=3) return "#f0730d";
      if (score>=2) return "#f59e0b";
      if (score>=1) return "#f6c30b";
      return "#b4f51c"
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f8fafc",
        fontFamily: "Arial, sans-serif",
        padding: "40px 20px",

      }}
    >
      <div style={{ maxWidth: "1000px", margin: "0 auto" }}>
        <div style={{ marginBottom: "30px" }}>
          <h1 style={{ fontSize: "32px", marginBottom: "8px", color: "#b7c24d" }}>
            Diligence Risk Analyzer
          </h1>
          <p style={{ color: "#83c95f", fontSize: "16px" }}>
            Upload a contract</p></div>

        <div
          style={{
            background: "#ffffff",
            borderRadius: "18px",
            padding: "24px",
            boxShadow: "0 8px 24px rgba(15, 23, 42, 0.08)",
            marginBottom: "28px",
          }}
        >
          <h2 style={{ marginTop: 0, color: "#ddb033" }}>Upload Document</h2>

          <div
            style={{
              border: "2px dashed #3a516e",
              borderRadius: "14px",
              padding: "24px",
              textAlign: "center",
              background: "#e932e351",
            }}
          >
            <input
              type="file"
              onChange={(e) => setFile(e.target.files[0])}
              style={{ marginBottom: "16px" }}
            />
            <br />
            <button
              onClick={handleUpload}
              style={{
                background: "#c42294",
                color: "white",
                border: "none",
                padding: "12px 22px",
                borderRadius: "10px",
                cursor: "pointer",
                fontSize: "15px",
                fontWeight: "bold",
              }}
            >
              Upload and Analyze
            </button>

            {file && (
              <p style={{ marginTop: "14px", color: "#334155" }}>
                Selected file: <b>{file.name}</b>
              </p>
            )}
          </div>

          {loading && (
            <p style={{ marginTop: "18px", color: "#222a11", fontWeight: "bold" }}>
              Analyzing document...
            </p>
          )}

          {error && (
            <p style={{ marginTop: "18px", color: "#dc2626", fontWeight: "bold" }}>
              {error}
            </p>
          )}
        </div>

        {results.length > 0 && (
          <div>
            <h2 style={{ color: "#0f172a", marginBottom: "18px" }}>Analysis Results</h2>

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
                gap: "18px",
              }}
            >
              {results.map((item, index) => (
                <div
                  key={index}
                  style={{
                    background: "#ffffff",
                    borderRadius: "16px",
                    padding: "20px",
                    boxShadow: "0 6px 18px rgba(15, 23, 42, 0.08)",
                    borderTop: `6px solid ${getRiskColor(item.risk_score)}`,
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      marginBottom: "12px",
                    }}
                  >
                    <h3 style={{ margin: 0, color: "#0f172a", fontSize: "18px" }}>
                      {item.type}
                    </h3>
                    <span
                      style={{
                        background: "#eef2ff",
                        color: "#1e3a8a",
                        padding: "6px 10px",
                        borderRadius: "999px",
                        fontSize: "13px",
                        fontWeight: "bold",
                      }}
                    >
                      Risk {item.risk_score}
                    </span>
                  </div>

                  <div style={{ marginBottom: "10px", color: "#334155" }}>
                    <b>Confidence:</b>{" "}
                    {typeof item.confidence === "number"
                      ? item.confidence.toFixed(2)
                      : item.confidence}
                  </div>

                  <div style={{ marginBottom: "12px", color: "#334155" }}>
                    <b>Reason:</b> {item.risk_reason}
                  </div>

                  <div
                    style={{
                      background: "#f8fafc",
                      border: "1px solid #e2e8f0",
                      borderRadius: "12px",
                      padding: "14px",
                      color: "#1e293b",
                      lineHeight: "1.5",
                    }}
                  >
                    {item.text}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}