# Set up an OPC UA source in

SiteWise Edge

You can use the AWS IoT SiteWise console or a SiteWise Edge gateway capability to define and
add an OPC UA source to your SiteWise Edge gateway to represent a local OPC UA
server.

###### Topics

- [Configure an OPC UA source
  (console)](#config-opcua-source-console "#config-opcua-source-console")
- [Configure an OPC UA source
  (AWS CLI)](#configure-opc-ua-source-cli "#configure-opc-ua-source-cli")

## Configure an OPC UA source

(console)

You can use the console to configure the OPC UA source with the following
procedure.

###### Note

Warning: Duplicate TQVs may result in double charging.

###### To configure an OPC UA source using the AWS IoT SiteWise console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Select the SiteWise Edge gateway to add an OPC UA source.
4. Choose **Add data source**.
5. Enter a name for the source.
6. Enter the **Local endpoint** of the data source
   server. The endpoint can be the IP address or hostname. You may also
   add a port number to the local endpoint. For example, your local
   endpoint might look like this:
   `opc.tcp://203.0.113.0:49320`
7. (Optional) For **Node ID for selection**, add
   node filters to limit which data streams are ingested to the AWS
   Cloud. By default, SiteWise Edge gateways use the root node of a server to
   ingest all data streams. You can use node filters to reduce your SiteWise Edge gateway's startup time and CPU usage
   by only including paths to data that you model in AWS IoT SiteWise. By default, SiteWise Edge gateways upload
   all OPC UA paths except those that start with `/Server/`. To define OPC UA
   node filters, you can use node paths and the `*` and `**`
   wildcard characters. For more information, see [Use OPC UA node filters in SiteWise Edge](opc-ua-node-filters.md "opc-ua-node-filters.md").
8. **Destinations** vary between MQTT-enabled, V3
   gateways and Classic streams, V2 gateways.
   - **Classic steams, V2 gateway
     destinations** have a 1:1 relationship with the
     source. Each source sends data to a particular
     destination.
   - **MQTT-enabled, V3 gateway destinations**
     are set up separately because the hub and spoke model lets
     you centralize configuration and management of multiple data
     sources across different gateways. To set up destinations in
     a V3 gateway, see [Understand AWS IoT SiteWise Edge destinations](gw-destinations.md#source-destination "gw-destinations.md#source-destination").

Classic steams, V2 gateway destinations

    * **AWS IoT SiteWise real-time** –
     Choose this to send data directly to AWS IoT SiteWise
     storage. Ingest and monitor data in real-time at
     the edge.
    * **AWS IoT SiteWise Buffered using
     Amazon S3** – Send data in Parquet
     format to Amazon S3 and then import into AWS IoT SiteWise
     storage. Choose this option to ingest data in
     batches, and store historical data in a
     cost-effective way. You can configure your
     preferred Amazon S3 bucket location, and the frequency
     at which you want data to be uploaded to Amazon S3. You
     can also choose what to do with the data after
     ingestion into AWS IoT SiteWise. You can choose to have the
     data available in both AWS IoT SiteWise and Amazon S3 or you can
     choose to delete it automatically from Amazon S3 after
     it has been imported into AWS IoT SiteWise.




    	+ The Amazon S3 bucket is a staging and buffering
    	 mechanism and supports files in the Parquet
    	 format.
    	+ If you select the check box **Import data into AWS IoT SiteWise
    	 storage**, data is uploaded into Amazon S3
    	 first, and then into AWS IoT SiteWise storage.




    		- If you select the check box **Delete data from Amazon S3**, data
    		 is deleted from Amazon S3, after it is imported into
    		 SiteWise storage.
    		- If you clear the check box **Delete data from Amazon S3**, data
    		 is stored both in Amazon S3, and in SiteWise storage.
    	+ If you clear the check box **Import data into AWS IoT SiteWise
    	 storage**, data is stored only in Amazon S3.
    	 It is not imported into SiteWise storage.
    Visit [Manage data storage](manage-data-storage.md "manage-data-storage.md") for
     details on the various storage options AWS IoT SiteWise
     provides. To learn more about pricing options, see
     [AWS IoT SiteWise pricing](https://aws.amazon.com/iot-sitewise/pricing/ "https://aws.amazon.com/iot-sitewise/pricing/").
    * **AWS IoT Greengrass stream manager**
     – Use AWS IoT Greengrass stream manager to send data to
     the following AWS Cloud destinations: channels
     in AWS IoT Analytics, streams in Amazon Kinesis Data Streams, asset properties
     in AWS IoT SiteWise, or objects in Amazon Simple Storage Service (Amazon S3). For more
     information, see [Manage
     data streams on the AWS IoT Greengrass Core](../../../greengrass/v2/developerguide/manage-data-streams.md "../../../greengrass/v2/developerguide/manage-data-streams.md") in
     *AWS IoT Greengrass Version 2 Developer Guide*.


    Enter a name for the AWS IoT Greengrass stream.

MQTT-enabled, V3 gateway destinations

    1. See [MQTT-enabled, V3 gateways for AWS IoT SiteWise Edge](mqtt-enabled-v3-gateway.md "mqtt-enabled-v3-gateway.md") for
     information on adding your relevant
     destinations.
    2. Return to this procedure after adding your
     source destinations.

9.  In the **Advanced configuration** pane, you can
    do the following:
    1. Choose a **Message security mode** for
       connections and data in transit between your source server
       and your SiteWise Edge gateway. This field is the combination of
       the OPC UA security policy and message security mode. Choose
       the same security policy and message security mode that you
       specified for your OPC UA server.
    2. If your source requires authentication, choose an
       AWS Secrets Manager secret from the **Authentication
       configuration** list. The SiteWise Edge gateway uses
       the authentication credentials in this secret when it
       connects to this data source. You must attach secrets to
       your SiteWise Edge gateway's AWS IoT Greengrass component to use them for data
       source authentication. For more information, see [Configure data source
       authentication for SiteWise Edge](configure-source-authentication-ggv2.md "configure-source-authentication-ggv2.md").

    ###### Tip

    Your data server might have an option named
    **Allow anonymous login**. If this
    option is **Yes**, then your source
    doesn't require authentication. 3. (Optional) You can activate a data stream prefix by
    selecting **Activate data stream prefix -
    _optional_**.

        1. Enter a **Data stream prefix**.
         The SiteWise Edge gateway adds this prefix to all data
         streams from this source. Use a data stream prefix
         to distinguish between data streams that have the
         same name from different sources. Each data stream
         should have a unique name within your
         account.

    4. (Optional) Choose a **Data type
       conversion** option to convert unsupported OPC
       UA data types into strings before ingesting them into
       AWS IoT SiteWise. Convert array values with simple data types to JSON
       strings and DateTime data types to ISO 8601 strings. For
       more information, see [Converting unsupported data types](string-conversion.md "string-conversion.md").
    5. Choose a **Default data change trigger**
       for nodes that are not contained in a user-defined property
       group. The default data change trigger determines when the
       OPC UA server sends updated values to the gateway. You can
       choose one of the following options:
       - **Status** –
         to receive data only when a status changes.
       - **StatusValue**
         – to receive data when a status or value
         changes.
       - **StatusValueTimestamp** – to
         receive data when a status, value, or timestamp
         changes.

    6. (Optional) On an MQTT-enabled, V3 gateway, you can use
       **Discovery configuration** to
       configure the OPC UA node discovery process. Discovery
       configuration replaces the previous config override file
       system for these options with console-based settings that
       update dynamically without needing to restart the
       gateway.

    ###### Note

    **Default data change trigger**
    requires version 3.1.0 or later of the
    IoT SiteWise OPC UA collector component. For more information,
    see [Update the version of an AWS IoT SiteWise
    component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version").

        1. For **Maximum concurrent browse request
         count**, enter the maximum number of
         browse requests that your OPC UA server can handle
         simultaneously. You can configure up to 500
         concurrent browse requests per data source.
        2. For **Maximum node count per browse
         request**, enter the maximum number of
         nodes to send in each browse request to the OPC UA
         server. You can send up to 1,000 nodes per browse
         request.
        3. Choose **Avoid node tree loops**
         to prevent the gateway from getting stuck in
         circular references when browsing the OPC UA
         server's structure. When selected, the gateway
         tracks visited locations to avoid infinite loops
         that can occur when server nodes reference each
         other in a circular pattern.
        4. Choose **Enable node traversal**
         to allow the gateway to explore the complete
         structure of your OPC UA server to discover all
         available data points from your equipment and
         devices. When selected, the gateway navigates
         through your equipment's data organization beyond
         the root level to find all sensors, controls, and
         measurement points automatically.
        5. Choose **Enable periodic
         discovery** to automatically run
         discovery operations at regular intervals to detect
         changes in the OPC UA server's structure. When
         selected, the gateway continuously monitors for
         newly added equipment or data points, ensuring they
         are automatically detected and made available for
         data collection.


        	1. For **Periodic discovery
        	 interval**, set the time interval between
        	 automatic discovery operations when periodic
        	 discovery is running. The minimum periodic
        	 discovery interval is 30 seconds and the maximum is
        	 30 days.
        	2. For **Maximum nodes discovered per
        	 interval**, set the maximum number of
        	 nodes that should be discovered per discovery
        	 interval. This helps control the load on both the
        	 gateway and the OPC UA server during discovery
        	 operations.

    7.  (Optional) For **Property groups**,
        choose **Add new group**.
        1.  Enter a **Name** for the property
            group.
        2.  For **Properties**:
            1. For **Node paths**, add OPC
               UA node filters to limit which OPC UA paths are
               uploaded to AWS IoT SiteWise. The format is similar to
               **Node ID for selection**.

        3.  For **Group settings**, do the
            following:
            1. For **Data quality
               setting**, choose the type of data
               quality that you want AWS IoT SiteWise Collector to
               ingest.
            2. For **Scan mode setting**,
               configure the standard subscription properties
               using **Scan mode**. You can
               select **Subscribe** or
               **Poll**. For more information
               about scan mode, see [Filter data ingestion ranges with OPC
               UA](opcua-data-acquisition.md "opcua-data-acquisition.md").

            Subscribe

            ###### To send every data point

                1. Choose **Subscribe** and
                 set the following:


                	1. **[Data change trigger](https://reference.opcfoundation.org/v104/Core/docs/Part4/7.17.2/ "https://reference.opcfoundation.org/v104/Core/docs/Part4/7.17.2/")** –
                	 The condition that initiates a data change
                	 alert.
                	2. **[Subscription queue size](https://reference.opcfoundation.org/v104/Core/docs/Part4/7.16/ "https://reference.opcfoundation.org/v104/Core/docs/Part4/7.16/")**
                	 – The depth of the queue on an OPC UA
                	 server for a particular metric where notifications
                	 for monitored items are queued.
                	3. **[Subscription publishing
                	 interval](https://reference.opcfoundation.org/v104/Core/docs/Part4/5.13.2/ "https://reference.opcfoundation.org/v104/Core/docs/Part4/5.13.2/")** – The interval
                	 (in milliseconds) of publishing cycle specified
                	 when subscription is created.
                	4. **Snapshot interval -
                	 *Optional*** –
                	 The snapshot frequency timeout setting to ensure
                	 that AWS IoT SiteWise Edge ingests a steady stream of
                	 data.
                	5. **Scan rate** – The
                	 rate that you want the SiteWise Edge gateway to read
                	 your registers. AWS IoT SiteWise automatically calculates
                	 the minimum allowable scan rate for your SiteWise Edge
                	 gateway.
                	6. **Timestamp** – The timestamp to include with your OPC UA data points. You can use the server timestamp or your device's timestamp.


                	###### Note

                	Use version 2.5.0 or later of the
                	 IoT SiteWise OPC UA collector component. If you use the
                	 timestamp feature with earlier versions,
                	 configuration updates fail. For more information,
                	 see [Update the version of an AWS IoT SiteWise
                	 component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version").
                2. In **Deadband settings**,
                 configure a **Deadband type**.
                 The deadband type controls what data your source
                 sends to your AWS IoT SiteWise, and what data it discards.
                 For more information about the deadband setting,
                 see [Filter data ingestion ranges with OPC
                 UA](opcua-data-acquisition.md "opcua-data-acquisition.md").




                	* **None** – The
                	 associated server sends all data points for this
                	 property group.
                	* **Percentage** – The
                	 associated server only sends data that falls
                	 outside a specified percentage of the data's
                	 range. This range is computed by the server based
                	 on the engineering unit minimum and maximum
                	 defined for each node. If the server does not
                	 support percentage deadbands or lacks defined
                	 engineering units, the gateway calculates the
                	 range using the minimum and maximum values
                	 provided below.
                	* **Absolute** – The
                	 associated server only sends data that falls
                	 outside of a specific range.
                	1. Set the **Deadband value**
                	 as the percentage of the data range to
                	 deadband.
                	2. (Optional) Specify a minimum and maximum for
                	 the deadband range using **Minimum range -
                	 *optional*** and
                	 **Maximum range -
                	 *optional***.

            Poll

            ###### To send data points at a specific

            interval

                * Choose **Poll** and set the
                 following:


                	1. **Scan rate** – The
                	 rate that you want the SiteWise Edge gateway to read
                	 your registers. AWS IoT SiteWise automatically calculates
                	 the minimum allowable scan rate for your SiteWise Edge
                	 gateway.
                	2. **Timestamp** – The timestamp to include with your OPC UA data points. You can use the server timestamp or your device's timestamp.


                	###### Note

                	Use version 3.1.0 or later of the
                	 IoT SiteWise OPC UA collector component. If you use the
                	 timestamp feature with earlier versions,
                	 configuration updates fail. For more information,
                	 see [Update the version of an AWS IoT SiteWise
                	 component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version").

            ###### Note

            **Deadband settings** are
            applicable when you've selected
            **Subscribe** in the
            **Scan mode settings**.

10. Choose **Save**.

## Configure an OPC UA source

(AWS CLI)

You can define OPC UA data sources for an SiteWise Edge gateway using the AWS CLI.
To do this, create an OPC UA capability configuration JSON file and use the
[update-gateway-capability-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway-capability-configuration.html# "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway-capability-configuration.html#") command to update the
SiteWise Edge gateway configuration. You must define all of your OPC UA sources in
a single capability configuration.

MQTT-enabled, V3 gateway
This capability has the following namespace.

- `iotsitewise:opcuacollector:3`

```
{
  "sources": [
    {
      "name": "`string`",
      "endpoint": {
        "certificateTrust": {
          "type": "`TrustAny`" | "`X509`",
          "certificateBody": "`string`",
          "certificateChain": "`string`",
        },
        "endpointUri": "`string`",
        "securityPolicy": "`NONE`" | "`BASIC128_RSA15`" | "`BASIC256`" | "`BASIC256_SHA256`" | "`AES128_SHA256_RSAOAEP`" | "`AES256_SHA256_RSAPSS`",
        "messageSecurityMode": "`NONE`" | "`SIGN`" | "`SIGN_AND_ENCRYPT`",
        "identityProvider": {
          "type": "`Anonymous`" | "`Username`",
          "usernameSecretArn": "`string`"
        },
        "nodeFilterRules": [
          {
            "action": "`INCLUDE`",
            "definition": {
              "type": "`OpcUaRootPath`",
              "rootPath": "`string`"
            }
          }
        ]
      },
      "measurementDataStreamPrefix": "`string`",
      "typeConversions": {
        "array": "`JsonArray`",
        "datetime": "`ISO8601String`"
        },
      "destination": {
        {
          "type":"`MQTT`"
        }
      },
      "defaultPropertyGroupConfig": {
        "dataChangeTrigger": "`STATUS`" | "`STATUS_VALUE`" | "`STATUS_VALUE_TIMESTAMP`"
      },
      "discoveryConfig": {
        "enableNodeTraversal": `true` | `false`,
        "avoidNodeTreeLoops": `true` | `false`,
        "maxConcurrentBrowseRequests": `integer`,
        "maxNodesPerBrowseRequest": `integer`,
        "periodicDiscovery": {
          "interval": "`string`",
          "maxNodesDiscoveredPerInterval": `integer`
        }
      },
      "propertyGroups": [
        {
          "name": "`string`",
          "nodeFilterRuleDefinitions": [
            {
              "type": "`OpcUaRootPath`",
              "rootPath": "`string`"
            }
          ],
          "deadband": {
            "type": "`PERCENT`" | "`ABSOLUTE`",
            "value": `double`,
            "eguMin": `double`,
            "eguMax": `double`,
            "timeoutMilliseconds": `integer`
          },
          "scanMode": {
            "type": "`EXCEPTION`" | "`POLL`",
            "rate": `integer`,
            "timestampToReturn": "`SOURCE_TIME`" | "`SERVER_TIME`"
          },
          "dataQuality": {
            "allowGoodQuality": `true` | `false`,
            "allowBadQuality": `true` | `false`,
            "allowUncertainQuality": `true` | `false`
          },
          "subscription": {
            "dataChangeTrigger": "`STATUS`" | "`STATUS_VALUE`" | "`STATUS_VALUE_TIMESTAMP`",
            "queueSize": `integer`,
            "publishingIntervalMilliseconds": `integer`,
            "snapshotFrequencyMilliseconds": `integer`
          }
        }
      ]
    }
  ]
}
```

Classic streams, V2 gateway
This capability has the following namespace.

- `iotsitewise:opcuacollector:2`

Request syntax

```
{
  "sources": [
    {
      "name": "`string`",
      "endpoint": {
        "certificateTrust": {
          "type": "`TrustAny`" | "`X509`",
          "certificateBody": "`string`",
          "certificateChain": "`string`",
        },
        "endpointUri": "`string`",
        "securityPolicy": "`NONE`" | "`BASIC128_RSA15`" | "`BASIC256`" | "`BASIC256_SHA256`" | "`AES128_SHA256_RSAOAEP`" | "`AES256_SHA256_RSAPSS`",
        "messageSecurityMode": "`NONE`" | "`SIGN`" | "`SIGN_AND_ENCRYPT`",
        "identityProvider": {
          "type": "`Anonymous`" | "`Username`",
          "usernameSecretArn": "`string`"
        },
        "nodeFilterRules": [
          {
            "action": "`INCLUDE`",
            "definition": {
              "type": "`OpcUaRootPath`",
              "rootPath": "`string`"
            }
          }
        ]
      },
      "measurementDataStreamPrefix": "`string`",
      "typeConversions": {
        "array": "`JsonArray`",
        "datetime": "`ISO8601String`"
        },
      "destination": {
        "type": "`StreamManager`",
        "streamName": "`string`",
        "streamBufferSize": `integer`,
      },
      "propertyGroups": [
        {
          "name": "`string`",
          "nodeFilterRuleDefinitions": [
            {
              "type": "`OpcUaRootPath`",
              "rootPath": "`string`"
            }
          ],
          "deadband": {
            "type": "`PERCENT`" | "`ABSOLUTE`",
            "value": `double`,
            "eguMin": `double`,
            "eguMax": `double`,
            "timeoutMilliseconds": `integer`
          },
          "scanMode": {
            "type": "`EXCEPTION`" | "`POLL`",
            "rate": `integer`,
            "timestampToReturn": "`SOURCE_TIME`" | "`SERVER_TIME`"
          },
          "dataQuality": {
            "allowGoodQuality": `true` | `false`,
            "allowBadQuality": `true` | `false`,
            "allowUncertainQuality": `true` | `false`
          },
          "subscription": {
            "dataChangeTrigger": "`STATUS`" | "`STATUS_VALUE`" | "`STATUS_VALUE_TIMESTAMP`",
            "queueSize": `integer`,
            "publishingIntervalMilliseconds": `integer`,
            "snapshotFrequencyMilliseconds": `integer`
          }
        }
      ]
    }
  ]
}
```

### Request body

`sources`

A list of OPC UA source definition structures that each
contain the following information:

`name`

A unique, friendly name for the source.

`endpoint`

An endpoint structure that contains the
following information:

`certificateTrust`

A certificate trust policy structure that
contains the following information:

`type`

The certificate trust mode for the source.
Choose one of the following:

- `TrustAny` – The SiteWise Edge
  gateway trusts any certificate when it connects to
  the OPC UA source.
- `X509` – The SiteWise Edge
  gateway trusts an X.509 certificate when it
  connects to the OPC UA source. If you choose this
  option, you must define
  `certificateBody` in
  `certificateTrust`. You can also define
  `certificateChain` in
  `certificateTrust`.

`certificateBody`

(Optional) The body of an X.509
certificate.

This field is required if you choose
`X509` for `type` in
`certificateTrust`.

`certificateChain`

(Optional) The chain of trust for an X.509
certificate.

This field is used only if you choose
`X509` for `type` in
`certificateTrust`.

`endpointUri`

The local endpoint of the OPC UA source. For
example, your local endpoint might look like
`opc.tcp://203.0.113.0:49320`.

`securityPolicy`

The security policy to use so that you can
secure messages that are read from the OPC UA
source. Choose one of the following:

- `NONE` – The SiteWise Edge
  gateway doesn't secure messages from the OPC UA
  source. We recommend that you choose a different
  security policy. If you choose this option, you
  must also choose `NONE` for
  `messageSecurityMode`.
- `BASIC256_SHA256` – The
  `Basic256Sha256` security
  policy.
- `AES128_SHA256_RSAOAEP` –
  The `Aes128_Sha256_RsaOaep` security
  policy.
- `AES256_SHA256_RSAPSS` –
  The `Aes256_Sha256_RsaPss` security
  policy.
- `BASIC128_RSA15` –
  (Deprecated) The `Basic128Rsa15`
  security policy is deprecated in the OPC UA
  specification because it's no longer considered
  secure. We recommend that you choose a different
  security policy. For more information, see [Profile SecurityPolicy –
  Basic128Rsa15](https://profiles.opcfoundation.org/profile/1532 "https://profiles.opcfoundation.org/profile/1532").
- `BASIC256` – (Deprecated)
  The `Basic256` security policy is
  deprecated in the OPC UA specification because
  it's no longer considered secure. We recommend
  that you choose a different security policy. For
  more information, see [SecurityPolicy – Basic256](https://profiles.opcfoundation.org/profile/1536 "https://profiles.opcfoundation.org/profile/1536").

###### Important

If you choose a security policy other than
`NONE`, you must choose
`SIGN` or `SIGN_AND_ENCRYPT`
for `messageSecurityMode`. You must
also configure your source server to trust the
SiteWise Edge gateway. For more information, see [Set up OPC UA servers to trust the
AWS IoT SiteWise Edge gateway](enable-source-trust.md "enable-source-trust.md").

`messageSecurityMode`

The message security mode to use to secure
connections to the OPC UA source. Choose one of
the following:

- `NONE` – The SiteWise Edge
  gateway doesn't secure connections to the OPC UA
  source. We recommend that you choose a different
  message security mode. If you choose this option,
  you must also choose `NONE` for
  `securityPolicy`.
- `SIGN` – Data in transit
  between the SiteWise Edge gateway and the OPC UA source
  is signed but not encrypted.
- `SIGN_AND_ENCRYPT` – Data
  in transit between the gateway and the OPC UA
  source is signed and encrypted.

###### Important

If you choose a message security mode other
than `NONE`, you must choose a
`securityPolicy` other than
`NONE`. You must also configure your
source server to trust the SiteWise Edge gateway. For
more information, see [Set up OPC UA servers to trust the
AWS IoT SiteWise Edge gateway](enable-source-trust.md "enable-source-trust.md").

`identityProvider`

An identity provider structure that contains
the following information:

`type`

The type of authentication credentials
required by the source. Choose one of the
following:

- `Anonymous` – The source
  doesn't require authentication to connect.
- `Username` – The source
  requires a user name and password to connect. If
  you choose this option, you must define
  `usernameSecretArn` in
  `identityProvider`.

`usernameSecretArn`

(Optional) The ARN of an AWS Secrets Manager secret.
The SiteWise Edge gateway uses
the authentication credentials in this secret when it connects to this source. You
must attach secrets to your SiteWise Edge gateway's IoT SiteWise connector to use them for
source authentication. For more information, see [Configure data source
authentication for SiteWise Edge](configure-source-authentication-ggv2.md "configure-source-authentication-ggv2.md").

This field is required if you choose
`Username` for `type` in
`identityProvider`.

`nodeFilterRules`

A list of node filter rule
structures that define the OPC UA data stream
paths to send to the AWS Cloud.
You can use node filters to reduce your SiteWise Edge gateway's startup time and CPU usage
by only including paths to data that you model in AWS IoT SiteWise. By default, SiteWise Edge gateways upload
all OPC UA paths except those that start with `/Server/`. To define OPC UA
node filters, you can use node paths and the `*` and `**`
wildcard characters. For more information, see [Use OPC UA node filters in SiteWise Edge](opc-ua-node-filters.md "opc-ua-node-filters.md").

Each structure in the list must contain the
following information:

`action`

The action for this node filter rule. You
can choose the following option:

- `INCLUDE` – The SiteWise Edge
  gateway includes only data streams that match this
  rule.

`definition`

A node filter rule structure that contains
the following information:

`type`

The type of node filter path for this rule.
You can choose the following option:

- `OpcUaRootPath` – The
  SiteWise Edge gateway evaluates this node filter path
  against the root of the OPC UA path
  hierarchy.

`rootPath`

The node filter path to evaluate against the
root of the OPC UA path hierarchy. This path must
start with `/`.

`measurementDataStreamPrefix`

A string to prepend to all data streams from
the source. The SiteWise Edge gateway adds this
prefix to all data streams from this source. Use a data stream prefix to distinguish
between data streams that have the same name from different sources. Each data stream
should have a unique name within your account.

`typeConversions`

The types of conversions available for
unsupported OPC UA data types. Each data type is
converted to strings. For more information, see
[Converting unsupported data types](string-conversion.md "string-conversion.md").

`array`

The simple array data type that is converted
to strings. You can choose the following
option:

- `JsonArray` – Indicates
  that you choose to convert your simple array data
  types to strings.

`datetime`

The DateTime data type that is converted to
strings. You can choose the following
option:

- `ISO8601String` –
  Indicates that you choose to convert ISO 8601 data
  types to strings.

`destination`

Configuration for the destination of OPC UA
tags. Classic stream, v2 and MQTT-enabled, V3
gateways have differing configurations for
destinations.

`type`

The type of the destination.

`streamName` –
_only for Classic streams, V2
gateways_

The name of the stream. The stream name
should be unique.

`streamBufferSize` –
_only for Classic streams, V2
gateways_

The buffer size of the stream. This is
important for managing the flow of data from OPC
UA sources.

`defaultPropertyGroupConfig` –
_MQTT-enabled, V3 gateways
only_

(Optional) Configuration for the default
property group. The default property group
contains all nodes not otherwise contained in a
user-defined property group.

`dataChangeTrigger`

The default data change trigger to use in
the default property group. Valid values are
`STATUS_VALUE_TIMESTAMP`,
`STATUS_VALUE`, or
`STATUS`.

###### Note

`defaultPropertyGroupConfig`
requires version 3.1.0 or later of the
IoT SiteWise OPC UA collector component. For more information,
see [Update the version of an AWS IoT SiteWise
component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version").

`discoveryConfig` –
_MQTT-enabled, V3 gateways
only_

(Optional) Configuration for the OPC UA node
discovery process.

`enableNodeTraversal`

Specifies whether to continue traversing
child nodes of the root node defined by the data
source's node filter. When set to
`false`, discovery stops at the root
node.

`avoidNodeTreeLoops`

Specifies whether to avoid infinite loops
during the OPC UA node browsing process. When set
to `true`, the gateway tracks visited
nodes to prevent circular references.

`maxConcurrentBrowseRequests`

The maximum number of concurrent browse
requests that your OPC UA server can handle
simultaneously. Valid range is 1 to 500.

`maxNodesPerBrowseRequest`

The maximum number of nodes to send in each
browse request to the OPC UA server. Valid range
is 1 to 1,000.

`periodicDiscovery`

Configuration for running discovery
periodically at fixed intervals. Periodic
discovery is enabled when this configuration is
provided.

`interval`

The amount of time between periodic
discovery operations. You can use `m`
for minutes, `h` for hours, and
`d` for days. For example,
`90m` or `1h`. The
minimum interval is 30 seconds.

`maxNodesDiscoveredPerInterval`

The maximum number of nodes that should be
discovered per discovery interval. This helps
control the load on both the gateway and the OPC
UA server.

###### Note

`periodicDiscovery`
requires version 3.1.0 or later of the
IoT SiteWise OPC UA collector component. For more information,
see [Update the version of an AWS IoT SiteWise
component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version").

###### Note

If discovery loops infinitely, enable
`avoidNodeTreeLoops`. Monitor discovery
progress in CloudWatch logs under the
`aws.iot.SiteWiseOpcUaCollector`
component.

`propertyGroups`

(Optional) The list of property groups that define the
`deadband` and `scanMode`
requested by the protocol.

`name`

The name of the property group. This should be
a unique identifier.

`deadband`

The `deadband` value defines the
minimum change in a data point's value that must
occur before the data is sent to the cloud. It
contains the following information:

`type`

The supported types of deadband. You can
choose the following options:

- `ABSOLUTE` – A fixed value
  that specifies the minimum absolute change
  required to consider a data point significant
  enough to be sent to the cloud.
- `PERCENT` – A dynamic
  value that specifies the minimum change required
  as a percentage of the last sent data point's
  value. This type of deadband is useful when the
  data values vary significantly over time.

`value`

The value of the deadband. When
`type` is `ABSOLUTE`, this
value is a unitless double. When `type`
is `PERCENT`, this value is a double
between `1` and
`100`.

`eguMin`

(Optional) The engineering unit minimum when
using a `PERCENT` deadband. You set
this if the OPC UA server doesn't have engineering
units configured.

`eguMax`

(Optional) The engineering unit maximum when
using a `PERCENT` deadband. You set
this if the OPC UA server doesn't have engineering
units configured.

`timeoutMilliseconds`

The duration in milliseconds before timeout.
The minimum is `100`.

`scanMode`

The `scanMode` structure that
contains the following information:

`type`

The supported types of
`scanMode`. Accepted values are
`POLL` and
`EXCEPTION`.

`rate`

The sampling interval for the scan
mode.

`timestampToReturn`

The source of the timestamp. You can choose
the following options:

- `SOURCE_TIME` – Uses the
  timestamp from your device.
- `SERVER_TIME` – Uses the
  timestamp from your server.

###### Note

Use `TimestampToReturn` with
version 2.5.0 or later of the
IoT SiteWise OPC UA collector component. If you use this
feature with earlier versions, configuration
updates fail. For more information, see [Update the version of an AWS IoT SiteWise
component](manage-gateways-ggv2.md#update-component-version "manage-gateways-ggv2.md#update-component-version").

`nodeFilterRuleDefinitions`

(Optional) A list of node paths to include in
the property group. Property groups can't overlap.
If you don't specify a value for this field, the
group contains all paths under the root, and you
can't create additional property groups. The
`nodeFilterRuleDefinitions` structure
contains the following information:

`type`

`OpcUaRootPath` is the only
supported type. This specifies that the value of
`rootPath` is a path relative to the
root of the OPC UA browsing space.

`rootPath`

A comma-delimited list that specifies the
paths (relative to the root) to include in the
property group.

### Additional capability

configuration examples for Classic streams, V2 gateways (AWS CLI)

The following example defines an OPC UA SiteWise Edge gateway capability
configuration from a payload stored in a JSON file.

```
aws iotsitewise update-gateway-capability-configuration \
--capability-namespace "iotsitewise:opcuacollector:2" \
--capability-configuration file://opc-ua-configuration.json
```

###### Example: OPC UA source configuration

The following `opc-ua-configuration.json` file
defines a basic, insecure OPC UA source configuration.

```
{
    "sources": [
        {
            "name": "Wind Farm #1",
            "endpoint": {
                "certificateTrust": {
                    "type": "TrustAny"
                },
                "endpointUri": "opc.tcp://203.0.113.0:49320",
                "securityPolicy": "NONE",
                "messageSecurityMode": "NONE",
                "identityProvider": {
                    "type": "Anonymous"
                },
                "nodeFilterRules": []
            },
            "measurementDataStreamPrefix": ""
        }
    ]
}
```

###### Example: OPC UA source configuration with defined property

groups

The following `opc-ua-configuration.json` file
defines a basic, insecure OPC UA source configuration with defined
property groups.

```
{
    "sources": [
        {
            "name": "source1",
            "endpoint": {
                "certificateTrust": {
                    "type": "TrustAny"
                },
                "endpointUri": "opc.tcp://10.0.0.9:49320",
                "securityPolicy": "NONE",
                "messageSecurityMode": "NONE",
                "identityProvider": {
                    "type": "Anonymous"
                },
                "nodeFilterRules": [
                    {
                        "action": "INCLUDE",
                        "definition": {
                            "type": "OpcUaRootPath",
                            "rootPath": "/Utilities/Tank"
                        }
                    }
                ]
            },
            "measurementDataStreamPrefix": "propertyGroups",
            "propertyGroups": [
                 {
                     "name": "Deadband_Abs_5",
                     "nodeFilterRuleDefinitions": [
                         {
                             "type": "OpcUaRootPath",
                             "rootPath": "/Utilities/Tank/Temperature/TT-001"
                         },
                         {
                             "type": "OpcUaRootPath",
                             "rootPath": "/Utilities/Tank/Temperature/TT-002"
                         }
                     ],
                     "deadband": {
                         "type":"ABSOLUTE",
                         "value": 5.0,
                         "timeoutMilliseconds": 120000
                     }
                 },
                 {
                     "name": "Polling_10s",
                     "nodeFilterRuleDefinitions": [
                         {
                             "type": "OpcUaRootPath",
                             "rootPath": "/Utilities/Tank/Pressure/PT-001"
                         }
                     ],
                     "scanMode": {
                         "type": "POLL",
                         "rate": 10000
                     }
                 },
                 {
                     "name": "Percent_Deadband_Timeout_90s",
                     "nodeFilterRuleDefinitions": [
                         {
                             "type": "OpcUaRootPath",
                             "rootPath": "/Utilities/Tank/Flow/FT-*"
                         }
                     ],
                     "deadband": {
                         "type":"PERCENT",
                         "value": 5.0,
                         "eguMin": -100,
                         "eguMax": 100,
                         "timeoutMilliseconds": 90000
                     }
                 }
             ]
        }
    ]
}
```

###### Example: OPC UA source configuration with properties

The following JSON example for
`opc-ua-configuration.json` defines an OPC UA
source configuration with the following properties:

- Trusts any certificate.
- Uses the `BASIC256` security policy to secure
  messages.
- Uses the `SIGN_AND_ENCRYPT` mode to secure
  connections.
- Uses authentication credentials stored in a Secrets Manager
  secret.
- Filters out data streams except those whose path starts
  with `/WindFarm/2/WindTurbine/`.
- Adds `/Washington` to the start of every data
  stream path to distinguish between this "Wind Farm #2" and a
  "Wind Farm #2" in another area.

```
{
    "sources": [
        {
            "name": "Wind Farm #2",
            "endpoint": {
                "certificateTrust": {
                    "type": "TrustAny"
                },
                "endpointUri": "opc.tcp://203.0.113.1:49320",
                "securityPolicy": "BASIC256",
                "messageSecurityMode": "SIGN_AND_ENCRYPT",
                "identityProvider": {
                    "type": "Username",
                    "usernameSecretArn": "arn:aws:secretsmanager:`region`:123456789012:secret:greengrass-windfarm2-auth-1ABCDE"
                },
                "nodeFilterRules": [
                  {
                      "action": "INCLUDE",
                      "definition": {
                          "type": "OpcUaRootPath",
                          "rootPath": "/WindFarm/2/WindTurbine/"
                    }
                  }
                ]
            },
            "measurementDataStreamPrefix": "/Washington"
        }
    ]
}
```

###### Example: OPC UA source configuration with certificate trust

The following JSON example for
`opc-ua-configuration.json` defines an OPC UA
source configuration with the following properties:

- Trusts a given X.509 certificate.
- Uses the `BASIC256` security policy to secure
  messages.
- Uses the `SIGN_AND_ENCRYPT` mode to secure
  connections.

```
{
    "sources": [
        {
            "name": "Wind Farm #3",
            "endpoint": {
                "certificateTrust": {
                    "type": "X509",
                    "certificateBody": "-----BEGIN CERTIFICATE-----
          MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w
 0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZ
 WF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIw
 EAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5
 jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBh
 MCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBb
 WF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMx
 HzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQE
 BBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVI
 k60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQ
 ITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nr
 AgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auN
 KyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6Guo
 EDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw
 3rrszlaEXAMPLE=
          -----END CERTIFICATE-----",
                    "certificateChain": "-----BEGIN CERTIFICATE-----
          MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w
 0BAQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZ
 WF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIw
 EAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5
 jb20wHhcNMTEwNDI1MjA0NTIxWhcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBh
 MCVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBb
 WF6b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMx
 HzAdBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQE
 BBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVI
 k60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9TrDHudUZg3qX4waLG5M43q7Wgc/MbQ
 ITxOUSQv7c7ugFFDzQGBzZswY6786m86gpEIbb3OhjZnzcvQAaRHhdlQWIMm2nr
 AgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4nUhVVxYUntneD9+h8Mg9q6q+auN
 KyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FkbFFBjvSfpJIlJ00zbhNYS5f6Guo
 EDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTbNYiytVbZPQUQ5Yaxu2jXnimvw
 3rrszlaEXAMPLE=
          -----END CERTIFICATE-----"
                },
                "endpointUri": "opc.tcp://203.0.113.2:49320",
                "securityPolicy": "BASIC256",
                "messageSecurityMode": "SIGN_AND_ENCRYPT",
                "identityProvider": {
                    "type": "Anonymous"
                },
                "nodeFilterRules": []
              },
            "measurementDataStreamPrefix": ""

        }
    ]
}
```
