# Troubleshoot email validation problems

Consult the following guidance if you are having trouble validating a certificate domain
with email.

###### Topics

- [Not receiving validation email](#troubleshooting-no-mail "#troubleshooting-no-mail")
- [Persistent initial timestamp for email validation](#initial-dates "#initial-dates")
- [I can't switch to DNS validation](#troubleshoot-switch-to-dns "#troubleshoot-switch-to-dns")

## Not receiving validation email

When you request a certificate from ACM and choose email validation, domain
validation email is sent to the five common administrative addresses. For more
information, see [AWS Certificate Manager email validation](email-validation.md "email-validation.md"). If
you are experiencing problems receiving validation email, review the suggestions that
follow.

**Where to look for email**

ACM sends validation email messages to your requested domain name. You can
also specify a superdomain as a validation domain if you wish to receive these
emails at that domain instead. Any subdomain up to the minimal website address is
valid, and is used as the domain for the email address as the suffix after @. For
example, you can receive an email to admin@example.com if you specify example.com as
the validation domain for subdomain.example.com. Review the list of email addresses
that are displayed in the ACM console (or returned from the CLI or API) to
determine where you should be looking for validation email. To see the list, click
the icon next to the domain name in the box labeled **Validation not
complete**.

**The email is marked as spam**

Check your spam folder for the validation email.

**GMail automatically sorts your email**

If you are using GMail, the validation email may have been automatically sorted
into the **Updates** or **Promotions**
tabs.

**Contact the Support Center**

If, after reviewing the preceding guidance, you still don't receive the domain
validation email, please visit the [Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") and create a case. If you don't have a support agreement,
post a message to the [ACM
Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=206 "https://forums.aws.amazon.com/forum.jspa?forumID=206").

## Persistent initial timestamp for email validation

The timestamp of a certificate's first email-validation request persists through later
requests for validation renewal. This is not evidence of an error in ACM
operations.

## I can't switch to DNS validation

After you create a certificate with email validation, you cannot switch to validating it with DNS. To use DNS validation, delete the certificate and then create a new one that uses DNS validation.
