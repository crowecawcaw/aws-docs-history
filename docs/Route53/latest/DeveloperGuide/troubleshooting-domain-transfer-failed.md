# Transferring my domain to

Amazon Route 53 failed

If your domain transfer has already failed or been rejected, use this section to
diagnose and resolve the failure.

###### Note

For preventing issues during active transfers, see [Preventing common Route 53 transfer issues](domain-transfer-troubleshooting.md "domain-transfer-troubleshooting.md").

###### Topics

- [You didn't click
  the link in the authorization email](#troubleshooting-domain-transfer-failed-click-link "#troubleshooting-domain-transfer-failed-click-link")
- [The authorization code that you got from the current registrar is not valid](#troubleshooting-domain-transfer-failed-authorization-code-invalid "#troubleshooting-domain-transfer-failed-authorization-code-invalid")
- ["Parameters in request are not valid" error when trying to transfer a .es
  domain to Amazon Route 53](#troubleshooting-domain-transfer-failed-parameters-in-request-are-not-valid "#troubleshooting-domain-transfer-failed-parameters-in-request-are-not-valid")
- [Is the internationalized domain name you're transferring to Amazon Route 53 listed in
  punycode?](#troubleshooting-domain-transfer-failed-internationalized-domain-names "#troubleshooting-domain-transfer-failed-internationalized-domain-names")
- [Common transfer
  error messages](#troubleshooting-domain-transfer-error-messages "#troubleshooting-domain-transfer-error-messages")

## You didn't click

the link in the authorization email

When you transfer domain registration to Amazon Route 53, we're required by ICANN, the
governing body for domain registration, to get authorization for the transfer from
the registrant contact for the domain. To get authorization, we send you an email
that contains a link. You have between 5 and 15 days to click the link, depending on
the top-level domain. After that time, the link stops working.

If you don't click the link in the email in the allotted amount of time, ICANN
requires that we cancel the transfer. For information about how to resend the
authorization email to the registrant contact, see [Resending authorization and confirmation
emails](domain-click-email-link.md "domain-click-email-link.md").

## The authorization code that you got from the current registrar is not valid

If you request the transfer of a domain to Amazon Route 53 and you don't receive the
authorization email, check [the status page in
the Route 53 console](domain-transfer-to-route-53-status.md "domain-transfer-to-route-53-status.md"). If the status page shows that the transfer
authorization code that you got from your registrar is not valid, perform the
following steps:

1. Contact the current registrar for the domain and request a new
   authorization code. Confirm the following:
   - How long the new authorization code will remain active. You must
     request a domain transfer before the code expires.
   - The new authorization code is different from the code that isn't
     valid. If not, ask the current registrar to refresh the
     authorization code.

2. Submit another request to transfer the domain. For more information, see
   [Step 5: Request the
   transfer](domain-transfer-to-route-53.md#domain-transfer-to-route-53-request-transfer "domain-transfer-to-route-53.md#domain-transfer-to-route-53-request-transfer") in the
   topic [Transferring registration for a domain to
   Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").

## "Parameters in request are not valid" error when trying to transfer a .es

domain to Amazon Route 53

Amazon Route 53 returns a "Parameters in request are not valid" error when you try to
transfer a .es domain to Route 53 and the contact type of the registrant contact is
**Company**. To complete the transfer, change the contact type
of the registrant to **Person**, and re-submit.

## Is the internationalized domain name you're transferring to Amazon Route 53 listed in

punycode?

When you register a new domain name or create hosted zones and records, you can
specify letters other than a-z (for example, the ç in French), characters in
other alphabets (for example, Cyrillic or Arabic), and characters in Chinese,
Japanese, or Korean. Amazon Route 53 stores these internationalized domain names (IDNs) in
Punycode, which represents Unicode characters as ASCII strings.

If you get an error while transferring an IDNs to Route 53, use punycode to represent
it and try again. For more information, see [Formatting internationalized domain names](DomainNameFormat.md#domain-name-format-idns "DomainNameFormat.md#domain-name-format-idns").

## Common transfer

error messages

When a domain transfer fails, you'll typically receive an error message either in the
Route 53 console or via email. Here are the most common error messages and how to resolve them:

### "Transfer was rejected by the registry"

This error occurs when the domain registry blocks the transfer for one of several reasons.
The most common causes are:

- The domain doesn't meet the 60-day ICANN rule. ICANN requires that transfers be blocked
  within 60 days of initial registration or a registrant contact change.
- The domain has transfer lock enabled at your current registrar.
- The domain is in a status that prevents transfers, such as
  `clientTransferProhibited`,
  `serverTransferProhibited`,
  `pendingDelete`, `pendingTransfer`, or
  `redemptionPeriod`.

To resolve this issue, check the following with your current registrar:

- Verify that the domain is more than 60 days old from the date of registration.
  If you recently changed the registrant contact information, you might need to wait
  60 days from that change. Some registrars allow you to opt out of this restriction,
  so ask your current registrar if this option is available.
- Unlock the domain by disabling any transfer locks or domain locks.
- Check that your domain status allows transfers. You can verify the domain status
  using a WHOIS lookup or by contacting your current registrar.

### "Invalid authorization code" or "Auth code is incorrect"

This error means that the authorization code (also called an EPP code or transfer code)
that you entered is not valid. This can happen if the code has expired, was entered incorrectly,
or wasn't obtained from your current registrar.

To resolve this issue:

- Contact your current registrar to request a new authorization code. Make sure to ask
  how long the code will remain active so you can complete the transfer before it expires.
- When you receive the new code, verify that it's different from the previous code.
  If it's the same, ask your registrar to refresh or regenerate the authorization code.
- Double-check that you're entering the code exactly as provided, including any
  uppercase or lowercase letters, numbers, and special characters.

### "Transfer authorization email not received" or "Authorization timeout"

This error occurs when you don't click the authorization link in the transfer confirmation
email within the required timeframe (typically 5 days). ICANN requires this authorization
step for all domain transfers.

If you didn't receive the authorization email or missed the deadline, check the following:

- Check your spam or junk mail folder. Transfer authorization emails are sometimes
  filtered by email providers.
- Verify that your mailbox isn't full and doesn't have storage limitations that
  might prevent email delivery.
- Check if your email provider has policies that filter incoming mail from
  unknown senders.
- Confirm that you can access the registrant email account and that the email
  address is still active.

If necessary, update your contact information with your current registrar before
requesting another transfer. For information about resending the authorization email, see
[Resending authorization and confirmation
emails](domain-click-email-link.md "domain-click-email-link.md").

### "Domain is locked" or "Transfer prohibited"

This error indicates that your domain has a lock enabled that prevents transfers.
Most registrars enable domain locks by default as a security measure to prevent
unauthorized transfers.

To resolve this issue, log into your account with your current registrar and disable
the domain lock or transfer lock settings. The exact steps vary by registrar, but you'll
typically find these settings in your domain management or security settings. If you need
help finding these settings, contact your current registrar for assistance.

### "Contact information verification required"

This error occurs when you've recently changed your domain's contact information.
ICANN rules require a 60-day waiting period after contact changes before a domain
can be transferred to prevent fraudulent transfers.

To resolve this issue, you have two options:

- Wait 60 days from the date of the contact change before attempting the transfer again.
- Contact your current registrar to verify your current contact information.
  Some registrars may allow you to opt out of the 60-day restriction if you can
  verify your identity.

###### Note

If you receive an error message that isn't listed here, contact AWS Support and
include the exact error text. Our support team can help you diagnose and resolve
transfer issues specific to your situation.
