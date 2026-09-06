

# Actions, resources, and condition keys for Amazon API Gateway Management
<a name="list_apigateway"></a>

Amazon API Gateway Management (service prefix: `apigateway`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/apigateway/apigateway.json) for this service.

**Topics**
+ [API operations defined by Amazon API Gateway Management](#list_apigateway-operations)
+ [Actions defined by Amazon API Gateway Management](#list_apigateway-actions-as-permissions)
+ [Resource types defined by Amazon API Gateway Management](#list_apigateway-resources-for-iam-policies)
+ [Condition keys for Amazon API Gateway Management](#list_apigateway-policy-keys)

## API operations defined by Amazon API Gateway Management
<a name="list_apigateway-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_apigateway-actions-as-permissions).




- **   CreateApiKey  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAuthorizer  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   CreateBasePathMapping  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDeployment  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDocumentationPart  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDocumentationVersion  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomainName  **
  - **IAM action:**  [apigateway:AddCertificateToDomain](#list_apigateway-action-AddCertificateToDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:UpdateDomainNamePolicy](#list_apigateway-action-UpdateDomainNamePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateDomainNameAccessAssociation  **
  - **IAM action:**  [apigateway:CreateAccessAssociation](#list_apigateway-action-CreateAccessAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateModel  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRequestValidator  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResource  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRestApi  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:UpdateRestApiPolicy](#list_apigateway-action-UpdateRestApiPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateStage  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUsagePlan  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUsagePlanKey  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVpcLink  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteApiKey  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAuthorizer  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBasePathMapping  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClientCertificate  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeployment  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDocumentationPart  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDocumentationVersion  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainName  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:RemoveCertificateFromDomain](#list_apigateway-action-RemoveCertificateFromDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DeleteDomainNameAccessAssociation  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGatewayResponse  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegrationResponse  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMethod  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMethodResponse  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModel  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRequestValidator  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResource  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRestApi  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStage  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUsagePlan  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUsagePlanKey  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcLink  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FlushStageAuthorizersCache  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FlushStageCache  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateClientCertificate  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetAccount  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiKey  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiKeys  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAuthorizer  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAuthorizers  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBasePathMapping  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBasePathMappings  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClientCertificate  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClientCertificates  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployment  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployments  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentationPart  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentationParts  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentationVersion  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentationVersions  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainName  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainNameAccessAssociations  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainNames  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExport  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGatewayResponse  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGatewayResponses  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegration  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegrationResponse  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMethod  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMethodResponse  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModel  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModelTemplate  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModels  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRequestValidator  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRequestValidators  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResource  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResources  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRestApi  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRestApis  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSdk  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSdkType  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSdkTypes  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStage  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStages  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTags  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsage  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsagePlan  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsagePlanKey  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsagePlanKeys  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsagePlans  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcLink  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcLinks  **
  - **IAM action:**  [apigateway:GET](#list_apigateway-action-GET) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportApiKeys  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ImportDocumentationParts  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ImportRestApi  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:UpdateRestApiPolicy](#list_apigateway-action-UpdateRestApiPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   PutGatewayResponse  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutIntegration  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   PutIntegrationResponse  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMethod  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutMethodResponse  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRestApi  **
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:UpdateRestApiPolicy](#list_apigateway-action-UpdateRestApiPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   RejectDomainNameAccessAssociation  **
  - **IAM action:**  [apigateway:RejectAccessAssociation](#list_apigateway-action-RejectAccessAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   TagResource  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PUT](#list_apigateway-action-PUT)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TestInvokeAuthorizer  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestInvokeMethod  **
  - **IAM action:**  [apigateway:POST](#list_apigateway-action-POST) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [apigateway:DELETE](#list_apigateway-action-DELETE)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateAccount  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   UpdateApiKey  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAuthorizer  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   UpdateBasePathMapping  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClientCertificate  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDeployment  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDocumentationPart  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDocumentationVersion  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainName  **
  - **IAM action:**  [apigateway:AddCertificateToDomain](#list_apigateway-action-AddCertificateToDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:RemoveCertificateFromDomain](#list_apigateway-action-RemoveCertificateFromDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:UpdateDomainNameManagementPolicy](#list_apigateway-action-UpdateDomainNameManagementPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apigateway:UpdateDomainNamePolicy](#list_apigateway-action-UpdateDomainNamePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   UpdateGatewayResponse  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntegration  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** apigateway.amazonaws.com / **Access level:** Write

- **   UpdateIntegrationResponse  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMethod  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMethodResponse  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModel  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRequestValidator  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResource  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRestApi  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apigateway:UpdateRestApiPolicy](#list_apigateway-action-UpdateRestApiPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   UpdateStage  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUsage  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUsagePlan  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcLink  **
  - **IAM action:**  [apigateway:PATCH](#list_apigateway-action-PATCH) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon API Gateway Management
<a name="list_apigateway-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddCertificateToDomain](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to add certificates for mutual TLS authentication to a domain name. This is an additional authorization control for managing the DomainName resource due to the sensitive nature of mTLS
  - **Resource types (\*required):** [DomainName](#list_apigateway-resource-DomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/MtlsTrustStoreUri](#list_apigateway-apigateway_Resource_MtlsTrustStoreUri)<br />[apigateway:Resource/MtlsTrustStoreVersion](#list_apigateway-apigateway_Resource_MtlsTrustStoreVersion)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DomainNames](#list_apigateway-resource-DomainNames) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateAccessAssociation](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to create an access association from an access association source to a custom domain name for private APIs
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName)
  - **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DELETE](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to delete a particular resource
  - **Resource types (\*required):** [ApiKey](#list_apigateway-resource-ApiKey) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Authorizer](#list_apigateway-resource-Authorizer) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [BasePathMapping](#list_apigateway-resource-BasePathMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [ClientCertificate](#list_apigateway-resource-ClientCertificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Deployment](#list_apigateway-resource-Deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DocumentationPart](#list_apigateway-resource-DocumentationPart) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DocumentationVersion](#list_apigateway-resource-DocumentationVersion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DomainName](#list_apigateway-resource-DomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/MtlsTrustStoreUri](#list_apigateway-apigateway_Resource_MtlsTrustStoreUri)<br />[apigateway:Resource/MtlsTrustStoreVersion](#list_apigateway-apigateway_Resource_MtlsTrustStoreVersion)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DomainNameAccessAssociation](#list_apigateway-resource-DomainNameAccessAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [GatewayResponse](#list_apigateway-resource-GatewayResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Integration](#list_apigateway-resource-Integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigateway-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Method](#list_apigateway-resource-Method) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [MethodResponse](#list_apigateway-resource-MethodResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Model](#list_apigateway-resource-Model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [PrivateBasePathMapping](#list_apigateway-resource-PrivateBasePathMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RequestValidator](#list_apigateway-resource-RequestValidator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Resource](#list_apigateway-resource-Resource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RestApi](#list_apigateway-resource-RestApi) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigateway-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_apigateway-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigateway-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigateway-apigateway_Resource_AccessLoggingFormat)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Tags](#list_apigateway-resource-Tags) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Template](#list_apigateway-resource-Template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [UsagePlan](#list_apigateway-resource-UsagePlan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [UsagePlanKey](#list_apigateway-resource-UsagePlanKey) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [VpcLink](#list_apigateway-resource-VpcLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Access level:** Write

- **   [GET](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to read a particular resource
  - **Resource types (\*required):** [Account](#list_apigateway-resource-Account) / **Condition keys:**  
  - **Resource types (\*required):** [ApiKey](#list_apigateway-resource-ApiKey) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ApiKeys](#list_apigateway-resource-ApiKeys) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Authorizer](#list_apigateway-resource-Authorizer) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Authorizers](#list_apigateway-resource-Authorizers) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [BasePathMapping](#list_apigateway-resource-BasePathMapping) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [BasePathMappings](#list_apigateway-resource-BasePathMappings) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ClientCertificate](#list_apigateway-resource-ClientCertificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ClientCertificates](#list_apigateway-resource-ClientCertificates) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Deployment](#list_apigateway-resource-Deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Deployments](#list_apigateway-resource-Deployments) / **Condition keys:** [apigateway:Request/StageName](#list_apigateway-apigateway_Request_StageName)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DocumentationPart](#list_apigateway-resource-DocumentationPart) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DocumentationParts](#list_apigateway-resource-DocumentationParts) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DocumentationVersion](#list_apigateway-resource-DocumentationVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DocumentationVersions](#list_apigateway-resource-DocumentationVersions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DomainName](#list_apigateway-resource-DomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/MtlsTrustStoreUri](#list_apigateway-apigateway_Resource_MtlsTrustStoreUri)<br />[apigateway:Resource/MtlsTrustStoreVersion](#list_apigateway-apigateway_Resource_MtlsTrustStoreVersion)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DomainNameAccessAssociations](#list_apigateway-resource-DomainNameAccessAssociations) / **Condition keys:** [apigateway:Request/AccessAssociationSource](#list_apigateway-apigateway_Request_AccessAssociationSource)<br />[apigateway:Request/DomainNameArn](#list_apigateway-apigateway_Request_DomainNameArn)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DomainNames](#list_apigateway-resource-DomainNames) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [GatewayResponse](#list_apigateway-resource-GatewayResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [GatewayResponses](#list_apigateway-resource-GatewayResponses) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Integration](#list_apigateway-resource-Integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigateway-resource-IntegrationResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Method](#list_apigateway-resource-Method) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MethodResponse](#list_apigateway-resource-MethodResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Model](#list_apigateway-resource-Model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Models](#list_apigateway-resource-Models) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PrivateBasePathMapping](#list_apigateway-resource-PrivateBasePathMapping) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PrivateBasePathMappings](#list_apigateway-resource-PrivateBasePathMappings) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RequestValidator](#list_apigateway-resource-RequestValidator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RequestValidators](#list_apigateway-resource-RequestValidators) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Resource](#list_apigateway-resource-Resource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Resources](#list_apigateway-resource-Resources) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RestApi](#list_apigateway-resource-RestApi) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigateway-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RestApis](#list_apigateway-resource-RestApis) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Sdk](#list_apigateway-resource-Sdk) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stage](#list_apigateway-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigateway-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigateway-apigateway_Resource_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stages](#list_apigateway-resource-Stages) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Tags](#list_apigateway-resource-Tags) / **Condition keys:**  
  - **Resource types (\*required):** [UsagePlan](#list_apigateway-resource-UsagePlan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [UsagePlanKey](#list_apigateway-resource-UsagePlanKey) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [UsagePlanKeys](#list_apigateway-resource-UsagePlanKeys) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [UsagePlans](#list_apigateway-resource-UsagePlans) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VpcLink](#list_apigateway-resource-VpcLink) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [VpcLinks](#list_apigateway-resource-VpcLinks) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PATCH](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to update a particular resource
  - **Resource types (\*required):** [Account](#list_apigateway-resource-Account) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [ApiKey](#list_apigateway-resource-ApiKey) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Authorizer](#list_apigateway-resource-Authorizer) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [BasePathMapping](#list_apigateway-resource-BasePathMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [ClientCertificate](#list_apigateway-resource-ClientCertificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Deployment](#list_apigateway-resource-Deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DocumentationPart](#list_apigateway-resource-DocumentationPart) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DocumentationVersion](#list_apigateway-resource-DocumentationVersion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DomainName](#list_apigateway-resource-DomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/MtlsTrustStoreUri](#list_apigateway-apigateway_Resource_MtlsTrustStoreUri)<br />[apigateway:Resource/MtlsTrustStoreVersion](#list_apigateway-apigateway_Resource_MtlsTrustStoreVersion)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [GatewayResponse](#list_apigateway-resource-GatewayResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Integration](#list_apigateway-resource-Integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigateway-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Method](#list_apigateway-resource-Method) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [MethodResponse](#list_apigateway-resource-MethodResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Model](#list_apigateway-resource-Model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [PrivateBasePathMapping](#list_apigateway-resource-PrivateBasePathMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RequestValidator](#list_apigateway-resource-RequestValidator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Resource](#list_apigateway-resource-Resource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RestApi](#list_apigateway-resource-RestApi) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigateway-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_apigateway-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigateway-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigateway-apigateway_Resource_AccessLoggingFormat)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Template](#list_apigateway-resource-Template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [UsagePlan](#list_apigateway-resource-UsagePlan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [UsagePlanKey](#list_apigateway-resource-UsagePlanKey) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [VpcLink](#list_apigateway-resource-VpcLink) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Access level:** Write

- **   [POST](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to create a particular resource
  - **Resource types (\*required):** [ApiKeys](#list_apigateway-resource-ApiKeys) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Authorizers](#list_apigateway-resource-Authorizers) / **Condition keys:** [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [BasePathMappings](#list_apigateway-resource-BasePathMappings) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [ClientCertificates](#list_apigateway-resource-ClientCertificates) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Deployments](#list_apigateway-resource-Deployments) / **Condition keys:** [apigateway:Request/StageName](#list_apigateway-apigateway_Request_StageName)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DocumentationParts](#list_apigateway-resource-DocumentationParts) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DocumentationVersions](#list_apigateway-resource-DocumentationVersions) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DomainNameAccessAssociations](#list_apigateway-resource-DomainNameAccessAssociations) / **Condition keys:** [apigateway:Request/AccessAssociationSource](#list_apigateway-apigateway_Request_AccessAssociationSource)<br />[apigateway:Request/DomainNameArn](#list_apigateway-apigateway_Request_DomainNameArn)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [DomainNames](#list_apigateway-resource-DomainNames) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [GatewayResponses](#list_apigateway-resource-GatewayResponses) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigateway-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [MethodResponse](#list_apigateway-resource-MethodResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Models](#list_apigateway-resource-Models) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [PrivateBasePathMappings](#list_apigateway-resource-PrivateBasePathMappings) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RequestValidators](#list_apigateway-resource-RequestValidators) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Resources](#list_apigateway-resource-Resources) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RestApis](#list_apigateway-resource-RestApis) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Stages](#list_apigateway-resource-Stages) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [UsagePlanKeys](#list_apigateway-resource-UsagePlanKeys) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [UsagePlans](#list_apigateway-resource-UsagePlans) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [VpcLinks](#list_apigateway-resource-VpcLinks) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Access level:** Write

- **   [PUT](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to update a particular resource
  - **Resource types (\*required):** [DocumentationPart](#list_apigateway-resource-DocumentationPart) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [GatewayResponse](#list_apigateway-resource-GatewayResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationResponse](#list_apigateway-resource-IntegrationResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [MethodResponse](#list_apigateway-resource-MethodResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [RestApi](#list_apigateway-resource-RestApi) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigateway-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Resource types (\*required):** [Tags](#list_apigateway-resource-Tags) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apigateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apigateway-aws_TagKeys)
  - **Access level:** Write

- **   [RejectAccessAssociation](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to reject an existing access association owned by another account to a custom domain name for private APIs
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName)
  - **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RemoveCertificateFromDomain](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to remove certificates for mutual TLS authentication from a domain name. This is an additional authorization control for managing the DomainName resource due to the sensitive nature of mTLS
  - **Resource types (\*required):** [DomainName](#list_apigateway-resource-DomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/MtlsTrustStoreUri](#list_apigateway-apigateway_Resource_MtlsTrustStoreUri)<br />[apigateway:Resource/MtlsTrustStoreVersion](#list_apigateway-apigateway_Resource_MtlsTrustStoreVersion)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DomainNames](#list_apigateway-resource-DomainNames) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SetWebACL](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to set a WAF access control list (ACL). This is an additional authorization control for managing the Stage resource due to the sensitive nature of WebAcl's
  - **Resource types (\*required):** [Stage](#list_apigateway-resource-Stage) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigateway-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigateway-apigateway_Resource_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stages](#list_apigateway-resource-Stages) / **Condition keys:** [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateDomainNameManagementPolicy](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to update the management policy of a custom domain name for private APIs
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName)
  - **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateDomainNamePolicy](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to update the invoke policy of a custom domain name for private APIs
  - **Resource types (\*required):** [DomainNames](#list_apigateway-resource-DomainNames) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [PrivateDomainName](#list_apigateway-resource-PrivateDomainName) / **Condition keys:** [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateRestApiPolicy](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html)  **
  - **Description:** Grants permission to manage the IAM resource policy for an API. This is an additional authorization control for managing an API due to the sensitive nature of the resource policy
  - **Resource types (\*required):** [RestApi](#list_apigateway-resource-RestApi) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigateway-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RestApis](#list_apigateway-resource-RestApis) / **Condition keys:** [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon API Gateway Management
<a name="list_apigateway-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Account](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/account |   | 
|  [ApiKey](https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html)  | arn:${Partition}:apigateway:${Region}::/apikeys/${ApiKeyId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [ApiKeys](https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html)  | arn:${Partition}:apigateway:${Region}::/apikeys | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Authorizer](https://docs.aws.amazon.com/apigateway/latest/api/API_Authorizer.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/authorizers/${AuthorizerId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/authorizers/${AuthorizerId} | [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Authorizers](https://docs.aws.amazon.com/apigateway/latest/api/API_Authorizer.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/authorizers, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/authorizers | [apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [BasePathMapping](https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}/basepathmappings/${BasePath} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [BasePathMappings](https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}/basepathmappings | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [ClientCertificate](https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html)  | arn:${Partition}:apigateway:${Region}::/clientcertificates/${ClientCertificateId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [ClientCertificates](https://docs.aws.amazon.com/apigateway/latest/api/API_ClientCertificate.html)  | arn:${Partition}:apigateway:${Region}::/clientcertificates | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Deployment](https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/deployments/${DeploymentId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/deployments/${DeploymentId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Deployments](https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/deployments, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/deployments | [apigateway:Request/StageName](#list_apigateway-apigateway_Request_StageName)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DocumentationPart](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPart.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/documentation/parts/${DocumentationPartId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DocumentationParts](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPart.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/documentation/parts | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DocumentationVersion](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationVersion.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/documentation/versions/${DocumentationVersionId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DocumentationVersions](https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationVersion.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/documentation/versions | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DomainName](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName} | [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/MtlsTrustStoreUri](#list_apigateway-apigateway_Resource_MtlsTrustStoreUri)<br />[apigateway:Resource/MtlsTrustStoreVersion](#list_apigateway-apigateway_Resource_MtlsTrustStoreVersion)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DomainNameAccessAssociation](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainNameAccessAssociation.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/domainnameaccessassociations/domainname/${DomainName}/${SourceType}/${SourceId} |   | 
|  [DomainNameAccessAssociations](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainNameAccessAssociation.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/domainnameaccessassociations | [apigateway:Request/AccessAssociationSource](#list_apigateway-apigateway_Request_AccessAssociationSource)<br />[apigateway:Request/DomainNameArn](#list_apigateway-apigateway_Request_DomainNameArn)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [DomainNames](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html)  | arn:${Partition}:apigateway:${Region}::/domainnames | [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/MtlsTrustStoreUri](#list_apigateway-apigateway_Request_MtlsTrustStoreUri)<br />[apigateway:Request/MtlsTrustStoreVersion](#list_apigateway-apigateway_Request_MtlsTrustStoreVersion)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [GatewayResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/gatewayresponses/${ResponseType} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [GatewayResponses](https://docs.aws.amazon.com/apigateway/latest/api/API_GatewayResponse.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/gatewayresponses | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Integration](https://docs.aws.amazon.com/apigateway/latest/api/API_Integration.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/integrations/${IntegrationId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId}/methods/${HttpMethodType}/integration | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [IntegrationResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_IntegrationResponse.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/integrations/${IntegrationId}/integrationresponses/${IntegrationResponseId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId}/methods/${HttpMethodType}/integration/responses/${StatusCode} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Method](https://docs.aws.amazon.com/apigateway/latest/api/API_Method.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId}/methods/${HttpMethodType} | [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [MethodResponse](https://docs.aws.amazon.com/apigateway/latest/api/API_MethodResponse.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId}/methods/${HttpMethodType}/responses/${StatusCode} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Model](https://docs.aws.amazon.com/apigateway/latest/api/API_Model.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/models/${ModelId}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/models/${ModelName} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Models](https://docs.aws.amazon.com/apigateway/latest/api/API_Model.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/models, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/models | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [PrivateBasePathMapping](https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}\+${DomainIdentifier}/basepathmappings/${BasePath} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [PrivateBasePathMappings](https://docs.aws.amazon.com/apigateway/latest/api/API_BasePathMapping.html)  | arn:${Partition}:apigateway:${Region}::/domainnames/${DomainName}\+${DomainIdentifier}/basepathmappings | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [PrivateDomainName](https://docs.aws.amazon.com/apigateway/latest/api/API_DomainName.html)  | arn:${Partition}:apigateway:${Region}:${Account}:/domainnames/${DomainName}\+${DomainIdentifier} | [apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RoutingMode](#list_apigateway-apigateway_Resource_RoutingMode)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [RequestValidator](https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/requestvalidators/${RequestValidatorId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [RequestValidators](https://docs.aws.amazon.com/apigateway/latest/api/API_RequestValidator.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/requestvalidators | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Resource](https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Resources](https://docs.aws.amazon.com/apigateway/latest/api/API_Resource.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/resources | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [RestApi](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId} | [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[apigateway:Resource/ApiKeyRequired](#list_apigateway-apigateway_Resource_ApiKeyRequired)<br />[apigateway:Resource/ApiName](#list_apigateway-apigateway_Resource_ApiName)<br />[apigateway:Resource/AuthorizerType](#list_apigateway-apigateway_Resource_AuthorizerType)<br />[apigateway:Resource/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Resource_DisableExecuteApiEndpoint)<br />[apigateway:Resource/EndpointType](#list_apigateway-apigateway_Resource_EndpointType)<br />[apigateway:Resource/RouteAuthorizationType](#list_apigateway-apigateway_Resource_RouteAuthorizationType)<br />[apigateway:Resource/SecurityPolicy](#list_apigateway-apigateway_Resource_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [RestApis](https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html)  | arn:${Partition}:apigateway:${Region}::/restapis | [apigateway:Request/ApiKeyRequired](#list_apigateway-apigateway_Request_ApiKeyRequired)<br />[apigateway:Request/ApiName](#list_apigateway-apigateway_Request_ApiName)<br />[apigateway:Request/AuthorizerType](#list_apigateway-apigateway_Request_AuthorizerType)<br />[apigateway:Request/DisableExecuteApiEndpoint](#list_apigateway-apigateway_Request_DisableExecuteApiEndpoint)<br />[apigateway:Request/EndpointType](#list_apigateway-apigateway_Request_EndpointType)<br />[apigateway:Request/RouteAuthorizationType](#list_apigateway-apigateway_Request_RouteAuthorizationType)<br />[apigateway:Request/SecurityPolicy](#list_apigateway-apigateway_Request_SecurityPolicy)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Sdk](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/stages/${StageName}/sdks/${SdkType} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Stage](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages/${StageName}, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/stages/${StageName} | [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[apigateway:Resource/AccessLoggingDestination](#list_apigateway-apigateway_Resource_AccessLoggingDestination)<br />[apigateway:Resource/AccessLoggingFormat](#list_apigateway-apigateway_Resource_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Stages](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html)  | arn:${Partition}:apigateway:${Region}::/apis/${ApiId}/stages, arn:${Partition}:apigateway:${Region}::/restapis/${RestApiId}/stages | [apigateway:Request/AccessLoggingDestination](#list_apigateway-apigateway_Request_AccessLoggingDestination)<br />[apigateway:Request/AccessLoggingFormat](#list_apigateway-apigateway_Request_AccessLoggingFormat)<br />[aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [Tags](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | arn:${Partition}:apigateway:${Region}::/tags/${UrlEncodedResourceARN} |   | 
|  [Template](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:apigateway:${Region}::/restapis/models/${ModelName}/template | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [UsagePlan](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html)  | arn:${Partition}:apigateway:${Region}::/usageplans/${UsagePlanId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [UsagePlanKey](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlanKey.html)  | arn:${Partition}:apigateway:${Region}::/usageplans/${UsagePlanId}/keys/${Id} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [UsagePlanKeys](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlanKey.html)  | arn:${Partition}:apigateway:${Region}::/usageplans/${UsagePlanId}/keys | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [UsagePlans](https://docs.aws.amazon.com/apigateway/latest/api/API_UsagePlan.html)  | arn:${Partition}:apigateway:${Region}::/usageplans | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [VpcLink](https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html)  | arn:${Partition}:apigateway:${Region}::/vpclinks/${VpcLinkId} | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 
|  [VpcLinks](https://docs.aws.amazon.com/apigateway/latest/api/API_VpcLink.html)  | arn:${Partition}:apigateway:${Region}::/vpclinks | [aws:ResourceTag/${TagKey}](#list_apigateway-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon API Gateway Management
<a name="list_apigateway-policy-keys"></a>

Amazon API Gateway Management defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [apigateway:Request/AccessAssociationSource](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access association source. Available during the CreateDomainNameAccessAssociation operation | String | 
|   [apigateway:Request/AccessLoggingDestination](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log destination. Available during the CreateStage and UpdateStage operations | String | 
|   [apigateway:Request/AccessLoggingFormat](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log format. Available during the CreateStage and UpdateStage operations | String | 
|   [apigateway:Request/ApiKeyRequired](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by whether an API key is required or not. Available during the CreateMethod and PutMethod operations. Also available as a collection during import and reimport | ArrayOfBool | 
|   [apigateway:Request/ApiName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by API name. Available during the CreateRestApi and UpdateRestApi operations | String | 
|   [apigateway:Request/AuthorizerType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by type of authorizer in the request, for example TOKEN, REQUEST, JWT. Available during CreateAuthorizer and UpdateAuthorizer. Also available during import and reimport as an ArrayOfString | ArrayOfString | 
|   [apigateway:Request/DisableExecuteApiEndpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by status of the default execute-api endpoint. Available during the CreateRestApi and DeleteRestApi operations | Bool | 
|   [apigateway:Request/DomainNameArn](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by domain name ARN. Available during the CreateDomainNameAccessAssociation operation | ARN | 
|   [apigateway:Request/EndpointType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by endpoint type. Available during the CreateDomainName, UpdateDomainName, CreateRestApi, and UpdateRestApi operations | ArrayOfString | 
|   [apigateway:Request/MtlsTrustStoreUri](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by URI of the truststore used for mutual TLS authentication. Available during the CreateDomainName and UpdateDomainName operations | String | 
|   [apigateway:Request/MtlsTrustStoreVersion](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by version of the truststore used for mutual TLS authentication. Available during the CreateDomainName and UpdateDomainName operations | String | 
|   [apigateway:Request/RouteAuthorizationType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by authorization type, for example NONE, AWS\_IAM, CUSTOM, JWT, COGNITO\_USER\_POOLS. Available during the CreateMethod and PutMethod operations Also available as a collection during import | ArrayOfString | 
|   [apigateway:Request/RoutingMode](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by routing mode of the domain name. Available during the CreateDomainName and UpdateDomainName operations | String | 
|   [apigateway:Request/SecurityPolicy](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by TLS version. Available during the CreateDomain and UpdateDomain operations | ArrayOfString | 
|   [apigateway:Request/StageName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by stage name of the deployment that you attempt to create. Available during the CreateDeployment operation | String | 
|   [apigateway:Resource/AccessLoggingDestination](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log destination of the current Stage resource. Available during the UpdateStage and DeleteStage operations | String | 
|   [apigateway:Resource/AccessLoggingFormat](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by access log format of the current Stage resource. Available during the UpdateStage and DeleteStage operations | String | 
|   [apigateway:Resource/ApiKeyRequired](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by whether an API key is required or not for the existing Method resource. Available during the PutMethod and DeleteMethod operations. Also available as a collection during reimport | ArrayOfBool | 
|   [apigateway:Resource/ApiName](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by API name of the existing RestApi resource. Available during UpdateRestApi and DeleteRestApi operations | String | 
|   [apigateway:Resource/AuthorizerType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by the current type of authorizer, for example TOKEN, REQUEST, JWT. Available during UpdateAuthorizer and DeleteAuthorizer operations. Also available during reimport as an ArrayOfString | ArrayOfString | 
|   [apigateway:Resource/DisableExecuteApiEndpoint](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by status of the default execute-api endpoint of the current RestApi resource. Available during UpdateRestApi and DeleteRestApi operations | Bool | 
|   [apigateway:Resource/EndpointType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by endpoint type. Available during the UpdateDomainName, DeleteDomainName, UpdateRestApi, and DeleteRestApi operations | ArrayOfString | 
|   [apigateway:Resource/MtlsTrustStoreUri](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by URI of the truststore used for mutual TLS authentication. Available during UpdateDomainName and DeleteDomainName operations | String | 
|   [apigateway:Resource/MtlsTrustStoreVersion](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by version of the truststore used for mutual TLS authentication. Available during UpdateDomainName and DeleteDomainName operations | String | 
|   [apigateway:Resource/RouteAuthorizationType](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by authorization type of the existing Method resource, for example NONE, AWS\_IAM, CUSTOM, JWT, COGNITO\_USER\_POOLS. Available during the PutMethod and DeleteMethod operations. Also available as a collection during reimport | ArrayOfString | 
|   [apigateway:Resource/RoutingMode](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-routing-mode)  | Filters access by routing mode of the domain name. Available during the UpdateDomainName and DeleteDomainName operations | String | 
|   [apigateway:Resource/SecurityPolicy](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by TLS version. Available during UpdateDomain and DeleteDomain operations | ArrayOfString | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)  | Filters access by the tag keys in the request | ArrayOfString | 