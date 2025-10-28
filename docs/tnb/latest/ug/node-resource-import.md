# AWS.Resource.Import

You can import the following AWS resources into AWS TNB:

- VPC
- Subnet
- Route Table
- Internet Gateway
- Security Group

## Syntax

```
tosca.nodes.AWS.Resource.Import
  properties:
    resource_type: String
    resource_id: String
```

## Properties

`resource_type`

The resource type that is imported to AWS TNB.

Required: No

Type: List

`resource_id`

The resource ID that is imported to AWS TNB.

Required: No

Type: List

## Example

```
SampleImportedVPC:
  type: tosca.nodes.AWS.Resource.Import
  properties:
    resource_type: "tosca.nodes.AWS.Networking.VPC"
    resource_id: "`vpc-123456`"
```
