

# Limitations and notes for the PagerDuty connector
<a name="pagerduty-connector-limitations"></a>

The following are limitations and notes for the PagerDuty connector:
+ PagerDuty is supported as a source only. Writing to PagerDuty is not supported.
+ Without a `created_at` filter, the `incidents` entity returns incidents from approximately the last month. A filtered time window can span at most six months.
+ Without an `execution_time` filter, the `audit_records` entity returns records from the last 24 hours. A filtered time window can span at most 31 days.
+ Without a `start` filter, the `oncalls` entity returns on-calls that are active at the current time. A filtered range returns on-call periods that overlap the range.
+ PagerDuty offset pagination returns at most 10,000 records per query.
+ Rows from `team_members` and `incident_notes` don't include the parent team or incident ID.
+ Job bookmarks are not supported.