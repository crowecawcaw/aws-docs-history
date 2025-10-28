# How Amazon API Gateway works with

IAM

Before you use IAM to manage access to API Gateway, you should understand what
IAM features are available to use with API Gateway. To get a high-level view of how
API Gateway and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [API Gateway
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [API Gateway
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  API Gateway tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [API Gateway IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## API Gateway

identity-based policies

With IAM identity-based policies, you can specify which actions and resources are allowed or denied as
well as the conditions under which actions are allowed or denied. API Gateway supports specific actions,
resources, and condition keys. For more information about the API Gateway-specific actions,
resources, and condition keys, see
[Actions, resources, and condition keys for Amazon API Gateway Management](../../../service-authorization/latest/reference/list_amazonapigatewaymanagement.md "../../../service-authorization/latest/reference/list_amazonapigatewaymanagement.md") and
[Actions, resources, and condition keys for Amazon API Gateway Management V2](../../../service-authorization/latest/reference/list_amazonapigatewaymanagementv2.md "../../../service-authorization/latest/reference/list_amazonapigatewaymanagementv2.md"). For information about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

The following example shows an identity-based policy that allows a user to create or update only private
REST APIs. For more examples, see [Amazon API Gateway identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ScopeToPrivateApis",
 "Effect": "Allow",
 "Action": [
 "apigateway:PATCH",
 "apigateway:POST",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/restapis",
 "arn:aws:apigateway:us-east-1::/restapis/??????????"
 ],
 "Condition": {
 "ForAllValues:StringEqualsIfExists": {
 "apigateway:Request/EndpointType": "PRIVATE",
 "apigateway:Resource/EndpointType": "PRIVATE"
 }
 }
 },
 {
 "Sid": "AllowResourcePolicyUpdates",
 "Effect": "Allow",
 "Action": [
 "apigateway:UpdateRestApiPolicy"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/restapis/*"
 ]
 }
 ]
}`

```

### Actions

The `Action` element of a JSON policy describes the actions that you can use to allow or deny
access in a policy.

Policy actions in API Gateway use the following prefix before the action:
`apigateway:`. Policy statements must include either an `Action` or
`NotAction` element. API Gateway defines its own set of actions that describe tasks that you
can perform with this service.

The API-managing `Action` expression has the format
`apigateway:`action``, where
 `action` is one of the following API Gateway actions: **GET**,
**POST**, **PUT**, **DELETE**, **PATCH**
(to update resources), or **\***, which is all of the previous actions.

Some examples of the `Action` expression include:

- `apigateway:*` for all API Gateway actions.
- `apigateway:GET` for just the GET action in API Gateway.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "apigateway:*action1*",
      "apigateway:*action2*"
```

For information about HTTP verbs to use for specific API Gateway operations, see [Amazon API Gateway Version 1 API Reference](../../api-reference.md "../../api-reference.md") (REST APIs) and [Amazon API Gateway Version 2 API
Reference](../../../apigatewayv2/latest/api-reference/api-reference.md "../../../apigatewayv2/latest/api-reference/api-reference.md") (WebSocket and HTTP APIs).

For more information, see [Amazon API Gateway identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

API Gateway resources have the following ARN format:

```
arn:aws:apigateway:`region`::`resource-path-specifier`
```

For example, to specify a REST API with the id `api-id` and its
sub-resources, such as authorizers in your statement, use the following ARN:

```
"Resource": "arn:aws:apigateway:us-east-2::/restapis/api-id/*"
```

To specify all REST APIs and sub-resources that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:apigateway:us-east-2::/restapis/*"
```

For a list of API Gateway resource types and their ARNs, see [API Gateway Amazon Resource Name (ARN)
reference](arn-format-reference.md "arn-format-reference.md").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

API Gateway defines its own set of condition keys and also supports using some global condition
keys. For a list of API Gateway condition keys, see [Condition Keys for Amazon API Gateway](../../../IAM/latest/UserGuide/list_manageamazonapigateway.md#manageamazonapigateway-policy-keys "../../../IAM/latest/UserGuide/list_manageamazonapigateway.md#manageamazonapigateway-policy-keys") in the
_IAM User Guide_. For information about which actions and resources you can use with a
condition key, see [Actions Defined by Amazon API Gateway](../../../IAM/latest/UserGuide/list_manageamazonapigateway.md#amazonapigateway-actions-as-permissions "../../../IAM/latest/UserGuide/list_manageamazonapigateway.md#amazonapigateway-actions-as-permissions").

For information about tagging, including attribute-based access control, see [Tagging your API Gateway resources](apigateway-tagging.md "apigateway-tagging.md").

### Examples

For examples of API Gateway identity-based policies, see [Amazon API Gateway identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## API Gateway

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a specified principal can
perform on the API Gateway resource and under what conditions. API Gateway supports resource-based permissions
policies for REST APIs. You use resource policies to control who can invoke a REST API. For
more information, see [Control access to a REST API with API Gateway
resource policies](apigateway-resource-policies.md "apigateway-resource-policies.md").

### Examples

For examples of API Gateway resource-based policies, see [API Gateway resource policy
examples](apigateway-resource-policies-examples.md "apigateway-resource-policies-examples.md").

## Authorization based on

API Gateway tags

You can attach tags to API Gateway resources or pass tags in a request to
API Gateway. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`apigateway:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
API Gateway resources, see [Using tags to control access to API Gateway REST API resources](apigateway-tagging-iam-policy.md "apigateway-tagging-iam-policy.md").

For an examples of identity-based policies for limiting access to a resource based on the tags on that
resource, see [Using tags to control access to API Gateway REST API resources](apigateway-tagging-iam-policy.md "apigateway-tagging-iam-policy.md").

## API Gateway IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with API Gateway

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

API Gateway supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

API Gateway supports service-linked roles. For information about creating or managing
API Gateway service-linked roles, see [Using service-linked roles for
API Gateway](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles

A service can assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your
behalf. A service role allows the service to access resources in other services to complete an action on your
behalf. Service roles appear in your IAM account and are owned by the account, so an administrator can
change the permissions for this role. However, doing so might break the functionality of the service.

API Gateway supports service roles.
