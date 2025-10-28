# Ireland sender ID registration in AWS End User Messaging SMS

Follow these directions to register your sender ID in Ireland.

###### Important

Before you begin your Ireland sender ID registration with AWS End User Messaging SMS, you must first
complete registration on the Ireland Commission for Communications Regulation (ComReg)
Sender ID registration portal at
[https://senderid.comreg.ie/sender-id-sign-up](https://senderid.comreg.ie/sender-id-sign-up "https://senderid.comreg.ie/sender-id-sign-up").

When completing your ComReg Sender ID Registration, make sure you complete the
following:

- In ComReg’s Section 2, choose **Assign a 3rd party** and
  **Amazon Web Services**.
- In ComReg’s Section 3 "Select OPAs," choose all of the following:

      + **Sinch Sweden AB**
      + **Telesign Corporation**
      + **Twilio Inc**
      + **Vonage**

  Failure to choose **Amazon Web Services** as a third party or failure
  to choose all of the OPAs might result in impact to your SMS delivery to Ireland. After
  ComReg has approved your sender ID registration, you can proceed with the AWS
  registration process below.

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

Choose **Next**. 4. In the **Ireland specific info** section, enter the following:

    * For **Sender ID Owner (SIDO) Number ID**, enter the SIDO number your received from ComReg when registering. You can find your SIDO number in the ComReg registry portal by logging in and choosing the account icon in the top-right corner of the home screen.
    * For **Company registration documentation**, upload the registration documentation for your company. This can be a certificate of incorporation (COI), trade license, or international equivalent.

Choose **Next**. 5. In the **Company info** section, enter the following:

    * For **Company Name**, enter the name of your company.
    * For **Company identification number**, enter your tax ID, like EIN or VAT.
    * For **Doing Business As (DBA)**, enter your DBA or brand name if different from the legal name of your company.
    * For **Company website**, enter the URL for your company's
     website.
    * **Area of business**
    * **Company customer care email address**
    * **Company customer care phone number**

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

    * **First name**
    * **Last name**
    * **Contact email address**
    * **Contact phone number**

Choose **Next**. 8. In **Messaging Use Case**, provide

    * **Use case category**, choose one of the following use
     case types:




    	+ **One-time passwords** – Use this for sending a user a one
    	 time password.
    	+ **Account or security alerts**
    	+ **Purchase or delivery notifications** – Use this if you only intend to send
    	 your users important notifications.
    	+ **Public service announcements** – An informational message that is meant to raise the audience's awareness about an important issue.
    	+ **Polling and surveys** – Use this to poll users on their
    	 preferences.
    	+ **Info on demand** – This is for sending users messages
    	 after they have sent a request.
    	+ **Promotions and marketing**
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

Choose **Next**. 9. In **Message samples**, provide:

    * At least one message sample (required)
    * Up to two additional message samples (optional)

Choose **Next**. 10. On the **Review and submit** page verify the information you are about to submit is correct.
To make updates choose **Edit** next to the section. 11. Choose **Submit registration**.
