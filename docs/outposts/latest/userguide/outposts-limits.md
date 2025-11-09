# Quotas for AWS Outposts

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some
quotas, but not for all quotas.

To view the quotas for AWS Outposts, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose
**AWS services**, and select **AWS Outposts**.

To request a quota increase, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

Your AWS account has the following quotas related to AWS Outposts.

| Resource          | Default | Adjustable                                                                                                                                                                           | Comments                                                                                                                                                                                              |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Outpost sites     | 100     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/outposts/quotas/L-3D389D34 "https://console.aws.amazon.com/servicequotas/home/services/outposts/quotas/L-3D389D34") | An Outpost site is the customer managed physical building where you<br>power and attach your Outpost equipment to the network.<br>You can have 100 Outposts sites in each Region of your AWS account. |
| Outposts per site | 10      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/outposts/quotas/L-0B277C74 "https://console.aws.amazon.com/servicequotas/home/services/outposts/quotas/L-0B277C74") | AWS Outposts includes hardware and virtual resources, known as Outposts. This<br>quota limits your Outpost virtual resources.<br>You can have 10 Outposts in each Outpost site.                       |

## AWS Outposts and the quotas for other services

AWS Outposts relies on the resources of other services and those services may have their own
default quotas. For example, your quota for local network interfaces comes from the
Amazon VPC quota for network interfaces.
