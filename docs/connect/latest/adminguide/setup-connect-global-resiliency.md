# Set up Amazon Connect Global Resiliency

###### Note

**New user?** Check out the [Amazon Connect Global Resiliency
Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US "https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US"). This online course guides you through the process of onboarding and testing phone number
and agent failover using new APIs through the AWS CLI.

Global Resiliency is available only for Amazon Connect instances created in the following AWS Regions: US East (N. Virginia),
US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).

- You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around.
- You can only create a replica in the Europe (Frankfurt) Region if your source
  is Europe (London), or the other way around.
- You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
  To obtain access to this feature, contact your Amazon Connect Solutions Architect or Technical Account Manager.

Amazon Connect Global Resiliency enables you to provide customer service anywhere in the world with
the highest reliability, performance, and efficiency. With its distributed telephony
features, your contact center can meet international regulatory requirements.

Amazon Connect Global Resiliency provides a set of APIs that you use to:

- Provision a linked Amazon Connect instance in another AWS Region.
- Provision and manage phone numbers that are global and accessible in both
  Regions.
- Distribute telephony traffic and agents across Amazon Connect instances and Regions in 10%
  increments, or shift them all at once. This enables you to slowly shift inbound
  voice contacts and agents across Regions or shift them all at the same time.

For example, you can distribute inbound voice contacts and agents 100% in US East
(N. Virginia) and 0% in US West (Oregon), or 50% in each Region.

- Access reserved capacity across Regions.

###### Contents

- [Global Resiliency
  requirements](connect-global-resiliency-requirements.md "connect-global-resiliency-requirements.md")
- [Get
  started](get-started-connect-global-resiliency.md "get-started-connect-global-resiliency.md")
- [Manage
  traffic distribution groups](manage-traffic-distribution-groups.md "manage-traffic-distribution-groups.md")
- [Manage phone numbers
  across Regions](manage-phone-numbers-across-regions.md "manage-phone-numbers-across-regions.md")
- [Manage chat across
  Regions](manage-chat-across-regions.md "manage-chat-across-regions.md")
