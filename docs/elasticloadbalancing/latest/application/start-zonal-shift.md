# Start a zonal shift for your Application Load Balancer

Zonal shift in ARC enables you to temporarily move traffic for supported resources away from an Availability Zone
so that your application can continue to operate normally with other Availability Zones in an AWS Region.

###### Prerequisite

Before you begin, verify that you [enabled zonal shift](enable-zonal-shift.md#enable-zonal-shift.title "enable-zonal-shift.md#enable-zonal-shift.title")
for the load balancer.

Console
This procedure explains how to start a zonal shift using the Amazon EC2 console.
For steps to start a zonal shift using the ARC console, see [Starting a zonal shift](../../../r53recovery/latest/dg/arc-zonal-shift.md "../../../r53recovery/latest/dg/arc-zonal-shift.md")
in the _Amazon Application Recovery Controller (ARC) Developer Guide_.

###### To start a zonal shift

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the Application Load Balancer.
4. On the **Integrations** tab, expand **Amazon Application Recovery Controller (ARC)** and
   choose **Start zonal shift**.
5. Select the Availability Zone that you want to move traffic away from.
6. Choose or enter an expiration for the zonal shift. A zonal shift can initially be set from 1 minute up to three days (72 hours).

All zonal shifts are temporary. You must set an expiration, but you can update active shifts later to set a new expiration. 7. Enter a comment. You can update the zonal shift later to edit the comment. 8. Select the check box to acknowledge that starting a zonal shift reduces capacity for your
application by shifting traffic away from the Availability Zone. 9. Choose **Confirm**.

AWS CLI

###### To start a zonal shift

Use the Amazon Application Recovery Controller (ARC) [start-zonal-shift](../../../cli/latest/reference/arc-zonal-shift/start-zonal-shift.md "../../../cli/latest/reference/arc-zonal-shift/start-zonal-shift.md") command.

```
aws arc-zonal-shift start-zonal-shift \
    --resource-identifier `load-balancer-arn` \
    --away-from `use2-az2` \
    --expires-in `2h` \
    --comment "`zonal shift due to scheduled maintenance`"
```
