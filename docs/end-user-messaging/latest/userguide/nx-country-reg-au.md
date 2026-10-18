

# Australia registration
<a name="nx-country-reg-au"></a>

The following registrations are available for Australia.

## Sender ID registration
<a name="nx-country-reg-au-senderid"></a>

Starting July 1, 2026, the Australian Communications and Media Authority (ACMA) requires all alphanumeric SMS sender IDs used to send messages to Australian recipients to be registered in the ACMA SMS Sender ID Register. Messages sent using an unregistered sender ID will be labeled as "Unverified" or may be blocked by Australian carriers. Please submit your registration as soon as possible to allow time for processing before the enforcement date.

Follow these directions to register your sender ID in Australia.

### Before you begin
<a name="nx-registration-australia-registrations-australia-before-you-begin"></a>

To satisfy ACMA's verification process, your registration must establish three things. Have the supporting evidence for each ready before you start:
+ **Business or entity verification** – proof of the legal entity that owns the sender ID, such as an ASIC company extract for Australian companies or the equivalent business registry document.
+ **Authorized representative verification** – a person authorized to act for the entity, verified with a government-issued photo ID and, where required, a Letter of Authorization.
+ **Sender ID use-case verification** – evidence that the sender ID matches your business name or brand.

The next section describes exactly what to provide for each attachment and the most common reasons registrations are denied.

### Guidance for Australia sender ID registration
<a name="nx-registration-australia-registrations-australia-guidance"></a>

The documentation and identity requirements on the registration form are required to satisfy ACMA's sender ID verification process. The following guidance addresses the most common questions about these requirements.

#### Document requirements and common reasons for denial
<a name="nx-registration-australia-registrations-australia-document-requirements"></a><a name="nx-registration-australia-registrations-australia-loa-requirements"></a><a name="nx-registration-australia-registrations-australia-company-registration-docs"></a>

The following requirements apply to each document and identity attachment on the registration form. Most denials are caused by avoidable mismatches between these attachments. Review each item before submitting.

Government-issued photo ID  
Must be a current, unexpired government photo ID (driver's license or passport) belonging to the *authorized representative named on the registration form*. The name on the ID must match the authorized representative's first and last name exactly. If the ID has information on both sides (for example, an Australian driver's license), include both sides. The image must be legible.  
**Common reasons for denial:** the ID belongs to a different person than the named authorized representative; the name does not match the form; the ID is expired; the image is cropped, blurred, or missing a required side.

Letter of authorization (LOA)  
An LOA is required *only* when the authorized representative is not listed on the company registration documentation. If the authorized representative matches a contact already listed on that documentation, no LOA is needed.  
When an LOA is required, use the current template linked on the registration form. The LOA must be signed by a person who is listed as a director, officer, or company secretary on the company registration documentation, and it must explicitly name the sender ID (or sender IDs) being registered. The authorized representative named in the LOA must match the authorized representative on the registration form.  
**Common reasons for denial:** an outdated LOA template; the signer is not listed on the company registration documentation; the LOA does not name the specific sender ID; the representative on the LOA does not match the form. A company secretary is an officer for this purpose and is an acceptable signer.

Company registration documentation  
For Australian companies, provide a current ASIC company extract or annual company statement that lists the entity's directors and officers. The legal entity name on the extract must match the company name on the registration form and the ABN. For a trust, provide the extract for the corporate trustee. For international entities, provide the equivalent official business registry extract from the country of incorporation.  
**For Australian government entities** that are not ASIC-registered, follow these steps to obtain your ABR documentation:  

1. Navigate to the [Australian Business Register](https://abr.gov.au).

1. Under **Online Services**, select **Update your ABN details**.

1. Log in using your myID app credentials.

1. Select **Update ABN record** to view non-public ABR information.

1. Choose the **Contacts** tab.

1. Take a screenshot of the information in that tab. This shows the authorized contacts for your ABN.

1. Submit this screenshot as the **Company registration documentation** attachment on the registration form.
This screenshot serves as proof that the authorized representative is listed on the business registry. If the authorized representative appears in the **Contacts** tab, no separate LOA is needed.  
**Common reasons for denial:** the document does not show directors or officers (for example, a simple ABN lookup instead of a full company extract); only the first page of the ASIC extract is included rather than the complete extract that lists directors and officers; the entity name does not match the form or the ABN; the extract is for a related but different legal entity than the one being registered.

Proof of sender ID connection  
Required when the connection between your company name and the requested sender ID is not obvious. The sender ID string must be an exact match, or a clear abbreviation, acronym, or initialism, of the registered business name, brand, or trademark. Acceptable evidence includes a registered business name, a trademark certificate, or a domain registration that resolves to a website associated with the brand.  
**Common reasons for denial:** the sender ID does not clearly relate to the verified business name or brand; the supporting evidence does not reference the entity being registered.

#### Processing times
<a name="nx-registration-australia-registrations-australia-processing-times"></a>

Typical estimated completion time is 2 weeks from successful submission. Processing times may vary during high-volume periods, particularly as the ACMA SMS Sender ID Register enforcement date (July 1, 2026) approaches.

### Confirming your ACMA registration status
<a name="nx-registration-australia-registrations-australia-confirmation"></a>

After you submit your registration, it is shared with the relevant reviewers for processing. When ACMA approves your sender ID registration, there are two indicators of approval:
+ **Email from ACMA** – ACMA sends a confirmation email directly to the authorized representative email address that you provided during registration. This confirms that ACMA has approved your sender ID.
+ **Console status** – The registration status changes to **Complete** on the **Registrations** page in the AWS End User Messaging console. This confirms the registration is fully recorded in AWS End User Messaging.

The ACMA confirmation email and the console status update do not always arrive at the same time. Because registration is processed through a downstream partner, there can be a delay of up to one to two days between when ACMA sends the confirmation email and when the registration status updates to **Complete** in the console.

If you receive the ACMA confirmation email, your sender ID is registered with ACMA and is compliant for the July 1, 2026 enforcement date. The ACMA confirmation email is the authoritative signal of ACMA registration. Because registration is processed through a downstream partner, the console status typically updates to **Complete** within one to two days afterward.

ACMA compliance and AWS End User Messaging sending behavior are separate. The ACMA confirmation email confirms your sender ID is registered with ACMA and is compliant for the July 1, 2026 enforcement date. However, AWS End User Messaging does not apply your sender ID to outbound messages until the registration status is **Complete** in the console. Although the registration is still in **Reviewing**, the service treats the sender ID as unregistered — even after you have received the ACMA confirmation email. Your messages continue to be sent from a shared Australian long code or displayed as "Unverified" until the console status changes to **Complete**.

### Delivery behavior for unregistered sender IDs after July 1, 2026
<a name="nx-registration-australia-registrations-australia-unregistered-delivery"></a>

Starting July 1, 2026, unregistered sender IDs will change how your messages appear to Australian recipients. If you have not completed registration, your messages might be delivered from a shared Australian long code or might be displayed as "Unverified" by Australian carriers. In some cases, carriers might block messages from unregistered sender IDs entirely.

When delivery succeeds, the difference is in how the origination identity appears to the end user — a shared Australian phone number or "Unverified" might be displayed instead of your sender ID string.

After your sender ID registration is approved and the status changes to **Complete** in the console, your messages will resume displaying your registered sender ID.

This behavior applies only to alphanumeric sender IDs. Messages sent from dedicated long codes, short codes, or other phone number types are not affected.

### Australia sender ID registration frequently asked questions
<a name="nx-registration-australia-registrations-australia-faq"></a>

Frequently asked questions about the Australia sender ID registration process.

#### Do I need to register the same sender ID separately for each AWS account?
<a name="nx-registration-australia-registrations-australia-faq1"></a>

Yes. Sender ID registration applies per AWS account and AWS Region. If you send with the same sender ID from more than one account, either submit a registration from each account, or register the sender ID in one account and share that origination identity with your other accounts using AWS Resource Access Manager (RAM). For more information, see [Sharing AWS End User Messaging resources](shared-resources.html).

#### I already registered my sender ID directly with ACMA or through another provider. Do I still need to register it through AWS End User Messaging?
<a name="nx-registration-australia-registrations-australia-faq2"></a>

Yes. Each provider that sends messages using your sender ID must have that sender ID registered. Registering through AWS End User Messaging ensures the traffic you send from AWS is verified and is not labeled "Unverified."

#### Are Australia sender IDs case-sensitive?
<a name="nx-registration-australia-registrations-australia-faq3"></a>

No. Alphanumeric sender IDs are case-insensitive for registration and verification. For example, "MyBrand," "MYBRAND," and "mybrand" are treated as the same sender ID. Use consistent capitalization for branding in your messages.

### Australia sender ID registration form
<a name="nx-registration-australia-form"></a>

Complete the Australia sender ID registration form to submit your sender ID for ACMA verification. For the documents and identity evidence you must attach, and the most common reasons registrations are denied, see [Document requirements and common reasons for denial](#nx-registration-australia-registrations-australia-document-requirements).

**Complete an Australia sender ID registration**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**.
**Note**  
If you already created a registration when requesting the origination identity, use that registration form.

   For **Registration form name**, enter a friendly name. Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. The sender ID must be between 3 and 11 alphanumeric characters. For more information on sender ID formatting rules, see sender ID considerations.
   + For **Sender ID description – optional**, you can add more details about the connection between the requested sender ID and company name.
   + For **Proof of sender ID connection – optional**, if the connection between your company name and this sender ID is not obvious, provide evidence of your rights to the brand. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For what is accepted, see [Document requirements and common reasons for denial](#nx-registration-australia-registrations-australia-document-requirements).

   Choose **Next**.

1. In the **Australia specific info** section, enter the following:
   + For **Australian Business Number (ABN)**, enter your 11-digit Australian Business Number as registered with the Australian Business Register (ABR). If you do not have an ABN, enter your international business registration number.
   + For **Entity type**, select the entity type that matches your registration. Options include: Individual, Body corporate, Corporation sole, Body politic, Government entity, Partnership, Unincorporated association, Trust, and Superannuation fund.
   + For **Authorized representative first name** and **Authorized representative last name**, enter the full name of the authorized representative for this registration.
   + For **Authorized representative email**, enter the corporate email address of the authorized representative. Freemail addresses (such as Gmail or Yahoo) are not accepted.
   + For **Authorized representative phone number**, enter the phone number of the authorized representative.
   + For **Global headquarters country** (optional), select the country where your company's global headquarters is located, if different from your business address.
   + For **Government-issued photo ID**, upload a government-issued photo ID of the authorized representative. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For the requirements, see [Document requirements and common reasons for denial](#nx-registration-australia-registrations-australia-document-requirements).
   + For **Letter of authorization** (optional), download, complete, and attach the [letter of authorization](samples/Australia_SenderId_LetterOfAuthorization.zip). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. An LOA is not always required. For when it is required and how to complete it, see [Document requirements and common reasons for denial](#nx-registration-australia-registrations-australia-document-requirements).
   + For **Company registration documentation**, provide a copy of your company's registration documentation. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For what to submit (including guidance for government entities), see [Document requirements and common reasons for denial](#nx-registration-australia-registrations-australia-document-requirements).
   + For **Proof of sender ID connection**, provide evidence of your rights to the sender ID. Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB. For what is accepted, see [Document requirements and common reasons for denial](#nx-registration-australia-registrations-australia-document-requirements).

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
   + For **State/Province (optional)**, enter the state of your corporate headquarters.
   + For **Postal code (optional)**, enter the postal or zip code of your corporate headquarters.
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

## Dedicated number registration
<a name="nx-country-reg-au-dednum"></a>

Registering a dedicated number is the first step in creating an origination identity.

To request a long code phone number, see the long code request process.

Follow these directions to register your dedicated number in Australia.

**Complete Common Dedicated Number registration form**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose the registration number to complete.
**Note**  
If you already created a registration when requesting the toll-free number then you can use that registration form. 

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the legal name of your company. 
   + For **Company identification number**, enter the legal identification number of your company (such as EIN or VAT).
   + For **Doing Business As (DBA) name**, enter the DBA or brand name if different from the legal name of your company.
   + For **Company website**, enter the full URL of your company website.

   Choose **Next**.

1. In the **Company Address** section, enter the following:
   + For **Address 1**, enter the physical street address associated with your company.
   + For **Address 2**, enter the unit number of the physical address, if applicable.
   + For **City** enter city where the physical address is located.
   + For **State / Province (optional)**, enter the state, province, or region where the physical address is located.
   + For **Postal code (optional)**, enter the postal code / ZIP code where the physical address is located.
   + For **Country code**, enter the two-digit ISO country code where the physical address is located.

   Choose **Next**.

1. In the ** Service Information and Use Case** section, enter the following:

   In order to give approval, mobile carriers need to know how you plan to use your dedicated number, and how you will interact with end users.
   + For **Service name**, Name of your SMS service or feature.
   + For **Use case category**, select the category which most closely aligns with your use case.
   + For **Use case description**, enter a description of your use case for sending SMS messages with this long code..
   + For **Monthly SMS volume**, enter a estimated number of SMS messages which will be sent from this long code each month.
   + For **Is this a one-way or two-way program?**, select whether you require only sending outbound messages with this number or if you require 2-way messaging (both outbound and inbound).
   + For **Opt-in Method**, enter a how the user will opt-in..
   + For **Opt-in method other**, ff you chose Other, please explain.
   + For **Opt-in method user experience flow 1**, provide a step-by-step description of the end user experience when signing up for the SMS service..
   + For **Opt-in mock-up 1**, attach a mock up showing the call-to-action or opt-in location.
   + For **Opt-in method user experience flow 2**, provide a step-by-step description of the end user experience when signing up for the SMS service.
   + For **Opt-in mock-up 2**, attach a mock up showing the call-to-action or opt-in location.
   + For **Opt-in method user experience flow 3**, provide a step-by-step description of the end user experience when signing up for the SMS service.
   + For **Opt-in mock-up 3**, attach a mock up showing the call-to-action or opt-in location.

   Choose **Next**.

1. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.

1. Choose **Submit registration**.