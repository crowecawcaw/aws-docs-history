

# Update or terminate Load balancer Capacity Unit reservations for your Gateway Load Balancer
<a name="update-capacity-unit-reservation"></a>

**Update or terminate a LCU reservation**  
The steps in this procedure explain how to update or terminate a LCU reservation on your load balancer.

**To update or terminate a LCU reservation using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer name.

1. On the **Capacity** tab, confirm the status of reservation is Provisioned.

   1. To update the LCU reservation choose **Edit LCU Reservation**.

   1. To terminate the LCU reservation, choose **Cancel Capacity**.

**To update or terminate a LCU reservation using the AWS CLI**  
Use the [modify-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-capacity-reservation.html) command.