import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container component-container">
              <div className="home-hero">
                <h1 className="display-4">🏃 Welcome to OctoFit Tracker!</h1>
                <p className="lead">Track your fitness activities, compete with teams, and reach your goals.</p>
                <hr className="my-4" style={{borderColor: 'rgba(255,255,255,0.3)'}} />
                <p className="mb-0">Use the navigation menu above or the cards below to explore different sections of the app.</p>
              </div>
              
              <div className="row mt-4">
                <div className="col-md-4 mb-4">
                  <Link to="/users" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center">
                        <i className="bi bi-person-circle" style={{fontSize: '3rem', color: '#667eea'}}></i>
                        <h3 className="card-title mt-3">Users</h3>
                        <p className="card-text text-muted">View all registered users and their profiles</p>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-4 mb-4">
                  <Link to="/activities" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center">
                        <i className="bi bi-activity" style={{fontSize: '3rem', color: '#667eea'}}></i>
                        <h3 className="card-title mt-3">Activities</h3>
                        <p className="card-text text-muted">Track and view all fitness activities</p>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-4 mb-4">
                  <Link to="/leaderboard" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center">
                        <i className="bi bi-trophy" style={{fontSize: '3rem', color: '#667eea'}}></i>
                        <h3 className="card-title mt-3">Leaderboard</h3>
                        <p className="card-text text-muted">See top performers and rankings</p>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
              
              <div className="row">
                <div className="col-md-6 mb-4">
                  <Link to="/teams" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center">
                        <i className="bi bi-people" style={{fontSize: '3rem', color: '#667eea'}}></i>
                        <h3 className="card-title mt-3">Teams</h3>
                        <p className="card-text text-muted">Manage and view team competitions</p>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 mb-4">
                  <Link to="/workouts" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center">
                        <i className="bi bi-lightning" style={{fontSize: '3rem', color: '#667eea'}}></i>
                        <h3 className="card-title mt-3">Workouts</h3>
                        <p className="card-text text-muted">Browse personalized workout suggestions</p>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
