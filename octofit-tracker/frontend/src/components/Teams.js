import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams component: Processed teams:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams component: Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  const getTeamEmoji = (name) => {
    const teamEmojis = ['🦸‍♂️', '🦸‍♀️', '🦹‍♂️', '🦹‍♀️', '⚡', '🔥', '💥', '🌟', '🚀', '🏅', '⭐', '💫'];
    if (!name) return '🦸‍♂️';
    const index = name.length % teamEmojis.length;
    return teamEmojis[index];
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner-border text-primary spinner-border-custom" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading teams...</p>
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

  return (
    <div className="container component-container">
      <div className="row">
        <div className="col-12">
          <div className="card data-card">
            <div className="card-header">
              <h2 className="mb-0"><i className="bi bi-people"></i> Teams</h2>
            </div>
            <div className="card-body">
              <div className="mb-3">
                <span className="badge bg-info badge-custom">Total Teams: {teams.length}</span>
              </div>
              <div className="table-responsive">
                <table className="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Members</th>
              <th>Created</th>
            </tr>
          </thead>
          <tbody>
            {teams.length === 0 ? (
                      <tr>
                        <td colSpan="5" className="text-center text-muted py-4">
                          <i className="bi bi-people" style={{fontSize: '2rem'}}></i>
                          <p className="mb-0 mt-2">No teams found</p>
                        </td>
                      </tr>
                    ) : (
                      teams.map((team) => (
                        <tr key={team.id}>
                          <td><span className="badge bg-secondary">{team.id}</span></td>
                          <td><span style={{fontSize: '1.5rem', marginRight: '0.5rem'}}>{getTeamEmoji(team.name)}</span><strong>{team.name}</strong></td>
                          <td>{team.description || <span className="text-muted">No description</span>}</td>
                          <td><span className="badge bg-success">{team.member_count || 0} members</span></td>
                          <td>{team.created_at ? new Date(team.created_at).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
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

export default Teams;
