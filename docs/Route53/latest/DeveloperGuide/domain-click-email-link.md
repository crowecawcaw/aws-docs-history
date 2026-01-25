# Resending authorization and confirmation

emails

For several operations related to domain registration, ICANN requires that we get
authorization from the registrant contact for the domain or confirmation that the email
address for the registrant contact is valid. To get authorization or confirmation, we send
an email that contains a link. You have between 3 and 15 days to click the link, depending
on the operation and the top-level domain. After that time, the link stops working.

If you don't click the link in the email in the allotted amount of time, ICANN generally
requires that we suspend the domain or cancel the operation, depending on what you were
trying to do:

**Register a domain**

We suspend the domain, so that it's not accessible on the internet. To resend
the confirmation email, see [To resend the confirmation
email for a domain registration](#domain-click-email-link-register-procedure "#domain-click-email-link-register-procedure").

**Geographic TLDs only – Transfer a domain to Amazon Route 53**

If you're transferring a domain that has a [geographic TLD](registrar-tld-list.md#registrar-tld-list-geographic "registrar-tld-list.md#registrar-tld-list-geographic"), we cancel the transfer. To resend the authorization
email, see [To resend the authorization
email for a domain transfer](#domain-click-email-link-transfer-procedure "#domain-click-email-link-transfer-procedure").

###### Note

Authorization isn't required for domains that have a [generic TLD](registrar-tld-list.md#registrar-tld-list-generic "registrar-tld-list.md#registrar-tld-list-generic"), such as .com, .net, or .org.

**Change the name or email address of the registrant contact for the domain (the
owner)**

We cancel the change. To resend the authorization email, see [To resend the authorization
email to update the registrant contact or delete a domain](#domain-click-email-link-update-procedure "#domain-click-email-link-update-procedure").

**Delete a domain**

We cancel the deletion request. To resend the authorization email, see [To resend the authorization
email to update the registrant contact or delete a domain](#domain-click-email-link-update-procedure "#domain-click-email-link-update-procedure").

**Geographic TLDs only – Transfer a domain from Route 53 to another
registrar**

If you're transferring a domain that has a [geographic TLD](registrar-tld-list.md#registrar-tld-list-geographic "registrar-tld-list.md#registrar-tld-list-geographic"), the new registrar cancels the transfer.

###### Note

Authorization isn't required for domains that have a [generic TLD](registrar-tld-list.md#registrar-tld-list-generic "registrar-tld-list.md#registrar-tld-list-generic"), such as .com, .net, or .org.

###### Topics

- [Updating your email
  address](#domain-click-email-link-update-address "#domain-click-email-link-update-address")
- [Resending emails](#domain-click-email-link-resend-email "#domain-click-email-link-resend-email")

## Updating your email

address

We always send confirmation and authorization emails to the email address for the
registrant contact for a domain. For some TLDs, we're required to send email to the old
and new email addresses for the registrant contact in the following cases:

- You're changing the email address for a domain that is already registered with
  Amazon Route 53
- You're changing the email address for a domain that you're transferring to
  Route 53

## Resending emails

Use the applicable procedure to resend confirmation or authorization emails.

- [To resend the confirmation
  email for a domain registration](#domain-click-email-link-register-procedure "#domain-click-email-link-register-procedure")
- [To resend the authorization
  email for a domain transfer](#domain-click-email-link-transfer-procedure "#domain-click-email-link-transfer-procedure")
- [To resend the authorization
  email to update the registrant contact or delete a domain](#domain-click-email-link-update-procedure "#domain-click-email-link-update-procedure")

###### To resend the confirmation

email for a domain registration

1. Check the email address for the registrant contact and, if necessary, update
   it. For more information, see [Updating contact information and ownership for
   a domain](domain-update-contacts.md "domain-update-contacts.md").
2. Check the spam folder in your email application for an email from one of the
   following email addresses.

If too much time has passed, the link won't work any longer, but you'll know
where to look for the confirmation email when we send you another one.

| TLDs       | Email address that the approval or confirmation email comes<br>from                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| .fr        | nic@nic.fr                                                                                                                                      |
| All others | One of the following email addresses:<br>• noreply@registrar.amazon<br>• noreply@domainnameverification.net<br>• noreply@emailverification.info |

###### Note

The emails might contain a link to www.verify-whois.com. This link is safe
to use. 3. Use the Amazon Route 53 console to resend the confirmation email:

    1. Sign in to the AWS Management Console and open the Route 53 console at
     [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
    2. In the navigation pane, choose **Registered
     domains**.
    3. Choose the name of the domain that you want to resend the email
     for.
    4. In the warning box with the heading "Your domain might be suspended,"
     choose **Send email again**.


    ###### Note

    If there's no warning box, you already confirmed that the email
     address for the registrant contact is valid.

4. If you encounter issues while resending the confirmation email, you can
   contact AWS Support for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

###### To resend the authorization

email for a domain transfer

This method doesn't work for .jp domain transfer out requests.

1. Use the method provided by the current domain registrar to confirm that
   privacy protection for the domain is disabled. If not, disable it.

We send the authorization email to the email address that the current
registrar saved in the WHOIS database. When privacy protection is enabled, that
email address typically is obfuscated. The current registrar might not forward
to your actual email address the email that Amazon Route 53 sends to the email address
in the WHOIS database.

###### Note

If the current registrar for the domain won't let you turn off privacy
protection, we can still transfer the domain if you specified a valid
authorization code in [Step 5: Request the
transfer](domain-transfer-to-route-53.md#domain-transfer-to-route-53-request-transfer "domain-transfer-to-route-53.md#domain-transfer-to-route-53-request-transfer"). 2. Check the email address for the registrant contact and, if necessary, update
it. Use the method provided by the current registrar for the domain. 3. Check the spam folder in your email application for an email from one of the
following email addresses.

If too much time has passed, the link won't work any longer, but you'll know
where to look for the authorization email when we send you another one.

| TLDs                | Email address that the approval or confirmation email comes<br>from                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| .com.au and .net.au | no-reply@ispapi.net<br>The email contains a link to<br>https://approve.domainadmin.com.                                                         |
| .fr                 | nic@nic.fr                                                                                                                                      |
| All others          | One of the following email addresses:<br>• noreply@registrar.amazon<br>• noreply@domainnameverification.net<br>• noreply@emailverification.info |

###### Note

The emails might contain a link to www.verify-whois.com. This link is safe
to use. 4. If the transfer is no longer in process (if we already canceled it because too
much time has passed), request the transfer again, and we'll send you another
authorization email.

###### Note

For the first 15 days after you request a transfer, you can determine the
status of the transfer by checking the **Notifications**
table on the **Dashboard** page in the Route 53 console. After
15 days, use the AWS CLI to get the status. For more information, see [route53domains](../../../cli/latest/reference/route53domains/index.md "../../../cli/latest/reference/route53domains/index.md") in
the _AWS CLI Command Reference_.

If the transfer is still in progress, perform the following steps to resend
the authorization email.

    1. Sign in to the AWS Management Console and open the Route 53 console at
     [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
    2. In the **Notifications** table, find the domain that
     you want to transfer.
    3. In the **Status** column for that domain, choose
     **Resend email**.

5. If you encounter issues while resending the authorization email for a domain
   transfer, you can contact AWS Support for free. For more information, see
   [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

###### To resend the authorization

email to update the registrant contact or delete a domain

1. Check the email address for the registrant contact and, if necessary, update
   it. For more information, see [Updating contact information and ownership for
   a domain](domain-update-contacts.md "domain-update-contacts.md").
2. Check the spam folder in your email application for an email from one of the
   following email addresses.

If too much time has passed, the link won't work any longer, but you'll know
where to look for the authorization email when we send you another one.

| TLDs       | Email address that the authorization email comes from                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| .fr        | nic@nic.fr                                                                                                                                      |
| All others | One of the following email addresses:<br>• noreply@registrar.amazon<br>• noreply@domainnameverification.net<br>• noreply@emailverification.info |

###### Note

The emails might contain a link to www.verify-whois.com. This link is safe
to use. 3. Cancel the change or deletion. You have two options:

    * You can wait for the 3 to 15 day waiting period to pass, after which
     we automatically cancel the requested operation.
    * Alternatively, you can contact AWS Support and ask them to cancel
     the operation.

###### Important

**Transfer types and cancellation methods:**
The cancellation method depends on the type of transfer:

    * **External registrar to Route 53:**
     Follow the procedures in this topic (wait for auto-cancellation or
     contact AWS Support)
    * **Between AWS accounts:** Use the
     `CancelDomainTransferToAnotherAwsAccount` API or
     contact AWS SupportDon't contact your current external registrar to cancel a transfer to

Route 53, as they can't cancel transfers that are already in progress with
AWS. 4. After the change or deletion is canceled, you can change the contact
information or delete the domain again, and we'll send you another authorization
email. 5. If you encounter issues while resending the authorization email, you can
contact AWS Support for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").
