# Limitations

The following are limitations for the Microsoft Dynamics 365 CRM connector:

- In Microsoft Dynamics 365 CRM, record based partitioning is not supported as it does not support an offset parameter, and thus record based partitioning cannot be supported.
- Pagination is set at a maximum of 500 records per page to avoid Internal Server exceptions from SaaS due to a combination of data size and rate limitations.
  - [SaaS documentation on pagination](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query/page-results?view=dataverse-latest "https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query/page-results?view=dataverse-latest")
  - [SaaS documentation on rate limits](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits?tabs=sdk "https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits?tabs=sdk")

- Microsoft Dynamics 365 CRM supports `order by` on only parent fields for all entities. `order by` is not supported on sub-fields.
  - Both ASC and DESC directions are supported.
  - `order by` on multiple fields is supported.

- Filtering on "createddatetime" field of the `aadusers` standard entity is throwing a bad request error from SaaS even though it supports filtration. There is no specific identification of any other entity having a similar issue due to the dynamic nature of the metadata and neither is the root cause known. Hence, it cannot be handled.
- Complex object types, such as Struct, List, and Map do not support filtration.
- Many fields that can be retrieved from a response have `isRetrievable` marked as `false` in dynamic metadata response. In order to avoid data loss, `isRetrievable` is set to `true` for all fields.
- Field based partitioning will be supported on all entities when it adheres to the following criteria:
  - DateTime queryable fields should be present in standard entities or `createdon` and `modifiedon` fields (system-generated) in custom entities.
  - There is no exclusive identification of system generated fields or the nullable property from any SaaS metadata APIs, however it is a general practice that only the fields available by default, are filterable and non-nullable. Therefore, the above criterion of field selection is considered null safe and if it is filterable, it will be eligible for partitioning.
