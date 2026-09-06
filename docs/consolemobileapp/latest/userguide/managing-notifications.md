

# Push notifications
<a name="managing-notifications"></a>

You can use Notifications in the Console Mobile Application to create actionable push notifications from AWS services, such as CloudWatch. These notifications can be delivered to your mobile device when a resource requires your attention. Enabling push notifications requires you to [share your device ID with AWS](data-protection.md#data-privacy). Use this tutorial to get started with and manage your push notifications in the Console Mobile Application.

**Note**  
Push notifications depend on external services, such as Apple and Google messaging services. In the event of a service outage, AWS can’t guarantee the reliability or timeliness of notification delivery.

## Prerequisites
<a name="prerequisites"></a>

Before you begin, be sure that you’ve completed the steps in [Getting started with the AWS Console Mobile Application](getting-started.md).

To receive push notifications, you must have the appropriate AWS User Notifications permissions. For more information, see [Resource-level permissions](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html) in the *AWS User Notifications User Guide*.

## Step 1: Get started with push notifications
<a name="step-1-get-started-with-push-notifications"></a>

To receive notifications about resources of interest, you must allow push notifications and create or subscribe to an existing notification configuration. A notification configuration is a container of your selected services and event rules. An event rule specifies what event generates a notification.

 **To create new notification configurations** 

1. In the Console Mobile Application, from the tab menu at the bottom of your device, choose **Notifications**.

1. Choose **Agree**.

1. Choose **Allow**.

1. Set up notification configurations as follows:
**Tip**  
If someone in your account has already created notification configurations, you can use them by choosing **Select existing**. For more information, see the next procedure.

   1. Choose **Create new**.

   1. Enter a name.

   1. (Optional) Enter a description.
**Tip**  
Using distinct descriptions helps other account users differentiate alarms.

   1. Select a Region.

   1. (Optional) Select alarms.
**Note**  
Choosing **Specific alarms** allows you to select individual alarms to receive notifications for. Choosing **All alarms** selects all available alarms in the account. Note that choosing **All alarms** can result in increased notifications.

   1. Choose **Next**.

1. View your selected notification configurations.

 **To select existing notification configurations** 

1. In the Console Mobile Application, from the tab menu at the bottom of your device, choose **Notifications**.

1. Choose **Agree**.

1. Choose **Allow**.

1. Set up notification configurations as follows:

   1. Choose **Select existing**.

   1. Select notification configurations by choosing the plus sign (**\+**).

   1. View your selected notification configurations.

**Note**  
You can view other notification configurations by choosing the **All** tab. You can always return and modify previously selected notification preferences from this screen. If you deselect a notification configuration, you won’t receive push notifications for it.

## Step 2: Viewing notifications
<a name="step-2-viewing-notifications"></a>

You can view console notifications directly in the Console Mobile Application.

**Note**  
Whenever a new notification is available, the bell icon in the tab menu shows a blue badge.  
If you log out of the application, you will still receive push notifications on your device. You must sign back in to the application to view its details.

 **To view your notifications** 

1. Open the Console Mobile Application.

1. From the tab menu at the bottom of your device, choose **Notifications**.

1. Select a notification in your inbox to view additional details.

## Managing notifications
<a name="managing-notifications-2"></a>

You can manage your notifications in any of the following ways:

### Subscribing to a notification configuration
<a name="subscribing-to-a-notification-configuration"></a>

You can generate push notifications from existing notification configurations in your account by selecting them.

 **To subscribe to an existing notification configuration** 

1. In the Console Mobile Application, from the tab menu at the bottom of your device, choose **Notifications**.

1. Choose **Configurations**.

1. In the **All** tab, select notification configurations by choosing the plus sign (**\+**).

### Unsubscribing from a notification configuration
<a name="unsubscribing-from-a-notification-configuration"></a>

If you no longer wish to receive push notifications for an existing configuration, you can unsubscribe.

 **To unsubscribe from an existing notification configuration** 

1. In the Console Mobile Application, from the tab menu at the bottom of your device, choose **Notifications**.

1. Choose **Configurations**.

1. In the **Selected** tab, deselect notification configurations by choosing the green checkmark icon.

### Deleting a notification configuration
<a name="deleting-a-notification-configuration"></a>

If you no longer need a notification configuration, you can delete it.

**Warning**  
Deleting a notification configuration removes it from the account.

 **To delete a notification configuration** 

1. In the Console Mobile Application, from the tab menu at the bottom of your device, choose **Notifications**.

1. Choose **Configurations**.

1. Locate and choose the notification configuration.

1. Choose the vertical ellipsis icon.

1. Choose **Delete**.

**Note**  
You can also manage your mobile device’s push notifications from the AWS User Notifications console by adding your mobile device as a delivery channel, but this requires additional permissions. For more information, see [Listing mobile devices as delivery channels](permissions-policies.md).