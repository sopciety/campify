import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="App">
      <header className="App-header">
        <h1>Campify</h1>
        <div className="button-container">
          <button onClick={() => navigate("/red")}>Go to Red Page</button>
          <button onClick={() => navigate("/green")}>Go to Green Page</button>
          <button onClick={() => navigate("/blue")}>Go to Blue Page</button>
        </div>
      </header>
    </div>
  );
};

export default Home;
