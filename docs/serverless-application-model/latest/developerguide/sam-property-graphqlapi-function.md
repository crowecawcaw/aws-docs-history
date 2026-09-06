

# Function
<a name="sam-property-graphqlapi-function"></a>

Configure functions in GraphQL APIs to perform certain operations.

## Syntax
<a name="sam-property-graphqlapi-function-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-function-syntax-yaml"></a>

```
{{LogicalId}}:
  CodeUri: {{String}}
  DataSource: {{String}}
  Description: {{String}}
  Id: {{String}}
  InlineCode: {{String}}
  MaxBatchSize: {{Integer}}
  Name: {{String}}
  Runtime: {{Runtime}}
  Sync: {{[SyncConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)}}
```

## Properties
<a name="sam-property-graphqlapi-function-properties"></a>

`CodeUri`  <a name="sam-graphqlapi-function-codeuri"></a>
The function code’s Amazon Simple Storage Service (Amazon S3) URI or path to local folder.  
If you specify a path to a local folder, CloudFormation requires that the file is first uploaded to Amazon S3 before deployment. You can use the AWS SAM CLI to facilitate this process. For more information, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md).  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CodeS3Location](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-codes3location)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`DataSource`  <a name="sam-graphqlapi-function-datasource"></a>
The name of the data source that this function will attach to.  
+ To reference a data source within the `AWS::Serverless::GraphQLApi` resource, specify its logical ID.
+ To reference a data source outside of the `AWS::Serverless::GraphQLApi` resource, provide its `Name` attribute using the `Fn::GetAtt` intrinsic function. For example, `!GetAtt MyLambdaDataSource.Name`.
+ To reference a data source from a different stack, use `[Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html)`.
If a variation of `[NONE | None | none]` is specified, AWS SAM will generate a `None` value for the `AWS::AppSync::DataSource` `[Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type)` object.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[DataSourceName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`Description`  <a name="sam-graphqlapi-function-description"></a>
The description of your function.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`Id`  <a name="sam-graphqlapi-function-id"></a>
The Function ID for a function located outside of the `AWS::Serverless::GraphQLApi` resource.  
+ To reference a function within the same AWS SAM template, use the `Fn::GetAtt` intrinsic function. For example `Id: !GetAtt createPostItemFunc.FunctionId`.
+ To reference a function from a different stack, use `[Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html)`.
When using `Id`, all other properties are not allowed. AWS SAM will automatically pass the Function ID of your referenced function.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`InlineCode`  <a name="sam-graphqlapi-function-inlinecode"></a>
The function code that contains the request and response functions.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Code](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-code)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`LogicalId`  <a name="sam-graphqlapi-function-logicalid"></a>
The unique name of your function.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`MaxBatchSize`  <a name="sam-graphqlapi-function-maxbatchsize"></a>
The maximum number of resolver request inputs that will be sent to a single AWS Lambda function in a `BatchInvoke` operation.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the [MaxBatchSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-maxbatchsize) property of an `AWS::AppSync::FunctionConfiguration` resource.

`Name`  <a name="sam-graphqlapi-function-name"></a>
The name of the function. Specify to override the `LogicalId` value.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`Runtime`  <a name="sam-graphqlapi-function-runtime"></a>
Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use.  
*Type*: [Runtime](sam-property-graphqlapi-function-runtime.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent. It is similar to the `[Runtime](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-runtime)` property of an `AWS::AppSync::FunctionConfiguration` resource.

`Sync`  <a name="sam-graphqlapi-function-sync"></a>
Describes a Sync configuration for a function.  
Specifies which Conflict Detection strategy and Resolution strategy to use when the function is invoked.  
*Type*: [SyncConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[SyncConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig)` property of an `AWS::AppSync::FunctionConfiguration` resource.