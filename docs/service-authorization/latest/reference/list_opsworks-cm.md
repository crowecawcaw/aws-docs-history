# Actions, resources, and condition keys for AWS OpsWorks Configuration Management

AWS OpsWorks Configuration Management (service prefix: `opsworks-cm`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../opsworks/latest/userguide.md "../../../opsworks/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../opsworks-cm/latest/APIReference.md "../../../opsworks-cm/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../opsworks/latest/userguide/workingsecurity.md "../../../opsworks/latest/userguide/workingsecurity.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/opsworks-cm/opsworks-cm.json "https://servicereference.us-east-1.amazonaws.com/v1/opsworks-cm/opsworks-cm.json") for this service.

###### Topics

- [Actions defined by AWS OpsWorks Configuration Management](#list_opsworks-cm-actions-as-permissions "#list_opsworks-cm-actions-as-permissions")
- [Resource types defined by AWS OpsWorks Configuration Management](#list_opsworks-cm-resources-for-iam-policies "#list_opsworks-cm-resources-for-iam-policies")
- [Condition keys for AWS OpsWorks Configuration Management](#list_opsworks-cm-policy-keys "#list_opsworks-cm-policy-keys")

## Actions defined by AWS OpsWorks Configuration Management

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                        | Description                                                                                                             | Resource types (\*required) | Condition keys | Access level   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | -------------- |
| [AssociateNode](../../../opsworks-cm/latest/APIReference/API_AssociateNode.md "../../../opsworks-cm/latest/APIReference/API_AssociateNode.md")                                                 | Grants permission to associate a node to a configuration management server                                              |                             |                | Write          |
| [CreateBackup](../../../opsworks-cm/latest/APIReference/API_CreateBackup.md "../../../opsworks-cm/latest/APIReference/API_CreateBackup.md")                                                    | Grants permission to create a backup for the specified server                                                           |                             |                | Write          |
| [CreateServer](../../../opsworks-cm/latest/APIReference/API_CreateServer.md "../../../opsworks-cm/latest/APIReference/API_CreateServer.md")                                                    | Grants permission to create a new server                                                                                |                             |                | Write          |
| [DeleteBackup](../../../opsworks-cm/latest/APIReference/API_DeleteBackup.md "../../../opsworks-cm/latest/APIReference/API_DeleteBackup.md")                                                    | Grants permission to delete the specified backup and possibly its S3 bucket                                             |                             |                | Write          |
| [DeleteServer](../../../opsworks-cm/latest/APIReference/API_DeleteServer.md "../../../opsworks-cm/latest/APIReference/API_DeleteServer.md")                                                    | Grants permission to delete the specified server with its corresponding CloudFormation stack and possibly the S3 bucket |                             |                | Write          |
| [DescribeAccountAttributes](../../../opsworks-cm/latest/APIReference/API_DescribeAccountAttributes.md "../../../opsworks-cm/latest/APIReference/API_DescribeAccountAttributes.md")             | Grants permission to describe the service limits for the user's account                                                 |                             |                | List           |
| [DescribeBackups](../../../opsworks-cm/latest/APIReference/API_DescribeBackups.md "../../../opsworks-cm/latest/APIReference/API_DescribeBackups.md")                                           | Grants permission to describe a single backup, all backups of a specified server or all backups of the user's account   |                             |                | List           |
| [DescribeEvents](../../../opsworks-cm/latest/APIReference/API_DescribeEvents.md "../../../opsworks-cm/latest/APIReference/API_DescribeEvents.md")                                              | Grants permission to describe all events of the specified server                                                        |                             |                | List           |
| [DescribeNodeAssociationStatus](../../../opsworks-cm/latest/APIReference/API_DescribeNodeAssociationStatus.md "../../../opsworks-cm/latest/APIReference/API_DescribeNodeAssociationStatus.md") | Grants permission to describe the association status for the specified node token and the specified server              |                             |                | List           |
| [DescribeServers](../../../opsworks-cm/latest/APIReference/API_DescribeServers.md "../../../opsworks-cm/latest/APIReference/API_DescribeServers.md")                                           | Grants permission to describe the specified server or all servers of the user's account                                 |                             |                | List           |
| [DisassociateNode](../../../opsworks-cm/latest/APIReference/API_DisassociateNode.md "../../../opsworks-cm/latest/APIReference/API_DisassociateNode.md")                                        | Grants permission to disassociate a specified node from a server                                                        |                             |                | Write          |
| [ExportServerEngineAttribute](../../../opsworks-cm/latest/APIReference/API_ExportServerEngineAttribute.md "../../../opsworks-cm/latest/APIReference/API_ExportServerEngineAttribute.md")       | Grants permission to export an engine attribute from a server                                                           |                             |                | Read           |
| [ListTagsForResource](../../../opsworks-cm/latest/APIReference/API_ListTagsForResource.md "../../../opsworks-cm/latest/APIReference/API_ListTagsForResource.md")                               | Grants permission to list the tags that are applied to the specified server or backup                                   |                             |                | Read           |
| [RestoreServer](../../../opsworks-cm/latest/APIReference/API_RestoreServer.md "../../../opsworks-cm/latest/APIReference/API_RestoreServer.md")                                                 | Grants permission to apply a backup to specified server. Possibly swaps out the ec2-instance if specified               |                             |                | Write          |
| [StartMaintenance](../../../opsworks-cm/latest/APIReference/API_StartMaintenance.md "../../../opsworks-cm/latest/APIReference/API_StartMaintenance.md")                                        | Grants permission to start the server maintenance immediately                                                           |                             |                | Write          |
| [TagResource](../../../opsworks-cm/latest/APIReference/API_TagResource.md "../../../opsworks-cm/latest/APIReference/API_TagResource.md")                                                       | Grants permission to apply tags to the specified server or backup                                                       |                             |                | Tagging, Write |
| [UntagResource](../../../opsworks-cm/latest/APIReference/API_UntagResource.md "../../../opsworks-cm/latest/APIReference/API_UntagResource.md")                                                 | Grants permission to remove tags from the specified server or backup                                                    |                             |                | Tagging, Write |
| [UpdateServer](../../../opsworks-cm/latest/APIReference/API_UpdateServer.md "../../../opsworks-cm/latest/APIReference/API_UpdateServer.md")                                                    | Grants permission to update general server settings                                                                     |                             |                | Write          |
| [UpdateServerEngineAttributes](../../../opsworks-cm/latest/APIReference/API_UpdateServerEngineAttributes.md "../../../opsworks-cm/latest/APIReference/API_UpdateServerEngineAttributes.md")    | Grants permission to update server settings specific to the configuration management type                               |                             |                | Write          |

## Resource types defined by AWS OpsWorks Configuration Management

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                  | ARN                                                                                           | Condition keys |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------- |
| [backup](../../../opsworks/latest/userguide/security_iam_service-with-iam-opscm.md "../../../opsworks/latest/userguide/security_iam_service-with-iam-opscm.md") | arn:${Partition}:opsworks-cm::${Account}:backup/${ServerName}-{Date-and-Time-Stamp-of-Backup} |                |
| [server](../../../opsworks/latest/userguide/security_iam_service-with-iam-opscm.md "../../../opsworks/latest/userguide/security_iam_service-with-iam-opscm.md") | arn:${Partition}:opsworks-cm::${Account}:server/${ServerName}/${UniqueId}                     |                |

## Condition keys for AWS OpsWorks Configuration Management

AWS OpsWorks Configuration Management has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
