

# Limitations and notes for the Sentry connector
<a name="sentry-connector-limitations"></a>

The following are limitations and notes for the Sentry connector:
+ Sentry is supported as a source only. Writing to Sentry is not supported.
+ The `organizations-issues` entity returns issues in every status, including resolved and ignored issues. To read only unresolved issues, filter on `query` with the value `is:unresolved`.
+ Job bookmarks are not supported.