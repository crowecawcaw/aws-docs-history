For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# General security

###### Topics

- [Permissions](#timestream-for-influx-getting-started-security-permissions "#timestream-for-influx-getting-started-security-permissions")
- [Network access](#timestream-for-influx-getting-started-security-network-access "#timestream-for-influx-getting-started-security-network-access")
- [Dependencies](#timestream-for-influx-getting-started-security-dependencies "#timestream-for-influx-getting-started-security-dependencies")
- [S3 buckets](#timestream-for-influx-getting-started-security-s3-buckets "#timestream-for-influx-getting-started-security-s3-buckets")

## Permissions

InfluxDB users should be granted least-privilege permissions. Only tokens granted to specific users, instead of operator tokens, should be used during migration.

Timestream for InfluxDB uses IAM permissions to control user permissions. We recommend users be granted access to the specific actions and resources that they require.
For more information, see [Grant least privilege access](../../../wellarchitected/2022-03-31/framework/sec_permissions_least_privileges.md "../../../wellarchitected/2022-03-31/framework/sec_permissions_least_privileges.md").

## Network access

The Influx migration script can function locally, migrating data between two InfluxDB instances on the same system,
but it is assumed that the primary use case for migrations will be migrating data across the network,
either a local or public network. With this comes security considerations.
The Influx migration script will, by default, verify TLS certificates for instances with TLS enabled: we recommend
that users enable TLS in their InfluxDB instances and do not use the `--skip-verify` option for the script.

We recommend you use an allow-list to restrict network traffic to be from sources you are expecting. You can do this by limiting network traffic to the InfluxDB instances only from known IPs.

## Dependencies

The latest major versions of all dependencies should be used, including Influx CLI, InfluxDB, Python, the Requests module,
and optional dependencies such as `mountpoint-s3` and `rclone`.

## S3 buckets

If S3 buckets are used as a temporary storage for migration, we recommend enabling TLS, versioning, and disabling public access.

###### Using S3 buckets for migration

1. Open the AWS Management Console, navigate to **Amazon Simple Storage Service** and then choose **Buckets**.
2. Choose the bucket you wish to use.
3. Choose the **Permissions** tab.
4. Under **Block public access (bucket settings)**, choose **Edit**.
5. Check **Block all public access**.
6. Choose **Save changes**.
7. Under **Bucket policy**, choose **Edit**.
8. Enter the following, replacing _<example-bucket>_ with your bucket name, to enforce the use of TLS version 1.2 or later
   for connections:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceTLSv12orHigher",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "s3:*"
 ],
 "Effect": "Deny",
 "Resource": [
 "arn:aws:s3:::<example bucket>/*",
 "arn:aws:s3:::<example bucket>"
 ],
 "Condition": {
 "NumericLessThan": {
 "s3:TlsVersion": 1.2
 }
 }
 }
 ]
}`

```

9. Choose **Save changes**.
10. Choose the **Properties** tab.
11. Under **Bucket Versioning**, choose **Edit**.
12. Check **Enable**.
13. Choose **Save changes**.

For information about Amazon S3 bucket best security practices, see [Security best practices for Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").
