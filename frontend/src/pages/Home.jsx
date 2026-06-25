import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";

function Home() {
  return (
    <>
      <Navbar />
      <div className="container">

      {/* Hero Section */}
      <div className="hero">
        <h1>PlagiScan AI</h1>
        <p>AI-Powered Plagiarism Detection System</p>
      </div>

      {/* Feature Cards */}
      <div className="features">

        <div className="feature-card">
          <h3>Document Analysis</h3>
          <p>Analyze TXT, PDF and DOCX files.</p>
        </div>

        <div className="feature-card">
          <h3>Similarity Detection</h3>
          <p>Find plagiarism using AI techniques.</p>
        </div>

        <div className="feature-card">
          <h3>PDF Reports</h3>
          <p>Download detailed plagiarism reports.</p>
        </div>

      </div>

      {/* Upload Section */}
      <UploadBox />
      <footer className="footer">
  <p>
    © 2026 PlagiScan-AI 
  </p>
</footer>
</div>

    </>
  );
}

export default Home;