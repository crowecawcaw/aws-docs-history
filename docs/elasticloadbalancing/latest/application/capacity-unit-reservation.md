# Capacity reservations for your Application Load Balancer

Load balancer Capacity Unit (LCU) reservations allow
you to reserve a static minimum capacity for your load balancer. Application Load Balancers
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
represents the upcoming traffic you expect. Using the Elastic Load Balancing console, you can
estimate how much capacity you need to reserve based on the reviewed traffic.

Alternatively, you can utilize the CloudWatch metric `PeakLCUs` to
determine the level of capacity needed. The `PeakLCUs` metric
accounts for peaks in your traffic pattern that the load balancer must scale across all
scaling dimensions to support your workload. The `PeakLCUs` metric is
different from the `ConsumedLCUs` metric, which only aggregates the
billing dimensions of your traffic. Using the `PeakLCUs` metric is
recommended to ensure your LCU reservation is adequate during load balancer scaling.
When estimating capacity, use a per-minute `Sum` of `PeakLCUs`.

If you don't have historical workload data to reference and cannot perform load
testing, you can estimate capacity needed using the LCU reservation calculator. The
LCU reservation calculator uses data based on historical workloads AWS observe and
may not represent your specific workload. For more information,
see [Load
Balancer Capacity Unit Reservation Calculator](https://exampleloadbalancer.com/ondemand_capacity_reservation_calculator.html "https://exampleloadbalancer.com/ondemand_capacity_reservation_calculator.html").

###### Minimum and maximum values for an LCU reservation

The total reservation request must be at least 100 LCU. The maximum value
is determined by the quotas for your account. For more information, see
[Load Balancer Capacity Units](load-balancer-limits.md#lcu-quotas "load-balancer-limits.md#lcu-quotas").
