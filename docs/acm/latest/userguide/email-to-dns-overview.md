# How migration works

When you initiate migration, ACM generates one CNAME record for each domain on
the certificate. You have up to 72 hours to add these records to your DNS configuration.
After ACM verifies the records, the certificate switches from email validation to
DNS validation. The certificate ARN remains the same.

- **Certificate ARN** — The ARN is preserved.
  You don't need to update any references to the certificate.
- **Certificate validity** — In most cases,
  the existing expiration date is preserved. If the certificate is within
  the renewal window, ACM also renews the certificate during migration
  and extends the expiration date.
- **Auto-renewal** — After migration, the
  certificate behaves like any other DNS-validated ACM certificate.
  As long as DNS validation records remain in place, ACM
  automatically renews the certificate before expiration without requiring
  you to approve validation emails.

###### Important

You can only migrate from email to DNS validation. Migration from DNS to
email validation is not supported.

You can initiate a migration through the ACM console or by calling the [UpdateCertificateOptions](../APIReference/API_UpdateCertificateOptions.md "../APIReference/API_UpdateCertificateOptions.md") API operation with the
`ValidationMethod` option set to `DNS`. For step-by-step
instructions, see [Migrating a certificate (console or AWS CLI)](email-to-dns-migrate.md "email-to-dns-migrate.md").

## Monitor migration

To monitor migration progress, use the certificate details page in the ACM
console or call the [ListCertificateDomainValidations](../APIReference/API_ListCertificateDomainValidations.md "../APIReference/API_ListCertificateDomainValidations.md") API operation. The response
returns a domain validation summary for each domain on the certificate.
The summary includes the following fields:

- **ActiveValidationConfiguration**—Shows the validation
  method currently in effect. While migration is in progress, the active
  method is `EMAIL`.
- **RequestedValidationConfiguration**—Shows the validation
  configuration that ACM is attempting to switch to
  (`DNS`), including the CNAME record you must add and the
  current validation status (`PENDING_VALIDATION` until
  verified).

Migration is complete when ACM completes DNS validation for every domain
in the certificate. For a Java code example, see [Listing domain validation status](sdk-listdomainvalidations.md "sdk-listdomainvalidations.md").

If ACM doesn't verify the CNAME records within 72 hours, the migration
request expires and the certificate remains email-validated. You can
reinitiate migration at any time, which starts a new 72-hour window. If your
migration timed out and you can't determine why, see [My email-to-DNS migration timed out](troubleshooting-email-validation.md#troubleshoot-migration-timeout "troubleshooting-email-validation.md#troubleshoot-migration-timeout").

## Migration eligibility

You can migrate a certificate when all of the following conditions are
true:

- The certificate is a public certificate issued by ACM.
- The certificate currently uses email validation.

###### Note

To find your email-validated certificates, use certificate search
to filter by validation method. For more information, see [certificate search](gs-acm-list.md "gs-acm-list.md").

- The certificate status is **Issued**.
- The certificate does not have another migration request already in
  progress.

You cannot migrate the following certificates:

- Private certificates issued by AWS Private Certificate Authority.
- Certificates that already use DNS validation.
- Imported certificates.
- Certificates with a status other than **Issued**.
