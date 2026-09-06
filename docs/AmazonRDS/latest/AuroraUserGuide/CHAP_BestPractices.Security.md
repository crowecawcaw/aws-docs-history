

# Security best practices for Amazon Aurora
<a name="CHAP_BestPractices.Security"></a>

Use AWS Identity and Access Management (IAM) accounts to control access to Amazon RDS API operations, especially operations that create, modify, or delete Amazon Aurora resources. Such resources include DB clusters, security groups, and parameter groups. Also use IAM to control actions that perform common administrative actions such as backing up and restoring DB clusters. 
+ Create an individual user for each person who manages Amazon Aurora resources, including yourself. Don't use AWS root credentials to manage Amazon Aurora resources.
+ Grant each user the minimum set of permissions required to perform his or her duties.
+ Use IAM groups to effectively manage permissions for multiple users.
+ Rotate your IAM credentials regularly.
+ Configure AWS Secrets Manager to automatically rotate the secrets for Amazon Aurora. For more information, see [Rotating your AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. You can also retrieve the credential from AWS Secrets Manager programmatically. For more information, see [Retrieving the secret value](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_retrieve-secret.html) in the *AWS Secrets Manager User Guide*. 

For more information about Amazon Aurora security, see [Security in Amazon Aurora](UsingWithRDS.md) . For more information about IAM, see [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/Welcome.html). For information on IAM best practices, see [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html). 

AWS Security Hub CSPM uses security controls to evaluate resource configurations and security standards to help you comply with various compliance frameworks. For more information about using Security Hub CSPM to evaluate RDS resources, see [Amazon Relational Database Service controls](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html) in the AWS Security Hub User Guide.

You can monitor your usage of RDS as it relates to security best practices by using Security Hub CSPM. For more information, see [What is AWS Security Hub CSPM?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). 

Use the AWS Management Console, the AWS CLI, or the RDS API to change the password for your master user. If you use another tool, such as a SQL client, to change the master user password, it might result in privileges being revoked for the user unintentionally.

Amazon GuardDuty is a continuous security monitoring service that analyzes and processes various data sources, including Amazon RDS login activity. It uses threat intelligence feeds and machine learning to identify unexpected, potentially unauthorized, suspicious login behavior, and malicious activity within your AWS environment.

 When Amazon GuardDuty RDS Protection detects a potentially suspicious or anomalous login attempt that indicates a threat to your database, GuardDuty generates a new finding with details about the potentially compromised database. For more information, see [Monitoring threats with Amazon GuardDuty RDS Protectionfor Amazon Aurora](guard-duty-rds-protection.md) .