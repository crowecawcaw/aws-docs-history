

# India sender ID registration process in AWS End User Messaging SMS
<a name="registrations-sms-senderid-india"></a>

There are two ways to send SMS messages to recipients in India: *international routes* and *local routes*.

To send messages using local routes, you must first register your use case and message templates with the Telecom Regulatory Authority of India (TRAI) through a Distributed Ledger Technology (DLT) portal. When you register your use case through a DLT portal, you receive an Entity ID and a Template ID, which you must specify when you send your messages through AWS End User Messaging SMS. These registration requirements are designed to reduce the number of unsolicited messages that Indian consumers receive and to protect consumers from potentially harmful messages.

To complete the registration process, you must provide the following information:
+ Your organization's Permanent Account Number (PAN).
+ Your organization's Tax Deduction Account Number (TAN).
+ Your organization's Goods and Services Tax Identification Number (GSTIN).
+ Your organization's Corporate Identity Number (CIN).
+ A letter of authorization that gives you the authority to register your organization with Vilpower. The Vilpower website includes a template that you can download and modify to fit your needs.

To send SMS messages to India, follow these steps:

1. [Register your company and use case with the TRAI and create the required Telemarketer chains](registrations-sms-senderid-india-register.md)

1. [India sender ID registration in AWS End User Messaging SMS](registrations-sms-senderid-india-support.md)

1. [Specify the Entity ID and Template ID values to send messages to India](registrations-sms-senderid-india-specify-ids.md)

**Topics**
+ [International and local routes](registrations-sms-senderid-india-routes.md)
+ [Register with TRAI and create Telemarketer chains](registrations-sms-senderid-india-register.md)
+ [India sender ID registration](registrations-sms-senderid-india-support.md)
+ [Specify the Entity and Template ID values to send messages](registrations-sms-senderid-india-specify-ids.md)
+ [Understanding template matching issues](registrations-sms-senderid-india-template-issues.md)