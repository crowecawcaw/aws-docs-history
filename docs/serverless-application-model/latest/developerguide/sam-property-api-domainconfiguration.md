# DomainConfiguration

Configures a custom domain for an API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AccessAssociation: `DomainAccessAssociation`
  BasePath: `List`
  CertificateArn: `String`
  DomainName: `String`
  EndpointConfiguration: `String`
  MutualTlsAuthentication: `MutualTlsAuthentication`
  NormalizeBasePath: `Boolean`
  OwnershipVerificationCertificateArn: `String`
  Policy: `Json`
  Route53: `Route53Configuration`
  SecurityPolicy: `String`

```

## Properties

`AccessAssociation`

The configuration required to generate `AWS::ApiGateway::DomainNameAccessAssociation` resource.

AWS SAM generates an [AWS::ApiGateway::DomainNameAccessAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnameaccessassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnameaccessassociation.md") resource when
this property is set.
For information about generated AWS CloudFormation resources, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: [DomainAccessAssociation](sam-property-api-domainaccessassociation.md "sam-property-api-domainaccessassociation.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`BasePath`

A list of the basepaths to configure with the Amazon API Gateway domain name.

_Type_: List

_Required_: No

_Default_: /

_AWS CloudFormation compatibility_: This property is similar to the
`BasePath` property of an `AWS::ApiGateway::BasePathMapping` resource. AWS SAM creates multiple `AWS::ApiGateway::BasePathMapping` resources, one per `BasePath` specified in this property.

`CertificateArn`

The Amazon Resource Name (ARN) of an AWS managed certificate this domain name's endpoint. AWS Certificate Manager is the only supported source.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is similar to the
`CertificateArn` property of an
`AWS::ApiGateway::DomainName` resource. If `EndpointConfiguration` is set to `REGIONAL` (the default value),
`CertificateArn` maps to [RegionalCertificateArn](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md#cfn-apigateway-domainname-regionalcertificatearn "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md#cfn-apigateway-domainname-regionalcertificatearn")
in `AWS::ApiGateway::DomainName`. If the `EndpointConfiguration` is set to `EDGE`, `CertificateArn` maps to
[CertificateArn](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md#cfn-apigateway-domainname-certificatearn "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md#cfn-apigateway-domainname-certificatearn") in `AWS::ApiGateway::DomainName`.
If `EndpointConfiguration` is set to `PRIVATE`, this property is passed to the
[AWS::ApiGateway::DomainNameV2](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md") resource.

_Additional notes_: For an `EDGE` endpoint, you must create the certificate in the `us-east-1` AWS Region.

`DomainName`

The custom domain name for your API Gateway API. Uppercase letters are not supported.

AWS SAM generates an [AWS::ApiGateway::DomainName](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md") resource when this property is set. For information about this scenario, see [DomainName
property is specified](sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-domain-name "sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-domain-name"). For information about generated AWS CloudFormation resources, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`DomainName`
property of an `AWS::ApiGateway::DomainName` resource, or to [`AWS::ApiGateway::DomainNameV2`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md")
when EndpointConfiguration is set to `PRIVATE`.

`EndpointConfiguration`

Defines the type of API Gateway endpoint to map to the custom domain. The value of this property determines how the `CertificateArn` property is mapped in AWS CloudFormation.

_Valid values_: `EDGE`, `REGIONAL`, or
`PRIVATE`

_Type_: String

_Required_: No

_Default_: `REGIONAL`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`MutualTlsAuthentication`

The mutual Transport Layer Security (TLS) authentication configuration for a custom domain name.

_Type_: [MutualTlsAuthentication](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md#cfn-apigateway-domainname-mutualtlsauthentication "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.md#cfn-apigateway-domainname-mutualtlsauthentication")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `MutualTlsAuthentication` property of an `AWS::ApiGateway::DomainName` resource.

`NormalizeBasePath`

Indicates whether non-alphanumeric characters are allowed in basepaths defined by the
`BasePath` property. When set to `True`, non-alphanumeric characters are removed
from basepaths.

Use `NormalizeBasePath` with the `BasePath` property.

_Type_: Boolean

_Required_: No

_Default_: True

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an
AWS CloudFormation equivalent.

`OwnershipVerificationCertificateArn`

The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Required only when you configure mutual TLS and you specify an ACM imported or private CA certificate ARN for the `CertificateArn`.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`OwnershipVerificationCertificateArn` property of an `AWS::ApiGateway::DomainName` resource.

`Policy`

The IAM policy to attach to the API Gateway domain name. Only applicable when `EndpointConfiguration` is set to `PRIVATE`.

_Type_: Json

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Policy` property of an
`AWS::ApiGateway::DomainNameV2` resource when `EndpointConfiguration` is set to `PRIVATE`. For examples of valid policy documents, see
[AWS::ApiGateway::DomainNameV2](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md").

`Route53`

Defines an Amazon Route 53 configuration.

_Type_: [Route53Configuration](sam-property-api-route53configuration.md "sam-property-api-route53configuration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`SecurityPolicy`

The TLS version plus cipher suite for this domain name.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`SecurityPolicy`
property of an `AWS::ApiGateway::DomainName` resource, or to [`AWS::ApiGateway::DomainNameV2`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnamev2.md")
when `EndpointConfiguration` is set to `PRIVATE`. For `PRIVATE` endpoints, only TLS_1_2 is supported.

## Examples

### DomainName

DomainName example

#### YAML

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
