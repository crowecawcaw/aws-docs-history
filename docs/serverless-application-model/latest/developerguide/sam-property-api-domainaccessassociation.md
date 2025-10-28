# DomainAccessAssociation

Configures a domain access association between an access association source and a private
custom domain name. The only supported access association source is a VPC endpoint ID. For
more information, see [Custom domain names for private APIs in API Gateway](../../../apigateway/latest/developerguide/apigateway-private-custom-domains.md "../../../apigateway/latest/developerguide/apigateway-private-custom-domains.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
 VpcEndpointId: `String`
```

## Properties

`VpcEndpointId`

The endpoint ID of the VPC interface endpoint associated with the API Gateway
VPC service.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly
to the `AccessAssociationSource` property of an
`AWS::ApiGateway::DomainNameAccessAssociation` resource.
