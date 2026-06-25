import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <h2>PlagiScan AI</h2>

      <div>
        <Link to="/">Home</Link>
        <Link to="/history">History</Link>
      </div>
    </nav>
  );
}

export default Navbar;