# Connect to a prebuilt data source with a wizard

This topic provides instructions for using the wizard to connect CloudWatch to the following data sources.

- Amazon OpenSearch Service
- Amazon Managed Service for Prometheus
- Amazon RDS for MySQL
- Amazon RDS for PostgreSQL
- Amazon S3 CSV files
- Microsoft Azure Monitor
- Prometheus

The subsections in this topic include notes about managing and querying with each of these data sources.

###### To create a connector to a data source

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Metrics data sources** tab.
4. Choose **Create data source**.
5. Select the source that you want, then choose **Next**.
6. Enter a name for the data source.
7. Enter the other required information, depending on the data source that you chose. This can
   include credentials to access the data source and data source identifying information such
   as Prometheus workspace name, database name, or Amazon S3 bucket name. For AWS services, the
   wizard discovers the resources and populates them into the selection dropdown.

For more notes about the data source you are using, see the sections after this procedure. 8. To have CloudWatch connect to the data source in a VPC, choose **Use a VPC**
and select the VPC to use. Then select the subnet and security group. 9. Choose **I acknowledge that AWS CloudFormation will create IAM resources**. This resource is the Lambda function
execution role. 10. Choose **Create data source**.

The new source that you just added doesn't
appear until the AWS CloudFormation stack is done creating it. To check progress, you can choose
**View the status of my CloudFormation stack**. Or you can choose the
refresh icon to update this list.

When your new data source appears in this list, it is ready to use. You can choose **Query from
CloudWatch metrics** to begin querying with it. For more information, see
[Creating a graph of metrics from
another data source](graph_a_metric.md#create-metric-graph-multidatasource "graph_a_metric.md#create-metric-graph-multidatasource").

##

Amazon Managed Service for Prometheus

**Updating the data source configuration**

- You can update your data source
  manually by doing the following:
  - To update the Amazon Managed Service for Prometheus workspace ID, update the
    `AMAZON_PROMETHEUS_WORKSPACE_ID` environment variable for the data source connector Lambda function.
  - To update the VPC configuration, see [Configuring VPC access (console)](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring") for more information.

**Querying the data source**

- When querying Amazon Managed Service for Prometheus, after you select the data source in the **Multi source query** tab
  and select an Amazon Managed Service for Prometheus connector,
  you can use the **Query helper** to discover metrics and labels and provide simple PromQL queries.
  You can also use the PromQL query editor to build a PromQL query.
- Multi-line queries are not supported by the CloudWatch data source connectors. Every line feed is
  replaced with a space when the query is executed, or when you create an alarm or a
  dashboard widget with the query. In some cases, this might make your query not valid.
  For example, if your query contains a single line comment it will not be valid. If you
  try to create a dashboard or alarm with a multi-line query from the command line or
  Infrastructure as Code, the API will reject the action with a parse error.

##

Amazon OpenSearch Service

**Creating the data source**

If the OpenSearch domain is enabled for FGAC, you must map the execution role of the connector Lambda function to a user in OpenSearch Service.
For more information, see the **Mapping users to roles** section in
[Managing permissions](../../../opensearch-service/latest/developerguide/fgac.md#fgac-access-control "../../../opensearch-service/latest/developerguide/fgac.md#fgac-access-control") in the OpenSearch Service documentation.

If your OpenSearch domain is only accessible within a Virtual Private Cloud (VPC), you need to manually include a new environment variable in the Lambda function called
`AMAZON_OPENSEARCH_ENDPOINT`. The value for this variable should be the root domain of the OpenSearch endpoint. You can obtain this root domain by
removing `https://` and `<region>.es.amazonaws.com` from the domain endpoint listed in the OpenSearch Service console.
For example, if your domain endpoint is `https://sample-domain.us-east-1.es.amazonaws.com`, the root domain would be `sample-domain`.

**Updating the data source**

- You can update your data source
  manually by doing the following:
  - To update the OpenSearch Service domain, update the
    `AMAZON_OPENSEARCH_DOMAIN_NAME` environment variable for the data source connector Lambda function.
  - To update the VPC configuration, see [Configuring VPC access (console)](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring") for more information.

**Querying the data source**

- When querying OpenSearch Service, after you select the data source in the **Multi source query** tab,
  do the following:
  - Select the Index to query.
  - Select the Metric name (Any numeric field in the document) and Stat.
  - Select the Time axis (Any date field in the document).
  - Select Filters to apply (Any String field in the document).
  - Choose **Graph query**.

##

Amazon RDS for PostgreSQL and Amazon RDS for MySQL

**Creating the data source**

- If your data source is only accessible in a VPC, you must include the VPC configuration
  for the connector, as described in [Connect to a prebuilt data source with a wizard](CloudWatch_MultiDataSources-Connect.md "CloudWatch_MultiDataSources-Connect.md"). If the data source is to connect to the VPC
  for credentials, the endpoint must be configured in the VPC. For more
  information, see [Using an AWS Secrets Manager VPC endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md").

Additionally, you must create a VPC endpoint for the Amazon RDS service. For more information,
see [Amazon RDS API and interface VPC endpoints (AWS PrivateLink)](../../../AmazonRDS/latest/UserGuide/vpc-interface-endpoints.md "../../../AmazonRDS/latest/UserGuide/vpc-interface-endpoints.md").

**Updating the data source**

- You can update your data source
  manually by doing the following:
  - To update the database instance, update the
    `RDS_INSTANCE` environment variable for the data source connector Lambda function.
  - To update the username and password used to connect to Amazon RDS, use
    AWS Secrets Manager. You can find the ARN of the secret used for the data
    source in the environment variable `RDS_SECRET` on the data source Lambda
    function. For more information about updating the secret in
    AWS Secrets Manager, see [Modify an
    AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md").
  - To update the VPC configuration, see [Configuring VPC access (console)](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring") for more information.

**Querying the data source**

- When querying Amazon RDS, after you select the data source in the **Multi source query** tab
  and select an Amazon RDS connector, you can use the database discoverer to view available databases,
  tables, and columns. You can also use the SQL editor to create an SQL query.

You can use the following variables in the query:

    + `$start.iso` – The start time in ISO date format
    + `$end.iso` – The end time in ISO date format
    + `$period` – The selected period in seconds

For example, you can query `SELECT value, timestamp FROM table WHERE timestamp BETWEEN $start.iso and $end.iso`

- Multi-line queries are not supported by the CloudWatch data source connectors. Every line feed is
  replaced with a space when the query is executed, or when you create an alarm or a
  dashboard widget with the query. In some cases, this might make your query not valid.
  For example, if your query contains a single line comment it will not be valid. If you
  try to create a dashboard or alarm with a multi-line query from the command line or
  Infrastructure as Code, the API will reject the action with a parse error.

###### Note

If no date field is found in the results, the values for each numeric field are summed to
single values and plotted across the provided time range. If the timestamps don't align
with the selected period in CloudWatch, the data is automatically aggregated using
`SUM` and aligned with the period in CloudWatch.

##

Amazon S3 CSV files

**Querying the data source**

- When querying Amazon S3 CSV files, after you select the data source in the **Multi source query** tab
  and select an Amazon S3 connector, you select the Amazon S3 bucket and key.

The CSV file must be formatted in the following ways:

    + The time stamp must be the first column.
    + The table must have a header row. The headers are used to name your
     metrics. The title of the time stamp column will be ignored, only the titles of the
     metrics columns are used.
    + The time stamps must be in ISO date format.
    + The metrics must be numeric fields.

```
Timestamp, Metric-1, Metric-2, ...
```

The following is an example:

| timestamp                 | CPU (%) | Memory (%) | Storage (%) |
| ------------------------- | ------- | ---------- | ----------- |
| 2023-11-23T17:09:41+00:00 | 1       | `2`        | `3`         |
| 2023-11-23T17:04:41+00:00 | 4       | `5`        | `6`         |
| 2023-11-23T16:59:41+00:00 | 7       | `8`        | `9`         |
| 2023-11-23T16:54:41+00:00 | 10      | `11`       | `12`        |

###### Note

If no timestamp is provided, the values for each metric are summed to single values and
plotted across the provided time range. If the timestamps don't align with the selected
period in CloudWatch, the data is automatically aggregated using `SUM` and aligned
with the period in CloudWatch.

##

Microsoft Azure Monitor

**Creating the data source**

- You must provide your tenant ID, client ID, and client secret to connect to Microsoft Azure
  Monitor. The credentials will be stored in AWS Secrets Manager. For more
  information, see [Create a Microsoft Entra application and service principal that can access
  resources](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal "https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal") in the Microsoft documentation.

**Updating the data source**

- You can update your data source
  manually by doing the following:
  - To update the tenant ID, client ID, and client secret used to connect to Azure Monitor, you can find the ARN of
    the secret used for the data source as the `AZURE_CLIENT_SECRET` environment
    variable on the data source Lambda function. For more information about updating the
    secret in AWS Secrets Manager, see [Modify an
    AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md").

**Querying the data source**

- When querying Azure Monitor, after you select the data source in the **Multi source query** tab
  and select an Azure Monitor connector,
  you specify the Azure subscription, and the resource group and resource. You can then select the metric namespace, metric,
  and aggregation, and filter by dimensions.

##

Prometheus

**Creating the data source**

- You must provide the Prometheus endpoint and the user and password required to query
  Prometheus. The credentials will be stored in AWS Secrets Manager.
- If your data source is only accessible in a VPC, you must include the VPC configuration
  for the connector, as described in [Connect to a prebuilt data source with a wizard](CloudWatch_MultiDataSources-Connect.md "CloudWatch_MultiDataSources-Connect.md"). If the data source is to connect to
  for credentials, the endpoint must be configured in the VPC. For more
  information, see [Using an AWS Secrets Manager VPC endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md").

**Updating data source configuration**

- You can update your data source
  manually by doing the following:
  - To update the Prometheus endpoint, specify the new endpoint as
    the `PROMETHEUS_API_ENDPOINT` environment variable on
    the data source Lambda function.
  - To update the username and password used to connect to Prometheus, you can find the ARN of the
    secret used for the data source as the `PROMETHEUS_API_SECRET`
    environment variable on the data source Lambda function. For more information about
    updating the secret in AWS Secrets Manager, see [Modify an
    AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md").
  - To update the VPC configuration, see [Configuring VPC access (console)](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring") for more information.

**Querying the data source**

###### Important

Prometheus metric types are different than CloudWatch metrics and many metrics available through
Prometheus are cumulative by design. When you query Prometheus metrics, CloudWatch doesn't apply any additional
transformation to the data: if you specify only the metric name or label, the displayed value
will be cumulative.
For more information, see [Metric types](https://prometheus.io/docs/concepts/metric_types/ "https://prometheus.io/docs/concepts/metric_types/") in the Prometheus documentation.

To see Prometheus metrics data as discrete values, like CloudWatch metrics, you need to edit
the query before you run it. For example, you might need to add a call to the rate
function over your Prometheus metric name. For documentation about the rate function and
other Prometheus functions, see [rate()](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate "https://prometheus.io/docs/prometheus/latest/querying/functions/#rate") in the Prometheus documentation.

Multi-line queries are not supported by the CloudWatch data source connectors. Every line feed
is replaced with a space when the query is executed, or when you create an alarm or a
dashboard widget with the query. In some cases, this might make your query not valid. For
example, if your query contains a single line comment it will not be valid. If you try to
create a dashboard or alarm with a multi-line query from the command line or Infrastructure
as Code, the API will reject the action with a parse error.

##

Notification of Available Updates

From time to time, Amazon might notify you that we recommend that you update your connectors
with a newer available version and will provide instructions for how to do so.
