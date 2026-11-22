

# Creating and updating health checks

The following procedure describes how to create and update health checks using the Route 53 console.<a name="health-checks-creating-proc"></a>

**To create or update a health check**

1. If you're updating health checks that are already associated with records, perform the recommended tasks in [Updating or deleting health checks when DNS failover is configured](health-checks-updating-deleting-tasks.md).

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health Checks**.

1. If you want to update an existing health check, choose the linked ID of the health check, and then choose **Edit**.

   If you want to create a health check, choose **Create health check**.

1. Enter the applicable values. Note that some values can't be changed after you create a health check. For more information, see [Values that you specify when you create or update health checks](health-checks-creating-values.md).
**Note**  
To monitor a private endpoint, choose **Private endpoint** for **Resource**, and then choose an existing health check source or create one. For the values to specify, see [Values that you specify when you create or update a private endpoint health check](health-checks-creating-values.md#health-checks-creating-values-private-endpoint). For more information about health check sources, see [Health check sources](health-check-sources.md).

1. Choose **Create health check**.
**Note**  
Route 53 considers a new health check to be healthy until there's enough data to determine the actual status, healthy or unhealthy.

1. Associate the health check with one or more Route 53 records. For information about creating and updating records, see [Working with records](rrsets-working-with.md).