**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Create and configure a

project

In Amazon Pinpoint, a _project_ is a collection of settings, customer
information, segments, and campaigns. If you're new to Amazon Pinpoint, the first step you should take
is to create a project.

###### Note

If you've used the Amazon Pinpoint API, you might have seen references to "applications." In
Amazon Pinpoint, a _project_ is the same as an
_application_.

This section shows you how to create a project. As part of this procedure, you verify an
email address and grant Amazon Pinpoint access to use your Amazon SES resources to send email from a
campaign. The verified email address is used as the sender email address when you create
your email campaign later in this tutorial.

## Create and configure a project

The procedures in this section show you how to create a project and verify an email
address.

###### To create a project and verify an email address

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. If this is your first time using Amazon Pinpoint, you see a page that introduces you to
   the features of the service.

In the **Get started** section, enter a name for your
project, and then choose **Create a project**.

###### Note

The project name can contain up to 64 characters. 3. On the **Configure features** page, next to
**Email**, choose **Configure**. 4. For **Email address**, type an email address that you want to
use to send email. For example, you can use your personal email address, or your
work email address. Choose **Verify**. 5. Wait for 1–2 minutes, and then check the inbox for the email address
that you specified in step 4. You should see an email from _Amazon Web Services
(no-reply-aws@amazon.com)_ with the subject line "Amazon Web
Services – Email Address Verification Request in Region
`RegionName`", where
`RegionName` is the name of the AWS Region that
you're configuring Amazon Pinpoint in. 6. Open the email, and then click the link in the body of the email. 7. Return to the Amazon Pinpoint console in your browser. On the **Set up
email** page, choose **Save**.

## Create an orchestration sending role arn

You must create an **Orchestration sending role arn** to grant Amazon Pinpoint
access to use your Amazon SES resources to be able to send email from a campaign or journey.
If you already have an **Orchestration sending role arn**, then you can
choose to use that role in step 6.

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

**Next:**
[Import customer data and create a
segment](gettingstarted-import-customer-data.md "gettingstarted-import-customer-data.md")
