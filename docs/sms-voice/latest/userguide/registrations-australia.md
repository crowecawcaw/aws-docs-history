

# Australia sender ID registration in AWS End User Messaging SMS
<a name="registrations-australia"></a>

Starting July 1, 2026, the Australian Communications and Media Authority (ACMA) requires all alphanumeric SMS sender IDs used to send messages to Australian recipients to be registered in the ACMA SMS Sender ID Register. Messages sent using an unregistered sender ID will be labeled as "Unverified" or may be blocked by Australian carriers. Please submit your registration as soon as possible to allow time for processing before the enforcement date.

Follow these directions to register your sender ID in Australia.

## Before you begin
<a name="registrations-australia-before-you-begin"></a>

To satisfy ACMA's verification process, your registration must establish three things. Have the supporting evidence for each ready before you start:
+ **Business or entity verification** – proof of the legal entity that owns the sender ID, such as an ASIC company extract for Australian companies or the equivalent business registry document.
+ **Authorized representative verification** – a person authorized to act for the entity, verified with a government-issued photo ID and, where required, a Letter of Authorization.
+ **Sender ID use-case verification** – evidence that the sender ID matches your business name or brand.

The next section describes exactly what to provide for each attachment and the most common reasons registrations are denied.

## Guidance for Australia sender ID registration
<a name="registrations-australia-guidance"></a>

The documentation and identity requirements on the registration form are required to satisfy ACMA's sender ID verification process. The following guidance addresses the most common questions about these requirements.

### Document requirements and common reasons for denial
<a name="registrations-australia-document-requirements"></a><a name="registrations-australia-loa-requirements"></a><a name="registrations-australia-company-registration-docs"></a>

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

### Processing times
<a name="registrations-australia-processing-times"></a>

Typical estimated completion time is 2 weeks from successful submission. Processing times may vary during high-volume periods, particularly as the ACMA SMS Sender ID Register enforcement date (July 1, 2026) approaches.

## Confirming your ACMA registration status
<a name="registrations-australia-confirmation"></a>

After you submit your registration, it is shared with the relevant reviewers for processing. When ACMA approves your sender ID registration, there are two indicators of approval:
+ **Email from ACMA** – ACMA sends a confirmation email directly to the authorized representative email address that you provided during registration. This confirms that ACMA has approved your sender ID.
+ **Console status** – The registration status changes to **Complete** on the **Registrations** page in the AWS End User Messaging SMS console. This confirms the registration is fully recorded in AWS End User Messaging SMS.

The ACMA confirmation email and the console status update do not always arrive at the same time. Because registration is processed through a downstream partner, there can be a delay of up to one to two days between when ACMA sends the confirmation email and when the registration status updates to **Complete** in the console.

If you receive the ACMA confirmation email, your sender ID is registered with ACMA and is compliant for the July 1, 2026 enforcement date. The ACMA confirmation email is the authoritative signal of ACMA registration. Because registration is processed through a downstream partner, the console status typically updates to **Complete** within one to two days afterward.

ACMA compliance and AWS End User Messaging SMS sending behavior are separate. The ACMA confirmation email confirms your sender ID is registered with ACMA and is compliant for the July 1, 2026 enforcement date. However, AWS End User Messaging SMS does not apply your sender ID to outbound messages until the registration status is **Complete** in the console. Although the registration is still in **Reviewing**, the service treats the sender ID as unregistered — even after you have received the ACMA confirmation email. Your messages continue to be sent from a shared Australian long code or displayed as "Unverified" until the console status changes to **Complete**.

## Delivery behavior for unregistered sender IDs after July 1, 2026
<a name="registrations-australia-unregistered-delivery"></a>

Starting July 1, 2026, unregistered sender IDs will change how your messages appear to Australian recipients. If you have not completed registration, your messages might be delivered from a shared Australian long code or might be displayed as "Unverified" by Australian carriers. In some cases, carriers might block messages from unregistered sender IDs entirely.

When delivery succeeds, the difference is in how the origination identity appears to the end user — a shared Australian phone number or "Unverified" might be displayed instead of your sender ID string.

After your sender ID registration is approved and the status changes to **Complete** in the console, your messages will resume displaying your registered sender ID.

This behavior applies only to alphanumeric sender IDs. Messages sent from dedicated long codes, short codes, or other phone number types are not affected.

## Australia sender ID registration frequently asked questions
<a name="registrations-australia-faq"></a>

Frequently asked questions about the Australia sender ID registration process.

### Do I need to register the same sender ID separately for each AWS account?
<a name="registrations-australia-faq1"></a>

Yes. Sender ID registration applies per AWS account and AWS Region. If you send with the same sender ID from more than one account, either submit a registration from each account, or register the sender ID in one account and share that origination identity with your other accounts using AWS Resource Access Manager (RAM). For more information, see [Sharing AWS End User Messaging SMS resources](shared-resources.html).

### I already registered my sender ID directly with ACMA or through another provider. Do I still need to register it through AWS End User Messaging SMS?
<a name="registrations-australia-faq2"></a>

Yes. Each provider that sends messages using your sender ID must have that sender ID registered. Registering through AWS End User Messaging SMS ensures the traffic you send from AWS is verified and is not labeled "Unverified."

### Are Australia sender IDs case-sensitive?
<a name="registrations-australia-faq3"></a>

No. Alphanumeric sender IDs are case-insensitive for registration and verification. For example, "MyBrand," "MYBRAND," and "mybrand" are treated as the same sender ID. Use consistent capitalization for branding in your messages.