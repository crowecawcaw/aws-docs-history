# Run Athena queries with Step Functions

You can integrate AWS Step Functions with Amazon Athena to start and
stop query execution and get query results with Step Functions. Using Step Functions, you can run ad-hoc or scheduled
data queries, and retrieve results targeting your S3 data lakes. Athena is serverless, so
there is no infrastructure to set up or manage, and you pay only for the queries you
run. This page lists the supported Athena APIs and provides an example `Task` state to start
an Athena query.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized Athena integration

- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration
  pattern is supported.
- There are no specific optimizations for the [Request Response](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") integration pattern.
- The [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token")
  integration pattern is not supported.
  To integrate AWS Step Functions with Amazon Athena, you use the provided Athena service integration
  APIs.

The service integration APIs are the same as the corresponding Athena APIs. Not all APIs
support all integration patterns, as shown in the following table.

| API                   | Request Response | Run a Job (.sync) |
| --------------------- | ---------------- | ----------------- |
| `StartQueryExecution` | Supported        | Supported         |
| `StopQueryExecution`  | Supported        | _Not supported_   |
| `GetQueryExecution`   | Supported        | _Not supported_   |
| `GetQueryResults`     | Supported        | _Not supported_   |

The following includes a Task state that starts an Athena query.

```
"Start an Athena query": {
  "Type": "Task",
  "Resource": "arn:aws:states:::athena:startQueryExecution.sync",
  "Arguments": {
    "QueryString": "SELECT * FROM \"myDatabase\".\"myTable\" limit 1",
    "WorkGroup": "primary",
    "ResultConfiguration": {
       "OutputLocation": "s3://amzn-s3-demo-bucket"
    }
  },
  "Next": "Get results of the query"
}
```

## Optimized Amazon Athena APIs:

- [`StartQueryExecution`](../../../athena/latest/APIReference/API_StartQueryExecution.md "../../../athena/latest/APIReference/API_StartQueryExecution.md")
- [`StopQueryExecution`](../../../athena/latest/APIReference/API_StopQueryExecution.md "../../../athena/latest/APIReference/API_StopQueryExecution.md")
- [`GetQueryExecution`](../../../athena/latest/APIReference/API_GetQueryExecution.md "../../../athena/latest/APIReference/API_GetQueryExecution.md")
- [`GetQueryResults`](../../../athena/latest/APIReference/API_GetQueryResults.md "../../../athena/latest/APIReference/API_GetQueryResults.md")

###### Quota for input or result data

When sending or receiving data between services, the maximum input or result for a task is 256 KiB of data as a UTF-8 encoded string. See [Quotas related to state
machine executions](service-quotas.md#service-limits-state-machine-executions "service-quotas.md#service-limits-state-machine-executions").

## IAM policies for calling Amazon Athena

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

###### Note

In addition to IAM policies, you might need to use AWS Lake Formation to grant access to data in services, such as Amazon S3 and the AWS Glue Data Catalog. For more information, see [Use Athena to query data registered with AWS Lake Formation](../../../athena/latest/ug/security-athena-lake-formation.md "../../../athena/latest/ug/security-athena-lake-formation.md").

### `StartQueryExecution`

_Static resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:startQueryExecution",
 "athena:stopQueryExecution",
 "athena:getQueryExecution",
 "athena:getDataCatalog",
 "athena:GetWorkGroup",
 "athena:BatchGetQueryExecution",
 "athena:GetQueryResults",
 "athena:ListQueryExecutions"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/myWorkGroup",
 "arn:aws:athena:`us-east-1`:`123456789012`:datacatalog/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:CreateBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:UpdateDatabase",
 "glue:DeleteDatabase",
 "glue:CreateTable",
 "glue:UpdateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:BatchCreatePartition",
 "glue:CreatePartition",
 "glue:UpdatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`123456789012`:catalog",
 "arn:aws:glue:`us-east-1`:`123456789012`:database/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:table/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:userDefinedFunction/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": [
 "*"
 ]
 }
]
}`

```

Request Response

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:startQueryExecution",
 "athena:getDataCatalog"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/myWorkGroup",
 "arn:aws:athena:`us-east-1`:`123456789012`:datacatalog/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:CreateBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:UpdateDatabase",
 "glue:DeleteDatabase",
 "glue:CreateTable",
 "glue:UpdateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:BatchCreatePartition",
 "glue:CreatePartition",
 "glue:UpdatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`123456789012`:catalog",
 "arn:aws:glue:`us-east-1`:`123456789012`:database/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:table/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:userDefinedFunction/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": [
 "*"
 ]
 }
]
}`

```

_Dynamic resources_

Run a Job (.sync)

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:startQueryExecution",
 "athena:stopQueryExecution",
 "athena:getQueryExecution",
 "athena:getDataCatalog",
 "athena:GetWorkGroup",
 "athena:BatchGetQueryExecution",
 "athena:GetQueryResults",
 "athena:ListQueryExecutions"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/*",
 "arn:aws:athena:`us-east-1`:`123456789012`:datacatalog/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:CreateBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:UpdateDatabase",
 "glue:DeleteDatabase",
 "glue:CreateTable",
 "glue:UpdateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:BatchCreatePartition",
 "glue:CreatePartition",
 "glue:UpdatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`123456789012`:catalog",
 "arn:aws:glue:`us-east-1`:`123456789012`:database/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:table/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:userDefinedFunction/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": [
 "*"
 ]
 }
]
}`

```

Request Response

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:startQueryExecution",
 "athena:getDataCatalog"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/*",
 "arn:aws:athena:`us-east-1`:`123456789012`:datacatalog/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:CreateBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:UpdateDatabase",
 "glue:DeleteDatabase",
 "glue:CreateTable",
 "glue:UpdateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:BatchCreatePartition",
 "glue:CreatePartition",
 "glue:UpdatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`123456789012`:catalog",
 "arn:aws:glue:`us-east-1`:`123456789012`:database/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:table/*",
 "arn:aws:glue:`us-east-1`:`123456789012`:userDefinedFunction/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": [
 "*"
 ]
 }
]
}`

```

### `StopQueryExecution`

_Resources_

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:stopQueryExecution"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/*"
 ]
 }
 ]
}`

```

### `GetQueryExecution`

_Resources_

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:getQueryExecution"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/*"
 ]
 }
 ]
}`

```

### `GetQueryResults`

_Resources_

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:getQueryResults"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 }
 ]
}`

```
