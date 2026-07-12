# Actions, resources, and condition keys for AWS Identity Sync

AWS Identity Sync (service prefix: `identity-sync`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md").
- View a list of the [API operations available for
  this service](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../singlesignon/latest/userguide/iam-auth-access.md "../../../singlesignon/latest/userguide/iam-auth-access.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/identity-sync/identity-sync.json "https://servicereference.us-east-1.amazonaws.com/v1/identity-sync/identity-sync.json") for this service.

###### Topics

- [Actions defined by AWS Identity Sync](#list_identity-sync-actions-as-permissions "#list_identity-sync-actions-as-permissions")
- [Permission-only actions for AWS Identity Sync](#list_identity-sync-permission-only-actions "#list_identity-sync-permission-only-actions")
- [Resource types defined by AWS Identity Sync](#list_identity-sync-resources-for-iam-policies "#list_identity-sync-resources-for-iam-policies")
- [Condition keys for AWS Identity Sync](#list_identity-sync-policy-keys "#list_identity-sync-policy-keys")

## Actions defined by AWS Identity Sync

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                        | Description                                                                                      | Resource types (\*required)                                                                                                  | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [CreateSyncFilter](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")  | Grants permission to create a sync filter on the sync profile                                    | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [CreateSyncProfile](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md") | Grants permission to create a sync profile for the identity source                               |                                                                                                                              |                | Write        |
| [CreateSyncTarget](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")  | Grants permission to create a sync target for the identity source                                | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [DeleteSyncFilter](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")  | Grants permission to delete a sync filter from the sync profile                                  | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [DeleteSyncProfile](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md") | Grants permission to delete a sync profile from the source                                       | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [DeleteSyncTarget](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")  | Grants permission to delete a sync target from the source                                        | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [SyncTargetResource\*](#list_identity-sync-resource-SyncTargetResource "#list_identity-sync-resource-SyncTargetResource")                                      |                                                                                                  |
| [GetSyncProfile](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")    | Grants permission to retrieve a sync profile by using a sync profile name                        | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Read         |
| [GetSyncTarget](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")     | Grants permission to retrieve a sync target from the sync profile                                | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Read         |
| [SyncTargetResource\*](#list_identity-sync-resource-SyncTargetResource "#list_identity-sync-resource-SyncTargetResource")                                      |                                                                                                  |
| [ListSyncFilters](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")   | Grants permission to list the sync filters from the sync profile                                 | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | List         |
| [StartSync](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")         | Grants permission to start a sync process or to resume a sync process that was previously paused | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [StopSync](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")          | Grants permission to stop any planned sync process in the sync schedule from starting            | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [UpdateSyncTarget](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")  | Grants permission to update a sync target on the sync profile                                    | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Write        |
| [SyncTargetResource\*](#list_identity-sync-resource-SyncTargetResource "#list_identity-sync-resource-SyncTargetResource")                                      |                                                                                                  |

## Permission-only actions for AWS Identity Sync

The following actions are defined by AWS Identity Sync but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                  | Description                                                           | Resource types (\*required)                                                                                                  | Condition keys | Access level                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| [AllowVendedLogDeliveryForResource](../../../singlesignon/latest/userguide/logging-ad-sync-errors.md "../../../singlesignon/latest/userguide/logging-ad-sync-errors.md") | Grants permission to configure vended log delivery for a Sync Profile | [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource "#list_identity-sync-resource-SyncProfileResource") |                | Permissions management, Write |

## Resource types defined by AWS Identity Sync

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                   | ARN                                                                                             | Condition keys |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------- |
| [SyncProfileResource](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md") | arn:${Partition}:identity-sync:${Region}:${Account}:profile/${SyncProfileName}                  |                |
| [SyncTargetResource](../../../singlesignon/latest/userguide/provision-users-groups-AD.md "../../../singlesignon/latest/userguide/provision-users-groups-AD.md")  | arn:${Partition}:identity-sync:${Region}:${Account}:target/${SyncProfileName}/${SyncTargetName} |                |

## Condition keys for AWS Identity Sync

AWS Identity Sync has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
