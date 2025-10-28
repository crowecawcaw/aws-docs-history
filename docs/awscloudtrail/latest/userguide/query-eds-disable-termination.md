# Manage event data store

lifecycles

The following are the lifecycle stages of an event data store:

- `CREATED` – A short-term state indicating that the event
  data store has been created.
- `ENABLED` – The event data store is active and ingesting
  events. You can run queries and copy trail events to the event data
  store.
- `STARTING_INGESTION` – A short-term state indicating
  that the event data store will start ingesting live events.
- `STOPPING_INGESTION` – A short-term state indicating
  that the event data store will stop ingesting live events.
- `STOPPED_INGESTION` – The event data store is not
  ingesting live events. You can still run queries on any events already in
  the event data store and copy trail events to the event data store.
- `PENDING_DELETION` – The event data store was in an
  `ENABLED` or `STOPPED_INGESTION` state and has
  been deleted but is within the 7-day wait period before permanent deletion.
  You cannot run queries on the event data store, and no operations can be
  performed on the event data store except restoration.
  You can only delete an event data store if both federation and termination
  protection are disabled. _Termination protection_
  prevents an event data store from getting accidentally deleted. By default,
  termination protection is enabled on an event data store. [Federation](query-federation.md "query-federation.md") lets you query your event data
  store data in Athena and is disabled by default.

After you delete an event data store, it remains in the
`PENDING_DELETION` state for 7 days before it is permanently deleted.
You can restore an event data store during the 7-day wait period. While in the
`PENDING_DELETION` state, an event data store is not available for
queries, and no other operations can be performed on the event data store except
restore operations. An event data store that is pending deletion does not ingest
events and does not incur costs. However, event data stores that are pending
deletion count toward the quota of event data stores that can exist in one
AWS Region.

**Actions available on event data stores**

To [delete](query-event-data-store-delete.md "query-event-data-store-delete.md") or [restore](query-eds-restore.md "query-eds-restore.md") an event data store, [copy trail
events](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md"), start or stop ingesting events, or turn on or turn off an event data store's
termination protection, use commands on the **Actions** menu of the
event data store's details page.

![Event data store Actions menu.](images/query-eds-actions.png)
The option to **Copy trail events** is only available on event
data stores that contain CloudTrail events. The options to
**Start ingestion** and **Stop ingestion** are
only available on event data stores containing either CloudTrail events (management and
data events), or AWS Config configuration items.
