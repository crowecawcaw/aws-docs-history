# Internetwork traffic privacy for AWS IoT SiteWise

Connections between AWS IoT SiteWise and on-premises applications, such as SiteWise Edge gateways, are secured over
Transport Layer Security (TLS) connections. For more information, see [Data encryption in transit for AWS IoT SiteWise](encryption-in-transit.md "encryption-in-transit.md").

AWS IoT SiteWise doesn't support connections between Availability Zones within an
AWS Region or connections between AWS accounts.

You can configure IAM Identity Center in only one Region at a time.
SiteWise Monitor connects to the Region that you configured for IAM Identity Center. This means that you use one Region
for IAM Identity Center access, but you can create portals in any Region.
