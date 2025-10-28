# Limitations and notes for Salesforce Marketing Cloud Account Engagement connector

The following notes and limitations apply:

- When both a limit and partitioning are applied, the limit takes precedence over the partitioning.
- As per the API Docs, `SalesforceMarketingCloudEngagement` enforced a RateLimit on daily and concurrent requests. For more information, see [Rate Limits](https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html?q=limitation#rate-limits "https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html?q=limitation#rate-limits").
- The Export API is subject to the daily Account Engagement API call limit and the concurrent Account Engagement API call limit for your account.
- Similar to a queue, Export/Async API calls are executed sequentially for each account. Older exports are processed before newer exports.
- Partition is not supported in Async mode.
- The number of selected fields specified in the Export/Async API calls can’t exceed 150.
- The **Prospect** entity supports over 150 fields, but only 150 fields can be selected at a time. If `Select All` is chosen, some fields will be excluded. To retrieve data for these excluded fields, you have to include them in the `Selected Fields` option.

The following is the list of excluded fields in `SELECT_ALL` - `updatedBy.firstName`, `updatedBy.lastName`, `updatedBy.jobTitle`, `updatedBy.roleName`, `updatedBy.salesforceId`, `updatedBy.createdAt`, `updatedBy.updatedAt`, `updatedBy.isDeleted`, `updatedBy.createdById`, `updatedBy.updatedById`, `updatedBy.tagReplacementLanguage`

- Collection fields can’t be exported for Async. For example, on List Email the `senderOptions` and `replyToOptions` fields are not supported.
- For all entities, filter is mandatory. If no filter is provided the default filter predicate is set to the `Created After` field with a value of the current date-time (adjusted to your time zone) minus one year.
- As per Salesforce Marketing Cloud Account Engagement limitations, in Async, the maximum range to fetch data is 1 year. If a query is provided for more than 1 year, the job will throw an error.
- Currently, there is a bug in Salesforce Pardot. When the job includes only a single field which does not have any data, the field value is not returning correct result and instead, the field name is being returned multiple times.
  The Salesforce Pardot team is aware of the issue and is actively working on a resolution.
