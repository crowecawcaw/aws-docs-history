# Schema for type definitions

The following sections detail the schema used for type definitions.

## $id

The $id element identifies the schema definition. It must follow this structure:

- Start with the `/schema-versions/` URI prefix
- Include the `definition` schema type
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

The $ref element references an existing type definition within the system. It follows the same constraints as the `$id` element.

###### Note

A type definition or capability must exist with the value provided in the `$ref` file.

###### Example $ref

```
/schema-version/definition/aws.capability@1.0
```

## name

The name element is a string representing the entity name in the schema document. It often contains abbreviations and must follow these rules:

- Contain only alphanumeric characters, periods (.), forward slashes (/), hyphens (-), and spaces
- Start with a letter
- Maximum of 192 characters

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

###### Example titles

```
Real-time Communication (RTC) Session Controller
Energy EVSE Capability
```

## description

The `description` element provides a detailed explanation of the entity represented by the schema document. It can contain any characters and is used in documentation.

###### Example description

```
Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or Plug-In Hybrid Electric Vehicle.
            This capability provides an interface to the functionality of Electric Vehicle Supply Equipment (EVSE) management.
```

## extrinsicId

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
