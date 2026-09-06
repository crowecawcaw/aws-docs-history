

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Creating an email orchestration sending role in Amazon Pinpoint
<a name="channels-email-orchestration-sending-role"></a>

Amazon Pinpoint uses your Amazon SES resources for sending email messages that are either part of a campaign or a journey. To set up Amazon Pinpoint to use your Amazon SES resources to send email, create or update an IAM role to grant Amazon Pinpoint access.

**Note**  
You only have to create an **Orchestration sending role arn** if you're sending emails from a campaign or a journey. For direct send email, you must have permissions for `ses:SendEmail` and `ses:SendRawEmail`.

**Create orchestration sending role arn**

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. On the **All projects** page, choose the project that you want to update email settings for.

1. In the navigation pane, under **Settings**, choose **Email**.

1. On the **Identities** tab, choose **Edit**.

1. Choose **Enable campaigns and journeys for this email channel**.

1. For **IAM role** choose either:
   + **Create a new role** (Recommended) – To have Amazon Pinpoint create the IAM role and configure the IAM roles permissions. Enter a name for the IAM role in **IAM role name**.
   + **Use an existing role** – If you have an existing IAM role that already contains permissions to allow Amazon Pinpoint access to `ses:SendEmail` and `ses:SendRawEmail` then choose that IAM role from the drop down list. If you need to create the IAM role, see [IAM role for sending email through Amazon SES](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-ses.html) in the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/).

1. Choose **I acknowledge that the IAM role I selected has the required permissions.**

1. Choose **Save**.

## Deleting an email orchestration sending role in Amazon Pinpoint
<a name="channels-email-orchestration-sending-role-delete"></a>

You can delete the **Orchestration sending role arn** when you don't want to send email messages for the project. To delete the **Orchestration sending role arn**, delete the email channel from the project.

**Important**  
This action deletes the email channel from your project. Only do this if you don't want to send emails from a campaign or a journey. 

To delete the email channel, use the [delete-email-channel](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/delete-email-channel.html) command:

```
aws pinpoint delete-email-channel --application-id {{application-id}}
```

Where:
+ *application-id* is the ID of the Amazon Pinpoint project that contains the email channel.

The response to this command is the JSON definition of the email channel that you deleted.

## Find your email orchestration sending role ARN in Amazon Pinpoint
<a name="channels-email-orchestration-sending-role-verify"></a>

For Amazon Pinpoint to begin email through Amazon SES, delegate the required permissions to Amazon Pinpoint. When the IAM role is set up, Amazon Pinpoint uses the **Orchestration sending role arn** to send email through Amazon SES. If the **Orchestration sending role arn** is present, then the project has delegated the permissions to Amazon Pinpoint.

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. On the **All projects** page, choose the project that you want to update email settings for.

1. In the navigation pane, under **Settings**, choose **Email**.

1. On the **Identities** tab, you can view your **Orchestration sending role arn**.