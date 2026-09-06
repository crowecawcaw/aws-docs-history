

# Australia sender ID registration form
<a name="registrations-australia-form"></a>

Complete the Australia sender ID registration form to submit your sender ID for ACMA verification. For the documents and identity evidence you must attach, and the most common reasons registrations are denied, see [Document requirements and common reasons for denial](registrations-australia.md#registrations-australia-document-requirements).

**Complete an Australia sender ID registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**.
**Note**  
If you already created a registration when requesting the origination identity, use that registration form.

   For **Registration form name**, enter a friendly name. Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. The sender ID must be between 3 and 11 alphanumeric characters. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations).
   + For **Sender ID description – optional**, you can add more details about the connection between the requested sender ID and company name.
   + For **Proof of sender ID connection – optional**, if the connection between your company name and this sender ID is not obvious, provide evidence of your rights to the brand. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For what is accepted, see [Document requirements and common reasons for denial](registrations-australia.md#registrations-australia-document-requirements).

   Choose **Next**.

1. In the **Australia specific info** section, enter the following:
   + For **Australian Business Number (ABN)**, enter your 11-digit Australian Business Number as registered with the Australian Business Register (ABR). If you do not have an ABN, enter your international business registration number.
   + For **Entity type**, select the entity type that matches your registration. Options include: Individual, Body corporate, Corporation sole, Body politic, Government entity, Partnership, Unincorporated association, Trust, and Superannuation fund.
   + For **Authorized representative first name** and **Authorized representative last name**, enter the full name of the authorized representative for this registration.
   + For **Authorized representative email**, enter the corporate email address of the authorized representative. Freemail addresses (such as Gmail or Yahoo) are not accepted.
   + For **Authorized representative phone number**, enter the phone number of the authorized representative.
   + For **Global headquarters country** (optional), select the country where your company's global headquarters is located, if different from your business address.
   + For **Government-issued photo ID**, upload a government-issued photo ID of the authorized representative. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For the requirements, see [Document requirements and common reasons for denial](registrations-australia.md#registrations-australia-document-requirements).
   + For **Letter of authorization** (optional), download, complete, and attach the [letter of authorization](samples/Australia_SenderId_LetterOfAuthorization.zip). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. An LOA is not always required. For when it is required and how to complete it, see [Document requirements and common reasons for denial](registrations-australia.md#registrations-australia-document-requirements).
   + For **Company registration documentation**, provide a copy of your company's registration documentation. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For what to submit (including guidance for government entities), see [Document requirements and common reasons for denial](registrations-australia.md#registrations-australia-document-requirements).
   + For **Proof of sender ID connection**, provide evidence of your rights to the sender ID. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For what is accepted, see [Document requirements and common reasons for denial](registrations-australia.md#registrations-australia-document-requirements).

   Choose **Next**.

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the name of your company.
   + For **Company identification number**, enter the identification number of your company. For Australian entities, provide your Australian Business Number (ABN). For international entities, provide your business or trade license number, VAT number, or other legal identification number.
   + For **Doing Business As (DBA)**, enter your DBA or brand name if different from the legal name of your company.
   + For **Company website**, enter the URL for your company's website.

   Choose **Next**.

1. In the **Company address** section, enter the following:
   + For **Address 1**, enter the street address of your corporate headquarters.
   + For **Address 2 - optional**, if needed enter the suite number of your corporate headquarters.
   + For **City**, enter the city of your corporate headquarters.
   + For **State/Province**, enter the state of your corporate headquarters.
   + For **Postal code**, enter the postal or zip code of your corporate headquarters.
   + For **Country**, enter the two digit ISO country code.

   Choose **Next**.

1. In the **Contact info** section, enter the following:
   + For **Contact Email**, enter the email address of the person who will be your business's point of contact.
   + For **Contact Phone Number**, enter the phone number of the person who will be your business's point of contact.

   Choose **Next**.

1. In **Messaging Use Case**, do the following:
   + For **Use case category**, choose one of the following use case types:
     + **One-time passwords** – Use this for sending a user a one-time password.
     + **Purchase or delivery notifications** – Use this if you only intend to send your users important notifications.
     + **Public service announcements** – An informational message that is meant to raise the audience's awareness about an important issue.
     + **Polling and surveys** – Use this to poll users on their preferences.
     + **Info on demand** – This is for sending users messages after they have sent a request.
     + **Promotions and Marketing** – Use this if you only intend to send marketing messages to your users.
     + **Other** – Use this if your use case doesn't fall into any other category. Be sure that you fill out the **Use case details** for this option.
   + Complete **Use case description** to provide additional context to the selected **Use case category**.
   + For **Monthly SMS Volume**, choose the number of SMS messages that will be sent each month.
   + For **Opt-in workflow description**, enter a description of how users consent to receive messages. The description must be between 40 and 500 characters and must not contain leading or trailing spaces. Your description should include a program or product description, identify your organization and the service represented in the initial message, and clearly explain how end users opt in and any associated fees or charges.

   Choose **Next**.

1. In **Message samples**, do the following:
   + For **Message Sample 1**, enter an example of an SMS message body that will be sent to your end users.
   + For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages, if needed.

   Choose **Next**.

1. On the **Review and submit** page, verify the information you are about to submit is correct. To make updates, choose **Edit** next to the section.

1. Choose **Submit registration**.