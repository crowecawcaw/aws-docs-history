**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Sending a test email message

To send a test email message, you must use a project that has the email channel enabled.
To learn how to create a new project and enable the email channel for it, see [Setting up the Amazon Pinpoint email channel](channels-email-setup.md "channels-email-setup.md"). To learn how to
enable the email channel for an existing project, see [Managing the Amazon Pinpoint email channel](channels-email-manage.md "channels-email-manage.md").

###### To send a test email message

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you want to
   send a test message for.
3. In the navigation pane, choose **Test messaging**.
4. On the **Test messaging** page, under
   **Channel**, choose **Email**.
5. For **Destination type**, choose one of the following
   destinations for your message:
   - **Email addresses** – Each destination is a
     recipient's email address.
   - **Endpoint IDs** – Each destination is a unique ID
     that's assigned to an endpoint for the project.

6. Depending on your selection for **Destination type**, enter one
   or more **Endpoint IDs** or **Email addresses**.
   You can enter up to 15 values. Use commas to separate multiple values.
7. For **Message content**, choose whether you want to
   **Create a new message** or **Use an existing
   template**.

###### Note

The maximum email message size for **Create a new message** is 200 KB. You can
use email templates to send larger email messages.

If you choose to use an existing template, choose the template from the
**Template** list. After you choose a template, Amazon Pinpoint displays
a preview of the active version of the template. The active version is typically the
version of a template that's been reviewed and approved for use, depending on your
workflow.

If you choose to create a new message, specify a subject in the
**Subject** field, and a message body in the
**Message** field.

###### Tip

You can enter the message body by using either HTML or Design view. In the
HTML view, you can manually enter HTML content for the message body, including
formatting, links, and other features that you want to include in the message.
In the Design view, you can use a rich text editor to enter the content of the
message body. You can use the formatting toolbar to apply formatting and add
links and other features to the message body. To switch views, choose
**HTML** or **Design** from the view
selector above the message editor.

In the field below the message editor, optionally enter the content that you want
to display in the body of messages that are sent to recipients whose email
applications don't display HTML content. 8. ###### Note

You must set up an email orchestration sending role before you can use email headers. For more
information, see [Creating an email orchestration
sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md").

Under **Headers**, choose **Add new headers**,
to add up to 15 headers for the email message. For a list of supported headers, see
[Amazon SES header
fields](../../../ses/latest/dg/header-fields.md "../../../ses/latest/dg/header-fields.md") in the [Amazon Simple Email Service
Developer Guide](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md").

    * For **Name**, enter the name of the header.
    * For **Value**, enter the value of the header.

(Optional) To add a One-click unsubscribe link to a promotional email, add the
following two headers:

    1. Create a header with `List-Unsubscribe` for **Name** and set
     **Value** to your unsubscribe link. The link must
     support HTTP POST requests to process the recipients unsubscribe
     request.
    2. Create a header with `List-Unsubscribe-Post` for **Name** and set
     **Value** to
     `List-Unsubscribe=One-Click`.

9. When you finish, choose **Send message**.
