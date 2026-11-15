

# Limitations and notes for the Todoist connector
<a name="todoist-connector-limitations"></a>

The following are limitations and notes for the Todoist connector:
+ Todoist is supported as a source only. Writing to Todoist is not supported.
+ The `tasks` entity returns active tasks only. Completed tasks aren't included.
+ The `comments` entity returns task comments. Project comments aren't included.
+ The `activities` entity has no primary key column because Todoist activity IDs exceed the connector's supported numeric range. You can use `object_id`, `event_type`, and `event_date` as a best-effort downstream deduplication key, but Todoist doesn't guarantee that this combination is unique.
+ The `workspace_invitations` entity returns pending invitations only.
+ Job bookmarks are not supported.