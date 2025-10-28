# SourceReference

A reference to a source resource that the [AWS::Serverless::Connector](sam-resource-connector.md "sam-resource-connector.md") resource type uses.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
Qualifier: `String`
```

## Properties

`Qualifier`

A qualifier for a resource that narrows its scope. `Qualifier` replaces the `*`
value at the end of a resource constraint ARN.

###### Note

Qualifier definition varies per resource type. For a list of supported source and destination resource
types, see [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md").

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation
equivalent.

## Examples

**The following example uses embedded connectors to define a source resource with a property
other than `Id`:**

```
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyApi:
    Type: AWS::Serverless::Api
    Connectors:
      ApitoLambdaConn:
        Properties:
          SourceReference:
            Qualifier: Prod/GET/foobar
          Destination:
            Id: MyTable
          Permissions:
            - Read
            - Write
  MyTable:
    Type: AWS::DynamoDB::Table
    ...
```
