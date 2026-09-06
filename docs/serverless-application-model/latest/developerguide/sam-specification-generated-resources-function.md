

# CloudFormation resources generated when AWS::Serverless::Function is specified
<a name="sam-specification-generated-resources-function"></a>

When an `AWS::Serverless::Function` is specified, AWS Serverless Application Model (AWS SAM) always creates an `AWS::Lambda::Function` base CloudFormation resource.

**`AWS::Lambda::Function`**  
*`LogicalId`: *`{{<function‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::Function` is specified, AWS SAM also generates CloudFormation resources for the following scenarios.

**Topics**
+ [Core function properties](#sam-specification-generated-resources-function-core-properties)
+ [Event sources](#sam-specification-generated-resources-function-event-sources)
+ [Event configuration](#sam-specification-generated-resources-function-event-configuration)

## Core function properties
<a name="sam-specification-generated-resources-function-core-properties"></a>

The following scenarios generate CloudFormation resources based on core function properties:

### Role property is not specified
<a name="sam-specification-generated-resources-function-not-role"></a>

When the `Role` property of an `AWS::Serverless::Function` is *not* specified, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource.

**`AWS::IAM::Role`**  
*`LogicalId`: *`{{<function‑LogicalId>}}Role`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

### AutoPublishAlias property is specified
<a name="sam-specification-generated-resources-function-autopublishalias"></a>

When the `AutoPublishAlias` property of an `AWS::Serverless::Function` is specified, AWS SAM generates the following CloudFormation resources: `AWS::Lambda::Alias` and `AWS::Lambda::Version`.

**`AWS::Lambda::Alias`**  
*`LogicalId`: *`{{<function‑LogicalId>}}Alias{{<alias‑name>}}`  
`{{<alias‑name>}}` is the string that `AutoPublishAlias` is set to. For example, if you set `AutoPublishAlias` to `live`, the `LogicalId` is: {{MyFunction}}Alias{{live}}.  
*Referenceable property: *`{{<function‑LogicalId>}}.Alias`

**`AWS::Lambda::Version`**  
*`LogicalId`: *`{{<function‑LogicalId>}}Version{{<sha>}}`  
`{{<sha>}}` is a unique hash value that is generated when the stack is created. For example, {{MyFunction}}Version{{926eeb5ff1}}.  
*Referenceable property: *`{{<function‑LogicalId>}}.Version`

For additional information on the `AutoPublishAlias` property, see the [Properties section of AWS::Serverless::Function](sam-resource-function.md#sam-resource-function-properties).

### DeploymentPreference property is specified
<a name="sam-specification-generated-resources-function-deploymentpreference"></a>

When the `DeploymentPreference` property of an `AWS::Serverless::Function` is specified, AWS SAM generates the following resources CloudFormation resources: `AWS::CodeDeploy::Application` and `AWS::CodeDeploy::DeploymentGroup`. In addition, if the `Role` property of the `DeploymentPreference` object is *not* specified, AWS SAM also generates an `AWS::IAM::Role` CloudFormation resource.

**`AWS::CodeDeploy::Application`**  
*`LogicalId`: *`ServerlessDeploymentApplication`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::CodeDeploy::DeploymentGroup`**  
*`LogicalId`: *`{{<function‑LogicalId>}}DeploymentGroup`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::IAM::Role`**  
*`LogicalId`: *`CodeDeployServiceRole`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

### FunctionUrlConfig property is specified
<a name="sam-specification-generated-resources-function-functionurlconfig"></a>

When the `FunctionUrlConfig` property is specified, AWS SAM generates different CloudFormation resources based on the `AuthType`.

When `AuthType: NONE` is specified, AWS SAM generates the following CloudFormation resources:

**`AWS::Lambda::Permission` (Invoke Access)**  
*`LogicalId`: *`{{<function‑LogicalId>}}URLInvokeAllowPublicAccess`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::Lambda::Permission` (Public Access)**  
*`LogicalId`: *`{{<function‑LogicalId>}}UrlPublicPermissions`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::Lambda::Url`**  
*`LogicalId`: *`{{<function‑LogicalId>}}Url`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

When `AuthType: AWS_IAM` is specified, AWS SAM generates only:

**`AWS::Lambda::Url`**  
*`LogicalId`: *`{{<function‑LogicalId>}}Url`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

For additional information on the `FunctionUrlConfig` property, see [FunctionUrlConfig](sam-property-function-functionurlconfig.md).

## Event sources
<a name="sam-specification-generated-resources-function-event-sources"></a>

The following scenarios generate CloudFormation resources based on event sources:

### An Api event source is specified
<a name="sam-specification-generated-resources-function-api"></a>

When the `Event` property of an `AWS::Serverless::Function` is set to `Api`, but the `RestApiId` property is *not* specified, AWS SAM generates the `AWS::ApiGateway::RestApi` CloudFormation resource.

**`AWS::ApiGateway::RestApi`**  
*`LogicalId`: *`ServerlessRestApi`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

### An HttpApi event source is specified
<a name="sam-specification-generated-resources-function-httpapi"></a>

When the `Event` property of an `AWS::Serverless::Function` is set to `HttpApi`, but the `ApiId` property is *not* specified, AWS SAM generates the `AWS::ApiGatewayV2::Api` CloudFormation resource.

**`AWS::ApiGatewayV2::Api`**  
*`LogicalId`: *`ServerlessHttpApi`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

### A streaming event source is specified
<a name="sam-specification-generated-resources-function-streaming"></a>

When the `Event` property of an `AWS::Serverless::Function` is set to one of the streaming types, AWS SAM generates the `AWS::Lambda::EventSourceMapping` CloudFormation resource. This applies to the following types: `DynamoDB`, `Kinesis`, `MQ`, `MSK`, and `SQS`.

**`AWS::Lambda::EventSourceMapping`**  
*`LogicalId`: *`{{<function‑LogicalId><event‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

### An event bridge (or event bus) event source is specified
<a name="sam-specification-generated-resources-function-eventbridge"></a>

When the `Event` property of an `AWS::Serverless::Function` is set to one of the event bridge (or event bus) types, AWS SAM generates the `AWS::Events::Rule` CloudFormation resource. This applies to the following types: `EventBridgeRule`, `Schedule`, and `CloudWatchEvents`.

**`AWS::Events::Rule`**  
*`LogicalId`: *`{{<function‑LogicalId><event‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

### An IotRule event source is specified
<a name="sam-specification-generated-resources-function-iotrule"></a>

When the `Event` property of an `AWS::Serverless::Function` is set to IoTRule, AWS SAM generates the `AWS::IoT::TopicRule` CloudFormation resource.

**`AWS::IoT::TopicRule`**  
*`LogicalId`: *`{{<function‑LogicalId><event‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## Event configuration
<a name="sam-specification-generated-resources-function-event-configuration"></a>

The following scenarios generate CloudFormation resources based on event configuration:

### OnSuccess (or OnFailure) property is specified for Amazon SNS events
<a name="sam-specification-generated-resources-function-sns-onsuccess"></a>

When the `OnSuccess` (or `OnFailure`) property of the `DestinationConfig` property of the `EventInvokeConfig` property of an `AWS::Serverless::Function` is specified, and the destination type is `SNS` but the destination ARN is *not* specified, AWS SAM generates the following CloudFormation resources: `AWS::Lambda::EventInvokeConfig` and `AWS::SNS::Topic`.

**`AWS::Lambda::EventInvokeConfig`**  
*`LogicalId`: *`{{<function‑LogicalId>}}EventInvokeConfig`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::SNS::Topic`**  
*`LogicalId`: *`{{<function‑LogicalId>}}OnSuccessTopic` (or `{{<function‑LogicalId>}}OnFailureTopic`)  
*Referenceable property: *`{{<function‑LogicalId>}}.DestinationTopic`  
If both `OnSuccess` and `OnFailure` are specified for an Amazon SNS event, to distinguish between the generated resources, you must use the `LogicalId`.

### OnSuccess (or OnFailure) property is specified for Amazon SQS events
<a name="sam-specification-generated-resources-function-sqs-onsuccess"></a>

When the `OnSuccess` (or `OnFailure`) property of the `DestinationConfig` property of the `EventInvokeConfig` property of an `AWS::Serverless::Function` is specified, and the destination type is `SQS` but the destination ARN is *not* specified, AWS SAM generates the following CloudFormation resources: `AWS::Lambda::EventInvokeConfig` and `AWS::SQS::Queue`.

**`AWS::Lambda::EventInvokeConfig`**  
*`LogicalId`: *`{{<function‑LogicalId>}}EventInvokeConfig`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::SQS::Queue`**  
*`LogicalId`: *`{{<function‑LogicalId>}}OnSuccessQueue` (or `{{<function‑LogicalId>}}OnFailureQueue`)  
*Referenceable property: *`{{<function‑LogicalId>}}.DestinationQueue`  
If both `OnSuccess` and `OnFailure` are specified for an Amazon SQS event, to distinguish between the generated resources, you must use the `LogicalId`.