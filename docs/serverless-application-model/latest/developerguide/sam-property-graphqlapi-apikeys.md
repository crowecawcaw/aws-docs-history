

# ApiKeys
<a name="sam-property-graphqlapi-apikeys"></a>

Create a unique key that can be used to perform GraphQL operations requiring an API key.

## Syntax
<a name="sam-property-graphqlapi-apikeys-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-apikeys-syntax-yaml"></a>

```
{{LogicalId}}:
  ApiKeyId: {{String}}
  Description: {{String}}
  ExpiresOn: {{Double}}
```

## Properties
<a name="sam-property-graphqlapi-apikeys-properties"></a>

`ApiKeyId`  <a name="sam-graphqlapi-apikeys-apikeyid"></a>
The unique name of your API key. Specify to override the `LogicalId` value.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[ApiKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid)` property of an `AWS::AppSync::ApiKey` resource.

`Description`  <a name="sam-graphqlapi-apikeys-description"></a>
Description of your API key.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description)` property of an `AWS::AppSync::ApiKey` resource.

`ExpiresOn`  <a name="sam-graphqlapi-apikeys-expireson"></a>
The time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour.  
*Type*: Double  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Expires](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires)` property of an `AWS::AppSync::ApiKey` resource.

`LogicalId`  <a name="sam-graphqlapi-apikeys-logicalid"></a>
The unique name of your API key.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[ApiKeyId](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid)` property of an `AWS::AppSync::ApiKey` resource.