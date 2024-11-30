import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="App-container">
      <div className="App-header">
        <h1>Welcome to Campify</h1>
      </div>

      <div className="button-container">
        <button onClick={() => navigate("/red")}>Connect Spotify</button>
      </div>

      <footer className="footer">
        <p>Made by Sophia Shaw, Sophia Zhang, Heather Nguyen, & Jyoti Maharjan</p>
      </footer>
    </div>
  );
};

export default Home;
