# Movie Recommender

A simple Streamlit movie recommender app built with Python. The app uses a precomputed similarity matrix and a movie dictionary to recommend 5 movies based on the selected title.

## Features

- Select a movie from a dropdown list
- Generate 5 recommended movies using a precomputed similarity matrix
- Built with Streamlit for a lightweight web UI

## Files

- `app.py` - Streamlit application entrypoint
- `movie_dict.pkl` - serialized movie dataset used by the app
- `similarity.pkl` - serialized similarity matrix used for recommendations
- `tmdb_5000_credits.csv` - original TMDB credits dataset
- `tmdb_5000_movies.csv` - original TMDB movies dataset
- `requirements.txt` - project dependencies
- `setup.sh` - Streamlit environment configuration for deployment
- `procfile` - Heroku-style startup command
- `main.ipynb` - notebook for exploration or development

## Requirements

- Python 3.11+ (recommended)
- `streamlit`
- `pandas`

> The existing `requirements.txt` includes a full environment snapshot. For a minimal install, you mainly need `streamlit`, `pandas`, and Python standard libraries.

## Installation

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run locally

Start the Streamlit app from the project folder:

```powershell
streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`).

## Deployment

For Heroku-style deployment, the app uses `setup.sh` and `procfile`.

- `setup.sh` sets Streamlit server configuration for the hosting environment.
- `procfile` runs the app with:

```text
web: sh setup.sh && streamlit run app.py
```

## Usage

1. Open the web app UI.
2. Choose a movie from the dropdown.
3. Click **Recommend**.
4. View the top 5 recommended movies.

## Notes

- Make sure `movie_dict.pkl` and `similarity.pkl` are present in the same directory as `app.py`.
- `app.py` currently uses the first selected movie name match from the movie title list.

## License

This project does not include a license file. Add one if you want to share or distribute the app.
