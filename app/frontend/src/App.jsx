import { useState } from "react";
import axios from "axios";

function App() {
  const [liked, setLiked] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const getRecommendations = async () => {
    try {
      const response = await axios.post("http://localhost:8000/recommend", {
        liked_movies: liked.split(",").map(m => m.trim())
      });
      setRecommendations(response.data.recommendations);
    } catch (err) {
      alert("No matches found or error occurred.");
      setRecommendations([]);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Movie Recommender</h1>
      <input
        type="text"
        value={liked}
        onChange={(e) => setLiked(e.target.value)}
        placeholder="Type movies you liked, separated by commas"
        style={{ width: "80%", padding: 10 }}
      />
      <button onClick={getRecommendations} style={{ marginLeft: 10, padding: 10 }}>
        Recommend
      </button>

      {recommendations.length > 0 && (
        <div style={{ marginTop: 20 }}>
          <h2>Recommended Movies</h2>
          <ul>
            {recommendations.map((movie, index) => (
              <li key={index}>{movie}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
