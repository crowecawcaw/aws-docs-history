

# Limitations and notes for the BugSnag connector

The following are limitations and notes for the BugSnag connector:
+ BugSnag is supported as a source only. Writing to BugSnag is not supported.
+ Job bookmarks are not supported.
+ Reading the `projects` entity requires an `organization_id`; reading the `errors` entity requires a `project_id`.