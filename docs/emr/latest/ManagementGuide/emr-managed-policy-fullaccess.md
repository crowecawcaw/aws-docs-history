# IAM managed policy for full

access (on path to deprecation)

The `AmazonElasticMapReduceFullAccess` and
`AmazonEMRFullAccessPolicy_v2` AWS Identity and Access Management (IAM) managed policies
grant all the required actions for Amazon EMR and other services.

###### Important

The `AmazonElasticMapReduceFullAccess` managed policy is on the
path to deprecation, and no longer recommended for use with Amazon EMR. Instead,
use [AmazonEMRFullAccessPolicy_v2](emr-managed-policy-fullaccess-v2.md "emr-managed-policy-fullaccess-v2.md"). When the IAM
service eventually deprecates the v1 policy, you won't be able to attach it
to a role. However, you can attach an existing role to a cluster even if
that role uses the deprecated policy.

The Amazon EMR full-permissions default managed policies incorporate `iam:PassRole` security configurations, including the following:

- `iam:PassRole` permissions only for specific default Amazon EMR roles.
- `iam:PassedToService` conditions that allow you to use the policy with only specified AWS services, such as `elasticmapreduce.amazonaws.com` and `ec2.amazonaws.com`.
  You can view the JSON version of the [AmazonEMRFullAccessPolicy_v2](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRFullAccessPolicy_v2 "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRFullAccessPolicy_v2") and [AmazonEMRServicePolicy_v2](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2 "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AmazonEMRServicePolicy_v2") policies in the IAM console. We recommend that you create new clusters with the v2 managed policies.

You can view the contents of the deprecated v1 policy in the AWS Management Console at
[`AmazonElasticMapReduceFullAccess`](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess"). The
`ec2:TerminateInstances` action in the policy grants permission
to the a user or role to terminate any of the Amazon EC2 instances associated with
the IAM account. This includes instances that are not part of an
EMR cluster.
