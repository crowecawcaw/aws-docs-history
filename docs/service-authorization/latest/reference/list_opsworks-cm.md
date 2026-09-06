

# Actions, resources, and condition keys for AWS OpsWorks Configuration Management
<a name="list_opsworks-cm"></a>

AWS OpsWorks Configuration Management (service prefix: `opsworks-cm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opsworks/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opsworks/latest/userguide/workingsecurity.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/opsworks-cm/opsworks-cm.json) for this service.

**Topics**
+ [Actions defined by AWS OpsWorks Configuration Management](#list_opsworks-cm-actions-as-permissions)
+ [Resource types defined by AWS OpsWorks Configuration Management](#list_opsworks-cm-resources-for-iam-policies)
+ [Condition keys for AWS OpsWorks Configuration Management](#list_opsworks-cm-policy-keys)

## Actions defined by AWS OpsWorks Configuration Management
<a name="list_opsworks-cm-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AssociateNode](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_AssociateNode.html)  | Grants permission to associate a node to a configuration management server |  |   | Write | 
|   [CreateBackup](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_CreateBackup.html)  | Grants permission to create a backup for the specified server |  |   | Write | 
|   [CreateServer](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_CreateServer.html)  | Grants permission to create a new server |  |   | Write | 
|   [DeleteBackup](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DeleteBackup.html)  | Grants permission to delete the specified backup and possibly its S3 bucket |  |   | Write | 
|   [DeleteServer](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DeleteServer.html)  | Grants permission to delete the specified server with its corresponding CloudFormation stack and possibly the S3 bucket |  |   | Write | 
|   [DescribeAccountAttributes](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DescribeAccountAttributes.html)  | Grants permission to describe the service limits for the user's account |  |   | List | 
|   [DescribeBackups](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DescribeBackups.html)  | Grants permission to describe a single backup, all backups of a specified server or all backups of the user's account |  |   | List | 
|   [DescribeEvents](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DescribeEvents.html)  | Grants permission to describe all events of the specified server |  |   | List | 
|   [DescribeNodeAssociationStatus](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DescribeNodeAssociationStatus.html)  | Grants permission to describe the association status for the specified node token and the specified server |  |   | List | 
|   [DescribeServers](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DescribeServers.html)  | Grants permission to describe the specified server or all servers of the user's account |  |   | List | 
|   [DisassociateNode](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_DisassociateNode.html)  | Grants permission to disassociate a specified node from a server |  |   | Write | 
|   [ExportServerEngineAttribute](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_ExportServerEngineAttribute.html)  | Grants permission to export an engine attribute from a server |  |   | Read | 
|   [ListTagsForResource](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_ListTagsForResource.html)  | Grants permission to list the tags that are applied to the specified server or backup |  |   | Read | 
|   [RestoreServer](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_RestoreServer.html)  | Grants permission to apply a backup to specified server. Possibly swaps out the ec2-instance if specified |  |   | Write | 
|   [StartMaintenance](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_StartMaintenance.html)  | Grants permission to start the server maintenance immediately |  |   | Write | 
|   [TagResource](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_TagResource.html)  | Grants permission to apply tags to the specified server or backup |  |   | Tagging, Write | 
|   [UntagResource](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_UntagResource.html)  | Grants permission to remove tags from the specified server or backup |  |   | Tagging, Write | 
|   [UpdateServer](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_UpdateServer.html)  | Grants permission to update general server settings |  |   | Write | 
|   [UpdateServerEngineAttributes](https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_UpdateServerEngineAttributes.html)  | Grants permission to update server settings specific to the configuration management type |  |   | Write | 

## Resource types defined by AWS OpsWorks Configuration Management
<a name="list_opsworks-cm-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [backup](https://docs.aws.amazon.com/opsworks/latest/userguide/security_iam_service-with-iam-opscm.html)  | arn:${Partition}:opsworks-cm::${Account}:backup/${ServerName}-{Date-and-Time-Stamp-of-Backup} |   | 
|  [server](https://docs.aws.amazon.com/opsworks/latest/userguide/security_iam_service-with-iam-opscm.html)  | arn:${Partition}:opsworks-cm::${Account}:server/${ServerName}/${UniqueId} |   | 

## Condition keys for AWS OpsWorks Configuration Management
<a name="list_opsworks-cm-policy-keys"></a>

AWS OpsWorks Configuration Management has no service-specific condition keys that can be used in the `Condition` element of policy statements.