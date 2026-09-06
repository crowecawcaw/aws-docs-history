

# Actions, resources, and condition keys for AWS IQ Permissions
<a name="list_iq-permission"></a>

AWS IQ Permissions (service prefix: `iq-permission`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-iq/latest/experts-user-guide/set-up-expert-account-permissions-to-use-aws-iq.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iq-permission/iq-permission.json) for this service.

**Topics**
+ [Actions defined by AWS IQ Permissions](#list_iq-permission-actions-as-permissions)
+ [Resource types defined by AWS IQ Permissions](#list_iq-permission-resources-for-iam-policies)
+ [Condition keys for AWS IQ Permissions](#list_iq-permission-policy-keys)

## Actions defined by AWS IQ Permissions
<a name="list_iq-permission-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ApproveAccessGrant](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to approve a permission request
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ApprovePermissionRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to approve a permission request
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssumePermissionRole](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to obtain a set of temporary security credentials for experts which they can use to access buyers' AWS resources
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePermissionRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to create a permission request
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetPermissionRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to get a permission request
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPermissionRequests](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to list permission requests
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Read

- **   [RejectPermissionRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to reject a permission request
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RevokePermissionRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to revoke a permission request which was previously approved
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write

- **   [WithdrawPermissionRequest](https://aws.amazon.com/iq/)  **
  - **Description:** Grants permission to withdraw a permission request that has not been approved or declined
  - **Resource types (\*required):** [permission\*](#list_iq-permission-resource-permission)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS IQ Permissions
<a name="list_iq-permission-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [permission](https://aws.amazon.com/iq/)  | arn:${Partition}:iq-permission:${Region}::permission/${PermissionRequestId} |   | 

## Condition keys for AWS IQ Permissions
<a name="list_iq-permission-policy-keys"></a>

AWS IQ Permissions has no service-specific condition keys that can be used in the `Condition` element of policy statements.