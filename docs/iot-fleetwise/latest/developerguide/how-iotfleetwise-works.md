# Key concepts and features of AWS IoT FleetWise

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The following sections provide an overview of AWS IoT FleetWise service components and how they interact.

After you read this introduction, see the [Set up AWS IoT FleetWise](setting-up.md "setting-up.md") section to learn how to set up AWS IoT FleetWise.

###### Topics

- [Key concepts](#key-concepts "#key-concepts")
- [Features of AWS IoT FleetWise](#iotfleetwise-feature-overview "#iotfleetwise-feature-overview")

## Key concepts

AWS IoT FleetWise provides a vehicle modeling framework for you to model your vehicle and its
sensors and actuators in the cloud. To enable the secure communication between your
vehicle and the cloud, AWS IoT FleetWise also provides a reference implementation to help you
develop Edge Agent software that you can install in your vehicle. You can define data
collection schemes in the cloud and deploy them to your vehicle. The Edge Agent software running
in your vehicle uses data collection schemes to control what data to collect and when to
transfer it to the cloud.

The following are the core concepts of AWS IoT FleetWise.

**Signal**

Signals are fundamental structures that you define to contain vehicle data and
its metadata. A signal can be an attribute, a branch, a sensor, or an actuator.
For example, you can create a sensor to receive in-vehicle temperature values,
and to store its metadata, including a sensor name, a data type, and a unit. For
more information, see [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md "signal-catalogs.md").

**Attribute**

Attributes represent static information that generally doesn't change, such as
manufacturer and manufacturing date.

**Branch**

Branches represent signals in a nested structure. Branches demonstrate signal
hierarchies. For example, the `Vehicle` branch has a child branch,
`Powertrain`. The `Powertrain` branch has a child
branch, `combustionEngine`. To locate the
`combustionEngine` branch, use the
`Vehicle.Powertrain.combustionEngine` expression.

**Sensor**

Sensor data reports the current state of the vehicle and change over time, as
the state of the vehicle changes, such as fluid levels, temperatures,
vibrations, or voltage.

**Actuator**

Actuator data reports the state of a vehicle device, such as motors, heaters,
and door locks. Changing the state of a vehicle device can update actuator data.
For example, you can define an actuator to represent the heater. The actuator
receives new data when you turn on or off the heater.

**Custom structure**

A custom structure (also known as a struct) represents a complex or
higher-order data structure. It facilitates logical binding or grouping of data
that originates from the same source. A struct is used when data is read or
written in an atomic operation, such as to represent a complex data type or
higher-order shape.

A signal of struct type is defined in the signal catalog using a reference to
a struct data type instead of a primitive data type. Structs can be used for all
types of signals including sensors, attributes, actuators, and vision system data types. If a
signal of struct type is sent or received, AWS IoT FleetWise expects all included items to
have valid values, so all items are mandatory. For example, if a struct contains
the items Vehicle.Camera.Image.height, Vehicle.Camera.Image.width, and
Vehicle.Camera.Image.data – it's expected that the sent signal contains
values for all of these items.

###### Note

Vision system data is in preview release and is subject to change.

**Custom property**

A custom property represents a member of the complex data structure. The data
type of the property can be either primitive or another struct.

When representing a higher-order shape using a struct and custom property, the
intended higher-order shape is always defined and visioned as a tree structure.
The custom property is used to define all the leaf nodes while the struct is
used to define all the non-leaf nodes.

**Signal catalog**

A signal catalog contains a collection of signals. Signals in a signal catalog
can be used to model vehicles that use different protocols and data formats. For
example, there are two cars made by different automakers: one uses the Control
Area Network (CAN bus) protocol; the other one uses the On-board Diagnostics
(OBD) protocol. You can define a sensor in the signal catalog to receive
in-vehicle temperature values. This sensor can be used to represent the
thermocouples in both cars. For more information, see [Manage AWS IoT FleetWise signal catalogs](signal-catalogs.md "signal-catalogs.md").

**Vehicle model (model manifest)**

Vehicle models are declarative structures that you can use to standardize the
format of your vehicles and to define relationships between signals in the
vehicles. Vehicle models enforce consistent information across multiple vehicles
of the same type. You add signals to create vehicle models. For more
information, see [Manage AWS IoT FleetWise vehicle models](vehicle-models.md "vehicle-models.md").

**Decoder manifest**

Decoder manifests contain decoding information for each signal in vehicle
models. Sensors and actuators in vehicles transmit low-level messages (binary
data). With decoder manifests, AWS IoT FleetWise is able to transform binary data into
human-readable values. Every decoder manifest is associated with a vehicle
model. For more information, see [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md "decoder-manifests.md").

**Network interface**

Contains information about the protocol that the in-vehicle network uses.
AWS IoT FleetWise supports the following protocols.

**Controller Area Network (CAN bus)**

A protocol that defines how data is communicated between
electronic control units (ECUs). ECUs can be the engine control
unit, airbags, or the audio system.

**On-board diagnostic (OBD) II**

A further developed protocol that defines how self-diagnostic data
is communicated between ECUs. It provides a number of standard
diagnostic trouble codes (DTCs) that help identify what is wrong
with your vehicle.

**Vehicle middleware**

The vehicle middleware defined as a type of network interface. Examples
of vehicle middleware include Robot Operating System (ROS 2) and Scalable
service-Oriented MiddlewarE over IP (SOME/IP).

###### Note

AWS IoT FleetWise supports ROS 2 middleware for vision system data.

**Custom interfaces**

You can also use your own interface to decode signals at the Edge. This
can save you time since you don't need to create decoding rules in the
cloud.

**Signal decoder**

Provides detailed decoding information for a specific signal. Every signal
specified in the vehicle model must be paired with a signal decoder. If the
decoder manifest contains CAN network interfaces, it must contain CAN decoder
signals. If the decoder manifest contains OBD network interfaces, it must
contain OBD signal decoders.

The decoder manifest must contain message signal decoders if it also contains
vehicle middleware interfaces. Or, if the decoder manifest contains custom decoding
interfaces, it must also contain custom decoding signals.

**Vehicle**

A virtual representation of your physical vehicle, such a car or a truck.
Vehicles are instances of vehicle models. Vehicles created from the same vehicle
model inherit the same group of signals. Each vehicle corresponds to an AWS IoT
thing.

**Fleet**

A fleet represents a group of vehicles. Before you can easily manage a fleet
of vehicles, you must associate individual vehicles to a fleet.

**Campaign**

Contains data collection schemes. You define a campaign in the cloud and
deploy it to a vehicle or fleet. Campaigns give the Edge Agent software instructions on
how to select, collect, and transfer data to the cloud.

**Data partition**

Configure partitioned data in a campaign to temporarily store signal
data. You configure when and how to forward the data to the cloud.

**Data collection scheme**

Data collection schemes give the Edge Agent software instructions on how to collect
data. Currently, AWS IoT FleetWise supports the condition-based collection scheme and
the time-based collection scheme.

**Condition-based collection scheme**

Use a logical expression to recognize what data to collect. The Edge Agent
software collects data when the condition is met. For example, if the expression
is `$variable.myVehicle.InVehicleTemperature >35.0`, the Edge Agent
software collects temperature values that are greater than 35.0.

**Time-based collection scheme**

Specify a time period in milliseconds to define how often to collect data. For
example, if the time period is 10,000 milliseconds, the Edge Agent software
collects data once every 10 seconds.

**Commands**

Commands execute commands on a vehicle from the cloud. You can remotely send
commands to a vehicle, and within a few seconds, the vehicle will execute the command.
For example, you can configure commands to lock a vehicle’s door or set the
temperature.

The command is a resource that's managed by AWS IoT Device Management. It contains reusable configurations
that are applied when sending a command execution to the vehicle. For more information, see
[AWS IoT
commands](../../../iot/latest/developerguide/iot-remote-command.md "../../../iot/latest/developerguide/iot-remote-command.md") in the _AWS IoT Core Developer Guide_.

**State templates**

State templates provide a mechanism for vehicle owners to track the state of their
vehicle. The Edge Agent software Agent that runs on the vehicle collects and sends signal updates
to the cloud. Each state template contains a list of signals from which data is collected.

## Features of AWS IoT FleetWise

The following are the key features of AWS IoT FleetWise.

**Vehicle modeling**

Build virtual representations of your vehicles and apply a common format
to organize vehicle signals. AWS IoT FleetWise supports [Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/introduction/overview/ "https://covesa.github.io/vehicle_signal_specification/introduction/overview/") that you can use to
standardize vehicle signals.

**Scheme-based data collection**

Define schemes to transfer only high-value vehicle data to the cloud. You
can define condition-based schemes to control what data to collect, such as
data in-vehicle temperature values that are greater than 40 degrees. You can
also define time-based schemes to control how often to collect data.

**Edge Agent for AWS IoT FleetWise software**

The Edge Agent software running in vehicles facilitates communication between
vehicles and the cloud. While vehicles are connected to the cloud, the
Edge Agent software continually receives data collection schemes and collects data
accordingly.
