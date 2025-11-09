# Amazon EMR managed

policies

The easiest way to grant full access or read-only access to required Amazon EMR actions
is to use the IAM managed policies for Amazon EMR. Managed policies offer the benefit
of updating automatically if permission requirements change. If you use inline
policies, service changes may occur that cause permission errors to appear.

Amazon EMR will be deprecating existing managed policies (v1 policies) in favor of new
managed policies (v2 policies). The new managed policies have been scoped-down to
align with AWS best practices. After the existing v1 managed policies are
deprecated, you will not be able to attach these policies to any new IAM roles or
users. Existing roles and users that use deprecated policies can continue to use
them. The v2 managed policies restrict access using tags. They allow only specified
Amazon EMR actions and require cluster resources that are tagged with an EMR-specific
key. We recommend that you carefully review the documentation before using the new
v2 policies.

The v1 policies will be marked deprecated with a warning icon next to them in the
**Policies** list in the IAM console. The deprecated policies
will have the following characteristics:

- They will continue to work for all currently attached users, groups, and
  roles. Nothing breaks.
- They cannot be attached to new users, groups, or roles. If you detach one
  of the policies from a current entity, you cannot reattach it.
- After you detach a v1 policy from all current entities, the policy will no
  longer be visible and can no longer be used.
  The following table summarizes the changes between current policies (v1) and v2
  policies.

| Amazon EMR managed policy changes                                                 | Policy type                                                                                                                                                                                                                                                                 | Policy names                                                                                                                                                                                                                             | Policy purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Changes to v2 policy |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Default EMR service role and attached managed policy                              | Role name: **EMR_DefaultRole**<br>V1 policy (to be deprecated): \*_AmazonElasticMapReduceRole_<br>• (EMR Service<br>Role)<br>V2 (scoped-down) policy name: [AmazonEMRServicePolicy_v2](emr-iam-role.md "emr-iam-role.md")                                                   | Allows Amazon EMR to call other AWS services on your behalf when<br>provisioning resources and performing service-level actions.<br>This role is required for all clusters.                                                              | Policy adds the new permission `"ec2:DescribeInstanceTypeOfferings"`. This API<br>operation returns a list of instance types that are supported by a list of given Availability Zones.                                                                                                                                                                                                                                                                                                                                                                     |
| IAM managed policy for full Amazon EMR access by attached user,<br>role, or group | V2 (scoped) policy name: [AmazonEMRServicePolicy_v2](emr-managed-policy-fullaccess-v2.md "emr-managed-policy-fullaccess-v2.md")                                                                                                                                             | Allows users full permissions for EMR actions. Includes<br>iam:PassRole permissions for resources.                                                                                                                                       | Policy adds a prerequisite that users must add user tags to<br>resources before they can use this policy. See [Tagging resources to use managed<br>policies](#manually-tagged-resources "#manually-tagged-resources").<br>iam:PassRole action requires iam:PassedToService condition set<br>to specified service. Access to Amazon EC2, Amazon S3, and other services<br>is not allowed by default. See [IAM Managed<br>Policy for Full Access (v2 Managed Default<br>Policy)](emr-managed-policy-fullaccess-v2.md "emr-managed-policy-fullaccess-v2.md"). |
| IAM managed policy for read-only access by attached user,<br>role, or group       | V1 policy (to be deprecated): [AmazonElasticMapReduceReadOnlyAccess](emr-managed-policy-readonly.md "emr-managed-policy-readonly.md")<br>V2 (scoped) policy name: [AmazonEMRReadOnlyAccessPolicy_v2](emr-managed-policy-readonly-v2.md "emr-managed-policy-readonly-v2.md") | Allows users read-only permissions for Amazon EMR actions.                                                                                                                                                                               | Permissions allow only specified elasticmapreduce read-only<br>actions. Access to Amazon S3 is access not allowed by default. See<br>[IAM Managed<br>Policy for Read-Only Access (v2 Managed Default<br>Policy)](emr-managed-policy-readonly-v2.md "emr-managed-policy-readonly-v2.md").                                                                                                                                                                                                                                                                   |
| Default EMR service role and attached managed policy                              | Role name: **EMR_DefaultRole**<br>V1 policy (to be deprecated): \*_AmazonElasticMapReduceRole_<br>• (EMR Service<br>Role)<br>V2 (scoped-down) policy name: [AmazonEMRServicePolicy_v2](emr-iam-role.md "emr-iam-role.md")                                                   | Allows Amazon EMR to call other AWS services on your behalf when<br>provisioning resources and performing service-level actions.<br>This role is required for all clusters.                                                              | The v2 service role and v2 default policy replace the<br>deprecated role and policy. The policy adds a prerequisite that<br>users must add user tags to resources before they can use this<br>policy. See [Tagging resources to use managed<br>policies](#manually-tagged-resources "#manually-tagged-resources"). See [Service role for Amazon EMR (EMR role)](emr-iam-role.md "emr-iam-role.md").                                                                                                                                                        |
| Service role for cluster EC2 instances (EC2 instance<br>profile)                  | Role name: **EMR_EC2_DefaultRole**<br>Deprecated policy name: **AmazonElasticMapReduceforEC2Role**                                                                                                                                                                          | Allows applications running on an EMR cluster to access other<br>AWS resources, such as Amazon S3. For example, if you run Apache<br>Spark jobs that process data from Amazon S3, the policy needs to<br>allow access to such resources. | Both default role and default policy are on the path to<br>deprecation. There is no replacement AWS default managed role<br>or policy. You need to provide a resource-based or<br>identity-based policy. This means that, by default, applications<br>running on an EMR cluster do not have access to Amazon S3 or<br>other resource unless you manually add these to the policy. See<br>[Default role and managed policy](emr-iam-role-for-ec2.md#emr-ec2-role-default "emr-iam-role-for-ec2.md#emr-ec2-role-default").                                   |
| Other EC2 service role policies                                                   | Current policy names: **AmazonElasticMapReduceforAutoScalingRole,<br>AmazonElasticMapReduceEditorsRole,<br>AmazonEMRCleanupPolicy**                                                                                                                                         | Provides permissions that Amazon EMR needs to access other AWS<br>resources and perform actions if using auto scaling, notebooks,<br>or to clean up EC2 resources.                                                                       | No changes for v2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Securing iam:PassRole

The Amazon EMR full-permissions default managed policies incorporate `iam:PassRole` security configurations, including the following:

- `iam:PassRole` permissions only for specific default Amazon EMR roles.
- `iam:PassedToService` conditions that allow you to use the policy with only specified AWS services, such as `elasticmapreduce.amazonaws.com` and `ec2.amazonaws.com`.

You can view the JSON version of the [AmazonEMRFullAccessPolicy_v2](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRFullAccessPolicy_v2 "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRFullAccessPolicy_v2") and [AmazonEMRServicePolicy_v2](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2 "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2") policies in the IAM console. We recommend that you create new clusters with the v2 managed policies.

To create custom policies, we recommend that you begin with the managed
policies and edit them according to your requirements.

For information about how to attach policies to a users (principals), see
[Working with managed policies using the AWS Management Console](../../../IAM/latest/UserGuide/access_policies_managed-using.md#policies_using-managed-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#policies_using-managed-console") in the
_IAM User Guide_.

## Tagging resources to use managed

policies

**AmazonEMRServicePolicy_v2** and **AmazonEMRFullAccessPolicy_v2** depend on scoped-down
access to resources that Amazon EMR provisions or uses. The scope down is achieved by
restricting access to only those resources that have a predefined user tag
associated with them. When you use either of these two policies, you must pass
the predefined user tag `for-use-with-amazon-emr-managed-policies =
 true` when you provision the cluster. Amazon EMR will then automatically
propagate that tag. Additionally, you must add a user tag to the resources
listed in the following section. If you use the Amazon EMR console to launch your
cluster, see [Considerations for
using the Amazon EMR console to launch clusters with v2 managed policies](#emr-cluster-v2policy-awsconsole-launch "#emr-cluster-v2policy-awsconsole-launch").

To use managed policies, pass the user tag
`for-use-with-amazon-emr-managed-policies = true` when you
provision a cluster with the CLI, SDK, or another method.

When you pass the tag, Amazon EMR propagates the tag to private subnet ENI, EC2
instance, and EBS volumes that it creates. Amazon EMR also automatically tags
security groups that it creates. However, if you want Amazon EMR to launch with a
certain security group, you must tag it. For resources that are not created by
Amazon EMR, you must add tags to those resources. For example, you must tag Amazon EC2
subnets, EC2 security groups (if not created by Amazon EMR), and VPCs (if you want
Amazon EMR to create security groups). To launch clusters with v2 managed policies in
VPCs, you must tag those VPCs with the predefined user tag. See, [Considerations for
using the Amazon EMR console to launch clusters with v2 managed policies](#emr-cluster-v2policy-awsconsole-launch "#emr-cluster-v2policy-awsconsole-launch").

###### Propagated user-specified tagging

Amazon EMR tags resources that it creates using the Amazon EMR tags that you specify
when creating a cluster. Amazon EMR applies tags to the resources it creates
during the lifetime of the cluster.

Amazon EMR propagates user tags for the following resources:

- Private Subnet ENI (service access elastic network interfaces)
- EC2 Instances
- EBS Volumes
- EC2 Launch Template

###### Automatically-tagged security groups

Amazon EMR tags EC2 security groups that it creates with the tag that is
required for v2 managed policies for Amazon EMR,
`for-use-with-amazon-emr-managed-policies`, regardless of
which tags you specify in the create cluster command. For a security group
that was created before the introduction of v2 managed policies, Amazon EMR does
not automatically tag the security group. If you want to use v2 managed
policies with the default security groups that already exist in the account,
you need to tag the security groups manually with
`for-use-with-amazon-emr-managed-policies = true`.

###### Manually-tagged cluster resources

You must manually tag some cluster resources so that they can be accessed
by Amazon EMR default roles.

- You must manually tag EC2 security groups and EC2 subnets with the
  Amazon EMR managed policy tag
  `for-use-with-amazon-emr-managed-policies`.
- You must manually tag a VPC if you want Amazon EMR to create default
  security groups. EMR will try to create a security group with the
  specific tag if the default security group doesn't already exist.

Amazon EMR automatically tags the following resources:

- EMR-created EC2 Security Groups

You must manually tag the following resources:

- EC2 Subnet
- EC2 Security Groups

Optionally, you can manually tag the following resources:

- VPC - only when you want Amazon EMR to create security groups

## Considerations for

using the Amazon EMR console to launch clusters with v2 managed policies

You can provision clusters with v2 managed policies using the Amazon EMR console.
Here are some considerations when you use the console to launch Amazon EMR
clusters.

- You do not need to pass the predefined tag. Amazon EMR automatically adds
  the tag and propagates it to the appropriate components.
- For components that need to be manually tagged, the old Amazon EMR console
  tries to automatically tag them if you have the required permissions to
  tag resources. If you don’t have the permissions to tag resources or if
  you want to use the console, ask your administrator to tag those
  resources.
- You cannot launch clusters with v2 managed policies unless all the
  prerequisites are met.
- The old Amazon EMR console shows you which resources (VPC/Subnets) need to
  be tagged.

## AWS managed policies for

Amazon EMR

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.
