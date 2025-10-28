# Monitor the last known state of your vehicles

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can monitor the last known state of your vehicles in near-real time by creating
state templates and associating them with your vehicles. Vehicles associated with state
templates stream telemetry data with either an `onChange` or `periodic` update
strategy. With an on-change update strategy, the associated vehicles stream telemetry data when there is a change. During a periodic update
strategy, the associated vehicles stream telemetry data during a specified time period.

With on-demand operations, you can request the current vehicle state at one time (fetch). You can also activate or deactivate previously deployed state templates to start or stop
reporting vehicle state data. Last known state operations are performed using the AWS IoT command
APIs.

Each state template contains the following information.

`name`

The unique alias of the state template.

`signalCatalogArn`

The Amazon Resource Name (ARN) of the signal catalog associated with the
state template.

`stateTemplateProperties`

A list of signals from which data is collected. The state template properties determine the specific signal updates the vehicle sends to the cloud.

`dataExtraDimensions`

A list of vehicle attributes to be included in the protocol buffers (Protobuf) encoded processed
data.

`metadataExtraDimensions`

A list of vehicle attributes to be published with the processed data as an MQTT 5
user property.

`id`

A unique, service-generated identifier.

For methods to collect data sent by a vehicle that uses the Edge Agent for AWS IoT FleetWise software, see [Process last known state vehicle
data using MQTT messaging](process-last-known-state-vehicle-data.md "process-last-known-state-vehicle-data.md"). For more information about how to associate a state
template with a vehicle, see [Create an AWS IoT FleetWise vehicle](create-vehicle.md "create-vehicle.md").

###### Topics

- [Create an AWS IoT FleetWise state template](state-templates.md "state-templates.md")
- [Update an AWS IoT FleetWise state template](update-state-template.md "update-state-template.md")
- [Delete an AWS IoT FleetWise state template](delete-state-template.md "delete-state-template.md")
- [Get AWS IoT FleetWise state template information](get-state-template.md "get-state-template.md")
- [State template operations for data
  collection and processing](state-template-api-operations.md "state-template-api-operations.md")
