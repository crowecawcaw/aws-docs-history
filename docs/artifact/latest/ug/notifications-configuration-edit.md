# Editing a configuration for AWS Artifact notification settings

###### Note

The content of this page is only applicable to commercial AWS [Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region"), and does not currently apply to AWS GovCloud (US) Regions.

After you [create a configuration](notifications-configuration-create.md "notifications-configuration-create.md")
for AWS Artifact notification settings, you can edit the configuration at any time to change
your notification settings. For example, to add or remove recipients, change what types
of notifications they receive, and add or remove tags.

###### To edit a configuration

1. Open the [Notification settings](https://console.aws.amazon.com/artifact/notification "https://console.aws.amazon.com/artifact/notification") page of the AWS Artifact console.
2. Select the configuration that you want to edit.
3. Choose **Edit**.
4. Edit any of the configuration selections and fields. When you're done,
   choose **Save changes**.

If you've added new email addresses as notification recipients, then AWS User Notifications sends a verification
email those email addresses. To verify the email address, in the verification email, the recipient must choose
**Verify email**. Only verified email addresses will receive AWS Artifact notifications.
