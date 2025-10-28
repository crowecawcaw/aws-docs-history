# ApiKeys

Create a unique key that can be used to perform GraphQL operations requiring
an API key.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
`LogicalId`:
  ApiKeyId: `String`
  Description: `String`
  ExpiresOn: `Double`
```

## Properties

`ApiKeyId`

The unique name of your API key. Specify to override the `LogicalId` value.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`ApiKeyId` property of an `AWS::AppSync::ApiKey`
resource.

`Description`

Description of your API key.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::AppSync::ApiKey`
resource.

`ExpiresOn`

The time after which the API key expires. The date is represented as seconds since
the epoch, rounded down to the nearest hour.

_Type_: Double

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Expires` property of an `AWS::AppSync::ApiKey`
resource.

`LogicalId`

The unique name of your API key.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`ApiKeyId` property of an `AWS::AppSync::ApiKey`
resource.
