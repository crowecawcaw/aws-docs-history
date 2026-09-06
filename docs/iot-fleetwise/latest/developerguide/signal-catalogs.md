

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Manage AWS IoT FleetWise signal catalogs
<a name="signal-catalogs"></a>

**Note**  
You can download a [demo script](https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-nodes.py) to convert ROS 2 messages to VSS .json files that are compatible with the signal catalog. For more information, see the [*Vision System Data Developer Guide*](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb).

A signal catalog is a collection of standardized signals that can be reused to create vehicle models. AWS IoT FleetWise supports [Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/introduction/overview/) that you can follow to define signals. A signal can be any of the following type.

**Attribute**  <a name="attribute-definition"></a>
Attributes represent static information that generally doesn't change, such as manufacturer and manufacturing date.

**Branch**  <a name="branch-definition"></a>
Branches represent signals in a nested structure. Branches demonstrate signal hierarchies. For example, the `Vehicle` branch has a child branch, `Powertrain`. The `Powertrain` branch has a child branch, `combustionEngine`. To locate the `combustionEngine` branch, use the `Vehicle.Powertrain.combustionEngine` expression.

**Sensor**  <a name="sensor-definition"></a>
Sensor data reports the current state of the vehicle and change over time, as the state of the vehicle changes, such as fluid levels, temperatures, vibrations, or voltage.

**Actuator**  <a name="actuator-definition"></a>
Actuator data reports the state of a vehicle device, such as motors, heaters, and door locks. Changing the state of a vehicle device can update actuator data. For example, you can define an actuator to represent the heater. The actuator receives new data when you turn on or off the heater.

**Custom structure**  <a name="custom-structure-definition"></a>
A custom structure (also known as a struct) represents a complex or higher-order data structure. It facilitates logical binding or grouping of data that originates from the same source. A struct is used when data is read or written in an atomic operation, such as to represent a complex data type or higher-order shape.  
A signal of struct type is defined in the signal catalog using a reference to a struct data type instead of a primitive data type. Structs can be used for all types of signals including sensors, attributes, actuators, and vision system data types. If a signal of struct type is sent or received, AWS IoT FleetWise expects all included items to have valid values, so all items are mandatory. For example, if a struct contains the items Vehicle.Camera.Image.height, Vehicle.Camera.Image.width, and Vehicle.Camera.Image.data – it's expected that the sent signal contains values for all of these items.  
Vision system data is in preview release and is subject to change.

**Custom property**  <a name="custom-property-definition"></a>
A custom property represents a member of the complex data structure. The data type of the property can be either primitive or another struct.  
When representing a higher-order shape using a struct and custom property, the intended higher-order shape is always defined and visioned as a tree structure. The custom property is used to define all the leaf nodes while the struct is used to define all the non-leaf nodes.

**Note**  
<a name="console-auto-create-signal-catalog"></a>If you use the AWS IoT FleetWise console to create the first vehicle model, you don't need to manually create a signal catalog. When you create your first vehicle model, AWS IoT FleetWise automatically creates a signal catalog for you. For more information, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md).
<a name="console-auto-update-signal-catalog"></a>If you use the AWS IoT FleetWise console to create a vehicle model, you can upload .dbc files to import signals. .dbc is a file format that Controller Area Network (CAN bus) databases support. After the vehicle model is created, new signals are automatically added to the signal catalog. For more information, see [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md).
<a name="signal-catalog-quota"></a>AWS IoT FleetWise currently supports a signal catalog for each AWS account per Region.

AWS IoT FleetWise provides the following API operations that you can use to create and manage signal catalogs.
+ [CreateSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateSignalCatalog.html) – Creates a new signal catalog.
+ [ImportSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ImportSignalCatalog.html) – Imports signals to create a signal catalog by uploading a .json file. Signals must be defined by following VSS and saved in the JSON format.
+ [UpdateSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateSignalCatalog.html) – Updates an existing signal catalog by updating, removing, or adding signals.
+ [DeleteSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteSignalCatalog.html) – Deletes an existing signal catalog.
+ [ListSignalCatalogs](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogs.html) – Retrieves a paginated list of summaries of all signal catalogs.
+ [ListSignalCatalogNodes](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogNodes.html) – Retrieves a paginated list of summaries of all signals (nodes) in a given signal catalog.
+ [GetSignalCatalog](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetSignalCatalog.html) – Retrieves information about a signal catalog.

**Topics**
+ [Configure AWS IoT FleetWise signals](define-signal.md)
+ [Create an AWS IoT FleetWise signal catalog](create-signal-catalog.md)
+ [Import an AWS IoT FleetWise signal catalog](import-signal.md)
+ [Update an AWS IoT FleetWise signal catalog](update-signal-catalog.md)
+ [Delete an AWS IoT FleetWise signal catalog](delete-signal-catalog.md)
+ [Get AWS IoT FleetWise signal catalog information](get-signal-catalog-information.md)