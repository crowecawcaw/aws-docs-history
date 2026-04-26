# WebSocketApiDomainConfiguration

Configures a custom domain for a WebSocket API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  BasePath: `List`
  CertificateArn: `String`
  DomainName: `String`
  EndpointConfiguration: `String`
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

_CloudFormation compatibility_: This property is passed directly to the `CertificateArn` property of an `AWS::ApiGatewayV2::DomainName DomainNameConfiguration` resource.

`DomainName`

The custom domain name for your API Gateway WebSocket API. Uppercase letters are not supported.

AWS SAM generates an `AWS::ApiGatewayV2::DomainName` resource when this property is set. For information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `DomainName` property of an `AWS::ApiGatewayV2::DomainName` resource.

`EndpointConfiguration`

Defines the type of API Gateway endpoint to map to the custom domain. The value of this property determines how the `CertificateArn` property is mapped in CloudFormation.

The only valid value for WebSocket APIs is `REGIONAL`.

_Type_: String

_Required_: No

_Default_: `REGIONAL`

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Route53`

Defines an Route 53 configuration.

_Type_: [Route53Configuration](sam-property-websocketapi-route53configuration.md "sam-property-websocketapi-route53configuration.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`SecurityPolicy`

The TLS version of the security policy for this domain name.

The only valid value for WebSocket APIs is `TLS_1_2`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `SecurityPolicy` property of the `AWS::ApiGatewayV2::DomainName` `DomainNameConfiguration` data type.

## Examples

### DomainName

DomainName example

#### YAML

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
