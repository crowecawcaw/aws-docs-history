# AWS STS condition context keys for

IAM Identity Center

When a [principal](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal") makes a [request](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-request "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-request") to AWS, AWS gathers the request
information into a _request context_, which is used to evaluate and authorize the request. You can
use the `Condition` element of a JSON policy to compare keys in the request
context with key values that you specify in your policy. Request information is provided by
different sources, including the principal making the request, the resource, the request it is
made against, and the metadata about the request itself. _Service-specific condition keys_ are defined for use with
an individual AWS service.

IAM Identity Center includes an AWS STS context provider that enables AWS managed applications and third-party applications
to add values for condition keys that are defined by IAM Identity Center. These keys are included in [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md"). The
key values are set when an application passes a token to AWS STS. The application obtains the token that it passes to AWS STS in either of the following ways:

- During authentication with IAM Identity Center.
- After token exchange with a [trusted token issuer](using-apps-with-trusted-token-issuer.md#trusted-token-issuer-overview "using-apps-with-trusted-token-issuer.md#trusted-token-issuer-overview") for trusted identity propagation. In this case, the application obtains a token from a trusted token issuer and exchanges that token for a token from IAM Identity Center.
  These keys are typically used by applications that integrate with trusted identity
  propagation. In some cases, when key values are present, you can use these keys in IAM policies that you create to allow or deny permissions.

For example, you might want to provide conditional access to a resource based on the value of the `UserId`. This value indicates which IAM Identity Center user is using the role. The example is similar to using `SourceId`. Unlike `SourceId`, however, the value for `UserId` represents a specific, verified user from the identity store. This value is present in the token that the application obtains and then passes to AWS STS. It is not a general purpose string that can contain arbitrary values.

###### Topics

- [identitystore:UserId](#condition-keys-identity-store-user-id "#condition-keys-identity-store-user-id")
- [identitystore:IdentityStoreArn](#condition-keys-identity-store-arn "#condition-keys-identity-store-arn")
- [identitycenter:ApplicationArn](#condition-keys-identity-center-application-arn "#condition-keys-identity-center-application-arn")
- [identitycenter:CredentialId](#condition-keys-identity-center-credential-id "#condition-keys-identity-center-credential-id")
- [identitycenter:InstanceArn](#condition-keys-identity-center-instance-arn "#condition-keys-identity-center-instance-arn")

## identitystore:UserId

This context key is the `UserId` of the IAM Identity Center user who is the subject of
the context assertion issued by IAM Identity Center. The context assertion is passed to AWS STS. You can
use this key to compare the `UserId` of the IAM Identity Center user on behalf of whom the
request is made with the identifier for the user that you specify in the policy.

- **Availability** – This key is included
  in the request context after a context assertion issued by IAM Identity Center is set, when a role is assumed using any AWS STS `assume-role` command in the AWS CLI or AWS STS `AssumeRole` API operation.
- **Data type** – [String](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String")
- **Value type** – Single-valued

## identitystore:IdentityStoreArn

This context key is the ARN of the identity store that is attached to the instance of
IAM Identity Center that issued the context assertion. It is also the identity store in which you can
look up attributes for `identitystore:UserID`. You can use this key in
policies to determine whether the `identitystore:UserID` comes from an
expected identity store ARN.

- **Availability** – This key is included
  in the request context after a context assertion issued by IAM Identity Center is set, when a role is assumed using any AWS STS `assume-role` command in the AWS CLI or AWS STS `AssumeRole` API operation.
- **Data type** – [Arn](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN"),
  [String](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String")
- **Value type** – Single-valued

## identitycenter:ApplicationArn

This context key is the ARN of the application to which IAM Identity Center issued a context
assertion. You can use this key in policies to determine whether
`identitycenter:ApplicationArn` comes from an expected application. Using
this key can help prevent an IAM role from being accessed by an unexpected
application.

- **Availability** – This key is included
  in the request context of an AWS STS `AssumeRole` API operation. The request context includes a context assertion issued by IAM Identity Center.
- **Data type** – [Arn](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN"),
  [String](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String")
- **Value type** – Single-valued

## identitycenter:CredentialId

This context key is a random ID for the identity-enhanced role credential and is used
for logging only. Because this key value is unpredictable, we recommend that you do not
use it for context assertions in policies.

- **Availability** – This key is included
  in the request context of an AWS STS `AssumeRole` API operation. The request context includes a context assertion issued by IAM Identity Center.
- **Data type** – [String](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String")
- **Value type** – Single-valued

## identitycenter:InstanceArn

This context key is the ARN of the instance of IAM Identity Center that issued the context assertion
for the `identitystore:UserID`. You can use this key to determine whether the
`identitystore:UserID` and context assertion came from an expected IAM Identity Center
instance ARN.

- **Availability** – This key is included
  in the request context of an AWS STS `AssumeRole` API operation. The request context includes a context assertion issued by IAM Identity Center.
- **Data type** – [Arn](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN"),
  [String](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String")
- **Value type** – Single-valued
