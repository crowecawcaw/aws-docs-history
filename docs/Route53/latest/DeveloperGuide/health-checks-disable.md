

# Disabling or enabling health checks

Disabling a health check stops Route 53 from performing health checks. When you disable a health check, Route 53 stops aggregating the status of the referenced health checks. After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of **Inverted**.

You can also disable or enable a health check when you create or edit it. For more information, see [Values that you specify when you create or update health checks](health-checks-creating-values.md).

To disable or enable a health check, perform the following procedure.<a name="health-checks-disable-proc"></a>

**To disable or enable a health check**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health checks**.

1. In the **Actions** column select the three dots and then **Disable** or **Enable**. 

   Or, select the linked ID of the health check that you want to disable or enable.

1. On the **Configuration** table, the **Status** field specifies whether the health check is enabled, or disabled.

1. Choose **Disable** or **Enable** to either disable or enable the health check.