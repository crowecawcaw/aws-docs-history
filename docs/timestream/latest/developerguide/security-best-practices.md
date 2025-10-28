For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Security best practices for Timestream for InfluxDB

Amazon Timestream for InfluxDB provides a number of security features to consider as you develop and implement your own security policies.
The following best practices are general guidelines and don’t represent a complete security solution. Because these best
practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than
prescriptions.

## Implement least privilege access

When granting permissions, you decide who is getting what permissions to which Timestream for InfluxDB resources. You enable
specific actions that you want to allow on those resources. Therefore you should grant only the permissions that are
required to perform a task. Implementing least privilege access is fundamental in reducing security risk and the impact
that could result from errors or malicious intent.

## Use IAM roles

Producer and client applications must have valid credentials to access
Timestream for InfluxDB DB instances. You should not store AWS credentials directly in a client application or in an Amazon S3 bucket.
These are long-term credentials that are not automatically rotated and could have a significant business impact if they are compromised.

Instead, you should use an IAM role to manage temporary credentials for your producer and client applications to access Timestream for InfluxDB DB instances. When you
use a role, you don't have to use long-term credentials (such as a user name and password or access keys) to access other resources.

For more information, see the following topics in the _IAM User Guide_:

- [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
- [Common Scenarios for Roles: Users, Applications, and Services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md")

Use AWS Identity and Access Management (IAM) accounts to control access to Amazon Timestream for InfluxDB API operations, especially operations that create, modify, or delete Amazon Timestream for InfluxDB resources. Such resources include DB instances, security groups, and parameter groups.

- Create an individual user for each person who manages Amazon Timestream for InfluxDB resources, including yourself. Don't use AWS root credentials to manage Amazon Timestream for InfluxDB resources.
- Grant each user the minimum set of permissions required to perform his or her duties.
- Use IAM groups to effectively manage permissions for multiple users.
- Rotate your IAM credentials regularly.
- Configure AWS Secrets Manager to automatically rotate the secrets for Amazon Timestream for InfluxDB.
  For more information, see [Rotating your AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the
  _AWS Secrets Manager User Guide_. You can also retrieve the credential from AWS Secrets Manager programmatically.
  For more information, see [Retrieving the secret value](../../../secretsmanager/latest/userguide/manage_retrieve-secret.md "../../../secretsmanager/latest/userguide/manage_retrieve-secret.md") in the _AWS Secrets Manager User Guide_.
- Secure your Timestream for InfluxDB influx API tokens by using the [API tokens](timestream-for-influx-security-db-authentication.md#timestream-for-influx-security-db-authentication-api-token "timestream-for-influx-security-db-authentication.md#timestream-for-influx-security-db-authentication-api-token").

## Implement Server-Side Encryption in Dependent Resources

Data at rest and data in transit can be encrypted in Timestream for InfluxDB. For more information, see [Encryption in transit](EncryptionInTransit-for-influx-db.md "EncryptionInTransit-for-influx-db.md").

## Use CloudTrail to Monitor API Calls

Timestream for InfluxDB is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Timestream for InfluxDB.

Using the information collected by CloudTrail, you can determine the request that was made to Timestream for InfluxDB, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information, see [Logging Timestream for LiveAnalytics API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

Amazon Timestream for InfluxDB supports control plane CloudTrail events, but not data plane. For more information, see [Control planes and data planes](../../../whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.md").

## Public accessibility

When you launch a DB instance inside a virtual private cloud (VPC) based on the Amazon VPC service, you can turn on or off public accessibility for that DB instance.
To designate whether the DB instance that you create has a DNS name that resolves to a public IP address, you use the Public accessibility parameter. By using this parameter, you can designate whether there is public access to the DB instance

If your DB instance is in a VPC but isn't publicly accessible, you can also use an AWS Site-to-Site VPN connection or an AWS Direct Connect connection to access it from a private network.

If your DB instance is publicly accessible, be sure to take steps to prevent or help mitigate denial of service related threats. For more information, see [Introduction to denial of service attacks](../../../whitepapers/latest/aws-best-practices-ddos-resiliency/introduction-denial-of-service-attacks.md "../../../whitepapers/latest/aws-best-practices-ddos-resiliency/introduction-denial-of-service-attacks.md") and [Protecting networks](../../../wellarchitected/latest/security-pillar/protecting-networks.md "../../../wellarchitected/latest/security-pillar/protecting-networks.md").
