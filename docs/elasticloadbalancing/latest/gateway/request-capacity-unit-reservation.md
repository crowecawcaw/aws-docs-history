# Request Load balancer Capacity Unit reservation for your Gateway Load Balancer

Before you use LCU reservation, review the following:

- LCU reservation only supports reserving throughput capacity for
  Gateway Load Balancers. When requesting a LCU reservation, convert your capacity
  needs from Mbps to LCUs using the conversion rate of 1 LCU to 2.2
  Mbps.
- Capacity is reserved at the regional level and is evenly
  distributed across availability zones. Confirm you have
  enough evenly distributed targets in each availability zone
  before turning on LCU reservation.
- LCU reservation requests are fulfilled on a first
  come first serve basis, and depends on available capacity
  for a zone at that time. Most requests are typically fulfilled
  within an hour, but can take up to a few hours.
- To update an existing reservation, the previous request
  must be provisioned or failed. You can increase reserved
  capacity as many times as you need, however you can only decrease the
  reserved capacity two times per day.

###### Request a LCU reservation

The steps in this procedure explain how to request a LCU reservation on
your load balancer.

###### To request a LCU reservation using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer name.
4. On the **Capacity** tab, choose **Edit LCU
   Reservation**.
5. Select **Historic reference based estimate**, then select
   the load balancer from the dropdown list.
6. Select the reference period to view the recommended reserved LCU level.
7. If you do not have historic reference workload, you can choose
   **Manual estimate** and enter the number of LCUs
   to be reserved.
8. Choose **Save**.

###### To request a LCU reservation using AWS CLI

Use the [modify-capacity-reservation](../../../cli/latest/reference/elbv2/modify-capacity-reservation.md "../../../cli/latest/reference/elbv2/modify-capacity-reservation.md") command.
