AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Receiving findings from AWS Security Hub

in Explorer

[AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
provides a comprehensive view of your security state in AWS. The service collects
security data, called _findings_, from across
AWS accounts, services, and supported third-party products. Security Hub findings can
help you check your environment against security industry standards and best
practices, analyze your security trends, and identify the highest priority security
issues.

Security Hub sends findings to Amazon EventBridge, which uses an event rule to send the findings to
Explorer. After you enable integration, as described here, you can view Security Hub
findings in an Explorer widget and view finding details in OpsCenter OpsItems. The
widget provides a summary of all Security Hub findings based on severity. New findings in
Security Hub are usually visible in Explorer within seconds of being created.

###### Warning

Note the following important information:

- Explorer is integrated with OpsCenter, a tool in Systems Manager. After you
  enable Explorer integration with Security Hub, OpsCenter automatically creates
  OpsItems for Security Hub findings. Depending on your AWS environment, enabling
  integration can result in large numbers of OpsItems, at a cost.

Before you continue, read about OpsCenter integration with Security Hub. The
topic includes specific details about how changes and updates to
findings and OpsItems are charged to your account. For more information,
see [Understanding OpsCenter
integration with AWS Security Hub](OpsCenter-applications-that-integrate.md#OpsCenter-integrate-with-security-hub "OpsCenter-applications-that-integrate.md#OpsCenter-integrate-with-security-hub"). For
OpsCenter pricing information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

- If you create a resource data sync in Explorer while logged into the
  administrator account, Security Hub integration is automatically enabled for
  the administrator and all member accounts in the sync. Once enabled,
  OpsCenter automatically creates OpsItems for Security Hub findings, at a cost. For
  more information about creating a resource data sync, see [Setting up Systems Manager Explorer to display data from
  multiple accounts and Regions](Explorer-resource-data-sync.md "Explorer-resource-data-sync.md").

## Types

of findings that Explorer receives

Explorer receives [all findings](../../../securityhub/latest/userguide/securityhub-cwe-integration-types.md#securityhub-cwe-integration-types-all-findings "../../../securityhub/latest/userguide/securityhub-cwe-integration-types.md#securityhub-cwe-integration-types-all-findings") from Security Hub. You can see all findings based on severity
in the Explorer widget when you turn on the Security Hub default settings. By default,
Explorer creates OpsItems for critical and high severity findings. You can manually
configure Explorer to create OpsItems for medium and low severity findings.

Though Explorer doesn't create OpsItems for informational findings, you can view
informational operations data (OpsData) in the Security Hub findings summary widget.
Explorer creates OpsData for all findings regardless of severity. For more
information about Security Hub severity levels, see [Severity](../../../securityhub/1.0/APIReference/API_Severity.md "../../../securityhub/1.0/APIReference/API_Severity.md") in
the _AWS Security Hub API Reference_.

## Enabling

integration

This section describes how to enable and configure Explorer to start receiving
Security Hub findings.

###### Before you begin

Complete the following tasks before you configure Explorer to start
receiving Security Hub findings.

- Enable and configure Security Hub. For more information, see [Setting up Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the _AWS Security Hub User Guide_.
- Log into the AWS Organizations management account. Systems Manager requires access to
  AWS Organizations to create OpsItems from Security Hub findings. After you log in to the
  management account, you're prompted to select the **Enable
  access** button on the Explorer **Configure
  dashboard** tab, as described in the following procedure.
  If you don't log in to the AWS Organizations management account, you can't allow
  access and Explorer can't create OpsItems from Security Hub findings.

###### To start receiving Security Hub findings

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Select **Settings**.
4. Select the **Configure dashboard** tab.
5. Select **AWS Security Hub**.
6. Select the **Disabled** slider to turn on
   **AWS Security Hub**.

Critical and high severity findings are displayed by default. To
display medium and low severity findings, select the
**Disabled** slider next to
**Medium,Low**. 7. In the **OpsItems created by Security Hub findings** section,
choose **Enable access**. If you don't see this button,
log in to the AWS Organizations management account and return to this page to
select the button.

## How to

view findings from Security Hub

The following procedure describes how to view Security Hub findings.

###### To view Security Hub findings

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Find the **AWS Security Hub findings summary** widget. This
   displays your Security Hub findings. You can select a severity level to view a
   detailed description of the corresponding OpsItem.

## How to stop

receiving findings

The following procedure describes how to stop receiving Security Hub findings.

###### To stop receiving Security Hub findings

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Select **Settings**.
4. Select the **Configure dashboard** tab.
5. Select the **Enabled** slider to turn off
   **AWS Security Hub**.

###### Important

If the option to disable Security Hub findings is grayed out in the console, you
can disable this setting by running the following command in the AWS CLI. You
must run the command while logged into either the AWS Organizations management
account or the Systems Manager delegated administrator account. For the
`region` parameter, specify the AWS Region where you want
to stop receiving Security Hub findings in Explorer.

```

aws ssm update-service-setting --setting-id /ssm/opsdata/SecurityHub --setting-value Disabled --region `AWS Region`
```

Here's an example.

```

aws ssm update-service-setting --setting-id /ssm/opsdata/SecurityHub --setting-value Disabled --region us-east-1
```
