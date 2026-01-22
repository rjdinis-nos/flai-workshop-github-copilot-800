import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard component: Processed leaderboard:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard component: Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner-border text-primary spinner-border-custom" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading leaderboard...</p>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="error-container">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  const getRankBadge = (rank) => {
    if (rank === 1) return <span className="badge bg-warning text-dark">🥇 {rank}</span>;
    if (rank === 2) return <span className="badge bg-secondary">🥈 {rank}</span>;
    if (rank === 3) return <span className="badge bg-danger">🥉 {rank}</span>;
    return <span className="badge bg-primary">{rank}</span>;
  };

  return (
    <div className="container component-container">
      <div className="row">
        <div className="col-12">
          <div className="card data-card">
            <div className="card-header">
              <h2 className="mb-0"><i className="bi bi-trophy"></i> Leaderboard</h2>
            </div>
            <div className="card-body">
              <div className="mb-3">
                <span className="badge bg-success badge-custom">Total Competitors: {leaderboard.length}</span>
              </div>
              <div className="table-responsive">
                <table className="table table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Type</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length === 0 ? (
                      <tr>
                        <td colSpan="5" className="text-center text-muted py-4">
                          <i className="bi bi-trophy" style={{fontSize: '2rem'}}></i>
                          <p className="mb-0 mt-2">No leaderboard data found</p>
                        </td>
                      </tr>
                    ) : (
                      leaderboard.map((entry, index) => (
                        <tr key={entry.id || index}>
                          <td>{getRankBadge(entry.rank || (index + 1))}</td>
                          <td><strong>{entry.user_name || entry.user_alias || 'N/A'}</strong></td>
                          <td><span className="badge bg-info">{entry.team_name || entry.team || 'No team'}</span></td>
                          <td><span className="badge bg-success">{entry.total_points || 0} pts</span></td>
                          <td><span className="badge bg-secondary">{entry.type || 'individual'}</span></td>
                        </tr>
                      ))
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
