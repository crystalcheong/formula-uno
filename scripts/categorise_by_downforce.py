import fastf1
import pandas as pd
import numpy as np
import logging

# Reduce FastF1 verbosity
logging.getLogger('fastf1').setLevel(logging.WARNING)
fastf1.Cache.enable_cache('cache')

# 2022 F1 Calendar round numbers (Hamilton's championship runner-up year)
tracks_with_rounds = {
    'Bahrain': 1,
    'Saudi Arabia': 2, 
    'Australia': 3,
    'Imola': 4,  # Emilia Romagna GP was round 4 in 2022
    'Miami': 5,
    'Spain': 6,  # Spanish GP
    'Monaco': 7,
    'Azerbaijan': 8,  # Baku 
    'Canada': 9,
    'Silverstone': 10,  # British GP
    'Austria': 11,
    'Hungary': 13,
    'Belgium': 14,
    'Netherlands': 15,
    'Monza': 16,  # Italian GP
    'Singapore': 17,  
    'Japan': 18,
    'United States':19
}

# Keep only the tracks you want to analyze
wanted_tracks = {
    'Australia': 3,
    'Imola': 4,  # This was round 4 in 2022
    'Bahrain': 1, 
    'Saudi Arabia': 2,
    'Azerbaijan': 8,  # Baku (round 8 in 2022, not 4)
    'Miami': 5,
    'Monaco': 7,
    'Spain': 6,  
    'Canada': 9,
    'Austria': 11,
    'Silverstone': 10,
    'Hungary': 13,
    'Belgium': 14,
    'Netherlands': 15,
    'Monza': 16,
    'Singapore': 17,  
    'Japan': 18,
    'United States':19
}

tracks_with_rounds = wanted_tracks

def get_track_characteristics(session, driver='HAM'):
    """
    Get multiple track characteristics for downforce analysis.
    
    Returns dict with:
    - max_speed: Top speed (lower DF = higher speed)
    - speed_range: Speed difference (higher DF = bigger range) 
    - avg_speed: Overall average speed
    - full_throttle_pct: % of lap at full throttle
    """
    try:
        laps = session.laps.pick_drivers(driver)
        if laps.empty:
            return None
            
        fastest_lap = laps.pick_fastest()
        if fastest_lap.empty:
            return None
            
        telemetry = fastest_lap.get_car_data()
        if telemetry.empty:
            return None
            
        # Calculate characteristics
        max_speed = telemetry['Speed'].max()
        min_speed = telemetry['Speed'].min()
        speed_range = max_speed - min_speed
        avg_speed = telemetry['Speed'].mean()
        
        # Full throttle percentage
        full_throttle_pct = (telemetry['Throttle'] > 95).sum() / len(telemetry) * 100
        
        return {
            'max_speed': max_speed,
            'speed_range': speed_range, 
            'avg_speed': avg_speed,
            'full_throttle_pct': full_throttle_pct,
            'min_speed': min_speed
        }
        
    except Exception as e:
        print(f"Error processing {driver}: {e}")
        return None

def analyze_downforce_simple():
    """Simple downforce analysis using Hamilton's 2022 top speeds."""
    
    results = []
    year = 2022  # Only use 2022
    
    for track_name, round_num in tracks_with_rounds.items():
        print(f"Processing {track_name} (Round {round_num})...")
        
        try:
            # Use qualifying session for max speeds
            session = fastf1.get_session(year, round_num, 'Q')
            session.load(telemetry=True, weather=False, messages=False)
            
            # Only get Hamilton's data
            characteristics = get_track_characteristics(session, 'HAM')
            
            if characteristics:
                results.append({
                    'Track': track_name,
                    **characteristics
                })
                print(f"✓ {track_name}: {characteristics['max_speed']:.1f} km/h max")
            else:
                print(f"✗ {track_name}: No Hamilton data")
                
        except Exception as e:
            print(f"✗ {track_name}: {e}")
    
    return pd.DataFrame(results)

def analyze_downforce_robust():
    """More robust analysis using multiple sessions/years."""
    
    results = []
    years_rounds = {
        2022: tracks_with_rounds,  # Same rounds generally
        2023: tracks_with_rounds
    }
    sessions = ['Q', 'FP2', 'FP3']
    
    for track_name, round_num in tracks_with_rounds.items():
        print(f"Processing {track_name} (Round {round_num})...")
        
        all_characteristics = []
        
        for year, track_dict in years_rounds.items():
            if track_name in track_dict:
                round_number = track_dict[track_name]
                for session_type in sessions:
                    try:
                        session = fastf1.get_session(year, round_number, session_type)
                        session.load(telemetry=True, weather=False, messages=False)
                        
                        chars = get_track_characteristics(session, 'HAM')
                        if chars:
                            all_characteristics.append(chars)
                            
                    except Exception:
                        continue
        
        if all_characteristics:
            # Average across all sessions
            avg_chars = {
                'Track': track_name,
                'max_speed': np.mean([c['max_speed'] for c in all_characteristics]),
                'speed_range': np.mean([c['speed_range'] for c in all_characteristics]),
                'avg_speed': np.mean([c['avg_speed'] for c in all_characteristics]),
                'full_throttle_pct': np.mean([c['full_throttle_pct'] for c in all_characteristics]),
                'sample_size': len(all_characteristics)
            }
            results.append(avg_chars)
            print(f"✓ {track_name}: {avg_chars['max_speed']:.1f} km/h (n={len(all_characteristics)})")
        else:
            print(f"✗ {track_name}: No data")
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    print("=== DOWNFORCE ANALYSIS USING HAMILTON'S 2022 TOP SPEEDS ===")
    print("Lower max speed = Higher downforce required")
    print()
    
    # Simple analysis only - Hamilton 2022
    print("Analyzing Hamilton's qualifying speeds from 2022...")
    df = analyze_downforce_simple()
    
    if not df.empty:
        # Sort by max speed (lowest = highest downforce)
        df = df.sort_values('max_speed', ascending=True)
        
        print("\n" + "="*60)
        print("TRACK CHARACTERISTICS")
        print("="*60)
        print(df[['Track', 'max_speed', 'avg_speed', 'speed_range', 'full_throttle_pct']].to_string(index=False, float_format='%.1f'))
        
        # Create downforce categories based on max speed
        # Lower speed = higher downforce
        df['downforce_category'] = pd.cut(
            df['max_speed'],
            bins=5,
            labels=['Very High DF', 'High DF', 'Medium DF', 'Low DF', 'Very Low DF']
        )
        
        print("\n" + "="*60) 
        print("DOWNFORCE CATEGORIES (Based on Max Speed)")
        print("="*60)
        
        for category in ['Very High DF', 'High DF', 'Medium DF', 'Low DF', 'Very Low DF']:
            tracks_in_cat = df[df['downforce_category'] == category]
            if not tracks_in_cat.empty:
                track_names = tracks_in_cat['Track'].tolist()
                avg_speed = tracks_in_cat['max_speed'].mean()
                print(f"{category:13}: {', '.join(track_names)} (avg: {avg_speed:.1f} km/h)")
        
        # Create mapping for your dataframe
        print("\n" + "="*60)
        print("MAPPING FOR TRAINING DATA")
        print("="*60)
        
        # Map back to your original track names (most are already correct)
        track_name_mapping = {
            'Azerbaijan': 'Baku',
            'Spain': 'Spain',  # You might want 'Barcelona' 
            'Silverstone': 'Silverstone',  # You might want 'Britain'
            'Belgium': 'Belgium',  # You might want 'Spa'
            'Netherlands': 'Netherlands',  # You might want 'Zandvoort'
            'Monza': 'Monza'  # You might want 'Italy'
            # Add others if needed
        }
        
        # Create final mapping
        final_mapping = {}
        for _, row in df.iterrows():
            original_name = track_name_mapping.get(row['Track'], row['Track'])
            final_mapping[original_name] = row['downforce_category']
        
        print("track_downforce_mapping = {")
        for track, category in final_mapping.items():
            print(f"    '{track}': '{category}',")
        print("}")
        
        # Numerical mapping
        numeric_mapping = {
            'Very High DF': 5,
            'High DF': 4,
            'Medium DF': 3, 
            'Low DF': 2,
            'Very Low DF': 1
        }
        
        print("\nNumerical mapping:")
        print("downforce_numeric_mapping = {")
        for track, category in final_mapping.items():
            numeric = numeric_mapping[category]
            print(f"    '{track}': {numeric},")
        print("}")
        
        # Save results
        df.to_csv('downforce_analysis_simple.csv', index=False)
        print(f"\nResults saved to 'downforce_analysis_simple.csv'")
        
        print("\n" + "="*60)
        print("INTERPRETATION:")
        print("• Very High DF: Slow, twisty tracks (Monaco, Hungary)")
        print("• Very Low DF: Fast tracks with long straights (Monza, Spa)")
        print("• Max speed is the most reliable indicator available in FastF1")
        print("="*60)
        
    else:
        print("Fzzzt.....Error........Check.....Internet.....Eurgh")