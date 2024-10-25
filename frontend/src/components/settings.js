// src/components/Settings.js
import React from 'react';
import Navbar from './Navbar';  // Import the Navbar component

const Settings = () => {
  return (
    <div className="bg-dark text-white min-h-screen">
      {/* Navbar */}
      <Navbar /> {/* Use the Navbar component here */}

      {/* Settings Page Content */}
      <div className="container mx-auto p-6">
        <h1 className="text-4xl font-bold text-steins-green">Settings</h1>
        <p className="text-lg mt-4">Here you can configure your preferences and system settings.</p>
        {/* Add more settings-related content here */}
      </div>
    </div>
  );
};

export default Settings;
