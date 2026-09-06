

# Understand codes for Elastic Load Balancing in billing and usage reports
<a name="load-balancer-billing-usage-reports"></a>

When you use Elastic Load Balancing, we include related codes in your AWS billing and usage reports. Reviewing these codes helps you understand your load balancer costs and usage patterns. Tracking and managing your expenses is essential for optimizing your costs.

For more information, see [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/).

The following tables describe the codes for Elastic Load Balancing that appear in your billing and usage reports. The units are hours or load balancer capacity units (LCU). Each load balancer type has a specific definition of LCU. For information about the LCUs for each load balancer type, see [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/). For a list of the Region codes used in the billing and usage reports, see [AWS Region billing codes](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-region-billing-codes.html).

## Application Load Balancers
<a name="alb-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-LoadBalancerUsage | The running time. | Hours | 
| {{region}}-LCUUsage | The LCUs used. | LCU | 
| {{region}}-IdleProvisionedLBCapacity | The LCUs reserved but not used. | LCU | 
| {{region}}-TS-LoadBalancerUsage | The time that a trust store is used by Mutual TLS. | Hours | 
| {{region}}-Outposts-LoadBalancerUsage | The running time on Outposts. | Hours | 
| {{region}}-Outposts-LCUUsage | The LCUs used on Outposts. | LCU | 
| {{region}}-ReservedLCUUsage | The LCUs reserved. | LCU | 



## Network Load Balancers
<a name="nlb-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-LoadBalancerUsage | The running time. | Hours | 
| {{region}}-LCUUsage | The LCUs used. | LCU | 

## Gateway Load Balancers
<a name="glb-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-LoadBalancerUsage | The running time. | Hours | 
| {{region}}-LCUUsage | The LCUs used. | LCU | 

## Classic Load Balancers
<a name="clb-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-LoadBalancerUsage | The running time. | Hours | 
| {{region}}-DataProcessing-Bytes | The data processed. | GB | 
| {{region}}-IdleProvisionedLBCapacity | The LCUs reserved but not used. | LCU | 