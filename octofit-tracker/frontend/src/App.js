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
                <div style={{fontSize: '4rem', marginBottom: '1rem'}}>🦸‍♂️ 💪 🦸‍♀️</div>
                <h1 className="display-3 fw-bold">Unleash Your Inner Hero!</h1>
                <p className="lead fs-4 mt-3">Join the OctoFit Tracker and transform your fitness journey into an epic adventure.</p>
                <hr className="my-4" style={{borderColor: 'rgba(255,255,255,0.5)', borderWidth: '2px'}} />
                <p className="fs-5 mb-4">⚡ Track activities • 🏆 Compete with heroes • 🚀 Reach legendary status</p>
                <div className="mt-4">
                  <Link to="/users" className="btn btn-light btn-lg btn-custom me-3 mb-2">
                    🦸 Join Heroes
                  </Link>
                  <Link to="/leaderboard" className="btn btn-outline-light btn-lg btn-custom mb-2">
                    🏆 View Leaderboard
                  </Link>
                </div>
              </div>
              
              <div className="text-center mt-5 mb-4">
                <h2 className="fw-bold" style={{color: '#667eea'}}>Choose Your Mission</h2>
                <p className="text-muted">Select a category to begin your heroic journey</p>
              </div>
              
              <div className="row mt-4">
                <div className="col-md-4 mb-4">
                  <Link to="/users" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center py-4">
                        <div style={{fontSize: '4rem'}}>🦸</div>
                        <h3 className="card-title mt-3 fw-bold">Heroes</h3>
                        <p className="card-text text-muted">Meet our legendary fitness warriors and their incredible stats</p>
                        <span className="badge bg-primary mt-2">View Profiles</span>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-4 mb-4">
                  <Link to="/activities" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center py-4">
                        <div style={{fontSize: '4rem'}}>⚡</div>
                        <h3 className="card-title mt-3 fw-bold">Activities</h3>
                        <p className="card-text text-muted">Chronicle every heroic feat and training session</p>
                        <span className="badge bg-warning text-dark mt-2">Track Now</span>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-4 mb-4">
                  <Link to="/leaderboard" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center py-4">
                        <div style={{fontSize: '4rem'}}>🏆</div>
                        <h3 className="card-title mt-3 fw-bold">Leaderboard</h3>
                        <p className="card-text text-muted">Rise through the ranks and claim your glory</p>
                        <span className="badge bg-success mt-2">See Rankings</span>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
              
              <div className="row">
                <div className="col-md-6 mb-4">
                  <Link to="/teams" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center py-4">
                        <div style={{fontSize: '4rem'}}>🦸‍♂️🦸‍♀️</div>
                        <h3 className="card-title mt-3 fw-bold">Super Teams</h3>
                        <p className="card-text text-muted">Form alliances and conquer challenges together</p>
                        <span className="badge bg-info mt-2">Join Squad</span>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 mb-4">
                  <Link to="/workouts" className="text-decoration-none">
                    <div className="card data-card h-100 text-center">
                      <div className="card-body d-flex flex-column justify-content-center py-4">
                        <div style={{fontSize: '4rem'}}>🔥</div>
                        <h3 className="card-title mt-3 fw-bold">Power Workouts</h3>
                        <p className="card-text text-muted">Unlock legendary training programs and level up</p>
                        <span className="badge bg-danger mt-2">Start Training</span>
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
