# Using AWS Secrets Manager with AMS resources

There are many cases where you may need to share secrets with AMS, for example:

- Master password reset for RDS instance
- Certificates for load balancers
- Obtaining long-lived credentials for IAM users from AMS
  The safest way to share confidential information with AMS is through the AWS Secrets Manager; follow these steps:

1. Login to the AWS Console using your federated access and the CustomerReadOnly role for single-account landing zone (SALZ); use any of
   these roles, AWSManagedServicesSecurityOpsRole, AWSManagedServicesAdminRole, and AWSManagedServicesChangeManagementRole for multi-account landing zone (MALZ).
2. Navigate to the [AWS Secrets manager console](https://console.aws.amazon.com/secretsmanager/home "https://console.aws.amazon.com/secretsmanager/home") and click **Store a new secret**.
3. Select "Other type of secrets".
4. Enter the secret value as a plain-text and click **Next**.
5. Enter the secret name and description. The name should always starts with "**customer-shared/\***". For example
   "**customer-shared/license-2018**". Once you are done continue by clicking **Next**.
6. Use the default KMS encryption.
7. Leave automatic rotation disabled and click **Next**.
8. Review and click **Store**, to save the secret.
9. Reply to us in an AMS service request with the secret name and ARN, so we can identify and retrieve the secret. For information on creating service requests, see
   [Service Request Examples](../userguide/serv-req-mgmt-examples.md "../userguide/serv-req-mgmt-examples.md").
