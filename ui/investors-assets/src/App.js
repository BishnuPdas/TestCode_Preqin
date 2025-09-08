import React, { useState } from "react";
import InvestorsTable from "./components/InvestorsTable";
import CommitmentsTable from "./components/CommitmentsTable";

function App() {
  const [selectedMenu, setSelectedMenu] = useState("investors");

  return (
    <div>
      <nav style={{ display: "flex", gap: "24px", padding: "24px 20px 8px", borderBottom: "1px solid #eee" }}>
        <MenuItem label="Investors" active={selectedMenu === "investors"} onClick={() => setSelectedMenu("investors")} />
        <MenuItem label="Commitments" active={selectedMenu === "commitments"} onClick={() => setSelectedMenu("commitments")} />
      </nav>
      <div>
        {selectedMenu === "investors" && <InvestorsTable />}
        {selectedMenu === "commitments" && <CommitmentsTable/>}
      </div>
    </div>
  );
}

function MenuItem({ label, active, onClick }) {
  return (
    <button
      style={{
        background: active ? "#23238f" : "#fff",
        color: active ? "#fff" : "#23238f",
        padding: "10px 24px",
        border: "none",
        borderRadius: "20px",
        cursor: "pointer",
        fontWeight: active ? "bold" : "normal",
        fontSize: "1rem",
        boxShadow: active ? "0 2px 8px #ddd" : "none",
        transition: "all 0.15s"
      }}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

export default App;
