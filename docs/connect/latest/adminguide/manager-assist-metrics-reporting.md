# Manager assist contacts in metrics and reporting

When you enable the manager assist feature in Connect Customer, the system creates chat contacts for each manager session. These contacts have the subType `connect:Assistant`.

**Key behavior:**

- Manager assist contacts are excluded from out-of-the-box historical and real-time reports by default.
- Manager assist contacts do appear in the Connect Customer analytics data lake and are accessible through the Connect Customer API.
- Manager assist contacts do not route to agents.
- Contact details for manager assist contacts are not surfaced in the Contact Search page.
  **Impact on custom reporting:**

If you have built custom reports, dashboards, or custom ingestion pipelines, you must filter on the `connect:Subtype` segment attribute to exclude manager assist contacts.

Without this filter:

- Chat metrics such as `contact_flow_time_ms` and `chat_customer_metrics_max_response_time_ms` might show unexpectedly high values.
- Any query against `contact_statistic_record` that filters on `initiationMethod = 'API'` or `channel = 'CHAT'` will return manager assist contacts alongside standard customer chat contacts.

###### Important

The `contact_statistic_record` table does not contain a `subType` field. To filter out manager assist contacts, you must JOIN to `contact_record` and filter on the segment attribute. For an example query, see [Sample query to exclude manager assist contacts](data-lake-contact-data.md#data-lake-contact-statistic-sample-queries "data-lake-contact-data.md#data-lake-contact-statistic-sample-queries").
