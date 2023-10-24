import React, { useState } from "react";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append("image", selectedFile);

      try {
        const response = await fetch("http://localhost:5000/predict", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();
        setPrediction(data.class_name);
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  return (
    <div className="App">
      <h1>Image Classification</h1>
      <input
        type="file"
        accept=".jpg, .jpeg, .png"
        onChange={handleFileChange}
      />
      <button onClick={handleUpload}>Predict</button>
      <div>
        {prediction && (
          <div>
            <h2>Predicted Class:</h2>
            <p>{prediction}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
