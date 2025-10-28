# Viewing your configuration recorders

You can use the AWS Config console or the AWS CLI view details about your configuration
recorders.

To view your configuration recorders (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Settings** in the navigation pane.
3. For the customer managed configuration recorder, you can view details on the
   **Customer managed recorder** tab.
4. For service-linked configuration recorders, choose a service-linked
   configuration recorders on the **Service-linked recorders** tab,
   and then choose **View**.

To view your configuration recorders (CLI)
Use the [`describe-configuration-recorders`](../../../cli/latest/reference/configservice/describe-configuration-recorders.md "../../../cli/latest/reference/configservice/describe-configuration-recorders.md") command to view details
about your configuration recorders:

```
$ **aws configservice describe-configuration-recorders**
{
    "ConfigurationRecorders": [
        {
            "roleARN": "arn:aws:iam::012345678912:role/myConfigRole",
            "name": "default"
        }
    ]
}
```

Use the [`describe-configuration-recorder-status`](../../../cli/latest/reference/configservice/describe-configuration-recorder-status.md "../../../cli/latest/reference/configservice/describe-configuration-recorder-status.md") command to view the current
status of your configuration recorders:

```
$ **aws configservice describe-configuration-recorder-status**
{
    "ConfigurationRecordersStatus": [
        {
            "name": "default",
            "lastStatus": "SUCCESS",
            "lastStopTime": 1414511624.914,
            "lastStartTime": 1414708460.276,
            "recording": true,
            "lastStatusChangeTime": 1414816537.148,
            "lastErrorMessage": "NA",
            "lastErrorCode": "400"
        }
    ]
}
```

For both of these commands, you can use the `arn` and
`configuration-recorder-names` fields to specify a list of configuration
recorders. For service-linked configuration recorders, you can use the
`service-principal` field to specify a configuration recorder.

If a configuration recorder is not specified, this command returns the details of
all configuration recorders associated with the account.
