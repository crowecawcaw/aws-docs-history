# Define resource attributes with connectors in AWS SAM

Resource attributes can be defined for resources to specify additional behaviors and relationships. To learn
more about resource attributes, see [Resource attribute reference](../../../AWSCloudFormation/latest/UserGuide/aws-product-attribute-reference.md "../../../AWSCloudFormation/latest/UserGuide/aws-product-attribute-reference.md")
in the _AWS CloudFormation User Guide_.

You can add resource attributes to your embedded connector by defining them on the same level as your
connector properties. When your AWS SAM template is transformed at deployment, attributes will pass through to the
generated resources.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Connectors:
      MyConn:
        DeletionPolicy: Retain
        DependsOn: AnotherFunction
        Properties:
          ...
```

For more information on using connectors, refer to [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md").
