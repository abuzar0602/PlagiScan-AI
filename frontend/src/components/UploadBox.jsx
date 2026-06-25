import { useState } from "react";
import SimilarityMeter from "./SimilarityMeter";
import axios from "axios";
import { FiUploadCloud } from "react-icons/fi";

function UploadBox() {
  const [files, setFiles] = useState([]);
  const [dragActive, setDragActive] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleFiles = (selectedFiles) => {
    setFiles(Array.from(selectedFiles));
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragActive(false);
    handleFiles(e.dataTransfer.files);
  };

  const handleAnalyze = async () => {
    if (files.length < 2) {
      alert("Please upload at least 2 files");
      return;
    }

    const formData = new FormData();

    files.forEach((file) => {
      formData.append("files", file);
    });

    try {
      setLoading(true);

      const response = await axios.post(
        "https://plagiscan-ai.onrender.com/api/scan",
        formData
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error analyzing documents");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div
        className={`drop-zone ${dragActive ? "active" : ""}`}
        onDragEnter={() => setDragActive(true)}
        onDragLeave={() => setDragActive(false)}
        onDragOver={(e) => e.preventDefault()}
        onDrop={handleDrop}
      >
        <FiUploadCloud size={70} />

        <h2>Drag & Drop Files</h2>

        <p>PDF, DOCX, TXT Supported</p>

        <input
          type="file"
          multiple
          onChange={(e) => handleFiles(e.target.files)}
        />

        <button onClick={handleAnalyze}>
          {loading ? "Analyzing..." : "Analyze Documents"}
        </button>
      </div>

      {files.length > 0 && (
        <div className="file-list">
          <h3>Selected Files</h3>

          {files.map((file, index) => (
            <p key={index}>{file.name}</p>
          ))}
        </div>
      )}

      {result && (
        <div className="results-container">
          <h2>Results</h2>
          <button
  onClick={() =>
    window.open(
      "https://plagiscan-ai.onrender.com/api/report",
      "_blank"
    )
  }
>
  Download Report
</button>
          <SimilarityMeter
  value={result.overall_similarity}
/>

          <div className="stats-grid">
            <div className="result-card">
              <h3>Similarity</h3>
              <h2>{result.overall_similarity}%</h2>
            </div>

            <div className="result-card">
              <h3>Risk Level</h3>
              <h2>{result.risk_level}</h2>
            </div>

            <div className="result-card">
              <h3>Documents</h3>
              <h2>{result.total_documents}</h2>
            </div>

            <div className="result-card">
              <h3>Total Words</h3>
              <h2>{result.total_words}</h2>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default UploadBox;