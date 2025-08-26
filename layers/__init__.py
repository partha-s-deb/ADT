<<<<<<< HEAD
from backend import ingest_data, fetch_data, detect_spikes, detect_anomalies

raw = ingest_data()
fetched = fetch_data(raw)
spikes = detect_spikes(fetched)
anomalies = detect_anomalies(spikes)

print("Pipeline completed:", anomalies)
=======
from backend import ingest_data, fetch_data, detect_spikes, detect_anomalies

raw = ingest_data()
fetched = fetch_data(raw)
spikes = detect_spikes(fetched)
anomalies = detect_anomalies(spikes)

print("Pipeline completed:", anomalies)
>>>>>>> a347705c8c5f28079f1bf70e4843e6bdb254a997
