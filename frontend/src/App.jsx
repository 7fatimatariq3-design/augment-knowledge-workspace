import { BrowserRouter, Routes, Route } from "react-router-dom";

// Milestone 2: implement these pages
// import LoginPage from "./pages/LoginPage";
// import DashboardPage from "./pages/DashboardPage";
// import DocumentsPage from "./pages/DocumentsPage";
// import ChatPage from "./pages/ChatPage";

function Placeholder({ label }) {
  return <div style={{ padding: "2rem" }}>{label} — coming in a later milestone</div>;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Placeholder label="Dashboard" />} />
        <Route path="/login" element={<Placeholder label="Login" />} />
        <Route path="/documents" element={<Placeholder label="Documents" />} />
        <Route path="/chat" element={<Placeholder label="AI Chat" />} />
      </Routes>
    </BrowserRouter>
  );
}
