

# Terminating agreements for your organization in AWS Artifact
<a name="terminate-org-agreement"></a>

If you used the AWS Artifact console to [accept an agreement on behalf of all member accounts in an organization in AWS Organizations](accept-org-agreement.md), then you can use the console to terminate that agreement. Otherwise, see [Offline agreements in AWS Artifact](manage-offline-agreement.md).

If a member account is removed from an organization, then that member account is longer covered by organization agreements. Before removing member accounts from an organization, a management account administrator should communicate this to member accounts so that they can put new agreements in place if necessary. You can view a list of active organization agreements in the AWS Artifact console on the **Agreements** page, under [Organization agreements](https://console.aws.amazon.com/artifact/home?#!/agreements?tab=organizationAgreements).

For more information about AWS Organizations, see [Managing accounts in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html) in the *AWS Organizations User Guide*.

**Required permissions**  
To terminate an agreement, the owner of the management account must have the required [permissions](example-iam-policies.md#example-policy-manage-terminate-agreements).

For more information, see [Identity and access management in AWS Artifact](security-iam.md).

**To terminate your online organization agreement with AWS**

1. Open the AWS Artifact console at [https://console.aws.amazon.com/artifact/](https://console.aws.amazon.com/artifact/). 

1. On the AWS Artifact dashboard, choose **Agreements**.

1. Choose the **Organization agreements** tab.

1. Select the agreement and choose **Terminate agreement**.

1. Select all checkboxes to indicate that you agree to terminate the agreement.

1. Choose **Terminate**. When prompted for confirmation, choose **Terminate**.