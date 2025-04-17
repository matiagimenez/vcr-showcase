# 🎞️ VCR Showcase

This repository demonstrates how to use [VCR.py](https://github.com/kevin1024/vcrpy) to record and replay HTTP interactions in your tests. This helps make tests faster, more reliable, and independent of external APIs.

## 📦 What’s Inside

- Basic usage of `vcr` with `pytest`
- Example using the `requests` library
- Automatically records HTTP responses to cassette files (`.yaml`)
- Replays responses on future test runs, avoiding real network calls