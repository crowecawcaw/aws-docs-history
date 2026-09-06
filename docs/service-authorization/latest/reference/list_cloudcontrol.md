

# Actions, resources, and condition keys for AWS Cloud Control API
<a name="list_cloudcontrol"></a>

AWS Cloud Control API (service prefix: `cloudformation`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudformation/cloudformation.json) for this service.

**Topics**
+ [API operations defined by AWS Cloud Control API](#list_cloudcontrol-operations)
+ [Actions defined by AWS Cloud Control API](#list_cloudcontrol-actions-as-permissions)
+ [Resource types defined by AWS Cloud Control API](#list_cloudcontrol-resources-for-iam-policies)
+ [Condition keys for AWS Cloud Control API](#list_cloudcontrol-policy-keys)

## API operations defined by AWS Cloud Control API
<a name="list_cloudcontrol-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudcontrol-actions-as-permissions).




- **   CancelResourceRequest  **
  - **IAM action:**  [cloudformation:CancelResourceRequest](#list_cloudcontrol-action-CancelResourceRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResource  **
  - **IAM action:**  [cloudformation:CreateResource](#list_cloudcontrol-action-CreateResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   DeleteResource  **
  - **IAM action:**  [cloudformation:DeleteResource](#list_cloudcontrol-action-DeleteResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   GetResource  **
  - **IAM action:**  [cloudformation:GetResource](#list_cloudcontrol-action-GetResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   GetResourceRequestStatus  **
  - **IAM action:**  [cloudformation:GetResourceRequestStatus](#list_cloudcontrol-action-GetResourceRequestStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResourceRequests  **
  - **IAM action:**  [cloudformation:ListResourceRequests](#list_cloudcontrol-action-ListResourceRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResources  **
  - **IAM action:**  [cloudformation:ListResources](#list_cloudcontrol-action-ListResources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   UpdateResource  **
  - **IAM action:**  [cloudformation:UpdateResource](#list_cloudcontrol-action-UpdateResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write



## Actions defined by AWS Cloud Control API
<a name="list_cloudcontrol-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CancelResourceRequest](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_CancelResourceRequest.html)  | Grants permission to cancel resource requests in your account |  |   | Write | 
|   [CreateResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_CreateResource.html)  | Grants permission to create resources in your account |  |   | Write | 
|   [DeleteResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_DeleteResource.html)  | Grants permission to delete resources in your account |  |   | Write | 
|   [GetResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResource.html)  | Grants permission to get resources in your account |  |   | Read | 
|   [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html)  | Grants permission to get resource requests in your account |  |   | Read | 
|   [ListResourceRequests](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResourceRequests.html)  | Grants permission to list resource requests in your account |  |   | Read | 
|   [ListResources](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ListResources.html)  | Grants permission to list resources in your account |  |   | Read | 
|   [UpdateResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_UpdateResource.html)  | Grants permission to update resources in your account |  |   | Write | 

## Resource types defined by AWS Cloud Control API
<a name="list_cloudcontrol-resources-for-iam-policies"></a>

AWS Cloud Control API does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Cloud Control API
<a name="list_cloudcontrol-policy-keys"></a>

AWS Cloud Control API has no service-specific condition keys that can be used in the `Condition` element of policy statements.