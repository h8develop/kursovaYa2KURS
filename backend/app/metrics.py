from prometheus_client import Counter, Histogram

ads_created_counter = Counter(
    'ads_created_total', 
    'Total number of ads created'
)

ad_creation_latency = Histogram(
    'ad_creation_latency_seconds', 
    'Latency for creating an ad'
)
