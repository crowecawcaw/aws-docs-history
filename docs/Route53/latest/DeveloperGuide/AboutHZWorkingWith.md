# Working with public hosted zones

A public hosted zone is a container that holds information about how you want to route traffic on the internet for a specific domain,
such as example.com, and its subdomains (acme.example.com, zenith.example.com). You get a public hosted zone in one of two ways:

- When you register a domain with Route 53, we create a hosted zone for you automatically.
- When you transfer DNS service for an existing domain to Route 53, you start by creating a hosted zone for the domain.
  For more information, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").
  In both cases, you then create records in the hosted zone to specify how you want to route traffic for the domain and subdomains.
  For example, you might create a record to route traffic for www.example.com to a CloudFront distribution or to a web server in your data center.
  For more information about records, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").

This topic explains how to use the Amazon Route 53 console to create, list, and delete public hosted zones.

###### Note

You can also use a Route 53 _private_ hosted zone to route traffic within one or more VPCs that you create with the
Amazon VPC service. For more information, see [Working with private hosted zones](hosted-zones-private.md "hosted-zones-private.md").

###### Topics

- [Considerations when working with public hosted zones](hosted-zone-public-considerations.md "hosted-zone-public-considerations.md")
- [Creating a public hosted zone](CreatingHostedZone.md "CreatingHostedZone.md")
- [Getting the name servers for a public hosted zone](GetInfoAboutHostedZone.md "GetInfoAboutHostedZone.md")
- [Listing public hosted zones](ListInfoOnHostedZone.md "ListInfoOnHostedZone.md")
- [Viewing DNS query metrics for a public hosted zone](hosted-zone-public-viewing-query-metrics.md "hosted-zone-public-viewing-query-metrics.md")
- [Deleting a public hosted zone](DeleteHostedZone.md "DeleteHostedZone.md")
- [Checking DNS responses from Route 53](dns-test.md "dns-test.md")
- [Configuring white-label name servers](white-label-name-servers.md "white-label-name-servers.md")
- [NS and SOA records that Amazon Route 53 creates for a public hosted zone](SOA-NSrecords.md "SOA-NSrecords.md")
