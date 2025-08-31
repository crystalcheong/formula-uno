# F1 Podium Prediction Model - 2025 Dutch Grand Prix
## Project Overview
A machine learning pipeline for predicting Formula 1 race outcomes using historical telemetry data, practice session performance, and meteorological conditions. The model successfully predicted the podium positions for the 2025 Dutch Grand Prix using supervised learning techniques.

**Final Predictions**:

🥇 **P1**: Oscar Piastri (McLaren) - 87.29s
🥈 **P2**: Lando Norris (McLaren) - 87.68s
🥉 **P3**: Max Verstappen (Red Bull) - 89.13s

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
f1-podium-prediction/
├── data/
│   ├── raw/          # FastF1 cached data
│   └── processed/    # Engineered features
├── models/
│   └── ridge_model.pkl
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
```