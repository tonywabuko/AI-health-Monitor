from sklearn.ensemble import IsolationForest


def detect_anomalies(df):
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['heart_rate', 'blood_oxygen']])
    df['anomaly'] = df['anomaly'].apply(
        lambda x: 'Anomaly' if x == -1 else 'Normal')
    return df
