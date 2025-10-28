# How to request a sender ID through Support

If you plan to send messages to recipients a country where sender IDs are required,
you can request a sender ID by creating a new case in the AWS Support Center.

###### Important

To enable Amazon Pinpoint or Amazon SNS to use an origination identity you must add a **Resource
policy** to the origination identity. The resource policy must be added after the
registration has been approved and the origination identity has been added to your
AWS account. For example resource policies and directions on how to add one, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### Important

- If you need to register a sender ID in India, complete the procedures in [India sender ID registration process in
  AWS End User Messaging SMS](registrations-sms-senderid-india.md "registrations-sms-senderid-india.md")
  _before_ you open a case in Support Center.
- If you need to register a sender ID in Singapore, complete the procedures in [Singapore sender ID registration process](registrations-sg.md "registrations-sg.md").

###### To request a sender ID

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
   - For **Resource Type**, choose **Sender ID
     Registration**.
   - For **Quota**, choose either
     **Promotional/Marketing** or
     **Transactional/Notifications/OTP/2FA**.
   - For **New quota value** enter
     `1`.

4. Under **Case description**, for **Use case
   description**, provide the following information:
   - The sender ID that you want to register.
   - The template that you plan to use for your SMS messages.
   - The number of messages that you plan to send to each recipient per
     month.
   - Information about how your customers opt in to receiving messages from
     you.
   - The name of your company or organization.
   - The address that's associated with your company or
     organization.
   - The country where your company or organization is based.
   - A phone number for your company or organization.
   - The URL of the website for your company or organization.

5. (Optional) If you want to submit any further requests, choose **Add
   another request**.
6. Choose **Next Step: Solve now or Contact us**. For
   **Preferred contact language**, choose whether you want to
   receive communications for this case in **English** or
   **Japanese**.
7. When you finish, choose **Submit**.
   After we receive your request, we provide an initial response within 24 hours. We
   might contact you to request additional information.

If we're able to provide you with a Sender ID, we send you an estimate of the amount
of time that's required to provision it. In many countries, we can provide you with a
Sender ID within 2–4 weeks. However, in some countries, it can take several weeks to obtain a Sender ID.

In order to prevent our systems from being used to send unsolicited or malicious
content, we have to consider each request carefully. We might not be able to grant your
request if your use case doesn't align with our policies.
