

# Generated CloudFormation resources for AWS SAM
<a name="sam-specification-generated-resources"></a>

This section provides details on the CloudFormation resources that are created when AWS SAM processes your AWS template. The set of CloudFormation resources that AWS SAM generates differs depending on the scenarios you specify. A *scenario* is the combination of AWS SAM resources and properties specified in your template file. You can reference the generated CloudFormation resources elsewhere within your template file, similar to how you reference resources that you declare explicitly in your template file.

For example, if you specify an `AWS::Serverless::Function` resource in your AWS SAM template file, AWS SAM always generates an `AWS::Lambda::Function` base resource. If you also specify the optional `AutoPublishAlias` property, AWS SAM additionally generates `AWS::Lambda::Alias` and `AWS::Lambda::Version` resources.

This section lists the scenarios and the CloudFormation resources that they generate, and shows how to reference the generated CloudFormation resources in your AWS SAM template file.

## Referencing generated CloudFormation resources
<a name="sam-specification-generated-resources-referencing"></a>

You have two options for referencing generated CloudFormation resources within your AWS SAM template file, by `LogicalId` or by referenceable property.

### Referencing generated CloudFormation resources by LogicalId
<a name="sam-specification-generated-resources-referencing-logicalid"></a>

The CloudFormation resources that AWS SAM generates each have a `[LogicalId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-logicalid)`, which is an alphanumeric (A-Z, a-z, 0-9) identifier that is unique within a template file. AWS SAM uses the `LogicalIds` of the AWS SAM resources in your template file to construct the `LogicalIds` of the CloudFormation resources it generates. You can use the `LogicalId` of a generated CloudFormation resource to access properties of that resource within your template file, just like you would for an CloudFormation resource that you have explicitly declared. For more information about `LogicalIds` in CloudFormation and AWS SAM templates, see [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) in the *AWS CloudFormation User Guide*.

**Note**  
The `LogicalIds` of some generated resources include a unique hash value to avoid namespace clashes. The `LogicalIds` of these resources are derived when the stack is created. You can retrieve them only after the stack has been created using the AWS Management Console, AWS CLI, or one of the AWS SDKs. We don't recommend referencing these resources by `LogicalId` because the hash values might change.

### Referencing generated CloudFormation resources by referenceable property
<a name="sam-specification-generated-resources-referencing-referenceable-property"></a>

For some generated resources, AWS SAM provides a referenceable property of the AWS SAM resource. You can use this property to reference a generated CloudFormation resource and its properties within your AWS SAM template file.

**Note**  
Not all generated CloudFormation resources have referenceable properties. For those resources, you must use the `LogicalId`.

## Generated CloudFormation resource scenarios
<a name="sam-specification-generated-resources-scenarios"></a>

The following table summarizes the AWS SAM resources and properties that make up the scenarios that generate CloudFormation resources. The topics in the **Scenarios** column provide details about the additional CloudFormation resources that AWS SAM generates for that scenario.


| AWS SAM resource | Base CloudFormation resource | Scenarios | 
| --- | --- | --- | 
| AWS::Serverless::Api  | [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) |  +  [DomainName property is specified](sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-domain-name) <br />+  [UsagePlan property is specified](sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-usage-plan)   | 
| AWS::Serverless::Application  | [AWS::CloudFormation::Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html) |  +  Other than generating the base CloudFormation resource, there are no additional scenarios for this serverless resource.   | 
| AWS::Serverless::CapacityProvider  | [AWS::Lambda::CapacityProvider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html) |  +  [OperatorRole property is not specified](sam-specification-generated-resources-capacityprovider.md#sam-specification-generated-resources-capacityprovider-iam-role)   | 
| AWS::Serverless::MicrovmImage  | [AWS::Lambda::MicrovmImage](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html) |  +  [BuildRoleArn property is not specified](sam-specification-generated-resources-microvmimage.md#sam-specification-generated-resources-microvmimage-iam-role)   | 
| AWS::Serverless::NetworkConnector  | [AWS::Lambda::NetworkConnector](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-networkconnector.html) |  +  [OperatorRole property is not specified](sam-specification-generated-resources-networkconnector.md#sam-specification-generated-resources-networkconnector-iam-role)   | 
| AWS::Serverless::Function | [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html) |  +  [AutoPublishAlias property is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-autopublishalias) <br />+  [Role property is not specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-not-role) <br />+  [DeploymentPreference property is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-deploymentpreference) <br />+  [An Api event source is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-api) <br />+  [An HttpApi event source is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-httpapi) <br />+  [A streaming event source is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-streaming) <br />+  [An event bridge (or event bus) event source is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-eventbridge) <br />+  [An IotRule event source is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-iotrule) <br />+  [OnSuccess (or OnFailure) property is specified for Amazon SNS events](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-sns-onsuccess) <br />+  [OnSuccess (or OnFailure) property is specified for Amazon SQS events](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-sqs-onsuccess)   | 
| AWS::Serverless::HttpApi | [AWS::ApiGatewayV2::Api](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html) |  +  [StageName property is specified](sam-specification-generated-resources-httpapi.md#sam-specification-generated-resources-httpapi-stage-name) <br />+  [StageName property is *not* specified](sam-specification-generated-resources-httpapi.md#sam-specification-generated-resources-httpapi-not-stage-name) <br />+  [DomainName property is specified](sam-specification-generated-resources-httpapi.md#sam-specification-generated-resources-httpapi-domain-name)   | 
| AWS::Serverless::LayerVersion  | [AWS::Lambda::LayerVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html) |  +  Other than generating the base CloudFormation resource, there are no additional scenarios for this serverless resource.   | 
| AWS::Serverless::SimpleTable  | [AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html) |  +  Other than generating the base CloudFormation resource, there are no additional scenarios for this serverless resource.   | 
| AWS::Serverless::StateMachine  | [AWS::StepFunctions::StateMachine](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html) |  +  [Role property is not specified](sam-specification-generated-resources-statemachine.md#sam-specification-generated-resources-statemachine-not-role) <br />+  [An API event source is specified](sam-specification-generated-resources-statemachine.md#sam-specification-generated-resources-statemachine-api) <br />+  [An event bridge (or event bus) event source is specified](sam-specification-generated-resources-statemachine.md#sam-specification-generated-resources-statemachine-eventbridge)   | 

**Topics**
+ [Referencing generated CloudFormation resources](#sam-specification-generated-resources-referencing)
+ [Generated CloudFormation resource scenarios](#sam-specification-generated-resources-scenarios)
+ [CloudFormation resources generated when AWS::Serverless::Api is specified](sam-specification-generated-resources-api.md)
+ [CloudFormation resources generated when AWS::Serverless::Application is specified](sam-specification-generated-resources-application.md)
+ [CloudFormation resources generated when AWS::Serverless::CapacityProvider is specified](sam-specification-generated-resources-capacityprovider.md)
+ [CloudFormation resources generated when you specify AWS::Serverless::Connector](sam-specification-generated-resources-connector.md)
+ [CloudFormation resources generated when AWS::Serverless::Function is specified](sam-specification-generated-resources-function.md)
+ [CloudFormation resources generated when AWS::Serverless::GraphQLApi is specified](sam-specification-generated-resources-graphqlapi.md)
+ [CloudFormation resources generated when AWS::Serverless::HttpApi is specified](sam-specification-generated-resources-httpapi.md)
+ [CloudFormation resources generated when AWS::Serverless::MicrovmImage is specified](sam-specification-generated-resources-microvmimage.md)
+ [CloudFormation resources generated when AWS::Serverless::NetworkConnector is specified](sam-specification-generated-resources-networkconnector.md)
+ [CloudFormation resources generated when AWS::Serverless::WebSocketApi is specified](sam-specification-generated-resources-websocketapi.md)
+ [CloudFormation resources generated when AWS::Serverless::LayerVersion is specified](sam-specification-generated-resources-layerversion.md)
+ [CloudFormation resources generated when AWS::Serverless::SimpleTable is specified](sam-specification-generated-resources-simpletable.md)
+ [CloudFormation resources generated when AWS::Serverless::StateMachine is specified](sam-specification-generated-resources-statemachine.md)