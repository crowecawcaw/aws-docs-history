

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with multipartner opportunities
<a name="working-with-multi-partner-opportunities"></a>

AWS Partners can work together on opportunities with AWS as an active participant.

**Topics**
+ [Engagements and snapshots](#engagements-and-snapshots)
+ [Creating a custom policy for ResourceSnapshotJobRole](#creating-custom-policy-resourcesnapshotjobrole)
+ [Inviting partners to an opportunity](#inviting-partners-to-an-opportunity)
+ [Retrieving engagement invitation details](#retrieving-invitation-details)
+ [Responding to an engagement invitation](#responding-engagement-invitation)
+ [Reviewing and updating multipartner opportunities](#reviewing-and-updating-multipartner-opportunities)
+ [Using snapshots to receive partner updates](#using-snapshots-to-receive-partner-updates)
+ [Viewing engagement members](#viewing-engagement-members)
+ [Monitoring resource snapshot job status](#monitoring-resource-snapshot-job-status)

## Engagements and snapshots
<a name="engagements-and-snapshots"></a>

An *engagement* is a resource owned by AWS for collaboration between multiple AWS Partner accounts and AWS on a customer opportunity. Engagements facilitate secure information sharing among partners and collaboration while maintaining individual opportunity ownership and control. Engagements encompass opportunities that originate from both AWS and partners, with AWS as an active participant. Partners can invite AWS or other partners to join an engagement using `EngagementInvitations`. When invited partners accept, they receive their own opportunity within the same engagement.

Engagement members share progress through snapshots—point in time, immutable copies of specific fields from an underlying resource such as an opportunity. Snapshots are created within the engagement and shared with members. When the underlying resource changes, the owner can create a new snapshot revision to reflect updates. AWS provides snapshot jobs—customer-owned jobs that automatically create new revisions when the resource changes. Once shared, snapshots remain permanently accessible to engagement members.

## Creating a custom policy for ResourceSnapshotJobRole
<a name="creating-custom-policy-resourcesnapshotjobrole"></a>

Collaborating on multi-partner opportunities requires sharing snapshots of your opportunities with other partners in an engagement. To maintain access to the latest opportunity details, you need to create a custom role called `ResourceSnapshotJobRole`. This role allows the system to create snapshots of your opportunities on your behalf and retrieve snapshots from other partners in the same engagement. Without this role, any updates you make to your opportunity will not be visible to other partners in the engagement, and they will continue to see outdated snapshots of your opportunity data.

**Note**  
You can use a name other than `ResourceSnapshotJobRole`. If you use a different name, replace all instances of `ResourceSnapshotJobRole` in the following policies with your policy name. 

To create this role, go to your IAM console and create the `ResourceSnapshotJobRole` role with the following custom trust policy:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "resource-snapshot-job.partnercentral-selling.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

After creating this role, you need to attach the [AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy.html) AWS managed policy, or attach the following permissions policy:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:CreateResourceSnapshot"
            ],
            "Resource": [
                "arn:aws:partnercentral:*::catalog/AWS/engagement/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetOpportunity"
            ],
            "Resource": [
                "arn:aws:partnercentral:*:{{111122223333}}:catalog/AWS/opportunity/*"
            ]
        }
    ]
}
```

------

Replace `{account}` with your AWS account ID.

After you create the `ResourceSnapshotJobRole` role and attach the permissions, you need to set the `ResourceSnapshotJobRole` for your organization. Use the [PutSellingSystemSettings](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_PutSellingSystemSettings.html) action to set the role you created as the `ResourceSnapshotJobRole` for your company (identified by your AWS account):

```
aws-cli/2.13.5 Python/3.11.4 Linux/4.14.255-314-253.539.amzn2.x86_64
Host: partner-central.aws.amazon.com
Content-Type: application/json
  
{
  "ResourceSnapshotJobRoleIdentifier": "arn:aws:iam::{account}:role/ResourceSnapshotJobRole"
}
```

Replace `{account}` with your AWS account ID, and `ResourceSnapshotJobRole` with the name of the role you created. This role will be implicitly assumed by the resource snapshot jobs to access your opportunities and create snapshots for sharing with other partners in the engagement.

## Inviting partners to an opportunity
<a name="inviting-partners-to-an-opportunity"></a>

Partners can collaborate on opportunities that originate from both partners and AWS by initiating an engagement invitation. You can invite a maximum of nine partners to an opportunity. 

**To invite partners to an opportunity**

1. Follow the steps in [Finding and connecting with partners](https://docs.aws.amazon.com/partner-central/latest/sales-guide/partner-connections.html#finding-partners) in the *AWS Partner Central Sales Guide*. You must connect with partners before you can invite them to opportunities. This connection grants mutual access to each other's account IDs, ensuring invitations reach the intended partner account.

1. Use the [StartEngagementFromOpportunityTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartEngagementFromOpportunityTask.html) action to create an engagement and associate an opportunity with it. This asynchronous action performs the following tasks sequentially:

   1. Creates an engagement.

   1. Associates the opportunity with the engagement.

   1. Invokes the [CreateEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateEngagementInvitation.html) action to AWS.

   1. Submits the opportunity to AWS.

   1. Starts the `ResourceSnapshotJob` to create snapshots.

1. Invite other partners to join. 

   1. To get the engagement ID associated with your opportunity, use the [ListEngagementFromOpportunityTasks](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementFromOpportunityTasks.html) action, filtered by the `TaskIdentifier` returned in the previous step.

   1. Use the receiving partner's engagement ID and account ID to send an invitation with `CreateEngagementInvitation`.

A successful invitation sends an engagement invitation created event to the receiving partner.

## Retrieving engagement invitation details
<a name="retrieving-invitation-details"></a>

 When you receive an engagement invitation created event, use the [GetEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetEngagementInvitation.html) action to retrieve the invitation details. The response includes essential information about the customer opportunity associated with the engagement.

Review the invitation details, particularly the `InvitationMessage`, `Project.Title`, `Project.CustomerUseCase`, and `Project.CustomerBusinessProblem` fields. This information provides context about the customer opportunity and the inviting partner's expectations for collaboration.

Use these details to evaluate if you want to pursue the opportunity by accepting or declining the engagement invitation.

## Responding to an engagement invitation
<a name="responding-engagement-invitation"></a>

When a partner sends you an engagement invitation, it creates an engagement invitation created event that notifies you of the invitation. You have the option to accept or reject the invitation. This decision determines your involvement in the multipartner opportunity. 

**To reject an engagement invitation:**  
Use the [RejectEngagementInvitation](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_RejectEngagementInvitation.html) action to reject the invitation. You must provide a `RejectionReason` parameter explaining your decision. Once rejected, you lose access to the invitation details, and an engagement invitation rejected event notifies the sending partner that you have rejected their invitation.

**To accept an engagement invitation:**  
To accept the invitation and proceed with the multipartner opportunity, use the [StartEngagementByAcceptingInvitationTask](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartEngagementByAcceptingInvitationTask.html) action. This asynchronous action performs the following tasks sequentially:

1. Accepts the engagement invitation.

1. Creates a new opportunity in your partner account using data from the sending partner's opportunity. You will receive an opportunity created event.

1. Includes additional details required to identify the customer in your account.

1. Publishes an engagement invitation accepted event which notifies the partner that you have accepted the invitation and have been added to the engagement.

**Expired engagement invitation**  
If you do not respond to an engagement invitation within fifteen days, it expires, and you cannot participate in the multipartner opportunity. An engagement invitation expired event notifies the sending partner that the invitation expired.

**Note**  
 If you still want to collaborate, the sending partner must initiate a new engagement invitation. 

## Reviewing and updating multipartner opportunities
<a name="reviewing-and-updating-multipartner-opportunities"></a>

When a partner initiates an engagement on an opportunity, the review status of the newly created opportunity in the receiving partner's account is determined by the sending partner's opportunity status.

**Opportunity with submitted review status:**  
 If the sending partner's opportunity has `Lifecycle.ReviewStatus` set to `Submitted`, the following process occurs:

1. The new opportunity created in the receiving partner's account will have `Lifecycle.ReviewStatus` set to `Submitted`.

1. The `Submitted` status remains until the sending partner's opportunity is `Approved`.

1. Once the sending partner's opportunity is validated and the `Lifecycle.ReviewStatus` is set to `Approved`, the other partners' opportunities will automatically inherit the `Approved` status.

This process ensures consistent opportunity details across multipartner opportunities, eliminating the need for multiple reviews.

Once complete, an opportunity created event is triggered with the corresponding opportunity ID. Partners can use this ID with the `GetOpportunity` action to retrieve the full opportunity details.

**Opportunity with approved review status:**  
If the sending partner initiates an engagement on an opportunity with `Lifecycle.ReviewStatus` set to `Approved`, the following process occurs:

1. The new opportunity created in the receiving partner's account will have `Lifecycle.ReviewStatus` set to `Approved`.

1. An opportunity created event is triggered with the corresponding opportunity ID.

1. Partners can use the [GetOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html) action with the opportunity ID to retrieve the full opportunity details.

However, the approved opportunity may not have some partner-specific details that were not copied from the sending partner's opportunity. The receiving partner should update these details using the [UpdateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateOpportunity.html) action when the opportunity stage is updated to `Qualified` or a later stage:
+  `Project.CustomerUseCase` 
+  `Project.DeliveryModels` 
+  `Solution` 
+  `PrimaryNeedsFromAws` 
+  `LifeCycle.TargetCloseDate` 
+  `Project.ExpectedCustomerSpend.Amount` 
+  `Project.ExpectedCustomerSpend.Currency` 
+  `Marketing.source` 
+  `Marketing.AwsFundingUsed` 

 Once the opportunity is created in the receiving partner's account, it can be managed and updated like any other opportunity within the partner's system. Partners can use the [UpdateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateOpportunity.html) action to make changes or provide more information about their involvement in the opportunity.

## Using snapshots to receive partner updates
<a name="using-snapshots-to-receive-partner-updates"></a>

Within an engagement, partners maintain and update their opportunities independently. When someone revises an engagement's resources, such as adding an opportunity, an engagement resource snapshot created event is published.

To stay informed about changes and access the most current information from other partners' opportunities, you can use the following actions:
+ [ListEngagementResourceAssociations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementResourceAssociations.html) – Use this action to retrieve the engagement ID associated with the opportunity.
+ [ListResourceSnapshots](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListResourceSnapshots.html) – Use this action to retrieve a comprehensive list of all opportunity snapshots associated with the engagement, providing an overview of available snapshots across all partners. 
+ [GetResourceSnapshot](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetResourceSnapshot.html) – Use this action to obtain real-time summaries of specific opportunity snapshots, allowing you to view the most up-to-date information without directly accessing another partner's opportunity. 

If you identify relevant changes or updates from another partner's opportunity that should be reflected in your own, use the [UpdateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateOpportunity.html) action. This action facilitates selectively incorporating pertinent data into your opportunity, ensuring alignment and consistency across the engagement.

## Viewing engagement members
<a name="viewing-engagement-members"></a>

An engagement on a multipartner opportunity can have up to ten partners. Whenever a new partner accepts the engagement invitation, an engagement member added event is published, notifying all current members about the change.

To view all members collaborating within an engagement, follow these steps:

1.  Use the [ListEngagementResourceAssociations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementResourceAssociations.html) action to retrieve the engagement ID associated with the opportunity. 

1. Provide the ID from step 1 to the [ListEngagementMembers](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementMembers.html) action to fetch the partner details of engagement members.
**Note**  
 Only members of an engagement can invoke the `ListEngagementMembers` action. 

## Monitoring resource snapshot job status
<a name="monitoring-resource-snapshot-job-status"></a>

 When working with multipartner opportunities, you must create a role that allows you to create snapshots of your opportunities for other partners and retrieve opportunity snapshots from other partners in an engagement. Without this role, any updates you make to your opportunity will not be available to other partners in the engagement, and they will continue to see outdated snapshots of your opportunity.

To track the status of resource snapshot jobs associated with a multipartner opportunity in an engagement, follow these steps:

1. Use the [ListEngagementResourceAssociations](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementResourceAssociations.html) action to retrieve the engagement ID associated with the opportunity.

1. Provide the ID from step 1 to the [ListResourceSnapshotJobs](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListResourceSnapshotJobs.html) action to generate a list of all snapshot jobs owned by the caller in the engagement. Retrieve the job ID from the response.

1. Provide the job ID to the [GetResourceSnapshotJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetResourceSnapshotJob.html) action to track the job status and see if it's running.

 The `ResourceSnapshotJob` operation publishes metrics to Amazon CloudWatch for its asynchronous operations. CloudWatch processes the data into readable, near real-time metrics to help you monitor the performance and health of the service. 

 The following metrics are available: 
+  **Faults** – Counts internal issues during job execution. Use this metric to monitor service stability and set alarms for fault thresholds. 
+  **Errors** – Tracks customer-related issues during job processing. This metric helps identify problems with customer inputs or configurations. 
+  **Invocations** – Represents the total number of job invocations, including both successful and failed attempts. Use this to track service usage trends over time. 

**Note**  
 Metrics are reported to CloudWatch only when there is activity in the `ResourceSnapshotJob` service. If there are no jobs or no data for a specific metric, that metric isn't reported. 

 To ensure smooth operation of the `ResourceSnapshotJob` operation: 
+  Use the metrics to verify that the service performs as expected. 
+ Create CloudWatch alarms to monitor metrics and trigger actions (such as sending notifications) when metrics exceed acceptable ranges.
+  Set up proactive monitoring to Identify and resolve issues. 

 For more information about using CloudWatch metrics, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). 