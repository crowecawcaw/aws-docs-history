

# China sender ID registration in AWS End User Messaging SMS

**Mainland China business entity required**  
To register a sender for China, the registration must be held by a company that is legally registered in mainland China. A business registered outside mainland China does not satisfy this requirement. The contact person's identity document must be a Chinese ID, because the mobile operators' systems only recognize Chinese IDs.  
If your company is not registered in mainland China, you can establish a mainland China legal entity through the local branch of the State Administration for Market Regulation (SAMR) or a local municipal administrative service center, and then register with that entity's business license.

Registering a sender ID lets your company send SMS messages to recipients in China that meet local carrier requirements. Follow these directions to register your sender ID in China. Sender ID registration takes about 10 business days.

**Before you begin**

Before you create the registration, have the following ready. You cannot submit the registration without them.
+ Your mainland China business license.
+ A copy of the contact person's Chinese ID, and the contact person's name and mobile number.
+ Your signature: at least 2 Chinese characters that match your registered company name or trademark. You must prepend this signature, in full-width brackets (【 】), to the start of every message you send.
+ The completed [letter of undertaking](samples/China_LetterOfUndertaking.zip) and [signature registration form](samples/China_SignatureRegistrationForm.zip). Download both templates from the links in this guide, complete them, and attach them during registration.
+ If your signature differs from your registered company name, a trademark certificate or other official document that proves the relationship. A letter of authorization is not accepted.
+ Example message content for each template you plan to send. AWS End User Messaging SMS matches your content exactly against what you register and blocks anything you have not registered. Use the Chinese period (`。`) instead of the English period (`.`) in your message content.

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**.
**Note**  
If you already created a registration when requesting the origination identity then you should use that registration form. 

   For **Registration form name** enter a friendly name.

   Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. The sender ID must be between 3 and 11 alphanumeric characters. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations)
   + For **Sender ID description – optional** you can add more details about the connection between the requested sender ID and company name.
   + For **Proof of sender ID connection – optional**, if the connection between your company name and this sender ID is not obvious, then you are required to provide evidence of your intellectual property rights to the brand. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.

   Choose **Next**.

1. In the **China specific info** section, enter the following:
   + For **Signature**, enter the signature that appears at the start of your message body. Use at least 2 Chinese characters that match your registered company name or trademark. Spaces are allowed; pure numbers and special symbols are not. You must prepend this registered signature, enclosed in full-width brackets (【 】), to the body of every message you send. AWS End User Messaging SMS does not add it for you, so each message must begin with the signature exactly as you register it here.
   + For **Business license**, provide a copy of your mainland China business license. A company registered outside mainland China does not satisfy this requirement. If your company is not registered in mainland China, you can establish a mainland China legal entity through the local branch of the State Administration for Market Regulation (SAMR) or a local municipal administrative service center, and then register with that entity's business license. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Representative ID**, provide a copy of the Chinese ID of the contact person named in the signature registration form. The contact person must have a Chinese ID. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Letter of undertaking**, you must download, complete, and attach the [letter of undertaking](samples/China_LetterOfUndertaking.zip). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Signature registration form**, you must download, complete, and attach the [signature registration form](samples/China_SignatureRegistrationForm.zip), completing all required fields. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Trademark certificate** (optional), provide this only if your signature differs from your registered company name. Provide a trademark certificate or other official document that proves the relationship between the signature and your company; a letter of authorization is not accepted. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Message template list** (optional), you can attach a list of the message templates you plan to send. AWS End User Messaging SMS matches your message content exactly against the templates you register and blocks any content that you have not registered.

   The following CSV example shows a message template list. Each row is one message template, beginning with your registered signature in full-width brackets, with no sender ID and no separate signature column:

   ```
   No,Message template
   1,【示例】Your verification code is 123456。Valid for 10 minutes。Do not share it with anyone。
   2,【示例】Your one-time password is 123456 for completing your payment。
   ```

   Choose **Next**.

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the name of your company. 
   + For **Company identification number**, enter your tax ID, like EIN or VAT. 
   + For **Doing Business As (DBA)**, enter your DBA or brand name if different from the legal name of your company. 
   + For **Company website**, enter the URL for your company's website. 

   Choose **Next**.

1. In the **Company address** section, enter the following:
   + For **Address 1**, enter the street address of your corporate headquarters. 
   + For **Address 2 - optional**, if needed enter suite number of your corporate headquarters. 
   + For **City**, enter the city of your corporate headquarters. 
   + For **State/Province**, enter the state of your corporate headquarters. 
   + For **Postal code**, enter the Postal/Zip code of your corporate headquarters. 
   + For **Country**, enter the two digit ISO country code. 

   Choose **Next**.

1. In the **Contact info** section, enter the following:
   + For **Contact Email**, enter the email address of the person who will be your business's point of contact.
   + For **Contact Phone Number**, enter the phone number of the person who will be your business's point of contact.

   Choose **Next**.

1. In **Messaging Use Case**, do the following:
   + For **Use case category**, choose one of the following use case types: 
     +  **One-time passwords** – Use this for sending a user a one time password.
     +  **Purchase or delivery notifications** – Use this if you only intend to send your users important notifications.
     +  **Public service announcements** – An informational message that is meant to raise the audience's awareness about an important issue.
     +  **Polling and surveys** – Use this to poll users on their preferences.
     +  **Info on demand** – This is for sending users messages after they have sent a request.
     +  **Other** – Use this if your use case doesn't fall into any other category. Be sure that you fill out the **Use case details** for this option.
   + Complete **Use case description** to provide additional context to the selected **Use case category**.
   + For **Monthly SMS Volume**, choose the number of SMS messages that will be each month.
   + For **Opt-in workflow description**, enter a description of how users consent to receive messages. The description has to be between 40 – 500 characters and must not contain leading or trailing spaces. For example, by filling out an online form on your website. 

     Your **Opt-in workflow description** should include the following:
     + Program or product description
     + Identify your organization and service being represented in the initial message sent to your end users
     + Clear and thorough information about how your end-users opt-in to your SMS service and any associated fees or charges

   Choose **Next**.

1. In **Message samples**, do the following:
   + For **Message Sample 1**, enter an example message of an SMS message body that will be sent to your end users. 
   + For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages, if needed, of the SMS message body that will be sent.

   Choose **Next**.

1. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.

1. Choose **Submit registration**.