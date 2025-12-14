# Vietnam sender ID registration in AWS End User Messaging SMS

Follow these directions to register your sender ID in Vietnam.

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Registrations**, choose **Create
   registration**.

###### Note

If you already created a registration when requesting the origination identity then you
should use that registration form.

For **Registration form name** enter a friendly name.

Choose **Next**. 3. In the **Sender ID info** section, enter the following:

    * For **Sender ID**, enter the sender ID to request. The sender ID must be between 3 and 11 alphanumeric characters. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations "sender-id.md#sender-id-considerations")
    * For **Sender ID description – optional** you can add more details about the connection between the requested sender ID and company name.

Choose **Next**. 4. In the **Vietnam specific info** section, enter the following:

    * For **Letter of authorization: Local**, if your company is local to Vietnam, then you are required to download, complete, and attach the [letter of authorization (LOA)](samples/Vietnam_SenderId_LetterOfAuthorization_Local.md "samples/Vietnam_SenderId_LetterOfAuthorization_Local.md"), also called a BM02 form. **This document must be on company letterhead, stamped, and signed with company seal on all pages**. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Letter of authorization: International**, if your company is not local to Vietnam, then you are required to download, complete, and attach the [letter of authorization (LOA)](samples/Vietnam_SenderId_LetterOfAuthorization_International.md "samples/Vietnam_SenderId_LetterOfAuthorization_International.md"), also called a BM04 form. **This document must be on company letterhead, stamped, and signed with company seal on all pages**. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Company registration documentation**, you are required to provide a copy of your company's registration documentation, regardless if your company is local to Vietnam or international. This document is also known as a business license. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Financial sector business license (SSC)**, if your company operates in the financial sector, you must submit a business license issued by the State Securities Commission (SSC) in addition to the standard business license and BM02/BM04 form. This is a mandatory requirement from Vietnamese operators for all financial sector registrations. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Proof of sender ID connection**, you are required to provide evidence of your intellectual property rights to the sender ID you wish to register. The document you provide should demonstrate the connection between your company name and this sender ID. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Acknowledgement of transactional content**, promotional content is disallowed for Vietnam sender IDs. Choose **Yes** to acknowledge that this sender ID will only be used for sending transactional messages.

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

Choose **Next**. 9. All messages must include your brand/service name. If your company operates locally in Vietnam, all provided message samples must have an English and Vietnamese version, and all provided message samples must include a URL to your business website. Message samples must be provided in template format, and must be an exact match to what you intend to send.
If there are variables in the template, ensure that you define them correctly. Define if the variable is text/number only or alphanumeric; if there's any special characters, or URL. Define variable length

In **Message samples**, do the following:

    * For **Message Sample 1**, enter at least one sample is required of an SMS message which will be sent from this sender ID.
    * For **Message Sample 2 – optional** and **Message Sample
     3 – optional**, enter additional example messages, if needed, of the
     SMS message body that will be sent.

Choose **Next**. 10. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section. 11. Choose **Submit registration**.
