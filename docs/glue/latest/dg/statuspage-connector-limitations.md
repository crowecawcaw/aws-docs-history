

# Limitations and notes for the Statuspage connector

The following are limitations and notes for the Statuspage connector:
+ Statuspage is supported as a source only. Writing to Statuspage is not supported.
+ The `component-groups`, `components`, `incident-templates`, `incidents`, and `metrics` entities return only the first page of results from Statuspage, up to 100 records for each status page. The connector doesn't read records beyond the first 100. The `pages` and `metrics-providers` entities return all records.
+ Job bookmarks are not supported.