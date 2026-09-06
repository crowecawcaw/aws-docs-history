

# Cancel a zonal shift for your Network Load Balancer
<a name="cancel-zonal-shift"></a>

You can cancel a zonal shift any time before it expires. You can cancel zonal shifts that you initiate, or zonal shifts that AWS starts for a resource for a practice run for zonal autoshift.

------
#### [ Console ]

This procedure explains how to cancel a zonal shift using the Amazon EC2 console. For steps to cancel a zonal shift using the Amazon Application Recovery Controller (ARC) console, see [Canceling a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

**To cancel a zonal shift**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select a Network Load Balancer with an active zonal shift.

1. On the **Integrations** tab, under **Amazon Application Recovery Controller (ARC)**, choose **Cancel zonal shift**.

   This opens the ARC console to continue the cancelation process.

1. Choose **Cancel zonal shift**.

1. When prompted for confirmation, choose **Confirm**.

------
#### [ AWS CLI ]

**To cancel a zonal shift**  
Use the Amazon Application Recovery Controller (ARC) [cancel-zonal-shift](https://docs.aws.amazon.com/cli/latest/reference/arc-zonal-shift/cancel-zonal-shift.html) command.

```
aws arc-zonal-shift cancel-zonal-shift \
    --zonal-shift-id {{9ac9ec1e-1df1-0755-3dc5-8cf57EXAMPLE}}
```

------