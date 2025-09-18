# 🏎️ F1 Race Winner Predictor

A machine learning pipeline for predicting Formula 1 race outcomes using historical telemetry data, practice session performance, and meteorological conditions. Updated weekly with predictions for each Grand Prix.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastF1](https://img.shields.io/badge/FastF1-3.6+-red.svg)](https://docs.fastf1.dev)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org)
[![Accuracy](https://img.shields.io/badge/Race_Winner_Accuracy-100%25-brightgreen.svg)](https://github.com)

## 🏆 Latest Predictions

### 🇮🇹 2025 Italian Grand Prix (Monza) - September 7, 2025
🥇 **P1**: Lando Norris (McLaren) - 89.971s  
🥈 **P2**: Oscar Piastri (McLaren) - 90.011s  
🥉 **P3**: Charles Leclerc (Ferrari) - 90.173s  

**Model Performance**: R² = 0.835, MAE = 2.4s

## 📊 Season Performance Tracking

| Race | Predicted Winner | Actual Winner | P1 Accuracy | Podium Accuracy | Model R² |
|------|------------------|---------------|-------------|-----------------|----------|
| **Monza** | NOR | *Race: Sept 7* | *TBD* | *TBD* | 0.835 |
| **Zandvoort** | PIA | **PIA** ✅ | ✅ **100%** | ✅ **66%** | 0.559 |

### 🎯 Prediction Accuracy Summary
- **Race Winners**: 1/1 (100%)
- **Podium Finishers**: 2/3 (66%)
- **Average Position Error**: 2.1 positions

## 🏁 Race Results Analysis

### 🇳🇱 2025 Dutch Grand Prix - Zandvoort ✅ COMPLETED

**Final Predictions**:
🥇 **P1**: Oscar Piastri (McLaren) - 87.29s
🥈 **P2**: Lando Norris (McLaren) - 87.68s
🥉 **P3**: Max Verstappen (Red Bull) - 89.13s

| Position | **Predicted** | **Actual** | **Accuracy** |
|----------|---------------|------------|--------------|
| **P1** | **PIA** ✅ | **PIA** | ✅ **CORRECT** |
| **P2** | **NOR** ❌ | **VER** | ❌ Wrong (DNF) |
| **P3** | **VER** ✅ | **HAD** | ❌ Wrong |

**Race Winner**: ✅ **PREDICTED CORRECTLY** - Oscar Piastri  
**Notable**: Norris retired from P2 with mechanical failure, promoting Hadjar to surprise maiden podium

**Actual Final Results**:
1. **Oscar Piastri** (McLaren) - 1:38:29.849  
2. **Max Verstappen** (Red Bull) - +1.271s  
3. **Isack Hadjar** (Racing Bulls) - +3.233s  
4. George Russell (Mercedes) - +5.654s
5. Alexander Albon (Williams) - +6.327s

*DNF: Lando Norris (McLaren), Charles Leclerc (Ferrari), Lewis Hamilton (Ferrari)*

## 🏗️ Technical Architecture

### 📊 Data Pipeline
- **Source**: FastF1 API for telemetry and session data
- **Temporal Coverage**: 2024-2025 F1 seasons
- **Dataset Evolution**: 60 → 319 driver-race combinations
- **Tracks**: Zandvoort (2024), Imola, Suzuka, Miami, Monza (2025)
- **Update Frequency**: Weekly before each Grand Prix

### 🤖 Model Evolution

| Version | Race | Dataset Size | R² Score | MAE (seconds) | Key Improvements |
|---------|------|-------------|----------|---------------|------------------|
| **v2.0** | Monza 2025 | 319 samples | 0.835 | 2.4 | Weather integration, expanded dataset, track encoding |
| **v1.0** | Zandvoort 2025 | 60 samples | 0.559 | 3.89 | Initial Ridge regression implementation |


## Technical Architecture
### Data Pipeline

Source: FastF1 API for telemetry and session data
Temporal Coverage: 2024-2025 F1 seasons
Tracks: Zandvoort (2024), Imola, Suzuka, Miami (2025)
Sample Size: 60 driver-race combinations

## Feature Engineering
### Core Features

Clean Air Race Pace: Best lap time across FP1/FP2/FP3 sessions with track status filtering
Grid Performance: Qualifying position and gap to pole position
Teammate Comparison: Relative qualifying performance within teams
Practice-to-Race Analysis: Practice session consistency and pace differentials

### Derived Features
**Gap-based features**
```
Grid_Gap_to_Pole = GridPosition - min(GridPosition)
Practice_Gap_to_Fastest = CleanAirPace - min(CleanAirPace)
```

**Relative performance**
```
Quali_vs_Teammate = GridPosition - team_mean(GridPosition)
Practice_vs_Quali_Rank = rank(CleanAirPace) - GridPosition
```

### Environmental Data

Air temperature, humidity, atmospheric pressure
Precipitation detection (boolean)
Weather data integrated via OpenWeatherMap API

## Model Development
### Algorithm Selection Process

**Initial Exploration:** Deep Neural Networks, SVMs, XGBoost

**Issue:** Severe overfitting due to small dataset (n=60)
CV Results: High variance (MAE: 8.4±4.0 seconds)


**Final Implementation:** Ridge Regression with L2 regularization

Performance: Test MAE = 3.89 seconds, R² = 0.559
Regularization: α = 1.0



## Model Validation

Cross-Validation: 5-fold stratified CV
Stability Analysis: Standard deviation monitoring
Feature Importance: Coefficient magnitude analysis

## Data Processing Pipeline

### Session Data Extraction

```
def get_clean_air_race_pace(year, race):
    # Multi-session aggregation (FP1, FP2, FP3)
    # Track status filtering (green flag conditions only)
    # Personal best lap identification
    # Cross-session minimum selection
```

### Data Quality Controls

Outlier detection and removal (Miami data corruption: 384s average lap times)
Missing value imputation strategies
Multicollinearity assessment and resolution

## Results Analysis
### Model Performance

Ridge Regression MAE: 3.896 seconds
Linear Regression MAE: 3.882 seconds
Cross-Validation Stability: ±4.0 seconds standard deviation

### Feature Importance (Ridge Regression)

AirTemp: 2.13 (temperature impact on tire performance)
Practice_Gap_to_Fastest: -1.87 (practice pace predictive power)
CleanAirPace_seconds: 1.46 (baseline performance metric)
Race_encoded: -1.07 (track-specific effects)
TeamId_encoded: -0.62 (constructor performance differential)

## Prediction Results

```
Driver    Predicted_LapTime    Team
PIA       87.286              McLaren
NOR       87.683              McLaren  
VER       89.132              Red Bull Racing
HAD       89.594              Racing Bulls
LAW       91.211              Racing Bulls
RUS       91.339              Mercedes
SAI       92.422              Williams
TSU       92.946              Red Bull Racing
LEC       92.983              Ferrari
HAM       93.642              Ferrari
```

## Technical Challenges & Solutions
### Rookie Driver Problem

Challenge: No historical data for new drivers (ANT, BEA, COL)
Solution: Track similarity analysis using medium-high downforce circuits as proxy data

### Data Scarcity

Challenge: Limited sample size causing overfitting in complex models
Solution: Regularized linear models with comprehensive cross-validation

### Multicollinearity Issues

Detection: Correlation matrix analysis (CleanAirPace vs WindSpeed: -0.987)
Resolution: Feature selection and removal of redundant variables

### Dependencies
``` 
# Core libraries
import fastf1
import pandas as pd
import numpy as np
import sklearn

#Specific modules
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, r2_score
```

### Usage
```
# Install dependencies
pip install fastf1 pandas scikit-learn requests matplotlib
```
```
# Run prediction pipeline
python dutch_gp_prediction.ipynb
```

## Model Limitations

Sample Size: 60 observations limit model complexity
Temporal Scope: Limited to 2024-2025 seasons
Weather Prediction: Relies on forecast data for race day conditions
Track Variety: Limited circuit representation in training data

## Future Enhancements

Data Expansion: Integration of additional historical seasons
Feature Engineering: Tire strategy modeling, pit stop prediction
Ensemble Methods: Model combination for improved stability
Real-time Integration: Live telemetry incorporation during race weekends

## Repository Structure
```
f1-winner/
├── data/ # Contains all the dataframes used for training models for each race
│ 
├── prediction_notebooks/ # Notebooks with detailed code for prediction
│   ├── baku_prediction.ipynb
│   ├── dutch_gp_prediction.ipynb
│   ├── monza_prediction.ipynb  
│   ...
│ 
├── scripts/ 
│   └── categorise_by_downforce.py
│
├── venv/ # Environment folder
│
├──  README.md
└── requirements.txt
```