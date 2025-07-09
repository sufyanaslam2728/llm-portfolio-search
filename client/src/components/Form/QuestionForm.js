import React, { useState } from "react";
import "./QuestionForm.css";

const QuestionForm = () => {
  const [question, setQuestion] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [responseData, setResponseData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setResponseData(null);

    if (!question.trim()) {
      setError("Question is required");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error("Something went wrong while submitting the question");
      }

      const data = await response.json();
      setResponseData(data);
      console.log(data, data);
    } catch (err) {
      setError(err.message);
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    setResponseData(null);
    setQuestion("");
    setError("");
  };

  if (responseData) {
    return (
      <div className="form-container">
        <h2 className="form-heading">Response Summary</h2>
        <p className="form-summary">{responseData.summary}</p>

        <div className="projects">
          {responseData.projects?.map((project) => (
            <div className="project-card" key={project.id}>
              <h3>{project.name}</h3>
              <p>
                <strong>Industry:</strong> {project.industry}
              </p>
              <p>{project.description}</p>
              <p>
                <strong>Tags:</strong> {project.tags.join(", ")}
              </p>
              <a href={project.link} target="_blank" rel="noopener noreferrer">
                Visit Website
              </a>
            </div>
          ))}
        </div>

        <button className="form-button back-button" onClick={handleBack}>
          ← Back to Question Form
        </button>
      </div>
    );
  }

  return (
    <div className="form-container">
      <h2 className="form-heading">Ask a Question</h2>
      <form onSubmit={handleSubmit} className="question-form">
        <label htmlFor="question" className="form-label">
          Your Question
        </label>
        <input
          type="text"
          id="question"
          name="question"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="form-input"
          placeholder="Type your question here..."
        />
        {error && <p className="form-error">{error}</p>}

        <button type="submit" disabled={loading} className="form-button">
          {loading ? "Submitting..." : "Submit"}
        </button>

        {loading && (
          <div className="form-loader">⏳ Submitting your question...</div>
        )}
      </form>
    </div>
  );
};

export default QuestionForm;
