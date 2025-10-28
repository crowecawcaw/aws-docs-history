# Configuring email notifications in AWS Artifact

###### Note

The content of this page is only applicable to commercial AWS [Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region"), and does not currently apply to AWS GovCloud (US) Regions.

You can use the AWS Artifact console to configure email notifications for updates on agreements and
reports in AWS Artifact. AWS Artifact sends these email notifications using AWS User Notifications. To receive AWS Artifact
email notifications, you must first select AWS User Notifications notification hubs in the User Notifications console.
Then, in the AWS Artifact console, you can create a configuration for notification settings, in
which you specify your notification recipients and which notifications they receive.

To configure AWS Artifact email notifications, you must have the required permissions for AWS Artifact and
AWS User Notifications. For more information, see [Identity and access management in AWS Artifact](security-iam.md "security-iam.md").

###### Contents

- [Prerequisite](#notifications-hubs "#notifications-hubs")
- [Creating a configuration](notifications-configuration-create.md "notifications-configuration-create.md")
- [Editing a configuration](notifications-configuration-edit.md "notifications-configuration-edit.md")
- [Deleting a configuration](notifications-configuration-delete.md "notifications-configuration-delete.md")

## Prerequisite: Select notification hubs in User Notifications

Before you can receive AWS Artifact email notifications, you must first open the User Notifications console and
select the notification hubs in the AWS Regions where you want to store your User Notifications
data. Selecting notification hubs is required for AWS User Notifications, which AWS Artifact uses to send
notifications.

###### To select notification hubs

1. Open the [Notification hubs](https://console.aws.amazon.com/notifications/home?#/hub-regions "https://console.aws.amazon.com/notifications/home?#/hub-regions") page of the AWS User Notifications console.
2. Select the notification hubs in the AWS Regions where you want to store your AWS User Notifications resources.
   By default, your User Notifications data is stored in the US East (N. Virginia) Region. User Notifications replicates your notifications data
   across the other Regions that you select. For more information, see the [notification hubs documentation](../../../notifications/latest/userguide/notification-hubs.md "../../../notifications/latest/userguide/notification-hubs.md") in the
   _AWS User Notifications User Guide_.
3. Choose **Save and continue**.
