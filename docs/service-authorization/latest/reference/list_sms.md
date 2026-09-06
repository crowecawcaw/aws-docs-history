

# Actions, resources, and condition keys for AWS Server Migration Service
<a name="list_sms"></a>

AWS Server Migration Service (service prefix: `sms`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/server-migration-service/latest/userguide/SMS_setup.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/server-migration-service/latest/userguide/SMS_setup.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sms/sms.json) for this service.

**Topics**
+ [Actions defined by AWS Server Migration Service](#list_sms-actions-as-permissions)
+ [Permission-only actions for AWS Server Migration Service](#list_sms-permission-only-actions)
+ [Resource types defined by AWS Server Migration Service](#list_sms-resources-for-iam-policies)
+ [Condition keys for AWS Server Migration Service](#list_sms-policy-keys)

## Actions defined by AWS Server Migration Service
<a name="list_sms-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateApp](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_CreateApp.html)  | Grants permission to create an application configuration to migrate on-premise application onto AWS |  |   | Write | 
|   [CreateReplicationJob](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_CreateReplicationJob.html)  | Grants permission to create a job to migrate on-premise server onto AWS |  |   | Write | 
|   [DeleteApp](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DeleteApp.html)  | Grants permission to delete an existing application configuration |  |   | Write | 
|   [DeleteAppLaunchConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DeleteAppLaunchConfiguration.html)  | Grants permission to delete launch configuration for an existing application |  |   | Write | 
|   [DeleteAppReplicationConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DeleteAppReplicationConfiguration.html)  | Grants permission to delete replication configuration for an existing application |  |   | Write | 
|   [DeleteAppValidationConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DeleteAppValidationConfiguration.html)  | Grants permission to delete validation configuration for an existing application |  |   | Write | 
|   [DeleteReplicationJob](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DeleteReplicationJob.html)  | Grants permission to delete an existing job to migrate on-premise server onto AWS |  |   | Write | 
|   [DeleteServerCatalog](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DeleteServerCatalog.html)  | Grants permission to delete the complete list of on-premise servers gathered into AWS |  |   | Write | 
|   [DisassociateConnector](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_DisassociateConnector.html)  | Grants permission to disassociate a connector that has been associated |  |   | Write | 
|   [GenerateChangeSet](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GenerateChangeSet.html)  | Grants permission to generate a changeSet for the CloudFormation stack of an application |  |   | Write | 
|   [GenerateTemplate](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GenerateTemplate.html)  | Grants permission to generate a CloudFormation template for an existing application |  |   | Write | 
|   [GetApp](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetApp.html)  | Grants permission to get the configuration and statuses for an existing application |  |   | Read | 
|   [GetAppLaunchConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetAppLaunchConfiguration.html)  | Grants permission to get launch configuration for an existing application |  |   | Read | 
|   [GetAppReplicationConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetAppReplicationConfiguration.html)  | Grants permission to get replication configuration for an existing application |  |   | Read | 
|   [GetAppValidationConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetAppValidationConfiguration.html)  | Grants permission to get validation configuration for an existing application |  |   | Read | 
|   [GetAppValidationOutput](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetAppValidationOutput.html)  | Grants permission to get notification sent from application validation script. |  |   | Read | 
|   [GetConnectors](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetConnectors.html)  | Grants permission to get all connectors that have been associated |  |   | Read | 
|   [GetReplicationJobs](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetReplicationJobs.html)  | Grants permission to get all existing jobs to migrate on-premise servers onto AWS |  |   | Read | 
|   [GetReplicationRuns](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetReplicationRuns.html)  | Grants permission to get all runs for an existing job |  |   | Read | 
|   [GetServers](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_GetServers.html)  | Grants permission to get all servers that have been imported |  |   | Read | 
|   [ImportAppCatalog](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_ImportAppCatalog.html)  | Grants permission to import application catalog from AWS Application Discovery Service |  |   | Write | 
|   [ImportServerCatalog](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_ImportServerCatalog.html)  | Grants permission to gather a complete list of on-premise servers |  |   | Write | 
|   [LaunchApp](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_LaunchApp.html)  | Grants permission to create and launch a CloudFormation stack for an existing application |  |   | Write | 
|   [ListApps](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_ListAppss.html)  | Grants permission to get a list of summaries for existing applications |  |   | List | 
|   [NotifyAppValidationOutput](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_NotifyAppValidationOutput.html)  | Grants permission to send notification for application validation script |  |   | Write | 
|   [PutAppLaunchConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_PutAppLaunchConfiguration.html)  | Grants permission to create or update launch configuration for an existing application |  |   | Write | 
|   [PutAppReplicationConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_PutAppReplicationConfiguration.html)  | Grants permission to create or update replication configuration for an existing application |  |   | Write | 
|   [PutAppValidationConfiguration](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_PutAppValidationConfiguration.html)  | Grants permission to put validation configuration for an existing application |  |   | Write | 
|   [StartAppReplication](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_StartAppReplication.html)  | Grants permission to create and start replication jobs for an existing application |  |   | Write | 
|   [StartOnDemandAppReplication](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_StartOnDemandAppReplication.html)  | Grants permission to start a replication run for an existing application |  |   | Write | 
|   [StartOnDemandReplicationRun](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_StartOnDemandReplicationRun.html)  | Grants permission to start a replication run for an existing replication job |  |   | Write | 
|   [StopAppReplication](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_StopAppReplication.html)  | Grants permission to stop and delete replication jobs for an existing application |  |   | Write | 
|   [TerminateApp](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_TerminateApp.html)  | Grants permission to terminate the CloudFormation stack for an existing application |  |   | Write | 
|   [UpdateApp](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_UpdateApp.html)  | Grants permission to update an existing application configuration |  |   | Write | 
|   [UpdateReplicationJob](https://docs.aws.amazon.com/server-migration-service/latest/APIReference/API_UpdateReplicationJob.html)  | Grants permission to update an existing job to migrate on-premise server onto AWS |  |   | Write | 

## Permission-only actions for AWS Server Migration Service
<a name="list_sms-permission-only-actions"></a>

The following actions are defined by AWS Server Migration Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   GetMessages  | Grants permission to gets messages from AWS Server Migration Service to Server Migration Connector |  |   | Read | 
|   SendMessage  | Grants permission to send message from Server Migration Connector to AWS Server Migration Service |  |   | Write | 

## Resource types defined by AWS Server Migration Service
<a name="list_sms-resources-for-iam-policies"></a>

AWS Server Migration Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Server Migration Service
<a name="list_sms-policy-keys"></a>

AWS Server Migration Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.