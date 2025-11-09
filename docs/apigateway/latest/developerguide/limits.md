# Amazon API Gateway quotas

The following quotas apply for all Amazon API Gateway API types.

## API Gateway account-level quotas, per Region

The following quotas apply per account, per Region in Amazon API Gateway.

| Resource or operation                                                                                              | Default quota                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Can be increased                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Throttle quota per account, per Region across HTTP APIs, REST APIs, WebSocket APIs, and WebSocket<br>callback APIs | 10,000 requests per second (RPS) with an additional burst capacity provided by the [token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket "https://en.wikipedia.org/wiki/Token_bucket"), using a maximum bucket<br>capacity of 5,000 requests. \*NoteThe burst quota is determined by the API Gateway service team based on the overall RPS quota for the<br>account in the Region. It is not a quota that a customer can control or request changes to. | [Yes](https://console.aws.amazon.com/servicequotas/home/services/apigateway/quotas/L-8A5B8E43 "https://console.aws.amazon.com/servicequotas/home/services/apigateway/quotas/L-8A5B8E43") |

\* For the following Regions, the default throttle quota is 2500 RPS and the default burst quota is 1250 RPS:
Africa (Cape Town), Europe (Milan), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad),
Asia Pacific (Melbourne), Europe (Spain), Europe (Zurich), Israel (Tel Aviv),
Canada West (Calgary), Asia Pacific (Malaysia), Asia Pacific (Thailand), and Mexico (Central).

## API Gateway quotas for creating,

deploying and managing an API

The following fixed quotas apply to creating, deploying, and managing an API in API Gateway,
using the AWS CLI, the API Gateway console, or the API Gateway REST API and its SDKs. These quotas can't
be increased.

| Action                                                                                                                                                            | Default quota                                                        | Can be increased |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------- |
| [CreateApiKey](../api/API_CreateApiKey.md "../api/API_CreateApiKey.md")                                                                                           | 5 requests per second per account                                    | No               |
| [CreateDeployment](../api/API_CreateDeployment.md "../api/API_CreateDeployment.md")                                                                               | 1 request every 5 seconds per account                                | No               |
| [CreateDocumentationVersion](../api/API_CreateDocumentationVersion.md "../api/API_CreateDocumentationVersion.md")                                                 | 1 request every 20 seconds per account                               | No               |
| [CreateDomainName](../api/API_CreateDomainName.md "../api/API_CreateDomainName.md")                                                                               | 1 request every 30 seconds per account                               | No               |
| [CreateResource](../api/API_CreateResource.md "../api/API_CreateResource.md")                                                                                     | 5 requests per second per account                                    | No               |
| [CreateRestApi](../api/API_CreateRestApi.md "../api/API_CreateRestApi.md") for Regional or private API                                                            | 1 request every 3 seconds per account                                | No               |
| [CreateRestApi](../api/API_CreateRestApi.md "../api/API_CreateRestApi.md") for edge-optimized API                                                                 | 1 request every 30 seconds per account                               | No               |
| [CreateVpcLink](../../../apigatewayv2/latest/api-reference/vpclinks.md#CreateVpcLink "../../../apigatewayv2/latest/api-reference/vpclinks.md#CreateVpcLink") (V2) | 1 request every 15 seconds per account                               | No               |
| [DeleteApiKey](../api/API_DeleteApiKey.md "../api/API_DeleteApiKey.md")                                                                                           | 5 requests per second per account                                    | No               |
| [DeleteDomainName](../api/API_DeleteDomainName.md "../api/API_DeleteDomainName.md")                                                                               | 1 request every 30 seconds per account                               | No               |
| [DeleteResource](../api/API_DeleteResource.md "../api/API_DeleteResource.md")                                                                                     | 5 requests per second per account                                    | No               |
| [DeleteRestApi](../api/API_DeleteRestApi.md "../api/API_DeleteRestApi.md")                                                                                        | 1 request every 30 seconds per account                               | No               |
| [GetResources](../api/API_GetResources.md "../api/API_GetResources.md")                                                                                           | 5 requests every 2 seconds per account                               | No               |
| [DeleteVpcLink](../../../apigatewayv2/latest/api-reference/vpclinks.md#DeleteVpcLink "../../../apigatewayv2/latest/api-reference/vpclinks.md#DeleteVpcLink") (V2) | 1 request every 30 seconds per account                               | No               |
| [ImportDocumentationParts](../api/API_ImportDocumentationParts.md "../api/API_ImportDocumentationParts.md")                                                       | 1 request every 30 seconds per account                               | No               |
| [ImportRestApi](../api/API_ImportRestApi.md "../api/API_ImportRestApi.md") for Regional or private API                                                            | 1 request every 3 seconds per account                                | No               |
| [ImportRestApi](../api/API_ImportRestApi.md "../api/API_ImportRestApi.md") for edge-optimized API                                                                 | 1 request every 30 seconds per account                               | No               |
| [PutRestApi](../api/API_PutRestApi.md "../api/API_PutRestApi.md")                                                                                                 | 1 request per second per account                                     | No               |
| [UpdateAccount](../api/API_UpdateAccount.md "../api/API_UpdateAccount.md")                                                                                        | 1 request every 20 seconds per account                               | No               |
| [UpdateDomainName](../api/API_UpdateDomainName.md "../api/API_UpdateDomainName.md")                                                                               | 1 request every 30 seconds per account                               | No               |
| [UpdateUsagePlan](../api/API_UpdateUsagePlan.md "../api/API_UpdateUsagePlan.md")                                                                                  | 1 request every 20 seconds per account                               | No               |
| Other operations                                                                                                                                                  | No quota up to the total account quota.                              | No               |
| Total operations                                                                                                                                                  | 10 requests per second with a burst quota of 40 requests per second. | No               |
