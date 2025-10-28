# API Gateway Amazon Resource Name (ARN)

reference

The following tables list the Amazon Resource Names (ARNs) for API Gateway resources. To learn
more about using ARNs in AWS Identity and Access Management policies, see [How Amazon API Gateway works with
IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md") and
[Control access to a REST API with IAM permissions](permissions.md "permissions.md").

## HTTP API and WebSocket API resources

| Resource                          | ARN                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AccessLogSettings                 | `arn:`partition`:apigateway:`region`::/apis/`api-id`/stages/`stage-name`/accesslogsettings`                                                 |
| Api                               | `arn:`partition`:apigateway:`region`::/apis/`api-id``                                                                                       |
| Apis                              | `arn:`partition`:apigateway:`region`::/apis`                                                                                                |
| Authorizer                        | `arn:`partition`:apigateway:`region`::/apis/`api-id`/authorizers/`id``                                                                      |
| Authorizers                       | `arn:`partition`:apigateway:`region`::/apis/`api-id`/authorizers`                                                                           |
| Cors                              | `arn:`partition`:apigateway:`region`::/apis/`api-id`/cors`                                                                                  |
| Deployment                        | `arn:`partition`:apigateway:`region`::/apis/`api-id`/deployments/`id``                                                                      |
| Deployments                       | `arn:`partition`:apigateway:`region`::/apis/`api-id`/deployments`                                                                           |
| ExportedAPI                       | `arn:`partition`:apigateway:`region`::/apis/`api-id`/exports/`specification``                                                               |
| Integration                       | `arn:`partition`:apigateway:`region`::/apis/`api-id`/integrations/`integration-id``                                                         |
| Integrations                      | `arn:`partition`:apigateway:`region`::/apis/`api-id`/integrations`                                                                          |
| IntegrationResponse               | `arn:`partition`:apigateway:`region`::/apis/`api-id`/integrationresponses/`integration-response``                                           |
| IntegrationResponses              | `arn:`partition`:apigateway:`region`::/apis/`api-id`/integrationresponses`                                                                  |
| Model                             | `arn:`partition`:apigateway:`region`::/apis/`api-id`/models/`id``                                                                           |
| Models                            | `arn:`partition`:apigateway:`region`::/apis/`api-id`/models`                                                                                |
| ModelTemplate                     | `arn:`partition`:apigateway:`region`::/apis/`api-id`/models/`id`/template`                                                                  |
| Route                             | `arn:`partition`:apigateway:`region`::/apis/`api-id`/routes/`id``                                                                           |
| Routes                            | `arn:`partition`:apigateway:`region`::/apis/`api-id`/routes`                                                                                |
| RouteRequestParameter             | `arn:`partition`:apigateway:`region`::/apis/`api-id`/routes/`id`/requestparameters/`key``                                                   |
| RouteResponse                     | `arn:`partition`:apigateway:`region`::/apis/`api-id`/routes/`id`/routeresponses/`id``                                                       |
| RouteResponses                    | `arn:`partition`:apigateway:`region`::/apis/`api-id`/routes/`id`/routeresponses`                                                            |
| RouteSettings                     | `arn:`partition`:apigateway:`region`::/apis/`api-id`/stages/`stage-name`/routesettings/`route-key``                                         |
| Stage                             | `arn:`partition`:apigateway:`region`::/apis/`api-id`/stages/`stage-name``                                                                   |
| Stages                            | `arn:`partition`:apigateway:`region`::/apis/`api-id`/stages`                                                                                |
| VpcLink                           | `arn:`partition`:apigateway:`region`::/vpclinks/`vpclink-id``                                                                               |
| VpcLinks                          | `arn:`partition`:apigateway:`region`::/vpclinks`                                                                                            | ## REST API resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Resource                          | ARN                                                                                                                                         |
| ---                               | ---                                                                                                                                         |
| Account                           | `arn:`partition`:apigateway:`region`::/account`                                                                                             |
| ApiKey                            | `arn:`partition`:apigateway:`region`::/apikeys/`id``                                                                                        |
| ApiKeys                           | `arn:`partition`:apigateway:`region`::/apikeys`                                                                                             |
| Authorizer                        | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/authorizers/`id``                                                                  |
| Authorizers                       | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/authorizers`                                                                       |
| ClientCertificate                 | `arn:`partition`:apigateway:`region`::/clientcertificates/`id``                                                                             |
| ClientCertificates                | `arn:`partition`:apigateway:`region`::/clientcertificates`                                                                                  |
| Deployment                        | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/deployments/`id``                                                                  |
| Deployments                       | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/deployments`                                                                       |
| DocumentationPart                 | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/documentation/parts/`id``                                                          |
| DocumentationParts                | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/documentation/parts`                                                               |
| DocumentationVersion              | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/documentation/versions/`version``                                                  |
| DocumentationVersions             | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/documentation/versions`                                                            |
| GatewayResponse                   | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/gatewayresponses/`response-type``                                                  |
| GatewayResponses                  | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/gatewayresponses`                                                                  |
| Integration                       | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/resources/`resource-id`/methods/`http-method`/integration`                         |
| IntegrationResponse               | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/resources/`resource-id`/methods/`http-method`/integration/responses/`status-code`` |
| Method                            | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/resources/`resource-id`/methods/`http-method``                                     |
| MethodResponse                    | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/resources/`resource-id`/methods/`http-method`/responses/`status-code``             |
| Model                             | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/models/`model-name``                                                               |
| Models                            | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/models`                                                                            |
| RequestValidator                  | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/requestvalidators/`id``                                                            |
| RequestValidators                 | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/requestvalidators`                                                                 |
| Resource                          | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/resources/`id``                                                                    |
| Resources                         | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/resources`                                                                         |
| RestApi                           | `arn:`partition`:apigateway:`region`::/restapis/`api-id``                                                                                   |
| RestApis                          | `arn:`partition`:apigateway:`region`::/restapis`                                                                                            |
| Stage                             | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/stages/`stage-name``                                                               |
| Stages                            | `arn:`partition`:apigateway:`region`::/restapis/`api-id`/stages`                                                                            |
| Tags                              | `arn:`partition`:apigateway:`region`::/tags/`url-encoded-resource-arn``                                                                     |
| Template                          | `arn:`partition`:apigateway:`region`::/restapis/models/`model-name`/template`                                                               |
| UsagePlan                         | `arn:`partition`:apigateway:`region`::/usageplans/`usageplan-id``                                                                           |
| UsagePlans                        | `arn:`partition`:apigateway:`region`::/usageplans`                                                                                          |
| UsagePlanKey                      | `arn:`partition`:apigateway:`region`::/usageplans/`usageplan-id`/keys/`id``                                                                 |
| UsagePlanKeys                     | `arn:`partition`:apigateway:`region`::/usageplans/`usageplan-id`/keys`                                                                      |
| VpcLink                           | `arn:`partition`:apigateway:`region`::/vpclinks/`vpclink-id``                                                                               |
| VpcLinks                          | `arn:`partition`:apigateway:`region`::/vpclinks`                                                                                            | ## Domain names resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Resource                          | ARN                                                                                                                                         |
| ---                               | ---                                                                                                                                         |
| ApiMapping                        | `arn:`partition`:apigateway:`region`::/domainnames/`domain-name`/apimappings/`id``                                                          |
| ApiMappings                       | `arn:`partition`:apigateway:`region`::/domainnames/`domain-name`/apimappings`                                                               |
| BasePathMapping                   | `arn:`partition`:apigateway:`region`::/domainnames/`domain-name`/basepathmappings/`basepath``                                               |
| BasePathMappings                  | `arn:`partition`:apigateway:`region`::/domainnames/`domain-name`/basepathmappings`                                                          |
| DomainName                        | `arn:`partition`:apigateway:`region`::/domainnames/`domain-name``                                                                           |
| DomainNameAccessAssociation       | `arn:`partition`:apigateway:`region`:`account-id`:/domainnameaccessassociations/domainname/`domain-name`/vpcesource/`vpce-source-id``       |
| DomainNameAccessAssociations      | `arn:`partition`:apigateway:`region`:`account-id`:/domainnameaccessassociations`                                                            |
| DomainNames                       | `arn:`partition`:apigateway:`region`::/domainnames`                                                                                         |
| RoutingRule                       | `arn:`partition`:apigateway:`region`:`account-id`:/domainnames/`domain-name`/routingrules/`routing-rule-id``                                | ## `execute-api` (HTTP APIs, WebSocket APIs, and REST APIs)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Resource                          | ARN                                                                                                                                         |
| ---                               | ---                                                                                                                                         |
| WebSocket API endpoint            | `arn:`partition`:execute-api:`region`:`account-id`:`api-id`/`stage`/`route-key``                                                            |
| HTTP API and REST API endpoint \* | `arn:`partition`:execute-api:`region`:`account-id`:`api-id`/`stage`/`http-method`/`resource-path``                                          |
| Lambda authorizer \*\*            | `arn:`partition`:execute-api:`region`:`account-id`:`api-id`/authorizers/`authorizer-id``                                                    | \* The ARN for the `$default` route endpoint for HTTP APIs is `arn:`partition`:execute-api:`region`:`account-id`:`api-id`/`\*`/$default`. \*\* This ARN is applicable only when setting the `SourceArn` condition in the [resource policy](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") for a Lambda authorizer function. For an example, see [Create a Lambda authorizer](http-api-lambda-authorizer.md#http-api-lambda-authorizer.example-create "http-api-lambda-authorizer.md#http-api-lambda-authorizer.example-create"). |
