# Limitations and notes for Zoho CRM connector

The following are limitations or notes for the Zoho CRM connector:

- With API version v7, you can fetch a maximum of 100,000 records. See the [Zoho documentation](https://www.zoho.com/crm/developer/docs/api/v7/get-records.html "https://www.zoho.com/crm/developer/docs/api/v7/get-records.html") .
- For the Event entity, the label "Meeting" is displayed as mentioned in the [Zoho documentation](https://www.zoho.com/crm/developer/docs/api/v7/modules-api.html "https://www.zoho.com/crm/developer/docs/api/v7/modules-api.html").
- For Select All functionality:
  - You can fetch a maximum of 50 fields from SaaS for both the GET and POST call.
  - If you want to have data for some specific field that does not belong in the first 50 fields, you will need to manually provide the list of selected fields.
  - If more than 50 fields are selected, any fields beyond the 50 fields will be trimmed and will contain null data in Amazon S3.
  - In case of a filter expression, if the user-provided list of 50 fields does not include "id" and "Created_Time," a custom exception will be raised to prompt the user to include these fields.

- Filter operators may vary from field-to-field despite of having the same data type. Therefore, you must manually specify a different operator for any field that triggers an error in the SaaS platform.
- For Sort By functionality:
  - Data can only be sorted by a single field without a filter expression, whereas data can be sorted by multiple fields when a filter expression is applied.
  - If no sort order is specified for the selected field, the data will be retrieved in ascending order by default.

- The supported regions for the Zoho CRM connector are US, Europe, India, Australia and Japan.
- Async read functionality [Limitations:](https://www.zoho.com/crm/developer/docs/api/v7/bulk-read/limitations.html "https://www.zoho.com/crm/developer/docs/api/v7/bulk-read/limitations.html")
  - Limit order by and partitioning is not supported in the Async mode.
  - In the Async mode we can transfer data up to 500 pages with 200,000 records per page.
  - For a one-minute interval, only 10 requests are allowed for download. When you exceed the download limit, the system returns an HTTP 429 error and pauses all download requests for one minute before processing can resume.
  - After completing the bulk job, you can access the downloadable file only for a period of one day. After that, you cannot access the file via endpoints.
  - A maximum of 200 select fields can be given via an endpoint. If you specify more than 200 select fields in an endpoint, the system will automatically export all available fields for that module.
  - External fields created in any module are not supported in Bulk Read APIs.
  - Sorting and `Group_by` clauses are not supported via this API endpoint.
  - The values of the fields with sensitive health data will be retrieved only when the **Restrict Data access through API** option in the compliance settings is **disabled**. If the option is enabled, the value will be **empty** in the result.
  - Filtration/Criteria Limits
    - The maximum number of criteria that can be used in a query is 25.
    - Filtration/Criteria on multiline text fields is not supported.
