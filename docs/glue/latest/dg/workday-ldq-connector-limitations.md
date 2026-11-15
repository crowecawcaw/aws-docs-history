

# Limitations for the Workday Live Data Query connector
<a name="workday-ldq-connector-limitations"></a>

The following are limitations or notes for the Workday Live Data Query connector:
+ The connector is read-only. You can't use Workday Live Data Query as a target in AWS Glue ETL jobs.
+ When you read from Workday, provide the fully qualified entity name in the format `catalog.schema.table`, for example `workday_core.public.procurement_supplier`.
+ Field-based partitioning isn't supported. You can't use any Workday fields as a partition field.
+ The connector supports only Integration System User (ISU) authentication, which uses the OAuth 2.0 JWT bearer grant type. Workday User As Self (UAS) authentication isn't supported.
+ The data that you can read depends on the domain permissions granted to the ISU's security group in your Workday tenant. Tables and fields that the ISU can't access aren't returned. If you change the ISU's security permissions, Workday can take up to 15 minutes to apply the change.
+ The Workday tables and fields available through Live Data Query are a curated set that Workday maintains. For the current list, see [Data Cloud Catalog](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/data-cloud-catalog.html?toc=2.0) in the Workday documentation.
+ Workday applies its own guardrails to Live Data Query, such as limits on query run time, concurrent queries per tenant, and memory per query. These guardrails apply to queries from AWS Glue. For current limits, see [Get Started with Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html?toc=2.1.0) in the Workday documentation.
+ Queries run against the current data in your Workday tenant. For large historical reads where scheduled-refresh data is acceptable, consider Workday Data Connect instead. For more information, see [Federate to Workday Data Connect](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation-workday.html) in the AWS Lake Formation Developer Guide.