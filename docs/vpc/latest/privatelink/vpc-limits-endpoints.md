# AWS PrivateLink quotas

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas,
and other quotas cannot be increased. If you request a quota increase that applies per resource,
we increase the quota for all resources in the Region.

To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")
in the _Service Quotas User Guide_.

###### Request throttling

The API actions for AWS PrivateLink are part of the Amazon EC2 API. Amazon EC2 throttles its
API requests at the AWS account level. For more information, see [Request throttling](../../../ec2/latest/devguide/ec2-api-throttling.md "../../../ec2/latest/devguide/ec2-api-throttling.md") in the
_Amazon EC2 Developer Guide_. In addition, API requests are also throttled
at the organization level to help the performance of AWS PrivateLink. If you are using
AWS Organizations and you receive a `RequestLimitExceeded` error code while you are
still within your account-level API limits, see [How to identify AWS accounts that make a large number of API calls](https://repost.aws/knowledge-center/vpc-identify-accounts-api-calls-aws-organizations "https://repost.aws/knowledge-center/vpc-identify-accounts-api-calls-aws-organizations").
If you need help, contact your account team or open a technical support case using the
**VPC** service and the **VPC Endpoints** category.
Be sure to attach an image of the `RequestLimitExceeded` error code.

###### VPC endpoint quotas

Your AWS account has the following quotas related to VPC endpoints.

| Name                                                  | Default | Adjustable                                                                                                                                                                 | Comments                                                                             |
| ----------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Interface and Gateway Load Balancer endpoints per VPC | 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-29B6F2EB "https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-29B6F2EB") | This is a combined quota for interface endpoints and Gateway Load Balancer endpoints |
| Gateway VPC endpoints per Region                      | 20      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-1B52E74A "https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-1B52E74A") | You can create up to 255 gateway endpoints per VPC                                   |
| Resource VPC endpoints per VPC                        | 200     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-CA6CC422 "https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-CA6CC422") |                                                                                      |
| Service network VPC endpoints per VPC                 | 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-3B4E38D2 "https://console.aws.amazon.com/servicequotas/home/services/vpc/quotas/L-3B4E38D2") |                                                                                      |
| Characters per VPC endpoint policy                    | 20,480  | No                                                                                                                                                                         | The maximum size of a VPC endpoint policy, including white space                     |

The following considerations apply to traffic that passes through a VPC endpoint:

- By default, each VPC endpoint can support a bandwidth of up to 10 Gbps per Availability
  Zone, and automatically scales up to 100 Gbps. The maximum bandwidth for a VPC endpoint,
  when distributing the load across all Availability Zones, is the number of Availability
  Zones multiplied by 100 Gbps. If your application needs higher throughput, contact AWS
  support.
- The maximum transmission unit (MTU) of a network connection is the size, in bytes, of
  the largest permissible packet that can be passed through a VPC endpoint. The larger the
  MTU, the more data that can be passed in a single packet. A VPC endpoint supports an MTU of
  8500 bytes. Packets with a size larger than 8500 bytes that arrive at the VPC endpoint are
  dropped.
- Path MTU Discovery (PMTUD) is not supported. VPC endpoints do not generate the following
  ICMP message: `Destination Unreachable: Fragmentation needed and Don't Fragment was
Set` (Type 3, Code 4).
- VPC endpoints enforce Maximum Segment Size (MSS) clamping for all packets. For more
  information, see [RFC879](https://datatracker.ietf.org/doc/html/rfc879 "https://datatracker.ietf.org/doc/html/rfc879").
