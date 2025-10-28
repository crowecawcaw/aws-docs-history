# Schema for capability definitions

A capability is documented using a declarative JSON document that provides a clear contract for how the capability should function within the system.

For a capability, the mandatory elements are `$id`, `name`, `extrinsicId`, `extrinsicVersion` and at least one
element in at least one of the following sections:

- `properties`
- `actions`
- `events`
  The optional elements in a capability are
  `$ref`, `title`, `description`, `version`, `$defs` and `extrinsicProperties`. For a capability, `$ref` must refer
  to `aws.capability`.

The following sections detail the schema used for capability definitions.

## $id (mandatory)

The $id element identifies the schema definition. It must follow this structure:

- Start with the `/schema-versions/` URI prefix
- Include the `capability` schema type
- Use a forward slash (`/`) as a URI path separator
- Include the schema identity, with fragments separated by periods (`.`)
- Use the `@` character to separate the schema ID and version
- End with the semver version, using periods (`.`) to separate version fragments

The schema identity must start with a root namespace that is 3-12 characters long, followed by an optional sub-namespace and name.

The semver version includes a MAJOR version (up to 3 digits), a MINOR version (up to 3 digits), and an optional PATCH version (up to 4 digits).

###### Note

You can't use the reserved namespaces `aws` or `matter`

###### Example $id

```
/schema-version/capability/aws.Recording@1.0
```

## $ref

The `$ref` element references an existing capability within the system. It follows the same constraints as the `$id` element.

###### Note

A type definition or capability must exist with the value provided in the `$ref` file.

###### Example $ref

```
/schema-version/definition/aws.capability@1.0
```

## name (mandatory)

The name element is a string representing the entity name in the schema document. It often contains abbreviations and must follow these rules:

- Contain only alphanumeric characters, periods (.), forward slashes (/), hyphens (-), and spaces
- Start with a letter
- Maximum of 64 characters

The name element is used in the Amazon Web Services console UI and documentation.

###### Example names

```
Door Lock
On/Off
Wi-Fi Network Management
PM2.5 Concentration Measurement
RTCSessionController
Energy EVSE
```

## title

The title element is a descriptive string for the entity represented by the schema document. It can contain any characters and is used in documentation.
The maximum length for a capability title is 256 characters.

###### Example titles

```
Real-time Communication (RTC) Session Controller
Energy EVSE Capability
```

## description

The `description` element provides a detailed explanation of the entity represented by the schema document. It can contain any characters and is used in documentation.
The maximum length for a capability description is 2048 characters

###### Example description

```
Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or Plug-In Hybrid Electric Vehicle.
            This capability provides an interface to the functionality of Electric Vehicle Supply Equipment (EVSE) management.
```

## version

The `version` element is optional. It is a string that represents the version of the schema document. It has the following
constraints:

- Uses semver format, with following version fragments separated by `.` (periods).
  - `MAJOR` version, maximum of 3 digits
  - `MINOR` version, maximum of 3 digits
  - `PATCH` version (optional), maximum of 4 digits

- The length can be between 3 and 12 characters.

###### Example versions

```
1.0
```

```
1.12
```

```
1.4.1
```

### Working with capability versions

A capability is an immutable versioned entity. Any change is expected to create a new version. The system uses semantic versioning with MAJOR.MINOR.PATCH format, where:

- MAJOR version increases when making backward incompatible API changes
- MINOR version increases when adding functionality in a backward-compatible manner
- PATCH version increases when making minor non-impacting additions in the capability.

The capabilities derived from Matter clusters are baselined from version 1.4 and each Matter release is expected to be imported into the system.
As the Matter version consumes both MAJOR and MINOR levels of semver, managed integrations can only use PATCH versions.

When you add PATCH versions for Matter, be sure to take into account that that Matter uses sequential revisions. All PATCH versions
must comply with the revision documented in the Matter specification and these must be backward compatible.

To get any backward-incompatibly issues fixed, you must work with Connectivity Standards Alliance (CSA) to solve those in the specification and get a new revision released.

AWS-managed capabilities were released with an initial version of `1.0`. With these, all three levels of version can be used.

## extrinsicVersion (mandatory)

This is a string representing a version managed outside of the AWS IoT system. For Matter capabilities, `extrinsicVersion` maps to `revision`

It is represented as a stringified integer value, and the length can be from 1 to 10 numerical digits.

###### Example versions

```
7
```

```
1567
```

## extrinsicId (mandatory)

The `extrinsicId` element represents an identifier managed outside of the Amazon Web Services IoT system. For Matter capabilities, it maps to `clusterId`, `attributeId`,
`commandId`, `eventId`, or `fieldId`, depending on the context.

The `extrinsicId` can be either a stringified decimal integer (1-10 digits) or a stringified hexadecimal integer (0x or 0X prefix, followed by 1-8 hexadecimal digits).

###### Note

For AWS, the Vendor ID (VID) is 0x1577, and for Matter, it is 0. The system ensures that custom schemas don't use these reserved VIDs for capabilities.

###### Example extrinsicIds

```
0018
0x001A
0x15771002
```

## $defs

The `$defs` section is a map of sub-schemas that can be referenced within the schema document as allowed by the JSON schema. In this map, the key is used in the
local reference definitions and the value provides the JSON schema.

###### Note

The system only enforces that `$defs` is a valid map and that each sub-schema is a valid JSON schema. No additional rules are enforced.

Follow these constraints when working with definitions:

- Use only URI-friendly characters in definition names
- Ensure each value is a valid sub-schema
- Include any number of sub-schemas that fit within the schema document size limits

## extrinsicProperties

The `extrinsicProperties` element contains a set of properties defined in an external system but maintained within the data model. For
Matter capabilities, it maps to different unmodeled or partially modeled elements within ZCL cluster, attribute, command, or event.

Extrinsic Properties must follow these constraints:

- Property names must be alphanumeric without spaces or special characters
- Property values can be any JSON schema values
- Maximum of 20 properties

The system supports various `extrinsicProperties`, including `access`, `apiMaturity`, `cli`, `cliFunctionName`, and others.
These properties facilitate ACL to AWS (and vice versa) data model transformations.

###### Note

Extrinsic properties are supported for the `action`, `event`, `property`, and `struct` fields elements of a capability, but not for the
capability or cluster itself.

## Properties

Properties represent device-managed states of the capability. Each state is defined as a key-value pair, where the key describes the name of the state
and the value describes the definition of the state.

When working with properties, follow these constraints:

- Use only alphanumeric characters in property names, without spaces or special characters
- Include any number of properties that fit within the schema document size limits

### Working with properties

A property within a capability is a fundamental element that represents a specific state of a device powered by managed integrations. It represents the device's current condition or configuration.
By standardizing how these properties are defined and structured, smart home systems ensure that devices from different manufacturers can communicate effectively,
creating a seamless and interoperable experience.

For a capability property, the mandatory elements are `extrinsicId` and `value`. The optional elements in a capability property are `description`,
`retrievable`, `mutable`, `reportable` and `extrinsicProperties`.

#### Value

An unbounded structure that allows builders to put any JSON-schema compliant constraints to define the data type of this property.

When defining values, follow these constraints:

- For simple types, use `type` and any other native JSON-schema constraints such as `maxLength` or `maximum`
- For composite types, use `oneOf`, `allOf`, or `anyOf`. The system doesn't support the `not` keyword
- To refer to any global type, use `$ref` with a valid discoverable reference
- For nullability, follow OpenAPI type schema definition by providing the nullable attribute with a boolean flag (`true` if null is an allowed value)

Example:

```
{
    "$ref": "/schema-versions/definition/matter.uint16@1.4",
    "nullable": true,
    "maximum": 4096
}
```

#### Retrievable

A boolean describing if the state is readable or not.

The readability aspect of the state is deferred to the device's implementation of the capability. The device
decides if a given state is readable or not. This aspect of the state is not yet supported to be reported in the capability report and hence not enforced within the system.

Example: `true` or `false`

#### Mutable

A boolean describing if the state is writable or not.

The writability aspect of the state is deferred to the device's implementation of the capability. The device decides if a given state is
writable or not. This aspect of the state is not yet supported to be reported in the capability report and hence not enforced within the system.

Example: `true` or `false`

#### Reportable

A boolean describing if the state is reported by the device when there is a change in the state.

The reportability aspect of the state is deferred to the device's implementation of the capability.
The device decides if a given state is reportable or not. This aspect of the state is not yet supported to
be reported in the capability report and hence not enforced within the system.

Example: `true` or `false`

## Actions

Actions are schema-managed operations that follow a request-response model. Each action represents a device-implemented operation.

Follow these constraints when implementing actions:

- Include only unique actions in the actions array
- Include any number of actions that fit within the schema document size limits

### Working with actions

An action is a standardized way to interact with and control device capabilities in a managed integration system.
It represents a specific command or operation that can be executed on a device, complete with a structured format to model any necessary
request or response parameters. These actions serve as the bridge between user intentions and device operations, enabling consistent
and reliable control across different types of smart devices.

For an action, the mandatory elements are `name` and `extrinsicId`. The optional elements are `description`, `extrinsicProperties`,
`request` and `response`.

### Description

The description has a maximum length constraint of 1536 characters.

### Request

The request section is optional and can be omitted if there are no request parameters. If omitted,
the system supports sending a request without any payload by just using the name of `Action`. This is used in simple actions, like turning a light on or off.

The complex actions need additional parameters. For instance, a request to stream camera footage might include
parameters about the streaming protocol to use or whether to send the stream to a specific display device.

For an action request, the mandatory element is `parameters`. The optional elements are `description`, `extrinsicId`, and `extrinsicProperties`.

#### Request description

The description follows the same format as section 3.5, with a maximum length of 2048 characters.

### Response

In managed integrations, for any action request sent through the [SendManagedThingCommand](../APIReference/API_SendManagedThingCommand.md "../APIReference/API_SendManagedThingCommand.md") API,
the request reaches the device and expects an asynchronous response back. The action response defines the structure of this response.

For an action request, the mandatory element is `parameters`. The optional elements are `name`, `description`, `extrinsicId`,
`extrinsicProperties`, `errors` and `responseCode`.

#### Response description

The description follows the same format as [description](#capability-schema-description "#capability-schema-description"), and has a maximum length of 2048 characters.

#### Response name

The name follows the same format as [name (mandatory)](#capability-schema-name "#capability-schema-name"), with these additional details:

- The conventional name of a response is derived by appending `Response` to the action name.
- If you want to use a different name, you can provide it in this `name` element. If a `name` is provided in the response,
  then this value takes higher precedence than the conventional name.

#### Errors

An unbounded array of unique messages provided in the response, if there are errors while processing the request.

Constraints:

- A message item is declared as a JSON object with the following fields:
  - `code`: A string containing alphanumeric characters and `_` (underscores), with a length between 1 to 64 characters
  - `message`: An unbounded string value

###### Example Error message example

```
"errors": [
   {
      "code": "AD_001",
      "message": "Unable to receive signal from the sensor. Please check connection with the sensor."
   }
]
```

#### Response code

An integer code displaying how the request was handled. We recommend that the device code returns a code using the
HTTP server response status code specification to allow uniformity within the system.

Constraint: An integer value ranging from 100 to 599.

### Request or response parameters

The parameters section is defined as a map of name and sub-schema pairs. Any number of parameters can be defined within the request parameters, if they can fit in the schema document.

Parameter names can only contain alphanumeric characters. Spaces or any other characters are not allowed.

#### parameter field

The mandatory elements in a `parameter` are `extrinsicId` and `value`. The optional elements are `description` and `extrinsicProperties`.

The description element follows the same format as [description](#capability-schema-description "#capability-schema-description"), with a maximum length of 1024 characters.

### `extrinsicId` and `extrinsicProperties` overrides

the `extrinsicId` and `extrinsicProperties` follow the same format as [extrinsicId (mandatory)](#capability-schema-extrinsicId "#capability-schema-extrinsicId") and [extrinsicProperties](#capability-schema-extrinsicProperties "#capability-schema-extrinsicProperties"), with these additional details:

- If an `extrinsicId` is provided in the request or response, this value takes higher precedence
  than the value provided at the action level. The system must use request/response level `extrinsicId` first, if missing use the action level `extrinsicId`
- If `extrinsicProperties` are provided in the request or response, these properties take higher precedence than the va value provided at the action level.
  The system must take the action level `extrinsicProperties` and replace the key-value pairs provided at the request/response level `extrinsicProperties`

###### Example extrinsicId and extrinsicProperties override example

```
{
   "name": "ToggleWithEffect",
   "extrinsicId": "0x0001",

   "extrinsicProperties": {
      "apiMaturity": "provisional",
      "introducedIn": "1.2"
   },
   "request": {
      "extrinsicProperties": {
         "apiMaturity": "stable",
         "manufacturerCode": "XYZ"
      },
      "parameters": {
         ...
      }
   },
   "response": {
      "extrinsicProperties": {
         "noDefaultImplementation": true
      },
      "parameters": {
 {
         ...
      }
   }
}
```

In the above example, the effective values for the action request would be:

```
# effective request
"name": "ToggleWithEffect",
"extrinsicId": "0x0001",
"extrinsicProperties": {
   "apiMaturity": "stable",
   "introducedIn": "1.2"
   "manufacturerCode": "XYZ"
},
"parameters": {
   ...
}

# effective response
"name": "ToggleWithEffectResponse",
"extrinsicId": "0x0001",
"extrinsicProperties": {
   "apiMaturity": "provisional",
   "introducedIn": "1.2"
   "noDefaultImplementation": true
},
"parameters": {
   ...
}
```

### Built-in actions

For all capabilities, you can perform custom actions using the keywords `ReadState` and `UpdateState`. These two action keywords
will act on the capability's properties defined in the data model.

ReadState

Sends a command to the `managedThing` to read the values of its state properties. Use `ReadState` as a way to force the device state to be updated.

UpdateState

Sends a command to update some of the properties.

Forcing a device state synchronization may be useful in the following scenarios:

1. The device was offline for a period of time and was not emitting events.
2. The device was just provisioned and does not yet have any state maintained in the cloud.
3. The device state is out of sync with the real state of the device.

#### ReadState examples

Check if the light is on or off using the [SendManagedThingCommand](../APIReference/API_SendManagedThingCommand.md "../APIReference/API_SendManagedThingCommand.md") API:

```
{
  "Endpoints": [
    {
      "endpointId": "1",
      "capabilities": [
        {
          "id": "aws.OnOff",
          "name": "On/Off",
          "version": "1",
          "actions": [
            {
              "name": "ReadState",
              "parameters": {
                "propertiesToRead": [ "OnOff" ]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

Read all state properties for the `matter.OnOff` capability:

```
{
  "Endpoints": [
    {
      "endpointId": "1",
      "capabilities": [
        {
          "id": "aws.OnOff",
          "name": "On/Off",
          "version": "1",
          "actions": [
            {
              "name": "ReadState",
              "parameters": {
                "propertiesToRead": [ "*" ]
                // Use the wildcard operator to read ALL state properties for a capability
              }
            }
          ]
        }
      ]
    }
  ]
}
```

#### UpdateState example

Change the `OnTime` for a light using the [SendManagedThingCommand](../APIReference/API_SendManagedThingCommand.md "../APIReference/API_SendManagedThingCommand.md") API:

```
{
  "Endpoints": [
    {
      "endpointId": "1",
      "capabilities": [
        {
          "id": "matter.OnOff",
          "name": "On/Off",
          "version": "1",
          "actions": [
            {
              "name": "UpdateState",
              "parameters": {
                "OnTime": 5
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## Events

Events are schema-managed, unidirectional signals implemented by the device.

Implement events according to these constraints:

- Include only unique events in the events array
- Include any number of events that fit within the schema document size limits
