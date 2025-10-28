# Identity and access management in AWS Backup

Access to AWS Backup requires credentials. Those credentials must have permissions to access
AWS resources, such as an Amazon DynamoDB database or an Amazon EFS file system. Moreover, recovery
points created by AWS Backup for some AWS Backup-supported services cannot be deleted using the source
service (such as Amazon EFS). You can delete those recovery points using AWS Backup.

The following sections provide details on how you can use [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and AWS Backup to help secure
access to your resources.

###### Warning

AWS Backup uses the same IAM role that you chose when assigning resources to manage your
recovery point lifecycle. If you delete or modify that role, AWS Backup cannot manage your
recovery point lifecycle. When this occurs, it will attempt to use a service-linked role to
manage your lifecycle. In a small percentage of cases, this might also not work, leaving
`EXPIRED` recovery points on your storage, which might create unwanted costs.
To delete `EXPIRED` recovery points, manually delete them using the procedure in
[Deleting backups](deleting-backups.md "deleting-backups.md").

###### Topics

- [Authentication](authentication.md "authentication.md")
- [Access control](access-control.md "access-control.md")
- [IAM service roles](iam-service-roles.md "iam-service-roles.md")
- [Managed policies for AWS Backup](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Using service-linked roles for
  AWS Backup](using-service-linked-roles.md "using-service-linked-roles.md")
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
