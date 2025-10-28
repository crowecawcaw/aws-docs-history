# Monitor Load balancer Capacity Unit reservation for your Gateway Load Balancer

###### Reservation Status

LCU reservation has four available status:

- pending ‐ Indicates the reservation it is in the process of
  provisioning.
- provisioned ‐ Indicates the reserved capacity is
  ready and available to use.
- failed ‐ Indicates the request cannot be completed
  at the time.
- rebalancing ‐ Indicates an availability zone has been added
  and the load balancer is rebalancing capacity.

###### Reserved LCU

To determine reserved LCU utilization, you can compare the per-minute
**PeakBytesPerSecond** metric with the per-hour Sum(ReservedLCUs). To convert
bytes per minute to LCU per hour, use (bytes per min)\*8/60/ (10^6)/2.2.

###### Monitor reserved capacity

The steps in this process explain how to check the status
of a LCU reservation on your load balancer.

###### To view the status of a LCU reservation using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer name.
4. On the **Capacity** tab, you can view the
   **Reservation Status** and **Reserved
   LCU** value.

###### To monitor the status of the LCU reservation using AWS CLI

Use the [describe-capacity-reservation](../../../cli/latest/reference/elbv2/describe-capacity-reservation.md "../../../cli/latest/reference/elbv2/describe-capacity-reservation.md") command.
