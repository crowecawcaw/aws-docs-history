# Supported

Regions and DB engines for the Secrets Manager integration with Amazon RDS

With AWS Secrets Manager, you can replace hard-coded credentials in your code, including database
passwords, with an API call to Secrets Manager to retrieve the secret programmatically. For more
information about Secrets Manager, see [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md").

You can specify that Amazon RDS manages the master user password in Secrets Manager for an Amazon RDS DB
instance or Multi-AZ DB cluster. RDS generates the password, stores it in Secrets Manager, and rotates it regularly. For
more information, see [Password management with
Amazon RDS
and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md").

Secrets Manager integration is available in all AWS Regions.
