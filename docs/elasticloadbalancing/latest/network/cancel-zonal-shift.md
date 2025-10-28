# Cancel a zonal shift for your Network Load Balancer

You can cancel a zonal shift any time before it expires. You can cancel zonal shifts
that you initiate, or zonal shifts that AWS starts for a resource for a practice
run for zonal autoshift.

Console
This procedure explains how to cancel a zonal shift using the Amazon EC2 console.
For steps to cancel a zonal shift using the Amazon Application Recovery Controller (ARC) console, see [Canceling a zonal shift](../../../r53recovery/latest/dg/arc-zonal-shift.md "../../../r53recovery/latest/dg/arc-zonal-shift.md")
in the _Amazon Application Recovery Controller (ARC) Developer Guide_.

###### To cancel a zonal shift

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Load Balancers**.
3. Select a Network Load Balancer with an active zonal shift.
4. On the **Integrations** tab, under **Amazon Application Recovery Controller (ARC)**,
   choose **Cancel zonal shift**.

This opens the ARC console to continue the cancelation process. 5. Choose **Cancel zonal shift**. 6. When prompted for confirmation, choose **Confirm**.

AWS CLI

###### To cancel a zonal shift

Use the Amazon Application Recovery Controller (ARC) [cancel-zonal-shift](../../../cli/latest/reference/arc-zonal-shift/cancel-zonal-shift.md "../../../cli/latest/reference/arc-zonal-shift/cancel-zonal-shift.md") command.

```
aws arc-zonal-shift cancel-zonal-shift \
    --zonal-shift-id `9ac9ec1e-1df1-0755-3dc5-8cf57EXAMPLE`
```
