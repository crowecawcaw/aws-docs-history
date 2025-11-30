# Protecting data in transit with

encryption

Amazon S3 supports both HTTP and HTTPS protocols for data transmission. HTTP transmits data in
plain text, while HTTPS adds a security layer by encrypting data using Transport Layer
Security (TLS). TLS protects against eavesdropping, data tampering, and man-in-the-middle
attacks. While HTTP traffic is accepted, most implementations use encryption in transit with
HTTPS and TLS to protect data as it travels between clients and Amazon S3.

## TLS 1.2 and TLS 1.3 Support

Amazon S3 supports TLS 1.2 and TLS 1.3 for HTTPS connections across all API endpoints for all
AWS Regions. S3 automatically negotiates the strongest TLS protection supported by
your client software, and the S3 endpoint you are accessing. Current AWS tools (2014
or later) including the AWS SDKs and AWS CLI automatically default to TLS 1.3 with no action
required on your part. You can override this automatic negotiation through client
configuration settings to specify a particular TLS version if backward compatibility to
TLS 1.2 is needed. When using TLS 1.3, you can optionally configure hybrid post quantum
key exchange (ML-KEM) to make quantum-resistant requests to Amazon S3. For more information,
see [Configuring hybrid post-quantum TLS for your client](pqtls-how-to.md "pqtls-how-to.md").

###### Note

TLS 1.3 is supported in all S3 endpoints, except for AWS PrivateLink for Amazon S3 and
Multi-Region Access Points.

## Monitoring TLS usage

You can use either Amazon S3 server access logs or AWS CloudTrail to monitor requests to Amazon S3 buckets.
Both logging options record the TLS version and cipher suite used in each
request.

- **Amazon S3 server access logs** – Server access logging provides
  detailed records for the requests that are made to a bucket. For example, access
  log information can be useful in security and access audits. For more
  information, see [Amazon S3 server access log format](LogFormat.md "LogFormat.md").
- **AWS CloudTrail** – [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is a service that provides a record of actions taken by a
  user, role, or an AWS service. CloudTrail captures all API calls for Amazon S3 as events.
  For more information, see [Amazon S3 CloudTrail events](cloudtrail-logging-s3-info.md "cloudtrail-logging-s3-info.md").

## Enforcing encryption in transit

It’s a security best practice to enforce encryption of data in transit to Amazon S3. You can
enforce HTTPS-only communication or the use of specific TLS version through various
policy mechanisms. These include IAM resource-based policies for S3 buckets ([bucket policies](bucket-policies.md "bucket-policies.md")), [Service Control
Policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCPs), [Resource Control
Policies](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") (RCPs), and [VPC endpoint
policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md").

### Bucket policy examples for enforcing encryption in transit

You can use the [S3 condition key](../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys "../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys")
`s3:TlsVersion` to restrict access to Amazon S3 buckets based on the TLS
version that's used by the client. For more information, see [Example 6: Requiring a minimum TLS
version](amazon-s3-policy-keys.md#example-object-tls-version "amazon-s3-policy-keys.md#example-object-tls-version").

###### Example bucket policy enforcing TLS 1.3 using the `S3:TlsVersion` condition

key

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "DenyInsecureConnections",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::``amzn-s3-demo-bucket1``",
 "arn:aws:s3:::``amzn-s3-demo-bucket1``/*"
 ],
 "Condition": {
 "NumericLessThan": {
 "s3:TlsVersion": "1.3"
 }
 }
 }
 ]
}`
```

You can use the `aws:SecureTransport`
[global
condition key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in your S3 bucket policy to check whether the request was
sent through HTTPS (TLS). Unlike the previous example, this condition does not check
for a specific TLS version. For more information, see [Restrict access to only
HTTPS requests](example-bucket-policies.md#example-bucket-policies-use-case-HTTP-HTTPS-1 "example-bucket-policies.md#example-bucket-policies-use-case-HTTP-HTTPS-1").

###### Example bucket policy enforcing HTTPS using the `aws:SecureTransport` global condition

key

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RestrictToTLSRequestsOnly",
 "Action": "s3:*",
 "Effect": "Deny",
 "Resource": [
 "arn:aws:s3:::``amzn-s3-demo-bucket1``",
 "arn:aws:s3:::``amzn-s3-demo-bucket1``/*"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 },
 "Principal": "*"
 }
 ]
}`
```

###### Example policy based on both keys and more examples

You can use both types of condition keys in the previous examples in one
policy. For more information and additional enforcement approaches, see the
AWS Storage Blog article [Enforcing encryption in transit with TLS1.2 or higher with
Amazon S3](https://aws.amazon.com/blogs/storage/enforcing-encryption-in-transit-with-tls1-2-or-higher-with-amazon-s3/ "https://aws.amazon.com/blogs/storage/enforcing-encryption-in-transit-with-tls1-2-or-higher-with-amazon-s3/").
