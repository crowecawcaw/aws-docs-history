# .nz (New Zealand)

[Return to index](registrar-tld-list.md#index "registrar-tld-list.md#index")

**Lease period for registration and renewal**

One to ten years.

**Restrictions**

Open to the public, with some restrictions:

- Individuals must be at least 18.
- Organizations must be registered.

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

Supported.

**Authorization code required for transfers**

Yes

**DNSSEC**

Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

**Deadlines for renewing and restoring domains**

- Renewal is possible: Until the expiration date
- Late renewal with Route 53 is possible: Until 44 days after
  expiration
- Domain is deleted from Route 53: 44 days after
  expiration
- Restoration with the registry is possible: Between 44 days
  and 134 days after expiration
- Domain is deleted from the registry: 134 days after
  expiration
