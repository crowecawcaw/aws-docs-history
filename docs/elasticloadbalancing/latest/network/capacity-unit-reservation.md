# Capacity reservations for your Network Load Balancer

Load balancer Capacity Unit (LCU) reservations allow
you to reserve a static minimum capacity for your load balancer. Network Load Balancers
automatically scale to support detected workloads and meet capacity needs.
When minimum capacity is configured, your load balancer continues scaling
up or down based on the traffic received, but also prevents the capacity
from going lower than the minimum capacity configured.

Consider using LCU reservation in following situations:

- You have an upcoming event that will have a sudden, unusual
  high traffic and want to ensure your load balancer can support
  the sudden traffic spike during the event.
- You have unpredictable spiky traffic due to the nature of
  your workload for a short period.
- You are setting up your load balancer to on-board
  or migrate your services at a specific start time
  and need start with a high capacity instead of waiting
  for auto-scaling to take effect.
- You are migrating workloads between load balancers and
  want to configure the destination to match the scale of
  the source.

###### Estimate the capacity that you need

When determining the amount of capacity you should reserve for your load
balancer, we recommend performing load testing or reviewing historical workload data that
represents the upcoming traffic you expect. Using the ELB console, you can
estimate how much capacity you need to reserve based on the reviewed traffic.

Alternatively, you can refer to CloudWatch metric **ProcessedBytes** to
determine the right level of capacity. Capacity for your load balancer is reserved in
LCUs, with each LCU being equal to 2.2Mbps. You can use the Max
(**ProcessedBytes**) metric to see the maximum per-minute throughput
traffic on the load balancer, then convert that throughput to LCUs using a conversion
rate of 2.2Mbps equals 1 LCU.

If you don't have historical workload data to reference and cannot perform load
testing, you can estimate capacity needed using the LCU reservation calculator. The
LCU reservation calculator uses data based on historical workloads AWS observe and
may not represent your specific workload. For more information,
see [Load
Balancer Capacity Unit Reservation Calculator](https://exampleloadbalancer.com/ondemand_capacity_reservation_calculator.html "https://exampleloadbalancer.com/ondemand_capacity_reservation_calculator.html").

###### Supported Regions

This feature is available only in the following Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Asia Pacific (Hong Kong)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (Stockholm)

###### Minimum and maximum values for an LCU reservation

The total reservation request must be at least 2,750 LCU per Availability
Zone. The maximum value is determined by the quotas for your account. For
more information, see [Load Balancer Capacity Units](load-balancer-limits.md#lcu-quotas "load-balancer-limits.md#lcu-quotas").
