# Managing user subscriptions for IAM Identity Center-integrated applications

To manage user subscriptions added to an application environment, you can perform the
following actions:

###### Actions

- [Updating user subscriptions](#update-user-subscriptions "#update-user-subscriptions")
- [Canceling user or group subscriptions](#delete-user-subscriptions "#delete-user-subscriptions")
- [Listing user subscriptions](#list-user-subscriptions "#list-user-subscriptions")

## Updating user subscriptions

To update a subscription in an Amazon Q Business application, you can
use either the AWS Management Console or the [UpdateSubscription](../api-reference/API_UpdateSubscription.md "../api-reference/API_UpdateSubscription.md") API
operation.

For more information on user subscriptions for an IAM Identity Center-integrated Amazon Q Business application, see [Subscriptions for applications using
IAM Identity Center](tiers.md#managing-sub-tiers-sso "tiers.md#managing-sub-tiers-sso").

Console
**To update user or group subscription
tier**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   the application environment you created.
3. From your applications page, from the **User
   access** section, select **Manage user
   access**.
4. From **Manage access and subscriptions**
   select the subscription you want to update. Then, select
   **Edit subscription**.
5. In the **Confirm subscription change**
   dialog box that opens, from the **New
   subscription** dropdown select **Q
   Business Lite** or **Q Business
   Pro**.
6. Then, select **Confirm**. You will see
   the subscription status notification change next to the user
   you've added the subscription to.
7. Then, select **Confirm** to save your
   changes.

AWS CLI
**To update user or group subscription
tier**

```

aws qbusiness update-subscription \
--application-id `application-id` \
--subscription-id `subscription-id` \
--type `subscription-type`
```

## Canceling user or group subscriptions

To cancel subscriptions, you can use the AWS Management Console or the [CancelSubscription](../api-reference/API_CancelSubscription.md "../api-reference/API_CancelSubscription.md") API
operation.

When you unsubscribe and remove a user or group, it unsubscribes them from the
application environment and removes them from the user list.

For more information on user subscriptions for an IAM Identity Center-integrated Amazon Q Business application, see [Subscriptions for applications using
IAM Identity Center](tiers.md#managing-sub-tiers-sso "tiers.md#managing-sub-tiers-sso").

Console
**To unsubscribe a user or group from an
Amazon Q Business application environment**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   the application environment you created.
3. From your applications page, from the **User
   access** section, select **Manage user
   access**.
4. From **Manage access and subscriptions**
   select the user or group subscription you want to update.
   Then, select **Remove and
   unsubscribe**.
5. Then, from the **Unsubscribe and remove**
   dialog box, **Confirm**.
6. Then, select **Confirm** to save your
   changes.

This step cancels subscriptions for the selected users and
groups and also removes them from your Amazon Q Business application environment.

###### Note

To stop subscription charges for a user, ensure you
have unsubscribed that user from all Amazon Q Business application environments and Quick
instances. For instructions on how to unsubscribe a user
from Quick, see [Unsubscribing from Quick Q](../../../quicksight/latest/user/quicksight-q-unsubscribe.md "../../../quicksight/latest/user/quicksight-q-unsubscribe.md") in the Quick User
Guide.

To stop charges for an Amazon Q Business index,
you must delete either your Amazon Q Business
index or [delete your Amazon Q Business application environment](supported-app-actions.md#delete-app "supported-app-actions.md#delete-app"). If you use
the console, deleting your application environment is the only way
to delete an index associated with it.

AWS CLI
**To cancel user or group subscriptions to
Amazon Q Business**

```

aws qbusiness cancel-subscription \
--application-id `application-id` \
--subscription-id `subscription-id` \
--type `subscription-type`
```

## Listing user subscriptions

To see a list of user and group subscriptions within a specific Amazon Q Business
application, you can use the AWS Management Console or the [ListSubscriptions](../api-reference/API_ListSubscriptions.md "../api-reference/API_ListSubscriptions.md") API
operation.

For a consolidated view of your user subscriptions—including a list of
subscribed users, their subscription status, and applications, accounts, or
services a user can access through their subscriptions—you can also view
the [Amazon Q
subscriptions page](https://console.aws.amazon.com/amazonq/subscriptions "https://console.aws.amazon.com/amazonq/subscriptions").

Console
**To view a list of user and group
subscriptions in an Amazon Q Business
application environment**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   the application environment you created.
3. From your applications page, from the **User
   access** section, select **Manage user
   access**.
4. In the **Manage access and
   subscriptions** select
   **Users** if you want to view user
   subscriptions or **Groups** if you want to
   list group subscriptions.

**To view a consolidated list of all user
and group subscriptions across all Amazon Q Business
application environments**

1. Sign in to the AWS Management Console and open the Amazon Q
   console.
2. From the left navigation menu, choose
   **Subscriptions**,and then select
   **Users** if you want to view user
   subscriptions or **Groups** if you want to
   list group subscriptions.

AWS CLI
**To list user or group subscriptions in an
Amazon Q Business application**

```

aws qbusiness list-subscriptions \
--application-id `application-id`
```

**To list user or group subscriptions across
all Amazon Q Business applications**

This action is not supported.
