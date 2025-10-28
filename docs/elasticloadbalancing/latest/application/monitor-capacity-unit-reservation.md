# Monitor Load Balancer Capacity Unit reservation for your Application Load Balancer

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

The `ReservedLCUs` metric is reported on a per-minute basis.
Capacity is reserved on an hourly basis. For example, if you have a LCU
reservation of 6,000, the one-hour total for `ReservedLCUs` is 6,000,
and the one-minute total is 100. To determine your reserved LCU utilization, refer to
the `PeakLCUs` metric. You can set CloudWatch alarms to compare the per-minute
`Sum` of `PeakLCUs` against your reserved capacity value, or
the per-hour `Sum` of `ReservedLCUs`, to determine whether
you have reserved enough capacity to meet your needs.

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
