# Limitations and notes for Jira Cloud connector

The following are limitations or notes for the Jira Cloud connector:

- The `Contains` operator does not work with the `resourceName` field, which is of `String` data type.
- By default, if no explicit filter is applied, only issues from the past 30 days will be crawled. Users have the option to override
  this default filter by specifying a custom filter.
