# Release: App Runner adds support for Amazon Route 53 alias record for root domain on August 30, 2022

Your AWS App Runner service now supports using Amazon Route 53 alias record for creating root domain name.

**Release date:** August 30, 2022

## Changes

With this release, you can opt in to use an Amazon Route 53 alias record to create a root domain name. You can also use Amazon Route 53 alias records to map
custom domain names to your AWS App Runner environments without incurring an additional Amazon Route 53 charges. With this release, you have the flexibility to create
alias records for a root domain or subdomain. For example, if your domain name is `example.com`, you can create a record that routes requests
for `example.com` or `acme.example.com` to your App Runner service. For more information, see the following:

- [Managing custom domain names for an App Runner service](../dg/manage-custom-domains.md "../dg/manage-custom-domains.md") in the
  _AWS App Runner Developer Guide_.
- [Configure Amazon Route 53 alias record for your target DNS](../dg/manage-custom-domains-route53.md "../dg/manage-custom-domains-route53.md") in the
  _AWS App Runner Developer Guide_.

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Amazon Route 53 to perform three main functions in any
combination: domain registration, DNS routing, and health checking. To learn more about Amazon Route 53, see [Amazon Route 53 Developer Guide](../../../Route53/latest/DeveloperGuide.md "../../../Route53/latest/DeveloperGuide.md").
