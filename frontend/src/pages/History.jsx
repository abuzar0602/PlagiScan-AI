import { useEffect, useState } from "react";
import axios from "axios";
import api from "../services/api";
import Navbar from "../components/Navbar";

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/history")
      .then((res) => {
        setHistory(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <>
      <Navbar />

      <div className="history-page">
        <h1>Scan History</h1>

        {loading ? (
          <p>Loading...</p>
        ) : history.length === 0 ? (
          <p>No scans found.</p>
        ) : (
          <table className="history-table">
            <thead>
              <tr>
                <th>Files</th>
                <th>Similarity</th>
                <th>Risk</th>
                <th>Words</th>
              </tr>
            </thead>

            <tbody>
              {history.map((scan) => (
                <tr key={scan.id}>
                  <td>{scan.filename}</td>
                  <td>{scan.similarity_score}%</td>
                  <td>{scan.risk_level}</td>
                  <td>{scan.total_words}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
}

export default History;