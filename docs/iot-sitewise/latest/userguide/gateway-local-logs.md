# Use service logs in AWS IoT SiteWise

SiteWise Edge gateway devices include service log files to help debug issues. The following sections will help you find and utilize the service log files for the AWS IoT SiteWise OPC UA Collector
and AWS IoT SiteWise Publisher components.

## AWS IoT SiteWise OPC UA Collector service log file

The AWS IoT SiteWise OPC UA Collector component uses the following log file.

Linux

```
``/greengrass/v2``/logs/aws.iot.SiteWiseEdgeCollectorOpcua.log
```

Windows

```
`C:\greengrass\v2`\logs\aws.iot.SiteWiseEdgeCollectorOpcua.log
```

###### To view this component's logs

- Run the following command on the core device to view this component's log file in real
  time. Replace `/greengrass/v2` or `C:\greengrass\v2` with the path to the AWS IoT Greengrass root folder.

Linux

```
sudo tail -f ``/greengrass/v2``/logs/aws.iot.SiteWiseEdgeCollectorOpcua.log
```

Windows (PowerShell)

```
Get-Content `C:\greengrass\v2`\logs\aws.iot.SiteWiseEdgeCollectorOpcua.log -Tail 10 -Wait
```

## AWS IoT SiteWise Publisher service log file

The AWS IoT SiteWise Publisher component uses the following log file.

Linux

```
``/greengrass/v2``/logs/aws.iot.SiteWiseEdgePublisher.log
```

Windows

```
`C:\greengrass\v2`\logs\aws.iot.SiteWiseEdgePublisher.log
```

###### To view this component's logs

- Run the following command on the core device to view this component's log file in real
  time. Replace `/greengrass/v2` or `C:\greengrass\v2` with the path to the AWS IoT Greengrass root folder.

Linux

```
sudo tail -f ``/greengrass/v2``/logs/aws.iot.SiteWiseEdgePublisher.log
```

Windows (PowerShell)

```
Get-Content `C:\greengrass\v2`\logs\aws.iot.SiteWiseEdgePublisher.log -Tail 10 -Wait
```
