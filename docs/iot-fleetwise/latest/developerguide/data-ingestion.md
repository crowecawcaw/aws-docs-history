# Ingest AWS IoT FleetWise data to the cloud

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The Edge Agent for AWS IoT FleetWise software, when installed and running in vehicles, is designed to facilitate secure
communication between your vehicles and the cloud.

###### Note

- AWS IoT FleetWise is not intended for use in, or in association with, the operation of
  any hazardous environments or critical systems that may lead to serious bodily
  injury or death or cause environmental or property damage. Vehicle data
  collected through your use of AWS IoT FleetWise is for informational purposes only, and
  you may not use AWS IoT FleetWise to control or operate vehicle functions.
- Vehicle data collected through your use of AWS IoT FleetWise should be evaluated for
  accuracy as appropriate for your use case, including for purposes of meeting any
  compliance obligations you may have under applicable vehicle safety regulations
  (such as safety monitoring and reporting obligations). Such evaluation should
  include collecting and reviewing information through other industry standard
  means and sources (such as reports from drivers of vehicles).
  To ingest data to the cloud, do the following:

1. Develop and install your Edge Agent for AWS IoT FleetWise software in your vehicle. For more information
   about how to work with the Edge Agent software, do the following to download the [_Edge Agent for AWS IoT FleetWise software Developer Guide_](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-dev-guide.md "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-dev-guide.md").
   1. Navigate to the [AWS IoT FleetWise
      console](https://console.aws.amazon.com/iotfleetwise/home#/ "https://console.aws.amazon.com/iotfleetwise/home#/").
   2. On the service home page, in the **Get started with
      AWS IoT FleetWise** section, choose **Explore Edge
      Agent**.

2. Create or import a signal catalog containing signals that you'll use to create a
   vehicle model. For more information, see [Create an AWS IoT FleetWise signal catalog](create-signal-catalog.md "create-signal-catalog.md") and [Import a signal catalog (AWS CLI)](import-signal.md#import-signal-catalog "import-signal.md#import-signal-catalog").

###### Note

    * If you use the AWS IoT FleetWise
     console to create the first vehicle model, you don't need to manually
     create a signal catalog. When you create your first vehicle model,
     AWS IoT FleetWise automatically creates a signal catalog for you. For more
     information, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md "create-vehicle-model.md").
    * AWS IoT FleetWise currently supports a signal catalog for each AWS account
     per AWS Region.

3. Use signals in the signal catalog to create a vehicle model. For more information,
   see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md "create-vehicle-model.md").

###### Note

    * If you use the AWS IoT FleetWise
     console to create a vehicle model, you can upload .dbc files to import
     signals. .dbc is a file format that Controller Area Network (CAN bus)
     databases support. After the vehicle model is created, new signals are
     automatically added to the signal catalog. For more information, see
     [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md "create-vehicle-model.md").
    * If you use the `CreateModelManifest` API operation to
     create a vehicle model, you must use the
     `UpdateModelManifest` API operation to activate the
     vehicle model. For more information, see [Update an AWS IoT FleetWise vehicle model](update-vehicle-model-cli.md "update-vehicle-model-cli.md").
    * If you use the AWS IoT FleetWise console to create a vehicle model, AWS IoT FleetWise
     automatically activates the vehicle model for you.

4. Create a decoder manifest. The decoder manifest contains decoding information for
   every signal specified in the vehicle model that you created in the previous step.
   The decoder manifest is associated with the vehicle model that you created. For more
   information, see [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md "decoder-manifests.md").

###### Note

    * If you use the `CreateDecoderManifest` API operation to
     create a decoder manifest, you must use the
     `UpdateDecoderManifest` API operation to activate the
     decoder manifest. For more information, see [Update an AWS IoT FleetWise decoder manifest](update-decoder-manifest.md "update-decoder-manifest.md").
    * If you use the AWS IoT FleetWise console to create a decoder manifest,
     AWS IoT FleetWise automatically activates the decoder manifest for you.

5. Create vehicles from the vehicle model. Vehicles created from the same vehicle
   model inherit the same group of signals. You must use AWS IoT Core to provision your
   vehicle before you can ingest data to the cloud. For more information, see [Manage AWS IoT FleetWise vehicles](vehicles.md "vehicles.md").
6. (Optional) Create a fleet to represent a group of vehicles, and then associate
   individual vehicles with the fleet. This helps you manage multiple vehicles at the
   same time. For more information, see [Manage fleets in AWS IoT FleetWise](fleets.md "fleets.md").
7. (Optional) Create campaigns. Campaigns are deployed to a vehicle or a fleet of vehicles.
   Campaigns give the Edge Agent software instructions on how to select, collect, and transfer
   data to the cloud. For more information, see [Collect AWS IoT FleetWise data with campaigns](campaigns.md "campaigns.md"). You can create campaigns, state templates (below), or
   both to collect data.

###### Note

You must use the `UpdateCampaign` API operation to approve the
campaign before AWS IoT FleetWise can deploy it to the vehicle or fleet. For more
information, see [Update an AWS IoT FleetWise campaign](update-campaign-cli.md "update-campaign-cli.md"). 8. (Optional) Create state templates. State templates are deployed to a vehicle. State
templates provide a mechanism for Vehicle owners to track the state of their vehicle. For
more information, see [Monitor the last known state of your vehicles](last-known-state.md "last-known-state.md").
The Edge Agent software transfers vehicle data to AWS IoT Core using an MQTT topic that you choose. To send
the data to AWS IoT FleetWise for campaigns, it uses the reserved topic
`$aws/iotfleetwise/vehicles/`vehicleName`/signals`. For Last
Known State, the Edge Agent uses the reserved topic
`$aws/iotfleetwise/vehicles/`vehicleName`/last_known_states/data`.
For more information about how the ingested data is processed, see [Visualize AWS IoT FleetWise vehicle data](process-visualize-data.md "process-visualize-data.md").
