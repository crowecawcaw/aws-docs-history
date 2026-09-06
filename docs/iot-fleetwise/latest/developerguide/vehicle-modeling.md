

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Model AWS IoT FleetWise vehicles
<a name="vehicle-modeling"></a>

AWS IoT FleetWise provides a vehicle modeling framework that you can use to build virtual representations of your vehicles in the cloud. Signals, signal catalogs, vehicle models, and decoder manifests are the core components that you work with to model your vehicles.

![Image showing entities of the AWS IoT FleetWise domain and their relationships.](http://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/images/FleetWise-Domain-Entity-Relationships.png)


**Signal**  <a name="signal-definition"></a>
Signals are fundamental structures that you define to contain vehicle data and its metadata. A signal can be an attribute, a branch, a sensor, or an actuator. For example, you can create a sensor to receive in-vehicle temperature values, and to store its metadata, including a sensor name, a data type, and a unit. For more information, see [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md).

**Signal catalog**  <a name="signal-catalog-definition"></a>
A signal catalog contains a collection of signals. Signals in a signal catalog can be used to model vehicles that use different protocols and data formats. For example, there are two cars made by different automakers: one uses the Control Area Network (CAN bus) protocol; the other one uses the On-board Diagnostics (OBD) protocol. You can define a sensor in the signal catalog to receive in-vehicle temperature values. This sensor can be used to represent the thermocouples in both cars. For more information, see [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md).

**Vehicle model (model manifest)**  <a name="vehicle-model-definition"></a>
Vehicle models are declarative structures that you can use to standardize the format of your vehicles and to define relationships between signals in the vehicles. Vehicle models enforce consistent information across multiple vehicles of the same type. You add signals to create vehicle models. For more information, see [Manage AWS IoT FleetWise vehicle models](vehicle-models.md).

**Decoder manifest**  <a name="decoder-manifest-definition"></a>
Decoder manifests contain decoding information for each signal in vehicle models. Sensors and actuators in vehicles transmit low-level messages (binary data). With decoder manifests, AWS IoT FleetWise is able to transform binary data into human-readable values. Every decoder manifest is associated with a vehicle model. For more information, see [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md).

You can use the AWS IoT FleetWise console or API to model vehicles in the following way.

1. <a name="shared-create-import-signal-catalog"></a>Create or import a signal catalog containing signals that you'll use to create a vehicle model. For more information, see [Create an AWS IoT FleetWise signal catalog](create-signal-catalog.md) and [Import a signal catalog (AWS CLI)](import-signal.md#import-signal-catalog).
**Note**  
<a name="console-auto-create-signal-catalog"></a>If you use the AWS IoT FleetWise console to create the first vehicle model, you don't need to manually create a signal catalog. When you create your first vehicle model, AWS IoT FleetWise automatically creates a signal catalog for you. For more information, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md).
AWS IoT FleetWise currently supports a signal catalog for each AWS account per AWS Region.

1. <a name="shared-create-vehicle-model"></a>Use signals in the signal catalog to create a vehicle model. For more information, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md).
**Note**  
<a name="console-auto-update-signal-catalog"></a>If you use the AWS IoT FleetWise console to create a vehicle model, you can upload .dbc files to import signals. .dbc is a file format that Controller Area Network (CAN bus) databases support. After the vehicle model is created, new signals are automatically added to the signal catalog. For more information, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md).
If you use the `CreateModelManifest` API operation to create a vehicle model, you must use the `UpdateModelManifest` API operation to activate the vehicle model. For more information, see [Update an AWS IoT FleetWise vehicle model](update-vehicle-model-cli.md).
If you use the AWS IoT FleetWise console to create a vehicle model, AWS IoT FleetWise automatically activates the vehicle model for you.

1. <a name="shared-create-decoder-manifest"></a>Create a decoder manifest. The decoder manifest contains decoding information for every signal specified in the vehicle model that you created in the previous step. The decoder manifest is associated with the vehicle model that you created. For more information, see [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md).
**Note**  
If you use the `CreateDecoderManifest` API operation to create a decoder manifest, you must use the `UpdateDecoderManifest` API operation to activate the decoder manifest. For more information, see [Update an AWS IoT FleetWise decoder manifest](update-decoder-manifest.md).
If you use the AWS IoT FleetWise console to create a decoder manifest, AWS IoT FleetWise automatically activates the decoder manifest for you.

CAN bus databases support the .dbc file format. You might upload .dbc files to import signals and signal decoders. To get an example .dbc file, do the following.

**To get a .dbc file**

1. Download the [EngineSignals.zip](samples/EngineSignals.zip).

1. Navigate to the directory where you downloaded the `EngineSignals.zip` file.

1. Unzip the file and save it locally as `EngineSignals.dbc`.

**Topics**
+ [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md)
+ [Manage AWS IoT FleetWise vehicle models](vehicle-models.md)
+ [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md)