# Storing, processing, and replicating notifications using notification hubs in AWS User Notifications

Notification hubs are an account-level setting that identify the AWS Regions where you
store, process, and replicate notifications. You must select at least one notification hub before
you create any notification configurations. If you have no notification hubs, the console prompts
you to choose at least one before you create a notification configuration. You can also edit
notification hubs from **Notification hubs** in the navigation pane. Currently,
you can select up to three Regions.

###### Note

If you want to manage notification hubs, ensure you have the appropriate permissions. For more information, see [Resource-level permissions in AWS User Notifications](resource-level-permissions.md "resource-level-permissions.md").

###### Important

Notification hubs only set the Regional boundaries of notifications. User Notifications stores the
notification configuration's data in the default Region, US East (N. Virginia). This data is also
stored in individual Regions that you have configured rules for. For example, say that you create
a configuration that receives Amazon CloudWatch Alarm notifications about events in
Europe (Milan) and Europe (Frankfurt). User Notifications creates the notification configuration in
US East (N. Virginia). It then replicates the configuration to Europe (Milan) and
Europe (Frankfurt).

###### Important

User Notifications uses Amazon Simple Email Service (Amazon SES) API endpoints to deliver email notifications. Amazon SES API
endpoints aren't available in all
Regions.
For a list of Regions that support Amazon SES API endpoints, see [Amazon Simple Email Service endpoints and quotas](../../../general/latest/gr/ses.md#ses_region "../../../general/latest/gr/ses.md#ses_region") in the
_Amazon Web Services General Reference_. User Notifications routes emails about events originating from
Regions that aren't supported as Amazon SES API endpoints through US East (N. Virginia). If wanted, you
can turn off the receipt of notification for events that originate in Regions that Amazon SES API
endpoints don't support. To do so, don't configure emails for notification configurations that
contain events in these Regions.

###### Topics

- [Adding or removing a notification hub in AWS User Notifications](nhr-add-remove.md "nhr-add-remove.md")
- [Enabling or disabling opt-in Regions in AWS User Notifications](nhr-optin-out.md "nhr-optin-out.md")
