# Set up a private integration

To create a
private integration with an Application Load Balancer or Network Load Balancer, you create an HTTP proxy integration, specify the
[VPC link V2](apigateway-vpc-links-v2.md "apigateway-vpc-links-v2.md") to use, and
provide the ARN of an Network Load Balancer or an Application Load Balancer. By default, private integration traffic uses the HTTP protocol. To use HTTPS, specify an [`uri`](../api/API_PutIntegration.md#apigw-PutIntegration-request-uri "../api/API_PutIntegration.md#apigw-PutIntegration-request-uri")
that contains a secure server name, such as `https://example.com:443/test`. For a complete tutorial on how to create
a REST API with a private integration, see [Tutorial: Create a REST API with a private integration](getting-started-with-private-integration.md "getting-started-with-private-integration.md").

## Create a private integration

The following procedure shows how to create a private integration that connects to a load balancer by
using a VPC link V2.

AWS Management Console
For a tutorial on how to create a private integration see,
[Tutorial: Create a REST API with a private integration](getting-started-with-private-integration.md "getting-started-with-private-integration.md").

AWS CLIThe following [put-integration](../../../cli/latest/reference/latest/api/API_PutIntegration.md "../../../cli/latest/reference/latest/api/API_PutIntegration.md")
command creates a private integration that connects to a load balancer by using a VPC link V2:

```
aws apigateway put-integration \
    --rest-api-id abcdef123 \
    --resource-id aaa000 \
    --integration-target 'arn:aws:elasticloadbalancing:us-east-2:111122223333:loadbalancer/app/myLoadBalancerName/1234567891011' \
    --uri 'https://example.com:443/path' \
    --http-method GET \
    --type HTTP_PROXY \
    --integration-http-method GET \
    --connection-type VPC_LINK \
    --connection-id bbb111
```

Instead of directly providing the connection ID, you can use a stage variable instead. When you deploy
your API to a stage, you set the VPC link V2 ID. The following [put-integration](../../../cli/latest/reference/latest/api/API_PutIntegration.md "../../../cli/latest/reference/latest/api/API_PutIntegration.md") command creates a private
integration using a stage variable for the VPC link V2 ID:

```
aws apigateway put-integration \
    --rest-api-id abcdef123 \
    --resource-id aaa000 \
    --integration-target 'arn:aws:elasticloadbalancing:us-east-2:111122223333:loadbalancer/app/myLoadBalancerName/1234567891011' \
    --uri 'https://example.com:443/path' \
    --http-method GET \
    --type HTTP_PROXY \
    --integration-http-method GET \
    --connection-type VPC_LINK \
    --connection-id "\${stageVariables.vpcLinkV2Id}"
```

Make sure to double-quote the stage variable expression (${stageVariables.vpcLinkV2Id}) and escape the $ character.

OpenAPIYou can set up an API with the private integration by importing the API's
OpenAPI file. The settings are similar to the OpenAPI definitions of an API with HTTP
integrations, with the following exceptions:

- You must explicitly set `connectionType` to
  `VPC_LINK`.
- You must explicitly set `connectionId` to the ID of a
  `VpcLinkV2` or to a stage variable referencing the ID of a
  `VpcLinkV2`.
- The `uri` parameter in the private integration points to an
  HTTP/HTTPS endpoint in the VPC, but is used instead to set up the integration
  request's `Host` header.
- The `uri` parameter in the private integration with an HTTPS
  endpoint in the VPC is used to verify the stated domain name against the one in
  the certificate installed on the VPC endpoint.

You can use a stage variable to reference the `VpcLinkV2` ID.
Or you can assign the ID value directly to `connectionId`.

The following JSON-formatted OpenAPI file shows an example of an API with a VPC link
as referenced by a stage variable (`${stageVariables.vpcLinkIdV2}`):

```
{
  "swagger": "2.0",
  "info": {
    "version": "2017-11-17T04:40:23Z",
    "title": "MyApiWithVpcLinkV2"
  },
  "host": "abcdef123.execute-api.us-west-2.amazonaws.com",
  "basePath": "/test",
  "schemes": [
    "https"
  ],
  "paths": {
    "/": {
      "get": {
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "200 response",
            "schema": {
              "$ref": "#/definitions/Empty"
            }
          }
        },
        "x-amazon-apigateway-integration": {
          "responses": {
            "default": {
              "statusCode": "200"
            }
          },
          "uri": "https://example.com:443/path",
          "passthroughBehavior": "when_no_match",
          "connectionType": "VPC_LINK",
          "connectionId": "${stageVariables.vpcLinkV2Id}",
          "integration-target": "arn:aws:elasticloadbalancing:us-east-2:111122223333:loadbalancer/app/myLoadBalancerName/1234567891011",
          "httpMethod": "GET",
          "type": "http_proxy"
        }
      }
    }
  },
  "definitions": {
    "Empty": {
      "type": "object",
      "title": "Empty Schema"
    }
  }
}
```

## Update a private integration

The following example updates the VPC link V2 for a private integration.

AWS Management Console ###### To update a private integration

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose a REST API with a private integration.
3. Choose the resource and method that uses a private integration.
4. On the **Integration request tab**, under the **Integration request settings**, choose
   **Edit**.
5. You can edit the setting of your private integration. If you are currently using a VPC link V1,
   you can change your VPC link to a VPC link V2.
6. Choose **Save**.
7. Redeploy your API for the changes to take effect.

AWS CLI
The following [update-integration](../../../cli/latest/reference/latest/api/API_PutIntegration.md "../../../cli/latest/reference/latest/api/API_PutIntegration.md")
command updates a private integration to use a VPC link V2:

```
aws apigateway update-integration \
    --rest-api-id a1b2c3d4e5 \
    --resource-id a1b2c3 \
    --http-method GET \
    --patch-operations "[{\"op\":\"replace\",\"path\":\"/connectionId\",\"value\":\"pk0000\"}, {\"op\":\"replace\",\"path\":\"/uri\",\"value\":\"http://example.com\"}, {\"op\":\"replace\",\"path\":\"/integrationTarget\",\"value\":\"arn:aws:elasticloadbalancing:us-east-2:111122223333:loadbalancer/app/myLoadBalancerName/1234567891011\"}]"
```
