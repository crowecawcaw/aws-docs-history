# CloudFormation resources

generated when AWS::Serverless::CapacityProvider is specified

When an `AWS::Serverless::CapacityProvider` is specified, AWS Serverless Application Model
(AWS SAM) generates an `AWS::Lambda::CapacityProvider` base CloudFormation
resource.

**`AWS::Lambda::CapacityProvider`**

_`LogicalId`:_ `<capacityprovider‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::CapacityProvider` is
specified, AWS SAM also generates CloudFormation resources for the following scenarios:

###### Scenarios

- [OperatorRole property
  is not specified](#sam-specification-generated-resources-capacityprovider-iam-role "#sam-specification-generated-resources-capacityprovider-iam-role")

## OperatorRole property

is not specified

When the `OperatorRole` property of an `AWS::Serverless::CapacityProvider` is
_not_ specified, AWS SAM generates an `AWS::IAM::Role`
CloudFormation resource with the `AWSLambdaManagedEC2ResourceOperator` managed policy attached.

**`AWS::IAM::Role`**

_`LogicalId`:_ ``<capacityprovider‑LogicalId>`OperatorRole`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this CloudFormation resource)
