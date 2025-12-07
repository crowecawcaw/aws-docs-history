# Manage private hosted zone associations with Route 53 Global Resolver

## Creating private hosted zones for internal

applications

Before you can associate a private hosted zone with a DNS view, you must first create the
zone using the Amazon Route 53 console or API.

**To create a private hosted zone**

1. Open the Amazon Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose **Create hosted zone**.
4. For **Domain name**, enter the domain name for your private
   zone (for example, `internal.example.com`).
5. For **Type**, choose **Private hosted
   zone**.
6. For **VPCs to associate with the hosted zone**, choose the VPCs you want to associated with the hosted zone. Optionally, you can
   use the `CreateHostedZone` API operation to skip entering a value since you'll be associating the zone with Route 53 Global Resolver instead.
7. Choose **Create hosted zone**.

After creating the private hosted zone, add the DNS records you need for your internal
services.

## Associating private hosted zones with DNS

views

To enable Route 53 Global Resolver to resolve queries for your private hosted zone, you must associate the
zone with one or more DNS views.

**To associate a private hosted zone with a DNS view**

1. In the Route 53 Global Resolver console, navigate to your global resolver.
2. Choose the DNS view where you want to associate the private hosted zone.
3. In the **Private hosted zones** section, choose **Associate hosted zone**.
4. For **Hosted zone**, select the private hosted zone you want
   to associate.
5. For **Association name**, enter a descriptive name for this
   association.
6. Choose **Associate hosted zone**.

The association process typically takes a few minutes to complete. Once complete, Route 53 Global Resolver
will use the records in the private hosted zone to answer DNS queries from client devices
associated with the DNS view.
