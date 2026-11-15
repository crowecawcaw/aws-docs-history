

# Limitations and notes for the FireHydrant connector
<a name="firehydrant-connector-limitations"></a>

The following are limitations and notes for the FireHydrant connector:
+ FireHydrant is supported as a source only. Writing to FireHydrant is not supported.
+ Job bookmarks are not supported.
+ Each entity read returns at most the first 200 records. For the nested `incident_events`, `incident_milestones`, and `incident_role_assignments` entities, parent discovery also considers at most the first 200 incidents.
+ FireHydrant evaluates incident timestamp filter bounds at whole-second granularity.
+ The `incident_events` entity includes its parent `incident_id`. Reads of `incident_milestones` and `incident_role_assignments` return entity records without incident context.