# AWS.Store.SSMParameters

You can create SSM parameters through AWS TNB. The SSM parameters that you create are created in SSM and
prefixed by the AWS TNB network instance ID. This prevents parameter values from an
override when multiple instances are instantiated and upgraded using the same NSD
template.

## Syntax

```
tosca.nodes.AWS.Store.SSMParameters
  properties:
    parameters:
      name: String
      value: String
    tags: List
```

## Properties

###### Parameters

`name`

The name of the ssm property. Use the following format: `^[a-zA-Z0-9]+[a-zA-Z0-9\-\_]*[a-zA-Z0-9]+$`

Each parameter's name must be less than 256 characters.

Required: Yes

Type: String

`value`

The value of the ssm property. Use one of the following formats:

- For values without references: `^[a-zA-Z0-9]+[a-zA-Z0-9\-\_]*[a-zA-Z0-9]+$`
- For static references: `^\$\{[a-zA-Z0-9]+\.(properties|capabilities|requirements)(\.([a-zA-Z0-9\-_]+))+\}$`
- For dynamic references: `^\$\{[a-zA-Z0-9]+\.(name|id|arn)\}$`

Each parameter’s value must be less than 4 KB.

Required: Yes

Type: String

`tags`

The tags that you can attach to an SSM property.

Required: No

Type: List

## Example

```
SampleSSM
    type: tosca.nodes.AWS.Store.SSMParameters
    properties:
        parameters:
            - name: "`Name1`"
              value: "`Value1`"
            - name: "`EKS_VERSION`"
              value: "${SampleEKS.properties.version}"
            - name: "`VPC_ID`"
              value: "${SampleVPC.id}
            - name: "REGION"
              value: "${AWS::Region}
        tags:
            - "tagKey=tagValue"
```
