# VPC peering connection quotas for an account

VPC peering allows you to connect two VPCs. This enables resources in one VPC to
communicate with resources in the other VPC as if they were in the same network. VPC peering
is a useful feature for connecting your VPCs, whether they are in the same AWS Region or
different Regions. This section describes the quotas you should be aware of when working
with VPC peering connections.

The following table lists the quotas, formerly referred to as limits, for VPC peering
connections for your AWS account. Unless indicated otherwise, you can request an increase
for these quotas.

If you find that your current VPC peering connection requirements exceed the
default quotas, we encourage you to submit a service limit increase request. We will review
your use case and work with you to adjust the quotas accordingly, ensuring your VPC
environment can support your growing business needs.

| Name                                                         | Default            | Adjustable                                                                                                                                                                             |
| ------------------------------------------------------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active VPC peering connections per VPC                       | 50                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-7E9ECCDB "https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-7E9ECCDB") (up to 125) |
| Outstanding VPC peering connection requests                  | 25                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-DC9F7029 "https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-DC9F7029")             |
| Expiry time for an unaccepted VPC peering connection request | 1 week (168 hours) | No                                                                                                                                                                                     | For more information about the rules for using VPC peering connections, see [VPC peering limitations](vpc-peering-basics.md#vpc-peering-limitations "vpc-peering-basics.md#vpc-peering-limitations"). For additional information about quotas for Amazon VPC, see [Amazon VPC quotas](../userguide/amazon-vpc-limits.md "../userguide/amazon-vpc-limits.md") in the _Amazon VPC User Guide_. |
