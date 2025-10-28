# Limitations and notes for ServiceNow connector

The following are limitations or notes for the ServiceNow connector:

- As per [SaaS documentation](https://www.servicenow.com/docs/bundle/washingtondc-application-development/page/build/applications/reference/r_GlobalDefaultFields.html "https://www.servicenow.com/docs/bundle/washingtondc-application-development/page/build/applications/reference/r_GlobalDefaultFields.html"), `sys_created_on`, `sys_updated_on`, and `sys_mod_count` are system generated fields. The connector relies on SaaS APIs to provide these fields in the response body.
  - If SaaS doesn't generate these fields for any entity, filter based partitioning cannot be supported.

- If SaaS APIs don't return `sys_created_on` and `sys_updated_on` fields in the response, `DML_STATUS` cannot be calculated.
- Enhance read performance and efficiency
  - The ServiceNow connector now automatically sorts the records in ascending order by the `sys_id` field (must be present in metadata) when no ORDER BY clause is specified by the user. In this case, records will be paginated by the new optimized keyset based pagination.
  - If the ORDER BY clause is specified, the new optimization will not be used and the records will be fetched using the existing (user defined Order By and Offset-Limit based pagination) method.
