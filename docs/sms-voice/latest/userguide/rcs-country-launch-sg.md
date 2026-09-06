

# Launching RCS in Singapore
<a name="rcs-country-launch-sg"></a>

To launch your AWS RCS Agent in Singapore, submit a country launch registration using the `SG_RCS_LAUNCH_REGISTRATION` registration type. Singapore has a significant prerequisite: you must have a registered SMS sender on the SGNIC portal before you can register for RCS.

**Important**  
Before you can register for RCS in Singapore, you must have a registered SMS sender ID on the SGNIC (Singapore Network Information Centre) portal. Your RCS agent display name must exactly match your registered SMS sender name. This is required regardless of whether you intend to send SMS in Singapore.

## SGNIC SMS sender prerequisite
<a name="rcs-country-launch-sg-prerequisites"></a>

If you have not already registered an SMS sender in Singapore, complete the following steps first:

1. **Register your company on the SGNIC portal** at [https://www.sgnic.sg/](https://www.sgnic.sg/) (if not already registered).

1. **Register an SMS Sender Name/ID** on the SGNIC portal. The sender name is limited to 11 characters (spaces are allowed). SGNIC will contact you to confirm the registration.

1. **Wait for SGNIC approval** of your SMS sender.

For detailed instructions on Singapore SMS sender registration, see [Singapore sender ID registration process](registrations-sg.md).

**Warning**  
Your RCS agent display name must **exactly match** the SMS sender name registered on SGNIC. Mismatches will result in registration denial. Verify your SGNIC sender name before submitting your RCS registration.

**Note**  
The SGNIC prerequisite can add significant time to the Singapore launch process. If you do not already have a registered SMS sender in Singapore, plan for the SGNIC registration to take additional weeks before you can submit your RCS registration.

## Registration form (console)
<a name="rcs-country-launch-sg-console"></a>

The Singapore launch registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration. The display name must match your SGNIC registered sender name.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Screen recording** — A screen recording that demonstrates your RCS messaging experience. For detailed video requirements, see [Launch video requirements](rcs-compliance-video.md).
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.
+ **Bizfile** (optional in form) — Your Singapore business registration document from ACRA (Accounting and Corporate Regulatory Authority of Singapore).
+ **RBM LOA Template** (optional in form) — Letter of Authorization for RCS messaging. Download the pre-filled template below, complete the required fields, and upload it with your registration.

**Important**  
Although the Bizfile and LOA fields are marked as optional in the registration form, they are required for Singtel carrier approval. Singtel is the largest carrier in Singapore. We strongly recommend providing both documents when you submit your registration.

## Letter of Authorization (LOA)
<a name="rcs-country-launch-sg-loa"></a>

Download the LOA template, complete the required fields, and upload it as part of your Singapore RCS registration. The template has the aggregator (Infobip) and representative (AWS) details pre-filled — you only need to fill in your company information.

Download the LOA template: [Singapore\_RCS\_LOA\_Template.zip](samples/Singapore_RCS_LOA_Template.zip)

Complete the following fields in the template:

**Date**  
The date you are signing the LOA.

**Brand Owner Company Name and UEN**  
Your company's legal name and Unique Entity Number (UEN) as registered in Singapore.

**Authorized employee(s) table**  
The name, last four digits of NRIC (or equivalent ID for non-Singaporeans), and designation of each person authorized to give instructions on your behalf.

**Protected SID(s) table**  
Your registered Sender ID(s) as they appear on the SGNIC portal, along with effective date, expiration date, and scope.

**Brand Contact Information**  
Full name, job title, email address, and phone number of your brand contact person.

**Signature**  
Name, title, and company stamp of the authorized signatory on behalf of the brand owner.

**Important**  
The completed LOA must be printed on your company letterhead and must include your company stamp. LOAs submitted without company letterhead or a company stamp will be rejected.

**Note**  
The following fields are pre-filled in the template and should not be changed:  
**To:** INFOBIP, LTD
**Cc:** AMAZON WEB SERVICES SINGAPORE PRIVATE LIMITED
**Representative:** AMAZON WEB SERVICES SINGAPORE PRIVATE LIMITED (UEN 201434292D)

## After submitting your registration
<a name="rcs-country-launch-sg-after-submission"></a>

After you submit your Singapore RCS registration in the console with the Bizfile and completed LOA:
+ Provide a screenshot showing your sender name is active on the SGNIC portal.
+ Singtel will contact your brand contact person for final confirmation.

## Carrier coverage
<a name="rcs-country-launch-sg-carriers"></a>

Singapore has four carriers with different requirements:
+ **Singtel** — Requires the full SGNIC prerequisite, Bizfile, and LOA (described above).
+ **M1, StarHub, TPG** — Standard approval process with no additional requirements beyond the registration form.

**Note**  
Your agent may reach PARTIAL status (approved on M1, StarHub, and TPG) while Singtel completes their additional review process. You can begin sending RCS messages to recipients on approved carriers while waiting for Singtel approval.

## Approval timeline
<a name="rcs-country-launch-sg-timeline"></a>

The Singapore approval process includes the following steps:

1. Complete SGNIC SMS sender registration (if not already done) — timeline varies.

1. Submit the country launch registration in the AWS End User Messaging console.

1. Provide Bizfile, LOA, and SGNIC screenshot.

1. Singtel reviews and contacts your brand contact for confirmation.

1. Agent launches after Singtel approval.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).