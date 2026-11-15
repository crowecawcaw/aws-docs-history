

# Limitations and notes for the LaunchDarkly connector
<a name="launchdarkly-connector-limitations"></a>

The following are limitations and notes for the LaunchDarkly connector:
+ LaunchDarkly is supported as a source only. Writing to LaunchDarkly is not supported.
+ The connector connects only to the commercial LaunchDarkly instance at `https://app.launchdarkly.com`. The federal and EU instances aren't supported.
+ Timestamp fields are returned as LONG values in Unix epoch milliseconds, except `flag_statuses.lastRequested`, which is returned as an ISO 8601 string.
+ Nested objects and arrays, such as `tags`, `variations`, and `_links`, are returned as serialized JSON strings.
+ The `flag_statuses` entity has no flag-key column. To identify the flag for a row, parse the last segment of its URL in `_links`.
+ The `tokens` entity requests tokens for all members. To return all members' tokens, the connection's access token must have the Admin role.
+ Job bookmarks are not supported.