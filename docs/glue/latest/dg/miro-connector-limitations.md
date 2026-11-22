

# Limitations and notes for the Miro connector

The following are limitations and notes for the Miro connector:
+ Miro is supported as a source only. Writing to Miro is not supported.
+ The connector returns only the boards that the Miro user who authorized the connection can access.
+ When you filter on `query`, Miro returns at most the first 10,000 matching boards. To read more boards, filter on `team_id`, `project_id`, or `owner_id` instead.
+ Job bookmarks are not supported.