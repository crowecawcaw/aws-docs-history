

# Update a zonal shift for your Application Load Balancer
<a name="update-zonal-shift"></a>

You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.

------
#### [ Console ]

This procedure explains how to update a zonal shift using the Amazon EC2 console. For steps to update a zonal shift using the Amazon Application Recovery Controller (ARC) console, see [Updating a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

**To update a zonal shift**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select an Application Load Balancer with an active zonal shift.

1. On the **Integrations** tab, expand **Amazon Application Recovery Controller (ARC)** and choose **Update zonal shift**.

   This opens the ARC console to continue the update process.

1. (Optional) For **Set zonal shift expiration**, select or enter an expiration.

1. (Optional) For **Comment**, optionally edit the existing comment or enter a new comment.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To update a zonal shift**  
Use the Amazon Application Recovery Controller (ARC) [update-zonal-shift](https://docs.aws.amazon.com/cli/latest/reference/arc-zonal-shift/update-zonal-shift.html) command.

```
aws arc-zonal-shift update-zonal-shift \
    --zonal-shift-id {{9ac9ec1e-1df1-0755-3dc5-8cf57EXAMPLE}} \
    --expires-in {{1h}} \
    --comment "{{extending zonal shift for scheduled maintenance}}"
```

------