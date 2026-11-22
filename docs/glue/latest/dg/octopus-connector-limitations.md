

# Limitations and notes for the Octopus Deploy connector

The following are limitations and notes for the Octopus Deploy connector:
+ Octopus Deploy is supported as a source only. Writing to Octopus Deploy is not supported.
+ The `tasks` entity returns the tasks for one space. System tasks that don't belong to a space aren't returned.
+ Job bookmarks are not supported.