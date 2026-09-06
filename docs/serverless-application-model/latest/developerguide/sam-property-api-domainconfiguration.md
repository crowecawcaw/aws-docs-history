

# DomainConfiguration
<a name="sam-property-api-domainconfiguration"></a>

Configures a custom domain for an API.

## Syntax
<a name="sam-property-api-domainconfiguration-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-api-domainconfiguration-syntax.yaml"></a>

```
  [AccessAssociation](#sam-api-domainconfiguration-domainaccessassociation): {{DomainAccessAssociation}}
  [BasePath](#sam-api-domainconfiguration-basepath): {{List}}
  [CertificateArn](#sam-api-domainconfiguration-certificatearn): {{String}}
  [DomainName](#sam-api-domainconfiguration-domainname): {{String}}
  [EndpointAccessMode](#sam-api-domainconfiguration-endpointaccessmode): {{String}}
  [EndpointConfiguration](#sam-api-domainconfiguration-endpointconfiguration): {{String}}
  [MutualTlsAuthentication](#sam-api-domainconfiguration-mutualtlsauthentication): {{[MutualTlsAuthentication](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-mutualtlsauthentication)}}
  [NormalizeBasePath](#sam-api-domainconfiguration-normalizebasepath): {{Boolean}}
  [OwnershipVerificationCertificateArn](#sam-api-domainconfiguration-ownershipverificationcertificatearn): {{String}}
  [Policy: ](#sam-api-domainconfiguration-policy){{Json}}
  [Route53](#sam-api-domainconfiguration-route53): {{Route53Configuration}}
  [SecurityPolicy](#sam-api-domainconfiguration-securitypolicy): {{String}}
```

## Properties
<a name="sam-property-api-domainconfiguration-properties"></a>

 `AccessAssociation`   <a name="sam-api-domainconfiguration-domainaccessassociation"></a>
The configuration required to generate ` AWS::ApiGateway::DomainNameAccessAssociation` resource.  
AWS SAM generates an [AWS::ApiGateway::DomainNameAccessAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnameaccessassociation.html) resource when this property is set. For information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).  
*Type*: [DomainAccessAssociation](sam-property-api-domainaccessassociation.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `BasePath`   <a name="sam-api-domainconfiguration-basepath"></a>
A list of the basepaths to configure with the Amazon API Gateway domain name.  
*Type*: List  
*Required*: No  
*Default*: /  
*CloudFormation compatibility*: This property is similar to the `[BasePath](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html#cfn-apigateway-basepathmapping-basepath)` property of an `AWS::ApiGateway::BasePathMapping` resource. AWS SAM creates multiple `AWS::ApiGateway::BasePathMapping` resources, one per `BasePath` specified in this property.

 `CertificateArn`   <a name="sam-api-domainconfiguration-certificatearn"></a>
The Amazon Resource Name (ARN) of an AWS managed certificate this domain name's endpoint. AWS Certificate Manager is the only supported source.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is similar to the `[CertificateArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-certificatearn)` property of an `AWS::ApiGateway::DomainName` resource. If `EndpointConfiguration` is set to `REGIONAL` (the default value), `CertificateArn` maps to [RegionalCertificateArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-regionalcertificatearn) in `AWS::ApiGateway::DomainName`. If the `EndpointConfiguration` is set to `EDGE`, `CertificateArn` maps to [CertificateArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-certificatearn) in `AWS::ApiGateway::DomainName`. If `EndpointConfiguration` is set to `PRIVATE`, this property is passed to the [AWS::ApiGateway::DomainNameV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2) resource.  
*Additional notes*: For an `EDGE` endpoint, you must create the certificate in the `us-east-1` AWS Region.

 `DomainName`   <a name="sam-api-domainconfiguration-domainname"></a>
The custom domain name for your API Gateway API. Uppercase letters are not supported.  
AWS SAM generates an [AWS::ApiGateway::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html) resource when this property is set. For information about this scenario, see [DomainName property is specified](sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-domain-name). For information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-domainname)` property of an `AWS::ApiGateway::DomainName` resource, or to [`AWS::ApiGateway::DomainNameV2`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2) when EndpointConfiguration is set to `PRIVATE`.

 `EndpointConfiguration`   <a name="sam-api-domainconfiguration-endpointconfiguration"></a>
Defines the type of API Gateway endpoint to map to the custom domain. The value of this property determines how the `CertificateArn` property is mapped in CloudFormation.  
*Valid values*: `EDGE`, `REGIONAL`, or `PRIVATE`  
*Type*: String  
*Required*: No  
*Default*: `REGIONAL`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `EndpointAccessMode`   <a name="sam-api-domainconfiguration-endpointaccessmode"></a>
The access mode for the custom domain name endpoint. Required when using enhanced security policies (those prefixed with `SecurityPolicy_`).  
*Valid values*: `STRICT` or `BASIC`  
*Type*: String  
*Required*: Conditional  
*CloudFormation compatibility*: This property is passed directly to the `[EndpointAccessMode](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-endpointaccessmode)` property of an `AWS::ApiGateway::DomainName` resource, or to [`AWS::ApiGateway::DomainNameV2`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2) when `EndpointConfiguration` is set to `PRIVATE`.

 `MutualTlsAuthentication`   <a name="sam-api-domainconfiguration-mutualtlsauthentication"></a>
The mutual Transport Layer Security (TLS) authentication configuration for a custom domain name.  
*Type*: [MutualTlsAuthentication](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-mutualtlsauthentication)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MutualTlsAuthentication](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-mutualtlsauthentication)` property of an `AWS::ApiGateway::DomainName` resource.

 `NormalizeBasePath`   <a name="sam-api-domainconfiguration-normalizebasepath"></a>
Indicates whether non-alphanumeric characters are allowed in basepaths defined by the `BasePath` property. When set to `True`, non-alphanumeric characters are removed from basepaths.  
Use `NormalizeBasePath` with the `BasePath` property.  
*Type*: Boolean  
*Required*: No  
*Default*: True  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `OwnershipVerificationCertificateArn`   <a name="sam-api-domainconfiguration-ownershipverificationcertificatearn"></a>
The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Required only when you configure mutual TLS and you specify an ACM imported or private CA certificate ARN for the `CertificateArn`.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[OwnershipVerificationCertificateArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-ownershipverificationcertificatearn)` property of an `AWS::ApiGateway::DomainName` resource.

 `Policy`   <a name="sam-api-domainconfiguration-policy"></a>
The IAM policy to attach to the API Gateway domain name. Only applicable when `EndpointConfiguration` is set to `PRIVATE`.  
*Type*: Json  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `Policy` property of an `AWS::ApiGateway::DomainNameV2` resource when `EndpointConfiguration` is set to `PRIVATE`. For examples of valid policy documents, see [AWS::ApiGateway::DomainNameV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2).

 `Route53`   <a name="sam-api-domainconfiguration-route53"></a>
Defines an Amazon Route 53 configuration.  
*Type*: [Route53Configuration](sam-property-api-route53configuration.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `SecurityPolicy`   <a name="sam-api-domainconfiguration-securitypolicy"></a>
The TLS version plus cipher suite for this domain name.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[SecurityPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html#cfn-apigateway-domainname-securitypolicy)` property of an `AWS::ApiGateway::DomainName` resource, or to [`AWS::ApiGateway::DomainNameV2`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2) when `EndpointConfiguration` is set to `PRIVATE`. For `PRIVATE` endpoints, only TLS\_1\_2 is supported.

## Examples
<a name="sam-property-api-domainconfiguration--examples"></a>

### DomainName
<a name="sam-property-api-domainconfiguration--examples--domainname"></a>

DomainName example

#### YAML
<a name="sam-property-api-domainconfiguration--examples--domainname--yaml"></a>

```
Domain:
  DomainName: www.example.com
  CertificateArn: arn-example
  EndpointConfiguration: EDGE
  Route53:
    HostedZoneId: Z1PA6795UKMFR9
  BasePath:
    - foo
    - bar
```