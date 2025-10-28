# India sender ID registration

in AWS End User Messaging SMS

After you register your company and use case with TRAI, you must create a case with
Support. The Support team uses the information that you provide in your case to associate
your Entity ID and Template ID with your AWS account.

###### Note

India allows transactional sender IDs to be 3–6 characters in length.
Promotional sender IDs are required to be 6 characters. All sender ID approval is
owned by TRAI.

You can register a sender ID for [transactional
messages](#registrations-sms-senderid-india-support-case.title "#registrations-sms-senderid-india-support-case.title") using the AWS End User Messaging SMS console or to register a sender ID for [promotional messages](#registrations-sms-senderid-india-support.title "#registrations-sms-senderid-india-support.title")
create an AWS Support case.

## India transactional

message sender ID registration

Follow these directions to register your sender ID for transactional messages in
India.

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Registrations**, choose **Create
   registration**.

###### Note

If you already created a registration when requesting the origination identity then you
should use that registration form.

For **Registration form name** enter a friendly name.

Choose **Next**. 3. In the **Sender ID info** section, enter the following:

    * For **Sender ID**, enter the sender ID to request. India sender IDs must be 3-6 alphabetic characters.
    * For **Proof of sender ID connection – optional**, if the connection between your company name and this sender ID is not obvious, then you are required to provide evidence of your intellectual property rights to the brand. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.

Choose **Next**. 4. In the **India specific info** section, enter the following:

    * For **Chain ID: Principal Entity ID (PEID)**, enter the PEID that you received after completing the registration process with the Telecom Regulatory Authority of India (TRAI).
    * For **Chain ID: ROUTE LEDGER TECHNOLOGIES PRIVATE LIMITED**, enter the approved chain ID seen on your DLT platform after creating a chain of telemarketers.
    * For **Chain ID: Karix Mobile Pvt Ltd**, enter the approved chain ID seen on your DLT platform after creating a chain of telemarketers.
    * For **Chain ID: Sinch Cloud Communication Services India Private Limited**, enter the approved chain ID seen on your DLT platform after creating a chain of telemarketers.
    * For **Chain ID: Infobip India Private Limited**, enter the approved chain ID seen on your DLT platform after creating a chain of telemarketers.
    * For **Acknowledgement of required sending parameters**, choose Yes to acknowledge you will specify the [Entity ID and Template ID values](registrations-sms-senderid-india-specify-ids.md#registrations-sms-senderid-india-specify-ids.title "registrations-sms-senderid-india-specify-ids.md#registrations-sms-senderid-india-specify-ids.title") when you send your messages to India.

Choose **Next**. 5. In the **Company info** section, enter the following:

    * For **Company Name**, enter the name of your company.
    * For **Company identification number**, enter your tax ID, like EIN or VAT.
    * For **Doing Business As (DBA)**, enter your DBA or brand name if different from the legal name of your company.
    * For **Company website**, enter the URL for your company's
     website.

Choose **Next**. 6. In the **Company address** section, enter the following:

    * For **Address 1**, enter the street address of your corporate
     headquarters.
    * For **Address 2 - optional**, if needed enter suite number of
     your corporate headquarters.
    * For **City**, enter the city of your corporate headquarters.
    * For **State/Province**, enter the state of your corporate headquarters.
    * For **Postal code**, enter the Postal/Zip code of your corporate
     headquarters.
    * For **Country**, enter the two digit ISO country code.

Choose **Next**. 7. In the **Contact info** section, enter the following:

    * For **Contact Email**, enter the email address of the
     person who will be your business's point of contact.
    * For **Contact Phone Number**, enter the phone number of
     the person who will be your business's point of contact.

Choose **Next**. 8. In **Messaging Use Case**, do the following:

    * For **Use case category**, choose one of the following use case types:




    	+ **One-time passwords** – Use this for sending a user a one
    	 time password.
    	+ **Purchase or delivery notifications** – Use this if you only intend to send
    	 your users important notifications.
    	+ **Public service announcements** – An informational message that is meant to raise the audience's awareness about an important issue.
    	+ **Polling and surveys** – Use this to poll users on their
    	 preferences.
    	+ **Info on demand** – This is for sending users messages
    	 after they have sent a request.
    	+ **Other** – Use this if your use case doesn't
    	 fall into any other category. Be sure that you fill out the
    	 **Use case details** for this option.
    * Complete **Use case description** to provide additional
     context to the selected **Use case category**.
    * For **Monthly SMS Volume**, choose the number of SMS messages that
     will be each month.
    * For **Opt-in workflow description**, enter a description of
     how users consent to receive messages. The description has to be
     between 40 – 500 characters and must not contain leading or trailing
     spaces. For example, by filling out an online form on your website.


    Your **Opt-in workflow description** should include the
     following:




    	+ Program or product description
    	+ Identify your organization and service being represented in the
    	 initial message sent to your end users
    	+ Clear and thorough information about how your end-users opt-in to
    	 your SMS service and any associated fees or charges

Choose **Next**. 9. In **Message samples**, do the following:

    * For **Message Sample 1**, enter an example message of an SMS message
     body that will be sent to your end users.
    * For **Message Sample 2 – optional** and **Message Sample
     3 – optional**, enter additional example messages, if needed, of the
     SMS message body that will be sent.

Choose **Next**. 10. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section. 11. Choose **Submit registration**.

## India promotional

message sender ID registration

Follow these directions to register your sender ID for promotional messages in
India.

###### Register sender ID for promotional messages

1. Create an AWS Support case at [https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").
2. In the **Create Case** section, do the following:
   - For **Limit type**, choose
     **AWS End User Messaging SMS (Pinpoint)**.
   - For **Provide a link to the site or app which will be
     sending SMS messages**, identify the website or
     application where your audience members opt in to receive your SMS
     messages.
   - For **What type of messages do you plan to
     send**, choose **Promotional**:
     - **One Time Password** – Messages
       that provide passwords that your customers use to
       authenticate with your website or application.
     - **Promotional** – Noncritical
       messages that promote your business or service, such as
       special offers or announcements.
     - **Transactional** – Important
       informational messages that support customer transactions,
       such as order confirmations or account alerts. Transactional
       messages must not contain promotional or marketing
       content.

   - For **Which countries do you plan to send messages
     to**, choose the AWS Region that you will be sending
     messages from.

3. In the **Requests** section, do the following:
   - For the **Region**, choose the AWS Region that
     you plan to make API requests from.
   - For **Resource Type**, choose **Template
     Registration**.
   - For **Limit**, choose on of the following:
     - **One Time Password** – Messages
       that provide passwords that your customers use to
       authenticate with your website or application.
     - **Promotional** – Noncritical
       messages that promote your business or service, such as
       special offers or announcements.
     - **Transactional** – Important
       informational messages that support customer transactions,
       such as order confirmations or account alerts. Transactional
       messages must not contain promotional or marketing
       content.

4. Under **Case description**, for **Use case
   description**, explain your use case and opt-in workflow.
5. Under **Contact options**, for **Preferred
   contact language**, choose whether you want to receive
   communications for this case in **English** or
   **Japanese**.
6. When you finish, choose **Submit**.

After we receive your request, we provide an initial response within 24 hours. We
will send you a country-specific registration form for you to complete and provide
back to us for downstream processing.

###### Important

In order to prevent our systems from being used to send unsolicited or
malicious content, we consider each request carefully. We might not be able to
grant your request if your use case doesn't align with our policies.
