

# Limitations and notes for the Amplitude connector

The following are limitations and notes for the Amplitude connector:
+ Amplitude is supported as a source only. Writing to Amplitude is not supported.
+ Job bookmarks are not supported.
+ Amplitude enforces API rate limits: the Dashboard REST and cohort-download endpoints share a concurrency limit of 5, and the taxonomy endpoints use a cost-per-query budget. Large parallel Spark reads can receive HTTP 429 responses.
+ Reading the `cohorts` entity requires the Behavioral Cohorts add-on. Without it, the endpoint returns an error; the other entities are unaffected.
+ For EU data residency, set the connection URL to the EU host (`https://analytics.eu.amplitude.com`) when you create the connection.
+ The `events-list` entity reflects the current week's ingested-event totals, not a durable historical fact table.
+ The connector issues a single request per read and does not paginate Amplitude responses.