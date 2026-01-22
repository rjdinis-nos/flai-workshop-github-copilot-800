import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Activities component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Activities component: Processed activities:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities component: Error fetching data:', error);
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
        <p className="mt-3 text-muted">Loading activities...</p>
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
              <h2 className="mb-0"><i className="bi bi-activity"></i> Activities Log</h2>
            </div>
            <div className="card-body">
              <div className="mb-3 d-flex justify-content-between align-items-center">
                <span className="badge bg-primary badge-custom">Total Activities: {activities.length}</span>
              </div>
              <div className="table-responsive">
                <table className="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>User</th>
              <th>Activity Type</th>
              <th>Duration (min)</th>
              <th>Calories</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.length === 0 ? (
                      <tr>
                        <td colSpan="6" className="text-center text-muted py-4">
                          <i className="bi bi-inbox" style={{fontSize: '2rem'}}></i>
                          <p className="mb-0 mt-2">No activities found</p>
                        </td>
                      </tr>
                    ) : (
                      activities.map((activity) => (
                        <tr key={activity.id}>
                          <td><span className="badge bg-secondary">{activity.id}</span></td>
                          <td><strong>{activity.user_name || activity.user_alias || 'N/A'}</strong></td>
                          <td><span className="badge bg-info">{activity.activity_type}</span></td>
                          <td>{activity.duration_minutes} min</td>
                          <td><span className="badge bg-warning text-dark">{activity.calories_burned} cal</span></td>
                          <td>{activity.date ? new Date(activity.date).toLocaleDateString() : <span className="text-muted">N/A</span>}</td>
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

export default Activities;
