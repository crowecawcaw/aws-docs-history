# Security Lake queries for AWS source version 2 (OCSF 1.1.0)

The following section provides guidance on querying data from Security Lake and includes some query examples for natively-supported AWS sources for AWS source version 2. These
queries are designed to retrieve data in a specific AWS Region. These examples use us-east-1 (US East (N. Virginia)). In addition, the example queries
use a `LIMIT 25` parameter, which returns up to 25 records. You can omit this parameter or adjust it based on your preferences.
For more examples, see the [Amazon Security Lake OCSF Queries GitHub directory](https://github.com/awslabs/aws-security-analytics-bootstrap/tree/main/AWSSecurityAnalyticsBootstrap/amazon_security_lake_queries "https://github.com/awslabs/aws-security-analytics-bootstrap/tree/main/AWSSecurityAnalyticsBootstrap/amazon_security_lake_queries").

You can query the data that Security Lake stores in AWS Lake Formation databases and tables. You can also create third-party subscribers in the Security Lake console, API, or
AWS CLI. Third-party subscribers can also query Lake Formation data from the sources that you specify.

The Lake Formation data lake administrator must grant `SELECT` permissions on the relevant databases and
tables to the IAM identity that queries the data. A subscriber must also be created in Security Lake before it can query
data. For more information about how to create a subscriber with query access, see [Managing query access for Security Lake
subscribers](subscriber-query-access.md "subscriber-query-access.md").

The following queries include time-based filters using `eventDay`
to ensure your query is within the configured retention settings.
For more information, see [Querying data with retention settings](subscriber-query-examples.md#security-lake-retention-setting-query-data "subscriber-query-examples.md#security-lake-retention-setting-query-data").

For example,
if data older than 60 days has expired, your queries should include time
constraints to prevent accessing expired data. For a 60-day retention period,
include the following clause in your query:

```
...
WHERE time_dt > DATE_ADD('day', -59, CURRENT_TIMESTAMP)
...
```

This clause uses 59 days (rather than 60) to avoid any data or time
overlap between Amazon S3 and Apache Iceberg.

## Log source table

When you query Security Lake data, you must include the name of the Lake Formation table in which the data resides.

```
SELECT *
FROM "amazon_security_lake_glue_db_DB_Region"."amazon_security_lake_table_DB_Region_SECURITY_LAKE_TABLE"
WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
LIMIT 25
```

Common values for the log source table include the following:

- `cloud_trail_mgmt_2_0` – AWS CloudTrail management events
- `lambda_execution_2_0` – CloudTrail data events for Lambda
- `s3_data_2_0` – CloudTrail data events for S3
- `route53_2_0` – Amazon Route 53 resolver query logs
- `sh_findings_2_0` – AWS Security Hub CSPM findings
- `vpc_flow_2_0` – Amazon Virtual Private Cloud (Amazon VPC) Flow Logs
- `eks_audit_2_0` – Amazon Elastic Kubernetes Service (Amazon EKS) Audit Logs
- `waf_2_0` – AWS WAFv2 Logs

**Example: All Security Hub CSPM findings in table
`sh_findings_2_0` from us-east-1 Region**

```
SELECT *
    FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_sh_findings_2_0"
    WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
LIMIT 25
```

## Database Region

When you query Security Lake data, you must include the name of the database Region from which you're querying the data.
For a complete list of database Regions where Security Lake is currently available, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md").

**Example: List Amazon Virtual Private Cloud activity from source IP**

The following example lists all the Amazon VPC activities from the source IP
`192.0.2.1` that were recorded after
`20230301` (March 01, 2023), in the table
`vpc_flow_2_0` from the
`us-west-2`
`DB_Region`.

```
SELECT *
    FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_vpc_flow_2_0"
    WHERE time_dt > TIMESTAMP '2023-03-01'
    AND src_endpoint.ip = '192.0.2.1'
    ORDER BY time_dt desc
LIMIT 25
```

## Partition date

By partitioning your data, you can restrict the amount of data scanned by each query,
thereby improving performance and reducing cost. Partitions work slightly different in
Security Lake 2.0 compared to Security Lake 1.0. Security Lake now implements partitioning
through `time_dt`, `region`, and `accountid`. Whereas,
Security Lake 1.0 implemented partitioning through `eventDay`,
`region`, and `accountid` parameters.

Querying `time_dt` will automatically yield the date partitions from S3,
and can be queried just like any time based field in Athena.

This is an example query using the `time_dt` partition to query the logs
after the time March 01, 2023:

```
SELECT *
    FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_vpc_flow_2_0"
WHERE time_dt > TIMESTAMP '2023-03-01'
AND src_endpoint.ip = '192.0.2.1'
ORDER BY time desc
LIMIT 25
```

Common values for `time_dt` include the following:

**Events occurring in the last 1 year**

`WHERE time_dt > CURRENT_TIMESTAMP - INTERVAL '1' YEAR`

**Events occurring in the last 1 month**

`WHERE time_dt > CURRENT_TIMESTAMP - INTERVAL '1' MONTH`

**Events occurring in the last 30 days**

`WHERE time_dt > CURRENT_TIMESTAMP - INTERVAL '30' DAY`

**Events occurring in the last 12 hours**

`WHERE time_dt > CURRENT_TIMESTAMP - INTERVAL '12' HOUR`

**Events occurring in the last 5 minutes**

`WHERE time_dt > CURRENT_TIMESTAMP - INTERVAL '5' MINUTE`

**Events occurring between 7–14 days ago**

`WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '14' DAY AND CURRENT_TIMESTAMP - INTERVAL '7' DAY`

**Events occurring on or after a specific date**

`WHERE time_dt >= TIMESTAMP '2023-03-01'`

**Example: List of all CloudTrail activity from source IP `192.0.2.1` on or after March 1, 2023 in table `cloud_trail_mgmt_1_0`**

```
SELECT *
    FROM amazon_security_lake_glue_db_us_east_1.amazon_security_lake_table_us_east_1_cloud_trail_mgmt_1_0
    WHERE eventDay >= '`20230301`'
    AND src_endpoint.ip = '192.0.2.1'
    ORDER BY time desc
    LIMIT `25`
```

**Example: List of all CloudTrail activity from source IP `192.0.2.1` in the last 30 days in table `cloud_trail_mgmt_1_0`**

```
SELECT *
    FROM amazon_security_lake_glue_db_us_east_1.amazon_security_lake_table_us_east_1_cloud_trail_mgmt_1_0
    WHERE eventDay > cast(date_format(current_timestamp - INTERVAL '`30`' day, '%Y%m%d%H') as varchar)
    AND src_endpoint.ip = '192.0.2.1'
    ORDER BY time desc
    LIMIT `25`
```

## Querying Security Lake observables

Observables is a new feature now available in Security Lake 2.0. The observable object is a pivot element that contains related information found in many places in the event. Querying observables allows users to derive high level security insights from across their data sets.

By querying specific elements within observables, you can restrict the data sets to things such as specific User names, Resource UIDs, IPs, Hashes and other IOC type information

This is an example query using the observables array to query the logs across VPC Flow and Route53 tables containing the IP value '172.01.02.03'

```
WITH a AS
    (SELECT
    time_dt,
    observable.name,
    observable.value
    FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_vpc_flow_2_0",
    UNNEST(observables) AS t(observable)
    WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
    AND observable.value='172.01.02.03'
    AND observable.name='src_endpoint.ip'),
b as
    (SELECT
    time_dt,
    observable.name,
    observable.value
    FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_route53_2_0",
    UNNEST(observables) AS t(observable)
    WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
    AND observable.value='172.01.02.03'
    AND observable.name='src_endpoint.ip')
SELECT * FROM a
LEFT JOIN b ON a.value=b.value and a.name=b.name
LIMIT 25
```

## Example Security Lake queries for Amazon EKS audit logs

Amazon EKS logs track control plane activity provides audit and diagnostic logs directly from the Amazon EKS control plane to CloudWatch Logs in your account. These logs make it easy for you to secure and run your clusters. Subscribers can query EKS logs to learn the following types of information.

Here are some example queries for Amazon EKS audit logs for AWS source version 2:

**Requests to a specific URL in the last 7 days**

```
SELECT
    time_dt,
    actor.user.name,
    http_request.url.path,
    activity_name
FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_eks_audit_2_0"
WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
AND activity_name = 'get'
and http_request.url.path = '/apis/coordination.k8s.io/v1/'
LIMIT 25
```

**Update requests from '10.0.97.167' over the last 7 days**

```
SELECT
    activity_name,
    time_dt,
    api.request,
    http_request.url.path,
    src_endpoint.ip,
    resources
FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_eks_audit_2_0"
WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
AND src_endpoint.ip = '10.0.97.167'
AND activity_name = 'Update'
LIMIT 25
```

**Requests and Responses associated with resource 'kube-controller-manager' over the last 7 days**

```
SELECT
    activity_name,
    time_dt,
    api.request,
    api.response,
    resource.name
FROM "amazon_security_lake_glue_db_us_east_1"."amazon_security_lake_table_us_east_1_eks_audit_2_0",
UNNEST(resources) AS t(resource)
WHERE time_dt BETWEEN CURRENT_TIMESTAMP - INTERVAL '7' DAY AND CURRENT_TIMESTAMP
AND resource.name = 'kube-controller-manager'
LIMIT 25
```
