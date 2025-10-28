**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Creating an email orchestration

sending role in Amazon Pinpoint

Amazon Pinpoint uses your Amazon SES resources for sending email messages that are either part of a
campaign or a journey. To set up Amazon Pinpoint to use your Amazon SES resources to send email, create or
update an IAM role to grant Amazon Pinpoint access.

###### Note

You only have to create an **Orchestration sending role arn** if
you're sending emails from a campaign or a journey. For direct send email, you must have
permissions for `ses:SendEmail` and `ses:SendRawEmail`.

###### Create orchestration sending role arn

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you want to
   update email settings for.
3. In the navigation pane, under **Settings**, choose
   **Email**.
4. On the **Identities** tab, choose
   **Edit**.
5. Choose **Enable campaigns and journeys for this email
   channel**.
6. For **IAM role** choose either:
   - **Create a new role** (Recommended) – To have Amazon Pinpoint
     create the IAM role and configure the IAM roles permissions. Enter a
     name for the IAM role in **IAM role name**.
   - **Use an existing role** – If you have an existing
     IAM role that already contains permissions to allow Amazon Pinpoint access to
     `ses:SendEmail` and `ses:SendRawEmail` then choose
     that IAM role from the drop down list. If you need to create the IAM
     role, see [IAM role for sending email through Amazon SES](../developerguide/permissions-ses.md "../developerguide/permissions-ses.md")
     in the [Amazon Pinpoint Developer Guide](../developerguide.md "../developerguide.md").

7. Choose **I acknowledge that the IAM role I selected has the required
   permissions.**
8. Choose **Save**.

## Deleting an email

orchestration sending role in Amazon Pinpoint

You can delete the **Orchestration sending role arn** when you don't
want to send email messages for the project. To delete the **Orchestration
sending role arn**, delete the email channel from the project.

###### Important

This action deletes the email channel from your project. Only do this if you don't
want to send emails from a campaign or a journey.

To delete the email channel, use the [delete-email-channel](../../../cli/latest/reference/pinpoint/delete-email-channel.md "../../../cli/latest/reference/pinpoint/delete-email-channel.md") command:

```
`aws pinpoint delete-email-channel --application-id `application-id``
```

Where:

- _application-id_ is the ID of the Amazon Pinpoint
  project that contains the email channel.

The response to this command is the JSON definition of the email channel that you
deleted.

## Find your email

orchestration sending role ARN in Amazon Pinpoint

For Amazon Pinpoint to begin email through Amazon SES, delegate the required permissions to Amazon Pinpoint.
When the IAM role is set up, Amazon Pinpoint uses the **Orchestration sending role
arn** to send email through Amazon SES. If the **Orchestration sending
role arn** is present, then the project has delegated the permissions to
Amazon Pinpoint.

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to update email settings for.
3. In the navigation pane, under **Settings**, choose
   **Email**.
4. On the **Identities** tab, you can view your
   **Orchestration sending role arn**.
