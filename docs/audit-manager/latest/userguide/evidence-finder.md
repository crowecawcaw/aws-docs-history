# Evidence finder

Evidence finder provides a powerful way to search for evidence in Audit Manager. Instead of browsing
deeply nested evidence folders to find what you're looking for, you can now use evidence finder to
quickly query your evidence. If you use evidence finder as a delegated administrator, you can
search for evidence across all member accounts in your organization.

Using a combination of filters and groupings, you can progressively narrow the scope of your
search query. For example, if you want a high-level view of your system health, perform a broad
search and filter by assessment, date range, and resource compliance. If your goal is to remediate
a specific resource, you can perform a narrow search to target evidence for a specific control or
resource ID. After you define your filters, you can group and then preview the matching search
results before creating an assessment report.

To use evidence finder, you must enable this feature from your Audit Manager settings.

## Key points

### Understanding how evidence finder works with CloudTrail Lake

Evidence finder uses [AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") querying and
storage capability. Before you start using evidence finder, it's helpful to understand a little
more about how CloudTrail Lake works.

CloudTrail Lake aggregates data into a single, searchable event data store that supports powerful
SQL queries. This means that you can search for data across your organization and within custom
time ranges. With evidence finder, you can use this search functionality directly in the Audit Manager
console.

When you request to enable evidence finder, Audit Manager creates an event data store on your behalf.
After evidence finder is enabled, all of your future Audit Manager evidence is ingested into the event
data store where it's available for evidence finder search queries. After you enable evidence
finder, we also backfill the newly created event data store with your past two years’ worth of
evidence data. If you enable evidence finder as a delegated administrator, we backfill the data
for all member accounts in your organization.

All of your evidence data, whether backfilled or new, is retained in the event data store
for 2 years. You can change the default retention period at any time. For instructions, see
[Update an event
data store](../../../awscloudtrail/latest/userguide/query-lake-cli.md#lake-cli-update-eds. "../../../awscloudtrail/latest/userguide/query-lake-cli.md#lake-cli-update-eds.") in the _AWS CloudTrail User Guide_. You can keep
data in an event data store for up to 7 years, or 2,555 days.

###### Note

When new evidence data is added to the event data store, CloudTrail Lake charges are incurred for
data storage and ingestion.

For CloudTrail Lake queries, you pay as you go. This means that for each search query that you
run in evidence finder, you're charged for the data that's scanned.

For more information about CloudTrail Lake pricing, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Next steps

To get started, enable evidence finder from your Audit Manager settings. For instructions, see [Enabling evidence finder](evidence-finder-settings-enable.md "evidence-finder-settings-enable.md").

## Additional resources

- [Searching for evidence in evidence finder](search-for-evidence-in-evidence-finder.md "search-for-evidence-in-evidence-finder.md")
- [Viewing results in evidence finder](viewing-search-results-in-evidence-finder.md "viewing-search-results-in-evidence-finder.md")
- [Filter and grouping options for evidence finder](evidence-finder-filters-and-groups.md "evidence-finder-filters-and-groups.md")
- [Example use cases for evidence finder](example-use-cases-for-evidence-finder.md "example-use-cases-for-evidence-finder.md")
- [Troubleshooting evidence finder issues](evidence-finder-issues.md "evidence-finder-issues.md")
