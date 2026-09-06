

# Using service-linked roles for AWS Backup
<a name="using-service-linked-roles"></a>

AWS Backup uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts). A service-linked role is a unique type of IAM role that is linked directly to AWS Backup. Service-linked roles are predefined by AWS Backup and include all the permissions that the service requires to call other AWS services on your behalf. 

**Topics**
+ [Using roles to back up and copy](using-service-linked-roles-AWSServiceRoleForBackup.md)
+ [Using roles for AWS Backup Audit Manager](using-service-linked-roles-AWSServiceRoleForBackupReports.md)
+ [Using roles for restore testing](using-service-linked-roles-AWSServiceRoleForBackupRestoreTesting.md)