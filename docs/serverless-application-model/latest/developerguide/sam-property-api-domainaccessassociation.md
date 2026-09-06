

# DomainAccessAssociation
<a name="sam-property-api-domainaccessassociation"></a>

Configures a domain access association between an access association source and a private custom domain name. The only supported access association source is a VPC endpoint ID. For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html).

## Syntax
<a name="sam-property-api-domainaccessassociation-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-api-domainaccessassociation-syntax.yaml"></a>

```
 VpcEndpointId: {{String}}
```

## Properties
<a name="sam-property-api-domainaccessassociation-properties"></a>

 `VpcEndpointId`   <a name="sam-api-domainaccessassociation-vpcendpointid"></a>
The endpoint ID of the VPC interface endpoint associated with the API Gateway VPC service.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[ AccessAssociationSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainnameaccessassociation.html#cfn-apigateway-domainnameaccessassociation-accessassociationsource)` property of an `AWS::ApiGateway::DomainNameAccessAssociation` resource.