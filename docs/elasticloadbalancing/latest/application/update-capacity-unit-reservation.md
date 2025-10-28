# Update or cancel Load Balancer Capacity Unit reservations for your Application Load Balancer

If the traffic patterns for your load balancer change, you can update or cancel the
LCU reservation for your load balancer. The status of the LCU reservation must be
**Provisioned**.

Console

###### To update or cancel an LCU reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer name.
4. On the **Capacity** tab, do one of the following:
   1. To update the LCU reservation choose **Edit LCU Reservation**.
   2. To cancel the LCU reservation, choose **Cancel Capacity**.

AWS CLI

###### To cancel an LCU reservation

Use the [modify-capacity-reservation](../../../cli/latest/reference/elbv2/modify-capacity-reservation.md "../../../cli/latest/reference/elbv2/modify-capacity-reservation.md") command.

```
aws elbv2 modify-capacity-reservation \
    --load-balancer-arn `load-balancer-arn` \
    --reset-capacity-reservation
```
