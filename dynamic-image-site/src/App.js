import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import RedPage from "./pages/RedPage";
import GreenPage from "./pages/GreenPage";
import BluePage from "./pages/BluePage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/red" element={<RedPage />} />
        <Route path="/green" element={<GreenPage />} />
        <Route path="/blue" element={<BluePage />} />
      </Routes>
      <footer>
  <p>Made by Sophia Shaw, Sophia Zhang, Heather Nguyen, & Jyoti Maharjan</p>
</footer>
    </Router>
  );
}



export default App;
