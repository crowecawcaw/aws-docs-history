# Create message templates

If you frequently design and send a certain type of message, such as a weekly email or an
appointment reminder, you can create and save it as a message template. You can then use the
template as a starting point each time you need to send that type of message, instead of
designing and writing the message again.

This topic is for administrators and contact center managers who want to create message
templates using the Amazon Connect admin website.

###### Tip

Even though message templates use the Amazon Q in Connect APIs, message templates don't lead to
additional billing. You only pay for the chat message price or email price. For more
information, see [Amazon Connect
Pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/").

## What are message templates?

A _message template_ is a set of content and settings that you can
create, save, and then reuse in messages that you send. In some businesses they are
referred to as _email templates_ and _SMS
templates_. When you create a message template, you specify the content
that you want to reuse in various components of messages that are based on the
template.

When you create a message, you can choose a template to use for the message. If you
choose a template, Amazon Connect populates the message with the content and settings in the
template.

You can design the following types of message templates in Amazon Connect:

- **Email templates** for email messages that you send in reply
  to customer emails to your contact sent, or that agents can use for frequently
  asked questions. Email templates can define the structure of the email for the
  agent, for example, for a signature, or they can be a full response.
- **SMS templates** for SMS text messages that you send from
  campaigns, or to a limited audience as direct or test messages.
- **WhatsApp templates** for WhatsApp messages that you send from
  campaigns, or to a limited audience as direct or test messages.

You can create templates that have the following features:

- Rich text formatting (bold, italics, underline, strikethrough, superscript,
  subscript), rich text font styling (color, highlight, size, heading, family,
  block quote, code block), special characters, emojis, lists (bulleted,
  numbered), alignment and indentations, tables, hyperlinks, and embedded
  images
- Attributes within the email template to define personalize details such as
  customer name, customer email, customer account number, customer phone number,
  customer address, and agent name.
- Attachments up to 1 MB. For a list of supported attachment types, see [Amazon Connect feature specifications](feature-limits.md "feature-limits.md").

When you create an email message that's based on a template, Amazon Connect populates the
message with the content and settings that you defined in the template.

## How to create message templates

1. Log in to Amazon Connect admin website with an Admin account or a user account that has
   **Content Management** - **Message
   templates** - **Create** in it's security profile.
2. In the navigation pane, choose **Message templates**.
3. If this is the first time you've created templates, you are prompted to create
   a knowledge base, which is where the templates are stored.

Your business can have several knowledge bases, but only one of them can be
associated with templates. 4. Choose **Create template**. 5. Under **Channel**, choose a channel. 6. For **Name** enter a name for the template. The name must
begin with a letter or number. It can contain up to 128 characters. 7. For **Description - _optional_**, enter a
brief description of the template. The description can contain up to 255
characters. 8. For **Routing profiles - _optional_**,
enter the routing profiles for agents to be able to use this template from the
agent workspace. 9. Depending on whether you are creating an **Email**, an
**SMS** or **WhatsApp** template, do one of the following:

For email templates:

    1. Under **Email details**, use the following options to specify
     the content for messages that use the template:




    	* For **Subject**, enter the text that you want to
    	 display in the subject line of the message.
    	* For **Body**, enter the content that you want to
    	 display in the body of the message.




    		+ **Editor**: Use the rich text editor to enter
    		 the content. Use the formatting toolbar to apply formatting, add
    		 links, and other content to the message. To add attachments,
    		 your IT admin needs to enable the attachments feature for this
    		 option.
    		+ **Code**: Manually enter HTML content,
    		 including formatting, links, and other features that you want to
    		 include in the message.
    	You can also include personalized content in the subject and body of
    	 the template by using attributes. To do this, add message variables that
    	 refer to specific attributes that you or Amazon Connect created, such as an
    	 attribute that stores a user's first name. By using message
    	 variables, you can display different content for each recipient of a
    	 message that uses the template.


    	To use a message variable, choose the name of an existing attribute
    	 from the **Attribute finder**. Amazon Connect drops it into your
    	 message. You can copy and paste it to the location that you want. For
    	 more information, see [Add personalized content to message
    	 templates](personalize-templates.md "personalize-templates.md").



    	![The Attribute finder on the Message templates page.](images/message-template-attribute-finder.png)
    2. Under **Headers - *optional***, you can
     add two static headers to the email message. For example, to add a one-click
     unsubscribe link, to a promotional email, add the following two headers:




    	* **List-Unsubscribe**: Set to your organization's
    	 unsubscribe link. The link must support HTTP POST requests to process
    	 the recipients unsubscribe request.
    	* **List-Unsubscribe-Post**: Set to
    	 `List-Unsubscribe=One-Click`.
    Including an unsubscribe link in your email is a best practice, and in some
     countries it's a legal requirement. If your template includes a link with this
     attribute, you must have in place a system for handling opt-out requests.
    3. When you finish entering content and settings for the template, choose
     **Save**.
    4. Before making the template available to users, we recommend that you send a
     test email message to make sure the template works as intended.
    5. When you are ready for the template to be available in flows, campaigns, and
     to agents using the agent workspace, complete the steps to [activate](create-message-templates1.md "create-message-templates1.md") it.

###### For SMS templates:

1. Under **SMS details** in the **Body**
   write the message. Use the above instructions to personalize the message by
   adding attributes as needed.
2. When you finish entering content and settings for the template, choose
   **Create**.
3. Before making the template available to users we recommend that you send a test
   message to make sure the template works as intended.
4. When you're ready for the SMS template to be available in the **Send
   message** block, or for the Email template to be available for email
   campaigns, complete the steps to [activate](create-message-templates1.md "create-message-templates1.md") it.

###### For WhatsApp templates:

1. Under **WhatsApp details**, select the template from dropdown. Please note only Meta approved templates can be used to create message templates. Ensure your imported templates are approved in Meta Business WhatsApp Manager before proceeding.
2. Define a name for the template and add descriptions if needed.
3. Once you selected Meta approved template, you will see the details displayed in **Body** and **Template Metadata (JSON)** format.
4. **Attribute mapping:** To enable personalized message delivery in Amazon Connect, you will need to map your imported Meta attributes to custom text. By combining your existing Connect attributes with plain text, you can create customized messages for your customers. For example, you might see Hello {{1}} in the **Body**, and you can choose to `Attributes.Customer.FirstName` from Connect attribute list to match.
5. There are a variety of button types that can be added into a content template. If your selected template includes buttons, such as a Website URL that includes attributes, you can either select Connect attributes to map or type in static text.
6. When you completed attributes mapping, choose **Save**.
7. Before making the template available to users we recommend that you send a test message to make sure the template works as intended.
