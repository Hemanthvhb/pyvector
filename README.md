# VecFind - Lite

A lightweight in-memory vector database and semantic search engine built from scratch in Python.

## What it does

Stores high-dimensional vectors and finds the closest match to any query vector using a custom KD-Tree implementation. Designed for use as the memory layer in AI and RAG applications.

## How it works

```
insert vectors → stored in KD-Tree (O log N structure)
query vector   → KD-Tree search with backtracking → closest match returned
```

## Setup

```bash
git clone https://github.com/yourusername/vecfind
cd vecfind
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## API

**Insert a vector:**
```bash
curl -X POST http://localhost:8000/insert \
  -H "Content-Type: application/json" \
  -d '{"vector": [1.0, 2.0, 3.0], "payload": {"name": "cat"}}'
```

**Search for closest vector:**
```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"vector": [1.1, 2.1, 3.1]}'
```

**Response:**
```json
{
  "payload": {"name": "cat"},
  "distance": 0.173
}
```
## Run the demo

```bash
python demo.py
```

## Run tests

```bash
py -m pytest tests/ -v
```

## Project structure

```
vecfind/
├── main.py          — FastAPI server and endpoints
├── kdtree.py        — custom KD-Tree (build, search, insert)
├── math_engine.py   — NumPy distance functions
├── models.py        — Pydantic request/response models
├── benchmark.py     — search time vs dataset size
├── demo.py          — live demo with sample data
├── benchmark.png    — benchmark chart
└── tests/
    ├── test_api.py
    ├── test_kdtree.py
    └── test_math_engine.py
```

## Known limitations

- KD-Trees degrade past ~20 dimensions (curse of dimensionality). For high-dimensional embeddings (768D, 1536D), an ANN algorithm like HNSW would be used instead — planned for v2.
- No persistence — all data lives in RAM and is lost on server restart.
- Repeated insertions can unbalance the tree over time — periodic rebuilding would address this at scale.

## Tech stack

| Layer | Library |
|-------|---------|
| Math engine | NumPy |
| Web server | FastAPI, Uvicorn |
| Data validation | Pydantic |
| Testing | pytest |
| Benchmarking | Matplotlib |
