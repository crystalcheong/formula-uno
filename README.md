# 🏎️ F1 Race Winner Predictor

A machine learning pipeline for predicting Formula 1 race outcomes using historical telemetry data, practice session performance, and meteorological conditions. Updated weekly with predictions for each Grand Prix.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastF1](https://img.shields.io/badge/FastF1-3.6+-red.svg)](https://docs.fastf1.dev)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org)
[![Accuracy](https://img.shields.io/badge/Race_Winner_Accuracy-75%25-forestgreen.svg)](https://github.com)

## 🏆 Latest Predictions

🛠️ 🚧 🏗️ UNDER CONSTRUCTION: US GP PREDICTION NOTEBOOK (Kindly ignore changes made to the notebook until 20 October 🏗️ 🚧 🛠️

## 📊 Season Performance Tracking

| Race | Predicted Winner | Actual Winner | P1 Accuracy | Podium Accuracy | Model R² |
|------|------------------|---------------|-------------|-----------------|----------|
| **Singapore** | RUS | **RUS** ✅ | ✅ **100%** | ✅ **66%**  | 0.908 |
| **Baku** | VER | **VER** ✅ | ✅ **100%** | ✅ **66%** | 0.925 |
| **Monza** | NOR | **VER** ❌ | ❌ **0%** | ✅ **66%** | 0.835 |
| **Zandvoort** | PIA | **PIA** ✅ | ✅ **100%** | ✅ **66%** | 0.559 |

### 🎯 Prediction Accuracy Summary
- **Race Winners**: 3/4 (75%)
- **Podium Finishers**: 9/12 (67%)
- **Average Position Error**: 2.1 positions

## 🏁 Race Results Analysis
### 🇸🇬 2025 Singapore Grand Prix ✅ COMPLETED

**Final Predictions**:
- 🥇 **P1**: George Russell (Mercedes) - 124.38s
- 🥈 **P2**: Oscar Piastri (McLaren) - 124.55s
- 🥉 **P3**: Max Verstappen (Red Bull) - 124.99s

| Position | **Predicted** | **Actual** | **Accuracy** |
|----------|---------------|------------|--------------|
| **P1** | **RUS** ✅ | **RUS** | ✅ **CORRECT** |
| **P2** | **PIA** ❌ | **VER** | ❌ Wrong |
| **P3** | **VER** ❌ | **NOR** | ❌ Wrong |

**Race Winner**: ✅ **PREDICTED CORRECTLY** - George Russell
**Notable**: Model correctly predicted the winner. Piastri was 4th in the actual race. 2/3 of the podium finishers were predicted correctly.

### 🇦🇿 2025 Azerbaijan Grand Prix - Baku ✅ COMPLETED

**Final Predictions**:
- 🥇 **P1**: Max Verstappen (Red Bull) - 154.67s
- 🥈 **P2**: George Russell (Mercedes) - 155.08s
- 🥉 **P3**: Kimi Antonelli (Mercedes) - 155.09s

| Position | **Predicted** | **Actual** | **Accuracy** |
|----------|---------------|------------|--------------|
| **P1** | **VER** ✅ | **VER** | ✅ **CORRECT** |
| **P2** | **RUS** ✅ | **RUS** | ✅ **CORRECT** |
| **P3** | **ANT** ❌ | **SAI** | ❌ Wrong |

**Race Winner**: ✅ **PREDICTED CORRECTLY** - Max Verstappen
**Notable**: Model correctly predicted top 2 finishers, showcasing strong performance on street circuits. Antonelli was behind Sainz by 2s at 4th place.

**Actual Final Results**:
1. **Max Verstappen** (Red Bull) - Winner
2. **George Russell** (Mercedes)
3. **Carlos Sainz** (Williams)
4. Kimi Antonelli (Mercedes)
5. Lando Norris (McLaren)

### 🇮🇹 2025 Italian Grand Prix - Monza ✅ COMPLETED

**Final Predictions**:
- 🥇 **P1**: Lando Norris (McLaren) - 89.971s 
- 🥈 **P2**: Oscar Piastri (McLaren) - 90.011s
- 🥉 **P3**: Charles Leclerc (Ferrari) - 90.173s

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
- 🥇 **P1**: Oscar Piastri (McLaren) - 87.29s
- 🥈 **P2**: Lando Norris (McLaren) - 87.68s
- 🥉 **P3**: Max Verstappen (Red Bull) - 89.13s

| Position | **Predicted** | **Actual** | **Accuracy** |
|----------|---------------|------------|--------------|
| **P1** | **PIA** ✅ | **PIA** | ✅ **CORRECT** |
| **P2** | **NOR** ❌ | **VER** | ❌ Wrong (DNF) |
| **P3** | **VER** ✅ | **HAD** | ❌ Wrong |

**Race Winner**: ✅ **PREDICTED CORRECTLY** - Oscar Piastri  
**Notable**: Norris retired from P2 with mechanical failure, promoting Hadjar to surprise maiden podium. Hadjar was P4 in my prediction.

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
- **Dataset Evolution**: 60 → 319 → 339 → 359 driver-race combinations
- **Tracks**: Singapore (2024), All 2025 tracks so far
- **Update Frequency**: On Sundays before each Grand Prix

### 🤖 Model Evolution

| Version | Race | Dataset Size | R² Score | MAE (seconds) | Key Improvements |
|---------|------|-------------|----------|---------------|------------------|
| **v4.0** | Singapore 2025 | 359 samples | 0.90 | 2.0 | Safety car feature engineering, position flexibility |
| **v3.0** | Baku 2025 | 339 samples | 0.925 | 2.182 | Linear Regression optimization, selective normalization |
| **v2.0** | Monza 2025 | 319 samples | 0.835 | 2.4 | Weather integration, expanded dataset, track encoding |
| **v1.0** | Zandvoort 2025 | 60 samples | 0.559 | 3.89 | Initial Ridge regression implementation |


## Feature Engineering
### Core Features

- **Practice Pace Integration**: Best lap time across FP1/FP2/FP3 sessions
- **Grid Performance**: Qualifying position and gap to pole position  
- **Teammate Comparison**: Relative qualifying performance within teams  
- **Track Characteristics**: Downforce levels based on Hamilton's 2022 telemetry analysis

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

- **Weather Integration**: Air temperature, humidity, atmospheric pressure, precipitation detection  
- **Track-Specific Features**: Downforce categorization (5-tier system from Very High DF to Very Low DF)

## Model Development
### Algorithm Selection Process

**Model Comparison Results (Baku 2025)**:
- **Linear Regression**: MAE = 2.102s, R² = 0.904
- **Ridge Regression (α=5.0)**: MAE = 2.074s, R² = 0.909


**Why Ridge Regression Won**: With expanded dataset, using XGBoost made manual feature weighing difficult, suggesting feature set is well-suited to linear approach without complexity penalties.

### Technical Improvements (v4.0)

- **Feature Engineering**: Added Position Flexibility factor by calculating average positions lost or gained over the last 5 races.

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

- **Outlier Detection:** Removal of corrupted data and unrealistic lap times
- **Missing Value Strategy:** Imputation for weather data and track-specific features
- **Normalization Strategy:** Categorical columns preserved, continuous features Min-Max scaled

## Complete Prediction Results (Singapore GP)

```
RUS         124.155429
PIA         124.329632
VER         124.766341
ANT         124.936092
NOR         125.086558
HAM         125.407224
LEC         125.766541
LAW         126.243674
HAD         126.561356
ALO         127.488472
BEA         127.602225
HUL         127.733188
SAI         127.964576
TSU         128.119668
ALB         128.406562
STR         128.519824
GAS         128.949070
BOR         129.189293
COL         129.203600
OCO         129.248415  
```

## Technical Challenges & Solutions

### Track Categorization

- Challenge: Capturing circuit-specific characteristics
- Solution: Systematic downforce analysis using historical telemetry data

### Data Scarcity

- Challenge: Limited sample size causing overfitting in complex models
- Solution: Linear models with selective preprocessing 

### Multicollinearity Issues

- Detection: Correlation matrix analysis (CleanAirPace vs WindSpeed: -0.987)
- Resolution: Feature selection and removal of redundant variables

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

- Sample Density: Still building historical depth for certain track types
- Weather Dependency: Relies on forecast data for race day conditions
- Driver Transfers: Limited historical data for drivers in new teams
- Track Evolution: Circuit modifications and surface changes affect historical relevance

## Future Enhancements

- Ensemble Methods: Model combination once sufficient data prevents overfitting
- Tyre Strategy Integration: Compound selection and degradation modeling
- Real-time Integration: Live telemetry incorporation during race weekends if possible
- Feature Expansion: Pit stop prediction, safety car probability modeling

## Repository Structure
```
f1-winner/
├── data/ # Contains all the dataframes used for training models for each race
│ 
├── prediction_notebooks/ # Notebooks with detailed code for prediction
│   ├── baku_prediction.ipynb
│   ├── dutch_gp_prediction.ipynb
│   ├── monza_prediction.ipynb
│   ├── singapore_prediction.ipynb
│   ...
│ 
├── scripts/
│   ├── pos_flexibility_calculation.py
│   └── categorise_by_downforce.py
│
├── venv/ # Environment folder
│
├──  README.md
└── requirements.txt
