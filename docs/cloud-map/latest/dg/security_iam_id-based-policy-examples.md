# Identity-based policy examples

for AWS Cloud Map

By default, users and roles don't have permission to create or modify AWS Cloud Map
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS Cloud Map, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Cloud Map](../../../service-authorization/latest/reference/list_awscloudmap.md "../../../service-authorization/latest/reference/list_awscloudmap.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the AWS Cloud Map
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [AWS Cloud Map console
  access example](#security_iam_id-based-policy-examples-console-cmap "#security_iam_id-based-policy-examples-console-cmap")
- [Allow
  AWS Cloud Map users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow read
  access to all AWS Cloud Map resources](#security_iam_id-based-policy-examples-allow-read-access "#security_iam_id-based-policy-examples-allow-read-access")
- [AWS Cloud Map
  service instance example](#security_iam_id-based-policy-examples-service-instances "#security_iam_id-based-policy-examples-service-instances")
- [Create
  AWS Cloud Map service example](#security_iam_id-based-policy-examples-create-service "#security_iam_id-based-policy-examples-create-service")
- [Create AWS Cloud Map namespaces example](#security_iam_id-based-policy-examples-allow-create-namespaces "#security_iam_id-based-policy-examples-allow-create-namespaces")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS Cloud Map resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## Using the AWS Cloud Map

console

To access the AWS Cloud Map console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS Cloud Map resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the AWS Cloud Map console, also attach
the AWS Cloud Map `ConsoleAccess` or
`ReadOnly` AWS managed policy to the
entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## AWS Cloud Map console

access example

To grant full access to the AWS Cloud Map console, you grant the permissions in the
following permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "servicediscovery:*",
 "route53:GetHostedZone",
 "route53:ListHostedZonesByName",
 "route53:CreateHostedZone",
 "route53:DeleteHostedZone",
 "route53:ChangeResourceRecordSets",
 "route53:CreateHealthCheck",
 "route53:GetHealthCheck",
 "route53:DeleteHealthCheck",
 "route53:UpdateHealthCheck",
 "ec2:DescribeInstances",
 "ec2:DescribeVpcs",
 "ec2:DescribeRegions"
 ],
 "Resource":"*"
 }
 ]
}`

```

Here's why the permissions are required:

**`servicediscovery:*`**

Lets you perform all AWS Cloud Map actions.

**`route53:CreateHostedZone`, `route53:GetHostedZone`,
`route53:ListHostedZonesByName`,
`route53:DeleteHostedZone`**

Lets AWS Cloud Map manage hosted zones when you create and delete public
and private DNS namespaces.

**`route53:CreateHealthCheck`,
`route53:GetHealthCheck`,
`route53:DeleteHealthCheck`,
`route53:UpdateHealthCheck`**

Lets AWS Cloud Map manage health checks when you include Amazon Route 53 health
checks when you create a service.

**`ec2:DescribeVpcs` and `ec2:DescribeRegions`**

Let AWS Cloud Map manage private hosted zones.

## Allow

AWS Cloud Map users to view their own permissions

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

## Allow read

access to all AWS Cloud Map resources

The following permissions policy grants the user read-only access to all
AWS Cloud Map resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "servicediscovery:Get*",
 "servicediscovery:List*",
 "servicediscovery:DiscoverInstances"
 ],
 "Resource":"*"
 }
 ]
}`

```

## AWS Cloud Map

service instance example

The following example shows a permissions policy that grants a user permission to
register, deregister, and discover service instances. The `Sid`, or
statement ID, is optional:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid" : "AllowInstancePermissions",
 "Effect": "Allow",
 "Action": [
 "servicediscovery:RegisterInstance",
 "servicediscovery:DeregisterInstance",
 "servicediscovery:DiscoverInstances",
 "servicediscovery:Get*",
 "servicediscovery:List*",
 "route53:GetHostedZone",
 "route53:ListHostedZonesByName",
 "route53:ChangeResourceRecordSets",
 "route53:CreateHealthCheck",
 "route53:GetHealthCheck",
 "route53:DeleteHealthCheck",
 "route53:UpdateHealthCheck",
 "ec2:DescribeInstances"
 ],
 "Resource": "*"
 }
 ]
}`

```

The policy grants permissions to the actions that are required to register and
manage service instances. The Route 53 permission is required if you're using public or
private DNS namespaces because AWS Cloud Map creates, updates, and deletes Route 53
records and health checks when you register and deregister instances. The wildcard
character (\*) in `Resource` grants access to all AWS Cloud Map instances,
and Route 53 records and health checks that are owned by the current AWS account.

## Create

AWS Cloud Map service example

When adding a permissions policy to allow an IAM identity to create a AWS Cloud Map
service, you must specify the Amazon Resource Name (ARN) of both the AWS Cloud Map
namespace and service in the resource field. The ARN includes the Region, account
ID, and namespace ID. Since you won't know what the service ID of the service is
yet, we recommend using a wildcard. The following is an example policy
snippet.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicediscovery:CreateService"
 ],
 "Resource": [
 "arn:aws:servicediscovery:`us-east-1`:`111122223333`:namespace/`ns-p32123EXAMPLE`",
 "arn:aws:servicediscovery:`us-east-1`:`111122223333`:service/*"
 ]
 }
 ]
}`

```

##

Create AWS Cloud Map namespaces example

The following permissions policy allows users to create all types of AWS Cloud Map
namespaces:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "servicediscovery:CreateHttpNamespace",
 "servicediscovery:CreatePrivateDnsNamespace",
 "servicediscovery:CreatePublicDnsNamespace",
 "route53:CreateHostedZone",
 "route53:GetHostedZone",
 "route53:ListHostedZonesByName",
 "ec2:DescribeVpcs",
 "ec2:DescribeRegions"
 ],
 "Resource":"*"
 }
 ]
}`

```
