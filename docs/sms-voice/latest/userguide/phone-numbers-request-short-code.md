# Requesting dedicated short codes

A short code is a number that you can use for high-volume SMS and MMS message sending.
Short codes are often used for application-to-person (A2P) messaging, two-factor
authentication (2FA), and marketing. A short code typically contains between five and seven
digits, depending on the country that it's based in.

You can request a short code for the below countries through the End User Messaging console.
If you require a short code in a country not included in the below list you can request a
short code by opening a case in the Support by following the below process.

For information about short code pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

## Important

considerations

Before you request a short code, consider the following information:

- If you plan to use the short code to send messages that contain Protected
  Health Information (PHI), you should identify this purpose in the **Case
  description** field of your support case.
- AWS End User Messaging SMS currently only supports standard short codes. Free-to-End-User (FTEU)
  short codes aren't supported.
- If you're new to SMS and MMS messaging with AWS End User Messaging SMS, you should request a
  monthly SMS and MMS spending threshold that meets the expected demands of your
  SMS and MMS use case. By default, your monthly spending threshold is $1.00
  (USD). You can request to increase your spending threshold in the same support
  case that includes your request for a short code.

## Requesting a short code

You can only use short codes to send messages to recipients in the same country where the
short code is based. If your use case requires you to use short codes in more than one
country, you must request a separate short code for each country that your recipients are
located in.

Countries support through console and APIs:

- Chile (CL)
- Finland (FI)
- Germany (DE)
- India (IN)
- Netherlands (NL)
- Spain (ES)
- United Kingdom (GB)
- United States (US)

## Step 1: Open a support

case

The first step in requesting a short code is to open a Service Limit Increase case in
the Support Center Console.

###### To request a short code

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

3. In the **Requests** section, do the following:
   - For the **Region**, choose the AWS Region that you
     plan to send messages from.

   ###### Note

   The Region is required in the **Requests**
   section. Even if you provided this information in the **Case
   details** section you must also include it here.
   - For **Resource Type**, choose **Dedicated SMS
     Short Codes**.
   - For **Quota**, choose the message type that you
     plan to send using your short code.
     - **One Time Password/Two-Factor Authentication** – Messages that
       provide passwords that your customers use to authenticate with
       your website or application.
     - **Promotional/Marketing** – Noncritical messages
       that promote your business or service, such as special offers or
       announcements.
     - **Transactional** – Important
       informational messages that support customer transactions, such
       as order confirmations or account alerts. Transactional messages
       must not contain promotional or marketing content.
     - **Transactional/Notifications/OTP/2FA** – All message types.

   - For **New quota value**, enter the number of short
     codes that you want to purchase for the target country and use
     case.

   ###### Note

   If you want to request a short code for a different country, or
   for a separate use case in the same country, open a separate case in
   the Support Center Console. By creating separate cases, all communications
   for a particular country or use case are restricted to a single
   Support case, which reduces the potential for
   miscommunications.

4. Under **Case description**, for **Use case
   description**, provide details about your use case.
5. Choose **Next Step: Solve now or Contact us**. For
   **Preferred contact language**, choose whether you want to
   receive communications for this case in **English** or
   **Japanese**.
6. When you finish, choose **Submit**.

Support acknowledges your request within 24 hours of receipt. If we're able to provide
you with a short code, we provide you with a short code registration form as an
attachment to your Support case. Complete the registration form in its entirety. The
information in this form is required in order to set up a short code with the mobile
carriers. For more information about completing this form, see [Obtaining a short code for sending text messages to US recipients](https://aws.amazon.com/blogs/messaging-and-targeting/obtaining-a-short-code-for-sending-text-messages-to-us-recipients-part-1/ "https://aws.amazon.com/blogs/messaging-and-targeting/obtaining-a-short-code-for-sending-text-messages-to-us-recipients-part-1/") on the
AWS Messaging and Targeting Blog. This blog post covers the process of applying for US
short codes, but the information it provides is also useful when applying for short
codes in other countries.

###### Note

There is no Service Level Agreement for the time required to obtain a short code. The
amount of time required depends on whether or not your use case is compliant with the
requirements of the carriers.

There may be additional time in the request while our support teams work to ensure your application is compliant. Any provided estimated timelines would start once we have confirmation your application is in a state that can be submitted to carriers for review. If the carriers do not think that your use case is
compliant, they will reject your application and provide information about the reasons
for the rejection. If this happens, you will find this information in your Support case.
You can address the issues with your application in your Support case. When you do, we
send this updated information back to the carriers so that they can reconsider your
application.

The fees associated with using short codes begin immediately after we initiate your
short code request with carriers. You're responsible for paying these charges, even if
the short code hasn't been completely provisioned yet. In order to prevent our systems
from being used to send unsolicited or malicious content, we must consider each
request carefully. We might not be able to grant your request if your use case doesn't
align with our policies.

## Step 2: Update your SMS

settings in the AWS End User Messaging SMS console

After we notify you that your short code has been provisioned, complete the following
steps.

###### Note

You can't complete this step until the short code request has been approved and
the short code has been added to your AWS account.

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone number**.
3. On the **Phone number** page, choose the short code.
4. On the **Keywords** tab, verify that the responses for the
   _HELP_ and _STOP_ keywords match the
   values that you specified in your request.
