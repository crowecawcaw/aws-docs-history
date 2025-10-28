# Define resources by using other supported properties in AWS SAM

For both source and destination resources, when defined within the same template, use the `Id`
property. Optionally, a `Qualifier` can be added to narrow the scope of your defined resource. When
the resource is not within the same template, use a combination of supported properties.

- For a list of supported property combinations for source and destination resources, see
  [Supported source and destination resource
  types for connectors](reference-sam-connector.md#supported-connector-resource-types "reference-sam-connector.md#supported-connector-resource-types").
- For a description of properties that you can use with connectors, see [AWS::Serverless::Connector](sam-resource-connector.md "sam-resource-connector.md").
  When you define a source resource with a property other than `Id`, use the
  `SourceReference` property.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  `<source-resource-logical-id>`:
    Type: `<resource-type>`
    ...
    Connectors:
      `<connector-name>`:
        Properties:
          SourceReference:
            Qualifier: `<optional-qualifier>`
            `<other-supported-properties>`
          Destination:
            `<properties-that-identify-destination-resource>`
          Permissions:
            `<permission-types-to-provision>`
```

Here's an example, using a `Qualifier` to narrow the scope of an Amazon API Gateway resource:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyApi:
    Type: AWS::Serverless::Api
    Connectors:
      ApiToLambdaConn:
        Properties:
          SourceReference:
            Qualifier: Prod/GET/foobar
          Destination:
            Id: MyFunction
          Permissions:
            - Write
  ...
```

Here's an example, using a supported combination of `Arn` and `Type` to define a
destination resource from another template:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Connectors:
      TableConn:
        Properties:
          Destination:
            Type: AWS::DynamoDB::Table
            Arn: !GetAtt MyTable.Arn
  ...
```

For more information on using connectors, refer to [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md").
