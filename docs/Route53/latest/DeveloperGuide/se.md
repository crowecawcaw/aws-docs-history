# .se (Sweden)

[Return to index](registrar-tld-list.md#index "registrar-tld-list.md#index")

**Lease period for registration and renewal**

One to ten years.

**Restrictions**

Open to the public, with some restrictions:

- If you are located in Sweden, you must provide a valid
  Swedish ID number. The ID number format is
  `YYMMDD-NNNN`.
- If you are located outside of Sweden, you must enter a
  valid ID number such as a tax ID number.

**Additional verification requirements**

As of October 1, 2025, .se domain registrations require
additional identity verification to comply with the registry's new NIS 2.0 requirements.
When you register a .se domain, we'll contact you to request verification documents.
Your domain registration will remain pending until you provide the required documents
and verification is complete. To submit your documents, [contact AWS Support](domain-contact-support.md "domain-contact-support.md").

The .se registry also conducts periodic audits of existing domains and might request
additional verification for recently registered domains or when you
make certain changes to your domain (such as updating the domain
owner or contact information). If your domain is placed in
`serverHold` status, this means the registry requires
verification before your domain can be fully activated.

**Documents you'll need to provide:**

- **For individuals:** A
  government-issued ID document (such as an identity card or
  passport) and proof of address less than 3 months
  old.
- **For companies or
  organizations:** Registration certificate of
  the company or organization, and proof of address if
  different from the registration certificate.

**Privacy protection**

Not supported.

**Domain locking to prevent unauthorized transfers**

Not supported. We recommend that you prevent unauthorized
transfers by restricting access to the [RetrieveDomainAuthCode](../APIReference/API_domains_RetrieveDomainAuthCode.md "../APIReference/API_domains_RetrieveDomainAuthCode.md") API action. (When you restrict
access to this Route 53 API, you also restrict who can generate an
authorization code using the Route 53 console, AWS SDKs, and other
programmatic methods.) For more information, see [Identity and access management in
Amazon Route 53](auth-and-access-control.md "auth-and-access-control.md").

**Internationalized domain names**

Supported for Latin, Swedish, and Yiddish.

**Authorization code required for transfers**

Yes

**DNSSEC**

Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

**Deadlines for renewing and restoring domains**

- Renewal is possible: Until 1 day before the expiration
  date
- Late renewal with Route 53 is possible: No
- Domain is deleted from Route 53: 1 day before
  expiration
- Restoration with the registry is possible: Between 1 day
  before and 59 days after expiration
- Domain is deleted from the registry: 64 days after
  expiration
