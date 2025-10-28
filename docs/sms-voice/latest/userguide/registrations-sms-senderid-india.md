# India sender ID registration process in

AWS End User Messaging SMS

###### Warning

Starting April 30, 2025, End User Messaging will only support local India routes
through AWS regions: AP-SOUTH-1 Asia Pacific (Mumbai) and AP-SOUTH-2 Asia Pacific
(Hyderabad).

By default, when you send messages to recipients in India, AWS End User Messaging SMS uses International
Long-Distance Operator (ILDO) routes to transmit those messages. When recipients see a
message sent over an ILDO connection, it appears to be sent from a random numeric ID (unless
you purchase a dedicated short code).

Companies that are registered in India can also use dedicated sender IDs to send their
messages. If you prefer to use a sender ID, you have to send those messages over
_local routes_ rather than ILDO routes.

###### Note

The price for sending messages using ILDO routes is much higher than the price for
sending messages through local routes. The prices for sending messages using both ILDO
and local routes are shown on the [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/") page.

To send messages using local routes, you must first register your use case and message
templates with the Telecom Regulatory Authority of India (TRAI) through a Distributed Ledger
Technology (DLT) portal. When you register your use case through a DLT portal, you receive
an Entity ID and a Template ID, which you must specify when you send your messages through
AWS End User Messaging SMS. These registration requirements are designed to reduce the number of unsolicited
messages that Indian consumers receive and to protect consumers from potentially harmful
messages.

###### Warning

Starting April 30, 2025, End User Messaging will only support local India routes
through AWS regions: AP-SOUTH-1 Asia Pacific (Mumbai) and AP-SOUTH-2 Asia Pacific
(Hyderabad).

To complete the registration process, you must provide the following information:

- Your organization's Permanent Account Number (PAN).
- Your organization's Tax Deduction Account Number (TAN).
- Your organization's Goods and Services Tax Identification Number (GSTIN).
- Your organization's Corporate Identity Number (CIN).
- A letter of authorization that gives you the authority to register your
  organization with Vilpower. The Vilpower website includes a template that you can
  download and modify to fit your needs.
  To send SMS messages to India, follow these steps:

1. [Register your company and
   use case with the TRAI and create the required Telemarketer chains](registrations-sms-senderid-india-register.md "registrations-sms-senderid-india-register.md")
2. [India sender ID registration
   in AWS End User Messaging SMS](registrations-sms-senderid-india-support.md "registrations-sms-senderid-india-support.md")
3. [Specify the Entity ID and
   Template ID values to send messages to India](registrations-sms-senderid-india-specify-ids.md "registrations-sms-senderid-india-specify-ids.md")

###### Topics

- [Register with
  TRAI and create Telemarketer chains](registrations-sms-senderid-india-register.md "registrations-sms-senderid-india-register.md")
- [India sender ID
  registration](registrations-sms-senderid-india-support.md "registrations-sms-senderid-india-support.md")
- [Specify the
  Entity and Template ID values to send messages](registrations-sms-senderid-india-specify-ids.md "registrations-sms-senderid-india-specify-ids.md")
- [Understanding template matching issues](registrations-sms-senderid-india-template-issues.md "registrations-sms-senderid-india-template-issues.md")
