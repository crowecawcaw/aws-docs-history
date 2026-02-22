# Renewal for domains validated by

HTTP

ACM provides automated managed renewal for certificates that were originally
issued using HTTP validation through CloudFront.

At 45 days prior to expiration, ACM checks for the following renewal
criteria:

- The certificate is currently in use by CloudFront.
- All required HTTP validation records are accessible and contain the
  expected content.
  If these criteria are met, ACM considers the domain names validated and renews
  the certificate.

ACM sends AWS Health events and Amazon EventBridge events if it can't automatically
validate a domain during renewal. These events are sent at 30 days, 15
days, seven days, three days, and one day prior to expiration. For more information,
see [Amazon EventBridge support for ACM](supported-events.md "supported-events.md").

To ensure successful renewal, make sure that the content at the
`RedirectFrom` location matches the content at the
`RedirectTo` location for each domain in the certificate.
