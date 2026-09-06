

# Actions, resources, and condition keys for AWS Migration Hub
<a name="list_migration-hub"></a>

AWS Migration Hub (service prefix: `mgh`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/migrationhub/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/migrationhub/latest/ug/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/migrationhub/latest/ug/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mgh/mgh.json) for this service.

**Topics**
+ [API operations defined by AWS Migration Hub](#list_migration-hub-operations)
+ [Actions defined by AWS Migration Hub](#list_migration-hub-actions-as-permissions)
+ [Resource types defined by AWS Migration Hub](#list_migration-hub-resources-for-iam-policies)
+ [Condition keys for AWS Migration Hub](#list_migration-hub-policy-keys)

## API operations defined by AWS Migration Hub
<a name="list_migration-hub-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_migration-hub-actions-as-permissions).




- **   AssociateCreatedArtifact  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:AssociateCreatedArtifact](#list_migration-hub-action-AssociateCreatedArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateDiscoveredResource  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:AssociateDiscoveredResource](#list_migration-hub-action-AssociateDiscoveredResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateSourceResource  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:AssociateSourceResource](#list_migration-hub-action-AssociateSourceResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProgressUpdateStream  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:CreateProgressUpdateStream](#list_migration-hub-action-CreateProgressUpdateStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProgressUpdateStream  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:DeleteProgressUpdateStream](#list_migration-hub-action-DeleteProgressUpdateStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeApplicationState  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:DescribeApplicationState](#list_migration-hub-action-DescribeApplicationState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMigrationTask  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:DescribeMigrationTask](#list_migration-hub-action-DescribeMigrationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateCreatedArtifact  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:DisassociateCreatedArtifact](#list_migration-hub-action-DisassociateCreatedArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDiscoveredResource  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:DisassociateDiscoveredResource](#list_migration-hub-action-DisassociateDiscoveredResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSourceResource  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:DisassociateSourceResource](#list_migration-hub-action-DisassociateSourceResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ImportMigrationTask  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ImportMigrationTask](#list_migration-hub-action-ImportMigrationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListApplicationStates  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListApplicationStates](#list_migration-hub-action-ListApplicationStates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCreatedArtifacts  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListCreatedArtifacts](#list_migration-hub-action-ListCreatedArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDiscoveredResources  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListDiscoveredResources](#list_migration-hub-action-ListDiscoveredResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMigrationTaskUpdates  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListMigrationTaskUpdates](#list_migration-hub-action-ListMigrationTaskUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMigrationTasks  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListMigrationTasks](#list_migration-hub-action-ListMigrationTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProgressUpdateStreams  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListProgressUpdateStreams](#list_migration-hub-action-ListProgressUpdateStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceResources  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:ListSourceResources](#list_migration-hub-action-ListSourceResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   NotifyApplicationState  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:NotifyApplicationState](#list_migration-hub-action-NotifyApplicationState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   NotifyMigrationTaskState  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:NotifyMigrationTaskState](#list_migration-hub-action-NotifyMigrationTaskState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourceAttributes  **
  - **SDK client:** mgh
  - **IAM action:**  [mgh:PutResourceAttributes](#list_migration-hub-action-PutResourceAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateHomeRegionControl  **
  - **SDK client:** migrationhub-config
  - **IAM action:**  [mgh:CreateHomeRegionControl](#list_migration-hub-action-CreateHomeRegionControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHomeRegionControl  **
  - **SDK client:** migrationhub-config
  - **IAM action:**  [mgh:DeleteHomeRegionControl](#list_migration-hub-action-DeleteHomeRegionControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeHomeRegionControls  **
  - **SDK client:** migrationhub-config
  - **IAM action:**  [mgh:DescribeHomeRegionControls](#list_migration-hub-action-DescribeHomeRegionControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetHomeRegion  **
  - **SDK client:** migrationhub-config
  - **IAM action:**  [mgh:GetHomeRegion](#list_migration-hub-action-GetHomeRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Migration Hub
<a name="list_migration-hub-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptConnection](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to accept a connection
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-aws_TagKeys)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** Write

- **   [AssociateAutomationUnitRole](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateAutomationUnitRole.html)  **
  - **Description:** Grants permission to associate an IAM role to an automation unit
  - **Resource types (\*required):** [AutomationUnitResource\*](#list_migration-hub-resource-AutomationUnitResource)
  - **Condition keys:** [mgh:AutomationUnitResourceAutomationUnitArn](#list_migration-hub-mgh_AutomationUnitResourceAutomationUnitArn)
  - **Access level:** Write

- **   [AssociateCreatedArtifact](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateCreatedArtifact.html)  **
  - **Description:** Grants permission to associate a given AWS artifact to a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateDiscoveredResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateDiscoveredResource.html)  **
  - **Description:** Grants permission to associate a given ADS resource to a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateSourceResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AssociateSourceResource.html)  **
  - **Description:** Grants permission to associate source resource
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchAssociateIamRoleWithConnection](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to batch-associate IAM roles with a connection
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** Write

- **   [BatchDisassociateIamRoleFromConnection](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to batch-disassociate IAM roles from a connection
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** Write

- **   [CreateAutomationRun](https://docs.aws.amazon.com/migrationhub/latest/ug/API_CreateAutomationRun.html)  **
  - **Description:** Grants permission to create an automation unit run
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAutomationUnit](https://docs.aws.amazon.com/migrationhub/latest/ug/API_CreateAutomationUnit.html)  **
  - **Description:** Grants permission to create an automation unit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateHomeRegionControl](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.html)  **
  - **Description:** Grants permission to create a Migration Hub Home Region Control
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProgressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/API_CreateProgressUpdateStream.html)  **
  - **Description:** Grants permission to create a ProgressUpdateStream
  - **Resource types (\*required):** [progressUpdateStream\*](#list_migration-hub-resource-progressUpdateStream)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAutomationRun](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DeleteAutomationRun.html)  **
  - **Description:** Grants permission to delete an automation unit run
  - **Resource types (\*required):** [AutomationRunResource\*](#list_migration-hub-resource-AutomationRunResource)
  - **Condition keys:** [mgh:AutomationRunResourceRunID](#list_migration-hub-mgh_AutomationRunResourceRunID)
  - **Access level:** Write

- **   [DeleteAutomationUnit](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DeleteAutomationUnit.html)  **
  - **Description:** Grants permission to delete an automation unit
  - **Resource types (\*required):** [AutomationUnitResource\*](#list_migration-hub-resource-AutomationUnitResource)
  - **Condition keys:** [mgh:AutomationUnitResourceAutomationUnitArn](#list_migration-hub-mgh_AutomationUnitResourceAutomationUnitArn)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** Write

- **   [DeleteHomeRegionControl](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.html)  **
  - **Description:** Grants permission to delete a Migration Hub Home Region Control
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProgressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DeleteProgressUpdateStream.html)  **
  - **Description:** Grants permission to delete a ProgressUpdateStream
  - **Resource types (\*required):** [progressUpdateStream\*](#list_migration-hub-resource-progressUpdateStream)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeApplicationState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DescribeApplicationState.html)  **
  - **Description:** Grants permission to get an Application Discovery Service Application's state
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAutomationRun](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DescribeAutomationRun.html)  **
  - **Description:** Grants permission to describe an automation unit run
  - **Resource types (\*required):** [AutomationRunResource\*](#list_migration-hub-resource-AutomationRunResource)
  - **Condition keys:** [mgh:AutomationRunResourceRunID](#list_migration-hub-mgh_AutomationRunResourceRunID)
  - **Access level:** Read

- **   [DescribeAutomationUnit](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DescribeAutomationUnit.html)  **
  - **Description:** Grants permission to describe an automation unit
  - **Resource types (\*required):** [AutomationUnitResource\*](#list_migration-hub-resource-AutomationUnitResource)
  - **Condition keys:** [mgh:AutomationUnitResourceAutomationUnitArn](#list_migration-hub-mgh_AutomationUnitResourceAutomationUnitArn)
  - **Access level:** Read

- **   [DescribeHomeRegionControls](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.html)  **
  - **Description:** Grants permission to list Home Region Controls
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DescribeMigrationTask.html)  **
  - **Description:** Grants permission to describe a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateAutomationUnitRole](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateAutomationUnitRole.html)  **
  - **Description:** Grants permission to disassociate an IAM role from an automation unit
  - **Resource types (\*required):** [AutomationUnitResource\*](#list_migration-hub-resource-AutomationUnitResource)
  - **Condition keys:** [mgh:AutomationUnitResourceAutomationUnitArn](#list_migration-hub-mgh_AutomationUnitResourceAutomationUnitArn)
  - **Access level:** Write

- **   [DisassociateCreatedArtifact](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateCreatedArtifact.html)  **
  - **Description:** Grants permission to disassociate a given AWS artifact from a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateDiscoveredResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateDiscoveredResource.html)  **
  - **Description:** Grants permission to disassociate a given ADS resource from a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateSourceResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_DisassociateSourceResource.html)  **
  - **Description:** Grants permission to diassociate source resource
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetConnection](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to get a connection
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** Read

- **   [GetHomeRegion](https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_GetHomeRegion.html)  **
  - **Description:** Grants permission to get the Migration Hub Home Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportMigrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ImportMigrationTask.html)  **
  - **Description:** Grants permission to import a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListApplicationStates](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListApplicationStates.html)  **
  - **Description:** Grants permission to list Application statuses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationRuns](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListAutomationRuns.html)  **
  - **Description:** Grants permission to list automation unit runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationUnits](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListAutomationUnits.html)  **
  - **Description:** Grants permission to list automation units
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectionRoles](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to list connection roles
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** List

- **   [ListConnections](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to list connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCreatedArtifacts](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListCreatedArtifacts.html)  **
  - **Description:** Grants permission to list associated created artifacts for a MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDiscoveredResources](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListDiscoveredResources.html)  **
  - **Description:** Grants permission to list associated ADS resources from MigrationTask
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMigrationTaskUpdates](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListMigrationTaskUpdates.html)  **
  - **Description:** Grants permission to list migration tasks updates
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMigrationTasks](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListMigrationTasks.html)  **
  - **Description:** Grants permission to list MigrationTasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProgressUpdateStreams](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListProgressUpdateStreams.html)  **
  - **Description:** Grants permission to to list ProgressUpdateStreams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSourceResources](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListSourceResources.html)  **
  - **Description:** Grants permission to list source resources
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [NotifyApplicationState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_NotifyApplicationState.html)  **
  - **Description:** Grants permission to update an Application Discovery Service Application's state
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [NotifyMigrationTaskState](https://docs.aws.amazon.com/migrationhub/latest/ug/API_NotifyMigrationTaskState.html)  **
  - **Description:** Grants permission to notify latest MigrationTask state
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourceAttributes](https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html)  **
  - **Description:** Grants permission to put ResourceAttributes
  - **Resource types (\*required):** [migrationTask\*](#list_migration-hub-resource-migrationTask)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectConnection](https://docs.aws.amazon.com/mhj/latest/userguide/account-connections.html)  **
  - **Description:** Grants permission to reject a connection
  - **Resource types (\*required):** [ConnectionResource\*](#list_migration-hub-resource-ConnectionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migration-hub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_migration-hub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:TagKeys](#list_migration-hub-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Migration Hub
<a name="list_migration-hub-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AutomationRunResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AutomationRunResource.html)  | arn:${Partition}:mgh:${Region}:${Account}:automation-run/${RunID} | [mgh:AutomationRunResourceRunID](#list_migration-hub-mgh_AutomationRunResourceRunID) | 
|  [AutomationUnitResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_AutomationUnitResource.html)  | arn:${Partition}:mgh:${Region}:${Account}:automation-unit/${AutomationUnitId} | [mgh:AutomationUnitResourceAutomationUnitArn](#list_migration-hub-mgh_AutomationUnitResourceAutomationUnitArn) | 
|  [ConnectionResource](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ConnectionResource.html)  | arn:${Partition}:mgh:${Region}:${Account}:${ConnectionArn} | [aws:ResourceTag/${TagKey}](#list_migration-hub-aws_ResourceTag___TagKey_)<br />[mgh:ConnectionResourceConnectionArn](#list_migration-hub-mgh_ConnectionResourceConnectionArn) | 
|  [migrationTask](https://docs.aws.amazon.com/migrationhub/latest/ug/API_MigrationTask.html)  | arn:${Partition}:mgh:${Region}:${Account}:progressUpdateStream/${Stream}/migrationTask/${Task} |   | 
|  [progressUpdateStream](https://docs.aws.amazon.com/migrationhub/latest/ug/API_ProgressUpdateStreamSummary.html)  | arn:${Partition}:mgh:${Region}:${Account}:progressUpdateStream/${Stream} |   | 

## Condition keys for AWS Migration Hub
<a name="list_migration-hub-policy-keys"></a>

AWS Migration Hub defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 
|   [mgh:AutomationRunResourceRunID](https://docs.aws.amazon.com/migrationhub/latest/ug/ContextKeys_AutomationRunResourceRunID.html)  | AutomationRunResource resource runID identifier | String | 
|   [mgh:AutomationUnitResourceAutomationUnitArn](https://docs.aws.amazon.com/migrationhub/latest/ug/ContextKeys_AutomationUnitResourceAutomationUnitArn.html)  | AutomationUnitResource resource automationUnitArn identifier | ARN | 
|   [mgh:ConnectionResourceConnectionArn](https://docs.aws.amazon.com/migrationhub/latest/ug/security_iam_service-with-iam-id-based-policies-conditionkeys.html#condition-connectionresourceconnectionarn)  | ConnectionResource resource connectionArn identifier | String | 