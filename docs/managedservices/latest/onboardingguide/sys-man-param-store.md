# Use AMS SSP to provision AWS Systems Manager Parameter Store in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Systems Manager Parameter Store capabilities directly in your AMS managed account. AWS Systems Manager Parameter Store provides secure, hierarchical storage for configuration data management and secrets management.
You can store data such as passwords,
database strings, and license codes as parameter values. You can store values as plain text or encrypted data. You can then
reference values by using the unique name that
you specified when you created the parameter. Highly scalable, available, and durable, Parameter Store is backed by the
AWS Cloud. To learn more, see
[AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md").

###### Note

If you want a dedicated secrets store with lifecycle management, use
[Use AMS SSP to provision AWS Secrets Manager in your AMS account](secrets-manager.md "secrets-manager.md") instead of Parameter Store.
Secrets Manager helps you meet your security and compliance requirements by
enabling you to rotate secrets automatically. Secrets Manager offers built-in
integration for MySQL, PostgreSQL, and Amazon Aurora on Amazon RDS, that's
extensible to other types of secrets by customizing Lambda functions.

## AWS Systems Manager Parameter Store in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Systems Manager Parameter Store in my AMS account?**

Request access to AWS Systems Manager Parameter Store by submitting an RFC with the
Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account:
`customer_systemsmanager_parameterstore_console_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Systems Manager Parameter Store in my AMS account?**

You are required to use AWS Managed keys; access is restricted from
creating custom KMS keys. However, if a custom key is required, submit an
RFC to create a customer-managed key (CMK) using the Deployment | Advanced
Stack Components | KMS Key | Create change type (ct-1d84keiri1jhg) with this
IAM role, `customer_systemsmanager_parameterstore_console_role`
as the value for the `IAMPrincipalsRequiringDecryptPermissions`
and `IAMPrincipalsRequiringEncryptPermissionsPrincipal`
parameters. After the KMS Key is created, you can create a Secure String using it.

**Q: What are the prerequisites or dependencies to using AWS Systems Manager Parameter Store in my AMS
account?**

There are no prerequisites; however, SSM Parameter Store is dependent on
KMS to create a Secure String so you can encrypt and decrypt their Values
stored in Parameter Store.
