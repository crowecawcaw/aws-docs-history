

# Runtime
<a name="sam-property-graphqlapi-resolver-runtime"></a>

The runtime of your pipeline resolver or function. Specifies the name and version to use.

## Syntax
<a name="sam-property-graphqlapi-resolver-runtime-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-resolver-runtime-syntax-yaml"></a>

```
Name: {{String}}
Version: {{String}}
```

## Properties
<a name="sam-property-graphqlapi-resolver-runtime-properties"></a>

`Name`  <a name="sam-graphqlapi-resolver-runtime-name"></a>
The name of the runtime to use. Currently, the only allowed value is `APPSYNC_JS`.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-name)` property of an `AWS::AppSync::Resolver AppSyncRuntime` object.

`Version`  <a name="sam-graphqlapi-resolver-runtime-version"></a>
The version of the runtime to use. Currently, the only allowed version is `1.0.0`.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[RuntimeVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html#cfn-appsync-resolver-appsyncruntime-runtimeversion)` property of an `AWS::AppSync::Resolver AppSyncRuntime` object.