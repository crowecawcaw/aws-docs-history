# Set up Connect Customer Global Resiliency

###### Note

**New user?** Check out the [Connect Customer Global Resiliency
Workshop](https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US "https://catalog.workshops.aws/amazon-connect-global-resiliency/en-US"). This online course guides you through the process of onboarding and testing phone number
and agent failover using new APIs through the AWS CLI.

Global Resiliency is available only for Connect Customer instances created in the following AWS Regions: US East (N. Virginia),
US West (Oregon), Asia Pacific (Osaka), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (London).

- You can only create a replica in the US East (N. Virginia) Region if your source is US West (Oregon), or the other way around.
- You can only create a replica in the Europe (Frankfurt) Region if your source
  is Europe (London), or the other way around.
- You can only create a replica in Asia Pacific (Osaka) Region if your source is Asia Pacific (Tokyo).
  To obtain access to this feature, contact your Connect Customer Solutions Architect or Technical Account Manager.

###### Important

Connect Customer Global Resiliency (ACGR) is the only AWS-supported solution for multi-region
resiliency in Connect Customer. AWS does not support third-party or custom-built alternatives for
achieving global resiliency. Deploying unsupported solutions might result in denied or
reduced service limits on the secondary instance and could impact SLA coverage if
downtime is attributed to the unsupported deployment.

Connect Customer Global Resiliency enables you to provide customer service anywhere in the world with
the highest reliability, performance, and efficiency. With its distributed telephony
features, your contact center can meet international regulatory requirements.

Connect Customer Global Resiliency provides a set of APIs that you use to:

- Provision a linked Connect Customer instance in another AWS Region.
- Provision and manage phone numbers that are global and accessible in both
  Regions.
- Distribute telephony traffic and agents across Connect Customer instances and Regions in 10%
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
- [Metrics, Reports
  and Search across ACGR Regions](metrics-reports-and-search-across-acgr-regions.md "metrics-reports-and-search-across-acgr-regions.md")
