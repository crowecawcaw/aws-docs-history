# How Amazon Cognito works with IAM

Before you use IAM to manage access to Amazon Cognito, learn what IAM features are
available to use with Amazon Cognito.

| IAM features you can use with Amazon Cognito                                                                                                             | IAM feature | Amazon Cognito support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")                           | Yes         |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No          |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")                    | Yes         |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")              | Yes         |
| [Policy condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | Yes         |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")                                                                        | No          |
| [ABAC (tags in<br>policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                  | Partial     |
| [Temporary<br>credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")                              | Yes         |
| [Principal permissions](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions")                     | No          |
| [Service<br>roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")                                          | Yes         |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")                        | Yes         |

To get a high-level view of how Amazon Cognito and other AWS services work with most IAM
features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

## Identity-based

policies for Amazon Cognito

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

###

Identity-based policy examples for Amazon Cognito

To view examples of Amazon Cognito identity-based policies, see [Identity-based policy examples for
Amazon Cognito](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based

policies within Amazon Cognito

**Supports resource-based policies:**

No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
_IAM User Guide_.

## Policy actions

for Amazon Cognito

**Supports policy actions:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon Cognito actions, see [Actions defined by Amazon Cognito](../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-actions-as-permissions "../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-actions-as-permissions") in the
_Service Authorization Reference_.

Policy actions in Amazon Cognito use the following prefix before the action:

```
cognito-identity
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "cognito-identity:`action1`",
      "cognito-identity:`action2`"
         ]
```

### Signed versus

unsigned APIs

When you sign Amazon Cognito API requests with AWS credentials, you can restrict them
in an AWS Identity and Access Management (IAM) policy. API requests that you must sign with AWS
credentials include server-side sign-in with `AdminInitiateAuth`, and
actions that create, view, or modify your Amazon Cognito resources like
`UpdateUserPool`. For more information about signed API requests, see
[Signing AWS API requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md").

Because Amazon Cognito is a consumer identity product for apps that you want to make
available to the public, you have access to the following unsigned APIs. Your app
makes these API requests for your users and your prospective users. Some APIs require
no prior authorization, like `InitiateAuth` to start a new authentication
session. Some APIs use access tokens or session keys for authorization, like
`VerifySoftwareToken` to complete MFA setup for a user that has an
existing authenticated session. An unsigned, authorized Amazon Cognito user pools API supports a
`Session` or `AccessToken` parameter in the request syntax
as displayed in the [Amazon Cognito API Reference](../../../cognito-user-identity-pools/latest/APIReference/Welcome.md "../../../cognito-user-identity-pools/latest/APIReference/Welcome.md"). An unsigned Amazon Cognito Identity API supports
an `IdentityId` parameter as displayed in the [Amazon Cognito
Federated Identities API Reference](../../../cognitoidentity/latest/APIReference/Welcome.md "../../../cognitoidentity/latest/APIReference/Welcome.md").

For more information about the authorization models and roles of Amazon Cognito user pools API
operations, see [List of API operations grouped by authorization
model](authentication-flows-public-server-side.md#user-pool-apis-auth-unauth "authentication-flows-public-server-side.md#user-pool-apis-auth-unauth").

###### Amazon Cognito identity pools API operations

- `GetId`
- `GetOpenIdToken`
- `GetCredentialsForIdentity`
- `UnlinkIdentity`

###### Amazon Cognito user pools API operations

- `AssociateSoftwareToken`
- `ChangePassword`
- `ConfirmDevice`
- `ConfirmForgotPassword`
- `ConfirmSignUp`
- `DeleteUser`
- `DeleteUserAttributes`
- `ForgetDevice`
- `ForgotPassword`
- `GetDevice`
- `GetUser`
- `GetUserAttributeVerificationCode`
- `GlobalSignOut`
- `InitiateAuth`
- `ListDevices`
- `ResendConfirmationCode`
- `RespondToAuthChallenge`
- `RevokeToken`
- `SetUserMFAPreference`
- `SetUserSettings`
- `SignUp`
- `UpdateAuthEventFeedback`
- `UpdateDeviceStatus`
- `UpdateUserAttributes`
- `VerifySoftwareToken`
- `VerifyUserAttribute`

To view examples of Amazon Cognito identity-based policies, see [Identity-based policy examples for
Amazon Cognito](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

resources for Amazon Cognito

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

### Amazon resource names

(ARNs)

**ARNs for Amazon Cognito federated identities**

In Amazon Cognito identity pools (federated identities), it is possible to restrict an IAM
user's access to a specific identity pool, using the Amazon Resource Name (ARN)
format, as in the following example. For more information about ARNs, see [IAM
identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md "../../../IAM/latest/UserGuide/reference_identifiers.md").

```
arn:aws:cognito-identity:`REGION`:`ACCOUNT_ID`:identitypool/`IDENTITY_POOL_ID`
```

**ARNs for Amazon Cognito Sync**

In Amazon Cognito Sync, customers can also restrict access by the identity pool ID,
identity ID, and dataset name.

For APIs that operate on an identity pool, the identity pool ARN format is the
same as for Amazon Cognito Federated Identities, except that the service name is
`cognito-sync` instead of `cognito-identity`:

```
arn:aws:cognito-sync:`REGION`:`ACCOUNT_ID`:identitypool/`IDENTITY_POOL_ID`
```

For APIs that operate on a single identity, such as `RegisterDevice`,
you can refer to the individual identity by the following ARN format:

```
arn:aws:cognito-sync:`REGION`:`ACCOUNT_ID`:identitypool/`IDENTITY_POOL_ID`/identity/`IDENTITY_ID`
```

For APIs that operate on datasets, such as `UpdateRecords` and
`ListRecords`, you can refer to the individual dataset using the
following ARN format:

```
arn:aws:cognito-sync:`REGION`:`ACCOUNT_ID`:identitypool/`IDENTITY_POOL_ID`/identity/`IDENTITY_ID`/dataset/`DATASET_NAME`
```

**ARNs for Amazon Cognito user pools**

For Amazon Cognito Your User Pools, it is possible to restrict a user's access to a
specific user pool, using the following ARN format:

```
arn:aws:cognito-idp:`REGION`:`ACCOUNT_ID`:userpool/`USER_POOL_ID`
```

To see a list of Amazon Cognito resource types and their ARNs, see [Resources defined by Amazon Cognito](../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-resources-for-iam-policies")
in the _Service Authorization Reference_. To learn with which actions you can
specify the ARN of each resource, see [Actions defined by Amazon Cognito](../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-actions-as-permissions "../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-actions-as-permissions").

To view examples of Amazon Cognito identity-based policies, see [Identity-based policy examples for
Amazon Cognito](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Policy

condition keys for Amazon Cognito

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Amazon Cognito condition keys, see
[Condition keys for Amazon Cognito](../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-policy-keys "../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-policy-keys") in the _Service Authorization Reference_. To learn with
which actions and resources you can use a condition key, see
[Actions defined by Amazon Cognito](../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-actions-as-permissions "../../../service-authorization/latest/reference/list_amazoncognitoidentity.md#amazoncognitoidentity-actions-as-permissions").

To view examples of Amazon Cognito identity-based policies, see [Identity-based policy examples for
Amazon Cognito](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Access control lists (ACLs) in

Amazon Cognito

**Supports ACLs:**

No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are
similar to resource-based policies, although they do not use the JSON policy document format.

## Attribute-based access control

(ABAC) with Amazon Cognito

**Supports ABAC (tags in policies):**

Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

## Using temporary

credentials with Amazon Cognito

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Cross-service

principal permissions for Amazon Cognito

**Supports forward access sessions (FAS):**

No

Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

## Service roles for

Amazon Cognito

**Supports service roles:**

Yes

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

For details about Amazon Cognito service roles, see [Activate push synchronization](identity-pools.md#enable-push-synchronization "identity-pools.md#enable-push-synchronization")
and [Implementing push synchronization](push-sync.md "push-sync.md").

###### Warning

Changing the permissions for a service role might break Amazon Cognito functionality.
Edit service roles only when Amazon Cognito provides guidance to do so.

## Service-linked

roles for Amazon Cognito

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing Amazon Cognito service-linked roles, see [Using service-linked roles for
Amazon Cognito](using-service-linked-roles.md "using-service-linked-roles.md").
