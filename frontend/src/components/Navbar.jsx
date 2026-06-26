import { Link } from "react-router-dom";
import { FiShield } from "react-icons/fi";

function Navbar() {
  return (
    <header className="navbar">
      <div className="logo">
        <FiShield />
        <span>PlagiScan AI</span>
      </div>

      <nav className="nav-menu">
        <Link to="/">    Home    </Link>
        <Link to="/history">    History     </Link>
      </nav>

    </header>
  );
}

export default Navbar;