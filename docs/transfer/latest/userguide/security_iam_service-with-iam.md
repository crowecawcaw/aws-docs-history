# How AWS Transfer Family works with IAM

Before you use AWS Identity and Access Management (IAM) to manage access to AWS Transfer Family, you should understand
what IAM features are available to use with AWS Transfer Family. To get a high-level view of how
AWS Transfer Family and other AWS services work with IAM, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

###### Topics

- [AWS Transfer Family
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [AWS Transfer Family
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on AWS Transfer Family
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [AWS Transfer Family IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## AWS Transfer Family

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
AWS Transfer Family supports specific actions, resources, and condition keys. To learn about
all of the elements that you use in a JSON policy, see [IAM JSON policy
elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _AWS Identity and Access Management User
Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Transfer Family use the following prefix before the action:
`transfer:`. For example, to grant someone permission to create a
server, with the Transfer Family `CreateServer` API operation, you include the
`transfer:CreateServer` action in their policy. Policy statements
must include either an `Action` or `NotAction` element.
AWS Transfer Family defines its own set of actions that describe tasks that you can perform
with this service.

To specify multiple actions in a single statement, separate them with commas
as follows.

```
"Action": [
      "transfer:*action1*",
      "transfer:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Describe`, include the
following action.

```
`"Action": "transfer:Describe*"`
```

To see a list of AWS Transfer Family actions, see [Actions defined by AWS Transfer Family](../../../service-authorization/latest/reference/list_awstransferfamily.md#awstransferfamily-actions-as-permissions "../../../service-authorization/latest/reference/list_awstransferfamily.md#awstransferfamily-actions-as-permissions") in the
_Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Transfer Family server resource has the following ARN.

```
arn:aws:transfer:${Region}:${Account}:server/${ServerId}
```

For example, to specify the `s-01234567890abcdef` Transfer Family server in
your statement, use the following ARN.

```
"Resource": "arn:aws:transfer:us-east-1:123456789012:server/s-01234567890abcdef"
```

For more information about the format of ARNs, see [Amazon Resource Names
(ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _Service Authorization Reference_, or [IAM
ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") in the _IAM User Guide_.

To specify all instances that belong to a specific account, use the wildcard
(\*).

```
"Resource": "arn:aws:transfer:us-east-1:123456789012:server/*"
```

Some AWS Transfer Family actions are performed on multiple resources, such as those used
in IAM policies. In those cases, you must use the wildcard (\*).

```
"Resource": "arn:aws:transfer:*:123456789012:server/*"
```

In some cases you need to specify more than one type of resource, for example,
if you create a policy that allows access to Transfer Family servers and users. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
            ]
```

To see a list of AWS Transfer Family resources, see [Resource types defined by AWS Transfer Family](../../../service-authorization/latest/reference/list_awstransferfamily.md#awstransferfamily-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awstransferfamily.md#awstransferfamily-resources-for-iam-policies") in the
_Service Authorization Reference_.

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

AWS Transfer Family defines its own set of condition keys and also supports using some
global condition keys. To see a list of AWS Transfer Family condition keys, see [Condition keys for AWS Transfer Family](../../../service-authorization/latest/reference/list_awstransferfamily.md#awstransferfamily-policy-keys "../../../service-authorization/latest/reference/list_awstransferfamily.md#awstransferfamily-policy-keys") in the
_Service Authorization Reference_.

### Examples

To view examples of AWS Transfer Family identity-based policies, see [AWS Transfer Family identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). For VPC
endpoint-specific IAM policies, see [Limiting VPC endpoint access for Transfer Family
servers](create-server-in-vpc.md#limit-vpc-endpoint-access "create-server-in-vpc.md#limit-vpc-endpoint-access").

## AWS Transfer Family

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a
specified principal can perform on the AWS Transfer Family resource and under what conditions.
Amazon S3 supports resource-based permissions policies for Amazon S3
`buckets`. Resource-based policies let you grant usage
permission to other accounts on a per-resource basis. You can also use a
resource-based policy to allow an AWS service to access your Amazon S3
`buckets`.

To enable cross-account access, you can specify an entire account or IAM
entities in another account as the [principal
in a resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Adding a cross-account principal to a
resource-based policy is only half of establishing the trust relationship. When the
principal and the resource are in different AWS accounts, you must also grant the
principal entity permission to access the resource. Grant permission by attaching an
identity-based policy to the entity. However, if a resource-based policy grants
access to a principal in the same account, no additional identity-based policy is
required. For more information, see [How IAM
roles differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the _AWS Identity and Access Management
User Guide_.

The Amazon S3 service supports only one type of resource-based policy called a
_`bucket` policy_,
which is attached to a `bucket`. This policy defines which
principal entities (accounts, users, roles, and federated users) can perform actions
on the object.

### Examples

To view examples of AWS Transfer Family resource-based policies, see [AWS Transfer Family tag-based policy
examples](security_iam_tag-based-policy-examples.md "security_iam_tag-based-policy-examples.md").

## Authorization based on AWS Transfer Family

tags

You can attach tags to AWS Transfer Family resources or pass tags in a request to AWS Transfer Family.
To control access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`transfer:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For information about how to use tags
to control access to AWS Transfer Family resources, see [AWS Transfer Family tag-based policy
examples](security_iam_tag-based-policy-examples.md "security_iam_tag-based-policy-examples.md").

## AWS Transfer Family IAM roles

An [IAM
role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific
permissions.

### Using temporary

credentials with AWS Transfer Family

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

AWS Transfer Family supports using temporary credentials.
