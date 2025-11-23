# Understand codes for ELB in billing and usage reports

When you use ELB, we include related codes in your AWS billing and usage reports. Reviewing these
codes helps you understand your load balancer costs and usage patterns. Tracking and managing your
expenses is essential for optimizing your costs.

For more information, see [ELB pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").

The following tables describe the codes for ELB that appear in your billing and usage
reports. The units are hours or load balancer capacity units (LCU). Each load balancer type
has a specific definition of LCU. For information about the LCUs for each load balancer
type, see [ELB pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").
For a list of the Region codes used in the billing and usage reports, see [AWS Region
billing codes](../../../global-infrastructure/latest/regions/aws-region-billing-codes.md "../../../global-infrastructure/latest/regions/aws-region-billing-codes.md").

## Application Load Balancers

| Code                                  | Description                                        | Units |
| ------------------------------------- | -------------------------------------------------- | ----- |
| ``region`-LoadBalancerUsage`          | The running time.                                  | Hours |
| ``region`-LCUUsage`                   | The LCUs used.                                     | LCU   |
| ``region`-IdleProvisionedLBCapacity`  | The LCUs reserved but not used.                    | LCU   |
| ``region`-TS-LoadBalancerUsage`       | The time that a trust store is used by Mutual TLS. | Hours |
| ``region`-Outposts-LoadBalancerUsage` | The running time on Outposts.                      | Hours |
| ``region`-Outposts-LCUUsage`          | The LCUs used on Outposts.                         | LCU   |
| ``region`-ReservedLCUUsage`           | The LCUs reserved.                                 | LCU   |

## Network Load Balancers

| Code                         | Description       | Units |
| ---------------------------- | ----------------- | ----- |
| ``region`-LoadBalancerUsage` | The running time. | Hours |
| ``region`-LCUUsage`          | The LCUs used.    | LCU   |

## Gateway Load Balancers

| Code                         | Description       | Units |
| ---------------------------- | ----------------- | ----- |
| ``region`-LoadBalancerUsage` | The running time. | Hours |
| ``region`-LCUUsage`          | The LCUs used.    | LCU   |

## Classic Load Balancers

| Code                                 | Description                     | Units |
| ------------------------------------ | ------------------------------- | ----- |
| ``region`-LoadBalancerUsage`         | The running time.               | Hours |
| ``region`-DataProcessing-Bytes`      | The data processed.             | GB    |
| ``region`-IdleProvisionedLBCapacity` | The LCUs reserved but not used. | LCU   |
