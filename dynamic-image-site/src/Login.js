import React from 'react';
import { Link } from 'react-router-dom';
import './Login.css';

function Login() {
  return (
    <div className="login-container">
      <div className="login-card">
        <h1>Welcome to Camp Tunes</h1>
        <p>Your soundtrack for adventure</p>

        <div className="button-container">
          <Link to="/music">
            <button className="login-button">Listen Now</button>
          </Link>
          <Link to="/campsites">
            <button className="login-button">Explore Campsites</button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Login;
