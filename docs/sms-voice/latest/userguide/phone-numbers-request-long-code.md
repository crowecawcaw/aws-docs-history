# Requesting dedicated long codes

A long code (also referred to as a long virtual number, or LVN) is a standard phone number
that contains up to 12 digits, depending on the country that it's based in. Long codes are
typically meant for low-volume, person-to-person communication. In some countries, you can
use long codes for sending test messages, or for sending low volumes of messages to your
customers. In other countries, including the United States, senders are prohibited from
using long codes to send Application-to-Person (A2P) messages, which includes the messages
that you send from AWS End User Messaging SMS.

###### Note

If you're new to SMS messaging with AWS End User Messaging SMS, you should also request a monthly SMS and
MMS spending threshold that meets the expected demands of your SMS and MMS use case. By
default, your monthly spending threshold is $1.00 (USD). For more information, see [Requesting an SMS, MMS, or voice spending quota
change for AWS End User Messaging SMS](awssupport-spend-threshold.md "awssupport-spend-threshold.md").

## Requesting a long code

You can request a long code for the below countries through the End User Messaging console. If you require a
long code in a country not included in the below list you can request a long code by opening a case in the AWS Support
by following the below process.

Countries support through console and APIs:

- Australia (AU)
- Austria (AT)
- Chile (CL)
- Denmark (DK)
- Finland (FI)
- Hong Kong (HK)
- Hungary (HU)
- Italy (IT)
- Netherlands (NL)
- Norway (NO)
- Poland (PL)
- Portugal (PT)
- Spain (ES)
- Sweden (SE)
- United Kingdom (GB)

###### Important

To send messages to recipients in the United States or the US territories of
Puerto Rico, US Virgin Islands, Guam and American Samoa, you must use either a short
code, a 10DLC phone number, or a toll-free number. If you complete the following
steps and request a long code for the United States or US territories of Puerto
Rico, US Virgin Islands, Guam and American Samoa, your request will be
rejected.

###### To request a dedicated long code by opening a case in the AWS Support

Center

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
   - For the **Region**, choose the AWS Region from which
     you will be sending messages.

   ###### Note

   The Region is required in the **Requests**
   section. Even if you provided this information in the **Case
   details** section you must also include it here.
   - For **Resource Type**, choose **Dedicated SMS
     Long Codes**.
   - For **Quota**, choose the type of messages that you
     plan to send using your long code.
   - For **New quota value**, enter the number of long
     codes that you want to purchase.

4. Under **Case description**, for **Use case
   description**, provide details about your use case.
5. (Optional) If you want to submit any further requests, choose **Add
   another request**.
6. Choose **Next Step: Solve now or Contact us**. For
   **Preferred contact language**, choose whether you want to
   receive communications for this case in **English** or
   **Japanese**.
7. When you finish, choose **Submit**.

After we receive your request, we provide an initial response within 24 hours. We
might contact you to request additional information. Once approved, you can add keywords
and response messages to your long code.

If we're able to provide you with a long code, we send you information about the costs
associated with obtaining it. We also provide an estimate of the amount of time that's
required to provision the long code. In many countries, we can provide you with a
dedicated long code within 24 hours. However, in some countries and regions, it can take
several weeks to obtain a dedicated long code for the SMS channel.

In order to prevent our systems from being used to send unsolicited or malicious
content, we must consider each request carefully. We might not be able to grant your
request if your use case doesn't align with our policies.
