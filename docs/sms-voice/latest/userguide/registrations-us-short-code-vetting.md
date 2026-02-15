# Brand vetting requirements

The CTIA (Cellular Telecommunications Industry Association) and the US Short Code Registry
require all brands to complete a vetting process when leasing new short codes and annually
thereafter. This vetting process is designed to enhance consumer protection and improve
transparency in SMS messaging.

The vetting process validates the following information for each entity:

- Company name and legal entity type
- Federal Employer Identification Number (FEIN/EIN)
- Corporate registration
- Compliance history
- Legal history
  Once a brand is successfully vetted for short code leases, you don't need to go through
  the entire vetting process again when leasing additional codes. However, annual re-vetting
  is required to maintain your short code lease.

## How the vetting process works

AWS collects the required brand information (and content provider information, if
applicable) during the short code registration process. This information is submitted
to the US Short Code Registry so that their vetting agents can contact brand owners
to complete the vetting process and authorize the short code procurement.

The vetting process includes the following steps:

1. **Initial verification** – The vetting
   agent verifies that the legal name and Federal Employer Identification Number
   (FEIN) match, that the brand contact email is valid and relates to the
   company's published URL, and then triggers an authentication process.
2. **Email verification** – A verification
   PIN is sent to the brand's point of contact email address from
   `verify@usshortcodes.com`. The brand contact must click the
   verification link in the email and enter the PIN to complete the process.
3. **Completion** – Once verification is
   complete, the brand is approved and the short code can be provisioned.

###### Important

The verification PIN is valid for 7 days. A reminder is sent 48 hours before
the PIN expires. If the PIN expires, a second and final PIN is sent. If no
action is taken, you must create an AWS Support case to request the vetting
email be resent.

Common reasons for verification failure include:

- The information submitted does not match the brand's Form SS-4
  documentation provided by the IRS
- The brand is a new entity that has not yet been updated in
  verification systems
- The brand contact email uses a free email service (such as Gmail
  or Yahoo) instead of a company domain

If you need to appeal a verification failure, you can provide a copy of your
CP-575 notice (the official EIN confirmation letter issued by the IRS) for
further review via an AWS Support case.

## Contact information requirements

During the short code registration process, you must provide contact information
that will be used for vetting communications. The following fields are collected
in the registration form:

- **Contact name** – Name of your
  company's point of contact. If you are an ISV (Independent Software Vendor),
  enter your end customer's information.
- **Contact email address** – Email
  address of your company's point of contact. If you are an ISV, enter your
  end customer's information. This email will receive the verification PIN.
- **Contact phone number** – Phone
  number of your company's point of contact. If you are an ISV, enter your
  end customer's information.
- **Content provider name (ISV only)** –
  Optional. Name of the content provider point of contact.
- **Content provider email address (ISV only)** –
  Optional. Email address of the content provider point of contact.
- **Content provider phone number (ISV only)** –
  Optional. Phone number of the content provider point of contact.

###### Tip

Use a company email address that matches your company's website domain.
Free email services (such as Gmail, Yahoo, or Outlook.com) are not permitted
and will cause verification to fail.

## Tips for successful vetting

Follow these tips to ensure a smooth vetting process:

- **Add the verification email to your safe senders list** –
  The verification email comes from `verify@usshortcodes.com`. Add this
  address to your email safe senders list to ensure you receive the verification PIN.
- **Use your company email domain** –
  The brand contact email must match your company's website URL. Free email
  services are not permitted.
- **Ensure FEIN accuracy** –
  Your Federal Employer Identification Number (FEIN) and legal entity name must
  exactly match your IRS Form SS-4 or CP-575 documentation.
- **Complete verification promptly** –
  The verification PIN expires after 7 days. Complete the verification as soon
  as you receive the email to avoid delays.
- **Keep contact information current** –
  If your business contact details change, open a support case with AWS to
  update your information before the annual re-vetting period.

If you have problems completing the verification from the link in the email, try
the following:

- Turn off or pause your VPN
- Try a different browser
- Copy and paste the URL directly into your browser

## Annual re-vetting requirements

Re-vetting of brands is required annually by the US Short Code Registry. You should
expect to receive a verification email from `verify@usshortcodes.com`
approximately one year after your short code was provisioned to your account.

The annual re-vetting process is similar to the initial PIN verification:

1. The vetting agency sends an email to the brand point of contact on file
2. The email contains a verification link and PIN
3. You must complete the email verification within 7 days

###### Important

Failure to complete annual re-vetting can result in suspension of your short
code service. Monitor your email for verification requests and complete them
promptly.

If your business contact details have changed since your initial registration or
last re-vetting, you must open a support case with AWS to update your contact
information with the carriers before the annual re-vetting period. This ensures
that the verification email is sent to the correct recipient.
