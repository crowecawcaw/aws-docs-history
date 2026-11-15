

# Connecting to Workday Live Data Query
<a name="connecting-to-data-workday"></a>

Workday is a cloud application suite for human capital management (HCM), financial management, and planning. Workday Live Data Query is a feature of Workday Data Cloud. With it, you can run SQL queries against the current data in your Workday tenant, without copying or moving that data. For more information, see [Get Started with Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html) in the Workday documentation. With AWS Glue, you can connect to Workday Live Data Query. Then, you can run real-time SQL against your Workday datasets.

Workday Live Data Query returns the most current data in your Workday tenant. If you want to run large historical queries on Apache Iceberg tables that Workday maintains in Workday Data Cloud, and data that Workday refreshes on a schedule is acceptable, use Workday Data Connect instead. For more information, see [Federate to Workday Data Connect](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation-workday.html) in the AWS Lake Formation Developer Guide.

You can also use a Workday Live Data Query federated catalog to query Workday data from Amazon Athena. For more information, see [Amazon Athena Workday Live Data Query connector](https://docs.aws.amazon.com/athena/latest/ug/connectors-workday-ldq.html) in the Amazon Athena User Guide.

**Topics**
+ [AWS Glue support for Workday Live Data Query](workday-ldq-support.md)
+ [Policies containing the API operations for creating and using connections](workday-ldq-configuring-iam-permissions.md)
+ [Configuring Workday Live Data Query](workday-ldq-configuring.md)
+ [Configuring Workday Live Data Query connections](workday-ldq-configuring-connections.md)
+ [Limitations for the Workday Live Data Query connector](workday-ldq-connector-limitations.md)