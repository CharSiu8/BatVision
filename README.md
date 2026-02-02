# BatVision - Agentic AI and Image Detection on Batman
# BatVision

AI-powered image classifier that identifies Batman actors (Keaton, Bale, Pattinson) and distinguishes from similar characters (Nite Owl). Built with agentic AI capabilities.

## Features

- **Image Classification:** Upload an image → identifies which Batman actor
- **Agentic Search:** Agent automatically searches for actor filmography and related info based on prediction
- **Similarity Detection:** Flags lookalike characters (Nite Owl) as "Not Batman"

## Tech Stack

- Python
- Bing Image Search API (data collection)
- TensorFlow/PyTorch (model)
- FastAPI (backend)
- Gradio (UI)
- OpenAI API (agentic features)

## Data Structure
```
/data
  /raw
    /keaton
    /bale
    /pattinson
    /nite_owl
  /processed
  manifest.json
```

## Quick Start

1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add API keys to `.env`
4. Run: `python app.py`

## How It Works

1. User uploads image
2. Model classifies Batman actor (or flags as Nite Owl)
3. Agent fetches actor info, filmography, or trivia based on result
4. Returns prediction + enriched context

## License

AGPL-3.0 — Free for personal/educational use. For commercial licensing, contact: stpolino@gmail.com
