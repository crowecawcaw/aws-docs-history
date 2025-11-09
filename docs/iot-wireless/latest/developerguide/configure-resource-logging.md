# Configure resource logging for

AWS IoT Wireless resources

By default, if you create the IAM role, `IoTWirelessLogsRole`, as
described in [Create logging role and policy for
AWS IoT Wireless monitoring](create-logging-role-policy.md "create-logging-role-policy.md"), you'll see CloudWatch logs in the
AWS Management Console that have a default log level of `ERROR`. To change the
default log level for all your resources or for specific resources, you
can configure the logging settings.

To configure logging for AWS IoT Wireless resources, you can use the AWS IoT console,
the AWS IoT Wireless API, or the AWS CLI. The following section shows the various
logging API and how to use them to configure logging for your wireless resources.

###### Topics

- [Configure log levels of
  resources (console)](#configure-logging-console "#configure-logging-console")
- [Configure log levels of resources (CLI)](#configure-logging-api "#configure-logging-api")
- [Next Steps](#configure-logging-next-steps "#configure-logging-next-steps")

## Configure log levels of

resources (console)

To configure logging for AWS IoT Wireless resources from the console, first
go to the [AWS IoT Core for LoRaWAN hub](https://console.aws.amazon.com/iot/home#/wireless/landing "https://console.aws.amazon.com/iot/home#/wireless/landing")
page, and then perform the following steps.

1. Go to the hub page of the resources for which you want to configure
   logging. Depending on whether you want to monitor wireless devices, gateways,
   or FUOTA tasks, go to the [Devices hub](https://console.aws.amazon.com/iot/home#/wireless/devices "https://console.aws.amazon.com/iot/home#/wireless/devices"), [Gateways hub](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways"), or the [FUOTA tasks](https://console.aws.amazon.com/iot/home#/wireless/fuotaTasks "https://console.aws.amazon.com/iot/home#/wireless/fuotaTasks") page.
2. Choose the **Settings** tabs of the resources for
   which you want to configure logging, and specify whether to configure logging
   at the account level, or to configure the log-level overrides at the
   resource level.
3. If you choose the **Manage account log levels**
   setting, it goes to the [Manage service logs](https://console.aws.amazon.com/iot/home#/settings/logging "https://console.aws.amazon.com/iot/home#/settings/logging") page in the
   AWS IoT console where you can manage logging for your resources at the
   account level. For information about account-level logging, see
   [Configure AWS IoT
   logging](../../../iot/latest/developerguide/configure-logging.md "../../../iot/latest/developerguide/configure-logging.md") in the _AWS IoT Core developer guide_.
4. If you choose the **Manage log level overrides**
   setting, you can add the event type for which you want to configure logging,
   and the log levels for the events. The log levels can be error (less verbose)
   or informational (more detailed), or you can disable logging. For information
   about the event types for various wireless resources, see [Events and resource types](cwl-format.md#cwl-format-events-resources "cwl-format.md#cwl-format-events-resources").

## Configure log levels of resources (CLI)

This section describes how to configure log levels for AWS IoT Wireless
resources by using the API or AWS CLI. To use the AWS CLI, you must create the
following IAM policy to perform the logging API operations. You also need
the Amazon Resource Name (ARN) of the role that you want to use. If you
need to create a role to use for logging, see [Create logging role and policy for
AWS IoT Wireless monitoring](create-logging-role-policy.md "create-logging-role-policy.md").

###### Topics

- [Sample IAM policy for
  AWS IoT Wireless logging API actions](#logging-api-roles "#logging-api-roles")
- [How to configure logging using
  the AWS CLI](#configure-logging-api-how "#configure-logging-api-how")

### Sample IAM policy for

AWS IoT Wireless logging API actions

Before you use the CLI, you must create the IAM policy for the API operations
for which you want to run the CLI commands.

You can use the following API actions to configure logging of resources. The
table also shows a sample IAM policy that you must create for using the API
actions. The following section describes how you can use the APIs to configure
log levels of your resources.

| Logging API actions                                                                                                                                                         | API name                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                           | Sample IAM policy |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [GetLogLevelsByResourceTypes](../../2020-11-22/apireference/API_GetLogLevelsByResourceTypes.md "../../2020-11-22/apireference/API_GetLogLevelsByResourceTypes.md")          | Returns current default log levels, or log levels by<br>resource types, which can include log options for wireless<br>devices, wireless gateways, or FUOTA tasks.                                                                                                                                                                                                                                                                                            | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iotwireless:GetLogLevelsByResourceTypes"<br>],<br>"Resource": [<br>"*"<br>]<br>}<br>]<br>}`<br>``                                                                                                                                                                                         |
| [GetResourceLogLevel](../../2020-11-22/apireference/API_GetResourceLogLevel.md "../../2020-11-22/apireference/API_GetResourceLogLevel.md")                                  | Returns the log-level override for a given resource<br>identifier and resource type. The resource can be a wireless<br>device, a wireless gateway, or a FUOTA task.                                                                                                                                                                                                                                                                                          | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iotwireless:GetResourceLogLevel"<br>],<br>"Resource": [<br>"arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/012bc537-ab12-cd3a-d00e-1f0e20c1204a"<br>]<br>}<br>]<br>}`<br>``                                                                                                    |
| [PutResourceLogLevel](../../2020-11-22/apireference/API_PutResourceLogLevel.md "../../2020-11-22/apireference/API_PutResourceLogLevel.md")                                  | Sets the log-level override for a given resource<br>identifier and resource type. The resource can be a wireless<br>gateway, a wireless device, or a FUOTA task.<br>NoteThis API has a limit of 200 log-level overrides per<br>account.                                                                                                                                                                                                                      | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iotwireless:PutResourceLogLevel"<br>],<br>"Resource": [<br>"arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/012bc537-ab12-cd3a-d00e-1f0e20c1204a"<br>]<br>}<br>]<br>}`<br>``                                                                                                    |
| [ResetAllResourceLogLevels](../../2020-11-22/apireference/API_ResetAllResourceLogLevels.md "../../2020-11-22/apireference/API_ResetAllResourceLogLevels.md")                | Removes the log-level overrides for all resources, which<br>includes wireless gateways, wireless devices, and FUOTA<br>tasks.<br>NoteThis API doesn't affect the log levels that are set<br>using the `UpdateLogLevelsByResourceTypes`<br>API.                                                                                                                                                                                                               | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iotwireless:ResetAllResourceLogLevels"<br>],<br>"Resource": [<br>"arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/*",<br>"arn:aws:iotwireless:us-east-1:123456789012:WirelessGateway/*",<br>"arn:aws:iotwireless:us-east-1:123456789012:FuotaTask/*"<br>]<br>}<br>]<br>}`<br>`` |
| [ResetResourceLogLevel](../../2020-11-22/apireference/API_ResetResourceLogLevel.md "../../2020-11-22/apireference/API_ResetResourceLogLevel.md")                            | Removes the log-level override for a given resource<br>identifier and resource type. The resource can be a wireless<br>gateway or a wireless device.                                                                                                                                                                                                                                                                                                         | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iotwireless:ResetResourceLogLevel"<br>],<br>"Resource": [<br>"arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/012bc537-ab12-cd3a-d00e-1f0e20c1204a"<br>]<br>}<br>]<br>}`<br>``                                                                                                  |
| [UpdateLogLevelsByResourceTypes](../../2020-11-22/apireference/API_UpdateLogLevelsByResourceTypes.md "../../2020-11-22/apireference/API_UpdateLogLevelsByResourceTypes.md") | Set default log level, or log levels by resource types.<br>You can use this API for log options for wireless devices,<br>wireless gateways, or FUOTA tasks, and control the log<br>messages that'll be displayed in CloudWatch.<br>NoteEvents are optional and the event type is tied to the<br>resource type. For more information, see [Events and resource types](cwl-format.md#cwl-format-events-resources "cwl-format.md#cwl-format-events-resources"). | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iotwireless:UpdateLogLevelsByResourceTypes"<br>],<br>"Resource": [<br>"*"<br>]<br>}<br>]<br>}`<br>``                                                                                                                                                                                      |

You've learned how to create a logging role to log your AWS IoT Wireless
resources. By default, logs have a log level of `ERROR`, so if you
want to see only error information, go to [View CloudWatch AWS IoT Wireless log entries](cwl-format.md "cwl-format.md") to monitor your wireless resources by viewing the log
entries.

If you want more information in the log entries, you can configure the default
log level for your resources or for different event types, such as setting the
log level to `INFO`. For information about configuring logging for
your resources, see [Configure resource logging for
AWS IoT Wireless resources](configure-resource-logging.md "configure-resource-logging.md").

### How to configure logging using

the AWS CLI

The API actions can be categorized into the following types depending on
whether you want to configure log levels for all resources or for specific
resources:

- API actions `GetLogLevelsByResourceTypes` and
  `UpdateLogLevelsByResourceTypes` can retrieve and update
  the log levels for all resources in your account that are of a specific
  type, such as a wireless gateway, FUOTA task, or a LoRaWAN or Sidewalk
  device.
- API actions `GetResourceLogLevel`,
  `PutResourceLogLevel`, and
  `ResetResourceLogLevel` can retrieve, update, and reset
  log levels of individual resources that you specify using a resource
  identifier.
- API action `ResetAllResourceLogLevels` resets the log-level
  override to `null` for all resources for which you specified
  a log-level override using the `PutResourceLogLevel`
  API.

###### To use the CLI to configure resource-specific logging for AWS IoT

###### Note

You can also perform this procedure with the API by using the methods
in the AWS API that correspond to the CLI commands shown here.

1. By default, all resources have log level set to `ERROR`. To
   set the default log levels, or log levels by resource types for all
   resources in your account, use the [**update-log-levels-by-resource-types**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-log-levels-by-resource-types.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-log-levels-by-resource-types.html")
   command. The following example shows how you can create a JSON file,
   `Input.json`, and provide it as an input to the CLI
   command. You can use this command to selectively disable logging or
   override the default log level for specific types of resources and
   events.

```
{
    "DefaultLogLevel": "INFO",
    "FuotaTaskLogOptions":
     [
        {
        "Type": "LoRaWAN",
            "LogLevel": "INFO",
            "Events": [
                {
                    "Event": "Fuota",
                    "LogLevel": "DISABLED"
                },
            ]
        },
    ],
    "WirelessDeviceLogOptions":
     [
        {
         "Type": "Sidewalk",
         "LogLevel": "INFO",
         "Events":
          [
            {
              "Event": "Registration",
              "LogLevel": "DISABLED"
            }
          ]
        },
        {
         "Type": "LoRaWAN",
         "LogLevel": "INFO",
         "Events":
          [
            {
             "Event": "Join",
             "LogLevel": "DISABLED"
            },
            {
             "Event": "Rejoin",
             "LogLevel": "ERROR"
            }
          ]
        }
      ],
      "WirelessGatewayLogOptions":
      [
        {
         "Type": "LoRaWAN",
         "LogLevel": "INFO",
         "Events":
          [
            {
             "Event": "CUPS_Request",
             "LogLevel": "DISABLED"
            },
            {
              "Event": "Certificate",
              "LogLevel": "ERROR"
            }
          ]
        }
      ]
}
```

where:

**FuotaTaskLogOptions**

The list of log options for a FUOTA task. Each log option
includes the FUOTA task type (LoRaWAN), and a list of FUOTA
task event log options. Each FUOTA task event log option can
optionally include the event type and its log level.

**WirelessDeviceLogOptions**

The list of log options for a wireless device. Each log
option includes the wireless device type (Sidewalk or
LoRaWAN), and a list of wireless device event log options.
Each wireless device event log option can optionally include
the event type and its log level.

**WirelessGatewayLogOptions**

The list of log options for a wireless gateway. Each log
option includes the wireless gateway type (LoRaWAN), and a
list of wireless gateway event log options. Each wireless
gateway event log option can optionally include the event
type and its log level.

**DefaultLogLevel**

The log level to use for all your resources. Valid values
are: `ERROR`, `INFO`, and
`DISABLED`. The default value is
`INFO`.

**LogLevel**

The log level you want to use for individual resource
types and events. These log levels override the default log
level, such as the log level `INFO` for the
LoRaWAN gateway, and log levels `DISABLED` and
`ERROR` for the two event types.

Run the following command to provide the `Input.json` file
as input to the command. This command doesn't produce any output.

```
aws iotwireless update-log-levels-by-resource-types \
    --cli-input-json Input.json
```

If you want to remove the log options for wireless devices and
wireless gateways, run the following command.

```
{
    "DefaultLogLevel":"DISABLED",
    "WirelessDeviceLogOptions": [],
    "WireslessGatewayLogOptions":[]
}
```

2. The **update-log-levels-by-resource-types** command
   doesn't return any output. Use the [**get-log-levels-by-resource-types**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-log-levels-by-resource-types.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-log-levels-by-resource-types.html")
   command to retrieve resource-specific logging information. The command
   returns the default log level, and the wireless device and wireless
   gateway log options.

###### Note

The **get-log-levels-by-resource-types** command
can't directly retrieve the log levels in the CloudWatch console. You can
use the **get-log-levels-by-resource-types** command
to get the latest log-level information that you've specified for
your resources using the
**update-log-levels-by-resource-types**
command.

```
aws iotwireless get-log-levels-by-resource-types
```

When you run the following command, it returns the latest logging
information you specified with
**update-log-levels-by-resource-types**. For example,
if you remove the wireless device and FUOTA task log options, then
running the **get-log-levels-by-resource-types** will
return these values as `null`.

```
{
    "DefaultLogLevel": "INFO",
    "WirelessDeviceLogOptions": null,
    "FuotaTaskLogOptions": null,
     "WirelessGatewayLogOptions":
      [
        {
         "Type": "LoRaWAN",
         "LogLevel": "INFO",
         "Events":
          [
            {
             "Event": "CUPS_Request",
             "LogLevel": "DISABLED"
            },
            {
              "Event": "Certificate",
              "LogLevel": "ERROR"
            }
          ]
        }
      ]
}
```

3.  To control log levels for individual wireless gateways or wireless
    device resources, use the following CLI commands:

        * [**put-resource-log-level**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/put-resource-log-level.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/put-resource-log-level.html")
        * [**get-resource-log-level**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-resource-log-level.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-resource-log-level.html")
        * [**reset-resource-log-level**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/reset-resource-log-level.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/reset-resource-log-level.html")

    For an example for when to use these CLIs, say that you have a large
    number of wireless devices or gateways in your account that are being
    logged. If you want to troubleshoot errors for only some of your
    wireless devices, you can disable logging for all wireless devices by
    setting the `DefaultLogLevel` to `DISABLED`, and
    use the **put-resource-log-level** to set the
    `LogLevel` to `ERROR` for only those devices
    in your account.

```
aws iotwireless put-resource-log-level \
    --resource-identifier `<wireless-device-id>`
    --resource-type WirelessDevice
    --log-level ERROR
```

In this example, the command sets the log level to `ERROR`
only for the specified wireless device resource and the logs for all
other resources are disabled. This command doesn't produce any output.
To retrieve this information and verify that the log levels were set,
use the **get-resource-log-level** command. 4. In the previous step, after you've debugged the issue and resolved the
error, you can run the **reset-resource-log-level**
command to reset the log level for that resource to `null`.
If you used the `put-resource-log-level` command to set the
log-level override for more than one FUOTA task, wireless device, or
gateway resource, such as for troubleshooting errors for multiple
devices, you can reset the log-level overrides back to `null`
for all those resources using the [**reset-all-resource-log-levels**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/reset-all-resource-log-levels.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/reset-all-resource-log-levels.html")
command.

```
aws iotwireless reset-all-resource-log-levels
```

This command doesn't produce any output. To retrieve the logging
information for the resources, run the
**get-resource-log-level** command.

## Next Steps

You've learned how to create the logging role and use the AWS IoT Wireless
API to configure logging for your AWS IoT Core for LoRaWAN resources. Next, to learn about
monitoring your log entries, go to [Monitor AWS IoT Wireless using CloudWatch Logs](cloud-watch-logs.md "cloud-watch-logs.md").
