# Quotas for your Gateway Load Balancers

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some
quotas, and other quotas cannot be increased.

To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
If the quota is not yet available in Service Quotas, submit a request for a [service quota increase](https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

###### Quotas

- [Load balancers](#load-balancer-quotas "#load-balancer-quotas")
- [Target groups](#target-group-quotas "#target-group-quotas")
- [Load Balancer Capacity Units](#lcu-quotas "#lcu-quotas")

## Load balancers

Your AWS account has the following quotas related to Gateway Load Balancers.

| Name                                | Default | Adjustable |
| ----------------------------------- | ------- | ---------- |
| Gateway Load Balancers per Region   | 100     | Yes        |
| Gateway Load Balancers per VPC      | 100     | Yes        |
| Gateway Load Balancer ENIs per VPC  | 300 \*  | Yes        |
| Listeners per Gateway Load Balancer | 1       | No         |

**\*** Each Gateway Load Balancer uses one network interface per zone.

## Target groups

The following quotas are for target groups.

| Name                                                    | Default | Adjustable |
| ------------------------------------------------------- | ------- | ---------- |
| GENEVE target groups per Region                         | 100     | Yes        |
| Targets per Availability Zone per GENEVE target group   | 300     | No         |
| Targets per Availability Zone per Gateway Load Balancer | 300     | No         |
| Targets per Gateway Load Balancer                       | 300     | No         |

## Load Balancer Capacity Units

The following quotas are for Load Balancer Capacity Units (LCUs).

| Name                                                           | Default | Adjustable                                                                                                                                                                                                   |
| -------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reserved Gateway Load Balancer Capacity Units (LCU) per Region | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-7A15E3C5 "https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-7A15E3C5") |
