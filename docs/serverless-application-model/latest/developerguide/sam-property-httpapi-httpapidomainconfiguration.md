# HttpApiDomainConfiguration

Configures a custom domain for an API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  BasePath: `List`
  CertificateArn: `String`
  DomainName: `String`
  EndpointConfiguration: `String`
  MutualTlsAuthentication: `MutualTlsAuthentication`
  OwnershipVerificationCertificateArn: `String`
  Route53: `Route53Configuration`
  SecurityPolicy: `String`

```

## Properties

`BasePath`

A list of the basepaths to configure with the Amazon API Gateway domain name.

_Type_: List

_Required_: No

_Default_: /

_CloudFormation compatibility_: This property is similar to the `ApiMappingKey` property of an `AWS::ApiGatewayV2::ApiMapping` resource. AWS SAM creates multiple `AWS::ApiGatewayV2::ApiMapping` resources, one per value specified in this property.

`CertificateArn`

The Amazon Resource Name (ARN) of an AWS managed certificate for this domain name's endpoint. AWS Certificate Manager is the only supported source.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `CertificateArn` property of an `AWS::ApiGateway2::DomainName DomainNameConfiguration` resource.

`DomainName`

The custom domain name for your API Gateway API. Uppercase letters are not supported.

AWS SAM generates an `AWS::ApiGatewayV2::DomainName` resource when this property is set. For information about this scenario, see [DomainName
property is specified](sam-specification-generated-resources-httpapi.md#sam-specification-generated-resources-httpapi-domain-name "sam-specification-generated-resources-httpapi.md#sam-specification-generated-resources-httpapi-domain-name"). For information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `DomainName` property of an `AWS::ApiGateway2::DomainName` resource.

`EndpointConfiguration`

Defines the type of API Gateway endpoint to map to the custom domain. The value of this property determines how the `CertificateArn` property is mapped in CloudFormation.

The only valid value for HTTP APIs is `REGIONAL`.

_Type_: String

_Required_: No

_Default_: `REGIONAL`

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`MutualTlsAuthentication`

The mutual transport layer security (TLS) authentication configuration for a custom domain name.

_Type_: [MutualTlsAuthentication](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.md#cfn-apigatewayv2-domainname-mutualtlsauthentication "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.md#cfn-apigatewayv2-domainname-mutualtlsauthentication")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `MutualTlsAuthentication` property of an `AWS::ApiGatewayV2::DomainName` resource.

`OwnershipVerificationCertificateArn`

The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Required only when you configure mutual TLS and you specify an ACM imported or private CA certificate ARN for the `CertificateArn`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `OwnershipVerificationCertificateArn` property of the `AWS::ApiGatewayV2::DomainName` `DomainNameConfiguration` data type.

`Route53`

Defines an Amazon Route 53 configuration.

_Type_: [Route53Configuration](sam-property-httpapi-route53configuration.md "sam-property-httpapi-route53configuration.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`SecurityPolicy`

The TLS version of the security policy for this domain name.

The only valid value for HTTP APIs is `TLS_1_2`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `SecurityPolicy` property of the `AWS::ApiGatewayV2::DomainName` `DomainNameConfiguration` data type.

## Examples

### DomainName

DomainName example

#### YAML

```
Domain:
  DomainName: www.example.com
  CertificateArn: arn-example
  EndpointConfiguration: REGIONAL
  Route53:
    HostedZoneId: Z1PA6795UKMFR9
  BasePath:
    - foo
    - bar

```
