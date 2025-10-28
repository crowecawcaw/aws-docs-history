# Configure AWS IoT FleetWise signals

This section shows you how to configure branches, attributes, sensors, and
actuators.

###### Topics

- [Configure branches](#configure-branch "#configure-branch")
- [Configure attributes](#configure-attributes "#configure-attributes")
- [Configure sensors or
  actuators](#configure-sensors-or-acuators "#configure-sensors-or-acuators")
- [Configure complex data
  types](#configure-complex-data-types "#configure-complex-data-types")

## Configure branches

To configure a branch, specify the following information.

- `fullyQualifiedName` – The fully qualified name of
  the branch is the path to the branch plus the branch's name. Use a
  dot(.) to refer to a child branch. For example,
  `Vehicle.Chassis.SteeringWheel` is the fully qualified
  name for the `SteeringWheel` branch.
  `Vehicle.Chassis.` is the path to this branch.

The fully qualified name can have up to 150 characters. Valid
characters: a–z, A–Z, 0–9, colon (:), and
underscore (\_).

- (Optional) `Description` – The description for the
  branch.

The description can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore), and -
(hyphen).

- (Optional) `deprecationMessage` – The deprecation
  message for the node or branch being moved or deleted.

The deprecationMessage can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `comment` – A comment in addition to the
  description. A comment can be used to provide additional information
  about the branch, such as the rationale for the branch or references to
  related branches.

The comment can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore), and -
(hyphen).

## Configure attributes

To configure an attribute, specify the following information.

- `dataType` – The attribute's data type must be one
  of the following: INT8, UINT8, INT16, UINT16, INT32, UINT32, INT64,
  UINT64, BOOLEAN, FLOAT, DOUBLE, STRING, UNIX_TIMESTAMP, INT8_ARRAY,
  UINT8_ARRAY, INT16_ARRAY, UINT16_ARRAY, INT32_ARRAY, UINT32_ARRAY,
  INT64_ARRAY, UINT64_ARRAY, BOOLEAN_ARRAY, FLOAT_ARRAY, DOUBLE_ARRAY,
  STRING_ARRAY, UNIX_TIMESTAMP_ARRAY, UNKNOWN, fullyQualifiedName, or a
  custom struct defined in the data type branch.
- `fullyQualifiedName` – The fully qualified name of
  the attribute is the path to the attribute plus the attribute's name.
  Use a dot(.) to refer to a child signal. For example,
  `Vehicle.Chassis.SteeringWheel.Diameter` is the fully
  qualified name for the `Diameter` attribute.
  `Vehicle.Chassis.SteeringWheel.` is the path to this
  attribute.

The fully qualified name can have up to 150 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), and \_
(underscore).

- (Optional) `Description` – The description for the
  attribute.

The description can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore), and -
(hyphen).

- (Optional) `unit` – The scientific unit for the
  attribute, such as km or Celsius.
- (Optional) `min` – The minimum value of the
  attribute.
- (Optional) `max` – The maximum value of the
  attribute.
- (Optional) `defaultValue` – The default value of the
  attribute.
- (Optional) `assignedValue` – The value assigned to
  the attribute.
- (Optional) `allowedValues` – A list of values that
  the attribute accepts.
- (Optional) `deprecationMessage` – The deprecation
  message for the node or branch that's being moved or deleted.

The deprecationMessage can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `comment` – A comment in addition to the
  description. A comment can be used to provide additional information
  about the attribute, such as the rationale for the attribute or
  references to related attributes.

The comment can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore), and -
(hyphen).

## Configure sensors or

actuators

To configure a sensor or actuator, specify the following information.

- `dataType` – The signal's data type must be one of
  the following: INT8, UINT8, INT16, UINT16, INT32, UINT32, INT64, UINT64,
  BOOLEAN, FLOAT, DOUBLE, STRING, UNIX_TIMESTAMP, INT8_ARRAY, UINT8_ARRAY,
  INT16_ARRAY, UINT16_ARRAY, INT32_ARRAY, UINT32_ARRAY, INT64_ARRAY,
  UINT64_ARRAY, BOOLEAN_ARRAY, FLOAT_ARRAY, DOUBLE_ARRAY, STRING_ARRAY,
  UNIX_TIMESTAMP_ARRAY, UNKNOWN, fullyQualifiedName, or a custom struct
  defined in the data type branch.
- `fullyQualifiedName` – The fully qualified name of
  the signal is the path to the signal plus the signal's name. Use a
  dot(.) to refer to a child signal. For example,
  `Vehicle.Chassis.SteeringWheel.HandsOff.HandsOffSteeringState`
  is the fully qualified name for the `HandsOffSteeringState`
  actuator. `Vehicle.Chassis.SteeringWheel.HandsOff.` is the
  path to this actuator.

The fully qualified name can have up to 150 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), and \_
(underscore).

- (Optional) `Description` – The description for the
  signal.

The description can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore), and -
(hyphen).

- (Optional) `unit` – The scientific unit for the
  signal, such as km or Celsius.
- (Optional) `min` – The minimum value of the
  signal.
- (Optional) `max` – The maximum value of the
  signal.
- (Optional) `assignedValue` – The value assigned to
  the signal.
- (Optional) `allowedValues` – list of values that the
  signal accepts.
- (Optional) `deprecationMessage` – The deprecation
  message for the node or branch that's being moved or deleted.

The deprecationMessage can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `comment` – A comment in addition to the
  description. A comment can be used to provide additional information
  about the sensor or actuator, such as their rationale or references to
  related sensors or actuators.

The comment can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore), and -
(hyphen).

## Configure complex data

types

Complex data types are used when modeling vision systems. In addition to branches, these data types are made up of structures (also known as a struct) and properties. A struct is a signal that is described by multiple values, like an image. A property represents a member of the struct, like a primitive data type (such as UINT8) or another struct (such as timestamp). For example, Vehicle.Cameras.Front represents a branch, Vehicle.Cameras.Front.Image represents a struct, and Vehicle.Cameras.Timestamp represents a property.

The following complex data type example demonstrates how signals and data types are exported to a single .json file.

###### Example complex data type

```
{
  "Vehicle": {
    "type": "branch"
    // Signal tree
  },
  "ComplexDataTypes": {
    "VehicleDataTypes": {
      // complex data type tree
      "children": {
        "branch": {
          "children": {
            "Struct": {
              "children": {
                "Property": {
                  "type": "property",
                  "datatype": "Data type",
                  "description": "Description",
                  //                  ...
                }
              },
              "description": "Description",
              "type": "struct"
            }
          }
          "description": "Description",
          "type": "branch"
        }
      }
    }
  }
}
```

###### Note

You can download a [demo script](https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-nodes.py "https://raw.githubusercontent.com/aws/aws-iot-fleetwise-edge/main/tools/cloud/ros2-to-nodes.py") to convert ROS 2 messages to VSS .json files that are compatible with the signal catalog. For more information, see the [_Vision System Data Developer Guide_](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/vision-system-data/vision-system-data-demo.ipynb").

Vision system data is in preview release and is subject to change.

To configure a custom structure (or struct), specify the following
information.

- `fullyQualifiedName` – The fully qualified
  name of the custom structure. For example, the fully qualified
  name of a custom structure might be
  `ComplexDataTypes.VehicleDataTypes.SVMCamera`.

The fully qualified name can have up to 150 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), and \_
(underscore).

- (Optional) `Description` – The description
  for the signal.

The description can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `deprecationMessage` – The
  deprecation message for the node or branch that's being moved or
  deleted.

The deprecationMessage can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `comment` – A comment in addition
  to the description. A comment can be used to provide additional
  information about the sensor or actuator, such as their
  rationale or references to related sensors or actuators.

The comment can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore),
and - (hyphen).

To configure a custom property, specify the following
information.

- `dataType` – The signal's data type must be
  one of the following: INT8, UINT8, INT16, UINT16, INT32, UINT32,
  INT64, UINT64, BOOLEAN, FLOAT, DOUBLE, STRING, UNIX_TIMESTAMP,
  INT8_ARRAY, UINT8_ARRAY, INT16_ARRAY, UINT16_ARRAY, INT32_ARRAY,
  UINT32_ARRAY, INT64_ARRAY, UINT64_ARRAY, BOOLEAN_ARRAY,
  FLOAT_ARRAY, DOUBLE_ARRAY, STRING_ARRAY, UNIX_TIMESTAMP_ARRAY,
  STRUCT, STRUCT_ARRAY, or UNKNOWN.
- `fullyQualifiedName` – The fully qualified
  name of the custom property. For example, the fully qualified
  name of a custom property might be
  `ComplexDataTypes.VehicleDataTypes.SVMCamera.FPS`.

The fully qualified name can have up to 150 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), and \_
(underscore)

- (Optional) `Description` – The description
  for the signal.

The description can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `deprecationMessage` – The
  deprecation message for the node or branch that's being moved or
  deleted.

The deprecationMessage can have up to 2048 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), \_
(underscore), and - (hyphen).

- (Optional) `comment` – A comment in addition
  to the description. A comment can be used to provide additional
  information about the sensor or actuator, such as their
  rationale or references to related sensors or actuators.

The comment can have up to 2048 characters. Valid characters:
a–z, A–Z, 0–9, : (colon), \_ (underscore),
and - (hyphen).

- (Optional) `dataEncoding` – Indicates
  whether the property is binary data. The custom property's data
  encoding must be one of the following: BINARY or TYPED.
- (Optional) `structFullyQualifiedName` – The
  fully qualified name of the structure (struct) node for the
  custom property if the data type of the custom property is
  Struct or StructArray.

The fully qualified name can have up to 150 characters. Valid
characters: a–z, A–Z, 0–9, : (colon), and \_
(underscore).
