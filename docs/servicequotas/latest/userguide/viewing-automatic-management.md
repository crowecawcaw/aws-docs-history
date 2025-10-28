# Viewing Service Quotas Automatic Management configuration

Use the following procedure to view Service Quotas Automatic Management configurations for your AWS account
using the AWS Management Console or AWS CLI.

AWS Management Console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose
   **Automatic Management**.
   1. You can edit your notification configurations, [add exceptions for
      AWS services you don't want to monitor with
      Automatic Management](excluding-quotas.md "excluding-quotas.md") or [stop
      Automatic Management](stopping-automatic-management.md "stopping-automatic-management.md").

AWS CLI
Use the following command to view your Automatic Management configuration. Replace
the `italicized placeholder text` in the example
command with your information.

```
aws service-quotas get-auto-management-configuration --region `ca-central-1`
```

###### Example response

```
{
    "OptInLevel": "ACCOUNT",
    "OptInType": "NotifyAndAdjust",
    "OptInStatus": "ENABLED",
    "NotificationArn": "arn:aws:notifications::`111122223333`:configuration/`abc123def456gh789`"
    "ExclusionList": {
        "dynamodb": [{
            "QuotaCode": "`L-E123ABC4`",
            "QuotaName": "Maximum number of tables"
        }]
    }}
```
