# Actions, resources, and condition keys for AWS User Experience Customization

AWS User Experience Customization (service prefix: `uxc`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsconsolehelpdocs/latest/gsg/uxc.md "../../../awsconsolehelpdocs/latest/gsg/uxc.md").
- View a list of the [API operations available for
  this service](../../../awsconsolehelpdocs/latest/APIReference/Welcome.md "../../../awsconsolehelpdocs/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsconsolehelpdocs/latest/gsg/security_iam.md "../../../awsconsolehelpdocs/latest/gsg/security_iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/uxc/uxc.json "https://servicereference.us-east-1.amazonaws.com/v1/uxc/uxc.json") for this service.

###### Topics

- [API operations defined by AWS User Experience Customization](#list_uxc-operations "#list_uxc-operations")
- [Actions defined by AWS User Experience Customization](#list_uxc-actions-as-permissions "#list_uxc-actions-as-permissions")
- [Resource types defined by AWS User Experience Customization](#list_uxc-resources-for-iam-policies "#list_uxc-resources-for-iam-policies")
- [Condition keys for AWS User Experience Customization](#list_uxc-policy-keys "#list_uxc-policy-keys")

## API operations defined by AWS User Experience Customization

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_uxc-actions-as-permissions "#list_uxc-actions-as-permissions").

| Operation                                                                                                                      | IAM action                                                                                          | Condition key | Possible value(s) | Access level |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| GetAccountCustomizations                                                                                                       | [uxc:GetAccountColor](#list_uxc-action-GetAccountColor "#list_uxc-action-GetAccountColor")          |               |                   | Read         |
| [uxc:GetAccountCustomizations](#list_uxc-action-GetAccountCustomizations "#list_uxc-action-GetAccountCustomizations")          |                                                                                                     |               | Read              |
| ListServices                                                                                                                   | [uxc:ListServices](#list_uxc-action-ListServices "#list_uxc-action-ListServices")                   |               |                   | Read         |
| UpdateAccountCustomizations                                                                                                    | [uxc:DeleteAccountColor](#list_uxc-action-DeleteAccountColor "#list_uxc-action-DeleteAccountColor") |               |                   | Write        |
| [uxc:PutAccountColor](#list_uxc-action-PutAccountColor "#list_uxc-action-PutAccountColor")                                     |                                                                                                     |               | Write             |
| [uxc:UpdateAccountCustomizations](#list_uxc-action-UpdateAccountCustomizations "#list_uxc-action-UpdateAccountCustomizations") |                                                                                                     |               | Write             |

## Actions defined by AWS User Experience Customization

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                | Description                                                   | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [DeleteAccountColor](../../../awsconsolehelpdocs/latest/APIReference/API_DeleteAccountColor.md "../../../awsconsolehelpdocs/latest/APIReference/API_DeleteAccountColor.md")                            | Grants permission to delete account color setting             |                             |                | Write        |
| [GetAccountColor](../../../awsconsolehelpdocs/latest/APIReference/API_GetAccountColor.md "../../../awsconsolehelpdocs/latest/APIReference/API_GetAccountColor.md")                                     | Grants permission to retrieve account color for given account |                             |                | Read         |
| [GetAccountCustomizations](../../../awsconsolehelpdocs/latest/APIReference/API_GetAccountCustomizations.md "../../../awsconsolehelpdocs/latest/APIReference/API_GetAccountCustomizations.md")          | Grants permission to retrieve account customizations          |                             |                | Read         |
| [ListServices](../../../awsconsolehelpdocs/latest/APIReference/API_ListServices.md "../../../awsconsolehelpdocs/latest/APIReference/API_ListServices.md")                                              | Grants permission to list available services                  |                             |                | Read         |
| [PutAccountColor](../../../awsconsolehelpdocs/latest/APIReference/API_PutAccountColor.md "../../../awsconsolehelpdocs/latest/APIReference/API_PutAccountColor.md")                                     | Grants permission to set account color                        |                             |                | Write        |
| [UpdateAccountCustomizations](../../../awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.md "../../../awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.md") | Grants permission to update account customizations            |                             |                | Write        |

## Resource types defined by AWS User Experience Customization

AWS User Experience Customization does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS User Experience Customization

AWS User Experience Customization has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
