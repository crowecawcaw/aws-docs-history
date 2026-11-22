

# Business plans

Use a business plan to align your AWS partnership activities with measurable goals for the year. A plan describes your strategy, sets goals, and organizes the work that supports them. If you have an AWS partner development team, you can develop the plan with them.

**Topics**
+ [Plan prerequisites](#business-plans-prerequisites)
+ [Collaborating with AWS on business plans](#business-plans-enable-collaboration)
+ [Creating a draft plan](#business-plans-create)
+ [Adding plan content](#business-plans-build)
+ [Submitting a plan](#business-plans-submit)
+ [Tracking plan progress](#business-plans-track)
+ [Learning more about business plans](#business-plans-learn-more)
+ [Email notifications](business-plan-email-notifications.md)

## Plan prerequisites
<a name="business-plans-prerequisites"></a>

To work with business plans, use an AWS Identity and Access Management (IAM) role that has permission to create and manage business plans, such as a role with the `AWSPartnerCentralFullAccess` managed policy. For more information about this policy, see [AWS managed policy: `AWSPartnerCentralFullAccess`](managed-policies.md#security-iam-awsmanpol-AWSPartnerCentralFullAccess).

If **Business plans** isn't in the navigation pane of the AWS Partner Central console, your account doesn't have business planning yet. Check back later.

## Collaborating with AWS on business plans
<a name="business-plans-enable-collaboration"></a>

With AWS Partner Central, your organization owns the business plans in your AWS account. Turn on AWS collaboration so that your AWS partner development team can create and update your plans with you. You can also create a draft plan first and turn on AWS collaboration later.

**Important**  
AWS collaboration applies to all current and future business plans in the account. You can't limit it to specific plans. Before you turn it on, make sure that you want your AWS partner development team to work on every plan in the account.

To turn on AWS collaboration, create the business plan service-linked role. You do this on the **Service roles** tab of the AWS Partner Central settings page. Until you turn it on, the **Business plans** page shows a banner whose button opens that tab. For the steps, the permissions that you need, and what to do if an error appears, see [Managing service-linked roles for business plans](using-roles-for-partner-central-account.md).

To turn off AWS collaboration, on the **Service roles** tab, in the **Business plan service-linked roles** section, choose **Disconnect**, and then confirm. After you turn it off, your business plans stay available to your organization. Your AWS partner development team can still view them, but it can't create or update them. The service-linked role stays in your account. You can turn on AWS collaboration again at any time.

For instructions on starting your first plan, see [Creating a draft plan](#business-plans-create).

## Creating a draft plan
<a name="business-plans-create"></a>

Create a draft plan to start planning for an upcoming plan year. Each plan covers one plan year and one scope, such as **Global** or one country. Before you begin, make sure that you have the permissions described in [Plan prerequisites](#business-plans-prerequisites).

**To create a draft plan**

1. Open the [AWS Partner Central Business plans page](https://console.aws.amazon.com/partnercentral/business-plans), which lists your plans and their statuses.

1. On the **Business plans** page, choose **Create plan**.

1. For **Plan name**, enter a name for the plan.

1. For **Plan year** and **Scope**, select the year and the scope of the plan.

1. Choose **Create draft plan**.

The plan appears on the **Business plans** page with the status **Draft**. If you get a permissions error when you choose **Create draft plan**, check that your role has the permissions described in [Plan prerequisites](#business-plans-prerequisites).

Edit the draft while you write its content. When the plan is ready, submit it for review.

## Adding plan content
<a name="business-plans-build"></a>

Each plan has the following tabs. Use them to describe your priorities and the work needed to achieve your goals.

**Attachments**  
Add documents that give useful context for the plan.

**Goals**  
Set goals and key performance indicators (KPIs) with targets that show how you measure success.

**Initiatives**  
Record the initiatives and activities that support your goals.

**Plan narrative**  
Describe your business priorities and your strategy for growing your AWS partnership.

Review the plan with your AWS partner development team as you define its content, if you have one.

## Submitting a plan
<a name="business-plans-submit"></a>

Submit your plan for review to get it approved, so that it can guide your partnership activities through the year. The **Plan quality score** rates your draft and recommends areas to improve. For more information about plan statuses, see [Tracking plan progress](#business-plans-track).

Before you begin, make sure that the plan has the status **Draft** and that its **Plan quality score** is **Ready to submit** or **Complete**. **Submit for review** is available only at those scores. To raise the score, update the plan as the score recommends.

**To submit a business plan for review**

1. Open the [AWS Partner Central Business plans page](https://console.aws.amazon.com/partnercentral/business-plans).

1. On the **Business plans** page, select the plan name to open the plan.

1. On the plan page, choose **Submit for review**.

1. In the confirmation dialog, choose **Submit plan**.

The plan status changes to **Submitted**. The review includes automated checks and a manual review, so it takes time. You can't edit the plan until the review finishes. To follow its progress, check the plan status on the **Business plans** page.

To edit the plan during the review, choose **Withdraw submission**. The plan returns to **Draft**, and you can submit it again later.

When the review finishes, the plan status changes to **Approved**. If the plan needs changes, its status returns to **Draft**. Update the plan, and then submit it again.

## Tracking plan progress
<a name="business-plans-track"></a>

This section describes how to find your plans, what each plan status means, and how to export a plan. Use the **Business plans** page to follow the status of each plan, and return to your plans during the year to measure your progress.

On the **Business plans** page, each plan shows its **Plan ID**, **Plan name**, **Status**, **Scope**, and **Last updated** date. To find a plan, use *Find business plans* or **Filter year**.

Each plan has one of the following statuses:
+ **Draft**: The plan is new, or it returned from review. You can edit it.
+ **Submitted**: The plan is in review and is read-only.
+ **Approved**: The plan passed review. You can edit it.
+ **Completed**: The plan year ended. The plan is read-only.
+ **Canceled**: You canceled the plan. The plan is read-only.

During the year, compare your results with your goals and KPIs. When your priorities change, update the plan.

To support business reviews, export the plan as a Word document (.docx). On the **Business plans** page, select the plan, and then choose **Export**.

Your plan and progress can also support discussions about your tier in the AWS Partner Network, program eligibility, and customer opportunities.

## Learning more about business plans
<a name="business-plans-learn-more"></a>

For more information about business plans, see the following topics.
+ [Managing service-linked roles for business plans](using-roles-for-partner-central-account.md)
+ [AWS managed policy: `AWSPartnerCentralFullAccess`](managed-policies.md#security-iam-awsmanpol-AWSPartnerCentralFullAccess)
+ [Business plan events](https://docs.aws.amazon.com/partner-central/latest/developer-guide/account-api-events.html#types-of-events) in the *AWS Partner Central Developer Guide*
+ [Email notifications](business-plan-email-notifications.md)