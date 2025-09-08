import React, { useEffect, useState } from "react";

export default function InvestorsTable() {
  const [investors, setInvestors] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/investors/")
      .then((res) => res.json())
      .then((data) => {
        setInvestors(data);
        setLoading(false);
      })
      .catch((error) => {
        setLoading(false);
        alert("Failed to fetch investors. Check API and CORS.");
      });
  }, []);

  if (loading) return <div>Loading Investors...</div>;

  return (
    <div style={{ background: "#fff", borderRadius: "8px", padding: "24px", margin: "24px", boxShadow: "0 1px 8px #eee" }}>
      <h2 style={{ fontWeight: "bold", fontSize: "2rem", marginBottom: "24px" }}>Investors</h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr style={{ background: "#fafafa", borderBottom: "2px solid #e5e5e5" }}>
            <th style={{ padding: "8px" }}>Id</th>
            <th style={{ padding: "8px" }}>Name</th>
            <th style={{ padding: "8px" }}>Type</th>
            <th style={{ padding: "8px" }}>Date Added</th>
            <th style={{ padding: "8px" }}>Country</th>
            <th style={{ padding: "8px" }}>Total Commitment</th>
          </tr>
        </thead>
        <tbody>
          {investors.map(inv => (
            <tr key={inv.id} style={{ borderBottom: "1px solid #eee" }}>
              <td style={{ padding: "8px" }}>{inv.id}</td>
              <td style={{ padding: "8px" }}>{inv.name}</td>
              <td style={{ padding: "8px" }}>{inv.type}</td>
              <td style={{ padding: "8px" }}>{inv.date_added}</td>
              <td style={{ padding: "8px" }}>{inv.country}</td>
              <td style={{ padding: "8px", color: "#2f1ecc", fontWeight: "bold" }}>{inv.total_commitment}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
