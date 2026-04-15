# Baby Birth Weight Predictor

A machine learning-based web application that predicts baby birth weight based on health metrics.

## Project Structure

- **app.py** - Flask backend API
- **index.html** - Frontend interface
- **model.pkl** - Trained prediction model
- **model_training.ipynb** - Model training notebook
- **dataset/babies.csv** - Training dataset

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 3. Open the Frontend

Open `index.html` in your web browser or serve it through a local server:

```bash
# Option 1: Using Python's built-in server
python -m http.server 8000

# Option 2: Using Node.js http-server
npx http-server
```

Then navigate to `http://localhost:8000` (or your chosen port)

## Features

- 📊 User-friendly web interface
- 🧠 Machine learning-based predictions
- 📱 Responsive design for mobile and desktop
- ⚡ Real-time prediction results
- 🎨 Modern, clean UI

## Input Parameters

The predictor accepts the following baby health metrics:

- **Age** (months) - Baby's current age
- **Weight** (kg) - Baby's current weight
- **Height** (cm) - Baby's height
- **Head Circumference** (cm) - Circumference of baby's head
- **Gender** - Female (0) or Male (1)

## API Endpoint

### POST /predict

Send a POST request with baby data to get a weight prediction.

**Request:**
```json
[
  {
    "age": 9,
    "weight": 75,
    "height": 165,
    "head_circumference": 35,
    "gender": 1
  }
]
```

**Response:**
```json
{
  "prediction": 3.45
}
```

## Technology Stack

- **Backend**: Flask, scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **ML**: scikit-learn (model training)
- **Data**: pandas, numpy

## Notes

- Make sure both the Flask server and the frontend are running
- The frontend expects the API to be at `http://localhost:5000`
- The model is already trained and saved as `model.pkl`
