# Data model schemas

Managed integrations supports two schema types: _capability_ and _type definition_. If you are creating a custom data model, you use a JSON schema
document to define either type of schema.
Each schema document has a limit of 50,000 characters.

## Capability schema

A _capability_ is a fundamental building block that represents specific functionalities within an endpoint. With capabilities, you can
model device states and behaviors using properties, actions, and events. _Properties_ enable you to model the device's state attributes flexibly with any declarative data type.
_Actions_ and _events_ model the behavior of the device, including commands that it can execute and signals that it can report.

The following displays a high-level structure of a capability schema.

```
Capability
  |
  |-- Action
  |-- Event
  |-- Property
```

Action

An entity representing an interaction with a capability of a device. For example, ring the bell or view who is at the door.

Event

An entity representing an event from a capability of device. A device can send an event to report an incident, alarm, or an activity from a sensor such as a knock
at the door.

Property

An entity representing a particular attribute in the state of the device. For example, a bell is ringing or the porch light is on

Each capability includes a unique namespaced identifier, version information, and a description of its purpose.
The schema document uses semantic versioning to maintain backward compatibility while enabling new features.

For more information, see [Schema for capability definitions](schema-for-capability-definitions.md "schema-for-capability-definitions.md").

## Type definition schema

A type definition is a declarative structured data type that enables reusability and composability. It
defines how information should be formatted and constrained. Use type definitions to create standardized data formats across your IoT solution.

Each type definition includes:

- A unique namespaced identifier
- Title
- Description
- Properties that define data formatting and constraints

Types can be either simple primitives, such as integers or strings with defined limits, or complex structures such as enumerations or custom objects with multiple fields.
Type definitions use JSON schema syntax to specify constraints including minimum and maximum values, string lengths, and allowable patterns.

For more information, see [Schema for type definitions](schema-for-type-definitions.md "schema-for-type-definitions.md").
