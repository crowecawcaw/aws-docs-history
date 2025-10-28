# Register and manage domains for your website in Lightsail

Your website needs a name, such as `example.com`. With Amazon Lightsail you can
register a name for your website, known as a domain name. To access your website, users type
your domain name into their web browser.

Use the **Domains & DNS** tab in the Amazon Lightsail
console to register and manage domain names. Lightsail uses Amazon Route 53, a highly available and
scalable Domain Name System (DNS) web service, to register domains for you. After your domain is
registered, you can assign it to your Lightsail resources or manage DNS records for it. For
general information about DNS, see [DNS](understanding-dns-in-amazon-lightsail.md "understanding-dns-in-amazon-lightsail.md").

For more information about domain registration in Amazon Lightsail, continue reading.

**Contents**

- [How domain registration
  works](#how-registration-works "#how-registration-works")
- [Domains that you can register in
  Lightsail](#domains-register "#domains-register")
- [Pricing for domain
  registration](#domain-pricing "#domain-pricing")

## How domain registration works

The following overview shows how you register a domain name in Amazon Lightsail:

1. Confirm that the domain name you want is available to use on the internet. If the
   domain name you want is not available, you can try other names or change only the
   top-level domain, such as **.com**, to another top-level
   domain, such as **.org** or **.net**. For a list of the top-level domains (TLDs) that Lightsail supports,
   see [Domains that you can register in
   Amazon Lightsail](#domains-register "#domains-register").
2. Register the domain name with Lightsail. When you register a domain, you provide
   names and contact information for the domain owner and other contacts.

At the end of the registration process, we send the information that you provide to the
registrar for the domain. The domain registrar is a company that is accredited by the Internet
Corporation for Assigned Names and Numbers (ICANN) to process domain registrations for
specific TLDs. The registrar for the domain is either Amazon Registrar or our registrar
associate, Gandi.

Amazon Registrar and Gandi hide different information by default. Amazon Registrar, Inc.
hides all of your contact information, and Gandi hides all of your contact information except
organization name.

- To find out who the registrar is for your domain, see [Domains that you can register in
  Amazon Lightsail](#domains-register "#domains-register").
- The registrar sends your information to the registry for the domain. A registry is a
  company that sells domain registrations for one or more top-level domains, such as
  **.com**.
- The registry stores the information about your domain in their own database and also
  stores some of the information in the public WHOIS database.

For more information about how to register a domain name, see [Register a new domain](amazon-lightsail-register-new-domain.md "amazon-lightsail-register-new-domain.md").

After you register a domain using Lightsail, Route 53 makes itself the DNS service for your
domain by assigning a set of name servers to your domain. A name server is a server that helps
translate domain names into IP addresses. .

Lightsail automatically does the following to make itself the DNS service for the
domain:

- Creates a [Lightsail DNS
  zone](understanding-dns-in-amazon-lightsail.md "understanding-dns-in-amazon-lightsail.md") that has the same name as your domain.
- Assigns a set of four name servers to the Lightsail DNS zone.
- Replaces the domain’s Route 53 name servers with the name servers from your Lightsail
  DNS zone.

If you already registered a domain name with another registrar, you can choose to transfer
management of the domain’s DNS to Lightsail. This isn't required to use other Lightsail
features. For more information, see [Create a
DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md "lightsail-how-to-create-dns-entry.md").

## Domains that you can register in Lightsail

Lightsail uses the same generic top-level domains (TLDs) as Route 53. For a list of generic
TLDs that you can use to register domains in Lightsail, see [Domains that you can register with Amazon Route 53](../../../Route53/latest/DeveloperGuide/registrar-tld-list.md#registrar-tld-list-index-generic "../../../Route53/latest/DeveloperGuide/registrar-tld-list.md#registrar-tld-list-index-generic") in the Amazon Route 53 Developer Guide.

If the TLD isn’t included in the list, or if you would like to register a geographic
domain, we recommend you use the Route 53 console. Your geographic domain will be available in
the Lightsail console after it has been registered using Route 53. For more information, see
[Geographic top-level domains](../../../Route53/latest/DeveloperGuide/registrar-tld-list.md#registrar-tld-list-index-geographic "../../../Route53/latest/DeveloperGuide/registrar-tld-list.md#registrar-tld-list-index-geographic") in the Amazon Route 53 Developer Guide.

## Pricing for domain registration

Lightsail uses Route 53 for domain registration. Therefore, the Route 53 pricing also applies
to Lightsail registrations.

For information about the cost of registering domains, see [Domains that you can register in Amazon Route 53](../../../Route53/latest/DeveloperGuide/registrar-tld-list.md "../../../Route53/latest/DeveloperGuide/registrar-tld-list.md") in the Amazon Route 53 Developer Guide.

## Additional information about domains

The following articles can help you manage domains in Lightsail:

- [DNS](understanding-dns-in-amazon-lightsail.md "understanding-dns-in-amazon-lightsail.md")
- [Format domain names](amazon-lightsail-domain-name-format.md "amazon-lightsail-domain-name-format.md")
- [Manage a Lightsail domain in
  Amazon Route 53](amazon-lightsail-manage-domain-advanced.md "amazon-lightsail-manage-domain-advanced.md")
- [Create a DNS zone to manage your
  domain’s DNS records](lightsail-how-to-create-dns-entry.md "lightsail-how-to-create-dns-entry.md")
- [Domain registration
  renewal](amazon-lightsail-domain-manage-auto-renew.md "amazon-lightsail-domain-manage-auto-renew.md")
- [Edit or delete a DNS
  zone](amazon-lightsail-edit-or-delete-a-dns-zone.md "amazon-lightsail-edit-or-delete-a-dns-zone.md")
- [Point your domain to a
  load balancer](add-alias-record-for-lightsail-load-balancer.md "add-alias-record-for-lightsail-load-balancer.md")
- [Point your domain to a
  distribution](amazon-lightsail-point-domain-to-distribution.md "amazon-lightsail-point-domain-to-distribution.md")
- [Point your domain to an
  instance](amazon-lightsail-routing-to-instance.md "amazon-lightsail-routing-to-instance.md")
- [Route traffic for
  your domain to a container service](amazon-lightsail-point-domain-to-container-service.md "amazon-lightsail-point-domain-to-container-service.md")
