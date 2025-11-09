**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS Firewall Manager quotas

AWS Firewall Manager is subject to the following quotas (formerly referred to as limits).

AWS Firewall Manager has default quotas that you might be able to increase and fixed quotas.

The security group policies and network ACL policies that are managed by Firewall Manager are subject to standard Amazon VPC quotas. For
more information, see [Amazon VPC
Quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md") in the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

Each Firewall Manager Network Firewall policy creates a Network Firewall firewall with an associated
firewall policy and its rule groups. These Network Firewall resources are subject to the
quotas listed at [AWS Network Firewall
quotas](../../../network-firewall/latest/developerguide/quotas.md "../../../network-firewall/latest/developerguide/quotas.md") in the _Network Firewall Developer Guide_.

## Soft quotas

AWS Firewall Manager has default quotas on the number of entities per Region. You can [request an increase](https://console.aws.amazon.com/servicequotas/home/services/fms/quotas "https://console.aws.amazon.com/servicequotas/home/services/fms/quotas") in these quotas.

| All policy types                                                                                                                                                                        | Resource                                                                                                                                                                                                   | Default quota per Region |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Accounts per organization in AWS Organizations                                                                                                                                          | Varies. An invitation sent to an account counts against this quota.<br>The count is returned if the invited account declines, the management account cancels the invitation,<br>or the invitation expires. |
| Firewall Manager policies per organization in AWS Organizations.                                                                                                                        | 50. The Region specifications `Global` and `US East (N. Virginia) Region` refer to the same Region, so this limit applies to the total combined policies for the two of them.                              |
| Organizational units in scope per Firewall Manager policy.                                                                                                                              | 20                                                                                                                                                                                                         |
| Accounts in scope of a Firewall Manager policy if you explicitly include and exclude individual<br>accounts.                                                                            | 200                                                                                                                                                                                                        |
| Accounts in scope of a Firewall Manager policy if you do not explicitly include or exclude individual<br>accounts.                                                                      | 2,500                                                                                                                                                                                                      |
| Accounts that an organization in AWS Organizations can contain for the organization to be onboarded by Firewall Manager. The count includes the Firewall Manager administrator account. | 10,000                                                                                                                                                                                                     |
| Tags that include or exclude resources per Firewall Manager<br>policy.                                                                                                                  | 8                                                                                                                                                                                                          |
| Number of resource sets per account.                                                                                                                                                    | 20                                                                                                                                                                                                         |
| Number of resources per resource set.                                                                                                                                                   | 100                                                                                                                                                                                                        |
| Number of resources sets per Firewall Manager policy.                                                                                                                                   | 5                                                                                                                                                                                                          |

| AWS WAF policies                                                        | Resource | Default quota per Region |
| ----------------------------------------------------------------------- | -------- | ------------------------ |
| AWS WAF rule groups per Firewall Manager administrator account.         | 100      |
| AWS WAF Classic rule groups per Firewall Manager administrator account. | 10       |
| Rule groups per AWS WAF policy.                                         | 50       |
| Partner rule groups per AWS WAF policy.                                 | 1        |

| Common security group policies                                               | Resource | Default quota per Region. |
| ---------------------------------------------------------------------------- | -------- | ------------------------- |
| Primary security groups per policy.                                          | 3        |
| Amazon VPC instances in scope per policy per account, including shared VPCs. | 100      |

| Content audit security group policies                              | Resource | Default quota per Region |
| ------------------------------------------------------------------ | -------- | ------------------------ |
| Audit security groups per policy.                                  | 1        |
| Applications per application list.                                 | 50       |
| Custom managed application lists for rules that allow all traffic. | 1        |
| Custom managed application lists per policy rules.                 | 1        |
| Custom managed application lists per account.                      | 10       |
| Protocols per protocol list.                                       | 5        |
| Custom managed protocol lists for any setting in a policy.         | 1        |
| Custom managed protocol lists per account.                         | 10       |

| Network ACL policies                                                                                                                                                                                            | Resource | Default quota per Region |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------ |
| Number of inbound rules per network ACL policy, used for first or last rules. For example,<br>you can have 5 first and 0 last inbound rules, or 2 first and 3 last,<br>but you can't have 4 first and 2 last.   | 5        |
| Number of outbound rules per network ACL policy, used for first or last rules. For example,<br>you can have 5 first and 0 last outbound rules, or 2 first and 3 last,<br>but you can't have 4 first and 2 last. | 5        |

| Network Firewall policies                                          | Resource | Default quota per Region |
| ------------------------------------------------------------------ | -------- | ------------------------ |
| The number of IPV4 CIDRs that you can provide for a single policy. | 50       |
| Stateful rule group capacity per Network Firewall policy.          | 30,000   |

| DNS Firewall policies                             | Resource | Default quota per Region |
| ------------------------------------------------- | -------- | ------------------------ |
| DNS Firewall rule groups per DNS Firewall policy. | 2        |

## Hard quotas

The following per-Region quotas related to AWS Firewall Manager can't be changed.

| All policy types                                                                                                                                                                                                     | Resource | Quota per Region |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- |
| The maximum number of Firewall Manager administrators you can have in an AWS Organizations organization. You must have at one default administrator, and as many as nine additional Firewall Manager administrators. | 10       |

| AWS WAF policies                                                                | Resource | Quota per Region |
| ------------------------------------------------------------------------------- | -------- | ---------------- |
| Total web ACL capacity units (WCU) for the rule groups in an AWS WAF<br>policy. | 5,000    |

| AWS WAF Classic policies                                               | Resource                                                           | Quota per Region |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------- |
| AWS WAF Classic rule groups per policy.                                | 2: 1 customer-created rule group and 1 AWS Marketplace rule group. |
| AWS WAF Classic rules per Firewall Manager AWS WAF Classic rule group. | 10                                                                 |

| Network Firewall policies                                                | Resource | Quota per Region |
| ------------------------------------------------------------------------ | -------- | ---------------- |
| Number of VPCs that can be automatically remediated for a single policy. | 1,000    |
| Stateless rule groups per Network Firewall policy.                       | 20       |
| Stateful rule groups per Network Firewall policy.                        | 20       |
| Stateless rule group capacity per Network Firewall policy.               | 30,000   |
