import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts component: Fetching from API endpoint:', API_URL);
    
    fetch(API_URL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts component: Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts component: Processed workouts:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts component: Error fetching data:', error);
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
        <p className="mt-3 text-muted">Loading workouts...</p>
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

  const getDifficultyBadge = (difficulty) => {
    const difficultyLower = (difficulty || '').toLowerCase();
    if (difficultyLower === 'easy') return <span className="badge bg-success">{difficulty}</span>;
    if (difficultyLower === 'medium') return <span className="badge bg-warning text-dark">{difficulty}</span>;
    if (difficultyLower === 'hard') return <span className="badge bg-danger">{difficulty}</span>;
    return <span className="badge bg-secondary">{difficulty || 'N/A'}</span>;
  };

  return (
    <div className="container component-container">
      <div className="row">
        <div className="col-12">
          <div className="card data-card">
            <div className="card-header">
              <h2 className="mb-0"><i className="bi bi-lightning"></i> Workout Suggestions</h2>
            </div>
            <div className="card-body">
              <div className="mb-3">
                <span className="badge bg-success badge-custom">Available Workouts: {workouts.length}</span>
              </div>
              <div className="table-responsive">
                <table className="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Category</th>
              <th>Description</th>
              <th>Duration (min)</th>
              <th>Difficulty</th>
              <th>Exercises</th>
            </tr>
          </thead>
          <tbody>
            {workouts.length === 0 ? (
                      <tr>
                        <td colSpan="7" className="text-center text-muted py-4">
                          <i className="bi bi-lightning" style={{fontSize: '2rem'}}></i>
                          <p className="mb-0 mt-2">No workouts found</p>
                        </td>
                      </tr>
                    ) : (
                      workouts.map((workout) => (
                        <tr key={workout.id}>
                          <td><span className="badge bg-secondary">{workout.id}</span></td>
                          <td><strong>{workout.name}</strong></td>
                          <td><span className="badge bg-primary">{workout.category || 'N/A'}</span></td>
                          <td>{workout.description || <span className="text-muted">No description</span>}</td>
                          <td><span className="badge bg-info">{workout.duration_minutes || 'N/A'} min</span></td>
                          <td>{getDifficultyBadge(workout.difficulty)}</td>
                          <td><span className="badge bg-success">{workout.exercises ? workout.exercises.length : 0} exercises</span></td>
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

export default Workouts;
