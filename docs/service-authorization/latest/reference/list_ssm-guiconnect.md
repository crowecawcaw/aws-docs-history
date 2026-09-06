

# Actions, resources, and condition keys for AWS Systems Manager GUI Connect
<a name="list_ssm-guiconnect"></a>

AWS Systems Manager GUI Connect (service prefix: `ssm-guiconnect`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssm-guiconnect/ssm-guiconnect.json) for this service.

**Topics**
+ [API operations defined by AWS Systems Manager GUI Connect](#list_ssm-guiconnect-operations)
+ [Actions defined by AWS Systems Manager GUI Connect](#list_ssm-guiconnect-actions-as-permissions)
+ [Permission-only actions for AWS Systems Manager GUI Connect](#list_ssm-guiconnect-permission-only-actions)
+ [Resource types defined by AWS Systems Manager GUI Connect](#list_ssm-guiconnect-resources-for-iam-policies)
+ [Condition keys for AWS Systems Manager GUI Connect](#list_ssm-guiconnect-policy-keys)

## API operations defined by AWS Systems Manager GUI Connect
<a name="list_ssm-guiconnect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ssm-guiconnect-actions-as-permissions).




- **   DeleteConnectionRecordingPreferences  **
  - **IAM action:**  [ssm-guiconnect:DeleteConnectionRecordingPreferences](#list_ssm-guiconnect-action-DeleteConnectionRecordingPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetConnectionRecordingPreferences  **
  - **IAM action:**  [ssm-guiconnect:GetConnectionRecordingPreferences](#list_ssm-guiconnect-action-GetConnectionRecordingPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateConnectionRecordingPreferences  **
  - **IAM action:**  [ssm-guiconnect:UpdateConnectionRecordingPreferences](#list_ssm-guiconnect-action-UpdateConnectionRecordingPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Systems Manager GUI Connect
<a name="list_ssm-guiconnect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DeleteConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_DeleteConnectionRecordingPreferences.html)  | Grants permission to remove GUI Connect connection recording preferences |  |   | Write | 
|   [GetConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_GetConnectionRecordingPreferences.html)  | Grants permission to get GUI Connect connection recording preferences |  |   | Read | 
|   [UpdateConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_UpdateConnectionRecordingPreferences.html)  | Grants permission to update GUI Connect connection recording preferences |  |   | Write | 

## Permission-only actions for AWS Systems Manager GUI Connect
<a name="list_ssm-guiconnect-permission-only-actions"></a>

The following actions are defined by AWS Systems Manager GUI Connect but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CancelConnection](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html)  | Grants permission to terminate a GUI Connect connection |  |   | Write | 
|   [GetConnection](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html)  | Grants permission to get the metadata for a GUI Connect connection |  |   | Read | 
|   [ListConnections](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html)  | Grants permission to list the metadata for GUI Connect connections |  |   | List | 
|   [StartConnection](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html)  | Grants permission to start a GUI Connect connection |  |   | Write | 

## Resource types defined by AWS Systems Manager GUI Connect
<a name="list_ssm-guiconnect-resources-for-iam-policies"></a>

AWS Systems Manager GUI Connect does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Systems Manager GUI Connect
<a name="list_ssm-guiconnect-policy-keys"></a>

AWS Systems Manager GUI Connect has no service-specific condition keys that can be used in the `Condition` element of policy statements.