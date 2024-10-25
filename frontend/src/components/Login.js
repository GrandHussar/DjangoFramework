// src/components/Login.js
import React, { useState, useEffect } from 'react';
import axiosInstance from '../utils/axiosInstance';  // Use the custom axios instance
import { useNavigate } from 'react-router-dom';
import './steinsGateStyle.css';  // Import Steins;Gate styling

const Login = () => {
  const [username, setUsername] = useState(''); 
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [authenticated, setAuthenticated] = useState(false);

  const navigate = useNavigate();

  // Check if the user is already logged in
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // If token is found, redirect to the dashboard
      setAuthenticated(true);
      navigate('/dashboard');
    }
  }, [navigate]);

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axiosInstance.post('/auth/login/', {
        username,
        password,
      });

      // Store the token in localStorage
      localStorage.setItem('token', response.data.key);

      // Mark the user as authenticated and redirect to the dashboard
      setAuthenticated(true);
      setError('');
      navigate('/dashboard');
    } catch (err) {
      setError('Invalid username/email or password.');
    } finally {
      setLoading(false);
    }
  };

  if (authenticated) {
    return <p className="text-steins-green">Redirecting to the dashboard...</p>;
  }

  return (
    <div className="login-container steins-bg">  {/* Steins;Gate Background */}
      <div className="login-box steins-box">  {/* Steins;Gate styled box */}
        <h2 className="text-steins-green text-center mb-6">Login</h2>
        <form onSubmit={handleLogin}>
          <div className="form-group">
            <label className="text-steins-green">Username or Email:</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="form-control bg-dark text-white"
              required
            />
          </div>
          <div className="form-group">
            <label className="text-steins-green">Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="form-control bg-dark text-white"
              required
            />
          </div>
          {error && <p className="error-message text-steins-green">{error}</p>}
          <button type="submit" className="btn steins-btn" disabled={loading}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
