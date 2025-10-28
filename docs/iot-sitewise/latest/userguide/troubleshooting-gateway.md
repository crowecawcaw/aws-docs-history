# Troubleshooting a SiteWise Edge gateway

Troubleshoot common AWS IoT SiteWise Edge gateway issues by exploring relevant topics.

You can also view CloudWatch metrics reported by your SiteWise Edge gateways to troubleshoot issues with
connectivity or data streams. For more information, see [Monitor AWS IoT SiteWise with Amazon CloudWatch metrics](monitor-cloudwatch-metrics.md "monitor-cloudwatch-metrics.md").

###### Topics

- [Configure and access SiteWise Edge gateway logs](#configure-gateway-logs "#configure-gateway-logs")
- [Troubleshooting SiteWise Edge gateway issues](#troubleshoot-gateway-issues "#troubleshoot-gateway-issues")
- [Troubleshooting the AWS IoT SiteWise Edge application on
  Siemens Industrial Edge](#troubleshoot-siemens-app "#troubleshoot-siemens-app")
- [Troubleshooting open-source integrations at the Edge](#open-source-troubleshooting "#open-source-troubleshooting")
- [Troubleshooting AWS IoT Greengrass issues](#troubleshoot-greengrass-issues "#troubleshoot-greengrass-issues")

## Configure and access SiteWise Edge gateway logs

Before you can view SiteWise Edge gateway logs, you must configure your SiteWise Edge gateway to send
logs to Amazon CloudWatch Logs or store logs on the local file system.

- Use CloudWatch Logs if you want to use the AWS Management Console to view your SiteWise Edge gateway's log files.
  For more information, see [Use Amazon CloudWatch Logs](gateway-cloudwatch-logs.md "gateway-cloudwatch-logs.md").
- Use local file system logs if you want to use the command line or local software to
  view your SiteWise Edge gateway's log files. For more information, see [Use service logs in AWS IoT SiteWise](gateway-local-logs.md "gateway-local-logs.md").

## Troubleshooting SiteWise Edge gateway issues

Use the following information to troubleshoot SiteWise Edge gateway issues.

###### Issues

- [Unable to deploy packs to SiteWise Edge gateways](#gateway-issue-ggv2-packs "#gateway-issue-ggv2-packs")
- [AWS IoT SiteWise doesn't receive data from OPC UA servers](#gateway-issue-data-streams "#gateway-issue-data-streams")
- [No data shows in the dashboard](#gateway-issue-no-data "#gateway-issue-no-data")
- ["Could not find or load main class" showing up in
  the aws.iot.SiteWiseEdgePublisher logs at /greengrass/v2/logs error](#troubleshoot-java-issues "#troubleshoot-java-issues")
- [I see 'SESSION_TAKEN_OVER' or
  'com.aws.greengrass.mqttclient.MqttClient: Failed to publish the message via Spooler and
  will retry.' in the logs](#sa-troubleshoot-multiple-use "#sa-troubleshoot-multiple-use")
- [I see 'com.aws.greengrass.deployment.IotJobsHelper:
  No deployment job found.' or 'Deployment result already reported.' in the logs](#sa-troubleshoot-reuse "#sa-troubleshoot-reuse")
- [I see a 'SYNC_FAILED' status
  when attempting to configure the timestamp setting in a property group on an OPC UA data
  source](#troubleshoot-gateway-sync-failed-timestamp "#troubleshoot-gateway-sync-failed-timestamp")
- [Converted data types are not included](#troubleshoot-data-conversion "#troubleshoot-data-conversion")
- [Trust store issues](#troubleshoot-trust-stores "#troubleshoot-trust-stores")
- [Proxy-enabled installation
  issues](#troubleshoot-proxy-during-installation "#troubleshoot-proxy-during-installation")

### Unable to deploy packs to SiteWise Edge gateways

If the AWS IoT Greengrass nucleus component (`aws.greengrass.Nucleus`) is out of date, you
might not be able to deploy packs to your SiteWise Edge gateway. You can use the AWS IoT Greengrass V2 console to
upgrade the AWS IoT Greengrass nucleus component.

###### To upgrade the AWS IoT Greengrass nucleus component (console)

1. Navigate to the [AWS IoT Greengrass
   console](https://console.aws.amazon.com/greengrassIntro "https://console.aws.amazon.com/greengrassIntro").
2. In the navigation pane, under **AWS IoT Greengrass**, choose
   **Deployments**.
3. In the **Deployments** list, select the deployment that you want to
   revise.
4. Choose **Revise**.
5. On the **Specify target** page, choose
   **Next**.
6. On the **Select components** page, under **Public
   components**, in the search box, enter
   `aws.greengrass.Nucleus`, and then select
   **aws.greengrass.Nucleus**.
7. Choose **Next**.
8. On the **Configure components** page, choose
   **Next**.
9. On the **Configure advanced settings** page, choose
   **Next**.
10. On the **Review** page, choose **Deploy**.

### AWS IoT SiteWise doesn't receive data from OPC UA servers

If your AWS IoT SiteWise assets aren't receiving data sent by your OPC UA servers, you can search
your SiteWise Edge gateway's logs to troubleshoot issues. Look for info-level
`swPublisher` logs that contain the following message.

```
Emitting diagnostic name=PublishError.`SomeException`
```

Based on the type of `SomeException` in the log, use the
following exception types and corresponding issues to troubleshoot your SiteWise Edge
gateway:

- **ResourceNotFoundException** – Your OPC UA
  servers are sending data that doesn't match a property alias for any asset. This
  exception can occur in two cases:
  - Your property aliases don't exactly match your OPC UA variables, including any
    source prefix you defined. Check that your property aliases and source prefixes are
    correct.
  - You haven't mapped your OPC UA variables to asset properties. For more
    information, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

  If you already mapped all of the OPC UA variables that you want
  in AWS IoT SiteWise, you can filter which OPC UA variables the SiteWise Edge gateway sends. For more
  information, see [Use OPC UA node filters in SiteWise Edge](opc-ua-node-filters.md "opc-ua-node-filters.md").

- **InvalidRequestException** – Your OPC UA
  variables data types don't match your asset property data types. For example, if an OPC
  UA variable has an integer data type, your corresponding asset property must be integer
  data type. A double-type asset property can't receive OPC UA integer values. To fix this
  issue, define new properties with the correct data types.
- **TimestampOutOfRangeException** – Your SiteWise Edge
  gateway is sending data that is outside the range that AWS IoT SiteWise accepts. AWS IoT SiteWise rejects
  any data points with timestamps earlier than 7 days in the past or newer than 5 minutes
  in the future. If your SiteWise Edge gateway lost power or connection to the AWS Cloud, you
  might need to clear your SiteWise Edge gateway's cache.
- **ThrottlingException** or **LimitExceededException** – Your request exceeded an AWS IoT SiteWise service
  quota, such as rate of data points ingested or request rate for asset property data API
  operations. Check that your configuration doesn't exceed the [AWS IoT SiteWise quotas](endpoints-and-quotas.md#quotas "endpoints-and-quotas.md#quotas").

### No data shows in the dashboard

If there is no data shown in your dashboard, the **Publisher
configuration** and the **Data Source** of the SiteWise Edge gateway
may be out of sync. If they are out of sync, updating the name of the data source may
expedite the sync from the cloud to the edge, fixing the Out of sync error.

###### To update the name of a data source

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Select the SiteWise Edge gateway connected to the dashboard.
4. Under **Data sources**, select **Edit**.
5. Select a new source **Name**, and select **Save**
   to confirm your change.
6. Verify your changes by confirming the the data source name has been updated in the
   **Data sources** table.

### "Could not find or load main class" showing up in

the aws.iot.SiteWiseEdgePublisher logs at /greengrass/v2/logs error

If you see this error, you may need to update the java version of your SiteWise Edge
gateway.

- From a terminal, run the following command:

```
java -version
```

The version of java your SiteWise Edge gateway is running with will show up under
`OpenJDK Runtime Environment`. You'll see a response like the
following:

```
openjdk version "11.0.20" 2023-07-18 LTS
OpenJDK Runtime Environment Corretto011.0.20.8.1 (build 11.0.20+8-LTS
OpenJDK 64-Bit Server VM Corretto-11.0.20.8.1 (build 11.0.20+8-LTS, mixed node)
```

If you are running Java version 11.0.20.8.1 you must update the IoT SiteWise Publisher
pack to version 2.4.1 or newer. Only java version 11.0.20.8.1 is affected, environments with
other java versions can continue to use older versions of the IoT SiteWise Publisher
component. For more information about updating a component pack, see [Change the version of SiteWise Edge gateway
component packs](manage-gateways-ggv2.md#manage-gateway-update-packs "manage-gateways-ggv2.md#manage-gateway-update-packs").

### I see 'SESSION_TAKEN_OVER' or

'com.aws.greengrass.mqttclient.MqttClient: Failed to publish the message via Spooler and
will retry.' in the logs

If you see a warning that includes `SESSION_TAKEN_OVER` or an error that
includes `com.aws.greengrass.mqttclient.MqttClient: Failed to publish the message via
 Spooler and will retry.` in your logs at
`/greengrass/v2/logs/greengrass.log`, you may be trying to use the same
configuration file for multiple SiteWise Edge gateways on multiple devices. Each SiteWise Edge gateway
needs a unique configuration file to connect to your AWS account.

### I see 'com.aws.greengrass.deployment.IotJobsHelper:

No deployment job found.' or 'Deployment result already reported.' in the logs

If you see `com.aws.greengrass.deployment.IotJobsHelper: No deployment job
 found.` or `Deployment result already reported.` in your logs at
`/greengrass/v2/logs/greengrass.log`, you may be trying to reuse the same
configuration file.

There are multiple solutions:

- If you want to reuse the configuration file, do the following:
  1.  Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
  2.  In the navigation pane, choose **Edge gateways**.
  3.  Choose the SiteWise Edge gateway you want to reuse.
  4.  Choose the **Updates** tab.
  5.  Select a different Publisher version and choose
      **Deploy**.

Follow the steps in [Create a gateway for Siemens Industrial Edge](sa-create-config.md "sa-create-config.md")
to create a new configuration file.

### I see a 'SYNC_FAILED' status

when attempting to configure the timestamp setting in a property group on an OPC UA data
source

When AWS IoT SiteWise updated the OPC UA collector component for AWS IoT Greengrass in version 2.5.0, we
introduced a new timestamp configuration option. You can use the timestamp from either your
device, or the timestamp from the server. Older versions of the OPC UA collector component
do not support this option and fail to sync.

There are two ways to resolve a failing data source sync status. The recommended way is
to upgrade the IoT SiteWise OPC UA collector component to version 2.5.0 or above. Alternatively,
you can continue to use the older OPC UA collector component version, if you set the
timestamp to `Source`. To learn how to upgrade the IoT SiteWise OPC UA collector
component, see [Update the version of an AWS IoT SiteWise
component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version"). We recommend using the latest versions of all
components.

###### Note

There is no data interruption when a data source sync status fails. The source data
continues to flow into AWS IoT SiteWise. The configuration simply isn't syncing with the
IoT SiteWise OPC UA collector component on your AWS IoT Greengrass V2 deployment.

###### To change the timestamp configuration for a property group

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Select the gateway to edit.
4. In the **Data sources** section, select the data source with the
   failed sync status, and choose **Edit**.
5. Expand **Advanced configuration**, then expand **Group
   settings**.
6. In **Timestamp**, select **Source**. Selecting
   **Source** removes the `timestampToReturn` property from
   the configuration. This setting enables the collection of the data source timestamp from
   your device by default, allowing the data source to sync with the IoT SiteWise OPC UA collector
   component.
7. Choose **Save**.

### Converted data types are not included

If you see an error when converting unsupported OPC UA data types to strings in AWS IoT SiteWise,
there are a few possible reasons:

- The data type you're attempting to convert is a complex data type. Complex data
  types are not supported.
- When using **Destinations** as **AWS IoT SiteWise Buffered using
  Amazon S3**, the full string value is preserved in files pushed to an Amazon S3 bucket.
  When you later ingest data into AWS IoT SiteWise, full string values longer than 1024 bytes are
  rejected.

### Trust store issues

If you encounter issues related to trust stores in SiteWise Edge, consider the following
troubleshooting steps:

- Verify that the AWS IoT Greengrass root CA certificate is present and correctly formatted in the
  appropriate trust stores
- Ensure that the Java KeyStore password is correctly set and accessible to SiteWise Edge
  components
- Check that any custom certificates (such as for HTTPS proxies) are in the correct
  format (typically PEM) and properly imported into the trust stores
- Confirm that the trust stores have the correct file permissions and are accessible
  to the SiteWise Edge processes
- Review the SiteWise Edge logs for any SSL/TLS related errors, which may indicate trust
  store issues
- Test SSL/TLS connections independently using tools like `openssl` to
  verify trust store functionality

### Proxy-enabled installation

issues

If you encounter issues during the proxy configuration process, consider the following
troubleshooting steps:

- Verify that the proxy URL is correctly formatted and includes the proper scheme
  (`http://` or `https://`)
- Ensure that any proxy credentials are URL-encoded if they contain special
  characters
- Confirm that the no-proxy list includes all necessary local addresses and AWS
  service endpoints
- For HTTPS proxies, verify that the provided CA certificate is in PEM format
- Review the installation logs for specific error messages that may indicate the
  source of the problem
- Test the proxy connection independently to ensure it's functioning correctly

## Troubleshooting the AWS IoT SiteWise Edge application on

Siemens Industrial Edge

To troubleshoot the AWS IoT SiteWise Edge application on your Siemens Industrial Edge device, you can access the
logs for the application through the Siemens Industrial Edge Management or Siemens Industrial Edge Device (IED) portals. For
more information, see [Downloading Logs](https://docs.eu1.edge.siemens.cloud/build_a_device/device_building/concepts/howto-download-edge-device-logs.html "https://docs.eu1.edge.siemens.cloud/build_a_device/device_building/concepts/howto-download-edge-device-logs.html") in the Siemens documentation.

### My data doesn't display in AWS IoT SiteWise

- Ensure that there are no issues with your Databus users and that the
  checkmark icon for the **Databus_Configuration** is green rather than
  gray.
- You may not be running Siemens Industrial Edge Management on a version that contains Secure
  Storage. Upgrade your version of Siemens OS. For more information, see [Siemens Secure Storage and the AWS IoT SiteWise Edge
  application](sitewise-edge-on-siemens.md#sa-secure-storage "sitewise-edge-on-siemens.md#sa-secure-storage").

### I see 'Config file missing AWS_REGION' in the logs

If you see `Config file missing AWS_REGION` in the Siemens logs, the JSON of
the configuration file has been corrupted. You'll need to create a new configuration file.
Follow the steps in [Create a gateway for Siemens Industrial Edge](sa-create-config.md "sa-create-config.md") to
create a new configuration file.

### I see an 'Out of sync' error message on the Edge gateway

configuration

If you see an `Out of sync` error message on your Siemens Industrial Edge gateway after deployment is complete, it
means that IoT SiteWise publisher component is out of sync with your gateway. The IoT SiteWise publisher
component works in the background on Siemens Industrial Edge gateways to provide MQTT topic
functionality. We upgraded Siemens Industrial Edge gateways to use the capability namespace
`iotsitewise:publisher:3` rather than `iotsitewise:publisher:2`. You
can update to the latest version of the publisher to resolve this issue.

###### To upgrade to the latest version of the IoT SiteWise publisher

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Select the Siemens Industrial Edge gateway to edit.
4. In the **Edge capabilities** section, select the **View software versions**.
5. Select the latest version of the IoT SiteWise publisher under the **Publisher** dropdown menu.
6. Choose **Done**.

## Troubleshooting open-source integrations at the Edge

This section provides solutions for common issues you might encounter when integrating
open-source tools with SiteWise Edge.

###### Note

Node-RED®, InfluxDB®, and Grafana® are not vendors or suppliers for SiteWise Edge.

### Connection issues

Node-RED can't connect to MQTT broker

Verify that the MQTT broker is running and accessible on the specified port. Check your
network configuration and ensure that the broker address is correct.

To verify the MQTT broker status, run:

```
docker ps | grep emqx
```

InfluxDB connection errors

Ensure that your authentication token is valid and that you've specified the correct
organization and bucket names. Check that InfluxDB is running and accessible.

To verify InfluxDB status, run:

```
curl -I http://localhost:8086
```

Grafana can't connect to InfluxDB

Verify that the InfluxDB data source configuration in Grafana is correct, including
the URL, authentication token, organization, and bucket.

### Data flow issues

No data appearing in AWS IoT SiteWise

Check that your property alias in the Node-RED flow matches the expected format. Verify
that the MQTT topic structure is correct and that the SiteWise Edge gateway is properly configured
to receive data from the MQTT broker.

No SiteWise Edge data stored in InfluxDB

Verify that the Node-RED retention flow is correctly configured and that the InfluxDB
writer node has the proper bucket and measurement settings. Check the Node-RED debug output
for any errors.

Data format errors

Ensure that your data transformation functions correctly convert data between formats.
Use the Node-RED debug nodes to inspect the data at each stage of the flow.

### Performance issues

High CPU or memory usage

Monitor resource usage and adjust the configuration of your components as needed.
Consider reducing the data collection frequency or implementing data filtering to reduce the
processing load.

To monitor resource usage, run:

```
docker stats
```

Slow Grafana dashboard loading

Optimize your InfluxDB queries and consider adding time range limitations to your
dashboard panels. Reduce the number of data points displayed by using appropriate aggregation
functions.

### Logging and diagnostics

To troubleshoot issues, check the logs for each component:

Node-RED logs

View logs in the Node-RED console or run:

```
docker logs node-red
```

InfluxDB logs

Access logs by running:

```
docker logs influxdb
```

Grafana logs

View logs by running:

```
docker logs grafana
```

SiteWise Edge logs

Check the SiteWise Edge gateway logs for MQTT connection and data processing issues. For more
information, see [Troubleshooting a SiteWise Edge gateway](troubleshooting-gateway.md "troubleshooting-gateway.md").

## Troubleshooting AWS IoT Greengrass issues

To find solutions to many issues configuring or deploying your SiteWise Edge gateway on AWS IoT Greengrass,
see [Troubleshooting AWS IoT Greengrass](../../../greengrass/v1/developerguide/gg-troubleshooting.md "../../../greengrass/v1/developerguide/gg-troubleshooting.md") in the
_AWS IoT Greengrass Developer Guide_.
