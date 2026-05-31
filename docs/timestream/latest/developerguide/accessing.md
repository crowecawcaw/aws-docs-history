For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Accessing Timestream for LiveAnalytics

You can access Timestream for LiveAnalytics using the console, CLI or the API. For information about accessing Timestream for LiveAnalytics,
review the following:

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Provide Timestream for LiveAnalytics access](#getting-started.prereqs.iam-user "#getting-started.prereqs.iam-user")
- [Using the console](console_timestream.md "console_timestream.md")
- [Accessing Amazon Timestream for LiveAnalytics using the AWS CLI](Tools.CLI.md "Tools.CLI.md")
- [Using the API](Using.API.md "Using.API.md")
- [Using the AWS SDKs](getting-started-sdks.md "getting-started-sdks.md")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Provide Timestream for LiveAnalytics access

The permissions that are required to access Timestream for LiveAnalytics are already granted to the
administrator. For other users, you should grant them Timestream for LiveAnalytics access using the following
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "timestream:*",
 "kms:DescribeKey",
 "kms:CreateGrant",
 "kms:Decrypt",
 "dbqms:CreateFavoriteQuery",
 "dbqms:DescribeFavoriteQueries",
 "dbqms:UpdateFavoriteQuery",
 "dbqms:DeleteFavoriteQueries",
 "dbqms:GetQueryString",
 "dbqms:CreateQueryHistory",
 "dbqms:UpdateQueryHistory",
 "dbqms:DeleteQueryHistory",
 "dbqms:DescribeQueryHistory",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

For information about `dbqms`, see [Actions, resources, and condition keys for Database Query Metadata
Service](../../../service-authorization/latest/reference/list_databasequerymetadataservice.md "../../../service-authorization/latest/reference/list_databasequerymetadataservice.md"). For information about `kms` see [Actions, resources, and condition keys for AWS Key Management
Service](../../../service-authorization/latest/reference/list_awskeymanagementservice.md "../../../service-authorization/latest/reference/list_awskeymanagementservice.md").
