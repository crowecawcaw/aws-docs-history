# Changing an AWS KMS

policy for Performance Insights

Performance Insights uses an AWS KMS key to encrypt sensitive data. When you enable Performance Insights
through the API or the console, you can do either of the following:

- Choose the default AWS managed key.

Amazon RDS uses the AWS managed key for your new DB instance. Amazon RDS creates an
AWS managed key for your AWS account. Your AWS account has a different
AWS managed key for Amazon RDS for each AWS Region.

- Choose a customer managed key.

If you specify a customer managed key, users in your account that call the Performance Insights
API need the `kms:Decrypt` and `kms:GenerateDataKey`
permissions on the KMS key. You can configure these permissions through IAM
policies. However, we recommend that you manage these permissions through your
KMS key policy. For more information, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md")
in the _AWS Key Management Service Developer
Guide_.

###### Example

The following example shows how to add statements to your KMS key policy. These
statements allow access to Performance Insights.
Depending on how you use the KMS key, you might want to change some restrictions.
Before adding statements to your policy, remove all comments.

JSON

```
`{
 "Version":"2012-10-17",
 "Id" : "your-policy",
 "Statement" : [
 {
 "Sid" : "AllowViewingRDSPerformanceInsights",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`444455556666`:role/`Role1`"
 ]
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition" : {
 "StringEquals" : {
 "kms:ViaService" : "rds.`us-east-1`.amazonaws.com"
 },
 "ForAnyValue:StringEquals": {
 "kms:EncryptionContext:aws:pi:service": "rds",
 "kms:EncryptionContext:service": "pi",
 "kms:EncryptionContext:aws:rds:db-id": "`db-AAAAABBBBBCCCCDDDDDEEEEE`"
 }
 }
 }
 ]
}`

```

## How Performance Insights uses AWS KMS customer managed key

Performance Insights uses customer managed keys to encrypt sensitive data. When you turn on Performance Insights, you can provide an
AWS KMS key through the API. Performance Insights creates AWS KMS permissions on this key. It uses the key
and performs the necessary operations to process sensitive data. Sensitive data
includes fields such as user, database, application, and SQL query text. Performance Insights
ensures that the data remains encrypted both at rest and in-flight.

## How Performance Insights IAM works with AWS KMS

IAM gives permissions to specific APIs. Performance Insights has the following public APIs, which you can restrict using IAM policies:

- `DescribeDimensionKeys`
- `GetDimensionKeyDetails`
- `GetResourceMetadata`
- `GetResourceMetrics`
- `ListAvailableResourceDimensions`
- `ListAvailableResourceMetrics`

You can use the following API requests to get sensitive data.

- `DescribeDimensionKeys`
- `GetDimensionKeyDetails`
- `GetResourceMetrics`

When you use the API to get sensitive data, Performance Insights leverages the caller's credentials. This
check ensures that access to sensitive data is limited to those with access to the
KMS key.

When calling these APIs, you need permissions to call the API through the IAM policy and
permissions to invoke the `kms:decrypt` action through the AWS KMS key
policy.

The `GetResourceMetrics` API can return both sensitive and non-sensitive data. The request
parameters determine whether the response should include sensitive data. The API returns sensitive data
when the request includes a sensitive dimension in either the filter or group-by parameters.

For more information about the dimensions that you can use with the `GetResourceMetrics` API, see [DimensionGroup](../../../performance-insights/latest/APIReference/API_DimensionGroup.md "../../../performance-insights/latest/APIReference/API_DimensionGroup.md").

###### Examples

The following example requests the sensitive data for the `db.user` group:

```

POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetResourceMetrics
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "ServiceType": "RDS",
  "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
  "MetricQueries": [
    {
      "Metric": "db.load.avg",
      "GroupBy": {
        "Group": "db.user",
        "Limit": 2
      }
    }
  ],
  "StartTime": 1693872000,
  "EndTime": 1694044800,
  "PeriodInSeconds": 86400
}

```

###### Example

The following example requests the non-sensitive data for the `db.load.avg` metric:

```

POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetResourceMetrics
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "MetricQueries": [
        {
            "Metric": "db.load.avg"
        }
    ],
    "StartTime": 1693872000,
    "EndTime": 1694044800,
    "PeriodInSeconds": 86400
}

```
