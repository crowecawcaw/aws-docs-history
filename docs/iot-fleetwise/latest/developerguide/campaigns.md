# Collect AWS IoT FleetWise data with campaigns

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

A campaign is an orchestration of data collection rules. Campaigns give the Edge Agent for AWS IoT FleetWise software
instructions on how to select, collect, and transfer data to the cloud.

You create campaigns in the cloud. After you or your team has approved a campaign, AWS IoT FleetWise sets the campaign as ready to deploy,
and it will be deployed on the next vehicle check-in. You can choose to deploy a campaign to a vehicle or a fleet of vehicles. The Edge Agent software
doesn't start collecting data until a running campaign is deployed to the vehicle.

###### Important

Campaigns won't work until you have the following.

- The Edge Agent software is running in your vehicle. For more information about how to
  develop, install, and work with the Edge Agent software, do the following.
  1.  Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
  2.  On the service home page, in the **Get started with AWS IoT FleetWise**
      section, choose **Explore Edge Agent**.

- You've set up AWS IoT Core to provision your vehicle. For more information, see
  [Provision AWS IoT FleetWise vehicles](provision-vehicles.md "provision-vehicles.md").

###### Note

You can also [Monitor the last known state of your vehicles](last-known-state.md "last-known-state.md") (not fleets)
in near real time using state templates that allow you to stream telemetry data with either an
"On Change" or "Periodic" update strategy. The capability also provides "On Demand" features to
activate or deactivate previously deployed templates or request the current vehicle state one-time
(fetch).

Access to last known state is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

Each campaign contains the following information.

`signalCatalogArn`

The Amazon Resource Name (ARN) of the signal catalog associated with the
campaign.

(Optional) `tags`

Tags are metadata that can be used to manage the campaign. You can assign the same tag to resources from different services to indicate that the resources are related.

`TargetArn`

The ARN of a vehicle or fleet to which the campaign is deployed.

`name`

A unique name that helps identify the campaign.

`collectionScheme`

The data collection schemes give Edge Agent software instructions on what data to
collect or when to collect it. AWS IoT FleetWise currently supports the condition-based
collection scheme and the time-based collection scheme.

- `conditionBasedCollectionScheme` – the
  condition-based collection scheme uses a logical expression to recognize
  what data to collect. The Edge Agent software collects data when the condition is
  met.
  - `expression` – the logical expression used
    to recognize what data to collect. For example, if the
    `$variable.`myVehicle.InVehicleTemperature` >
50.0` expression is specified, the Edge Agent software collects
    temperature values that are greater than 50.0. For instructions
    on how to write expressions, see [Logical expressions for AWS IoT FleetWise
    campaigns](logical-expression.md "logical-expression.md").
  - (Optional) `conditionLanguageVersion` – the
    version of the conditional expression language.
  - (Optional) `minimumTriggerIntervalMs` – the
    minimum duration of time between two data collection events, in
    milliseconds. If a signal changes often, you might collect data
    at a slower rate.
  - (Optional) `triggerMode` – can be one of the
    following values:
    - `RISING_EDGE` – the Edge Agent software
      collects data only when the condition is met for the
      first time. For example,
      `$variable.`myVehicle.AirBagDeployed` ==
true`.
    - `ALWAYS` – Edge Agent software collects data
      whenever the condition is met.

- `timeBasedCollectionScheme` – when you define a
  time-based collection scheme, specify a time period in milliseconds. The
  Edge Agent software uses the time period to decide how often to collect
  data. For example, if the time period is 120,000 milliseconds, the Edge
  Agent software collects data once every two minutes.
  - `periodMs` – the time period (in
    milliseconds) to decide how often to collect data.

(Optional) `compression`

To save wireless bandwidth and reduce network traffic, you can specify [SNAPPY](https://opensource.google/projects/snappy "https://opensource.google/projects/snappy") to compress
data in vehicles.

By default (`OFF`), the Edge Agent software doesn't compress data.

`dataDestinationConfigs`

Choose the single destination where the campaign will transfer vehicle data. You can
send the data to an [MQTT topic](../../../iot/latest/developerguide/topics.md "../../../iot/latest/developerguide/topics.md"), or store it in Amazon S3 or Amazon Timestream.

MQTT (Message Queuing Telemetry Transport) is a lightweight and widely adopted
messaging protocol. You can publish data to an MQTT topic to stand up your own event-driven architectures using AWS IoT rules. AWS IoT support for MQTT
is based on the [MQTT v3.1.1 specification](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html "http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html") and the [MQTT v5.0 specification](http://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html "http://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html"),
with some differences. For more information, see [MQTT differences](../../../iot/latest/developerguide/mqtt.md#mqtt-differences.html "../../../iot/latest/developerguide/mqtt.md#mqtt-differences.html").

S3 can be a cost-effective data storage mechanism that offers durable data management
capabilities and downstream data services. You can use S3 for data related to driving
behaviors or analyzing long-term maintenance.

Timestream is a data persistence mechanism that can help you identify trends and
patterns in near real time. You can use Timestream for time-series data, such as to
analyze historical trends in vehicle speed or braking.

###### Note

Amazon Timestream is not available in the Asia Pacific (Mumbai) Region.

(Optional) `dataExtraDimensions`

You can add one or more attributes to provide additional information for a
signal.

(Optional) `dataPartitions`

Create a data partition to temporarily store signal data on a vehicle. You
configure when and how to forward the data to the cloud.

- Specify how AWS IoT FleetWise stores the data on a vehicle or fleet by defining
  the maximum storage size, minimum time to live, and storage
  location.
- The campaign `spoolingMode` must be
  `TO_DISK`.
- Uploading configurations include defining the version of the condition
  language and the logical expression.

(Optional) `description`

Add a description to help identify the campaign's purpose.

(Optional) `diagnosticsMode`

When the diagnostics mode is configured to `SEND_ACTIVE_DTCS`, the
campaign sends stored, standard diagnostic trouble codes (DTCs) that help
identify what is wrong with your vehicle. For example, P0097 indicates the
engine control module (ECM) has determined that the intake air temperature
sensor 2 (IAT2) input is lower than the normal sensor range.

By default (`OFF`), the Edge Agent software doesn't send diagnostic
codes.

(Optional) `expiryTime`

Define the expiration date for your campaign. When the campaign expires, the
Edge Agent software stops collecting data as specified in this campaign. If multiple
campaigns are deployed to the vehicle, the Edge Agent software uses other campaigns to
collect data.

Default value: `253402243200` (December 31, 9999, 00:00:00
UTC)

(Optional) `postTriggerCollectionDuration`

You can define a post-trigger collection duration, so that the Edge Agent software
continues collecting data for a specified period after a scheme is invoked. For
example, if a condition-based collection scheme with the following expression is
invoked: `$variable.`myVehicle.Engine.RPM` > 7000.0`, the Edge Agent software
continues to collect revolutions per minute (RPM) values for the engine. Even if
the RPM only goes higher than 7000 once, it might indicate that there's a
mechanical issue. In this case, you might want the Edge Agent software to continue
collecting data to help monitor the condition.

Default value: `0`

(Optional) `priority`

Specify an integer to indicate the priority level of the campaign. Campaigns
with a smaller number are higher priorities. If you deploy multiple campaigns to
a vehicle, the campaigns that are higher priorities are initiated first.

Default value: `0`

(Optional) `signalsToCollect`

A list of signals from which data is collected when the data collection scheme
is invoked.

- `name` – the name of the signal from which data is
  collected when the data collection scheme is invoked.
- `dataPartitionId` – the ID of the data partition to
  use in the signal. The ID must match one of the IDs provided in
  `dataPartitions`. If you upload a signal as a condition
  in your data partition, then those same signals must be included in
  `signalsToCollect`.
- (Optional) `maxSampleCount` – the maximum number of
  data samples that the Edge Agent software collects and transfers to the cloud
  when the data collection scheme is invoked.
- (Optional) `minimumSamplingIntervalMs` – the minimum
  duration of time between two data sample collection events, in
  milliseconds. If a signal changes often, you can use this parameter to
  collect data at a slower rate.

Valid range: 0‐4294967295

(Optional) `spoolingMode`

If `spoolingMode` is configured to `TO_DISK`, the
Edge Agent software temporarily stores data locally when a vehicle isn't connected to the
cloud. After the connection is reestablished, the data stored locally is
automatically transferred to the cloud.

Default value: `OFF`

(Optional) `startTime`

An approved campaign is activated at the start time.

Default value: `0`

The status of a campaign can be one of the following values.

- `CREATING` – AWS IoT FleetWise is processing your request to create the
  campaign.
- `WAITING_FOR_APPROVAL` – After a campaign is created, it enters
  the `WAITING_FOR_APPROVAL` state. To approve the campaign, use the
  `UpdateCampaign` API operation. After the campaign is approved,
  AWS IoT FleetWise automatically deploys the campaign to the target vehicle or fleet. For
  more information, see [Update an AWS IoT FleetWise campaign](update-campaign-cli.md "update-campaign-cli.md").
- `RUNNING` – The campaign is active.
- `SUSPENDED` – The campaign is suspended. To resume the campaign,
  use the `UpdateCampaign` API operation.
  AWS IoT FleetWise provides the following API operations that you can use to create and manage
  campaigns.

- [CreateCampaign](../APIReference/API_CreateCampaign.md "../APIReference/API_CreateCampaign.md") – Creates a new campaign.
- [UpdateCampaign](../APIReference/API_UpdateCampaign.md "../APIReference/API_UpdateCampaign.md") – Updates an existing campaign. After a campaign
  is created, you must use this API operation to approve the campaign.
- [DeleteCampaign](../APIReference/API_DeleteCampaign.md "../APIReference/API_DeleteCampaign.md") – Deletes an existing campaign.
- [ListCampaigns](../APIReference/API_ListCampaigns.md "../APIReference/API_ListCampaigns.md") – Retrieves a paginated list of summaries for all
  campaigns.
- [GetCampaign](../APIReference/API_GetCampaign.md "../APIReference/API_GetCampaign.md")
  – Retrieves information about a campaign.

###### Tutorials

- [Create an AWS IoT FleetWise campaign](create-campaign.md "create-campaign.md")
- [Update an AWS IoT FleetWise campaign](update-campaign-cli.md "update-campaign-cli.md")
- [Delete an AWS IoT FleetWise campaign](delete-campaign.md "delete-campaign.md")
- [Get AWS IoT FleetWise campaign information](get-campaign-information-cli.md "get-campaign-information-cli.md")
- [Store and forward campaign data](store-and-forward.md "store-and-forward.md")
- [Collect diagnostic trouble code data using AWS IoT FleetWise](diagnostic-trouble-codes.md "diagnostic-trouble-codes.md")
- [Visualize AWS IoT FleetWise vehicle data](process-visualize-data.md "process-visualize-data.md")
