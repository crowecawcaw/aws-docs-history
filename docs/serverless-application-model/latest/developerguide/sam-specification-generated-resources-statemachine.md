# AWS CloudFormation resources

generated when AWS::Serverless::StateMachine is specified

When an `AWS::Serverless::StateMachine` is specified, AWS Serverless Application Model
(AWS SAM) generates an `AWS::StepFunctions::StateMachine` base AWS CloudFormation
resource.

**`AWS::StepFunctions::StateMachine`**

_`LogicalId`:_ `<statemachine‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

In addition to this AWS CloudFormation resource, when `AWS::Serverless::StateMachine` is
specified, AWS SAM also generates AWS CloudFormation resources for the following scenarios:

###### Scenarios

- [Role property
  is not specified](#sam-specification-generated-resources-statemachine-not-role "#sam-specification-generated-resources-statemachine-not-role")
- [An API event
  source is specified](#sam-specification-generated-resources-statemachine-api "#sam-specification-generated-resources-statemachine-api")
- [An
  event bridge (or event bus) event source is specified](#sam-specification-generated-resources-statemachine-eventbridge "#sam-specification-generated-resources-statemachine-eventbridge")

## Role property

is not specified

When the `Role` property of an `AWS::Serverless::StateMachine` is
_not_ specified, AWS SAM generates an `AWS::IAM::Role`
AWS CloudFormation resource.

**`AWS::IAM::Role`**

_`LogicalId`:_ ``<statemachine‑LogicalId>`Role`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

## An API event

source is specified

When the `Event` property of an `AWS::Serverless::StateMachine`
is set to `Api`, but the `RestApiId` property is
_not_ specified, AWS SAM generates the
`AWS::ApiGateway::RestApi` AWS CloudFormation resource.

**`AWS::ApiGateway::RestApi`**

_`LogicalId`:_ `ServerlessRestApi`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

## An

event bridge (or event bus) event source is specified

When the `Event` property of an `AWS::Serverless::StateMachine`
is set to one of the event bridge (or event bus) types, AWS SAM generates the
`AWS::Events::Rule` AWS CloudFormation resource. This applies to the following types:
`EventBridgeRule`, `Schedule`, and
`CloudWatchEvents`.

**`AWS::Events::Rule`**

_`LogicalId`:_ `<statemachine‑LogicalId><event‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)
