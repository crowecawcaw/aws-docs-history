# AWS CloudFormation resources generated

when AWS::Serverless::Function is specified

When an `AWS::Serverless::Function` is specified, AWS Serverless Application Model
(AWS SAM) always creates an `AWS::Lambda::Function` base AWS CloudFormation resource.

**`AWS::Lambda::Function`**

_`LogicalId`:_ `<function‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

In addition to this AWS CloudFormation resource, when `AWS::Serverless::Function` is
specified, AWS SAM also generates AWS CloudFormation resources for the following scenarios.

###### Scenarios

- [Core function properties](#sam-specification-generated-resources-function-core-properties "#sam-specification-generated-resources-function-core-properties")
- [Event sources](#sam-specification-generated-resources-function-event-sources "#sam-specification-generated-resources-function-event-sources")
- [Event configuration](#sam-specification-generated-resources-function-event-configuration "#sam-specification-generated-resources-function-event-configuration")

## Core function properties

The following scenarios generate AWS CloudFormation resources based on core function properties:

### Role property

is not specified

When the `Role` property of an `AWS::Serverless::Function` is
_not_ specified, AWS SAM generates an `AWS::IAM::Role`
AWS CloudFormation resource.

**`AWS::IAM::Role`**

_`LogicalId`:_ ``<function‑LogicalId>`Role`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

### AutoPublishAlias property is specified

When the `AutoPublishAlias` property of an
`AWS::Serverless::Function` is specified, AWS SAM generates the following
AWS CloudFormation resources: `AWS::Lambda::Alias` and
`AWS::Lambda::Version`.

**`AWS::Lambda::Alias`**

_`LogicalId`:_ ``<function‑LogicalId>`Alias`<alias‑name>``

`<alias‑name>` is the
string that `AutoPublishAlias` is set to. For example, if you set
`AutoPublishAlias` to `live`, the
`LogicalId` is:
`MyFunction`Alias`live`.

_Referenceable property:_ ``<function‑LogicalId>`.Alias`

**`AWS::Lambda::Version`**

_`LogicalId`:_ ``<function‑LogicalId>`Version`<sha>``

`<sha>` is a unique hash value
that is generated when the stack is created. For example,
`MyFunction`Version`926eeb5ff1`.

_Referenceable property:_ ``<function‑LogicalId>`.Version`

For additional information on the `AutoPublishAlias` property, see the [Properties section of AWS::Serverless::Function](sam-resource-function.md#sam-resource-function-properties "sam-resource-function.md#sam-resource-function-properties").

### DeploymentPreference property is specified

When the `DeploymentPreference` property of an
`AWS::Serverless::Function` is specified, AWS SAM generates the following
resources AWS CloudFormation resources: `AWS::CodeDeploy::Application` and
`AWS::CodeDeploy::DeploymentGroup`. In addition, if the `Role`
property of the `DeploymentPreference` object is _not_
specified, AWS SAM also generates an `AWS::IAM::Role` AWS CloudFormation resource.

**`AWS::CodeDeploy::Application`**

_`LogicalId`:_ `ServerlessDeploymentApplication`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

**`AWS::CodeDeploy::DeploymentGroup`**

_`LogicalId`:_ ``<function‑LogicalId>`DeploymentGroup`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

**`AWS::IAM::Role`**

_`LogicalId`:_ `CodeDeployServiceRole`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

### FunctionUrlConfig property is specified

When the `FunctionUrlConfig` property is specified, AWS SAM generates different AWS CloudFormation resources based on the `AuthType`.

When `AuthType: NONE` is specified, AWS SAM generates the following AWS CloudFormation resources:

**`AWS::Lambda::Permission` (Invoke Access)**

_`LogicalId`:_ ``<function‑LogicalId>`URLInvokeAllowPublicAccess`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

**`AWS::Lambda::Permission` (Public Access)**

_`LogicalId`:_ ``<function‑LogicalId>`UrlPublicPermissions`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

**`AWS::Lambda::Url`**

_`LogicalId`:_ ``<function‑LogicalId>`Url`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

When `AuthType: AWS_IAM` is specified, AWS SAM generates only:

**`AWS::Lambda::Url`**

_`LogicalId`:_ ``<function‑LogicalId>`Url`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

For additional information on the `FunctionUrlConfig` property, see [FunctionUrlConfig](sam-property-function-functionurlconfig.md "sam-property-function-functionurlconfig.md").

## Event sources

The following scenarios generate AWS CloudFormation resources based on event sources:

### An Api

event source is specified

When the `Event` property of an `AWS::Serverless::Function` is
set to `Api`, but the `RestApiId` property is
_not_ specified, AWS SAM generates the
`AWS::ApiGateway::RestApi` AWS CloudFormation resource.

**`AWS::ApiGateway::RestApi`**

_`LogicalId`:_ `ServerlessRestApi`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

### An HttpApi

event source is specified

When the `Event` property of an `AWS::Serverless::Function` is
set to `HttpApi`, but the `ApiId` property is
_not_ specified, AWS SAM generates the
`AWS::ApiGatewayV2::Api` AWS CloudFormation resource.

**`AWS::ApiGatewayV2::Api`**

_`LogicalId`:_ `ServerlessHttpApi`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

### A streaming

event source is specified

When the `Event` property of an `AWS::Serverless::Function` is
set to one of the streaming types, AWS SAM generates the
`AWS::Lambda::EventSourceMapping` AWS CloudFormation resource. This applies to the
following types: `DynamoDB`, `Kinesis`, `MQ`,
`MSK`, and `SQS`.

**`AWS::Lambda::EventSourceMapping`**

_`LogicalId`:_ `<function‑LogicalId><event‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

### An event bridge

(or event bus) event source is specified

When the `Event` property of an `AWS::Serverless::Function` is
set to one of the event bridge (or event bus) types, AWS SAM generates the
`AWS::Events::Rule` AWS CloudFormation resource. This applies to the
following types: `EventBridgeRule`, `Schedule`, and
`CloudWatchEvents`.

**`AWS::Events::Rule`**

_`LogicalId`:_ `<function‑LogicalId><event‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

### An IotRule

event source is specified

When the `Event` property of an `AWS::Serverless::Function` is
set to IoTRule, AWS SAM generates the
`AWS::IoT::TopicRule` AWS CloudFormation resource.

**`AWS::IoT::TopicRule`**

_`LogicalId`:_ `<function‑LogicalId><event‑LogicalId>`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

## Event configuration

The following scenarios generate AWS CloudFormation resources based on event configuration:

### OnSuccess

(or OnFailure) property is specified for Amazon SNS events

When the `OnSuccess` (or `OnFailure`) property of the
`DestinationConfig` property of the `EventInvokeConfig`
property of an `AWS::Serverless::Function` is specified, and the destination
type is `SNS` but the destination ARN is _not_ specified,
AWS SAM generates the following AWS CloudFormation resources:
`AWS::Lambda::EventInvokeConfig` and `AWS::SNS::Topic`.

**`AWS::Lambda::EventInvokeConfig`**

_`LogicalId`:_ ``<function‑LogicalId>`EventInvokeConfig`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

**`AWS::SNS::Topic`**

_`LogicalId`:_ ``<function‑LogicalId>`OnSuccessTopic`
 (or
 ``<function‑LogicalId>`OnFailureTopic`)

_Referenceable property:_ ``<function‑LogicalId>`.DestinationTopic`

If both `OnSuccess` and `OnFailure` are specified
for an Amazon SNS event, to distinguish between the generated resources, you must
use the `LogicalId`.

### OnSuccess

(or OnFailure) property is specified for Amazon SQS events

When the `OnSuccess` (or `OnFailure`) property of the
`DestinationConfig` property of the `EventInvokeConfig`
property of an `AWS::Serverless::Function` is specified, and the destination
type is `SQS` but the destination ARN is _not_ specified,
AWS SAM generates the following AWS CloudFormation resources:
`AWS::Lambda::EventInvokeConfig` and `AWS::SQS::Queue`.

**`AWS::Lambda::EventInvokeConfig`**

_`LogicalId`:_ ``<function‑LogicalId>`EventInvokeConfig`

_Referenceable property:_ N/A (you must use the
`LogicalId` to reference this AWS CloudFormation resource)

**`AWS::SQS::Queue`**

_`LogicalId`:_ ``<function‑LogicalId>`OnSuccessQueue`
 (or
 ``<function‑LogicalId>`OnFailureQueue`)

_Referenceable property:_ ``<function‑LogicalId>`.DestinationQueue`

If both `OnSuccess` and `OnFailure` are specified
for an Amazon SQS event, to distinguish between the generated resources, you must
use the `LogicalId`.
