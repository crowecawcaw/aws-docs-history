

# Australia registration
<a name="nx-country-reg-au"></a>

## Sender ID registration
<a name="nx-country-reg-au-senderid"></a>

Starting July 1, 2026, the Australian Communications and Media Authority (ACMA) requires all alphanumeric SMS sender IDs used to send messages to Australian recipients to be registered in the ACMA SMS Sender ID Register. Messages sent using an unregistered sender ID will be labeled as "Unverified" or may be blocked by Australian carriers. Please submit your registration as soon as possible to allow time for processing before the enforcement date.

Follow these directions to register your sender ID in Australia.

### Before you begin
<a name="nx-registration-australia-registrations-australia-before-you-begin"></a>

To satisfy ACMA's verification process, your registration must establish three things. Have the supporting evidence for each ready before you start:


| What you must establish | Evidence to have ready | 
| --- | --- | 
| Business or entity verification | Proof of the legal entity that owns the sender ID, such as an ASIC company extract for Australian companies or the equivalent business registry document. | 
| Authorized representative verification | A person authorized to act for the entity, verified with a government-issued photo ID and, where required, a Letter of Authorization. | 
| Sender ID use-case verification | Evidence that the sender ID matches your business name or brand. | 

The next section describes exactly what to provide for each attachment and the most common reasons registrations are denied.

### Guidance for Australia sender ID registration
<a name="nx-registration-australia-registrations-australia-guidance"></a>

The documentation and identity requirements on the registration form are required to satisfy ACMA's sender ID verification process. The following guidance addresses the most common questions about these requirements.

#### Document requirements and common reasons for denial
<a name="nx-registration-australia-registrations-australia-document-requirements"></a><a name="nx-registration-australia-registrations-australia-loa-requirements"></a><a name="nx-registration-australia-registrations-australia-company-registration-docs"></a>

The following requirements apply to each document and identity attachment on the registration form. Most denials are caused by avoidable mismatches between these attachments. Review each item before submitting.


| Attachment | Requirements | Common reasons for denial | 
| --- | --- | --- | 
| Government-issued photo ID | A current, unexpired government photo ID (driver's license or passport) of the authorized representative named on the registration form. The name on the ID must match the authorized representative's first and last name exactly. If the ID has information on both sides, such as an Australian driver's license, include both sides, and make sure the image is legible. | The ID belongs to a different person than the named authorized representative, the name does not match the form, the ID is expired, or the image is cropped, blurred, or missing a required side. | 
| Letter of authorization (LOA) | Required only when the authorized representative is not listed on the company registration documentation. When required, use the current template linked on the registration form, signed by a director, officer, or company secretary listed on that documentation, and explicitly naming the sender ID or sender IDs being registered. The representative named in the LOA must match the authorized representative on the form. A company secretary is an officer for this purpose and is an acceptable signer. | An outdated LOA template, a signer who is not listed on the company registration documentation, an LOA that does not name the specific sender ID, or a representative that does not match the form. | 
| Company registration documentation | For Australian companies, a current ASIC company extract or annual company statement that lists the entity's directors and officers, with a legal entity name matching the company name on the form and the ABN. For a trust, provide the extract for the corporate trustee. For international entities, provide the equivalent official business registry extract from the country of incorporation. Australian government entities that are not ASIC-registered follow the ABR steps in the note after this table. | The document does not show directors or officers (for example, a simple ABN lookup instead of a full company extract), only the first page of the ASIC extract is included, the entity name does not match the form or the ABN, or the extract is for a related but different legal entity. | 
| Proof of sender ID connection | Required when the connection between your company name and the requested sender ID is not obvious. The sender ID string must be an exact match, or a clear abbreviation, acronym, or initialism, of the registered business name, brand, or trademark. Acceptable evidence includes a registered business name, a trademark certificate, or a domain registration that resolves to a website associated with the brand. | The sender ID does not clearly relate to the verified business name or brand, or the supporting evidence does not reference the entity being registered. | 

**Note**  
**For Australian government entities** that are not ASIC-registered, follow these steps to obtain your ABR documentation:  
Navigate to the [Australian Business Register](https://abr.gov.au).
Under **Online Services**, select **Update your ABN details**.
Log in using your myID app credentials.
Select **Update ABN record** to view non-public ABR information.
Choose the **Contacts** tab.
Take a screenshot of the information in that tab. This shows the authorized contacts for your ABN.
Submit this screenshot as the **Company registration documentation** attachment on the registration form.
This screenshot serves as proof that the authorized representative is listed on the business registry. If the authorized representative appears in the **Contacts** tab, no separate LOA is needed.

#### Processing times
<a name="nx-registration-australia-registrations-australia-processing-times"></a>

Typical estimated completion time is 2 weeks from successful submission. Processing times may vary during high-volume periods, particularly as the ACMA SMS Sender ID Register enforcement date (July 1, 2026) approaches.

### Confirming your ACMA registration status
<a name="nx-registration-australia-registrations-australia-confirmation"></a>

After you submit your registration, it is shared with the relevant reviewers for processing. When ACMA approves your sender ID registration, there are two indicators of approval:


| Approval indicator | What it confirms | 
| --- | --- | 
| Email from ACMA | ACMA sends a confirmation email directly to the authorized representative email address that you provided during registration. This confirms that ACMA has approved your sender ID. | 
| Console status | The registration status changes to Complete on the Registrations page in the AWS End User Messaging console. This confirms the registration is fully recorded in AWS End User Messaging. | 

The ACMA confirmation email and the console status update do not always arrive at the same time. Because registration is processed through a downstream partner, there can be a delay of up to one to two days between when ACMA sends the confirmation email and when the registration status updates to **Complete** in the console.

If you receive the ACMA confirmation email, your sender ID is registered with ACMA and is compliant for the July 1, 2026 enforcement date. The ACMA confirmation email is the authoritative signal of ACMA registration. Because registration is processed through a downstream partner, the console status typically updates to **Complete** within one to two days afterward.

ACMA compliance and AWS End User Messaging sending behavior are separate. The ACMA confirmation email confirms your sender ID is registered with ACMA and is compliant for the July 1, 2026 enforcement date. However, AWS End User Messaging does not apply your sender ID to outbound messages until the registration status is **Complete** in the console. Although the registration is still in **Reviewing**, the service treats the sender ID as unregistered, even after you have received the ACMA confirmation email. Your messages continue to be sent from a shared Australian long code or displayed as "Unverified" until the console status changes to **Complete**.

### Delivery behavior for unregistered sender IDs after July 1, 2026
<a name="nx-registration-australia-registrations-australia-unregistered-delivery"></a>

Starting July 1, 2026, unregistered sender IDs will change how your messages appear to Australian recipients. If you have not completed registration, your messages might be delivered from a shared Australian long code or might be displayed as "Unverified" by Australian carriers. In some cases, carriers might block messages from unregistered sender IDs entirely.

When delivery succeeds, the difference is in how the origination identity appears to the end user. A shared Australian phone number or "Unverified" might be displayed instead of your sender ID string.

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

1. In the **Sender ID info** section, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Sender ID</td><td>Required</td><td>The sender ID to register, between 3 and 11 alphanumeric characters, matching your business name or brand. For the formatting rules that affect what you can register, see <a href="nx-features-senders.md#nx-features-senders-considerations">Considerations for a sender ID</a>.</td></tr>
  <tr><td>Sender ID description</td><td>Optional</td><td>Additional detail about the connection between the requested sender ID and your company name.</td></tr>
  <tr><td>Proof of sender ID connection</td><td>Required</td><td>Evidence of your rights to the sender ID, such as a business registration certificate, trademark certificate, or domain certification. ACMA requires proof that the sender ID matches your entity name. Valid file types are PDF, PNG, and JPEG, with a maximum size of 500 KB. For what is accepted, see <a href="#nx-registration-australia-registrations-australia-document-requirements">Document requirements and common reasons for denial</a>.</td></tr>
</tbody>
</table>


1. In the **Australia specific info** section, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Australian Business Number (ABN)</td><td>Required</td><td>Your 11-digit Australian Business Number as registered with the Australian Business Register (ABR). If you do not have an ABN, enter your international business registration number.</td></tr>
  <tr><td>Entity type</td><td>Required</td><td>The entity type that matches your ACMA registration. Choose one of: Individual, Body corporate, Corporation sole, Body politic, Government entity, Partnership, Unincorporated association, Trust, or Superannuation fund.</td></tr>
  <tr><td>Authorized representative first name and last name</td><td>Required</td><td>The full name of the authorized representative for this registration. The representative must be a director or officer listed on your business registry, or you must provide a letter of authorization.</td></tr>
  <tr><td>Authorized representative email</td><td>Required</td><td>The corporate email address of the authorized representative. Freemail addresses (such as Gmail or Yahoo) are not accepted.</td></tr>
  <tr><td>Authorized representative phone number</td><td>Required</td><td>The phone number of the authorized representative.</td></tr>
  <tr><td>Global headquarters country</td><td>Optional</td><td>The country where your company's global headquarters is located, if different from your business address.</td></tr>
  <tr><td>Government-issued photo ID</td><td>Required</td><td>A government-issued photo ID of the authorized representative, required for ACMA verification. Valid file types are PDF, PNG, and JPEG, with a maximum size of 500 KB. For the requirements, see <a href="#nx-registration-australia-registrations-australia-document-requirements">Document requirements and common reasons for denial</a>.</td></tr>
  <tr><td>Letter of authorization</td><td>Optional</td><td>Required only when your authorized representative is not listed as a director or officer on your business registry. When required, download, complete, and attach the <a href="samples/Australia_SenderId_LetterOfAuthorization.zip">letter of authorization</a>, signed by a listed director or officer. Valid file types are PDF, PNG, and JPEG, with a maximum size of 500 KB. For when it is required and how to complete it, see <a href="#nx-registration-australia-registrations-australia-document-requirements">Document requirements and common reasons for denial</a>.</td></tr>
  <tr><td>Company registration documentation</td><td>Required</td><td>A copy of your company's registration documentation showing officers and directors, such as an ASIC company extract for Australian entities or the equivalent for international entities. Valid file types are PDF, PNG, and JPEG, with a maximum size of 500 KB. For what to submit, including guidance for government entities, see <a href="#nx-registration-australia-registrations-australia-document-requirements">Document requirements and common reasons for denial</a>.</td></tr>
</tbody>
</table>


1. In the **Company info** section, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Company name</td><td>Required</td><td>The legal name of your company.</td></tr>
  <tr><td>Company identification number</td><td>Required</td><td>For Australian entities, your Australian Business Number (ABN). For international entities, your business or trade license number, VAT number, or other legal identification number.</td></tr>
  <tr><td>Doing Business As (DBA)</td><td>Optional</td><td>Your DBA or brand name, if different from the legal name of your company.</td></tr>
  <tr><td>Company website</td><td>Required</td><td>The full URL of your company's website.</td></tr>
  <tr><td>Area of business</td><td>Required</td><td>The vertical that most closely aligns with your company's area of business. Choose one of: Agriculture, Communication, Construction, Education, Energy, Entertainment, Financial, Government, Healthcare, Hospitality, Insurance, Manufacturing, Real estate, Retail, Technology, or Other.</td></tr>
</tbody>
</table>


1. In the **Company address** section, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Address 1</td><td>Required</td><td>The street address of your corporate headquarters.</td></tr>
  <tr><td>Address 2</td><td>Optional</td><td>The suite or unit number of your corporate headquarters, if applicable.</td></tr>
  <tr><td>City</td><td>Required</td><td>The city of your corporate headquarters.</td></tr>
  <tr><td>State/Province</td><td>Optional</td><td>The state, province, or region of your corporate headquarters.</td></tr>
  <tr><td>Postal code</td><td>Optional</td><td>The postal or ZIP code of your corporate headquarters.</td></tr>
  <tr><td>Country</td><td>Required</td><td>The two-digit ISO country code of your corporate headquarters.</td></tr>
</tbody>
</table>


1. In the **Contact info** section, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Contact email</td><td>Required</td><td>The email address of your business's point of contact.</td></tr>
  <tr><td>Contact phone number</td><td>Required</td><td>The phone number of your business's point of contact.</td></tr>
</tbody>
</table>


1. In **Messaging use case**, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Use case category</td><td>Required</td><td>The category that most closely aligns with your use case. Choose one of: One-time passcodes, Account or security alerts, Purchase or delivery notifications, Public service announcements, Polling and surveys, Info on demand, Promotions and marketing, or Other.</td></tr>
  <tr><td>Use case description</td><td>Required</td><td>Additional context for the selected use case category.</td></tr>
  <tr><td>Monthly SMS volume</td><td>Required</td><td>The estimated number of SMS messages sent from this sender ID each month. Choose one of: 10, 100, 1,000, 10,000, 100,000, 1,000,000, or 10,000,000+.</td></tr>
  <tr><td>Opt-in workflow description</td><td>Required</td><td>A description of how your end users consent to receive messages, between 40 and 500 characters, with no leading or trailing spaces. Include a program or product description, identify your organization and the service represented in the initial message, and explain how end users opt in and any associated fees or charges.</td></tr>
</tbody>
</table>


1. In **Message samples**, enter the following, then choose **Next**.


<table>
<thead>
  <tr><th>Field</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Message Sample 1</td><td>Required</td><td>An example of an SMS message body that will be sent to your end users.</td></tr>
  <tr><td>Message Sample 2</td><td>Optional</td><td>An additional example message, if applicable.</td></tr>
  <tr><td>Message Sample 3</td><td>Optional</td><td>An additional example message, if applicable.</td></tr>
</tbody>
</table>


1. On the **Review and submit** page, verify the information you are about to submit is correct. To make updates, choose **Edit** next to the section.

1. Choose **Submit registration**.