

# Limitations and notes for the Apollo connector

The following are limitations and notes for the Apollo connector:
+ Apollo is supported as a source only. Writing to Apollo is not supported.
+ Job bookmarks are not supported.
+ Each read returns a single page of up to 100 records per entity. The connector does not paginate Apollo responses, so an entity with more than 100 records is not read in full.