from backend import ingest_data, fetch_data, detect_spikes, detect_anomalies

raw = ingest_data()
fetched = fetch_data(raw)
spikes = detect_spikes(fetched)
anomalies = detect_anomalies(spikes)

print("Pipeline completed:", anomalies)
