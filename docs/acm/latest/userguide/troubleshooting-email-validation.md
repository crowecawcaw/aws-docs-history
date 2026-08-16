# Troubleshoot email validation problems

Consult the following guidance if you are having trouble validating a certificate domain
with email.

###### Topics

- [Not receiving validation email](#troubleshooting-no-mail "#troubleshooting-no-mail")
- [Persistent initial timestamp for email validation](#initial-dates "#initial-dates")
- [Switching to DNS validation](#troubleshoot-switch-to-dns "#troubleshoot-switch-to-dns")
- [My email-to-DNS migration timed out](#troubleshoot-migration-timeout "#troubleshoot-migration-timeout")

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

## Switching to DNS validation

You can migrate an existing email-validated public certificate to DNS validation while preserving the certificate ARN. For more information, see [Migrating from email to DNS validation](email-to-dns-migration.md "email-to-dns-migration.md").

## My email-to-DNS migration timed out

If you initiate an email-to-DNS migration, you must add the CNAME records to your
DNS configuration within 72 hours. If you don't, the migration request expires. The
certificate remains email-validated and continues to work normally.

To resolve a timed-out migration:

1. Make sure the CNAME records returned by `ListCertificateDomainValidations`
   are correctly configured at your DNS provider. Use a tool such as **dig**
   or **nslookup** to confirm that the records resolve as expected.
2. Reinitiate the migration by calling `UpdateCertificateOptions` again,
   or by repeating the procedure in the ACM console. A new 72-hour window
   begins.
3. Monitor progress with `ListCertificateDomainValidations`. Migration
   completes when the active validation configuration for each domain shows
   `DNS`.

For more information, see [Migrating from email to DNS validation](email-to-dns-migration.md "email-to-dns-migration.md").
