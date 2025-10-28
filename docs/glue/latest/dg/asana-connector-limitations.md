# Limitations

The following are limitations for the Asana connector:

- Service Accounts in Enterprise Domains can only access audit log API endpoints. Authentication
  with a Service Account's personal access token is required to access these
  endpoints.
- The Goal entity can only be accessed for user accounts with Premium plan or
  above.
- `Audit Log Event Entity` – In the connector,
  `start_at` and `end_at` fields are combined into a
  single field "start_end_at" to support filtering and incremental
  transfer.
- Partitioning cannot be supported for the `Date` field, even though it supports
  greater-than-or-equal-to and less-than-or-equal-to operators. Scenario: Created
  a job with `partitionField` as `due_on` (datatype: date),
  `lowerBound` as `2019-09-14`, `upperBound`
  as `2019-09-16`, and `numPartition` as `2`. The
  filter part of the endpoint URL is created as follows:
  - partition1:
    due_on.before=2019-09-14&due_on.after=2019-09-14
  - partition2: due_on.before=2019-09-15&due_on.after=2019-09-15
    Output:
  - In partition1, we get data with due_date as 2019-09-14 and
    2019-09-15
  - In partition2, we get the same data with due_date as 2019-09-15 (which
    was in partition1) along with other data, causing data
    duplication.

- Filtering and partitioning cannot be supported on the same field as a bad request error is
  thrown from the SaaS end.
- The Task entity requires a minimum of 1 field in filter criteria. There is a limitation
  with Asana where pagination is not identified without sorting the records based
  on a time-based field. Hence, the Created_at field is used along with pagination
  to distinguish the next set of records. The Created_at field is marked as
  mandatory in the filter, with a default value of 2000-01-01T00:00:00Z if not
  provided. For more information about Pagination, see [Tasks
  in a workspace](https://developers.asana.com/reference/searchtasksforworkspace "https://developers.asana.com/reference/searchtasksforworkspace").
