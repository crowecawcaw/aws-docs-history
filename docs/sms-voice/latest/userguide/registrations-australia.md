# Australia sender ID registration in AWS End User Messaging SMS

Starting July 1, 2026, the Australian Communications and Media Authority (ACMA) requires
all alphanumeric SMS sender IDs used to send messages to Australian recipients to be
registered in the ACMA SMS Sender ID Register. Messages sent using an unregistered sender ID
will be labeled as "Unverified" or may be blocked by Australian carriers. Please
submit your registration as soon as possible to allow time for processing before the
enforcement date.

Follow these directions to register your sender ID in Australia.

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
    * For **Proof of sender ID connection – optional**, if the connection between your company name and this sender ID is not obvious, then you are required to provide evidence of your intellectual property rights to the brand. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.

Choose **Next**. 4. In the **Australia specific info** section, enter the following:

    * For **Australian Business Number (ABN)**, enter your 11-digit Australian Business Number as registered with the Australian Business Register (ABR). If you do not have an ABN, enter your international business registration number.
    * For **Entity type**, select the entity type that matches your registration. Options include: Individual, Body corporate, Corporation sole, Body politic, Government entity, Partnership, Unincorporated association, Trust, and Superannuation fund.
    * For **Authorized representative first name** and **Authorized representative last name**, enter the full name of the authorized representative for this registration. This person must be a Director or Officer listed on your business registry, or you must provide a letter of authorization.
    * For **Authorized representative email**, enter the corporate email address of the authorized representative. Freemail addresses (such as Gmail or Yahoo) are not accepted.
    * For **Authorized representative phone number**, enter the phone number of the authorized representative.
    * For **Global headquarters country** (optional), select the country where your company's global headquarters is located, if different from your business address.
    * For **Government-issued photo ID**, upload a government-issued photo ID of the authorized representative (such as a driver's license or passport). This is required for ACMA verification. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Letter of authorization** (optional), if your authorized representative is not listed as a Director or Officer on your business registry, download, complete, and attach the [letter of authorization](samples/Australia_SenderId_LetterOfAuthorization.zip.md "samples/Australia_SenderId_LetterOfAuthorization.zip.md"). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Company registration documentation**, provide a copy of your company's registration documentation showing officers and directors (for example, an ASIC company extract for Australian entities, or equivalent documentation for international entities). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.
    * For **Proof of sender ID connection**, provide evidence of your intellectual property rights to the sender ID (for example, business registration, trademark certificate, or domain certification). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.

Choose **Next**. 5. In the **Company info** section, enter the following:

    * For **Company Name**, enter the name of your company.
    * For **Company identification number**, enter the identification number of your company. For Australian entities, provide your Australian Business Number (ABN). For international entities, provide your business/trade license number, VAT number, or other legal identification number.
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
    	+ **Promotions and Marketing** – Use this if you only intend
    	 to send marketing messages to your users.
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
