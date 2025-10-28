# AWS.NS

Defines an AWS network service (NS) node.

## Syntax

```
tosca.nodes.AWS.NS:
  properties:
    descriptor_id: String
    descriptor_version: String
    descriptor_name: String
```

## Properties

`descriptor_id`

The UUID of the descriptor.

Required: Yes

Type: String

Pattern:
`[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

`descriptor_version`

The version of the NSD.

Required: Yes

Type: String

Pattern: `^[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}.*`

`descriptor_name`

The name of the descriptor.

Required: Yes

Type: String

## Example

```
SampleNS:
  type: tosca.nodes.AWS.NS
  properties:
    descriptor_id: "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
    descriptor_version: "1.0.0"
    descriptor_name: "Test NS Template"
```
