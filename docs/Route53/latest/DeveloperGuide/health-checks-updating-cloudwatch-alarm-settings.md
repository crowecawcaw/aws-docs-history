# Updating health

checks when you change CloudWatch alarm settings (health checks that monitor a CloudWatch
alarm only)

If you create a Route 53 health check that monitors the data stream for a CloudWatch alarm
and then you update the settings in the CloudWatch alarm, Route 53 doesn't automatically
update the alarm settings in the health check. If you want the health check to start
using the new alarm settings, you need to update the health check.

###### Note

To update a health check programmatically, you can use the
`UpdateHealthCheck` API. Just specify the current values for
`AlarmIdentifier` and `Region`, and Route 53 will get the
latest settings from CloudWatch. For more information, see [UpdateHealthCheck](../APIReference/API_UpdateHealthCheck.md "../APIReference/API_UpdateHealthCheck.md") in
the _Amazon Route 53 API Reference_.

###### Note

We're updating the health checks console for Route 53. During the transition period, you can continue
to use the old console.

Choose the tab for the console you are using.

- [New console](#health-checks-updating-cloudwatch-alarm-settings-new "#health-checks-updating-cloudwatch-alarm-settings-new")
- [Old console](#health-checks-updating-cloudwatch-alarm-settings-old "#health-checks-updating-cloudwatch-alarm-settings-old")

New console

###### To

update a health check with new CloudWatch alarm settings

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Health checks**.
3. Select the linked ID for the health check that you want to update.
4. Choose **Edit**.

A note explains that the CloudWatch alarm for the health check has changed. The
**Details** field shows the new alarm settings. 5. Choose **Save**.

Old console

###### To

update a health check with new CloudWatch alarm settings (console)

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Health Checks**.
3. Select the check box for the health check that you want to update.
4. Choose **Edit health check**.

A note explains that the CloudWatch alarm for the health check has changed. The
**Details** field shows the new alarm settings. 5. Choose **Save**.
