

# CloudFormation resources generated when AWS::Serverless::WebFunction is specified
<a name="sam-specification-generated-resources-webfunction"></a>

When you specify an `AWS::Serverless::WebFunction`, AWS Serverless Application Model (AWS SAM) generates the following base CloudFormation resources.

**`AWS::Lambda::WebFunction`**  
*`LogicalId`: *`{{<webfunction‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::Lambda::WebFunctionRevision`**  
*`LogicalId`: *`{{<webfunction‑LogicalId>}}Revision`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::Lambda::WebFunctionEndpoint`**  
*`LogicalId`: *`{{<webfunction‑LogicalId>}}Endpoint`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

All three resources use the same function name. If you don't specify the `FunctionName` property, AWS SAM generates a name of the form `{{<webfunction‑LogicalId>}}-{{<stack-id-prefix>}}`, where {{stack-id-prefix}} is the first 8 characters of the stack ID's unique identifier. AWS SAM shortens the logical ID if needed so that the name is at most 64 characters.

In addition to these CloudFormation resources, when `AWS::Serverless::WebFunction` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [ExecutionRoleArn property is not specified](#sam-specification-generated-resources-webfunction-iam-role)

## ExecutionRoleArn property is not specified
<a name="sam-specification-generated-resources-webfunction-iam-role"></a>

When you don't specify the `ExecutionRoleArn` property of an `AWS::Serverless::WebFunction`, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource with the `AWSLambdaBasicExecutionRole` AWS managed policy attached.

The role trust policy allows the `lambda.amazonaws.com` service principal to assume the role.

**`AWS::IAM::Role`**  
*`LogicalId`: *`{{<webfunction‑LogicalId>}}Role`