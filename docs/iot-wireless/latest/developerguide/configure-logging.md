# Configure Logging for AWS IoT Wireless

Before you can monitor and log AWS IoT Wireless activity, first enable
logging for your AWS IoT Wireless resources. You can enable logging by
using the AWS IoT console, the AWS IoT Wireless API, or the AWS CLI.

When starting to monitor AWS IoT Wireless resources, you can use the default
configuration. To do this, you can skip this topic and proceed to [Monitor AWS IoT Wireless using CloudWatch Logs](cloud-watch-logs.md "cloud-watch-logs.md") to monitor your logs.
After reviewing the initial logs, you can change the default log level to
`ERROR`, which is less verbose. You can then set a more verbose,
resource-specific log level on resources that might need more attention. Log levels can
be changed whenever you want.

## AWS IoT Wireless resources and log

levels

Before you use the console or the API, use the following table to learn about the
different log levels and the resources that you can configure logging for. The table
shows parameters that you see in the CloudWatch logs when you monitor the resources. How
you configure the logging for your resources will determine the logs you see in the
console.

For information about what a sample CloudWatch logs looks like and how you can use these
parameters to log useful information about the AWS IoT Wireless resources, see
[View CloudWatch AWS IoT Wireless log entries](cwl-format.md "cwl-format.md").

| Log levels and resources | Name                                                                                                                  | Possible values                                                                                                                                                                                                                                                               | Description |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `logLevel`               | `INFO`, `ERROR`, or<br>`DISABLED`                                                                                     | • `ERROR`: Displays any error that causes an<br>operation to fail. Logs include only `ERROR`<br>information.<br>• `INFO`: Provides high-level information<br>about the flow of things. Logs include `INFO`<br>and `ERROR` information.<br>• `DISABLED`: Disables all logging. |
| `resource`               | `WirelessGateway`, `WirelessDevice`, or<br>`FuotaTask`                                                                | The type of the resource, which can be<br>`WirelessGateway`, `WirelessDevice`,<br>or `FuotaTask`.                                                                                                                                                                             |
| `wirelessGatewayType`    | `LoRaWAN`                                                                                                             | The type of the wireless gateway, when `resource` is<br>`WirelessGateway`, which is always<br>`LoRaWAN`.                                                                                                                                                                      |
| `wirelessDeviceType`     | `LoRaWAN` or `Sidewalk`                                                                                               | The type of the wireless device, when `resource` is<br>`WirelessDevice`, which can be `LoRaWAN`<br>or `Sidewalk`.                                                                                                                                                             |
| `fuotaTaskType`          | `LoRaWAN`                                                                                                             | The type of the FUOTA task, when `resource` is<br>`fuotaTask`, which is always<br>`LoRaWAN`.                                                                                                                                                                                  |
| `wirelessGatewayId`      | -                                                                                                                     | The identifier of the wireless gateway, when<br>`resource` is `WirelessGateway`.                                                                                                                                                                                              |
| `wirelessDeviceId`       | -                                                                                                                     | The identifier of the wireless device, when `resource`<br>is `WirelessDevice`.                                                                                                                                                                                                |
| `fuotaTaskId`            | -                                                                                                                     | The identifier of the FUOTA task, when `resource` is<br>`FuotaTask`.                                                                                                                                                                                                          |
| `event`                  | `Join`, `Rejoin`,<br>`Registration`, `Uplink_data`,<br>`Downlink_data`, `CUPS_Request`,<br>`Certificate`, and `Fuota` | The type of event being logged, which depends on whether the<br>resource that you're logging is a wireless device, a wireless<br>gateway, or a FUOTA task. For more information, see [View CloudWatch AWS IoT Wireless log entries](cwl-format.md "cwl-format.md").           |

The following topic shows how to create a logging role and policy for
AWS IoT Wireless resources.

###### Topics

- [Create logging role and policy for
  AWS IoT Wireless monitoring](create-logging-role-policy.md "create-logging-role-policy.md")
- [Configure resource logging for
  AWS IoT Wireless resources](configure-resource-logging.md "configure-resource-logging.md")
