# .eu (European Union)

[Return to index](registrar-tld-list.md#index "registrar-tld-list.md#index")

**Lease period for registration and renewal**

One to ten years.

**Restrictions**

Open to the public, with one restriction:

- You must provide a valid postal address from one of the 30
  states of the European Economic Area (EEA) or if you’re a
  citizen of one of the 27 member-states of the European Union
  (EU), you must specify your EU country of
  citizenship.

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

You can also generate the auth code by using the "My.eu" panel at the registry: [https://my.eurid.eu/](https://my.eurid.eu/ "https://my.eurid.eu/").

**DNSSEC**

Supported for domain registration. For more information, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

**Deadlines for renewing and restoring domains**

- Renewal is possible: Until the expiration date
- Late renewal with Route 53 is possible: No
- Domain is deleted from Route 53: On the expiration
  date
- Restoration with the registry is possible: Until 40 days
  after expiration
- Domain is deleted from the registry: 40 days after
  expiration

**WHOIS Search**

For information about existing .eu domains, see [https://whois.eurid.eu/en/](https://whois.eurid.eu/en/ "https://whois.eurid.eu/en/").
