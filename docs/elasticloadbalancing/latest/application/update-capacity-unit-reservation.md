

# Update or cancel Load Balancer Capacity Unit reservations for your Application Load Balancer
<a name="update-capacity-unit-reservation"></a>

If the traffic patterns for your load balancer change, you can update or cancel the LCU reservation for your load balancer. The status of the LCU reservation must be **Provisioned**.

------
#### [ Console ]

**To update or cancel an LCU reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer name.

1. On the **Capacity** tab, do one of the following:

   1. To update the LCU reservation choose **Edit LCU Reservation**.

   1. To cancel the LCU reservation, choose **Cancel Capacity**.

------
#### [ AWS CLI ]

**To cancel an LCU reservation**  
Use the [modify-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-capacity-reservation.html) command.

```
aws elbv2 modify-capacity-reservation \
    --load-balancer-arn {{load-balancer-arn}} \
    --reset-capacity-reservation
```

------