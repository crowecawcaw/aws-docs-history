

# Actions, resources, and condition keys for AWS IAM Identity Center OIDC service
<a name="list_sso-oidc"></a>

AWS IAM Identity Center OIDC service (service prefix: `sso-oauth`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sso-oauth/sso-oauth.json) for this service.

**Topics**
+ [API operations defined by AWS IAM Identity Center OIDC service](#list_sso-oidc-operations)
+ [Actions defined by AWS IAM Identity Center OIDC service](#list_sso-oidc-actions-as-permissions)
+ [Permission-only actions for AWS IAM Identity Center OIDC service](#list_sso-oidc-permission-only-actions)
+ [Resource types defined by AWS IAM Identity Center OIDC service](#list_sso-oidc-resources-for-iam-policies)
+ [Condition keys for AWS IAM Identity Center OIDC service](#list_sso-oidc-policy-keys)

## API operations defined by AWS IAM Identity Center OIDC service
<a name="list_sso-oidc-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sso-oidc-actions-as-permissions).




- **   CreateToken  **
  - **IAM action:**  [sso-oauth:CreateTokenWithIAM](#list_sso-oidc-action-CreateTokenWithIAM) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTokenWithIAM  **
  - **IAM action:**  [sso-oauth:CreateTokenWithIAM](#list_sso-oidc-action-CreateTokenWithIAM) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IAM Identity Center OIDC service
<a name="list_sso-oidc-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateTokenWithIAM](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.html)  **
  - **Description:** Grants permission to create and return OAuth 2.0 access tokens and refresh tokens for authorized client applications. These tokens might contain defined scopes that specify permissions such as `read:profile` or `write:data`
  - **Resource types (\*required):** [Application\*](#list_sso-oidc-resource-Application)
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS IAM Identity Center OIDC service
<a name="list_sso-oidc-permission-only-actions"></a>

The following actions are defined by AWS IAM Identity Center OIDC service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [IntrospectTokenWithIAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-resource-based-policies.html)  **
  - **Description:** Grants permission to validate and retrieve information about active OAuth 2.0 access tokens and refresh tokens, including their associated scopes and permissions. This permission is used only by AWS managed applications and is not documented in the IAM Identity Center OIDC API Reference
  - **Resource types (\*required):** [Application\*](#list_sso-oidc-resource-Application)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RevokeTokenWithIAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-resource-based-policies.html)  **
  - **Description:** Grants permission to revoke OAuth 2.0 access tokens and refresh tokens, invalidating them before their normal expiration. This permission is used only by AWS managed applications and is not documented in the IAM Identity Center OIDC API Reference
  - **Resource types (\*required):** [Application\*](#list_sso-oidc-resource-Application)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS IAM Identity Center OIDC service
<a name="list_sso-oidc-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Application](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-enable-identity-center.html)  | arn:${Partition}:sso::${AccountId}:application/${InstanceId}/${ApplicationId} |   | 

## Condition keys for AWS IAM Identity Center OIDC service
<a name="list_sso-oidc-policy-keys"></a>

AWS IAM Identity Center OIDC service has no service-specific condition keys that can be used in the `Condition` element of policy statements.