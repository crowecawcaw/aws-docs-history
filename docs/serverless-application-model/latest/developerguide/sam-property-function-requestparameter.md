# RequestParameter

Configure Request Parameter for a specific Api+Path+Method.

Either `Required` or `Caching` property needs to be specified for request parameter

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Caching: `Boolean`
  Required: `Boolean`

```

## Properties

`Caching`

Adds `cacheKeyParameters` section to the API Gateway OpenApi definition

_Type_: Boolean

_Required_: Conditional

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Required`

This field specifies whether a parameter is required

_Type_: Boolean

_Required_: Conditional

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### Request Parameter

Example of setting Request Parameters

#### YAML

```
RequestParameters:
  - method.request.header.Authorization:
      Required: true
      Caching: true

```
