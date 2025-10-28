# Creating delegates

If you have Amazon Chime Pro permissions, you can assign delegate status to other Pro users.
This status allows them to schedule meetings on your behalf and use the meeting host actions. For more information about the
host actions available to delegates, see [Hosting meetings](chime-organizer-call-controls.md "chime-organizer-call-controls.md").

###### Topics

- [Creating delegates](#assign-delegates "#assign-delegates")
- [Setting delegate permissions in Microsoft Outlook](#set-delegate-permissions-outlook "#set-delegate-permissions-outlook")
- [Removing delegates](#remove-delegates "#remove-delegates")
- [Scheduling meetings as a delegate with a calendar app](#delegate-calendar "#delegate-calendar")
- [Scheduling meetings as a delegate using the Outlook Add-In](#delegate-outlook "#delegate-outlook")

## Creating delegates

You use the Amazon Chime desktop client or web apps to create delegates.

###### To create delegates

1. On the ellipsis menu next to your name, choose **Settings**.
2. Choose **Delegates**.
3. Choose **Add delegates**.
4. Search for and select the name of your delegate, then choose
   **Add**.

## Setting delegate permissions in Microsoft Outlook

If you use Amazon Chime with Microsoft Outlook, some delegates may not be able to schedule meetings unless they have **Owner** permissions to your inbox. If your delegate can't
schedule meetings, follow these steps:

###### To set delegate permissions

1. In Outlook, open the context (right-click) menu for your inbox and choose **Properties**.
2. In the **Inbox Properties** dialog box, choose the **Permissions** tab, and then choose **Add**.
3. In the **Add Users** dialog box, search for and select your delegate’s name, and then choose **OK**.
4. In the **Inbox Properties** dialog box, under **Permissions**, open the **Permissions** list and choose **Owner**,
   then choose **Apply**.

## Removing delegates

You use the Amazon Chime desktop client or web apps to remove delegates.

###### To remove delegates

1. On the **Amazon Chime** menu next to your name, choose
   **Settings**.
2. Under **Settings**, choose **Meetings**.
3. Choose a delegate from the list, and choose
   **Remove**.

## Scheduling meetings as a delegate with a calendar app

If you schedule meetings for another user, and they use a calendar app other than Microsoft Outlook, ask the meeting host to follow these steps.

Before the host begins this procedure, ask them to ensure that you're their delegate in Amazon Chime. For more information, see [Creating delegates](#assign-delegates "#assign-delegates").

###### To delegate a meeting using a calendar app

1. From the Amazon Chime desktop client or web application, choose **Meetings**, **Schedule a meeting**.
2. Select **Generate a new ID**.
3. Choose **Next**.
4. For **Select your calendar app:**, choose **Other**.
5. Do the following:
   - Choose **Copy addresses**, and paste the addresses into the
     body of a new email message.
   - Choose **Copy attendee invitation**, and paste this information into the same email.
   - In the Amazon Chime client, choose **I am done**.

6. Repeat steps 1-5 to generate three sets of meeting IDs.
7. Send an email with the meeting information to your delegate.

After you receive this information from your meeting host, follow these steps to schedule the meeting.

###### To schedule a meeting as a delegate

1. From the meeting host's calendar, open or create the meeting appointment.
2. Copy and paste one of the three sets of email addresses into the **To**
   field. For example, **meet@chime.aws** and
   **pin+`meeting-id`@chime.aws**.
3. Copy and paste the corresponding meeting instructions into the body of the appointment. Make
   sure the instructions include the link to the meeting, such as
   **https://chime.aws/`meeting-id`**.
4. Add the other meeting attendees to the appointment and finish scheduling it.

When scheduling back-to-back meetings, use a different set of meeting details to
schedule them. Doing so prevents the meetings from overlapping.

###### Note

As a delegate, do not use your personal Amazon Chime meeting ID. Doing so can cause a scheduling
failure, or split meeting attendees onto different meeting bridges.

## Scheduling meetings as a delegate using the Outlook Add-In

When scheduling meetings with the Outlook add-in, you receive a prompt to
select who you are scheduling the meeting for. For more information, see [Scheduling meetings with the Add-In for Outlook](chime-scheduling-outlook.md "chime-scheduling-outlook.md").
