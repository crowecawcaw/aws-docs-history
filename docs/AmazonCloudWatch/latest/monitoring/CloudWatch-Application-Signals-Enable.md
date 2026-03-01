# Enable Application Signals in your account

If you haven't enabled Application Signals in this account yet, you must grant Application Signals the permissions it needs to discover your services. You need to do this only once for your account.

###### To enable CloudWatch Application Signals, do the following.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Services**.
3. Choose **Start discovering your Services**.
4. Select the check box and choose **Start discovering Services**.

Completing this step for the first time in your account creates the
**AWSServiceRoleForCloudWatchApplicationSignals**
service-linked role. This role grants
Application Signals the following permissions:

    * `xray:GetServiceGraph`
    * `logs:StartQuery`
    * `logs:GetQueryResults`
    * `cloudwatch:GetMetricData`
    * `cloudwatch:ListMetrics`
    * `tag:GetResources`

For more information about this role, see
[Service-linked role permissions for CloudWatch Application Signals](using-service-linked-roles.md#service-linked-role-signals "using-service-linked-roles.md#service-linked-role-signals"). 5. Choose **Enable Application Signals**.
