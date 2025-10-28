# Monitor Load balancer Capacity Unit reservation for your Network Load Balancer

###### Reservation status

The following are the possible status values for an LCU reservation:

- `pending` ‐ Indicates the reservation it is in the process of
  provisioning.
- `provisioned` ‐ Indicates the reserved capacity is
  ready and available to use.
- `failed` ‐ Indicates the request cannot be completed
  at the time.
- `rebalancing` ‐ Indicates an availability zone has been added or
  removed and the load balancer is rebalancing capacity.

###### LCU utilization

To determine reserved LCU utilization, you can compare the per-minute
`ProcessedBytes` metric with the per-hour `Sum(ReservedLCUs)`.
To convert bytes per minute to LCU per hour, use (bytes per min)\*8/60/ (10^6)/2.2.

Console

###### To view the status of an LCU reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer name.
4. On the **Capacity** tab, you can view the
   **Reservation Status** and **Reserved
   LCU** value.

AWS CLI

###### To monitor the status of an LCU reservation

Use the [describe-capacity-reservation](../../../cli/latest/reference/elbv2/describe-capacity-reservation.md "../../../cli/latest/reference/elbv2/describe-capacity-reservation.md") command.

```
aws elbv2 describe-capacity-reservation \
    --load-balancer-arn `load-balancer-arn`
```
