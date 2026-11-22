

# Working with hosted zones

A hosted zone is a container for records. Records hold information about how to route traffic for a domain, such as example.com, and its subdomains (acme.example.com, zenith.example.com). A hosted zone has the same name as its domain. There are two types:
+ *Public hosted zones* contain records that specify how you want to route traffic on the internet. For more information, see [Working with public hosted zones](AboutHZWorkingWith.md).
+ *Private hosted zones* contain records that specify how you want to route traffic in an Amazon VPC. For more information, see [Working with private hosted zones](hosted-zones-private.md).

Every public and private hosted zone also has a tier, which determines the features that are available for the zone. For more information, see [Hosted zone tiers](hosted-zone-tiers.md) and [Hosted zone features](hosted-zone-features.md).