

# Provisioning users for AWS Quick


|  | 
| --- |
|    Applies to: Enterprise Edition and Standard Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators and AWS Quick administrators  | 

## Self-provisioning an AWS Quick administrator
<a name="assigning-the-admin"></a>

AWS Quick administrators are users who can also manage AWS Quick features such as account settings and accounts. They can also purchase additional AWS Quick user subscriptions, purchase [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html), and cancel the subscription to AWS Quick for your AWS account.

You can use an AWS user or group policy to give users the ability to add themselves as administrators of AWS Quick. Users that have been granted this ability can only add themselves as administrators and can't use this policy to add others. Their accounts become active and billable the first time that they open AWS Quick. To set up self-provisioning, give these users permission to use the `quicksight:CreateAdmin` action. 

Alternatively, you can use the following procedure to use the console to set or create the administrator for AWS Quick. 

**To make a user the AWS Quick administrator**

1. Create the AWS user:
   + Use IAM to create the user that you want to be the administrator of AWS Quick. Alternatively, identify an existing user in IAM for the administrator role. You can also put the user inside a new group, for manageability. 
   + Grant the user (or group) sufficient permissions. 

1. Sign in to your AWS Management Console with the target user's credentials.

1. Go to [http://quicksight.aws.amazon.com/sn/console/get-user-email](http://quicksight.aws.amazon.com/sn/console/get-user-email), type in the target user's email address, and choose **Continue**.

On success, the target user is now an administrator in AWS Quick.

## Self-provisioning an AWS Quick author
<a name="self-service-access"></a>

AWS Quick authors can create data sources, datasets, analyses, and dashboards. They can share analyses and dashboards with other AWS Quick users in your AWS Quick account. However, they don't have access to the **Manage AWS Quick** menu. They can't change account settings, manage accounts, purchase additional AWS Quick user subscriptions or [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) capacity, or cancel the subscription to AWS Quick for your AWS account. Author Pro users can additionally create content using natural language, build knowledge bases, configure actions, and access advanced automation capabilities.

You can use an AWS user or group policy to give users the ability to create an AWS Quick author account for themselves. Their accounts become active and billable the first time they open AWS Quick. To set up self-provisioning, you need to give them permission to use the `quicksight:CreateUser` action. 

## Self-provisioning an AWS Quick read-only user
<a name="self-service-read-only-users"></a>

AWS Quick Essentials (Readers) or AWS Quick Professional (Reader Pro) users can view and manipulate dashboards that are shared with them, but they can't make any changes or save a dashboard for further analysis. AWS Quick readers can't create data sources, datasets, analyses, or visuals. They can't do any administrative tasks. Choose this role for people who are consumers of the dashboards but don't author their own analysis, for example, executives. Both Essentials (Reader) and Professional (Reader Pro) users now have access to AWS Quick AI features.

If you are using Microsoft Active Directory with AWS Quick, you can manage read-only permissions by using a group. Otherwise, you can bulk-invite users to use AWS Quick. You can also use an AWS user or group policy to give people the ability to create an AWS Quick reader account for themselves. 

Reader accounts become active and billable the first time they open AWS Quick. If you decide to upgrade or downgrade a user, billing for that user is prorated for the month. To set up self-provisioning, you need to give them permission to use the `quicksight:CreateReader` action. For complete details about when billing begins, proration, and what happens when you remove a user, see [Understanding AWS Quick user billing](understanding-quick-user-billing.md).

Readers that are used to automatically or programmatically refresh dashboards for near real-time use cases must choose capacity pricing. For readers under user pricing, each reader is limited to manual use by one individual only. 