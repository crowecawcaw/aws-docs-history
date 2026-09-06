

# WebSocketApiDomainConfiguration
<a name="sam-property-websocketapi-websocketapidomainconfiguration"></a>

Configures a custom domain for a WebSocket API.

## Syntax
<a name="sam-property-websocketapi-websocketapidomainconfiguration-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-websocketapi-websocketapidomainconfiguration-syntax.yaml"></a>

```
  [BasePath](#sam-websocketapi-websocketapidomainconfiguration-basepath): {{List}}
  [CertificateArn](#sam-websocketapi-websocketapidomainconfiguration-certificatearn): {{String}}
  [DomainName](#sam-websocketapi-websocketapidomainconfiguration-domainname): {{String}}
  [EndpointConfiguration](#sam-websocketapi-websocketapidomainconfiguration-endpointconfiguration): {{String}}
  [Route53](#sam-websocketapi-websocketapidomainconfiguration-route53): {{Route53Configuration}}
  [SecurityPolicy](#sam-websocketapi-websocketapidomainconfiguration-securitypolicy): {{String}}
```

## Properties
<a name="sam-property-websocketapi-websocketapidomainconfiguration-properties"></a>

 `BasePath`   <a name="sam-websocketapi-websocketapidomainconfiguration-basepath"></a>
A list of the basepaths to configure with the Amazon API Gateway domain name.  
*Type*: List  
*Required*: No  
*Default*: /  
*CloudFormation compatibility*: This property is similar to the `[ApiMappingKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey)` property of an `AWS::ApiGatewayV2::ApiMapping` resource. AWS SAM creates multiple `AWS::ApiGatewayV2::ApiMapping` resources, one per value specified in this property.

 `CertificateArn`   <a name="sam-websocketapi-websocketapidomainconfiguration-certificatearn"></a>
The Amazon Resource Name (ARN) of an AWS managed certificate for this domain name's endpoint. AWS Certificate Manager is the only supported source.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[CertificateArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn)` property of an `AWS::ApiGatewayV2::DomainName DomainNameConfiguration` resource.

 `DomainName`   <a name="sam-websocketapi-websocketapidomainconfiguration-domainname"></a>
The custom domain name for your API Gateway WebSocket API. Uppercase letters are not supported.  
AWS SAM generates an `AWS::ApiGatewayV2::DomainName` resource when this property is set. For information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname)` property of an `AWS::ApiGatewayV2::DomainName` resource.

 `EndpointConfiguration`   <a name="sam-websocketapi-websocketapidomainconfiguration-endpointconfiguration"></a>
Defines the type of API Gateway endpoint to map to the custom domain. The value of this property determines how the `CertificateArn` property is mapped in CloudFormation.  
The only valid value for WebSocket APIs is `REGIONAL`.  
*Type*: String  
*Required*: No  
*Default*: `REGIONAL`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Route53`   <a name="sam-websocketapi-websocketapidomainconfiguration-route53"></a>
Defines an Route 53 configuration.  
*Type*: [Route53Configuration](sam-property-websocketapi-route53configuration.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `SecurityPolicy`   <a name="sam-websocketapi-websocketapidomainconfiguration-securitypolicy"></a>
The TLS version of the security policy for this domain name.  
The only valid value for WebSocket APIs is `TLS_1_2`.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[SecurityPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy)` property of the `AWS::ApiGatewayV2::DomainName` `DomainNameConfiguration` data type.

## Examples
<a name="sam-property-websocketapi-websocketapidomainconfiguration--examples"></a>

### DomainName
<a name="sam-property-websocketapi-websocketapidomainconfiguration--examples--domainname"></a>

DomainName example

#### YAML
<a name="sam-property-websocketapi-websocketapidomainconfiguration--examples--domainname--yaml"></a>

```
Domain:
  DomainName: ws.example.com
  CertificateArn: arn:aws:acm:us-east-1:123456789012:certificate/example
  EndpointConfiguration: REGIONAL
  Route53:
    HostedZoneId: Z1PA6795UKMFR9
  BasePath:
    - v1
    - v2
```