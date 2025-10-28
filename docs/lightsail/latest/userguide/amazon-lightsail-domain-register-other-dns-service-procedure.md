# Transfer DNS

management for your Lightsail domain

You can use an Amazon Lightsail DNS zone to manage the DNS records for a domain that you
registered using Lightsail. Or, if you'd like, you can transfer management of DNS records for
the domain to another DNS hosting provider. In this guide, we show you how to transfer
management of DNS records for a domain you registered with Lightsail to another DNS hosting
provider.

###### Important

Any changes you make to the DNS of your domain might require several hours to propagate
through the internet’s DNS. Because of this, you should keep the DNS records of your domain in
place at your current DNS hosting provider until the transfer of management is done. This
ensures that traffic for your domain continues to route to your resources uninterrupted while
the transfer takes place.

**Contents**

- [Complete the
  prerequisites](#other-dns-service-prerequisites "#other-dns-service-prerequisites")
- [Add records to the
  DNS zone](#other-dns-service-add-records-dns-zone "#other-dns-service-add-records-dns-zone")

## Complete the prerequisites

Complete the following prerequisites if you haven’t already done so:

1. Register a domain name. You can register a domain name using Lightsail. For more
   information, see [Register a new
   domain](amazon-lightsail-register-new-domain.md "amazon-lightsail-register-new-domain.md").
2. Use the process that’s provided by your DNS service to get the name servers for your
   domain.

## Add records to the DNS zone

Complete the following procedure to add the name servers for another DNS hosting provider
into your registered domain in Lightsail.

1. Sign in to the [Lightsail
   console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. Choose the **Domains & DNS** tab.
3. Choose the name of the domain that you want to configure to use another DNS
   service.
4. Choose **Edit Name Servers**.
5. Change the names of the name servers to the name servers that you got from your DNS
   service when you completed the prerequisites.
6. Choose **Save**.
