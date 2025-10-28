# Enable or disable Verified Access trust context

The trust context sent from your trust provider can optionally be enabled for inclusion
in your Verified Access logs. This can be useful when defining policies that allow or deny access
to your applications. After you enable it, the trust context is found in the log under
the `data` field. If trust context is disabled, the `data` field
is set to `null`. To configure Verified Access to include trust context in the logs, do
the following procedure.

###### Note

Including trust context in your Verified Access logs requires upgrading to the latest logging version
`ocsf-1.0.0-rc.2`. The following procedure assumes that you already
have logging enabled. If that is not true, see [Enable access logs](access-logs-enable.md#enable-access-logs "access-logs-enable.md#enable-access-logs") for the full procedure.

###### Contents

- [Enable trust context](#enable-trust-context "#enable-trust-context")
- [Disable trust context](#disable-trust-context "#disable-trust-context")

## Enable trust context

###### To include trust context in the Verified Access logs using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access instances**.
3. Select the appropriate Verified Access instance.
4. On the **Verified Access instance logging configuration** tab, choose
   **Modify Verified Access instance logging configuration**.
5. Select **ocsf-1.0.0-rc.2** from the **Update log
   version** drop-down list.
6. Turn on **Include trust context**.
7. Choose **Modify Verified Access instance logging configuration**.

###### To include trust context in the Verified Access logs using the AWS CLI

Use the [modify-verified-access-instance-logging-configuration](../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md "../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md") command.

## Disable trust context

If you no longer want to include trust context in the logs, you can remove it by
doing the following procedure.

###### To remove trust context from the Verified Access logs using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access
   instances**.
3. Select the appropriate Verified Access instance.
4. On the **Verified Access instance logging configuration** tab,
   choose **Modify Verified Access instance logging
   configuration**.
5. Turn off **Include trust context**.
6. Choose **Modify Verified Access instance logging
   configuration**.

###### To remove trust context from the Verified Access logs using the AWS CLI

Use the [modify-verified-access-instance-logging-configuration](../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md "../../../cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.md") command.
