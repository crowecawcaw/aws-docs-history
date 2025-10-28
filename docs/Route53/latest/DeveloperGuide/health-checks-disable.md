# Disabling or enabling health checks

Disabling a health check stops Route 53 from performing health checks. When you disable a health check,
Route 53 stops aggregating the status of the referenced health checks.

After you disable a health check, Route 53 considers the status of the health check to always be healthy.
If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources.
If you want to stop routing traffic to a resource, change the value of **Inverted**.

###### Note

We're updating the health checks console for Route 53. During the transition period, you can continue
to use the old console.

You can disable or enable a health check on the old console when you create or edit the health check. For more information, see
[Values that you specify when you
create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md").

To disable health checks on the new console, perform the following procedure.

###### To disable or enable a health check (new console only)

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Health checks**.
3. In the **Actions** column select the three dots and then **Disable** or **Enable**.

Or, select the linked ID of the health check that you want to disable or enable. 4. On the **Configuration** table, the **Status** field specifies whether the health check
is enabled, or disabled. 5. Choose **Disable** or **Enable** to either disable or enable the health check.
