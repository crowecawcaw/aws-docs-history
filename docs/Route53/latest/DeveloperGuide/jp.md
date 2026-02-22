# .jp (Japan)

[Return to index](registrar-tld-list.md#index "registrar-tld-list.md#index")

**Lease period for registration and renewal**

One year.

**Restrictions**

Open to the public, with one restriction:

- Only individuals or companies in Japan can register a .jp
  domain name.

**Privacy protection**

Not supported.

**Domain locking to prevent unauthorized transfers**

Not supported. We recommend that you prevent unauthorized
transfers by restricting access to the [RetrieveDomainAuthCode](../APIReference/API_domains_RetrieveDomainAuthCode.md "../APIReference/API_domains_RetrieveDomainAuthCode.md") API action. (When you restrict
access to this Route 53 API, you also restrict who can generate an
authorization code using the Route 53 console, AWS SDKs, and other
programmatic methods.) For more information, see [Identity and access management in
Amazon Route 53](security-iam.md "security-iam.md").

**Internationalized domain names**

Supported for Japanese.

**Authorization code required for transfers**

Yes.

**DNSSEC**

Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

**Deadlines for renewing and restoring domains**

- Renewal is possible: Until 16 days before the expiration date
- Late renewal with Route 53 is possible: No
- Domain is deleted from Route 53: 6 days before
  expiration
- Restoration with the registry is possible: Contact [AWS Support](domain-contact-support.md "domain-contact-support.md").
- Domain is deleted from the registry: Contact [AWS Support](domain-contact-support.md "domain-contact-support.md").

###### Note

Registering non-general-purpose JP domains such as .co.jp and .or.jp is
currently not possible.
