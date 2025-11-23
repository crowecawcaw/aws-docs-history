# SMS/MMS and Voice sandbox in AWS End User Messaging SMS

New AWS End User Messaging SMS accounts are placed into an SMS/MMS or voice sandbox. The sandbox protects both
AWS customers and recipients from fraud and abuse. It creates a safe environment for test
and development.

###### Topics

- [SMS/MMS sandbox](#sandbox-sms "#sandbox-sms")
- [Moving from the SMS/MMS
  sandbox](#sandbox-sms-move-to-production "#sandbox-sms-move-to-production")
- [Voice sandbox](#sandbox-voice "#sandbox-voice")

## The AWS End User Messaging SMS SMS/MMS sandbox

While your account is in the sandbox, you can use all of the SMS sending methods in
the AWS End User Messaging SMS console or the `SendTextMessages` API. To send an MMS message you
must use the `SendMediaMessage` API. However, the following restrictions are
in place while your account is in the sandbox:

- You have a monthly SMS spending limit of $1.00 (USD).
- You have a monthly MMS spending limit of $1.00 (USD).
- You can send SMS and MMS messages only to verified destination phone numbers.
  You can add up to 10 verified numbers.
- The rules and restrictions for sending SMS and MMS messages to each
  destination country apply. For example, to send a message to a recipient in the
  United States, you must first request and register a US number.
- To verify that you own a phone number, we send a verification code to that
  number. While the standard fees for each SMS message typically apply, we waive
  the fee for the first verification code for each phone number. For more
  information about SMS pricing, see the [AWS End User Messaging Pricing](https://aws.amazon.com//end-user-messaging/pricing/ "https://aws.amazon.com//end-user-messaging/pricing/")
  page.

###### Note

Message and data rates apply for messages that you receive. We send one
message per verification request.

- You can delete a destination phone number. However, you must wait 24 hours after
  adding a phone number before you can delete it.
- You can send SMS and MMS messages only to verified destination numbers. For
  more information about how to add a verified destination phone number, see [Add a verified destination phone
  number](verify-destination-phone-number.md "verify-destination-phone-number.md").

You can remove these restrictions by requesting production access. For more information,
see [Moving from the AWS End User Messaging SMS MMS and Voice
sandbox to production](#sandbox-sms-move-to-production "#sandbox-sms-move-to-production").

###### Note

If your account is observed to be sending suspicious SMS/MMS traffic, your
account's ability to send messages may be paused. If this occurs, please follow
the steps in [Moving from the AWS End User Messaging SMS MMS and Voice
sandbox to production](#sandbox-sms-move-to-production "#sandbox-sms-move-to-production") to gain production
access.

## Moving from the AWS End User Messaging SMS MMS and Voice

sandbox to production

After fully testing your SMS/MMS environment in the SMS/MMS sandbox, you can request
to move to production. Moving from the SMS sandbox to production also applies to MMS
capability.

###### Note

If your account is in multiple AWS Regions, you must submit a support request for each
Region.

Complete all fields in the support case, even if they are labeled as optional.

###### To move to production from the SMS sandbox

1. Create an AWS Support case at [https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").
2. On the **Create Case** page, complete the following:
   - Select **Account and Billing**.
   - For **Service**, choose **Service
     Quotas**.
   - For **Category** choose either
     **AWS End User Messaging SMS (Pinpoint)** or
     **AWS End User Messaging Voice (Pinpoint)**, depending on your
     request.
   - For **Severity**, choose **General
     Limits**.

3. Under **Requests**, complete the following sections:
   - For the **Region**, choose the AWS Regions from
     which you will be sending messages.

   ###### Note

   The AWS Regions is required in the **Requests**
   section. Even if you provided this information in the **Case
   details** section, you must also include it
   here.
   - For **Resource Type**, choose **General
     Limits**.
   - For the **Quota**, choose **SMS
     Production Access**.
   - For **New quota value**, enter 1.

4. Under **Description**, for **Use case
   description**, enter any relevant details about this request.
   Include answers to the
   following:
   - For **Provide a link to the site or app which will be sending
     SMS messages**, provide information about the website,
     application, or service that will send SMS/MMS messages.
   - For **What type of messages do you plan to send**,
     choose the type of message that you plan to send by using your long
     code:
     - **One Time Password** – Messages that
       provide passwords that your customers use to authenticate with
       your website or application.
     - **Promotional** – Noncritical messages
       that promote your business or service, such as special offers or
       announcements.
     - **Transactional** – Important
       informational messages that support customer transactions, such
       as order confirmations or account alerts. Transactional messages
       must not contain promotional or marketing content.

   - For **Which countries do you plan to send messages
     to**, enter the country or region that you want to purchase
     short codes in.
   - In the **How do your customers opt to receive messages from
     you**, provide details about your opt-in process.
   - In the **Please provide the message template that you plan to
     use to send messages to your customers** field, include the
     template that you will be using.

5. (Optional) If you want to submit any further requests, choose **Add
   another request**.
6. Choose **Next Step: Solve now or Contact us**. For
   **Preferred contact language**, choose whether you want to
   receive communications for this case in **English** or
   **Japanese**.
7. When you finish, choose **Submit**.

After we receive your request, we provide an initial response within 24 hours. We might
contact you to request additional information.

## AWS End User Messaging SMS Voice sandbox

To help protect our customers from fraud and abuse, we place your account in a sandbox
environment when you first create it. The sandbox environment also helps you test the
channel to help establish your reputation. While your account is in the sandbox, you
have full access to AWS End User Messaging SMS voice messaging, with the following restrictions:

- You have a daily limit of 20 messages.
- You can send a maximum of five voice messages to a single recipient during a
  24-hour period.
- You can send a maximum of five calls per minute.
- The maximum voice message length is 30 seconds.
- You can send voice messages only to specific countries. For more information, see [Voice quotas](quotas.md#quotas-voice "quotas.md#quotas-voice").
- For more information on how to add a verified destination phone number, see [Add a verified destination phone
  number](verify-destination-phone-number.md "verify-destination-phone-number.md").

When you're ready to move your account out of the voice sandbox, create an AWS Support case
for a **Service limit increase** request. For more information, see [SMS/MMS and Voice sandbox in AWS End User Messaging SMS](sandbox.md "sandbox.md").

###### Note

Before you request production access, you must send at least one voice message
from your AWS End User Messaging SMS account. You can send a voice message by using the [SendVoiceMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendVoiceMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendVoiceMessage.md") API.
