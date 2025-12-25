# Skill-Aware Project Recommendation System

## Project Summary
A content-based machine learning system that recommends software project ideas
based on a user's technical skill set and target role. The system uses feature
vectorization and cosine similarity to generate personalized, explainable
project recommendations.

## Features
- Skill-based project recommendations
- ML-powered cosine similarity ranking
- Identifies matched skills and skill gaps
- Cold-start friendly (no user history required)
- Modular and extensible design

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn

## How It Works
1. User enters skills and target role
2. Skills are vectorized into feature vectors
3. Cosine similarity ranks project relevance
4. Top projects are returned with explanations

## How to Run
```bash
python -m src.main
