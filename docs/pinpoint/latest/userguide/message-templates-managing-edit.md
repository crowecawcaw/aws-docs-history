**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Editing a message template

You can open a message template for editing in two ways: while you're authoring a message
that uses the template, and by using the **Message templates** page. This topic
explains how to open and edit a template by using the **Message templates**
page.

If you edit a template, Amazon Pinpoint might apply your changes to existing messages that use the
template and haven't been sent yet, such as campaign messages that are scheduled to be sent at a
later time. This depends on whether you edit the active version of the template and how you
configured the messages that use the template. For more information, see [Managing versions of message templates](message-templates-versioning.md "message-templates-versioning.md").

###### To edit a message template

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Message templates**.
3. On the **Message templates** page, choose the template that you want to
   edit. The template page opens and displays information about the template. It also displays the
   contents and settings for the active version of the template.
4. Choose **Edit**.
5. Under **Template details**, use the version selector to choose the
   version of the template that you want to use as a starting point for your changes. If you
   choose the most recent version of the template, you can save your changes directly to that
   version of the template. Otherwise, you can save your changes as a new version of the
   template.
6. Make the changes that you want. You can change any of the template's content or settings,
   except the name of the template. To change the name of the template, you can [create a copy of the template](message-templates-managing-copy.md "message-templates-managing-copy.md"), save the copy
   with the name that you want, and then optionally delete the original template.
7. When you finish making changes, do one of the following:
   - To save your changes as a new version of the template, choose **Save as new
     version**. To help make sure that your changes don't affect any existing messages,
     we recommend that you choose this option.
   - To save your changes as an update to the most recent version of the template, choose
     **Update version**. This option is available only if you chose the most
     recent version of the template in step 5. If you choose this option, your changes might
     affect existing messages that use the template.
