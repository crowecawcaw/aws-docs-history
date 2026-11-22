

# Limitations and notes for the Grafana connector

The following are limitations and notes for the Grafana connector:
+ Grafana is supported as a source only. Writing to Grafana is not supported.
+ The connector reads one page from Grafana endpoints that it can't paginate, so it doesn't read records beyond these limits. The `dashboards` entity returns up to 5,000 records. The `datasources` entity returns up to the Grafana data source limit, which is 5,000 by default. The `annotations`, `dashboard-snapshots`, `folders`, `org-users`, `playlists`, and `teams-search` entities return up to 1,000 records. Team discovery for `team-members` also reads only the first 1,000 teams.
+ The `access-control-roles` entity uses the Grafana role-based access control API, which is available only in Grafana Cloud and Grafana Enterprise.
+ Job bookmarks are not supported.