import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/dashboard.js';
import Welcome from './components/welcome.js';
import SimulationReports from './components/reports.js';
import './styles/output.css';
function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('/api/data/')
            .then(response => setMessage(response.data.message))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
      <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/" element={<Welcome />} />
        <Route path="/reports" element={<SimulationReports/>}/>
        
      </Routes>
    </Router>
    );
}

export default App;
