# EUCPERF02-BP03 Evaluate external data sources that your environment integrates with, and

assess its impact on performance

The location of user data and the services used to deliver access to this data are key
to providing the best performance for consumers of an AWS EUC deployment. Latency incurred
while accessing data sources may incur additional delays and contribute to end user
frustration and lack of engagement, as well as increased support calls.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Define a data architecture that describes how data is managed, from collection
through transformation, distribution, and consumption. This informs the EUC architects
where to place key application and desktop delivery services and where optimization may be
required to avoid performance degradation.

If migrating from an existing on-premises EUC architecture, you may need to deploy
[AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/") or [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/ "https://aws.amazon.com/vpn/site-to-site-vpn/") connections to provide
access between AWS and your on-premises infrastructure. For best practices related to
networking for Amazon WorkSpaces and descriptions for how and when to use Direct Connect and VPN
connections, see [Best Practices for VPCs and Networking in Amazon WorkSpaces Deployments](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf "https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf").

Be sure to architect network solutions with low enough latency and sufficient
bandwidth to support appropriate data access between desktops, applications, and any
on-premises data sources.

If your AWS EUC solution integrates with services offered by other cloud providers,
such as email, collaboration tools, or SaaS applications, be sure to size internet
connections or private networks accordingly to avoid high latency and bandwidth
constraints.
