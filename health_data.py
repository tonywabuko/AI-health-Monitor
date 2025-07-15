import pandas as pd
import numpy as np


def simulate_data(n=100):
    data = {
        'timestamp': pd.date_range(start='2025-07-15', periods=n, freq='T'),
        'heart_rate': np.random.randint(60, 100, n),
        'blood_oxygen': np.random.randint(90, 100, n),
        'activity_level': np.random.choice(['low', 'moderate', 'high'], n)
    }
    return pd.DataFrame(data)
