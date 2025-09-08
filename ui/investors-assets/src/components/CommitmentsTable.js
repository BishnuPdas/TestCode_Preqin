import React, { useEffect, useState } from "react";

function formatAmount(amt) {
  if (amt >= 1_000_000_000) return `${(amt / 1_000_000_000).toFixed(1)}B`;
  if (amt >= 1_000_000) return `${(amt / 1_000_000).toFixed(1)}M`;
  return `${amt.toFixed(1)}`;
}

export default function CommitmentsTable() {
  const [commitments, setCommitments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/commitments/") 
      .then(res => res.json())
      .then(data => {
        setCommitments(data);
        setLoading(false);
      })
      .catch(err => {
        setLoading(false);
        alert("Failed to load commitments");
      });
  }, []);

  // Compute summary by asset class
  const summary = {};
  let allTotal = 0;
  commitments.forEach(c => {
    const amt = typeof c.amount === "string" ? parseFloat(c.amount.replace(/[^\d.]/g, "")) * (c.amount.includes("B") ? 1e9 : c.amount.includes("M") ? 1e6 : 1) : c.amount;
    summary[c.asset_class] = (summary[c.asset_class] || 0) + amt;
    allTotal += amt;
  });

  const summaryOrder = [
    ["All", allTotal],
    ...Object.entries(summary)
  ];

  
  return (
    <div style={{ background: "#fff", borderRadius: "8px", padding: "24px", margin: "24px", boxShadow: "0 1px 8px #eee" }}>
      <h2 style={{ fontWeight: "bold", fontSize: "2rem", marginBottom: "24px" }}>Commitments</h2>
      <div style={{ display: "flex", gap: "16px", marginBottom: "24px" }}>
        <SummaryBox label="All" value={formatAmount(allTotal)} />
        {Object.entries(summary).map(([cls, val]) => (
          <SummaryBox key={cls} label={cls} value={formatAmount(val)} />
        ))}
      </div>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr style={{ background: "#fafafa", borderBottom: "2px solid #e5e5e5" }}>
            <th style={{ padding: "8px" }}>Id</th>
            <th style={{ padding: "8px" }}>Asset Class</th>
            <th style={{ padding: "8px" }}>Currency</th>
            <th style={{ padding: "8px" }}>Amount</th>
          </tr>
        </thead>
        <tbody>
          {loading ? (
            <tr><td colSpan="4">Loading...</td></tr>
          ) : (
            commitments.map(c => (
              <tr key={c.id} style={{ borderBottom: "1px solid #eee" }}>
                <td style={{ padding: "8px" }}>{c.id}</td>
                <td style={{ padding: "8px" }}>{c.asset_class}</td>
                <td style={{ padding: "8px" }}>{c.currency}</td>
                <td style={{ padding: "8px" }}>{formatAmount(typeof c.amount === "string" ? parseFloat(c.amount.replace(/[^\d.]/g, "")) * (c.amount.includes("B") ? 1e9 : c.amount.includes("M") ? 1e6 : 1) : c.amount)}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

function SummaryBox({ label, value }) {
  return (
    <div style={{
      border: "1px solid #eee",
      padding: "16px",
      borderRadius: "8px",
      minWidth: "140px",
      textAlign: "center"
    }}>
      <div style={{ fontWeight: "500", fontSize: "1rem", marginBottom: "6px" }}>{label}</div>
      <div style={{ fontWeight: "700", color: "#23238f", fontSize: "1.1rem" }}>£{value}</div>
    </div>
  );
}
