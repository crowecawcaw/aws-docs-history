# Create a network analyzer

configuration

Before you can monitor your wireless gateways or wireless devices, you must create
a network analyzer configuration. When creating the configuration, you only need to
specify a configuration name. You can customize your configuration settings and add
the resources that you want to monitor to your configuration even after it's
created. The configuration settings determine the trace messaging information that
you'll receive for those resources.

Depending on the resources you want to monitor and the level of information you
want to receive for them, you may want to create multiple configurations. For
example, you can create a configuration that displays only error information for a
set of gateways in your AWS account. You can also create a configuration that
displays all information about a wireless device that you want to monitor.

The following sections show the various configuration settings and how to create
your configuration.

## Configuration

settings

When creating or updating your network analyzer configuration, you can also
customize the following parameters to filter the log stream information.

- ###### Frame info

This setting is the frame info for your wireless device resources
for trace messages. The frame info can be used to debug the
communication between your network server and the end devices. It is
enabled by default.

- ###### Log levels

You can view Info or Error logs, or you can turn off
logging.

    + ###### Info


    Logs with a log level of **Info** are
     more verbose and contain both error log streams and
     informational log streams. The informational logs can be
     used to view changes to the state of a device or
     gateway.


    ###### Note

    Collecting more verbose log streams can incur additional
     costs. For more information about pricing, see [AWS IoT Core
     pricing](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").
    + ###### Error


    Logs with a log level of **Error** are
     less verbose and display only error information. You can use
     these logs when an application has an error, such as a
     device connection error. By using the information from the
     log stream, you can identify and troubleshoot errors for
     resources in your fleet.

## Create a

configuration using the console

You can create a network analyzer configuration and customize the optional
parameters using the AWS IoT console or the AWS IoT Wireless API. You can also
create multiple configurations and later delete any configurations that you're
no longer using.

###### Create a network analyzer configuration

1. Open the
   [Network Analyzer hub of the AWS IoT
   console](https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer "https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer") and choose **Create
   configuration**.
2. Specify the configuration settings.
   - ###### Name, description, and tags

   Specify a unique **Configuration name**
   that
   only
   contains letters, numbers, hyphens, or
   underscores. Use the optional
   **Description** field to provide
   information about the configuration, and the
   **Tags** field to add key-value pairs
   of metadata about the configuration. For more information
   about naming and describing your resources, see [Describing your AWS IoT Wireless
   resources](getting-started.md#iotwireless-describe-resources "getting-started.md#iotwireless-describe-resources").
   - ###### Configuration settings

   Choose whether to disable frame info, and use
   **Select log levels** to choose the log
   levels that you want to use for your trace message logs.
   Choose **Next**.

3. Add resources to your configuration. You can either add your resources
   now or choose **Create** and then add your resources
   later. To add resources later, choose
   **Create**.

In the **Network Analyzer hub page**, you'll see the
configuration that you created along with its settings. To view the
details of the new configuration, choose the configuration name.

###### Delete your network analyzer configuration

You can create multiple network analyzer configurations depending on the
resources you want to monitor and the level of trace messaging information that
you want to receive for them.

###### To remove configurations from the console

1. Go to the [Network Analyzer hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer "https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer") and choose the
   configuration that you want to remove.
2. Choose **Actions**, and then choose
   **Delete**.

## Create a

configuration using the API

To create a network analyzer configuration using the API, use the [CreateNetworkAnalyzerConfiguration](../../2020-11-22/apireference/API_CreateNetworkAnalyzerConfiguration.md "../../2020-11-22/apireference/API_CreateNetworkAnalyzerConfiguration.md") API operation or the [create-network-analyzer-configuration](../../../cli/latest/reference/iotwireless/create-network-analyzer-configuration.md "../../../cli/latest/reference/iotwireless/create-network-analyzer-configuration.md") CLI command.

When you create your configuration, you only need to specify a configuration
name. You can also use this API operation to specify the configuration settings
and add resources when creating the configuration. Alternatively, you can
specify them later by using the [UpdateNetworkAnalyzerConfiguration](../../2020-11-22/apireference/API_UpdateNetworkAnalyzerConfiguration.md "../../2020-11-22/apireference/API_UpdateNetworkAnalyzerConfiguration.md") API operation or the [update-network-analyzer-configuration](../../../cli/latest/reference/iotwireless/update-network-analyzer-configuration.md "../../../cli/latest/reference/iotwireless/update-network-analyzer-configuration.md") CLI.

- ###### Create a configuration

When you create your configuration, you must specify a name. For
example, the following command creates a configuration by providing
only a name and an optional description. By default, the
configuration has frame info activated and uses a log level of
`INFO`.

```
aws iotwireless create-network-analyzer-configuration \
    --configuration-name My_Network_Analyzer_Config \
    --description "My first network analyzer configuration"
```

Running this command displays the ARN and ID of your network analyzer
configuration.

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:NetworkAnalyzerConfiguration/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
}
```

- ###### Create configuration with resources

To customize the configuration settings, use the
`trace-content` parameter. To add resources, use the
`WirelessDevices` and `WirelessGateways`
parameters to specify the gateways, devices, or both that you want
to add to your configuration. For example, the following command
customizes the configuration settings and adds to your configuration
the wireless resources, specified by their
`WirelessGatewayID` and
`WirelessDeviceID`.

```
aws iotwireless create-network-analyzer-configuration \
    --configuration-name My_NetworkAnalyzer_Config \
    --trace-content WirelessDeviceFrameInfo=DISABLED,LogLevel="ERROR" \
    --wireless-gateways "12345678-a1b2-3c45-67d8-e90fa1b2c34d" "90123456-de1f-2b3b-4c5c-bb1112223cd1"
    --wireless-devices "1ffd32c8-8130-4194-96df-622f072a315f"
```

The following example shows the output of running the command:

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:NetworkAnalyzerConfiguration/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
}
```

###### List network analyzer configurations

You can create multiple network analyzer configurations depending on the
resources that you want to monitor and the level of detail of trace
messaging information that you want to receive for the resources. After you
create these configurations, you can use the [ListNetworkAnalyzerConfigurations](../../2020-11-22/apireference/API_ListNetworkAnalyzerConfigurations.md "../../2020-11-22/apireference/API_ListNetworkAnalyzerConfigurations.md") API operation or the [list-network-analyzer-configuration](../../../cli/latest/reference/iotwireless/list-network-analyzer-configuration.md "../../../cli/latest/reference/iotwireless/list-network-analyzer-configuration.md") CLI command to get a list
of these configurations.

```
aws iotwireless list-network-analyzer-configurations
```

Running this command displays all the network analyzer configurations in your
AWS account. You can also use the `max-results` parameter to
specify how many configurations you want to display. The following shows the
output of running this command.

```
{
   "NetworkAnalyzerConfigurationList": [
      {
         "Arn": "arn:aws:iotwireless:us-east-1:123456789012:NetworkAnalyzerConfiguration/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
         "Name": "My_Network_Analyzer_Config1"
      },
      {
         "Arn": "arn:aws:iotwireless:us-east-1:123456789012:NetworkAnalyzerConfiguration/90123456-a1a2-9a87-65b4-c12bf3c2d09a",
         "Name": "My_Network_Analyzer_Config2"
      }
   ]
}
```

###### Delete your network analyzer configuration

You can delete a configuration that you're no longer using with the [DeleteNetworkAnalyzerConfiguration](../../2020-11-22/apireference/API_DeleteNetworkAnalyzerConfiguration.md "../../2020-11-22/apireference/API_DeleteNetworkAnalyzerConfiguration.md") API operation or the [delete-network-analyzer-configuration](../../../cli/latest/reference/iotwireless/delete-network-analyzer-configuration.md "../../../cli/latest/reference/iotwireless/delete-network-analyzer-configuration.md") CLI command.

```
aws iotwireless delete-network-analyzer-configuration \
    --configuration-name My_NetworkAnalyzer_Config
```

Running this command doesn't produce any output. To see the available
configurations, you can use the `ListNetworkAnalyzerConfigurations`
API operation.

## Next steps

Now that you've created a network analyzer configuration, you can add
resources to your configuration or update your configuration settings. For more
information, see [Add resources and update the network
analyzer configuration](network-analyzer-resources.md "network-analyzer-resources.md").
