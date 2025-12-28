# 10DLC campaign registration form

###### Note

With our updated console experience you are now seeing a registration
**Name** field for your registration. This field is set to "–" as we
do not manually backfill any of your service values to prevent interruption to your service
and let you maintain your security posture. A registration **Name** is an
optional friendly name field that can be updated using the tags on the registration details
page. For more information on how to add a **Name** tag, see [Change a registration's name in AWS End User Messaging SMS](registrations-friendly-name.md "registrations-friendly-name.md").

AWS End User Messaging SMS’s vendors perform a manual review processes on 10DLC (10 Digit Long Code) campaigns
to address SMS spam concerns raised by US carriers. Reviews are triggered when a number is
associated to a 10DLC campaign. Reviews take at least 4 to 6 weeks to process.

When you register a 10DLC campaign, you provide a description of your use case, as well as
the message templates that you plan to use. Before you can create and register a 10DLC
campaign, you must first register your company. For information on registering your company,
see [10DLC brand registration form](registrations-10dlc-company.md "registrations-10dlc-company.md").

###### Note

For more information on expected registration times, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").

For more information on 10DLC campaign registration issues, see [Gen-AI Feedback on Registrations (Preview)](registrations-genai-feedback.md "registrations-genai-feedback.md").

In this section, you provide additional details about your 10DLC campaign.

###### To register a 10DLC campaign

1.  Open the AWS End User Messaging SMS console at
    [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2.  In the navigation pane, under **Registrations**, choose the 10DLC
    campaign registration to complete.
3.  On the **10DLC campaign registration information** page, do the following:
    1. For **Campaign description**, enter a name for the 10DLC
       campaign and description of the campaigns purpose.
    2. For **Vertical**, choose the option that represents your
       company.
    3. For **Company Terms & Conditions** choose
       either:
       1. **Enter URL** – Enter the publicly
          accessible URL that contains the **Terms &
          Conditions**.
       2. **Upload file** and then **Choose
          file** – Choose a file that contains the
          **Terms & Conditions**. The file can be up
          to 500KB and valid file formats are PNG, JPEG, and PDF.

    4. For **Privacy Policy** choose either:
       1. **Enter URL** – Enter the publicly accessible URL that contains the
          **Privacy Policy**.
       2. **Upload file** and then **Choose file** – Choose a
          file that contains the **Privacy Policy**. The file
          can be up to 500KB and valid file formats are PNG, JPEG, and PDF.

    5. For **Campaign opt-in workflow**, enter a description of
       how users consent to receive SMS and MMS messages. The description has to be
       between 40 – 2048 characters and must not contain leading or trailing
       spaces. For example, by filling out an online form on your website. If you
       have multiple opt-in methods, they have to be listed as well.

    Your **Opt-in workflow** should include the
    following:

        * Program or product description
        * Identify your organization and service being represented in the
         initial message sent to your end users
        * Clear and thorough information about how your end-users opt-in to
         your SMS service and any associated fees or charges
        * Include a link to the Terms & Conditions (which must be
         publicly accessible).
        * Include a link to the Privacy Policy (which must be publicly
         accessible).

        ###### Note

        If you don't have publicly accessible links to your Company
         Terms & Conditions or Privacy Policy documents then you can
         provide a copy of those as a document in the attachment fields
         for **Company Terms & Conditions** or
         **Privacy Policy**.
        * Explain if the Opt-in/Call to Action requires service log-in, is
         not yet published publicly, is a verbal opt-in, or if it occurs on
         printed sources such as fliers and paper forms.
        * The Call to Action/Opt-in location must include the
         following:




        	+ Comprehensive terms and conditions might be presented in
        	 full beneath the call-to-action, or they might be accessible
        	 from a link in proximity to the call-to-action.
        	+ Program (brand) name.
        	+ Message frequency disclosure.
        	+ Product description.
        	+ Customer care contact information.
        	+ Opt-out information.
        	+ “Message and data rates may apply” disclosure.

    6. For **Campaign opt-in screenshot - _optional_**, upload a
       file showing how users consent to receiving messages, as described in the
       **Campaign opt-in workflow** field. The supported file
       type are PNG, JPEG, and PDF and the maximum file size is 500KB. Additional
       information and examples of a compliant opt-in workflow can be found at
       [Obtain permission](best-practices.md#best-practices-sms-obtain-permission "best-practices.md#best-practices-sms-obtain-permission").

    ###### Important

    ###### Examples of opt-in mockups or screenshots:

        * **Website opt-in**: Mockup or screenshots of a
         web-form where the client adds their number and agrees to receive
         messages.
        * **Website Posting (Support)**: Where is the number advertised and where does the customer find the number to text in.
        * **Keyword or QR Code Opt-in**: Where does the
         customer find the keyword or QR code in order to opt-in to these messages.
        * **2FA/OTP**: Mockup or screenshot of opt-in if
         applicable, if verbal, provide a mockup or screenshot of the verbal opt-in
         script.
        * **Informational**: Provide a mockup or screenshot
         of a verbal consent workflow and provide the messaging content.

    7. For
       **Opt-in keyword – optional**
       enter the keyword that your customers will send to consent to opt-ing
       in.
    8. For **Opt-in confirmation message** enter the message
       that your customers receive if they send the Opt-in keyword to your 10DLC
       phone number.
    9. For **Help Message**, enter the message that your
       customers receive if they send the keyword "HELP" to your 10DLC phone
       number. The message has to be a minimum of 20 characters.
    10. For **Stop Message**, enter the message that your
        customers receive if they send the keyword "STOP" to your 10DLC phone
        number. The message has to be a minimum of 20 characters.

    ###### Tip

    Your customers can reply to your messages with the word "HELP" to
    learn more about the messages that they're receiving from you. They can
    also reply "STOP" to opt-out of receiving messages from you. The US
    mobile carriers require you to provide responses to both of these
    keywords.

    The following is an example of a HELP response that complies with the
    requirements of the US mobile carriers:

    `ExampleCorp Account Alerts: For help call 1-888-555-0142 or
 go to example.com. Msg&data rates may apply. Text STOP to
 cancel.`

    The following is an example of a compliant STOP response:

    `You are unsubscribed from ExampleCorp Account Alerts. No
 more messages will be sent. Reply HELP for help or call
 1-888-555-0142.`

    Your responses to these keywords must contain 160 characters or
    fewer.

4.  Choose **Next**.
5.  For the **Messaging capabilities** section, do the
    following:
    1. The capabilities you select are applied to your 10DLC phone number when you create the
       phone number request.

    For **Number capabilities**,
    choose:

        * Choose **SMS** to enable text messages for the 10DLC
         campaign.
        * Choose **SMS and MMS** to enable text and multimedia
         messages for the 10DLC campaign.
        * Choose **SMS and Voice** to enable text and voice
         messages for the 10DLC campaign.


        ###### Note

        When you choose to enable voice messages, it lengthens the amount of
         time to review your registration.
        * Choose **SMS and MMS and VOICE** to enable text and multimedia
         messages for the 10DLC campaign.

    2. For **Message type – optional**, choose either
       **Transactional** or **Promotional** message
       type.
       - **Transactional** – Choose this option if your use
         case is for time-sensitive content, such as alerts and one-time
         passwords.
       - **Promotional** – Choose this option if your use
         case is for marketing-related content.

6.  Choose **Next**.
7.  For **Messaging use case** section, do the following:
    1. For **Use case**, choose a use case that most closely
       resembles your campaign from the preset list of use cases.
       - **Account Notifications** – Standard
         notifications for account holders, relating to and being about an
         account.
       - **Charity** – Communications from a
         non-religious registered [501(c)(3) charity](<https://en.wikipedia.org/wiki/501(c)(3)_organization> "https://en.wikipedia.org/wiki/501(c)(3)_organization") aimed at providing
         help and raising money for those in need.
       - **Customer care** – All customer
         interaction, including account management and customer
         support.
       - **Delivery notifications** – Information
         about the status of the delivery of a product or service.
       - **Fraud alert messaging** – Messaging
         regarding potential fraudulent activity on an account.
       - **Higher education** – Campaigns created on
         behalf of Colleges or Universities. It also includes School
         Districts and education institutions that fall outside of any
         "free to the consumer" messaging model.
       - **Low Volume** – Small throughput, any
         combination of use-cases. Examples include: test, demo
         accounts.
       - **Marketing** – Any communication with
         marketing and/or promotional content.
       - **Mixed** – Mixed messaging reserved for
         specific consumer service industry.
       - **Public service announcement** – An
         informational message that is meant to raise the audience's
         awareness about an important issue.
       - **Polling and voting** – Requests for
         surveys and voting for non political arenas.
       - **Security alert** – A notification that
         the security of a system, either software or hardware, has been
         compromised in some way and there is an action the end users need to
         take.
       - **Two factor authentication** – Any authentication, verification,
         or one-time passcode.

    2. For **Sub use case – optional**, choose up to five
       sub use cases.
    3. **Subscriber opt-in** – Subscribers can opt in to
       receive messages about this campaign.
    4. **Subscriber opt-out** – Subscribers can opt out of
       receiving messages about this campaign.
    5. **Subscriber help** – Subscribers can contact the
       message sender after sending the HELP keyword.
    6. **Direct lending or loan arrangement** – The
       campaign includes information about direct lending or other loan
       arrangements.
    7. **Embedded link** – Choose
       **Yes** if the 10DLC campaign includes an embedded
       link. Links from common URL shorteners, such as TinyUrl or Bit.ly, are not
       allowed. However, you can use URL shorteners that offer custom
       domains.
    8. **Embedded link sample - optional** – An example of an embedded link
       that to be sent. Links from common URL shorteners, such as TinyUrl or
       Bit.ly, are not allowed. However, you can use URL shorteners that offer
       custom domains.
    9. **Embedded phone number** – The campaign includes a
       phone number that isn't a customer support number.
    10. **Age-gated content** – The 10DLC campaign includes
        age-gated content as defined by carrier and Cellular Telecommunications and
        Internet Association (CTIA) guidelines.

8.  Choose **Next**.
9.  In the **Message samples** section, do the following:
    1. Enter at least one **Message sample**. This is the sample
       text message that you plan to send to your customers. Each sample message
       has to be a minimum of 20 characters. If you plan to use multiple message
       templates for this 10DLC campaign, include them as well.

    ###### Important

    Don't use placeholder text for your sample messages. The example
    messages that you provide should reflect the actual messages that you
    plan to send as accurately as possible and should not contain any [Prohibited message content](best-practices.md#best-practices-sms-message-content "best-practices.md#best-practices-sms-message-content").

10. Choose **Next**.
11. In the **MMS file samples** section, do the following:
    1. (Optional) MMS sample files are only required if you plan to send MMS
       messages. In **MMS file samples** upload at least one
       sample image. A single MMS media file can be up to 500KB for GIF, JPEG, and
       PNG, and 600 KB in size for all other media file types, see [MMS file types, size and character limits](mms-limitations-character.md "mms-limitations-character.md").

    ###### Important

    Don't use placeholder text in your sample MMS images. The example
    MMS images that you provide should reflect the actual MMS image that you
    plan to send as accurately as possible and should not contain any [Prohibited message content](best-practices.md#best-practices-sms-message-content "best-practices.md#best-practices-sms-message-content").

12. Choose **Next**.
13. On the **Review and submit** page, verify the information you're
    about to submit is correct. To make updates choose **Edit** next to
    the section.
14. Choose **Submit registration**.

###### Note

After your 10DLC campaign registration has been approved you can request a new
10DLC phone number or use an existing 10DLC phone number and associate it with
the 10DLC campaign. For more information on registering for 10DLC, see [Requesting dedicated long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md").
