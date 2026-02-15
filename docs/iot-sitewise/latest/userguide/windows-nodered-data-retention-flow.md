# Configure the data retention

flow

The data retention flow is can be used to maintain operational visibility at the edge.
This is useful during network disruptions or when you need immediate access to your data.
This flow subscribes to the MQTT broker to receive device data, converts it to
InfluxDB® format, and stores it locally. By implementing this flow, you create a
resilient local data store that operators can access without cloud dependencies, enabling
real-time monitoring and decision-making at the edge.

The flow consists of three key components working together to ensure your data is
properly captured and stored:

- **MQTT subscription client** - Receives data from the
  broker, ensuring you capture all relevant industrial data
- **InfluxDB translator** - Converts AWS IoT SiteWise payload
  to InfluxDB format, preparing the data for efficient time-series storage
- **InfluxDB writer** - Handles local storage,
  ensuring data persistence and availability for local applications

![Node-RED data retention flow](images/gateway-open-source-nodered-data-retention.png)

## Set up the MQTT subscription

client

- Configure the MQTT subscription client in Node-RED to receive data from the
  MQTT EMQX broker in AWS IoT SiteWise by importing the example below.

###### Example: MQTT in node

```
[
    {
        "id": "string",
        "type": "mqtt in",
        "z": "string",
        "name": "Subscribe to MQTT broker",
        "topic": "`/Renton/WindFarm/Turbine/WindSpeed`",
        "qos": "`1`",
        "datatype": "auto-detect",
        "broker": "string",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 290,
        "y": 340,
        "wires": [
            [
                "string"
            ]
        ]
    },
    {
        "id": "string",
        "type": "mqtt-broker",
        "name": "emqx",
        "broker": "127.0.0.1",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "5",
        "keepalive": 15,
        "cleansession": true,
        "autoUnsubscribe": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "userProps": "",
        "sessionExpiry": ""
    }
]
```

This subscription ensures that all relevant data published to the broker is captured
for local storage, providing a complete record of your industrial operations. The node
uses the same MQTT connection parameters as the [Configure the MQTT
publisher](windows-nodered-data-publish-flow.md#windows-nodered-mqtt-publisher-config "windows-nodered-data-publish-flow.md#windows-nodered-mqtt-publisher-config") section, with the following
subscription settings:

- Topic – `/Renton/WindFarm/Turbine/WindSpeed`
- QoS – `1`

For more information, see [Connect to an MQTT
Broker](https://cookbook.nodered.org/mqtt/connect-to-broker "https://cookbook.nodered.org/mqtt/connect-to-broker") in the _Node-RED Documentation_.

## Configure the InfluxDB

translator

InfluxDB organizes data using [tags](https://docs.influxdata.com/influxdb/v1/concepts/glossary/#tag "https://docs.influxdata.com/influxdb/v1/concepts/glossary/#tag") for
indexing and [fields](https://docs.influxdata.com/influxdb/v1/concepts/glossary/#field "https://docs.influxdata.com/influxdb/v1/concepts/glossary/#field")
for values. This organization optimizes query performance and storage efficiency for
time-series data. Import the example function node that contains JavaScript code to
convert AWS IoT SiteWise payload to InfluxDB format. The translator splits the properties into
two groups:

- Tags – Quality and name properties for efficient indexing
- Fields – Timestamp (in milliseconds since epoch) and value

###### Example: Function node of translating to an InfluxDB payload

```
[
    {
        "id": "string",
        "type": "function",
        "z": "string",
        "name": "Translate to InfluxDB payload",
        "func": "let data = msg.payload;\n\nlet timeInSeconds = data.propertyValues[0].timestamp.timeInSeconds;\nlet offsetInNanos = data.propertyValues[0].timestamp.offsetInNanos;\nlet timestampInMilliseconds = (timeInSeconds * 1000) + (offsetInNanos / 1000000);\n\nmsg.payload = [\n    {\n        \"timestamp(milliseconds_since_epoch)\": timestampInMilliseconds,\n        \"value\": data.propertyValues[0].value.doubleValue\n    },\n    {\n        \"name\": data.propertyAlias,\n        \"quality\": data.propertyValues[0].quality\n    }\n]\n\nreturn msg",
        "outputs": 1,
        "timeout": "",
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 560,
        "y": 340,
        "wires": [
            [
                "string"
            ]
        ]
    }
]
```

For additional configuration options, see the [node-red-contrib-influxdb](https://github.com/mblackstock/node-red-contrib-influxdb "https://github.com/mblackstock/node-red-contrib-influxdb") in the Node-RED GitHub repository.

## Set up the InfluxDB writer

The InfluxDB writer node is the final component in your data retention flow,
responsible for storing your industrial data in the local InfluxDB database. This
local storage is important for maintaining operational visibility during network
disruptions and providing immediate access to data for time-critical
applications.

1. Install the node-red-contrib-influxdb package through the Manage palette option.
   This package provides the necessary nodes for connecting Node-RED with
   InfluxDB.
2. Add an InfluxDB out node to your flow. This node will handle the actual
   writing of data to your InfluxDB database.
3. Configure the server properties to establish a secure connection to your
   InfluxDB instance:
   1. Set Version to 2.0 - This specifies that you're connecting to InfluxDB
      v2.x, which uses a different API than earlier versions
   2. Set URL to `http://127.0.0.1:8086` - This points to your local
      InfluxDB instance
   3. Enter your InfluxDB authentication token. This secure token authorizes the
      connection to your database. You generated the token during the [Set up local storage with InfluxDB](windows-influxdb-setup.md "windows-influxdb-setup.md")
      procedure.

4. Specify the storage location parameters to define where and how your data will
   be stored:
   1. Enter your InfluxDB Organization name – The organization is a
      workspace for a group of users, where your buckets and dashboards belong. For
      more information, see [Manage
      organizations](https://docs.influxdata.com/influxdb/v2/admin/organizations/ "https://docs.influxdata.com/influxdb/v2/admin/organizations/") in the _InfluxData Documentation_.
   2. Specify the InfluxDB Bucket (for example, `WindFarmData`)
      – The bucket is equivalent to a database in traditional systems, serving
      as a container for your time series data
   3. Set the InfluxDB Measurement (for example, `TurbineData`)
      – The measurement is similar to a table in relational databases,
      organizing related data points

###### Note

Find your organization name in the InfluxDB instance's left sidebar. The
organization, bucket, and measurement concepts are fundamental to InfluxDB's data
organization model. For more information, see the [InfluxDB
documentation](https://docs.influxdata.com/influxdb/v2/admin/organizations/ "https://docs.influxdata.com/influxdb/v2/admin/organizations/").

## Deploy and verify the retention

flow

After configuring all components of the data retention flow, you need to deploy and
verify that the system is working correctly. This verification ensures that your
industrial data is being properly stored locally for immediate access and
analysis.

1. Connect the three nodes as shown in the data retention flow diagram. This
   creates a complete pipeline from data subscription to local storage.

![Node-RED data retention flow](images/gateway-open-source-nodered-data-retention.png) 2. Choose **Deploy** to apply your changes and activate the flow.
This starts the data collection and storage process. 3. Use the InfluxDB Data Explorer to query and visualize your data. This tool
allows you to verify that data is being properly stored and to create initial
visualizations of your time series data.

In the Data Explorer, you should be able to see your wind speed measurements
being recorded over time, confirming that the entire pipeline from data generation
to local storage is functioning correctly.

For more information, see [Query in Data Explorer](https://docs.influxdata.com/influxdb/v2/query-data/execute-queries/data-explorer/ "https://docs.influxdata.com/influxdb/v2/query-data/execute-queries/data-explorer/") in the _InfluxData Documentation_.

With both the data publish flow and data retention flow deployed, you now have a
complete system that sends data to the AWS IoT SiteWise cloud while maintaining a local copy for
immediate access and resilience. This dual-path approach ensures that you get the
benefits of cloud-based analytics and storage while maintaining operational visibility
at the edge.
