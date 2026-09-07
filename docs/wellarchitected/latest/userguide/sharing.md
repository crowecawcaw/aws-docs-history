

# Sharing your AWS WA Tool resources
<a name="sharing"></a>

To share a resource that you own, do the following:
+ [Activate resource sharing within AWS Organizations](#getting-started-sharing-orgs) (optional)
+ [Share a workload](workloads-sharing.md)
+ [Share a custom lens](lenses-sharing.md)
+ [Share a profile](sharing-profiles.md)
+ [Share a review template](sharing-review-templates.md)

**Notes**  
Sharing a resource makes it available for use by principals outside of the AWS account that created the resource. Sharing doesn't change any permissions that apply to the resource in the account that created it.
AWS WA Tool is a Regional service. The principals that you share with can access resource shares in only the AWS Regions in which they were created.
To share resources in a Region introduced after March 20, 2019, both you and the shared AWS account must enable the Region in the AWS Management Console. For more information, refer to [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## Activate resource sharing within AWS Organizations
<a name="getting-started-sharing-orgs"></a>

When your account is managed by AWS Organizations, you can take advantage of that to share resources more easily. With or without Organizations, a user can share with individual accounts. However, if your account is in an organization, then you can share with individual accounts, or with all accounts in the organization or in an OU without having to enumerate each account.

To share resources within an organization, you must first use the AWS WA Tool console or AWS Command Line Interface (AWS CLI) to enable sharing with AWS Organizations. When you share resources in your organization, AWS WA Tool doesn't send invitations to principals. Principals in your organization gain access to shared resources without exchanging invitations.

When you activate resource sharing within your organization, AWS WA Tool creates a service-linked role called `AWSServiceRoleForWellArchitected`. This role can be assumed by only the AWS WA Tool service, and grants AWS WA Tool permission to retrieve information about the organization it is a member of, by using the AWS managed policy `AWSWellArchitectedOrganizationsServiceRolePolicy`. 

If you no longer need to share resources with your entire organization or OUs, you can disable resource sharing.

**Requirements**
+ You can perform these steps only while signed in as a principal in the organization's management account.
+ The organization must have all features enabled. For more information, see [ Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.

**Important**  
You must turn on sharing with AWS Organizations by using the AWS WA Tool console. This ensures that the `AWSServiceRoleForWellArchitected` service-linked role is created. If you activate trusted access with AWS Organizations by using the AWS Organizations console or the [ enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html) AWS CLI command, the `AWSServiceRoleForWellArchitected` service-linked role isn't created, and you can't share resources within your organization.

**To activate resource sharing within your organization**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

   You must sign in as a principal in the organization's management account.

1. In the left navigation pane, choose **Settings**.

1. Choose **Activate AWS Organizations support**.

1. Choose **Save settings**.

**To disable resource sharing within your organization**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

   You must sign in as a principal in the organization's management account.

1. In the left navigation pane, choose **Settings**.

1. Unselect **Activate AWS Organizations support**.

1. Choose **Save settings**.