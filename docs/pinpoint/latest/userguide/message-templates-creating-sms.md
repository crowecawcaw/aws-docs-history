**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Creating SMS templates

An _SMS template_ is a type of message template that
contains content and settings that you want to create, save, and reuse in SMS text messages that
you send for any of your Amazon Pinpoint projects. You can use an SMS template in text messages that
you send from campaigns, or to a limited audience as direct or test messages.

When you create an SMS template, you specify the settings and content that you want to reuse
in the body of text messages that are based on the template. When you create a message that's
based on the template, Amazon Pinpoint populates the message with the settings and content that you
defined in the template.

###### To create an SMS template

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Message templates**.
3. Choose **Create template**.
4. Under **Channel**, choose **SMS**.
5. Under **Template details**, for **Template name**,
   enter a name for the template. The name must begin with a letter or number. It can contain
   up to 128 characters. The characters can be letters, numbers, underscores (\_), or hyphens
   (‐).
6. (Optional) For **Version description**, enter a brief description of
   the template. The description can contain up to 500 characters.
7. Under **SMS details**, for **Message**, enter the
   content that you want to display in the body of messages that use the template. The message
   body can contain up to 1,600 characters.

###### Tip

You can include personalized content in the body of the template. To do this, add
message variables that refer to specific attributes that you or Amazon Pinpoint created, such as an
attribute that stores a user's first name. By using message variables, you can
display different content for each recipient of a message that uses the template.

To use a message variable, choose the name of an existing attribute from the
**Attribute finder**. Amazon Pinpoint creates a message variable for the
attribute and copies it to your clipboard. Paste the variable in the location that you
want. For more information, see [Adding personalized content to message
templates](message-templates-personalizing.md "message-templates-personalizing.md"). 8. If you added personalized content to the template by using message variables,
specify a default value for each variable. If you do this, Amazon Pinpoint replaces the variable
with the value that you specify, if a corresponding value doesn't exist for a recipient. We recommend that
you do this for each variable in the template.

To
specify default values for variables, expand the **Default attribute
values** section. Then enter the default value that you want to use for each variable.
If you don't specify a default value and a value doesn't exist for a recipient, Amazon Pinpoint does not send the message. 9. When you finish entering content and settings for the template, choose
**Create**.
To test the template before you use it in a message that you send to users, you can [send a test message](messages-sms.md "messages-sms.md") that uses the template. If you do this, make
sure that you first complete step 8 to specify default values for all the variables in the
template. Otherwise, the message might not be sent or it might not render correctly.
