# Quotas for Route 53 Global Resolver

Your AWS account has default quotas, formerly referred to as limits, for
each AWS service. Unless otherwise noted, each quota is Region-specific. You
can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for Route 53 Global Resolver, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose **AWS
services** and select **Route 53 Global Resolver**.

To request a quota increase, see [Requesting a Quota
Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. If the quota is not yet
available in Service Quotas, use the [limit increase
form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

Your AWS account has the following quotas related to Route 53 Global Resolver.

## Soft quotas

The following table describes quotas in Route 53 Global Resolver that can be increased. For
information about changing quotas, see [Requesting a Quota
Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

For some customers, your account quota might be below these published quotas. If you
believe that you encountered a _Resource limit exceeded_ error
wrongfully, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home")
to request quota increases.

| Resource                                     | Default quota | Adjustable |
| -------------------------------------------- | ------------- | ---------- |
| Global resolvers per account                 | 2             | Yes        |
| DNS views per global resolver                | 5             | Yes        |
| DNS views per account                        | 50            | Yes        |
| Domain lists per account                     | 1,000         | Yes        |
| Domains per domain list                      | 100,000       | Yes        |
| Domains in a file imported from S3           | 10,000        | Yes        |
| Number of domains across all Firewall Rules  | 1,000,000     | Yes        |
| Firewall rules per DNS view                  | 100           | Yes        |
| Access tokens per global resolver            | 5,000         | Yes        |
| Access Sources per global resolver           | 1,000         | Yes        |
| Access Sources CIDR size per global resolver | 65,000        | No         |
| Private hosted zones per DNS view            | 1,000         | Yes        |

## Hard quotas

The following table describes quotas in Route 53 Global Resolver that can't be increased.

| Resource or operation                                                          | Quota |
| ------------------------------------------------------------------------------ | ----- |
| Log delivery configurations per (global resolver, destination type,<br>Region) | 1     |
