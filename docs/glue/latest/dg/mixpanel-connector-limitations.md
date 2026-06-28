# Limitations

The following are limitations for the Mixpanel connector:

- For `Segmentation Numeric` entity, the Mixpanel API throws a `400 (Bad
 Request)` error if no numeric data is found for the mandatory filters.
  We are treating this as an `OK` response to prevent flow
  failure.
- The queryable field `limit` has been removed from the supported entities
  because:

  - It was causing errors due to being interpreted as the SDK's limit
    feature
  - The filter served no practical purpose
  - Equivalent functionality is now covered by the limit feature
    implementation

- Field-based partitioning cannot be supported due to the absence of required operators
  (`>=`, `<=`, `<`, `>`,
  `between`) for partitioning from the SaaS platform. Although it
  supports the `between` operator, the fields for which it supports
  this operator are non-retrievable. Hence, the criteria for field-based
  partitioning are not satisfied.
- As there is no provision to get an 'offset' value for entities that support pagination,
  it is not possible to support record-based partitioning for Mixpanel.
- `Cohorts` entity only supports `CreatedDate/Time` field
  and there is no field to identify `UpdatedDate/Time` as a result
  `DML_Status` cannot be identified. Also, there is no endpoint to
  identify deleted records. Hence, CDC cannot be supported.
- To run a AWS Glue job for the entities mentioned below, mandatory filters are required. Refer
  to the table below for entity names and their required filters.

Entity name and required filters| Entity name | Mandatory Filters |
| --- | --- |
| Annotations | from\_date, to\_date |
| Cohorts | None |
| Engage | None |
| Event | event, type, unit, from\_date, to\_date,<br>on |
| Events Name | type |
| Events Properties | event, name, type, unit, from\_date,<br>to\_date |
| Events Properties Top | event |
| Events Properties Values | event, name |
| Events Top | type |
| Funnels | funnel\_id, from\_date, to\_date |
| Profile Event Activity | distinct\_ids, from\_date, to\_date |
| Retention | from\_date, to\_date, unit,<br>addiction\_unit |
| Segmentation | event, from\_date, to\_date |
| Segmentation Average | event, from\_date, to\_date, on |
| Segmentation Numeric | event, from\_date, to\_date, on |
| Segmentation Sum | event, from\_date, to\_date, on |
