

# Actions, resources, and condition keys for AWS Identity Sync
<a name="list_identity-sync"></a>

AWS Identity Sync (service prefix: `identity-sync`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/identity-sync/identity-sync.json) for this service.

**Topics**
+ [Actions defined by AWS Identity Sync](#list_identity-sync-actions-as-permissions)
+ [Permission-only actions for AWS Identity Sync](#list_identity-sync-permission-only-actions)
+ [Resource types defined by AWS Identity Sync](#list_identity-sync-resources-for-iam-policies)
+ [Condition keys for AWS Identity Sync](#list_identity-sync-policy-keys)

## Actions defined by AWS Identity Sync
<a name="list_identity-sync-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSyncFilter](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to create a sync filter on the sync profile
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSyncProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to create a sync profile for the identity source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSyncTarget](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to create a sync target for the identity source
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSyncFilter](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to delete a sync filter from the sync profile
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSyncProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to delete a sync profile from the source
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSyncTarget](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to delete a sync target from the source
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource) / **Condition keys:**  
  - **Resource types (\*required):** [SyncTargetResource\*](#list_identity-sync-resource-SyncTargetResource) / **Condition keys:**  
  - **Access level:** Write

- **   [GetSyncProfile](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to retrieve a sync profile by using a sync profile name
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSyncTarget](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to retrieve a sync target from the sync profile
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource) / **Condition keys:**  
  - **Resource types (\*required):** [SyncTargetResource\*](#list_identity-sync-resource-SyncTargetResource) / **Condition keys:**  
  - **Access level:** Read

- **   [ListSyncFilters](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to list the sync filters from the sync profile
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** List

- **   [StartSync](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to start a sync process or to resume a sync process that was previously paused
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopSync](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to stop any planned sync process in the sync schedule from starting
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSyncTarget](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  **
  - **Description:** Grants permission to update a sync target on the sync profile
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource) / **Condition keys:**  
  - **Resource types (\*required):** [SyncTargetResource\*](#list_identity-sync-resource-SyncTargetResource) / **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Identity Sync
<a name="list_identity-sync-permission-only-actions"></a>

The following actions are defined by AWS Identity Sync but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/singlesignon/latest/userguide/logging-ad-sync-errors.html)  **
  - **Description:** Grants permission to configure vended log delivery for a Sync Profile
  - **Resource types (\*required):** [SyncProfileResource\*](#list_identity-sync-resource-SyncProfileResource)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Identity Sync
<a name="list_identity-sync-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [SyncProfileResource](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  | arn:${Partition}:identity-sync:${Region}:${Account}:profile/${SyncProfileName} |   | 
|  [SyncTargetResource](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-users-groups-AD.html)  | arn:${Partition}:identity-sync:${Region}:${Account}:target/${SyncProfileName}/${SyncTargetName} |   | 

## Condition keys for AWS Identity Sync
<a name="list_identity-sync-policy-keys"></a>

AWS Identity Sync has no service-specific condition keys that can be used in the `Condition` element of policy statements.