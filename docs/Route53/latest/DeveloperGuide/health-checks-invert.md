# Inverting health checks

If you invert a health check, Route 53 considers the health
check to be unhealthy when the status is healthy and vice versa.

###### Note

We're updating the health checks console for Route 53. During the transition period, you can continue
to use the old console.

You can invert a health check on the old console when you create or edit the health check. For more information, see
[Values that you specify when you
create or update health checks](health-checks-creating-values.md "health-checks-creating-values.md").

To invert health checks on the new console, perform the following procedure.

###### To invert a health check (new console

only)

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Health checks**.
3. In the **Actions** column select the three dots and then **Invert**.

Or- select the linked ID of the health check that you want to invert. 4. On the **Configuration** table, the **Inverted** filed specifies whether the health check
is inverted (**Yes**) or not (**No**). 5. Choose **Invert** to invert the health check.

If you want to undo the inverted status, and the **Inverted** field is **Yes**, choose **Invert** again.
