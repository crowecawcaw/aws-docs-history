# EndpointConfiguration

The endpoint type of a REST API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Type: `String`
  VPCEndpointIds: `List`

```

## Properties

`Type`

The endpoint type of a REST API.

_Valid values_: `EDGE` or `REGIONAL` or `PRIVATE`

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Types` property of the `AWS::ApiGateway::RestApi` `EndpointConfiguration` data type.

`VPCEndpointIds`

A list of VPC endpoint IDs of a REST API against which to create Route53 aliases.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `VpcEndpointIds` property of the `AWS::ApiGateway::RestApi` `EndpointConfiguration` data type.

## Examples

### EndpointConfiguration

Endpoint Configuration example

#### YAML

```
EndpointConfiguration:
  Type: PRIVATE
  VPCEndpointIds:
    - vpce-123a123a
    - vpce-321a321a

```
