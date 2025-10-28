**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Deleting a message template

If you want to remove a message template from Amazon Pinpoint completely, you can delete the template.
If you delete a template, it doesn't affect any existing messages that use the template, such as
campaign messages that are scheduled to be sent at a later time.

###### Warning

If you delete a template, Amazon Pinpoint deletes all versions, content, and settings for the
template. In addition, the template becomes unavailable for all future messages. You can't
recover a template after you delete it.

###### To delete a message template

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, choose **Message templates**.
3. On the **Message templates** page, select the check box next to each
   template that you want to delete.
4. On the **Actions** menu, choose **Delete**.
