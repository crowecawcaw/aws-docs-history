# Using IAM policies with AWS KMS

You can use IAM policies, along with [key policies](key-policies.md "key-policies.md"),
[grants](grants.md "grants.md"), and [VPC endpoint
policies](../../../vpc/latest/privatelink/interface-endpoints.md#edit-vpc-endpoint-policy "../../../vpc/latest/privatelink/interface-endpoints.md#edit-vpc-endpoint-policy"), to control access to your AWS KMS keys in AWS KMS.

###### Note

To use an IAM policy to control access to a KMS key, the key policy for the KMS key
must give the account permission to use IAM policies. Specifically, the key policy must
include the [policy statement that
enables IAM policies](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam").

This section explains how to use IAM policies to control access to AWS KMS operations. For
more general information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

All KMS keys must have a key policy. IAM policies are optional. To use an IAM policy
to control access to a KMS key, the key policy for the KMS key must give the account
permission to use IAM policies. Specifically, the key policy must include the [policy statement that enables IAM
policies](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam").

IAM policies can control access to any AWS KMS operation. Unlike key policies, IAM
policies can control access to multiple KMS keys and provide permissions for the operations of
several related AWS services. But IAM policies are particularly useful for controlling
access to operations, such as [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md"),
that can't be controlled by a key policy because they don't involve any particular
KMS key.

If you access AWS KMS through an Amazon Virtual Private Cloud (Amazon VPC) endpoint, you can also use a VPC endpoint policy to limit access to your AWS KMS resources when using the endpoint. For example, when using the VPC endpoint, you might only allow the principals in your AWS account to access your customer managed keys. For details, see [VPC endpoint
policies](../../../vpc/latest/privatelink/interface-endpoints.md#edit-vpc-endpoint-policy "../../../vpc/latest/privatelink/interface-endpoints.md#edit-vpc-endpoint-policy").

For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

You can use IAM policies in the following ways:

- **Attach a permissions policy to a role for federation or
  cross-account permissions** – You can attach an IAM policy to an IAM
  role to enable identity federation, allow cross-account permissions, or give permissions to
  applications running on EC2 instances. For more information about the various use cases for
  IAM roles, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
  _IAM User Guide_.
- **Attach a permissions policy to a user or a group**
  – You can attach a policy that allows a user or group of users to call AWS KMS
  operations. However, IAM best practices recommend that you use identities with temporary
  credentials, such as IAM roles, whenever possible.
  The following example shows an IAM policy with AWS KMS permissions. This policy allows the
  IAM identities to which it is attached to list all KMS keys and aliases.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:ListKeys",
 "kms:ListAliases"
 ],
 "Resource": "*"
 }
}`

```

Like all IAM policies, this policy doesn't have a `Principal` element. When you
attach an IAM policy to an IAM identity, that identity gets the permissions specified in the
policy.

For a table showing all of the AWS KMS API actions and the resources that they apply to, see
the [Permissions reference](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

## Allowing multiple IAM principals

to access a KMS key

IAM groups are not valid principals in a key policy. To allow multiple users and roles
to access a KMS key, do one of the following:

- Use an IAM role as the principal in the key policy. Multiple authorized users can
  assume the role as needed. For details, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
  in the _IAM User Guide_.

While you can list multiple IAM users in a key policy, this practice is not
recommended because it requires that you update the key policy every time the list of
authorized users changes. Also, IAM best practices discourage the use of IAM users
with long-term credentials. For details, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

- Use an IAM policy to give permission to an IAM group. To do this, ensure that the
  key policy includes the statement that [enables IAM policies to allow
  access to the KMS key](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam"), [create an IAM policy](../../../IAM/latest/UserGuide/access_policies_managed-using.md#create-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#create-managed-policy-console") that allows access to the KMS key, and then [attach that policy to an IAM group](../../../IAM/latest/UserGuide/access_policies_managed-using.md#attach-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#attach-managed-policy-console") that contains the authorized IAM users.
  Using this approach, you don't need to change any policies when the list of authorized
  users changes. Instead, you only need to add or remove those users from the appropriate
  IAM group. For details, see [IAM user
  groups](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") in the _IAM User Guide_

For more information about how AWS KMS key policies and IAM policies work together, see
[Troubleshooting AWS KMS permissions](policy-evaluation.md "policy-evaluation.md").
