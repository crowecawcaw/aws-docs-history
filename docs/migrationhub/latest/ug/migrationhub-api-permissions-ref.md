AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# AWS Migration Hub API Permissions: Actions

and Resources Reference

When you are setting up [Access control](auth-and-access-control.md#access-control "auth-and-access-control.md#access-control") and writing a permissions policy that you can attach to an IAM identity
(identity-based policies), you can use the following table
as a reference. The table lists
each Migration Hub API operation, the
corresponding actions for which you can grant permissions to perform the action, and the
AWS resource for which you can grant the permissions. You specify the actions in the
policy's `Action` field, and you specify the resource value in the policy's
`Resource` field.

###### Note

To specify an action, use the `mgh:` prefix followed by the API
operation name (for example, `mgh:CreateProgressUpdateStream`).

Use the scroll bars to see the rest of the table.

AWS Migration Hub API and Required
Permissions for Actions | Migration Hub API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [AssociateCreatedArtifact](API_AssociateCreatedArtifact.md "API_AssociateCreatedArtifact.md") | `mgh:AssociateCreatedArtifact` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [AssociateDiscoveredResource](API_AssociateDiscoveredResource.md "API_AssociateDiscoveredResource.md") | `mgh:AssociateDiscoveredResource` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [CreateProgressUpdateStream](API_CreateProgressUpdateStream.md "API_CreateProgressUpdateStream.md") | `mgh:CreateProgressUpdateStream` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`` |
| [DeleteProgressUpdateStream](API_DeleteProgressUpdateStream.md "API_DeleteProgressUpdateStream.md") | `mgh:DeleteProgressUpdateStream` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`` |
| [DescribeApplicationState](API_DescribeApplicationState.md "API_DescribeApplicationState.md") | `mgh:DescribeApplicationState` | `*` |
| [DescribeMigrationTask](API_DescribeMigrationTask.md "API_DescribeMigrationTask.md") | `mgh:DescribeMigrationTask` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [DisassociateCreatedArtifact](API_DisassociateCreatedArtifact.md "API_DisassociateCreatedArtifact.md") | `mgh:DisassociateCreatedArtifact` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [DisassociateDiscoveredResource](API_DisassociateDiscoveredResource.md "API_DisassociateDiscoveredResource.md") | `mgh:DisassociateDiscoveredResource` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [ImportMigrationTask](API_ImportMigrationTask.md "API_ImportMigrationTask.md") | `mgh:ImportMigrationTask` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [ListCreatedArtifacts](API_ListCreatedArtifacts.md "API_ListCreatedArtifacts.md") | `mgh:ListCreatedArtifacts` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [ListDiscoveredResources](API_ListDiscoveredResources.md "API_ListDiscoveredResources.md") | `mgh:ListDiscoveredResources` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [ListMigrationTasks](API_ListMigrationTasks.md "API_ListMigrationTasks.md") | `mgh:ListMigrationTasks` | `*` |
| [ListProgressUpdateStreams](API_ListProgressUpdateStreams.md "API_ListProgressUpdateStreams.md") | `mgh:ListProgressUpdateStreams` | `*` |
| [NotifyApplicationState](API_NotifyApplicationState.md "API_NotifyApplicationState.md") | `mgh:NotifyApplicationState` | `*` |
| [NotifyMigrationTaskState](API_NotifyMigrationTaskState.md "API_NotifyMigrationTaskState.md") | `mgh:NotifyMigrationTaskState` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |
| [PutResourceAttributes](API_PutResourceAttributes.md "API_PutResourceAttributes.md") | `mgh:PutResourceAttributes` | `arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id``<br>or<br>`arn:aws:mgh:`region`:`account-id`:ProgressUpdateStreamName/`resource-id`/*` |

AWS Migration Hub Home Region API and Required
Permissions for Actions | Migration Hub API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [CreateHomeRegionControl](../../../migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.md "../../../migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.md") | `mgh:CreateHomeRegionControl` | `*` |
| [DescribeHomeRegionControls](../../../migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.md "../../../migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.md") | `mgh:DescribeHomeRegionControls` | `*` |
| [GetHomeRegion](../../../migrationhub-home-region/latest/APIReference/API_GetHomeRegion.md "../../../migrationhub-home-region/latest/APIReference/API_GetHomeRegion.md") | `mgh:GetHomeRegion` | `*` |

## Related Topics

- [Access control](auth-and-access-control.md#access-control "auth-and-access-control.md#access-control")
