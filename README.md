# 🏎️ F1 Race Winner Predictor

A machine learning pipeline for predicting Formula 1 race outcomes using historical telemetry data, practice session performance, and meteorological conditions. Updated weekly with predictions for each Grand Prix.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastF1](https://img.shields.io/badge/FastF1-3.6+-red.svg)](https://docs.fastf1.dev)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org)
[![Accuracy](https://img.shields.io/badge/Race_Winner_Accuracy-50%25-yellow.svg)](https://github.com)

## 🏆 Latest Predictions

### 🇦🇿 2025 Azerbaijan Grand Prix (Baku) - September 21, 2025
🥇 **P1**: Max Verstappen (Red Bull) - 159.84s  
🥈 **P2**: George Russell (Mercedes) - 159.88s  
🥉 **P3**: Yuki Tsunoda (Red Bull) - 160.22s  

**Model Performance**: R² = 0.925, MAE = 2.182s
**Prediction**: Red Bull double podium with Verstappen leading

## 📊 Season Performance Tracking

| Race | Predicted Winner | Actual Winner | P1 Accuracy | Podium Accuracy | Model R² |
|------|------------------|---------------|-------------|-----------------|----------|
| **Baku** | VER | *Race: Sept 21* | *TBD* | *TBD* | 0.925 |
| **Monza** | NOR | **VER** ❌ | ❌ **0%** | ✅ **66%** | 0.835 |
| **Zandvoort** | PIA | **PIA** ✅ | ✅ **100%** | ✅ **66%** | 0.559 |

### 🎯 Prediction Accuracy Summary
- **Race Winners**: 1/2 (50%)
- **Podium Finishers**: 4/6 (66%)
- **Average Position Error**: 2.3 positions

## 🏁 Race Results Analysis

### 🇮🇹 2025 Italian Grand Prix - Monza ✅ COMPLETED

**Final Predictions**:
🥇 **P1**: Lando Norris (McLaren) - 89.971s
🥈 **P2**: Oscar Piastri (McLaren) - 90.011s
🥉 **P3**: Charles Leclerc (Ferrari) - 90.173s

| Position | **Predicted** | **Actual** | **Accuracy** |
|----------|---------------|------------|--------------|
| **P1** | **NOR** ❌ | **VER** | ❌ **WRONG** |
| **P2** | **PIA** ✅ | **NOR** | ❌ Wrong position |
| **P3** | **LEC** ❌ | **PIA** | ❌ Wrong position |

**Race Winner**: ❌ **PREDICTED INCORRECTLY** - Predicted Norris, actual winner was Verstappen  
**Notable**: McLaren dominated practice but Verstappen converted pole position into victory after a dramatic start

**Actual Final Results**:
1. **Max Verstappen** (Red Bull) - Winner (from pole)
2. **Lando Norris** (McLaren) - +19.649s  
3. **Oscar Piastri** (McLaren) - +19.649s (team orders swap)
4. Charles Leclerc (Ferrari)
5. George Russell (Mercedes)
6. Lewis Hamilton (Ferrari)

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
- **Dataset Evolution**: 60 → 319 → 339 driver-race combinations
- **Tracks**: Zandvoort (2024), All 2025 tracks so far
- **Update Frequency**: Weekly before each Grand Prix

### 🤖 Model Evolution

| Version | Race | Dataset Size | R² Score | MAE (seconds) | Key Improvements |
|---------|------|-------------|----------|---------------|------------------|
| **v3.0** | Baku 2025 | 339 samples | 0.925 | 2.182 | Linear Regression optimization, selective normalization |
| **v2.0** | Monza 2025 | 319 samples | 0.835 | 2.4 | Weather integration, expanded dataset, track encoding |
| **v1.0** | Zandvoort 2025 | 60 samples | 0.559 | 3.89 | Initial Ridge regression implementation |


## Feature Engineering
### Core Features

**Practice Pace Integration**: Best lap time across FP1/FP2/FP3 sessions
**Grid Performance**: Qualifying position and gap to pole position  
**Teammate Comparison**: Relative qualifying performance within teams  
**Track Characteristics**: Downforce levels based on Hamilton's 2022 telemetry analysis

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

**Weather Integration**: Air temperature, humidity, atmospheric pressure, precipitation detection  
**Track-Specific Features**: Downforce categorization (5-tier system from Very High DF to Very Low DF)

## Model Development
### Algorithm Selection Process

**Model Comparison Results (Baku 2025)**:
- **Linear Regression**: MAE = 2.182s, R² = 0.925
- **Ridge Regression (α=7.0)**: MAE = 3.223s, R² = 0.876

**Why Linear Regression Won**: With expanded dataset, regularization actually hurt performance, suggesting feature set is well-suited to linear approach without complexity penalties.

### Technical Improvements (v3.0)

**Downforce Classification**: Analyzed Hamilton's 2022 qualifying telemetry across 16 circuits, categorizing by maximum speeds (lower max speed = higher downforce requirements)

**Selective Normalization**: Applied Min-Max scaling only to continuous features while preserving categorical encodings for teams, drivers, and track characteristics

**Feature Engineering**: Driver-specific encoding to emphasize driver characteristics for certain track types

## Data Processing Pipeline

### Session Data Extraction
```
def get_best_race_pace(year, race):
    # Multi-session aggregation (FP1, FP2, FP3)
    # Track status filtering (green flag conditions only)
    # Personal best lap identification
    # Cross-session minimum selection
```
## Data Quality Controls

**Outlier Detection:** Removal of corrupted data and unrealistic lap times
**Missing Value Strategy:** Imputation for weather data and track-specific features
**Normalization Strategy:** Categorical columns preserved, continuous features Min-Max scaled

## Prediction Results

```
Driver    Team
VER       Red Bull Racing
RUS       Mercedes  
TSU       Red Bull Racing
NOR       McLaren
PIA       McLaren
LEC       Ferrari
LAW       Racing Bulls
HAM       Ferrari
ANT       Mercedes
HAD       Racing Bulls
```

## Technical Challenges & Solutions

### Track Categorization

Challenge: Capturing circuit-specific characteristics
Solution: Systematic downforce analysis using historical telemetry data

### Data Scarcity

Challenge: Limited sample size causing overfitting in complex models
Solution: Linear models with selective preprocessing 

### Multicollinearity Issues

Detection: Correlation matrix analysis (CleanAirPace vs WindSpeed: -0.987)
Resolution: Feature selection and removal of redundant variables

## Dependencies
```
# Core libraries
import fastf1
import pandas as pd
import numpy as np
import sklearn

# Specific modules
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, r2_score
```
## Usage
```
# Install dependencies
pip install fastf1 pandas scikit-learn requests matplotlib

# Run prediction pipeline
python baku_gp_prediction.ipynb
```
## Model Limitations

Sample Density: Still building historical depth for certain track types
Weather Dependency: Relies on forecast data for race day conditions
Driver Transfers: Limited historical data for drivers in new teams
Track Evolution: Circuit modifications and surface changes affect historical relevance

## Future Enhancements

Ensemble Methods: Model combination once sufficient data prevents overfitting
Tyre Strategy Integration: Compound selection and degradation modeling
Real-time Integration: Live telemetry incorporation during race weekends if possible
Feature Expansion: Pit stop prediction, safety car probability modeling

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