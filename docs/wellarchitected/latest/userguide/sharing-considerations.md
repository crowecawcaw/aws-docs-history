# Considerations when sharing AWS Well-Architected Tool workloads

A workload can be shared with up to 20 different AWS accounts and users. A
workload can only be shared with accounts and users that are in the same AWS Region
as the workload.

To share a workload in a Region introduced after March 20, 2019, both you and the
shared AWS account must enable the Region in the AWS Management Console. For more information,
refer to [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

You can share a workload with an AWS account, individual users in an account,
or both. When you share a workload with an AWS account, all users in that
account are given access to the workload. If only specific users in an account
require access, follow the best practice of granting least privilege and share the
workload individually with those users.

If both an AWS account and a user in the account have workload invitations, the
workload invitation with the highest level permissions determines the user's
permission to the workload. If you delete the workload invitation for the user, the
user's access is determined by the workload invitation for the AWS account. Delete
both workload invitations to remove the user's access to the workload.

Before sharing a workload with an organization or one or more organization units (OUs),
you must enable AWS Organizations access.

If you share a workload with both an organization and one or more OUs,
the workload invitation with the highest level permissions determines the account's permission to the
workload.

###### To enable AWS Organizations sharing

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/ "https://console.aws.amazon.com/wellarchitected/").
2. In the left navigation pane, choose **Settings**.
3. Choose **Enable AWS Organizations support**.
4. Choose **Save settings**.
