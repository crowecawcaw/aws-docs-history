For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Configure S3 VPC Endpoint for Private Clusters

When deploying private clusters, you must configure an S3 VPC endpoint with appropriate
permissions to ensure cluster resources can access required S3 buckets.

## Prerequisites

- A VPC with private subnets configured for your cluster
- Appropriate IAM permissions to create and modify VPC endpoints

## Required S3 Endpoint Policy

Your S3 VPC endpoint requires a policy that grants sufficient access for cluster operations.
The following example provides full S3 access through the endpoint:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccess",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "*",
 "Resource": "*"
 }
 ]
}`

```

## Configuration Steps

1. Navigate to the VPC console and select **Endpoints**
2. Choose your S3 endpoint or create a new one
3. In the **Policy** tab, replace the existing policy with the example above
4. Save your changes
