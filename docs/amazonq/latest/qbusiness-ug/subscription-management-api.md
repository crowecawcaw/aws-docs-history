

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Managing subscriptions for an Amazon Q Business application using APIs
<a name="subscription-management-api"></a>

Amazon Q Business provides APIs to manage subscriptions in your Amazon Q Business application. You can use these APIs to implement your own subscription management solution if you create a Amazon Q Business application environment programmatically.

**Note**  
As of Dec 17, 2024, Amazon Q Business will recognize all email addresses as case-insensitive and recognize subaddresses as equivalent to the original email address. For example, JohnDoe@example.com, johndoe@example.com, and johndoe\+work@example.com will be considered the same email address. For assistance with applications or to report a concern, contact Support, sign into the [AWS Support Center](https://console.aws.amazon.com/support/home#/) .



| API action | API description | Relevant User Guide topic | 
| --- | --- | --- | 
| [CreateSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateSubscription.html) | Subscribes an IAM Identity Center user or a group to a pricing tier for an Amazon Q Business application  If you're using IAM federation to manage user and group access to Amazon Q Business, subscriptions are created automatically when a user logs in to their Amazon Q Business application.  | +  [Creating an IAM Identity Center-integrated Amazon Q Business application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-app.html) <br />+  [Creating an IAM-federated Amazon Q Business application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html)  | 
| [CancelSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CancelSubscription.html) | Unsubscribes a user or a group from their pricing tier in an Amazon Q Business application | +  [Canceling user subscriptions for IAM Identity Center-integrated applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions.html#delete-user-subscriptions) <br />+  [Canceling user subscriptions for IAM federated applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions-iam.html#delete-user-subscriptions-iam)  | 
| [ListSubscriptions](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListSubscriptions.html) | Lists all subscriptions created in an Amazon Q Business application | +  [Listing user subscriptions for IAM Identity Center-integrated applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions.html#list-user-subscriptions) <br />+  [Listing user subscriptions for IAM federated applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions-iam.html#list-user-subscriptions-iam)  | 
| [UpdateSubscription](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateSubscription.html) | Updates the pricing tier for an Amazon Q Business subscription | +  [Updating user subscriptions for IAM Identity Center-integrated applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions.html#update-user-subscriptions) <br />+  [Updating user subscriptions for IAM federated applications](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/manage-user-subscriptions-iam.html#update-user-subscriptions-tier-iam)  | 