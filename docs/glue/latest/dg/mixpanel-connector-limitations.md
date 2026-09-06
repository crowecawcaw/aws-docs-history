

# Limitations
<a name="mixpanel-connector-limitations"></a>

The following are limitations for the Mixpanel connector:
+ For `Segmentation Numeric` entity, the Mixpanel API throws a `400 (Bad Request)` error if no numeric data is found for the mandatory filters. We are treating this as an `OK` response to prevent flow failure.
+ The queryable field `limit` has been removed from the supported entities because:
  + It was causing errors due to being interpreted as the SDK's limit feature
  + The filter served no practical purpose
  + Equivalent functionality is now covered by the limit feature implementation
+ Field-based partitioning cannot be supported due to the absence of required operators (`>=`, `<=`, `<`, `>`, `between`) for partitioning from the SaaS platform. Although it supports the `between` operator, the fields for which it supports this operator are non-retrievable. Hence, the criteria for field-based partitioning are not satisfied.
+  As there is no provision to get an 'offset' value for entities that support pagination, it is not possible to support record-based partitioning for Mixpanel.
+ `Cohorts` entity only supports `CreatedDate/Time` field and there is no field to identify `UpdatedDate/Time` as a result `DML_Status` cannot be identified. Also, there is no endpoint to identify deleted records. Hence, CDC cannot be supported.
+  To run a AWS Glue job for the entities mentioned below, mandatory filters are required. Refer to the table below for entity names and their required filters.  
**Entity name and required filters**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/mixpanel-connector-limitations.html)