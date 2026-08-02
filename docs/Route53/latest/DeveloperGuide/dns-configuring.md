# Configuring Amazon Route 53 as your DNS service

You can use Amazon Route 53 as the DNS service for your domain, such as example.com. Route 53 routes internet traffic
to your website by translating domain names like www.example.com into IP addresses like 192.0.2.1. Computers use these IP addresses to connect to each other. When someone types your domain name in a browser or sends you an email, a DNS query goes to Route 53. It responds with the right value, such as the IP address for your web server.

###### DNS hosting vs. domain registration

This chapter covers using Route 53 for _DNS hosting only_. Your domain stays registered with your current registrar. You keep paying them for renewals. Route 53 only handles your DNS settings and DNS queries.

If you want to transfer your domain to Route 53 as well (making Route 53 both your
registrar and DNS service), see [Pre-transfer checklist for domain transfers](domain-transfer-checklist.md "domain-transfer-checklist.md") and [Transferring registration for a domain to Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").

This chapter explains how to set up Route 53 to route internet traffic to the right places. It also covers how to
move DNS service to Route 53 from another provider, and how to use Route 53 as the DNS service for a new domain.

###### Topics

- [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md")
- [Configuring DNS routing for a new domain](dns-configuring-new-domain.md "dns-configuring-new-domain.md")
- [Routing traffic to your resources](dns-routing-traffic-to-resources.md "dns-routing-traffic-to-resources.md")
- [Working with hosted zones](hosted-zones-working-with.md "hosted-zones-working-with.md")
- [Working with records](rrsets-working-with.md "rrsets-working-with.md")
- [Configuring DNSSEC signing in Amazon Route 53](dns-configuring-dnssec.md "dns-configuring-dnssec.md")
- [Using AWS Cloud Map to create records and health checks](autonaming.md "autonaming.md")
- [DNS constraints and behaviors](DNSBehavior.md "DNSBehavior.md")
- [Related topics](dns-configuring-related-topics.md "dns-configuring-related-topics.md")
