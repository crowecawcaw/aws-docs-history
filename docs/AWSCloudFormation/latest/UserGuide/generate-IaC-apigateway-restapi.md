# How to resolve issues with write-only
 properties in AWS::ApiGateway::RestAPI resources

This topic explains how to resolve issues with write-only properties in [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html") resources when using the IaC
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


1. Use the Amazon API Gateway [GetExport](https://docs.aws.amazon.com/apigateway/latest/api/API_GetExport.html "https://docs.aws.amazon.com/apigateway/latest/api/API_GetExport.html") API
 action to download the API. For example, by using the [aws apigateway
 get-export](https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-export.html "https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-export.html") AWS CLI command. For more information, see [Export a REST API from API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html "https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html") in the
 *API Gateway Developer Guide*.
2. Retrieve the `Body` property from the response of the
 `GetExport` API action. Upload it to an Amazon S3 bucket.
3. Download the generated template.
4. Add the `BodyS3Location/Bucket` and `BodyS3Location/Key`
 properties to the template, specifying the bucket name and key where the `Body`
 is stored.
5. Open the generated template in the IaC generator console and choose **Import
 edited template**.
