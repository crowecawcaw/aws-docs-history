

# Actions, resources, and condition keys for Amazon API Gateway Management V2
<a name="list_apigatewayv2"></a>

Amazon API Gateway Management V2 (service prefix: `apigateway`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/apigateway/apigateway.json) for this service.

**Topics**
+ [API operations defined by Amazon API Gateway Management V2](#list_apigatewayv2-operations)
+ [Actions defined by Amazon API Gateway Management V2](#list_apigatewayv2-actions-as-permissions)
+ [Resource types defined by Amazon API Gateway Management V2](#list_apigatewayv2-resources-for-iam-policies)
+ [Condition keys for Amazon API Gateway Management V2](#list_apigatewayv2-policy-keys)

## API operations defined by Amazon API Gateway Management V2
<a name="list_apigatewayv2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_apigatewayv2-actions-as-permissions).




- **   CreateApi  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   CreateApiMapping  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAuthorizer  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   CreateDeployment  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomainName  **
  - **IAM action:**  [apigateway:AddCertificateToDomain](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigatewayv2-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:UpdateDomainNamePolicy](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateIntegration  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   CreateIntegrationResponse  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateModel  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePortal  **
  - **IAM action:**  [apigateway:CreatePortal](#list_apigatewayv2-action-CreatePortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:GetPortalProduct](#list_apigatewayv2-action-GetPortalProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreatePortalProduct  **
  - **IAM action:**  [apigateway:CreatePortalProduct](#list_apigatewayv2-action-CreatePortalProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateProductPage  **
  - **IAM action:**  [apigateway:CreateProductPage](#list_apigatewayv2-action-CreateProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProductRestEndpointPage  **
  - **IAM action:**  [apigateway:CreateProductRestEndpointPage](#list_apigatewayv2-action-CreateProductRestEndpointPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRoute  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRouteResponse  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRoutingRule  **
  - **IAM action:**  [apigateway:CreateRoutingRule](#list_apigatewayv2-action-CreateRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStage  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigatewayv2-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateVpcLink  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigatewayv2-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAccessLogSettings  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApi  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApiMapping  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAuthorizer  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCorsConfiguration  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeployment  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainName  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:RemoveCertificateFromDomain](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DeleteIntegration  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegrationResponse  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModel  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortal  **
  - **IAM action:**  [apigateway:DeletePortal](#list_apigatewayv2-action-DeletePortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortalProduct  **
  - **IAM action:**  [apigateway:DeletePortalProduct](#list_apigatewayv2-action-DeletePortalProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortalProductSharingPolicy  **
  - **IAM action:**  [apigateway:DeletePortalProductSharingPolicy](#list_apigatewayv2-action-DeletePortalProductSharingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteProductPage  **
  - **IAM action:**  [apigateway:DeleteProductPage](#list_apigatewayv2-action-DeleteProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProductRestEndpointPage  **
  - **IAM action:**  [apigateway:DeleteProductRestEndpointPage](#list_apigatewayv2-action-DeleteProductRestEndpointPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoute  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRouteRequestParameter  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRouteResponse  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRouteSettings  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoutingRule  **
  - **IAM action:**  [apigateway:DeleteRoutingRule](#list_apigatewayv2-action-DeleteRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStage  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcLink  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisablePortal  **
  - **IAM action:**  [apigateway:DisablePortal](#list_apigatewayv2-action-DisablePortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportApi  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApi  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiMapping  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiMappings  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApis  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAuthorizer  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAuthorizers  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployment  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployments  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainName  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainNames  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegration  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegrationResponse  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegrationResponses  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegrations  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModel  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModelTemplate  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModels  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPortal  **
  - **IAM action:**  [apigateway:GetPortal](#list_apigatewayv2-action-GetPortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPortalProduct  **
  - **IAM action:**  [apigateway:GetPortalProduct](#list_apigatewayv2-action-GetPortalProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPortalProductSharingPolicy  **
  - **IAM action:**  [apigateway:GetPortalProductSharingPolicy](#list_apigatewayv2-action-GetPortalProductSharingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProductPage  **
  - **IAM action:**  [apigateway:GetProductPage](#list_apigatewayv2-action-GetProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProductRestEndpointPage  **
  - **IAM action:**  [apigateway:GetProductRestEndpointPage](#list_apigatewayv2-action-GetProductRestEndpointPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRoute  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouteResponse  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRouteResponses  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRoutes  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRoutingRule  **
  - **IAM action:**  [apigateway:GetRoutingRule](#list_apigatewayv2-action-GetRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStage  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStages  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTags  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcLink  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcLinks  **
  - **IAM action:**  [apigateway:GET](#list_apigatewayv2-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportApi  **
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigatewayv2-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   ListPortalProducts  **
  - **IAM action:**  [apigateway:ListPortalProducts](#list_apigatewayv2-action-ListPortalProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPortals  **
  - **IAM action:**  [apigateway:ListPortals](#list_apigatewayv2-action-ListPortals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProductPages  **
  - **IAM action:**  [apigateway:ListProductPages](#list_apigatewayv2-action-ListProductPages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProductRestEndpointPages  **
  - **IAM action:**  [apigateway:ListProductRestEndpointPages](#list_apigatewayv2-action-ListProductRestEndpointPages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoutingRules  **
  - **IAM action:**  [apigateway:ListRoutingRules](#list_apigatewayv2-action-ListRoutingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PreviewPortal  **
  - **IAM action:**  [apigateway:GetPortalProduct](#list_apigatewayv2-action-GetPortalProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apigateway:PreviewPortal](#list_apigatewayv2-action-PreviewPortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PublishPortal  **
  - **IAM action:**  [apigateway:GetPortalProduct](#list_apigatewayv2-action-GetPortalProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apigateway:PublishPortal](#list_apigatewayv2-action-PublishPortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutPortalProductSharingPolicy  **
  - **IAM action:**  [apigateway:PutPortalProductSharingPolicy](#list_apigatewayv2-action-PutPortalProductSharingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutRoutingRule  **
  - **IAM action:**  [apigateway:UpdateRoutingRule](#list_apigatewayv2-action-UpdateRoutingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReimportApi  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigatewayv2-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   ResetAuthorizersCache  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:POST](#list_apigatewayv2-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigatewayv2-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [apigateway:DELETE](#list_apigatewayv2-action-DELETE)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateApi  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   UpdateApiMapping  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAuthorizer  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   UpdateDeployment  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainName  **
  - **IAM action:**  [apigateway:AddCertificateToDomain](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:RemoveCertificateFromDomain](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:UpdateDomainNameManagementPolicy](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:UpdateDomainNamePolicy](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   UpdateIntegration  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   UpdateIntegrationResponse  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModel  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePortal  **
  - **IAM action:**  [apigateway:GetPortalProduct](#list_apigatewayv2-action-GetPortalProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apigateway:UpdatePortal](#list_apigatewayv2-action-UpdatePortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdatePortalProduct  **
  - **IAM action:**  [apigateway:UpdatePortalProduct](#list_apigatewayv2-action-UpdatePortalProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProductPage  **
  - **IAM action:**  [apigateway:UpdateProductPage](#list_apigatewayv2-action-UpdateProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProductRestEndpointPage  **
  - **IAM action:**  [apigateway:UpdateProductRestEndpointPage](#list_apigatewayv2-action-UpdateProductRestEndpointPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoute  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRouteResponse  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStage  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcLink  **
  - **IAM action:**  [apigateway:PATCH](#list_apigatewayv2-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon API Gateway Management V2
<a name="list_apigatewayv2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreatePortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals.html#portalspost)  **
  - **Description:** Grants permission to create a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Request/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Request_CognitoUserPoolArn)<br />[apigateway:Request/PortalDisplayName](#list_apigatewayv2-apigateway_Request_PortalDisplayName)<br />[apigateway:Request/PortalDomainName](#list_apigatewayv2-apigateway_Request_PortalDomainName)<br />[apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePortalProduct](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts.html#portalproductspost)  **
  - **Description:** Grants permission to create a Portal Product
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Request/PortalProductDisplayName](#list_apigatewayv2-apigateway_Request_PortalProductDisplayName)<br />[apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProductPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages.html#portalproducts-portalproductid-productpagespost)  **
  - **Description:** Grants permission to create a Product Page
  - **Resource types (\*required):** [ProductPage\*](#list_apigatewayv2-resource-ProductPage)
  - **Condition keys:** [apigateway:Request/ProductPageTitle](#list_apigatewayv2-apigateway_Request_ProductPageTitle)<br />[apigateway:Resource/ProductPageTitle](#list_apigatewayv2-apigateway_Resource_ProductPageTitle)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProductRestEndpointPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages.html#portalproducts-portalproductid-productrestendpointpagespost)  **
  - **Description:** Grants permission to create a Product REST Endpoint Page
  - **Resource types (\*required):** [ProductRestEndpointPage\*](#list_apigatewayv2-resource-ProductRestEndpointPage)
  - **Condition keys:** [apigateway:Request/Method](#list_apigatewayv2-apigateway_Request_Method)<br />[apigateway:Request/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Request_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Request/RestApiId](#list_apigatewayv2-apigateway_Request_RestApiId)<br />[apigateway:Request/Stage](#list_apigatewayv2-apigateway_Request_Stage)<br />[apigateway:Resource/Method](#list_apigatewayv2-apigateway_Resource_Method)<br />[apigateway:Resource/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Resource_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/RestApiId](#list_apigatewayv2-apigateway_Resource_RestApiId)<br />[apigateway:Resource/Stage](#list_apigatewayv2-apigateway_Resource_Stage)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRoutingRule](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules.html#domainnames-domainname-routingrulespost)  **
  - **Description:** Grants permission to create a routing rule
  - **Resource types (\*required):** [RoutingRule\*](#list_apigatewayv2-resource-RoutingRule)
  - **Condition keys:** [apigateway:Request/ConditionBasePaths](#list_apigatewayv2-apigateway_Request_ConditionBasePaths)<br />[apigateway:Request/Priority](#list_apigatewayv2-apigateway_Request_Priority)<br />[apigateway:Resource/ConditionBasePaths](#list_apigatewayv2-apigateway_Resource_ConditionBasePaths)<br />[apigateway:Resource/Priority](#list_apigatewayv2-apigateway_Resource_Priority)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DELETE](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html)  **
  - **Description:** Grants permission to delete a particular resource
  - **Resource types (\*required):** [AccessLogSettings](#list_apigatewayv2-resource-AccessLogSettings) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Api](#list_apigatewayv2-resource-Api) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigatewayv2-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigatewayv2-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [ApiMapping](#list_apigatewayv2-resource-ApiMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Authorizer](#list_apigatewayv2-resource-Authorizer) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [AuthorizersCache](#list_apigatewayv2-resource-AuthorizersCache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Cors](#list_apigatewayv2-resource-Cors) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Deployment](#list_apigatewayv2-resource-Deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Integration](#list_apigatewayv2-resource-Integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigatewayv2-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Model](#list_apigatewayv2-resource-Model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Route](#list_apigatewayv2-resource-Route) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [RouteRequestParameter](#list_apigatewayv2-resource-RouteRequestParameter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [RouteResponse](#list_apigatewayv2-resource-RouteResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [RouteSettings](#list_apigatewayv2-resource-RouteSettings) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_apigatewayv2-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigatewayv2-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigatewayv2-apigateway_Resource_AccessLoggingFormat)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [VpcLink](#list_apigatewayv2-resource-VpcLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [DeletePortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid.html#portals-portaliddelete)  **
  - **Description:** Grants permission to delete a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePortalProduct](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid.html#portalproducts-portalproductiddelete)  **
  - **Description:** Grants permission to delete a Portal Product
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePortalProductSharingPolicy](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-sharingpolicy.html#portalproducts-portalproductid-sharingpolicydelete)  **
  - **Description:** Grants permission to delete a Portal Product Sharing Policy
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteProductPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages-productpageid.html#portalproducts-portalproductid-productpages-productpageiddelete)  **
  - **Description:** Grants permission to delete a Product Page
  - **Resource types (\*required):** [ProductPage\*](#list_apigatewayv2-resource-ProductPage)
  - **Condition keys:** [apigateway:Resource/ProductPageTitle](#list_apigatewayv2-apigateway_Resource_ProductPageTitle)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProductRestEndpointPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.html#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageiddelete)  **
  - **Description:** Grants permission to delete a Product REST Endpoint Page
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct) / **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductRestEndpointPage\*](#list_apigatewayv2-resource-ProductRestEndpointPage) / **Condition keys:** [apigateway:Resource/Method](#list_apigatewayv2-apigateway_Resource_Method)<br />[apigateway:Resource/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Resource_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/RestApiId](#list_apigatewayv2-apigateway_Resource_RestApiId)<br />[apigateway:Resource/Stage](#list_apigatewayv2-apigateway_Resource_Stage)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRoutingRule](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules-routingruleid.html#domainnames-domainname-routingrules-routingruleiddelete)  **
  - **Description:** Grants permission to delete a routing rule
  - **Resource types (\*required):** [RoutingRule\*](#list_apigatewayv2-resource-RoutingRule)
  - **Condition keys:** [apigateway:Resource/ConditionBasePaths](#list_apigatewayv2-apigateway_Resource_ConditionBasePaths)<br />[apigateway:Resource/Priority](#list_apigatewayv2-apigateway_Resource_Priority)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisablePortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid-publish.html#portals-portalid-publishdelete)  **
  - **Description:** Grants permission to disable a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GET](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html)  **
  - **Description:** Grants permission to read a particular resource
  - **Resource types (\*required):** [AccessLogSettings](#list_apigatewayv2-resource-AccessLogSettings) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Api](#list_apigatewayv2-resource-Api) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigatewayv2-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigatewayv2-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ApiMapping](#list_apigatewayv2-resource-ApiMapping) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ApiMappings](#list_apigatewayv2-resource-ApiMappings) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Apis](#list_apigatewayv2-resource-Apis) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Authorizer](#list_apigatewayv2-resource-Authorizer) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Authorizers](#list_apigatewayv2-resource-Authorizers) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AuthorizersCache](#list_apigatewayv2-resource-AuthorizersCache) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Cors](#list_apigatewayv2-resource-Cors) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Deployment](#list_apigatewayv2-resource-Deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Deployments](#list_apigatewayv2-resource-Deployments) / **Condition keys:** [apigateway:Request/StageName](#list_apigatewayv2-apigateway_Request_StageName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ExportedAPI](#list_apigatewayv2-resource-ExportedAPI) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration](#list_apigatewayv2-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigatewayv2-resource-IntegrationResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [IntegrationResponses](#list_apigatewayv2-resource-IntegrationResponses) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integrations](#list_apigatewayv2-resource-Integrations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Model](#list_apigatewayv2-resource-Model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ModelTemplate](#list_apigatewayv2-resource-ModelTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Models](#list_apigatewayv2-resource-Models) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Route](#list_apigatewayv2-resource-Route) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RouteRequestParameter](#list_apigatewayv2-resource-RouteRequestParameter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RouteResponse](#list_apigatewayv2-resource-RouteResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RouteResponses](#list_apigatewayv2-resource-RouteResponses) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RouteSettings](#list_apigatewayv2-resource-RouteSettings) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Routes](#list_apigatewayv2-resource-Routes) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stage](#list_apigatewayv2-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigatewayv2-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigatewayv2-apigateway_Resource_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stages](#list_apigatewayv2-resource-Stages) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VpcLink](#list_apigatewayv2-resource-VpcLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VpcLinks](#list_apigatewayv2-resource-VpcLinks) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid.html#portals-portalidget)  **
  - **Description:** Grants permission to read a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPortalProduct](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid.html#portalproducts-portalproductidget)  **
  - **Description:** Grants permission to read a Portal Product
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPortalProductSharingPolicy](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-sharingpolicy.html#portalproducts-portalproductid-sharingpolicyget)  **
  - **Description:** Grants permission to read a Portal Product Sharing Policy
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProductPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages-productpageid.html#portalproducts-portalproductid-productpages-productpageidget)  **
  - **Description:** Grants permission to read a Product Page
  - **Resource types (\*required):** [PortalProduct](#list_apigatewayv2-resource-PortalProduct) / **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductPage\*](#list_apigatewayv2-resource-ProductPage) / **Condition keys:** [apigateway:Resource/ProductPageTitle](#list_apigatewayv2-apigateway_Resource_ProductPageTitle)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProductRestEndpointPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.html#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageidget)  **
  - **Description:** Grants permission to read a Product REST Endpoint Page
  - **Resource types (\*required):** [PortalProduct](#list_apigatewayv2-resource-PortalProduct) / **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductRestEndpointPage\*](#list_apigatewayv2-resource-ProductRestEndpointPage) / **Condition keys:** [apigateway:Resource/Method](#list_apigatewayv2-apigateway_Resource_Method)<br />[apigateway:Resource/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Resource_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/RestApiId](#list_apigatewayv2-apigateway_Resource_RestApiId)<br />[apigateway:Resource/Stage](#list_apigatewayv2-apigateway_Resource_Stage)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRoutingRule](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules-routingruleid.html#domainnames-domainname-routingrules-routingruleidget)  **
  - **Description:** Grants permission to read a routing rule
  - **Resource types (\*required):** [RoutingRule\*](#list_apigatewayv2-resource-RoutingRule)
  - **Condition keys:** [apigateway:Resource/ConditionBasePaths](#list_apigatewayv2-apigateway_Resource_ConditionBasePaths)<br />[apigateway:Resource/Priority](#list_apigatewayv2-apigateway_Resource_Priority)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPortalProducts](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts.html#portalproductsget)  **
  - **Description:** Grants permission to list Portal Products
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPortals](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals.html#portalsget)  **
  - **Description:** Grants permission to list Portals
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProductPages](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages.html#portalproducts-portalproductid-productpagesget)  **
  - **Description:** Grants permission to list Product Pages
  - **Resource types (\*required):** [PortalProduct](#list_apigatewayv2-resource-PortalProduct) / **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductPage\*](#list_apigatewayv2-resource-ProductPage) / **Condition keys:** [apigateway:Resource/ProductPageTitle](#list_apigatewayv2-apigateway_Resource_ProductPageTitle)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProductRestEndpointPages](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages.html#portalproducts-portalproductid-productrestendpointpagesget)  **
  - **Description:** Grants permission to list Product REST Endpoint Pages
  - **Resource types (\*required):** [PortalProduct](#list_apigatewayv2-resource-PortalProduct) / **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductRestEndpointPage\*](#list_apigatewayv2-resource-ProductRestEndpointPage) / **Condition keys:** [apigateway:Resource/Method](#list_apigatewayv2-apigateway_Resource_Method)<br />[apigateway:Resource/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Resource_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/RestApiId](#list_apigatewayv2-apigateway_Resource_RestApiId)<br />[apigateway:Resource/Stage](#list_apigatewayv2-apigateway_Resource_Stage)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRoutingRules](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules.html#domainnames-domainname-routingrulesget)  **
  - **Description:** Grants permission to list routing rules under a domain name
  - **Resource types (\*required):** [RoutingRule\*](#list_apigatewayv2-resource-RoutingRule)
  - **Condition keys:** [apigateway:Resource/ConditionBasePaths](#list_apigatewayv2-apigateway_Resource_ConditionBasePaths)<br />[apigateway:Resource/Priority](#list_apigatewayv2-apigateway_Resource_Priority)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PATCH](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html)  **
  - **Description:** Grants permission to update a particular resource
  - **Resource types (\*required):** [Api](#list_apigatewayv2-resource-Api) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigatewayv2-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigatewayv2-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [ApiMapping](#list_apigatewayv2-resource-ApiMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Authorizer](#list_apigatewayv2-resource-Authorizer) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Deployment](#list_apigatewayv2-resource-Deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Integration](#list_apigatewayv2-resource-Integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigatewayv2-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Model](#list_apigatewayv2-resource-Model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Route](#list_apigatewayv2-resource-Route) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [RouteRequestParameter](#list_apigatewayv2-resource-RouteRequestParameter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [RouteResponse](#list_apigatewayv2-resource-RouteResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_apigatewayv2-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigatewayv2-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigatewayv2-apigateway_Resource_AccessLoggingFormat)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [VpcLink](#list_apigatewayv2-resource-VpcLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [POST](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html)  **
  - **Description:** Grants permission to create a particular resource
  - **Resource types (\*required):** [ApiMappings](#list_apigatewayv2-resource-ApiMappings) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Apis](#list_apigatewayv2-resource-Apis) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Authorizers](#list_apigatewayv2-resource-Authorizers) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Deployments](#list_apigatewayv2-resource-Deployments) / **Condition keys:** [apigateway:Request/StageName](#list_apigatewayv2-apigateway_Request_StageName)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigatewayv2-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponses](#list_apigatewayv2-resource-IntegrationResponses) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Integrations](#list_apigatewayv2-resource-Integrations) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Models](#list_apigatewayv2-resource-Models) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [RouteResponses](#list_apigatewayv2-resource-RouteResponses) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Routes](#list_apigatewayv2-resource-Routes) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Stages](#list_apigatewayv2-resource-Stages) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [VpcLinks](#list_apigatewayv2-resource-VpcLinks) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [PUT](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html)  **
  - **Description:** Grants permission to update a particular resource
  - **Resource types (\*required):** [Api](#list_apigatewayv2-resource-Api) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigatewayv2-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigatewayv2-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [Apis](#list_apigatewayv2-resource-Apis) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigatewayv2-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [PreviewPortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid-preview.html#portals-portalid-previewpost)  **
  - **Description:** Grants permission to preview a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PublishPortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid-publish.html#portals-portalid-publishpost)  **
  - **Description:** Grants permission to publish a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutPortalProductSharingPolicy](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-sharingpolicy.html#portalproducts-portalproductid-sharingpolicyput)  **
  - **Description:** Grants permission to put a Portal Product Sharing Policy
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdatePortal](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid.html#portals-portalidpatch)  **
  - **Description:** Grants permission to update a Portal
  - **Resource types (\*required):** [Portal\*](#list_apigatewayv2-resource-Portal)
  - **Condition keys:** [apigateway:Request/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Request_CognitoUserPoolArn)<br />[apigateway:Request/PortalDisplayName](#list_apigatewayv2-apigateway_Request_PortalDisplayName)<br />[apigateway:Request/PortalDomainName](#list_apigatewayv2-apigateway_Request_PortalDomainName)<br />[apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [UpdatePortalProduct](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid.html#portalproducts-portalproductidpatch)  **
  - **Description:** Grants permission to update a Portal Product
  - **Resource types (\*required):** [PortalProduct\*](#list_apigatewayv2-resource-PortalProduct)
  - **Condition keys:** [apigateway:Request/PortalProductDisplayName](#list_apigatewayv2-apigateway_Request_PortalProductDisplayName)<br />[apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:RequestTag/${TagKey}](#list_apigatewayv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigatewayv2-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateProductPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productpages-productpageid.html#portalproducts-portalproductid-productpages-productpageidpatch)  **
  - **Description:** Grants permission to update a Product Page
  - **Resource types (\*required):** [ProductPage\*](#list_apigatewayv2-resource-ProductPage)
  - **Condition keys:** [apigateway:Request/ProductPageTitle](#list_apigatewayv2-apigateway_Request_ProductPageTitle)<br />[apigateway:Resource/ProductPageTitle](#list_apigatewayv2-apigateway_Resource_ProductPageTitle)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProductRestEndpointPage](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-productrestendpointpages-productrestendpointpageid.html#portalproducts-portalproductid-productrestendpointpages-productrestendpointpageidpatch)  **
  - **Description:** Grants permission to update a Product REST Endpoint Page
  - **Resource types (\*required):** [ProductRestEndpointPage\*](#list_apigatewayv2-resource-ProductRestEndpointPage)
  - **Condition keys:** [apigateway:Request/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Request_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/Method](#list_apigatewayv2-apigateway_Resource_Method)<br />[apigateway:Resource/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Resource_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/RestApiId](#list_apigatewayv2-apigateway_Resource_RestApiId)<br />[apigateway:Resource/Stage](#list_apigatewayv2-apigateway_Resource_Stage)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRoutingRule](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules-routingruleid.html#domainnames-domainname-routingrules-routingruleidput)  **
  - **Description:** Grants permission to update a routing rule using the PutRoutingRule API
  - **Resource types (\*required):** [RoutingRule\*](#list_apigatewayv2-resource-RoutingRule)
  - **Condition keys:** [apigateway:Request/ConditionBasePaths](#list_apigatewayv2-apigateway_Request_ConditionBasePaths)<br />[apigateway:Request/Priority](#list_apigatewayv2-apigateway_Request_Priority)<br />[apigateway:Resource/ConditionBasePaths](#list_apigatewayv2-apigateway_Resource_ConditionBasePaths)<br />[apigateway:Resource/Priority](#list_apigatewayv2-apigateway_Resource_Priority)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon API Gateway Management V2
<a name="list_apigatewayv2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AccessLogSettings](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages/${StageName}/accesslogsettings | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Api](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId} | [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigatewayv2-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigatewayv2-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [ApiMapping](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}/apimappings/${ApiMappingId} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [ApiMappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}/apimappings | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Apis](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis | [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigatewayv2-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigatewayv2-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigatewayv2-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/authorizers/${AuthorizerId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/authorizers/${AuthorizerId} | [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[apigateway:Resource/AuthorizerType](#list_apigatewayv2-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/AuthorizerUri](#list_apigatewayv2-apigateway_Resource_AuthorizerUri)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/authorizers, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/authorizers | [apigateway:Request/AuthorizerType](#list_apigatewayv2-apigateway_Request_AuthorizerType)<br />[apigateway:Request/AuthorizerUri](#list_apigatewayv2-apigateway_Request_AuthorizerUri)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [AuthorizersCache](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages/${StageName}/cache/authorizers | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Cors](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/cors | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/deployments/${DeploymentId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/deployments/${DeploymentId} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Deployments](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/deployments, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/deployments | [apigateway:Request/StageName](#list_apigatewayv2-apigateway_Request_StageName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [ExportedAPI](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/exports/${Specification} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/integrations/${IntegrationId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId}/methods/${HttpMethodType}/integration | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [IntegrationResponse](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/integrations/${IntegrationId}/integrationresponses/${IntegrationResponseId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId}/methods/${HttpMethodType}/integration/responses/${StatusCode} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [IntegrationResponses](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/integrations/${IntegrationId}/integrationresponses | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/integrations | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Model](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/models/${ModelId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/models/${ModelName} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [ModelTemplate](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/models/${ModelId}/template | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Models](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/models, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/models | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Portal](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/portals/${PortalId} | [apigateway:Resource/CognitoUserPoolArn](#list_apigatewayv2-apigateway_Resource_CognitoUserPoolArn)<br />[apigateway:Resource/PortalDisplayName](#list_apigatewayv2-apigateway_Resource_PortalDisplayName)<br />[apigateway:Resource/PortalDomainName](#list_apigatewayv2-apigateway_Resource_PortalDomainName)<br />[apigateway:Resource/PortalPublishStatus](#list_apigatewayv2-apigateway_Resource_PortalPublishStatus)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [PortalProduct](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/portalproducts/${PortalProductId} | [apigateway:Resource/PortalProductDisplayName](#list_apigatewayv2-apigateway_Resource_PortalProductDisplayName)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [ProductPage](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/portalproducts/${PortalProductId}/productpages/${ProductPageId} | [apigateway:Resource/ProductPageTitle](#list_apigatewayv2-apigateway_Resource_ProductPageTitle)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [ProductRestEndpointPage](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/portalproducts/${PortalProductId}/productrestendpointpages/${ProductRestEndpointPageId} | [apigateway:Resource/Method](#list_apigatewayv2-apigateway_Resource_Method)<br />[apigateway:Resource/ProductRestEndpointPageEndpointPrefix](#list_apigatewayv2-apigateway_Resource_ProductRestEndpointPageEndpointPrefix)<br />[apigateway:Resource/RestApiId](#list_apigatewayv2-apigateway_Resource_RestApiId)<br />[apigateway:Resource/Stage](#list_apigatewayv2-apigateway_Resource_Stage)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Route](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/routes/${RouteId} | [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigatewayv2-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigatewayv2-apigateway_Resource_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [RouteRequestParameter](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/routes/${RouteId}/requestparameters/${RequestParameterKey} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [RouteResponse](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/routes/${RouteId}/routeresponses/${RouteResponseId} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [RouteResponses](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/routes/${RouteId}/routeresponses | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [RouteSettings](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages/${StageName}/routesettings/${RouteKey} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Routes](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/routes | [apigateway:Request/ApiKeyRequired](#list_apigatewayv2-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigatewayv2-apigateway_Request_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [RoutingRule](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/domainnames/${DomainName}/routingrules/${RoutingRuleId} | [apigateway:Resource/ConditionBasePaths](#list_apigatewayv2-apigateway_Resource_ConditionBasePaths)<br />[apigateway:Resource/Priority](#list_apigatewayv2-apigateway_Resource_Priority)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages/${StageName}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/stages/${StageName} | [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigatewayv2-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigatewayv2-apigateway_Resource_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [Stages](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/stages | [apigateway:Request/AccessLoggingDestination](#list_apigatewayv2-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigatewayv2-apigateway_Request_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [VpcLink](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/vpclinks/${VpcLinkId} | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 
|  [VpcLinks](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/vpclinks | [aws:ResourceTag/${TagKey}](#list_apigatewayv2-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon API Gateway Management V2
<a name="list_apigatewayv2-policy-keys"></a>

Amazon API Gateway Management V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [apigateway:Request/AccessLoggingDestination](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log destination. Available during the CreateStage and UpdateStage operations | String | 
|   [apigateway:Request/AccessLoggingFormat](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log format. Available during the CreateStage and UpdateStage operations | String | 
|   [apigateway:Request/ApiKeyRequired](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by the requirement of API. Available during the CreateRoute and UpdateRoute operations. Also available as a collection during import and reimport | ArrayOfBool | 
|   [apigateway:Request/ApiName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by API name. Available during the CreateApi and UpdateApi operations | String | 
|   [apigateway:Request/AuthorizerType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by type of authorizer in the request, for example REQUEST or JWT. Available during CreateAuthorizer and UpdateAuthorizer. Also available during import and reimport as an ArrayOfString | ArrayOfString | 
|   [apigateway:Request/AuthorizerUri](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by URI of a Lambda authorizer function. Available during CreateAuthorizer and UpdateAuthorizer. Also available during import and reimport as an ArrayOfString | ArrayOfString | 
|   [apigateway:Request/CognitoUserPoolArn](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's CognitoUserPoolArn that is passed in the request | ARN | 
|   [apigateway:Request/ConditionBasePaths](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by base paths defined on the condition of a routing rule. Available during the CreateRoutingRule and UpdateRoutingRule operations | ArrayOfString | 
|   [apigateway:Request/DisableExecuteApiEndpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by status of the default execute-api endpoint. Available during the CreateApi and UpdateApi operations | Bool | 
|   [apigateway:Request/EndpointType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by endpoint type. Available during the CreateDomainName, UpdateDomainName, CreateApi, and UpdateApi operations | ArrayOfString | 
|   [apigateway:Request/Method](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's HTTP Method that is passed in the request | String | 
|   [apigateway:Request/MtlsTrustStoreUri](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by URI of the truststore used for mutual TLS authentication. Available during the CreateDomainName and UpdateDomainName operations | String | 
|   [apigateway:Request/MtlsTrustStoreVersion](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by version of the truststore used for mutual TLS authentication. Available during the CreateDomainName and UpdateDomainName operations | String | 
|   [apigateway:Request/PortalDisplayName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's Display Name that is passed in the request | String | 
|   [apigateway:Request/PortalDomainName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's vanity domain name that is passed in the request | String | 
|   [apigateway:Request/PortalProductDisplayName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a PortalProduct's Display Name that is passed in the request | String | 
|   [apigateway:Request/Priority](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by priority of the routing rule. Available during the CreateRoutingRule and UpdateRoutingRule operations | Numeric | 
|   [apigateway:Request/ProductPageTitle](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductPage's Title that is passed in the request | String | 
|   [apigateway:Request/ProductRestEndpointPageEndpointPrefix](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's EndpointPrefix that is passed in the request | String | 
|   [apigateway:Request/RestApiId](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's Amazon API Gateway API ID that is passed in the request | String | 
|   [apigateway:Request/RouteAuthorizationType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by authorization type, for example NONE, AWS\_IAM, CUSTOM, JWT. Available during the CreateRoute and UpdateRoute operations. Also available as a collection during import | ArrayOfString | 
|   [apigateway:Request/RoutingMode](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by routing mode of the domain name. Available during the CreateDomainName and UpdateDomainName operations | String | 
|   [apigateway:Request/SecurityPolicy](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by TLS version. Available during the CreateDomain and UpdateDomain operations | ArrayOfString | 
|   [apigateway:Request/Stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's Amazon API Gateway Stage Name that is passed in the request | String | 
|   [apigateway:Request/StageName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by stage name of the deployment that you attempt to create. Available during the CreateDeployment operation | String | 
|   [apigateway:Resource/AccessLoggingDestination](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log destination of the current Stage resource. Available during the UpdateStage and DeleteStage operations | String | 
|   [apigateway:Resource/AccessLoggingFormat](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log format of the current Stage resource. Available during the UpdateStage and DeleteStage operations | String | 
|   [apigateway:Resource/ApiKeyRequired](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by the requirement of API key for the existing Route resource. Available during the UpdateRoute and DeleteRoute operations. Also available as a collection during reimport | ArrayOfBool | 
|   [apigateway:Resource/ApiName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by API name. Available during the UpdateApi and DeleteApi operations | String | 
|   [apigateway:Resource/AuthorizerType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by the current type of authorizer, for example REQUEST or JWT. Available during UpdateAuthorizer and DeleteAuthorizer operations. Also available during import and reimport as an ArrayOfString | ArrayOfString | 
|   [apigateway:Resource/AuthorizerUri](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by the URI of the current Lambda authorizer associated with the current API. Available during UpdateAuthorizer and DeleteAuthorizer. Also available as a collection during reimport | ArrayOfString | 
|   [apigateway:Resource/CognitoUserPoolArn](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's CognitoUserPoolArn associated with the resource | ARN | 
|   [apigateway:Resource/ConditionBasePaths](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by base paths defined on the condition of the existing routing rule. Available during the UpdateRoutingRule and DeleteRoutingRule operations | ArrayOfString | 
|   [apigateway:Resource/DisableExecuteApiEndpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by status of the default execute-api endpoint. Available during the UpdateApi and DeleteApi operations | Bool | 
|   [apigateway:Resource/EndpointType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by endpoint type. Available during the UpdateDomainName, DeleteDomainName, UpdateApi, and DeleteApi operations | ArrayOfString | 
|   [apigateway:Resource/Method](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's HTTP Method associated with the resource | String | 
|   [apigateway:Resource/MtlsTrustStoreUri](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by URI of the truststore used for mutual TLS authentication. Available during the UpdateDomainName and DeleteDomainName operations | String | 
|   [apigateway:Resource/MtlsTrustStoreVersion](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by version of the truststore used for mutual TLS authentication. Available during the UpdateDomainName and DeleteDomainName operations | String | 
|   [apigateway:Resource/PortalDisplayName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's Display Name associated with the resource | String | 
|   [apigateway:Resource/PortalDomainName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's vanity domain name associated with the resource | String | 
|   [apigateway:Resource/PortalProductDisplayName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a PortalProduct's Display Name associated with the resource | String | 
|   [apigateway:Resource/PortalPublishStatus](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a Portal's published status associated with the resource | String | 
|   [apigateway:Resource/Priority](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by priority of the existing routing rule. Available during the UpdateRoutingRule and DeleteRoutingRule operations | Numeric | 
|   [apigateway:Resource/ProductPageTitle](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductPage's Title associated with the resource | String | 
|   [apigateway:Resource/ProductRestEndpointPageEndpointPrefix](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's EndpointPrefix associated with the resource | String | 
|   [apigateway:Resource/RestApiId](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's Amazon API Gateway API ID associated with the resource | String | 
|   [apigateway:Resource/RouteAuthorizationType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by authorization type of the existing Route resource, for example NONE, AWS\_IAM, CUSTOM. Available during the UpdateRoute and DeleteRoute operations. Also available as a collection during reimport | ArrayOfString | 
|   [apigateway:Resource/RoutingMode](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by routing mode of the existing domain name. Available during the UpdateDomainName and DeleteDomainName operations | String | 
|   [apigateway:Resource/SecurityPolicy](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by TLS version. Available during the UpdateDomainName and DeleteDomainName operations | ArrayOfString | 
|   [apigateway:Resource/Stage](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by a ProductRestEndpointPage's Amazon API Gateway Stage Name associated with the resource | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | Filters access by the presence of tag keys in the request | ArrayOfString | 