# Managing subscriptions for

applications using IAM Federation

To manage user subscriptions added to an application environment, you can perform the
following actions:

###### Actions

- [Updating subscription
  tiers](#update-user-subscriptions-tier-iam "#update-user-subscriptions-tier-iam")
- [Unsubscribing a user](#delete-user-subscriptions-iam "#delete-user-subscriptions-iam")
- [Listing user subscriptions](#list-user-subscriptions-iam "#list-user-subscriptions-iam")

## Updating subscription

tiers

You can update a subscription tier using the AWS Management Console or the [UpdateSubscription](../api-reference/API_UpdateSubscription.md "../api-reference/API_UpdateSubscription.md") API
operation.

Amazon Q Business automatically assigns subscriptions to users in an
IAM-federated application. You can update the auto-subscription tier for your
application. When you update the auto-subscription tier for the Amazon Q Business application, the new tier applies to new users logging into
your web experience. Existing subscription types assigned to users don't get
updated when you update your subscription tier.

You can also update the subscription tier for specific users already assigned
subscriptions.

For more information on user subscriptions for an IAM federated Amazon Q Business application, see [Subscriptions for applications using IAM
Federation](tiers.md#managing-sub-tiers-iam "tiers.md#managing-sub-tiers-iam").

Console
**To update auto-subscription tier for an
Amazon Q Business application**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   the application environment that your uploaded files belong to.
3. From your applications page, select **Application
   settings**, and then select
   **Edit**.
4. From **Update application**, under
   **Default subscription settings**, in
   **Subscription tier**, choose between
   **Q Business Pro** and **Q
   Business Lite**.
5. Select **Update**.

**To update a specific user's
subscription**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. In **Applications**, select the name of
   the application environment.
3. From your applications page, select **User
   access** and then select **Manage user
   access**.
4. On the **Manage access and
   subscriptions** page, from
   **Users**, select the user whose
   subscription you want to change and then select
   **Edit subscription**.
5. From the **Confirm subscription change**
   dialog box, from **New subscription**, and
   choose a new subscription tier.
6. Then, select **Confirm**.
7. On the **Manage access and
   subscriptions** page, select
   **Confirm** again.

AWS CLI
**To update user or group
subscriptions**

```

aws qbusiness update-subscription \
--application-id `application-id` \
--subscription-id `subscription-id` \
--type `subscription-type`
```

## Unsubscribing a user

When you remove a user, it cancels their subscription. The user continues to
be visible in the list of users till the end of the month, after which they're
removed from the list. An unsubscribed user can continue to use the application
until the end of the month on their canceled subscription.

You can choose to re-activate and re-assign a subscription to an inactive user
from the subscriptions list. When an unsubscribed user re-logs into a Amazon Q Business application, Amazon Q Business automatically
re-assigns them a subscription based on the active subscription tier for your
application. However, an unsubscribed user can continue to use the application
until the end of the month of their canceled subscription. So, if they start
re-using Amazon Q Business in the same month their subscription is
canceled, they will keep the same subscription tier they were originally
assigned during that month. You must cancel a subscription for a user removed
from your identity provider to stop subscription charges for them.

If an unsubscribed user wants to maintain the subscription beyond the first
month, and they start using Amazon Q Business again next month, then they
will get assigned the default subscription tier of their application (which
could be a different subscription tier than the one they were assigned
originally).

Console
**To unsubscribe a user from an Amazon Q Business application environment**

1. From your Amazon Q Business application home page,
   scroll down to the **Users** section,
   select **Manage user access**.
2. On the **Manage subscriptions** page,
   from **Users**, select
   **Remove**.
3. From the **Unsubscribe and remove** box,
   choose **Done**.

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
2. Sign in to the AWS Management Console and open the Amazon Q Business console.
3. From the left navigation menu, choose
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
