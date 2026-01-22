import React, { useState, useEffect } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Users component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users component: Processed users:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Users component: Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [API_URL]);

  const getEmojiAvatar = (name) => {
    const emojis = ['🦸', '🦹', '⚡', '🔥', '💪', '🌟', '🚀', '⭐', '💫', '🏆'];
    if (!name) return '🦸';
    const index = name.length % emojis.length;
    return emojis[index];
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner-border text-primary spinner-border-custom" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading users...</p>
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
              <h2 className="mb-0"><i className="bi bi-person-circle"></i> Users</h2>
            </div>
            <div className="card-body">
              <div className="mb-3">
                <span className="badge bg-primary badge-custom">Total Users: {users.length}</span>
              </div>
              <div className="table-responsive">
                <table className="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Alias</th>
              <th>Email</th>
              <th>Team</th>
              <th>Date Joined</th>
            </tr>
          </thead>
          <tbody>
            {users.length === 0 ? (
                      <tr>
                        <td colSpan="6" className="text-center text-muted py-4">
                          <i className="bi bi-person" style={{fontSize: '2rem'}}></i>
                          <p className="mb-0 mt-2">No users found</p>
                        </td>
                      </tr>
                    ) : (
                      users.map((user) => (
                        <tr key={user.id}>
                          <td><span className="badge bg-secondary">{user.id}</span></td>
                          <td><span style={{fontSize: '1.5rem', marginRight: '0.5rem'}}>{getEmojiAvatar(user.name)}</span><strong>{user.name}</strong></td>
                          <td>{user.alias || <span className="text-muted">No alias</span>}</td>
                          <td>{user.email || <span className="text-muted">No email</span>}</td>
                          <td><span className="badge bg-info">{user.team || 'No team'}</span></td>
                          <td>{user.created_at ? new Date(user.created_at).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
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

export default Users;
