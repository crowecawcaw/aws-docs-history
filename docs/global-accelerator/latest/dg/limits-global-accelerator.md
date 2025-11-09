# Quotas for AWS Global Accelerator

Your AWS account has specific quotas, also known as limits, related to AWS Global Accelerator.

The Service Quotas console provides information about Global Accelerator quotas. Along with viewing the
default quotas, you can use the Service Quotas console to [request quota increases](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas") for adjustable quotas.

You must be in the US East (N. Virginia) (us-east-1) Region to manage service limits and request
quota increases for Global Accelerator in the Service Quotas console. Global Accelerator service quotas are managed in the US East (N. Virginia)
Region because that's where
AWS Global Service quotas are defined. In any other AWS Region, you won't see Global Accelerator quotas and can't
change the quotas. Note, however, that all Global Accelerator API operations must be run in the US West (Oregon) (us-west-2)
Region.

###### Topics

- [General quotas](#limits-global-accelerator-general "#limits-global-accelerator-general")
- [Quotas for endpoints per endpoint group](#limits-global-accelerator-endpoints "#limits-global-accelerator-endpoints")
- [Related quotas](#limits-global-accelerator-additional "#limits-global-accelerator-additional")

## General quotas

The following are overall quotas for Global Accelerator.

| Entity                                                                                     | Quota                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard accelerators per AWS account                                                      | 20<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas").                                                                                                                                                          |
| Custom routing accelerators per AWS account                                                | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas").                                                                                                                                                          |
| Listeners per accelerator                                                                  | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas").                                                                                                                                                          |
| Endpoint groups per accelerator, across all listeners                                      | 42                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AWS Regions that Global Accelerator can point to, across all listeners and endpoint groups | 42<br>If your accelerator has one listener, you can point to all Global Accelerator supported Regions with your accelerator's endpoint group configuration.<br>Note that the maximum number of Regions that you can reference in an accelerator using endpoint groups decreases proportionally as<br>you increase the number of listeners. Your (total # of listeners) x (# of endpoint groups) must not exceed 42. |
| Port ranges per listener                                                                   | 10                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Port overrides per endpoint group                                                          | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas").                                                                                                                                                          |
| Principals per cross-account attachment                                                    | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas").                                                                                                                                                          |
| Resources per cross-account attachment                                                     | 500                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Quotas for endpoints per endpoint group

The following are Global Accelerator quotas that apply to the number of endpoints in endpoint groups.

| Entity                                                         | Description                                                                                                    | Quota                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint groups with more than one endpoint type               | Number of endpoints in an endpoint group containing more than one endpoint type.                               | 10                                                                                                                                                                                                                                                         |
| Endpoint groups with just Application Load Balancers           | Number of Application Load Balancers in an endpoint group containing only Application Load Balancer endpoints. | 10                                                                                                                                                                                                                                                         |
| Endpoint groups with just Network Load Balancers               | Number of Network Load Balancers in an endpoint group containing only Network Load Balancer endpoints.         | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas"). |
| Endpoint groups with just Amazon EC2 instances                 | Number of EC2 instances in an endpoint group containing only EC2 instance endpoints.                           | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas"). |
| Endpoint groups with just Elastic IP addresses                 | Number of Elastic IP addresses in an endpoint group containing only Elastic IP address endpoints.              | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas"). |
| Endpoint groups with just Amazon Virtual Private Cloud subnets | Number of Amazon VPC subnets in an endpoint group containing only subnet endpoints.                            | 10<br>You can [request a quota increase](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/globalaccelerator/quotas"). |

## Related quotas

In addition to quotas in Global Accelerator, there are quotas that apply to the resources that
you use as endpoints for an accelerator. For more information, see the following:

- [Elastic IP address quotas](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-limit "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-limit") in the
  _Amazon EC2 User Guide_.
- [Amazon EC2 service quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md") in the
  _Amazon EC2 User Guide_.
- [Quotas for your Network Load Balancers](../../../elasticloadbalancing/latest/network/load-balancer-limits.md "../../../elasticloadbalancing/latest/network/load-balancer-limits.md") in the
  _User Guide for Network Load Balancers_.
- [Quotas for your Application Load Balancers](../../../elasticloadbalancing/latest/application/load-balancer-limits.md "../../../elasticloadbalancing/latest/application/load-balancer-limits.md") in the
  _User Guide for Application Load Balancers_.
- [Amazon VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md") in the
  _Amazon VPC User Guide_.
