import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Campify</h1>
        <div className="button-container">
          <button onClick={() => navigate("/red")}>Connect Spotify</button>
          <button onClick={() => navigate("/green")}>Connect Apple Music</button>
          <button onClick={() => navigate("/blue")}>Go to Blue Page</button>
        </div>
      </header>
    </div>
  );
};

export default Home;