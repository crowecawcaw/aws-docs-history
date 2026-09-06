

# Data protection in DynamoDB
<a name="data-protection"></a>

Amazon DynamoDB provides a highly durable storage infrastructure designed for mission-critical and primary data storage. Data is redundantly stored on multiple devices across multiple facilities in an Amazon DynamoDB Region.

DynamoDB protects user data stored at rest and also data in transit between on-premises clients and DynamoDB, and between DynamoDB and other AWS resources within the same AWS Region.

**Avoid sensitive data in resource names**  
We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free-form fields such as a *Name* field, including DynamoDB table names and DynamoDB Accelerator (DAX) cluster names. This guidance applies when you work with DynamoDB or other AWS services using the console, API, AWS CLI, or AWS SDKs. Diagnostic logs might capture information that you enter into free-form fields, and for DAX clusters that use encryption in transit, public Certificate Transparency (CT) logs also record the cluster name. For more information, see [DAX access control](DAX.access-control.md). When you provide a URL to an external server, don't include credentials in the URL that validate your request to that server.

**Topics**
+ [DynamoDB encryption at rest](EncryptionAtRest.md)
+ [Securing DynamoDB connections using VPC endpoints and IAM policies"](inter-network-traffic-privacy.md)