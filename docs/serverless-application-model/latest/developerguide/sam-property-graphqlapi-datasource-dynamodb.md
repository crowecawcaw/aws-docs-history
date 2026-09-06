

# DynamoDb
<a name="sam-property-graphqlapi-datasource-dynamodb"></a>

Configure an Amazon DynamoDB table as a data source for your GraphQL API resolver.

## Syntax
<a name="sam-property-graphqlapi-datasource-dynamodb-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-datasource-dynamodb-syntax-yaml"></a>

```
{{LogicalId}}:
  DeltaSync: {{[DeltaSyncConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)}}
  Description: {{String}}
  Name: {{String}}
  Permissions: {{List}}
  Region: {{String}}
  ServiceRoleArn: {{String}}
  TableArn: {{String}}
  TableName: {{String}}
  UseCallerCredentials: {{Boolean}}
  Versioned: {{Boolean}}
```

## Properties
<a name="sam-property-graphqlapi-datasource-dynamodb-properties"></a>

`DeltaSync`  <a name="sam-graphqlapi-datasource-dynamodb-deltasync"></a>
Describes a Delta Sync configuration.  
*Type*: [DeltaSyncConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[DeltaSyncConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig)` property of an `AWS::AppSync::DataSource DynamoDBConfig` object.

`Description`  <a name="sam-graphqlapi-datasource-dynamodb-description"></a>
The description of your data source.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description)` property of an `AWS::AppSync::DataSource` resource.

`LogicalId`  <a name="sam-graphqlapi-datasource-dynamodb-logicalid"></a>
The unique name of your data source.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name)` property of an `AWS::AppSync::DataSource` resource.

`Name`  <a name="sam-graphqlapi-datasource-dynamodb-name"></a>
The name of your data source. Specify this property to override the `LogicalId` value.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name)` property of an `AWS::AppSync::DataSource` resource.

`Permissions`  <a name="sam-graphqlapi-datasource-dynamodb-permissions"></a>
Provision permissions to your data source using [AWS SAM connectors](managing-permissions-connectors.md). You can provide any of the following values in a list:  
+ `Read` – Allow your resolver to read your data source.
+ `Write` – Allow your resolver to write to your data source.
AWS SAM uses an `AWS::Serverless::Connector` resource which is transformed at deployment to provision your permissions. To learn about generated resources, see [CloudFormation resources generated when you specify AWS::Serverless::Connector](sam-specification-generated-resources-connector.md).  
You can specify `Permissions` or `ServiceRoleArn`, but not both. If neither are specified, AWS SAM will generate default values of `Read` and `Write`. To revoke access to your data source, remove the DynamoDB object from your AWS SAM template.
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent. It is similar to the `Permissions` property of an `AWS::Serverless::Connector` resource.

`Region`  <a name="sam-graphqlapi-datasource-dynamodb-region"></a>
The AWS Region of your DynamoDB table. If you don’t specify it, AWS SAM uses `[AWS::Region](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html#cfn-pseudo-param-region)`.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[AwsRegion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-awsregion)` property of an `AWS::AppSync::DataSource DynamoDBConfig` object.

`ServiceRoleArn`  <a name="sam-graphqlapi-datasource-dynamodb-servicerolearn"></a>
The AWS Identity and Access Management (IAM) service role ARN for the data source. The system assumes this role when accessing the data source.  
You can specify `Permissions` or `ServiceRoleArn`, but not both.  
*Type*: String  
*Required*: No. If not specified, AWS SAM applies the default value for `Permissions`.  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceRoleArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn)` property of an `AWS::AppSync::DataSource` resource.

`TableArn`  <a name="sam-graphqlapi-datasource-dynamodb-tablearn"></a>
The ARN for the DynamoDB table.  
*Type*: String  
*Required*: Conditional. If you don’t specify `ServiceRoleArn`, `TableArn` is required.  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`TableName`  <a name="sam-graphqlapi-datasource-dynamodb-tablename"></a>
The table name.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[TableName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-tablename)` property of an `AWS::AppSync::DataSource DynamoDBConfig` object.

`UseCallerCredentials`  <a name="sam-graphqlapi-datasource-dynamodb-usecallercredentials"></a>
Set to `true` to use IAM with this data source.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[UseCallerCredentials](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-usecallercredentials)` property of an `AWS::AppSync::DataSource DynamoDBConfig` object.

`Versioned`  <a name="sam-graphqlapi-datasource-dynamodb-versioned"></a>
Set to `true` to use [Conflict Detection, Conflict Resolution, and Sync](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html) with this data source.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Versioned](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-versioned)` property of an `AWS::AppSync::DataSource DynamoDBConfig` object.