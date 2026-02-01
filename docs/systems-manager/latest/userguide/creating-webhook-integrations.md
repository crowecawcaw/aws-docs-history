• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Creating webhook integrations for

Automation

To send messages using webhooks during an automation, create an integration.
Integrations can be invoked during an automation by using the
`aws:invokeWebhook` action in your runbook. If you haven't already
created a webhook, see [Creating webhooks for integrations](#creating-webhooks "#creating-webhooks"). To learn more about the
`aws:invokeWebhook` action, see [aws:invokeWebhook – Invoke an
Automation webhook integration](invoke-webhook.md "invoke-webhook.md").

As shown in the following procedures, you can create an integration by using
either the Systems Manager Automation console or your preferred command line tool.

## Creating integrations

(console)

###### To create an integration for Automation (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Automation**.
3. Choose the **Integrations** tab.
4. Select **Add integration**, and choose
   **Webhook**.
5. Enter the required values and any optional values you want to include
   for the integration.
6. Choose **Add** to create the integration.

## Creating integrations

(command line)

To create an integration using command line tools, you must create the
required `SecureString` parameter for an integration. Automation uses
a reserved namespace in Parameter Store, a tool in Systems Manager, to store information about
your integration. If you create an integration using the AWS Management Console, Automation
handles this process for you. Following the namespace, you must specify the type
of integration you want to create and then the name of your integration.
Currently, Automation supports `webhook` type integrations.

The supported fields for `webhook` type integrations are as
follows:

- Description
- headers
- payload
- URL

###### Before you begin

If you haven't already, install and configure the AWS Command Line Interface (AWS CLI) or the
AWS Tools for PowerShell. For information, see [Installing or
updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Installing
the AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md").

###### To create an integration for Automation (command line)

- Run the following commands to create the required
  `SecureString` parameter for an integration. Replace each
  `example resource placeholder` with your
  own information. The
  `/d9d01087-4a3f-49e0-b0b4-d568d7826553/ssm/integrations/webhook/`
  namespace is reserved in Parameter Store for integrations. The name of your
  parameter must use this namespace followed by the name of your
  integration. For example
  `/d9d01087-4a3f-49e0-b0b4-d568d7826553/ssm/integrations/webhook/`myWebhookIntegration``.

Linux & macOS

```
aws ssm put-parameter \
    --name "/d9d01087-4a3f-49e0-b0b4-d568d7826553/ssm/integrations/webhook/`myWebhookIntegration`" \
    --type "SecureString" \
    --data-type "aws:ssm:integration" \
    --value '{"description": "`My first webhook integration for Automation`.", "url": "`myWebHookURL`"}'
```

Windows

```
aws ssm put-parameter ^
    --name "/d9d01087-4a3f-49e0-b0b4-d568d7826553/ssm/integrations/webhook/`myWebhookIntegration`" ^
    --type "SecureString" ^
    --data-type "aws:ssm:integration" ^
    --value  "{\"description\":\"`My first webhook integration for Automation`.\",\"url\":\"`myWebHookURL`\"}"
```

PowerShell

```
Write-SSMParameter `
    -Name "/d9d01087-4a3f-49e0-b0b4-d568d7826553/ssm/integrations/webhook/`myWebhookIntegration`" `
    -Type "SecureString"
    -DataType "aws:ssm:integration"
    -Value '{"description": "`My first webhook integration for Automation`.", "url": "`myWebHookURL`"}'
```

## Creating webhooks for integrations

When creating webhooks with your provider, note the following:

- Protocol must be HTTPS.
- Custom request headers are supported.
- A default request body can be specified.
- The default request body can be overridden when an integration is
  invoked by using the `aws:invokeWebhook` action.
