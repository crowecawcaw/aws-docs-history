

# Security best practices in AWS HealthLake
<a name="best-practices-security"></a>

AWS HealthLake provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions. 
+ Implement least privilege access.
+ Whenever possible, use Customer-Managed-Keys(CMKs) to encrypt your data. To learn more about CMKs, see [Amazon Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html). 
+ Use Search with POST, not Search with GET when querying for PHI or PII in your data store.
+ Limit access to sensitive and important auditing functions.
+ When creating resources through the update or bulk import APIs, do not use PHI or PII, including the names of data stores and jobs, in any visible fields or in the logical FHIR ID (LID).
+ When sending create, read, update, delete, or search requests, do not use PHI in the HTTP header.
+ Enable AWS CloudTrail to audit AWS HealthLake use and to ensure that there is no unexpected activity. 
+ Review best practices for using Amazon S3 buckets securely. To learn more, see [Security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) in the *Amazon S3 user guide*. 