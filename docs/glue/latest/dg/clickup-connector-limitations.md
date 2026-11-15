

# Limitations and notes for the ClickUp connector
<a name="clickup-connector-limitations"></a>

The following are limitations and notes for the ClickUp connector:
+ ClickUp is supported as a source only. Writing to ClickUp is not supported.
+ Without `start_date` and `end_date` filters, the `team-time_entries` entity returns only time entries from the last 30 days that the authenticated user created. To read other dates or users, use `start_date`, `end_date`, and `assignee` in `FILTER_PREDICATE`.
+ Job bookmarks are not supported.