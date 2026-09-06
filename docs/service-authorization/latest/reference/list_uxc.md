

# Actions, resources, and condition keys for AWS User Experience Customization
<a name="list_uxc"></a>

AWS User Experience Customization (service prefix: `uxc`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/uxc.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/security_iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/uxc/uxc.json) for this service.

**Topics**
+ [API operations defined by AWS User Experience Customization](#list_uxc-operations)
+ [Actions defined by AWS User Experience Customization](#list_uxc-actions-as-permissions)
+ [Resource types defined by AWS User Experience Customization](#list_uxc-resources-for-iam-policies)
+ [Condition keys for AWS User Experience Customization](#list_uxc-policy-keys)

## API operations defined by AWS User Experience Customization
<a name="list_uxc-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_uxc-actions-as-permissions).




- **   GetAccountCustomizations  **
  - **IAM action:**  [uxc:GetAccountColor](#list_uxc-action-GetAccountColor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [uxc:GetAccountCustomizations](#list_uxc-action-GetAccountCustomizations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListServices  **
  - **IAM action:**  [uxc:ListServices](#list_uxc-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateAccountCustomizations  **
  - **IAM action:**  [uxc:DeleteAccountColor](#list_uxc-action-DeleteAccountColor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [uxc:PutAccountColor](#list_uxc-action-PutAccountColor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [uxc:UpdateAccountCustomizations](#list_uxc-action-UpdateAccountCustomizations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS User Experience Customization
<a name="list_uxc-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DeleteAccountColor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_DeleteAccountColor.html)  | Grants permission to delete account color setting |  |   | Write | 
|   [GetAccountColor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_GetAccountColor.html)  | Grants permission to retrieve account color for given account |  |   | Read | 
|   [GetAccountCustomizations](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_GetAccountCustomizations.html)  | Grants permission to retrieve account customizations |  |   | Read | 
|   [ListServices](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html)  | Grants permission to list available services |  |   | Read | 
|   [PutAccountColor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_PutAccountColor.html)  | Grants permission to set account color |  |   | Write | 
|   [UpdateAccountCustomizations](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.html)  | Grants permission to update account customizations |  |   | Write | 

## Resource types defined by AWS User Experience Customization
<a name="list_uxc-resources-for-iam-policies"></a>

AWS User Experience Customization does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS User Experience Customization
<a name="list_uxc-policy-keys"></a>

AWS User Experience Customization has no service-specific condition keys that can be used in the `Condition` element of policy statements.