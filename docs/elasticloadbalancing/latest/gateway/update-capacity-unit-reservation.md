# Update or terminate Load balancer Capacity Unit reservations for your Gateway Load Balancer

###### Update or terminate a LCU reservation

The steps in this procedure explain how to
update or terminate a LCU reservation on your
load balancer.

###### To update or terminate a LCU reservation using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer name.
4. On the **Capacity** tab, confirm the status
   of reservation is Provisioned.
   1. To update the LCU reservation choose **Edit LCU Reservation**.
   2. To terminate the LCU reservation, choose **Cancel Capacity**.

###### To update or terminate a LCU reservation using the AWS CLI

Use the [modify-capacity-reservation](../../../cli/latest/reference/elbv2/modify-capacity-reservation.md "../../../cli/latest/reference/elbv2/modify-capacity-reservation.md") command.
