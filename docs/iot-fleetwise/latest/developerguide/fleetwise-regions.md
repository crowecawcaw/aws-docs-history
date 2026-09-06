

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# AWS Region and feature availability in AWS IoT FleetWise
<a name="fleetwise-regions"></a>

For a list of AWS Regions that support AWS IoT FleetWise, see [AWS IoT FleetWise endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iotfleetwise.html). AWS IoT FleetWise features differ in their regional support.

**Note**  
Access to the Asia Pacific (Mumbai) Region and some AWS IoT FleetWise features are currently gated. To request access to this AWS Region and all gated features, contact your account manager or the [AWS Support Center](https://console.aws.amazon.com/support/home#/).

The following table shows feature support by Region:


| Features/Regions | US East (N. Virginia) | Europe (Frankfurt) | Asia Pacific (Mumbai) NOTE: Gated access only | 
| --- | --- | --- | --- | 
| [Signal catalogs](signal-catalogs.md) | Yes | Yes | Gated | 
| [Vehicle models](vehicle-models.md) | Yes | Yes | Gated | 
| [Decoder manifests](decoder-manifests.md) | Yes | Yes | Gated | 
| [Vehicles](vehicles.md) | Yes | Yes | Gated | 
| [Fleets](fleets.md) | Yes | Yes | Gated | 
| [Campaigns](campaigns.md) | Yes | Yes | Gated | 
| [Vision system data](define-signal.md) (in preview release) | Yes | Yes | Gated | 
| [MQTT topic as a campaign data destination](create-campaign.md) | Gated | Gated | Gated | 
| [Store and forward](store-and-forward.md) | Gated | Gated | Gated | 
| [Commands](remote-commands.md) | Gated | Gated | Gated | 
| [Last known state](last-known-state.md) | Gated | Gated | Gated | 
| [Network agnostic data collection using a custom decoding interface](network-agnostic-data-collection.md) | Gated | Gated | Gated | 
| [Diagnostic trouble code (DTC) fetching\*](diagnostic-trouble-codes.md) | Gated | Gated | Gated | 

\*DTC fetching offers a range of capabilities that go beyond basic DTC data retrieval. This functionality includes custom features that enable you to define functions at the edge and invoke them by name within condition-based campaign expressions. Additionally, it supports the collection of unbounded strings, providing flexible string data type handling. The Edge Agent can fetch data either on a periodic basis or triggered by specific conditions, enhancing its adaptability and efficiency in data collection processes. For more information, see the [custom function guide](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/custom-function-dev-guide.md) and the [DTC data collection reference implementation](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md#dtc_query-function-implementation) in the *Edge Agent Developer Guide*.