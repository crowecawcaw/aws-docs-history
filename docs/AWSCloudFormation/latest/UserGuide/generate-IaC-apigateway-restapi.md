# How to resolve issues with write-only

properties in AWS::ApiGateway::RestAPI resources

This topic explains how to resolve issues with write-only properties in [AWS::ApiGateway::RestApi](../TemplateReference/aws-resource-apigateway-restapi.md "../TemplateReference/aws-resource-apigateway-restapi.md") resources when using the IaC
generator.

## Issue

When a generated template contains `AWS::ApiGateway::RestApi` resources, then
warnings are generated stating that `Body`, `BodyS3Location`, and
`CloneFrom` properties are identified as `UNSUPPORTED_PROPERTIES`.
This is because these are optional write-only properties. The IaC generator doesn't know
whether these properties were ever applied to the resource. Therefore, it omits
these properties in the generated template.

## Resolution

To set the `Body` property for your REST API, update your generated
template.

1. Use the Amazon API Gateway [GetExport](../../../apigateway/latest/api/API_GetExport.md "../../../apigateway/latest/api/API_GetExport.md") API
   action to download the API. For example, by using the [aws apigateway
   get-export](../../../cli/latest/reference/apigateway/get-export.md "../../../cli/latest/reference/apigateway/get-export.md") AWS CLI command. For more information, see [Export a REST API from API Gateway](../../../apigateway/latest/developerguide/api-gateway-export-api.md "../../../apigateway/latest/developerguide/api-gateway-export-api.md") in the
   _API Gateway Developer Guide_.
2. Retrieve the `Body` property from the response of the
   `GetExport` API action. Upload it to an Amazon S3 bucket.
3. Download the generated template.
4. Add the `BodyS3Location/Bucket` and `BodyS3Location/Key`
   properties to the template, specifying the bucket name and key where the `Body`
   is stored.
5. Open the generated template in the IaC generator console and choose **Import
   edited template**.
