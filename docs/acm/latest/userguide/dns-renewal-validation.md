# Renewal for domains validated by

DNS

Managed renewal is fully automated for ACM certificates that were originally
issued using [DNS validation](dns-validation.md "dns-validation.md").

At 45 days prior to expiration, ACM checks for the following renewal
criteria:

- The certificate is currently in use by an AWS service.
- All required ACM-provided DNS CNAME records (one for each unique Subject
  Alternative Name) are present and accessible via public DNS.
  If these criteria are met, ACM considers the domain names validated and renews
  the certificate.

ACM sends AWS Health events and Amazon EventBridge events if it can't automatically
validate a domain during renewal. These events are sent at 30 days, 15
days, seven days, three days, and one day prior to expiration. For more information,
see [Amazon EventBridge support for ACM](supported-events.md "supported-events.md").
