import fastf1
import numpy as np
import logging

def calculate_driver_flexibility(year, race_rounds):
    """
    Calculate average position change for drivers over specified races.
    
    Args:
        year (int): Season year
        race_rounds (list): Race round numbers
        
    Returns:
        dict: {driver_abbr: avg_flexibility_score}
    """
    logging.getLogger('fastf1').setLevel(logging.WARNING)
    fastf1.Cache.enable_cache('cache')

    drivers=["PIA","NOR","VER","TSU","HAD","LAW","ALO","STR","OCO","BEA","RUS","ANT","GAS","COL","HAM","LEC","ALB","SAI","BOR","HUL"]
    flex_map=dict.fromkeys(drivers, 0) 
    for race_round in race_rounds:
        try: 
            cur_session=fastf1.get_session(year,race_round,'R')
            cur_session.load()
            cur_results=cur_session.results
            print(f"Processing race round {race_round}...")

            for driver in drivers:
                driver_row = cur_results[cur_results['Abbreviation'] == driver]
                if driver_row.empty:
                    continue 
                start_pos=driver_row['GridPosition'].values[0]
                if np.isnan(start_pos):
                    start_pos = 20
                else:
                    start_pos = int(start_pos)
                finish_pos=driver_row['ClassifiedPosition'].values[0]
                if finish_pos in ['R','D','E','W','F','N']:
                    finish_pos = 20
                else:
                    finish_pos=int(finish_pos)
                flex_map[driver]=flex_map[driver]+finish_pos-start_pos
        except Exception as e:
            print(f"Error loading race {race_round}: {e}")
            continue
            
    result = {key: value / len(race_rounds) for key, value in flex_map.items()}
        
    return result

if __name__ == "__main__":
    flexibility = calculate_driver_flexibility(2025, ['Singapore','Baku', 'Monza', 'Zandvoort', 'Hungary'])
    print("================================FINAL RESULTS FOR DRIVER POSITION FLEXIBILITY================================\n",flexibility)
    