import { useState } from 'react'

export default function App() {
    const [file, setFile] = useState(null);
    const [res, setRes] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleUpload = async () => {
        if (!file){
            setError("PLease select file!!");
            return;
        }
    
    setLoading(true);
    setError("");
    setRes([]);
    
    const formData = new FormData();
    formData.append("file", file);

    try{
        const respon = await fetch("http://127.0.0.1:8000/analyze", {method: "POST", body:formData});
        // console.log(respon)
        if (!respon.ok){
            throw new Error("Failed to analyze file. ");
        }
    const data = await respon.json();
    console.log(data);
    setRes(data);
    }
    catch (err){
        setError(err.message || "Something went wrong.");
        console.error(err);
    }
    finally{
        setLoading(false);
    }
    };

    const getRiskColor= (score) => {
      if (score>=3) return "#f0730d";
      if (score>=2) return "#f59e0b";
      if (score>=1) return "#f6c30b";
      return "#b4f51c"
    };

    return(
      <div
      style={{  fontFamily: "Arial, sans-serif, ",
                minHeight: "100vh",
                background: "rgba(238, 238, 221, 0.4)", 
                // borderRadius: "12px",
                padding: "30 px 20px",
                // boxShadow : "0 2px 10px rgba(0,0,0,0.08)",
            }}
      >
        <div style={{ maxWidth:"900px", margin: "0 auto"}}>
            <div style={{marginBottom: "20px"}}>
              <h1 style={{fontSize: "35px", "marginBottom": "2px", color:"rgba(241, 37, 149, 0.52)"}}>
                Diligence Risk Analyzer
              </h1>
              <p style={{fontSize: "22px", fontStyle: "italic"}}> Upload contract to view extracted clauses and risks. </p>
            </div>
        
        <div
        style={{
          background: "#fffbc5",
          borderRadius: "18px",
          padding: "26px",
          boxShadow: "0 8px 26px rgba(102, 111, 132, 0.08)",
          marginBottom: "27 px",
        }}
        >
          <h2 style={{marginTop: 0, color:"rgba(239, 127, 23, 0.47)", fontSize: "26px"}}> Upload Document </h2>

          <div
          style={{
            border: "2px dashed #cbd5e1",
            borderRadius: "14px",
            padding: "26px",
            textAlign: "center",
            background: "rgba(238, 156, 238, 0.67)"

          }}
          >
            <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            style={{marginBottom: "16px"}}
            />
            <br/>
            <button  
            onClick={handleUpload}
            style={{
              background: "#25ebca",
              color:"white",
              // border:"none",
              padding: "12px 52 px",
              borderRadius: "10px",
              cursor: "pointer",
              fontSize: "15px",
              fontWeight: "bold",
            }
            }>
              Upload to see result
            </button>

            {file && (
              <p style={{marginTop:"14px", color: "#334155"}}>
                Selected file: <b>{file.name} </b>
              </p>
            )}
          </div>
          {
            loading && (
              <p style={{ marginTop: "18px", color: "rgba(38, 38, 26, 0.8)", fontWeight: "bold"}}>
                Analyzing document ..
              </p>
            )
          }
          {
            error && (
              <p style ={{marginTop: "18px", color:"rgba(208, 123, 58, 0.4)"}}>
              {error}
              </p>
            )
          }
        </div>
        {res.length > 0 && (
          <div>
            <h2 style ={{color: "#10080d", marginBottom:"18px"}}>ANALYSIS RESULTS</h2>
            <div
            style={{
              display:"grid",
              gridTemplateColumns: "repeat(auto-fit, minmax(450px, 1fr))",
              gap: "18px",
            }}>
              {res.map((item, index) => (
                <div
                key={index}
                style={{
                  background:"#ffffff",
                  borderRadius: "16px",
                  padding:"20px",
                  boxShadow: "0 6px 18px rgba(20, 23, 42, 0.08)",
                  borderTop: `6px solid ${getRiskColor(item.risk_score)}`,

                }}
                >
                  <div style={{width: "100%"}}>
                  <div
                  style={{
                    display:"flex",
                    justfiyContent: "space-between",
                    alignItems: "center",
                    marginBottom: "12px",
                  }}
                  >
                    <div style={{color: "#0c1112", fontSize:"22px", fontWeight: "bold", }}> {item.predictiontype}  </div>
                    <div style={{
                      background: "rgba(80, 32, 56, 0.89)",
                      color: getRiskColor(item.risk_score),
                      marginLeft:"auto",

                      padding:"6px 10px",
                      borderRadius: "999px",
                      fontSize: "13px",
                      fontWeight: "bold",
                    
                    }}
                    >
                      Risk: {item.risk}
                    </div>
                    
                    {/* <h3 style={{margin:0, color: "#0c1112", fontSize:"22px"}}>
                      {item.predictiontype}  
                    </h3> */}
                    {/* <span style={{color: "#0c1112", fontSize:"22px", fontWeight: "bold", }}> {item.predictiontype}  </span>  */}
                    {/* <br/> */}
                    {/* <span
                    style={{
                      background: "rgba(80, 32, 56, 0.89)",
                      color: getRiskColor(item.risk),
                      padding:"6px 10px",
                      borderRadius: "999px",
                      fontSize: "13px",
                      fontWeight: "bold",
                      alignContent:"end",
                    }}
                    >
                      Risk: {item.risk}
                    </span>  */}

                  </div>
                  </div>
                  <div style={{marginBottom:"10px", color: "rgba(35, 47, 36, 0.89)"}}>
                    <b>Confidence:</b>{" "}
                    {typeof item.confidence === "number"
                    ? item.confidence.toFixed(2): item.confidence}
                  </div>
                    
                    <div style={{marginBottom: "12px", color:"rgba(41, 17, 29, 0.77)"}}>
                      <b>Reason: </b>{item.reason}
                    </div>

                    <div
                    style={{
                      background: "#f8fafc",
                      border: "1px solid #e2e8f0",
                      borderRadius: "14px",
                      padding: "14px",
                      color:"#1e293b",
                      lineHeight: "1.5",
                    }}
                    >
                      {item.text}
                    </div>
                    {/* <br/> */}
                    {/* <div style={{fontSize:"12px"}}>  Manual Review advised: {item.review} </div> */}
                  </div>
              ))}
            </div>
          </div>
        )}
        </div>
      </div>
    );
}

// export default App;
