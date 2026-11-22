

# China short code registration in AWS End User Messaging SMS

**Mainland China business entity required**  
A China short code is available only to companies with a mainland China presence. A business registered outside mainland China does not satisfy this requirement. The contact person's identity document must be a Chinese ID, because the mobile operators' systems only recognize Chinese IDs.  
If your company is not registered in mainland China, you can establish a mainland China legal entity through the local branch of the State Administration for Market Regulation (SAMR) or a local municipal administrative service center, and then register with that entity's business license.

Registering a short code lets your company send two-way SMS messages to recipients in China that meet local carrier requirements. Follow these directions to register a short code in China. Short code registration takes about 10 business days. A one-time setup fee and a monthly fee apply to a China short code. For pricing, see the [pricing page](https://aws.amazon.com/end-user-messaging/pricing/).

**Note**  
A China short code is a non-standard number that can vary by mobile network. Your recipients might see a different number depending on their mobile carrier.

**Before you begin**

Before you create the registration, have the following ready. You cannot submit the registration without them.
+ Your mainland China business license.
+ A copy of the contact person's Chinese ID, and the contact person's name and mobile number.
+ Your signature: at least 2 Chinese characters that match your registered company name or trademark. You must prepend this signature, in full-width brackets (【 】), to the start of every message you send.
+ The completed [letter of undertaking](samples/China_LetterOfUndertaking.zip) and [signature registration form](samples/China_SignatureRegistrationForm.zip). Download both templates from the links in this guide, complete them, and attach them during registration.
+ If your signature differs from your registered company name, a trademark certificate or other official document that proves the relationship. A letter of authorization is not accepted.
+ Example message content for each template you plan to send. AWS End User Messaging SMS matches your content exactly against what you register and blocks anything you have not registered. Use the Chinese period (`。`) instead of the English period (`.`) in your message content.

**Complete a China short code registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**, and then choose the China short code registration.
**Note**  
If you already created a registration when requesting the origination identity, use that registration form.

   For **Registration form name**, enter a friendly name.

   Choose **Next**.

1. In the **Company info** section, enter the following:
   + For **Company name**, enter the name of your company as it appears on your business license.
   + For **Signature**, enter the signature that appears at the start of your message body. Use at least 2 Chinese characters that match your registered company name or trademark. Spaces are allowed; pure numbers and special symbols are not. You must prepend this registered signature, enclosed in full-width brackets (【 】), to the body of every message you send. AWS End User Messaging SMS does not add it for you, so each message must begin with the signature exactly as you register it here.

   Choose **Next**.

1. In the **Supporting documents** section, enter the following:
   + For **Business license**, provide a copy of your mainland China business license. A company registered outside mainland China does not satisfy this requirement. If your company is not registered in mainland China, you can establish a mainland China legal entity through the local branch of the State Administration for Market Regulation (SAMR) or a local municipal administrative service center, and then register with that entity's business license. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Representative ID**, provide a copy of the Chinese ID of the contact person named in the signature registration form. The contact person must have a Chinese ID. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Letter of undertaking**, you must download, complete, and attach the [letter of undertaking](samples/China_LetterOfUndertaking.zip). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Signature registration form**, you must download, complete, and attach the [signature registration form](samples/China_SignatureRegistrationForm.zip), completing all required fields. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.
   + For **Trademark certificate** (optional), provide this only if your signature differs from your registered company name. Provide a trademark certificate or other official document that proves the relationship between the signature and your company; a letter of authorization is not accepted. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500 KB.

   Choose **Next**.

1. In the **Message templates** section, provide example message content for each template you plan to send. You can also attach a list of your message templates. AWS End User Messaging SMS matches your message content exactly against the templates you register and blocks any content that you have not registered.

   The following CSV example shows a message template list. Each row is one message template, beginning with your registered signature in full-width brackets, with no sender ID and no separate signature column:

   ```
   No,Message template
   1,【示例】Your verification code is 123456。Valid for 10 minutes。Do not share it with anyone。
   2,【示例】Your one-time password is 123456 for completing your payment。
   ```

   Choose **Next**.

1. On the **Review and submit** page, verify the information you are about to submit is correct. To make updates, choose **Edit** next to the section.

1. Choose **Submit registration**.