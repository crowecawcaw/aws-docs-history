# Edge Agent for AWS IoT FleetWise software issues

Troubleshoot Edge Agent software issues.

###### Issues

- [Issue: The Edge Agent software doesn't
  start.](#troubleshooting-issue1 "#troubleshooting-issue1")
- [Issue: [ERROR]
  [IoTFleetWiseEngine::connect]: [Failed to init persistency library]](#troubleshooting-issue2 "#troubleshooting-issue2")
- [Issue: The Edge Agent software doesn't collect
  on-board diagnostics (OBD) II PIDs and diagnostic trouble codes (DTCs).](#troubleshooting-issue3 "#troubleshooting-issue3")
- [Issue: The Edge Agent for AWS IoT FleetWise software doesn't collect
  data from the network or isn't able to apply data inspection rules.](#troubleshooting-issue5 "#troubleshooting-issue5")
- [Issue: [ERROR]
  [AwsIotConnectivityModule::connect]: [Connection failed with error] or [WARN]
  [AwsIotChannel::send]: [No alive MQTT Connection.]](#troubleshooting-issue4 "#troubleshooting-issue4")

## Issue: The Edge Agent software doesn't

start.

You might see the following errors when the Edge Agent software doesn't start.

- ```
  Error from reader: * Line 1, Column 1
  Syntax error: value, object or array expected.
  ```

````

**Solution:**  Make sure the Edge Agent for AWS IoT FleetWise software
 configuration file is using valid JSON format. For example, make sure that
 commas are used correctly. For more information about the configuration
 file, do the following to download the *Edge Agent for AWS IoT FleetWise software Developer
 Guide*.



	1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
	2. On the service home page, in the **Get started with AWS IoT FleetWise**
	 section, choose **Explore Edge Agent**.
* ```
[ERROR] [SocketCANBusChannel::connect]: [ SocketCan with name xxx is not accessible]
[ERROR] [IoTFleetWiseEngine::connect]: [ Failed to Bind Consumers to Producers ]
````

**Solution:** You might see this error when
the Edge Agent software fails to establish socket communication with the network
interfaces defined in the configuration file.

To check that every network interface defined in the configuration is
available, run the following command.

```
ip link show
```

To bring a network interface online, run the following command. Replace
`network-interface-id` with the ID of the
network interface.

```
sudo ip link set `network-interface-id` up
```

- ```
  [ERROR] [AwsIotConnectivityModule::connect]: [Connection failed with error]
  [WARN] [AwsIotChannel::send]: [No alive MQTT Connection.]
  ```

# or

[WARN] [AwsIotChannel::send]: [aws-c-common: AWS_ERROR_FILE_INVALID_PATH]

```

**Solution:**  You might see this error when
 the Edge Agent software fails to establish an MQTT connection to AWS IoT Core. Check
 that the following are configured correctly and restart the
 Edge Agent software.




	+ `mqttConnection::endpointUrl` – AWS account's
	 IoT device endpoint.
	+ `mqttConnection::clientID` – The ID of the
	 vehicle in which the Edge Agent software is running.
	+ `mqttConnection::certificateFilename` – The path
	 to the vehicle certificate file.
	+ `mqttConnection::privateKeyFilename` – The path
	 to the vehicle private key file.
	+ You have used AWS IoT Core to provision the vehicle. For more
	 information, see [Provision AWS IoT FleetWise vehicles](provision-vehicles.md "provision-vehicles.md").
For more troubleshooting information, see [AWS IoT Device SDK for C++ Frequently Asked Questions](https://github.com/aws/aws-iot-device-sdk-cpp-v2/blob/main/documents/FAQ.md#frequently-asked-questions "https://github.com/aws/aws-iot-device-sdk-cpp-v2/blob/main/documents/FAQ.md#frequently-asked-questions").

## Issue: [ERROR]
 [IoTFleetWiseEngine::connect]: [Failed to init persistency library]


**Solution:**  You might see this error when the
 Edge Agent software fails to locate the persistence storage. Check that the following is
 configured correctly and restart the Edge Agent software.


`persistency:persistencyPath` – A local path used to persist
 collection schemes, decoder manifests, and data snapshots.


## Issue: The Edge Agent software doesn't collect
 on-board diagnostics (OBD) II PIDs and diagnostic trouble codes (DTCs).


**Solution:**  You might see this error if
 `obdInterface:pidRequestIntervalSeconds` or
 `obdInterface:dtcRequestIntervalSeconds` is configured to 0.


If the Edge Agent software is running in an automatic transmission vehicle, make sure
 `obdInterface:hasTransmissionEcu` is configured to
 `true`.


If your vehicle supports extended Controller Area Network (CAN bus) arbitration
 IDs, make sure `obdInterface:useExtendedIds` is configured to
 `true`.


## Issue: The Edge Agent for AWS IoT FleetWise software doesn't collect
 data from the network or isn't able to apply data inspection rules.


**Solution:** You might see this error when the
 default quotas are breached.




| Resource | Quota | Adjustable | Note |
| --- | --- | --- | --- |
| Value of the signal ID | The signal ID must be less than or equal to 50,000 | Yes | The Edge Agent software won't collect data from signals that have an ID greater than 50,000. We recommend that you check how many signals the signal catalog contains before you change this quota. |
| Number of active data collection schemes per vehicle | 256 | Yes | We recommend that you check how many campaigns that you've created in the cloud and how many schemes each campaign contains before you change this quota. |
| Size of the signal history buffer | 20 MB | Yes | If the quota is breached, the Edge Agent software stops collecting new data. | ## Issue: [ERROR] [AwsIotConnectivityModule::connect]: [Connection failed with error] or [WARN] [AwsIotChannel::send]: [No alive MQTT Connection.] **Solution:** You might see this error when the Edge Agent software isn't connected to the cloud. By default, the Edge Agent software sends a ping request to AWS IoT Core every minute and waits for three minutes. If there's no response, the Edge Agent software automatically reestablishes the connection to the cloud.
```
