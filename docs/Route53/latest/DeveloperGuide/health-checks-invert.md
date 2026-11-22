

# Inverting health checks

If you invert a health check, Route 53 considers the health check to be unhealthy when the status is healthy and vice versa.

You can also invert a health check when you create or edit it. For more information, see [Values that you specify when you create or update health checks](health-checks-creating-values.md).

To invert a health check, perform the following procedure.<a name="health-checks-invert-proc"></a>

**To invert a health check**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health checks**.

1. In the **Actions** column select the three dots and then **Invert**.

   Or- select the linked ID of the health check that you want to invert.

1. On the **Configuration** table, the **Inverted** filed specifies whether the health check is inverted (**Yes**) or not (**No**).

1. Choose **Invert** to invert the health check.

   If you want to undo the inverted status, and the **Inverted** field is **Yes**, choose **Invert** again.