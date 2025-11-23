# Quotas for your Classic Load Balancer

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is Region-specific.

To view the quotas for your Classic Load Balancers, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS services** and
select **Elastic Load Balancing**. You can also use the [describe-account-limits](../../../cli/latest/reference/elb/describe-account-limits.md "../../../cli/latest/reference/elb/describe-account-limits.md") (AWS CLI)
command for ELB.

To request a quota increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

Your AWS account has the following quotas related to Classic Load Balancers.

| Name                                           | Default | Adjustable                                                                                                                                                                                                   |
| ---------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Classic Load Balancers per Region              | 20      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-E9E9831D "https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-E9E9831D") |
| Listeners per Classic Load Balancer            | 100     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-1A491844 "https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-1A491844") |
| Registered Instances per Classic Load Balancer | 1,000   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-CE3125E5 "https://console.aws.amazon.com/servicequotas/home/services/elasticloadbalancing/quotas/L-CE3125E5") |
