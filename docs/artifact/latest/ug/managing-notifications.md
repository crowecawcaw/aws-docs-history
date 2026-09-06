

# Configuring email notifications in AWS Artifact
<a name="managing-notifications"></a>

**Note**  
The content of this page is only applicable to commercial AWS [Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs_homepage_addtlrcs#region), and does not currently apply to AWS GovCloud (US) Regions.

 You can use the AWS Artifact console to configure email notifications for updates on agreements and reports in AWS Artifact. AWS Artifact sends these email notifications using AWS User Notifications. To receive AWS Artifact email notifications, you must first select AWS User Notifications notification hubs in the User Notifications console. Then, in the AWS Artifact console, you can create a configuration for notification settings, in which you specify your notification recipients and which notifications they receive.

To configure AWS Artifact email notifications, you must have the required permissions for AWS Artifact and AWS User Notifications. For more information, see [Identity and access management in AWS Artifact](security-iam.md).

**Topics**
+ [Prerequisite](#notifications-hubs)
+ [Creating a configuration](notifications-configuration-create.md)
+ [Editing a configuration](notifications-configuration-edit.md)
+ [Deleting a configuration](notifications-configuration-delete.md)

## Prerequisite: Select notification hubs in User Notifications
<a name="notifications-hubs"></a>

Before you can receive AWS Artifact email notifications, you must first open the User Notifications console and select the notification hubs in the AWS Regions where you want to store your User Notifications data. Selecting notification hubs is required for AWS User Notifications, which AWS Artifact uses to send notifications.

**To select notification hubs**

1. Open the [Notification hubs](https://console.aws.amazon.com/notifications/home?#/hub-regions) page of the AWS User Notifications console.

1. Select the notification hubs in the AWS Regions where you want to store your AWS User Notifications resources. By default, your User Notifications data is stored in the US East (N. Virginia) Region. User Notifications replicates your notifications data across the other Regions that you select. For more information, see the [notification hubs documentation](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html) in the *AWS User Notifications User Guide*.

1. Choose **Save and continue**.