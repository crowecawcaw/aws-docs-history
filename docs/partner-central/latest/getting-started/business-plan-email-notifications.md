

# Email notifications

AWS Partner Central sends email notifications when a business plan is created for your AWS account and when the status of a plan changes to activated, canceled, or completed. For the notifications and what they contain, see [Identifying business plan emails](#business-plan-email-types).

AWS Partner Central sends these notifications through AWS User Notifications, as AWS managed notifications. They appear in the Console Notification Center, and they go to the root user email address and the alternate contacts of your AWS account. You can choose which contacts receive them, and you can add delivery channels such as the AWS Console Mobile Application and Amazon Q Developer in chat applications. For more information, see [Managing email notifications](#business-plan-email-manage).

Business plan email notifications follow these rules:
+ Only plans in the AWS catalog send email notifications. Plans in the Sandbox catalog don't.
+ Submitting a plan for review doesn't send an email notification.
+ The emails don't include an unsubscribe link. To stop receiving them, change your subscriptions in AWS User Notifications.

**Note**  
Business plan email notifications come from `partner-central@aws.com`. If you don't receive them, check your spam folder or your email settings.

**Topics**
+ [Identifying business plan emails](#business-plan-email-types)
+ [Understanding email notification fields](#business-plan-email-fields)
+ [Managing email notifications](#business-plan-email-manage)

## Identifying business plan emails
<a name="business-plan-email-types"></a>

The following table shows the email notifications for business plans. Each email includes a link to the plan in AWS Partner Central. In the titles, {{plan year}} is the plan year of the business plan, such as 2027.


| Email | Event | Title | Fields | 
| --- | --- | --- | --- | 
| Business Plan Created | A business plan is created for your AWS account. | Your {{plan year}} business plan was created | Partner, Plan name, Plan ID, Plan year | 
| Business Plan Status Changed – activated | The plan passes review, and its status changes to Active. | Your {{plan year}} business plan is now activated | Partner, Plan name, Plan ID, Plan year, Status | 
| Business Plan Status Changed – canceled | The plan is canceled. | Your {{plan year}} business plan was canceled | Partner, Plan name, Plan ID, Plan year, Status | 
| Business Plan Status Changed – completed | The plan year ends, and the status of the plan changes to Completed. | Your {{plan year}} business plan is now completed | Partner, Plan name, Plan ID, Plan year, Status | 

## Understanding email notification fields
<a name="business-plan-email-fields"></a>

With business plan emails, the contacts of your AWS account stay informed when a plan is created and when its status changes, so you don't need to check AWS Partner Central for these changes. Each email shows a set of fields that identify the plan and, for a status change, its new status. The following table describes each field.


| Field | Description | 
| --- | --- | 
| Partner | The name of your company in AWS Partner Central. | 
| Plan name | The name of the business plan. | 
| Plan ID | The ID of the business plan, such as bp-a1b2c3d4e5f6g. | 
| Plan year | The calendar year in which the plan ends. | 
| Status | The new status of the plan, which is Active, Canceled, or Completed. | 

The **Business Plan Created** email also states the date on which the plan ends.

## Managing email notifications
<a name="business-plan-email-manage"></a>

Use the AWS User Notifications console to manage business plan email notifications together with the other AWS Partner Central managed notifications. Viewing and changing AWS managed notifications requires read and read-write permissions in AWS User Notifications. For more information, see [Resource-level permissions in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html) in the *AWS User Notifications User Guide*.

Use the console for the following tasks:
+ Add or remove the account contacts that receive the notifications. For instructions on adding and removing account contacts, see [Adding and removing account contacts for AWS managed notifications in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/Add-remove-account-contacts.html) in the *AWS User Notifications User Guide*.
+ Send the notifications to other delivery channels. For instructions on adding delivery channels, see [Delivery channels for AWS managed notifications in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/delivery-channels-managed-notifications.html) in the *AWS User Notifications User Guide*.
+ View the notifications that you received. For instructions on viewing your notifications, see [Viewing AWS managed notifications in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/viewing-managed-notifications.html) in the *AWS User Notifications User Guide*.