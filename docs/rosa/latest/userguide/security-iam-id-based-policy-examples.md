# ROSA identity-based policy examples

By default, IAM users and roles don’t have permission to create or modify AWS resources.
They also can’t perform tasks using the AWS Management Console, AWS CLI, or AWS API.
An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need.
The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_.

## Using the ROSA console

To subscribe to ROSA from the console, your IAM principal must have the required AWS Marketplace permissions.
The permissions allow the principal to subscribe and unsubscribe to the ROSA product listing in AWS Marketplace and view AWS Marketplace subscriptions.
To add the required permissions, go to the [ROSA console](https://console.aws.amazon.com/rosa "https://console.aws.amazon.com/rosa") and attach the AWS managed policy `ROSAManageSubscription` to your IAM principal.
For more information about `ROSAManageSubscription`, see [AWS managed policy: ROSAManageSubscription](security-iam-awsmanpol.md#security-iam-awsmanpol-rosamanagesubscription "security-iam-awsmanpol.md#security-iam-awsmanpol-rosamanagesubscription").

## Authorizing ROSA with HCP to manage AWS resources

ROSA with hosted control planes (HCP) uses AWS managed policies with permissions that are required for service operation and support.
You use the ROSA CLI or IAM console to attach these policies to service roles in your AWS account.

For more information, see [AWS managed policies for ROSA](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Authorizing ROSA classic to manage AWS resources

ROSA classic uses customer managed IAM policies with permissions that are pre-defined by the service.
You use the ROSA CLI to create these policies and attach them to service roles in your AWS account.
ROSA requires that these policies are configured as defined by the service to ensure continuous operation and service support.

###### Note

You should not alter ROSA classic policies without first consulting Red Hat.
Doing so may void Red Hat’s 99.95% cluster uptime service-level agreement.
ROSA with hosted control planes uses AWS managed policies with a more limited set of permissions.
For more information, see [AWS managed policies for ROSA](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

There are two types of customer managed policies for ROSA: account policies and operator policies.
Account policies are attached to IAM roles that the service uses to establish a trust relationship with Red Hat for site reliability engineer (SRE) support, cluster creation, and compute functionality.
Operator policies are attached to IAM roles that OpenShift operators use for cluster operations related to ingress, storage, image registry, and node management.
Account policies are created once per AWS account, whereas operator polices are created once per cluster.

For more information, see [ROSA classic account policies](security-iam-rosa-classic-account-policies.md "security-iam-rosa-classic-account-policies.md") and [ROSA classic operator policies](security-iam-rosa-classic-operator-policies.md "security-iam-rosa-classic-operator-policies.md").

## Allow users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.
This policy includes permissions to complete this action on the console or programmatically using the AWS CLI.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Effect": "Allow",
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
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
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```
