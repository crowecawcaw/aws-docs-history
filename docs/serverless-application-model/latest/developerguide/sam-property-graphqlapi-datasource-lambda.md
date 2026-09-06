

# Lambda
<a name="sam-property-graphqlapi-datasource-lambda"></a>

Configure an AWS Lambda function as a data source for your GraphQL API resolver.

## Syntax
<a name="sam-property-graphqlapi-datasource-lambda-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-datasource-lambda-syntax-yaml"></a>

```
{{LogicalId}}:
  Description: {{String}}
  FunctionArn: {{String}}
  Name: {{String}}
  ServiceRoleArn: {{String}}
```

## Properties
<a name="sam-property-graphqlapi-datasource-lambda-properties"></a>

`Description`  <a name="sam-graphqlapi-datasource-lambda-description"></a>
The description of your data source.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description)` property of an `AWS::AppSync::DataSource` resource.

`FunctionArn`  <a name="sam-graphqlapi-datasource-lambda-functionarn"></a>
The ARN for the Lambda function.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[LambdaFunctionArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html#cfn-appsync-datasource-lambdaconfig-lambdafunctionarn)` property of an `AWS::AppSync::DataSource LambdaConfig` object.

`LogicalId`  <a name="sam-graphqlapi-datasource-lambda-logicalid"></a>
The unique name of your data source.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name)` property of an `AWS::AppSync::DataSource` resource.

`Name`  <a name="sam-graphqlapi-datasource-lambda-name"></a>
The name of your data source. Specify this property to override the `LogicalId` value.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name)` property of an `AWS::AppSync::DataSource` resource.

`ServiceRoleArn`  <a name="sam-graphqlapi-datasource-lambda-servicerolearn"></a>
The AWS Identity and Access Management (IAM) service role ARN for the data source. The system assumes this role when accessing the data source.  
To revoke access to your data source, remove the Lambda object from your AWS SAM template.
*Type*: String  
*Required*: No. If not specified, AWS SAM will provision `Write` permissions using [AWS SAM connectors](managing-permissions-connectors.md).  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceRoleArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn)` property of an `AWS::AppSync::DataSource` resource.