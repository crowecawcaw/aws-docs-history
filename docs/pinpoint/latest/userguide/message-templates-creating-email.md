

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Creating email templates
<a name="message-templates-creating-email"></a>

An *email template* is a type of message template that contains content and settings that you want to create, save, and reuse in email messages that you send for any of your Amazon Pinpoint projects. You can use an email template in any type of email message that you create and send by using Amazon Pinpoint.

When you create an email template, you specify the content and settings that you want to reuse in various components of email messages that are based on the template. These components, referred to as *template parts*, can be the message subject, the message body, or both. The content can be static text, personalized content, images, or other design elements. A template part can also be a setting, such as the message body to use if a recipient's email application doesn't display HTML content.

When you create an email message that's based on a template, Amazon Pinpoint populates the message with the content and settings that you defined in the template. 

**To create an email template**

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. In the navigation pane, choose **Message templates**.

1. Choose **Create template**.

1. Under **Channel**, choose **Email**.

1. Under **Template details**, for **Template name**, enter a name for the template. The name must begin with a letter or number. It can contain up to 128 characters. The characters can be letters, numbers, underscores (\_), or hyphens (‐).

1. (Optional) For **Version description**, enter a brief description of the template. The description can contain up to 500 characters.

1. Under **Email details**, use the following options to specify the content for messages that use the template:
   + For **Subject**, enter the text that you want to display in the subject line of the message.
   + For **Message**, enter the content that you want to display in the body of the message.
**Tip**  
For the message body, you can enter the content by using either the HTML or Design view. In the HTML view, you can manually enter HTML content, including formatting, links, and other features that you want to include in the message. In the Design view, you can use a rich text editor to enter the content. Use the formatting toolbar to apply formatting and add links and other features to the content. To switch views, choose **HTML** or **Design** from the view selector above the message editor.  
You can also include personalized content in the subject and body of the template. To do this, add message variables that refer to specific attributes that you or Amazon Pinpoint created, such as an attribute that stores a user's first name. By using message variables, you can display different content for each recipient of a message that uses the template. To use a message variable, choose the name of an existing attribute from the **Attribute finder**. Amazon Pinpoint creates a message variable for the attribute and copies it to your clipboard. Paste the variable in the location that you want. For more information, see [Adding personalized content to message templates](message-templates-personalizing.md).

1. 
**Note**  
You must set up an email orchestration sending role before you can use email headers. For more information, see [Creating an email orchestration sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md).

   Under **Headers**, choose **Add new headers**, to add up to 15 headers for the email message. For a list of supported headers see [Amazon SES header fields](https://docs.aws.amazon.com/ses/latest/dg/header-fields.html) in the [Amazon Simple Email Service Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html).
   + For **Name**, enter the name of the header.
   + For **Value**, enter the value of the header.

   (Optional) To add a One-click unsubscribe link, to a promotional email, add the following two headers:

   1. Create a header with `List-Unsubscribe` for **Name** and set **Value** to your unsubscribe link. The link must support HTTP POST requests to process the recipients unsubscribe request.

   1. Create a header with `List-Unsubscribe-Post` for **Name** and set **Value** to `List-Unsubscribe=One-Click`.

1. (Optional) Under **Plain text version**, enter the content that you want to display in the body of messages that use the template and are sent to recipients whose email applications don't display HTML content.

1. If you added personalized content to the template by using message variables, specify a default value for each variable. If you do this, Amazon Pinpoint replaces the variable with the value that you specify, if a corresponding value doesn't exist for a recipient. We recommend that you do this for each variable in the template.

   To specify default values for variables, expand the **Default attribute values** section. Then enter the default value that you want to use for each variable. If you don't specify a default value and a value doesn't exist for a recipient, Amazon Pinpoint does not send the message.

1. When you finish entering content and settings for the template, choose **Create**.

To test the template before you use it in an email message that you send to users, you can [send a test message](messages-email.md) that uses the template. If you do this, make sure that you first complete step 9 to specify default values for all the variables in the template. Otherwise, the message might not be sent or it might not render correctly.

## Including unsubscribe links in message templates
<a name="message-templates-creating-email-optout"></a>

Including an unsubscribe link in your email is a best practice, and in some countries it's a legal requirement. In your unsubscribe links, you can include a special attribute, `ses:tags="unsubscribeLinkTag:{{value}}"`, where {{value}} is any value that you define. If a recipient clicks a link that contains this special attribute, Amazon Pinpoint counts it as an opt-out event for analytics purposes (for example, in the Opt-out rate metric on the [Analytics overview page](analytics-overview.md)). The following example shows the syntax for this type of link:

```
<a ses:tags="unsubscribeLinkTag:optout" href="https://www.example.com/preferences">Unsubscribe</a>
```

If your template includes a link with this attribute, you must still develop a system for handling opt-out requests. For an example of a system that processes opt-out requests, see the [Amazon Pinpoint Preference Center solution](https://aws.amazon.com/solutions/implementations/amazon-pinpoint-preference-center/) in the AWS Solutions Library.

**Note**  
The Amazon Pinpoint Preference Center solution is now guidance. The solution can no longer be deployed but the architectural diagram and code have been left as a reference.