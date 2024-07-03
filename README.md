## URL FOR HOSTED APP ##
`https://ds-flights-5.onrender.com`

## Overview ##

- `data/`: Directory containing the dataset(s).
- `templates/`: Directory containing HTML templates.
- `app.py`: The main Flask application file.
- `forms.py`: File containing form definitions and data loading logic.
- `model-training.ipynb`: Jupyter notebook used for training the model.
- `model.joblib`: Serialized model file.
- `README.md`: This file.

## Features

- Predicts flight prices based on input parameters.
- Web interface built using Flask.
- Deployed on Render for public access.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (for creating virtual environments)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DS_Flights.git
cd DS_Flights
```

2. Create a virtual environment and activate it:
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
3 Install the required packages:
```
pip install -r flask_proj/requirements.txt
```
4 Run the Flask application:
```
cd flask_proj
gunicorn --pythonpath flask_proj flask_proj.app:app --bind 0.0.0.0:$PORT
```
To run locally 
```
cd flask_proj
python app.py
```

