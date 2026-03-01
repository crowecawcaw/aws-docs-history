# Amazon API Gateway identity-based policy examples

By default, IAM users and roles don't have permission to create or modify
API Gateway resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS SDKs. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

For information about how to create IAM policies, see [Creating Policies on the JSON
Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_. For information about the actions, resources, and conditions specific to API Gateway, see
[Actions, resources, and condition keys for Amazon API Gateway Management](../../../service-authorization/latest/reference/list_amazonapigatewaymanagement.md "../../../service-authorization/latest/reference/list_amazonapigatewaymanagement.md") and
[Actions, resources, and condition keys for Amazon API Gateway Management V2](../../../service-authorization/latest/reference/list_amazonapigatewaymanagementv2.md "../../../service-authorization/latest/reference/list_amazonapigatewaymanagementv2.md").

###### Topics

- [Policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Simple read permissions](#api-gateway-policy-example-apigateway-general "#api-gateway-policy-example-apigateway-general")
- [Create only REQUEST or JWT authorizers](#security_iam_id-based-policy-examples-v2-import "#security_iam_id-based-policy-examples-v2-import")
- [Require that the default execute-api endpoint is disabled](#security_iam_id-based-policy-examples-v2-endpoint-status "#security_iam_id-based-policy-examples-v2-endpoint-status")
- [Allow users to create or update only private REST APIs](#security_iam_id-based-policy-examples-private-api "#security_iam_id-based-policy-examples-private-api")
- [Require that API routes have authorization](#security_iam_id-based-policy-examples-require-authorization "#security_iam_id-based-policy-examples-require-authorization")
- [Prevent a user from creating or updating a VPC link](#security_iam_id-based-policy-examples-deny-vpc-link "#security_iam_id-based-policy-examples-deny-vpc-link")
- [Example policies for using routing rules](#security_iam_id-based-policy-examples-routing-mode "#security_iam_id-based-policy-examples-routing-mode")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete API Gateway resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Allow users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Simple read permissions

This example policy gives a user permission to get information about all of the resources of an HTTP or
WebSocket API with the identifier of `a123456789` in the AWS Region of
us-east-1. The resource
`arn:aws:apigateway:`us-east-1`::/apis/a123456789/*`
includes all sub-resources of the API such as authorizers and deployments.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "apigateway:GET"
 ],
 "Resource": [
 "arn:aws:apigateway:`us-east-1`::/apis/a123456789/*"
 ]
 }
 ]
}`

```

## Create only REQUEST or JWT authorizers

This example policy allows a user to create APIs with only `REQUEST` or `JWT`
authorizers, including through [import](../../../apigatewayv2/latest/api-reference/apis.md#ImportApi "../../../apigatewayv2/latest/api-reference/apis.md#ImportApi"). In the `Resource`
section of the policy, `arn:aws:apigateway:us-east-1::/apis/??????????` requires that resources have
a maximum of 10 characters, which excludes sub-resources of an API. This example uses `ForAllValues`
in the `Condition` section because users can create multiple authorizers at once by importing an
API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OnlyAllowSomeAuthorizerTypes",
 "Effect": "Allow",
 "Action": [
 "apigateway:PUT",
 "apigateway:POST",
 "apigateway:PATCH"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/apis",
 "arn:aws:apigateway:us-east-1::/apis/??????????",
 "arn:aws:apigateway:us-east-1::/apis/*/authorizers",
 "arn:aws:apigateway:us-east-1::/apis/*/authorizers/*"
 ],
 "Condition": {
 "ForAllValues:StringEqualsIfExists": {
 "apigateway:Request/AuthorizerType": [
 "REQUEST",
 "JWT"
 ]
 }
 }
 }
 ]
}`

```

## Require that the default `execute-api` endpoint is disabled

This example policy allows users to create, update or import an API, with the
requirement that `DisableExecuteApiEndpoint` is `true`. When
`DisableExecuteApiEndpoint` is `true`, clients can't use the default
`execute-api` endpoint to invoke an API.

We use the `BoolIfExists` condition to handle a call to update an API that doesn't have the
`DisableExecuteApiEndpoint` condition key populated. When a user attempts to create or import an
API, the `DisableExecuteApiEndpoint` condition key is always populated.

Because the `apis/*` resource also captures sub resources such as authorizers or methods, we
explicitly scope it to just APIs with a `Deny` statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DisableExecuteApiEndpoint",
 "Effect": "Allow",
 "Action": [
 "apigateway:PATCH",
 "apigateway:POST",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/apis",
 "arn:aws:apigateway:us-east-1::/apis/*"
 ],
 "Condition": {
 "BoolIfExists": {
 "apigateway:Request/DisableExecuteApiEndpoint": true
 }
 }
 },
 {
 "Sid": "ScopeDownToJustApis",
 "Effect": "Deny",
 "Action": [
 "apigateway:PATCH",
 "apigateway:POST",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/apis/*/*"
 ]
 }
 ]
}`

```

## Allow users to create or update only private REST APIs

This example policy uses condition keys to require that a user creates only `PRIVATE`
APIs, and to prevent updates that might change an API from `PRIVATE` to another type, such as
`REGIONAL`.

We use `ForAllValues` to require that every `EndpointType` added to an API is
`PRIVATE`. We use a resource condition key to allow any update to an API as long as it's
`PRIVATE`. `ForAllValues` applies only if a condition key is present.

We use the non-greedy matcher (`?`) to explicitly match against API IDs to
prevent allowing non-API resources such as authorizers.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ScopePutToPrivateApis",
 "Effect": "Allow",
 "Action": [
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/restapis",
 "arn:aws:apigateway:us-east-1::/restapis/??????????"
 ],
 "Condition": {
 "ForAllValues:StringEquals": {
 "apigateway:Resource/EndpointType": "PRIVATE"
 }
 }
 },
 {
 "Sid": "ScopeToPrivateApis",
 "Effect": "Allow",
 "Action": [
 "apigateway:DELETE",
 "apigateway:PATCH",
 "apigateway:POST"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/restapis",
 "arn:aws:apigateway:us-east-1::/restapis/??????????"
 ],
 "Condition": {
 "ForAllValues:StringEquals": {
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

## Require that API routes have authorization

This policy causes attempts to create or update a route (including through [import](../../../apigatewayv2/latest/api-reference/apis.md#ImportApi "../../../apigatewayv2/latest/api-reference/apis.md#ImportApi")) to fail if the route has no
authorization. `ForAnyValue` evaluates to false if the key is not present, such as when a route is
not being created or updated. We use `ForAnyValue` because multiple routes can be created through
import.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUpdatesOnApisAndRoutes",
 "Effect": "Allow",
 "Action": [
 "apigateway:POST",
 "apigateway:PATCH",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/apis",
 "arn:aws:apigateway:us-east-1::/apis/??????????",
 "arn:aws:apigateway:us-east-1::/apis/*/routes",
 "arn:aws:apigateway:us-east-1::/apis/*/routes/*"
 ]
 },
 {
 "Sid": "DenyUnauthorizedRoutes",
 "Effect": "Deny",
 "Action": [
 "apigateway:POST",
 "apigateway:PATCH",
 "apigateway:PUT"
 ],
 "Resource": [
 "arn:aws:apigateway:us-east-1::/apis",
 "arn:aws:apigateway:us-east-1::/apis/*"
 ],
 "Condition": {
 "ForAnyValue:StringEqualsIgnoreCase": {
 "apigateway:Request/RouteAuthorizationType": "NONE"
 }
 }
 }
 ]
}`

```

## Prevent a user from creating or updating a VPC link

This policy prevents a user from creating or updating a VPC link. A VPC link enables you to expose resources
within an Amazon VPC to clients outside of the VPC.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyVPCLink",
 "Effect": "Deny",
 "Action": [
 "apigateway:POST",
 "apigateway:PUT",
 "apigateway:PATCH"
 ],
 "Resource": [
 "arn:aws:apigateway:`us-east-1`::/vpclinks",
 "arn:aws:apigateway:`us-east-1`::/vpclinks/*"
 ]
 }
 ]
}`

```

## Example policies for using routing rules

The following example policies show how to use the RoutingRule condition keys to control how users can route
traffic from their custom domain names to their REST APIs. You can use these examples to create fine-grained
policies for what kind of routing rules users can make. For more information, see [Routing rules to connect API stages to a custom domain name for REST APIs](rest-api-routing-rules.md "rest-api-routing-rules.md").

### Prevent a user from changing how a custom domain name routes a request

This policy prevents a user from creating or updating a `BasePathMapping`, `ApiMapping` or
`RoutingRule`.
All of these resources might change how a custom domain name routes requests to APIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAccessBasePathMappingsApiMappingsRoutingRules",
 "Effect": "Deny",
 "Action": "apigateway:*",
 "Resource": [
 "arn:aws:apigateway:`us-east-1`::/domainnames/`example.com`/basepathmappings/*",
 "arn:aws:apigateway:`us-east-1`::/domainnames/`example.com`/apimappings/*",
 "arn:aws:apigateway:`us-east-1`:`111122223333`:/domainnames/`example.com`/routingrules/*"
 ]
 }
 ]
}`

```

### Allow a user to update a routing rule for certain priorities

This policy allows a user to only update a routing rule to a priority between 1001 and 2000. You can use
this rule to separate your production rules from lower priority rules and then allow users to modify lower
priority rules without impacting production rules.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UpdatingRoutingRulePriorityBetween1001And2000",
 "Effect": "Allow",
 "Action": "apigateway:UpdateRoutingRule",
 "Resource": "arn:aws:apigateway:us-east-1:111122223333:/domainnames/example.com/routingrules/*",
 "Condition": {
 "NumericGreaterThanEquals": {
 "apigateway:Resource/Priority": 1001,
 "apigateway:Request/Priority": 1001
 },
 "NumericLessThanEquals": {
 "apigateway:Resource/Priority": 2000,
 "apigateway:Request/Priority": 2000
 }
 }
 }
 ]
}`

```

### Allow a user to update a routing rule or base path mapping for a certain base path value

This policy allows a user to only update a base path mapping for any base path that starts with
`orders` or update a routing rule matching a base path that starts with `orders`. In this policy, a user can update a base path mapping or routing rule for `orders/create` or `orders123`, but not
`payment/orders`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUpdateRoutingRuleUnderPathOrders",
 "Effect": "Allow",
 "Action": "apigateway:UpdateRoutingRule",
 "Resource": "arn:aws:apigateway:us-east-1:111122223333:/domainnames/example.com/routingrules/*",
 "Condition": {
 "ForAllValues:StringLike": {
 "apigateway:Request/ConditionBasePaths": ["orders*"],
 "apigateway:Resource/ConditionBasePaths": ["orders*"]
 },
 "Null":{
 "apigateway:Request/ConditionBasePaths":"false",
 "apigateway:Resource/ConditionBasePaths":"false"
 }
 }
 }
 ]
}`

```

### Allow a user to update the routing mode to specific values

This policy allows a user to only update the routing mode to `API_MAPPING_ONLY` and
`ROUTING_RULE_THEN_API_MAPPING`. For more information about routing mode, see [Set the routing mode for your custom domain name](set-routing-mode.md "set-routing-mode.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUpdateRoutingModeToAnythingWithApiMapping",
 "Effect": "Allow",
 "Action": ["apigateway:PATCH"],
 "Resource": "arn:aws:apigateway:us-east-1::/domainnames/example.com",
 "Condition": {
 "StringLike": {
 "apigateway:Request/RoutingMode":"*API_MAPPING*"
 }
 }
 }
 ]
}`

```
