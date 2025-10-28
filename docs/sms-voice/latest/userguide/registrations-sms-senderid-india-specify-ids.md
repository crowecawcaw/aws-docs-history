# Specify the Entity ID and

Template ID values to send messages to India

To successfully deliver your messages using local routes, you must specify Entity ID
and Template ID values that you received after completing the sender ID registration
process. You must also choose the correct entity type, and confirm that your messages
match the example templates that you registered.

The steps that you complete depend on how you send your SMS messages. If you use the
[SendTextMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md") API to send your messages, you can
include these attributes in your call to the API. If you use campaigns or journeys to
send your messages, you can specify the correct values when you set up the campaign or
journey. This section includes information for both scenarios.

###### To send messages over Indian local routes using the SendTextMessages API

1. In your call to the `SendTextMessages` API, provide values for the
   following parameters:
   - `EntityId` – The entity ID or Principal Entity (PE)
     ID that you received after completing the sender ID registration
     process.
   - `TemplateId` – The template ID that you received
     after completing the sender ID registration process.

   ###### Important

   Make sure that the Template ID that you specify matches your
   message template exactly. If your message doesn't match the template
   that you provided during the registration process, the mobile
   carriers might reject your message.

2. For the `MessageType` parameter, specify the appropriate route type
   for your message. You can specify one of the following values:
   - `Promotional` – Specify this message type for
     promotional messages. Promotional sender IDs only contain
     numbers.
   - `Transactional` – Specify this message type for
     transactional messages. Transactional sender IDs only contain letters,
     and are case-sensitive.

   ###### Note

   You can register both promotional (numeric) sender IDs and
   transactional (alphabetic) sender IDs in the same
   AWS account.

   For additional content guidelines, see the Vilpower website at
   [https://www.vilpower.in](https://www.vilpower.in "https://www.vilpower.in").

3. When you add content to your message, review your content thoroughly to verify
   that it matches the content in the DLT registered template exactly. If you
   include additional character returns, spaces, punctuation, or mismatched
   sentence case, carriers will block your SMS messages. For more information about
   issues related to template matching, see [Understanding
   template matching issues when sending messages](registrations-sms-senderid-india-template-issues.md "registrations-sms-senderid-india-template-issues.md").
