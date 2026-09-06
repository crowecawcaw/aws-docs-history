

# Actions, resources, and condition keys for AWS Proton
<a name="list_proton"></a>

AWS Proton (service prefix: `proton`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/proton/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/proton/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/proton/latest/adminguide/ag-controlling-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/proton/proton.json) for this service.

**Topics**
+ [API operations defined by AWS Proton](#list_proton-operations)
+ [Actions defined by AWS Proton](#list_proton-actions-as-permissions)
+ [Resource types defined by AWS Proton](#list_proton-resources-for-iam-policies)
+ [Condition keys for AWS Proton](#list_proton-policy-keys)

## API operations defined by AWS Proton
<a name="list_proton-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_proton-actions-as-permissions).




- **   AcceptEnvironmentAccountConnection  **
  - **IAM action:**  [proton:AcceptEnvironmentAccountConnection](#list_proton-action-AcceptEnvironmentAccountConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelComponentDeployment  **
  - **IAM action:**  [proton:CancelComponentDeployment](#list_proton-action-CancelComponentDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelEnvironmentDeployment  **
  - **IAM action:**  [proton:CancelEnvironmentDeployment](#list_proton-action-CancelEnvironmentDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelServiceInstanceDeployment  **
  - **IAM action:**  [proton:CancelServiceInstanceDeployment](#list_proton-action-CancelServiceInstanceDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelServicePipelineDeployment  **
  - **IAM action:**  [proton:CancelServicePipelineDeployment](#list_proton-action-CancelServicePipelineDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateComponent  **
  - **IAM action:**  [proton:CreateComponent](#list_proton-action-CreateComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEnvironment  **
  - **IAM action:**  [proton:CreateEnvironment](#list_proton-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** proton.amazonaws.com / **Access level:** Write

- **   CreateEnvironmentAccountConnection  **
  - **IAM action:**  [proton:CreateEnvironmentAccountConnection](#list_proton-action-CreateEnvironmentAccountConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** proton.amazonaws.com / **Access level:** Write

- **   CreateEnvironmentTemplate  **
  - **IAM action:**  [proton:CreateEnvironmentTemplate](#list_proton-action-CreateEnvironmentTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEnvironmentTemplateVersion  **
  - **IAM action:**  [proton:CreateEnvironmentTemplateVersion](#list_proton-action-CreateEnvironmentTemplateVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRepository  **
  - **IAM action:**  [proton:CreateRepository](#list_proton-action-CreateRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateService  **
  - **IAM action:**  [proton:CreateService](#list_proton-action-CreateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateServiceInstance  **
  - **IAM action:**  [proton:CreateServiceInstance](#list_proton-action-CreateServiceInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceSyncConfig  **
  - **IAM action:**  [proton:CreateServiceSyncConfig](#list_proton-action-CreateServiceSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateServiceTemplate  **
  - **IAM action:**  [proton:CreateServiceTemplate](#list_proton-action-CreateServiceTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceTemplateVersion  **
  - **IAM action:**  [proton:CreateServiceTemplateVersion](#list_proton-action-CreateServiceTemplateVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTemplateSyncConfig  **
  - **IAM action:**  [proton:CreateTemplateSyncConfig](#list_proton-action-CreateTemplateSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteComponent  **
  - **IAM action:**  [proton:DeleteComponent](#list_proton-action-DeleteComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeployment  **
  - **IAM action:**  [proton:DeleteDeployment](#list_proton-action-DeleteDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [proton:DeleteEnvironment](#list_proton-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentAccountConnection  **
  - **IAM action:**  [proton:DeleteEnvironmentAccountConnection](#list_proton-action-DeleteEnvironmentAccountConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentTemplate  **
  - **IAM action:**  [proton:DeleteEnvironmentTemplate](#list_proton-action-DeleteEnvironmentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentTemplateVersion  **
  - **IAM action:**  [proton:DeleteEnvironmentTemplateVersion](#list_proton-action-DeleteEnvironmentTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRepository  **
  - **IAM action:**  [proton:DeleteRepository](#list_proton-action-DeleteRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteService  **
  - **IAM action:**  [proton:DeleteService](#list_proton-action-DeleteService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceSyncConfig  **
  - **IAM action:**  [proton:DeleteServiceSyncConfig](#list_proton-action-DeleteServiceSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceTemplate  **
  - **IAM action:**  [proton:DeleteServiceTemplate](#list_proton-action-DeleteServiceTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceTemplateVersion  **
  - **IAM action:**  [proton:DeleteServiceTemplateVersion](#list_proton-action-DeleteServiceTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplateSyncConfig  **
  - **IAM action:**  [proton:DeleteTemplateSyncConfig](#list_proton-action-DeleteTemplateSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountSettings  **
  - **IAM action:**  [proton:GetAccountSettings](#list_proton-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComponent  **
  - **IAM action:**  [proton:GetComponent](#list_proton-action-GetComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployment  **
  - **IAM action:**  [proton:GetComponent](#list_proton-action-GetComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [proton:GetDeployment](#list_proton-action-GetDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [proton:GetEnvironment](#list_proton-action-GetEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [proton:GetService](#list_proton-action-GetService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [proton:GetServiceInstance](#list_proton-action-GetServiceInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [proton:GetEnvironment](#list_proton-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentAccountConnection  **
  - **IAM action:**  [proton:GetEnvironmentAccountConnection](#list_proton-action-GetEnvironmentAccountConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentTemplate  **
  - **IAM action:**  [proton:GetEnvironmentTemplate](#list_proton-action-GetEnvironmentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironmentTemplateVersion  **
  - **IAM action:**  [proton:GetEnvironmentTemplateVersion](#list_proton-action-GetEnvironmentTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepository  **
  - **IAM action:**  [proton:GetRepository](#list_proton-action-GetRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRepositorySyncStatus  **
  - **IAM action:**  [proton:GetRepositorySyncStatus](#list_proton-action-GetRepositorySyncStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcesSummary  **
  - **IAM action:**  [proton:GetResourcesSummary](#list_proton-action-GetResourcesSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **IAM action:**  [proton:GetService](#list_proton-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceInstance  **
  - **IAM action:**  [proton:GetServiceInstance](#list_proton-action-GetServiceInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceInstanceSyncStatus  **
  - **IAM action:**  [proton:GetServiceInstanceSyncStatus](#list_proton-action-GetServiceInstanceSyncStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceSyncBlockerSummary  **
  - **IAM action:**  [proton:GetServiceSyncBlockerSummary](#list_proton-action-GetServiceSyncBlockerSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceSyncConfig  **
  - **IAM action:**  [proton:GetServiceSyncConfig](#list_proton-action-GetServiceSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceTemplate  **
  - **IAM action:**  [proton:GetServiceTemplate](#list_proton-action-GetServiceTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceTemplateVersion  **
  - **IAM action:**  [proton:GetServiceTemplateVersion](#list_proton-action-GetServiceTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplateSyncConfig  **
  - **IAM action:**  [proton:GetTemplateSyncConfig](#list_proton-action-GetTemplateSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplateSyncStatus  **
  - **IAM action:**  [proton:GetTemplateSyncStatus](#list_proton-action-GetTemplateSyncStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListComponentOutputs  **
  - **IAM action:**  [proton:ListComponentOutputs](#list_proton-action-ListComponentOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponentProvisionedResources  **
  - **IAM action:**  [proton:ListComponentProvisionedResources](#list_proton-action-ListComponentProvisionedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponents  **
  - **IAM action:**  [proton:ListComponents](#list_proton-action-ListComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeployments  **
  - **IAM action:**  [proton:ListDeployments](#list_proton-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentAccountConnections  **
  - **IAM action:**  [proton:ListEnvironmentAccountConnections](#list_proton-action-ListEnvironmentAccountConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentOutputs  **
  - **IAM action:**  [proton:ListEnvironmentOutputs](#list_proton-action-ListEnvironmentOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentProvisionedResources  **
  - **IAM action:**  [proton:ListEnvironmentProvisionedResources](#list_proton-action-ListEnvironmentProvisionedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentTemplateVersions  **
  - **IAM action:**  [proton:ListEnvironmentTemplateVersions](#list_proton-action-ListEnvironmentTemplateVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironmentTemplates  **
  - **IAM action:**  [proton:ListEnvironmentTemplates](#list_proton-action-ListEnvironmentTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironments  **
  - **IAM action:**  [proton:ListEnvironments](#list_proton-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRepositories  **
  - **IAM action:**  [proton:ListRepositories](#list_proton-action-ListRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRepositorySyncDefinitions  **
  - **IAM action:**  [proton:ListRepositorySyncDefinitions](#list_proton-action-ListRepositorySyncDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceInstanceOutputs  **
  - **IAM action:**  [proton:ListServiceInstanceOutputs](#list_proton-action-ListServiceInstanceOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceInstanceProvisionedResources  **
  - **IAM action:**  [proton:ListServiceInstanceProvisionedResources](#list_proton-action-ListServiceInstanceProvisionedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceInstances  **
  - **IAM action:**  [proton:ListServiceInstances](#list_proton-action-ListServiceInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServicePipelineOutputs  **
  - **IAM action:**  [proton:ListServicePipelineOutputs](#list_proton-action-ListServicePipelineOutputs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServicePipelineProvisionedResources  **
  - **IAM action:**  [proton:ListServicePipelineProvisionedResources](#list_proton-action-ListServicePipelineProvisionedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceTemplateVersions  **
  - **IAM action:**  [proton:ListServiceTemplateVersions](#list_proton-action-ListServiceTemplateVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServiceTemplates  **
  - **IAM action:**  [proton:ListServiceTemplates](#list_proton-action-ListServiceTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServices  **
  - **IAM action:**  [proton:ListServices](#list_proton-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [proton:ListTagsForResource](#list_proton-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   NotifyResourceDeploymentStatusChange  **
  - **IAM action:**  [proton:NotifyResourceDeploymentStatusChange](#list_proton-action-NotifyResourceDeploymentStatusChange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectEnvironmentAccountConnection  **
  - **IAM action:**  [proton:RejectEnvironmentAccountConnection](#list_proton-action-RejectEnvironmentAccountConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [proton:TagResource](#list_proton-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [proton:UntagResource](#list_proton-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountSettings  **
  - **IAM action:**  [proton:UpdateAccountSettings](#list_proton-action-UpdateAccountSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** proton.amazonaws.com / **Access level:** Write

- **   UpdateComponent  **
  - **IAM action:**  [proton:UpdateComponent](#list_proton-action-UpdateComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironment  **
  - **IAM action:**  [proton:UpdateEnvironment](#list_proton-action-UpdateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** proton.amazonaws.com / **Access level:** Write

- **   UpdateEnvironmentAccountConnection  **
  - **IAM action:**  [proton:UpdateEnvironmentAccountConnection](#list_proton-action-UpdateEnvironmentAccountConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** proton.amazonaws.com / **Access level:** Write

- **   UpdateEnvironmentTemplate  **
  - **IAM action:**  [proton:UpdateEnvironmentTemplate](#list_proton-action-UpdateEnvironmentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironmentTemplateVersion  **
  - **IAM action:**  [proton:UpdateEnvironmentTemplateVersion](#list_proton-action-UpdateEnvironmentTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateService  **
  - **IAM action:**  [proton:UpdateService](#list_proton-action-UpdateService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceInstance  **
  - **IAM action:**  [proton:UpdateServiceInstance](#list_proton-action-UpdateServiceInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServicePipeline  **
  - **IAM action:**  [proton:UpdateServicePipeline](#list_proton-action-UpdateServicePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceSyncBlocker  **
  - **IAM action:**  [proton:UpdateServiceSyncBlocker](#list_proton-action-UpdateServiceSyncBlocker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceTemplate  **
  - **IAM action:**  [proton:UpdateServiceTemplate](#list_proton-action-UpdateServiceTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceTemplateVersion  **
  - **IAM action:**  [proton:UpdateServiceTemplateVersion](#list_proton-action-UpdateServiceTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTemplateSyncConfig  **
  - **IAM action:**  [proton:UpdateTemplateSyncConfig](#list_proton-action-UpdateTemplateSyncConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Proton
<a name="list_proton-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptEnvironmentAccountConnection](https://docs.aws.amazon.com/proton/latest/APIReference/API_AcceptEnvironmentAccountConnection.html)  **
  - **Description:** Grants permission to reject an environment account connection request from another environment account
  - **Resource types (\*required):** [environment-account-connection\*](#list_proton-resource-environment-account-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelComponentDeployment](https://docs.aws.amazon.com/proton/latest/APIReference/API_CancelComponentDeployment.html)  **
  - **Description:** Grants permission to cancel component deployment
  - **Resource types (\*required):** [component\*](#list_proton-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelEnvironmentDeployment](https://docs.aws.amazon.com/proton/latest/APIReference/API_CancelEnvironmentDeployment.html)  **
  - **Description:** Grants permission to cancel an environment deployment
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:EnvironmentTemplate](#list_proton-proton_EnvironmentTemplate)
  - **Access level:** Write

- **   [CancelServiceInstanceDeployment](https://docs.aws.amazon.com/proton/latest/APIReference/API_CancelServiceInstanceDeployment.html)  **
  - **Description:** Grants permission to cancel a service instance deployment
  - **Resource types (\*required):** [service-instance\*](#list_proton-resource-service-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [CancelServicePipelineDeployment](https://docs.aws.amazon.com/proton/latest/APIReference/API_CancelServicePipelineDeployment.html)  **
  - **Description:** Grants permission to cancel a service pipeline deployment
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [CreateComponent](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateComponent.html)  **
  - **Description:** Grants permission to create component
  - **Resource types (\*required):** [component\*](#list_proton-resource-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create an environment
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)<br />[proton:EnvironmentTemplate](#list_proton-proton_EnvironmentTemplate)
  - **Access level:** Write

- **   [CreateEnvironmentAccountConnection](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentAccountConnection.html)  **
  - **Description:** Grants permission to create an environment account connection
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironmentTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentTemplate.html)  **
  - **Description:** Grants permission to create an environment template
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironmentTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentTemplateMajorVersion.html)  **
  - **Description:** Grants permission to create an environment template major version. DEPRECATED - use CreateEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironmentTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentTemplateMinorVersion.html)  **
  - **Description:** Grants permission to create an environment template minor version. DEPRECATED - use CreateEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironmentTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironmentTemplateVersion.html)  **
  - **Description:** Grants permission to create an environment template version
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateRepository.html)  **
  - **Description:** Grants permission to create a repository
  - **Resource types (\*required):** [repository\*](#list_proton-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateService](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateService.html)  **
  - **Description:** Grants permission to create a service
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [CreateServiceInstance](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceInstance.html)  **
  - **Description:** Grants permission to create a service instance
  - **Resource types (\*required):** [service-instance\*](#list_proton-resource-service-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [CreateServiceSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceSyncConfig.html)  **
  - **Description:** Grants permission to create a service sync config
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateServiceTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceTemplate.html)  **
  - **Description:** Grants permission to create a service template
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceTemplateMajorVersion.html)  **
  - **Description:** Grants permission to create a service template major version. DEPRECATED - use CreateServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceTemplateMinorVersion.html)  **
  - **Description:** Grants permission to create a service template minor version. DEPRECATED - use CreateServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceTemplateVersion.html)  **
  - **Description:** Grants permission to create a service template version
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTemplateSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateTemplateSyncConfig.html)  **
  - **Description:** Grants permission to create a template sync config
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAccountRoles](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteAccountRoles.html)  **
  - **Description:** Grants permission to delete account roles. DEPRECATED - use UpdateAccountSettings instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteComponent](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteComponent.html)  **
  - **Description:** Grants permission to delete component
  - **Resource types (\*required):** [component\*](#list_proton-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeployment](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteDeployment.html)  **
  - **Description:** Grants permission to delete a deployment
  - **Resource types (\*required):** [deployment\*](#list_proton-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an environment
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:EnvironmentTemplate](#list_proton-proton_EnvironmentTemplate)
  - **Access level:** Write

- **   [DeleteEnvironmentAccountConnection](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironmentAccountConnection.html)  **
  - **Description:** Grants permission to delete an environment account connection
  - **Resource types (\*required):** [environment-account-connection\*](#list_proton-resource-environment-account-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironmentTemplate.html)  **
  - **Description:** Grants permission to delete an environment template
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironmentTemplateMajorVersion.html)  **
  - **Description:** Grants permission to delete an environment template major version. DEPRECATED - use DeleteEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironmentTemplateMinorVersion.html)  **
  - **Description:** Grants permission to delete an environment template minor version. DEPRECATED - use DeleteEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteEnvironmentTemplateVersion.html)  **
  - **Description:** Grants permission to delete an environment template version
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepository](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteRepository.html)  **
  - **Description:** Grants permission to delete a repository
  - **Resource types (\*required):** [repository\*](#list_proton-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteService](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteService.html)  **
  - **Description:** Grants permission to delete a service
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [DeleteServiceSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteServiceSyncConfig.html)  **
  - **Description:** Grants permission to delete a service sync config
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteServiceTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteServiceTemplate.html)  **
  - **Description:** Grants permission to delete a service template
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteServiceTemplateMajorVersion.html)  **
  - **Description:** Grants permission to delete a service template major version. DEPRECATED - use DeleteServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteServiceTemplateMinorVersion.html)  **
  - **Description:** Grants permission to delete a service template minor version. DEPRECATED - use DeleteServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteServiceTemplateVersion.html)  **
  - **Description:** Grants permission to delete a service template version
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTemplateSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteTemplateSyncConfig.html)  **
  - **Description:** Grants permission to delete a TemplateSyncConfig
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccountRoles](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetAccountRoles.html)  **
  - **Description:** Grants permission to get account roles. DEPRECATED - use GetAccountSettings instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountSettings](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to describe the account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetComponent](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetComponent.html)  **
  - **Description:** Grants permission to describe a component
  - **Resource types (\*required):** [component\*](#list_proton-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeployment](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to describe a deployment
  - **Resource types (\*required):** [deployment\*](#list_proton-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to describe an environment
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentAccountConnection](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironmentAccountConnection.html)  **
  - **Description:** Grants permission to describe an environment account connection
  - **Resource types (\*required):** [environment-account-connection\*](#list_proton-resource-environment-account-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironmentTemplate.html)  **
  - **Description:** Grants permission to describe an environment template
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironmentTemplateMajorVersion.html)  **
  - **Description:** Grants permission to get an environment template major version. DEPRECATED - use GetEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironmentTemplateMinorVersion.html)  **
  - **Description:** Grants permission to get an environment template minor version. DEPRECATED - use GetEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetEnvironmentTemplateVersion.html)  **
  - **Description:** Grants permission to describe an environment template version
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepository](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetRepository.html)  **
  - **Description:** Grants permission to describe a repository
  - **Resource types (\*required):** [repository\*](#list_proton-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepositorySyncStatus](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetRepositorySyncStatus.html)  **
  - **Description:** Grants permission to get the latest sync status for a repository
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceTemplateVersionStatusCounts](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetResourceTemplateVersionStatusCounts.html)  **
  - **Description:** Grants permission to list resource template version status counts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcesSummary](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetResourcesSummary.html)  **
  - **Description:** Grants permission to get resources summary
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetService.html)  **
  - **Description:** Grants permission to describe a service
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceInstance](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceInstance.html)  **
  - **Description:** Grants permission to describe a service instance
  - **Resource types (\*required):** [service-instance\*](#list_proton-resource-service-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceInstanceSyncStatus](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceInstanceSyncStatus.html)  **
  - **Description:** Grants permission to describe the sync status of a service instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceSyncBlockerSummary](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceSyncBlockerSummary.html)  **
  - **Description:** Grants permission to describe service sync blockers on a service or service instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceSyncConfig.html)  **
  - **Description:** Grants permission to describe a service sync config
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceTemplate.html)  **
  - **Description:** Grants permission to describe a service template
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceTemplateMajorVersion.html)  **
  - **Description:** Grants permission to get a service template major version. DEPRECATED - use GetServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceTemplateMinorVersion.html)  **
  - **Description:** Grants permission to get a service template minor version. DEPRECATED - use GetServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetServiceTemplateVersion.html)  **
  - **Description:** Grants permission to describe a service template version
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplateSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetTemplateSyncConfig.html)  **
  - **Description:** Grants permission to describe a TemplateSyncConfig
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTemplateSyncStatus](https://docs.aws.amazon.com/proton/latest/APIReference/API_GetTemplateSyncStatus.html)  **
  - **Description:** Grants permission to describe the sync status of a template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListComponentOutputs](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListComponentOutputs.html)  **
  - **Description:** Grants permission to list component outputs
  - **Resource types (\*required):** [component\*](#list_proton-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deployment](#list_proton-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComponentProvisionedResources](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListComponentProvisionedResources.html)  **
  - **Description:** Grants permission to list component provisioned resources
  - **Resource types (\*required):** [component\*](#list_proton-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComponents](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListComponents.html)  **
  - **Description:** Grants permission to list components
  - **Resource types (\*required):** [environment](#list_proton-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service](#list_proton-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-instance](#list_proton-resource-service-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeployments](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListDeployments.html)  **
  - **Description:** Grants permission to list deployments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironmentAccountConnections](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentAccountConnections.html)  **
  - **Description:** Grants permission to list environment account connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironmentOutputs](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentOutputs.html)  **
  - **Description:** Grants permission to list environment outputs
  - **Resource types (\*required):** [deployment](#list_proton-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentProvisionedResources](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentProvisionedResources.html)  **
  - **Description:** Grants permission to list environment provisioned resources
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentTemplateMajorVersions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentTemplateMajorVersions.html)  **
  - **Description:** Grants permission to list environment template major versions. DEPRECATED - use ListEnvironmentTemplateVersions instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentTemplateMinorVersions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentTemplateMinorVersions.html)  **
  - **Description:** Grants permission to list an environment template minor versions. DEPRECATED - use ListEnvironmentTemplateVersions instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentTemplateVersions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentTemplateVersions.html)  **
  - **Description:** Grants permission to list environment template versions
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentTemplates](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironmentTemplates.html)  **
  - **Description:** Grants permission to list environment templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositories](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListRepositories.html)  **
  - **Description:** Grants permission to list repositories
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositorySyncDefinitions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListRepositorySyncDefinitions.html)  **
  - **Description:** Grants permission to list repository sync definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServiceInstanceOutputs](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceInstanceOutputs.html)  **
  - **Description:** Grants permission to list service instance outputs
  - **Resource types (\*required):** [deployment](#list_proton-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service\*](#list_proton-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-instance\*](#list_proton-resource-service-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceInstanceProvisionedResources](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceInstanceProvisionedResources.html)  **
  - **Description:** Grants permission to list service instance provisioned resources
  - **Resource types (\*required):** [service\*](#list_proton-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-instance\*](#list_proton-resource-service-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceInstances](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceInstances.html)  **
  - **Description:** Grants permission to list service instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServicePipelineOutputs](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServicePipelineOutputs.html)  **
  - **Description:** Grants permission to list service pipeline outputs
  - **Resource types (\*required):** [deployment](#list_proton-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service\*](#list_proton-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServicePipelineProvisionedResources](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServicePipelineProvisionedResources.html)  **
  - **Description:** Grants permission to list service pipeline provisioned resources
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceTemplateMajorVersions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceTemplateMajorVersions.html)  **
  - **Description:** Grants permission to list service template major versions. DEPRECATED - use ListServiceTemplateVersions instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceTemplateMinorVersions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceTemplateMinorVersions.html)  **
  - **Description:** Grants permission to list service template minor versions. DEPRECATED - use ListServiceTemplateVersions instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceTemplateVersions](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceTemplateVersions.html)  **
  - **Description:** Grants permission to list service template versions
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServiceTemplates](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServiceTemplates.html)  **
  - **Description:** Grants permission to list service templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to list services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/proton/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags of a resource
  - **Resource types (\*required):** [component](#list_proton-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment](#list_proton-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment-account-connection](#list_proton-resource-environment-account-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment-template](#list_proton-resource-environment-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment-template-major-version](#list_proton-resource-environment-template-major-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment-template-minor-version](#list_proton-resource-environment-template-minor-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment-template-version](#list_proton-resource-environment-template-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [repository](#list_proton-resource-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service](#list_proton-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-instance](#list_proton-resource-service-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-template](#list_proton-resource-service-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-template-major-version](#list_proton-resource-service-template-major-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-template-minor-version](#list_proton-resource-service-template-minor-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-template-version](#list_proton-resource-service-template-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [NotifyResourceDeploymentStatusChange](https://docs.aws.amazon.com/proton/latest/APIReference/API_NotifyResourceDeploymentStatusChange.html)  **
  - **Description:** Grants permission to notify Proton of resource deployment status changes
  - **Resource types (\*required):** [environment](#list_proton-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-instance](#list_proton-resource-service-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectEnvironmentAccountConnection](https://docs.aws.amazon.com/proton/latest/APIReference/API_RejectEnvironmentAccountConnection.html)  **
  - **Description:** Grants permission to reject an environment account connection request from another environment account
  - **Resource types (\*required):** [environment-account-connection\*](#list_proton-resource-environment-account-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/proton/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [component](#list_proton-resource-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment](#list_proton-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-account-connection](#list_proton-resource-environment-account-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template](#list_proton-resource-environment-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template-major-version](#list_proton-resource-environment-template-major-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template-minor-version](#list_proton-resource-environment-template-minor-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template-version](#list_proton-resource-environment-template-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [repository](#list_proton-resource-repository) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_proton-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-instance](#list_proton-resource-service-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template](#list_proton-resource-service-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template-major-version](#list_proton-resource-service-template-major-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template-minor-version](#list_proton-resource-service-template-minor-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template-version](#list_proton-resource-service-template-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_proton-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/proton/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [component](#list_proton-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment](#list_proton-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-account-connection](#list_proton-resource-environment-account-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template](#list_proton-resource-environment-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template-major-version](#list_proton-resource-environment-template-major-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template-minor-version](#list_proton-resource-environment-template-minor-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [environment-template-version](#list_proton-resource-environment-template-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [repository](#list_proton-resource-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_proton-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-instance](#list_proton-resource-service-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template](#list_proton-resource-service-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template-major-version](#list_proton-resource-service-template-major-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template-minor-version](#list_proton-resource-service-template-minor-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Resource types (\*required):** [service-template-version](#list_proton-resource-service-template-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_proton-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountRoles](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateAccountRoles.html)  **
  - **Description:** Grants permission to update account roles. DEPRECATED - use UpdateAccountSettings instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update the account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateComponent](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateComponent.html)  **
  - **Description:** Grants permission to update component
  - **Resource types (\*required):** [component\*](#list_proton-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update an environment
  - **Resource types (\*required):** [environment\*](#list_proton-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:EnvironmentTemplate](#list_proton-proton_EnvironmentTemplate)
  - **Access level:** Write

- **   [UpdateEnvironmentAccountConnection](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentAccountConnection.html)  **
  - **Description:** Grants permission to update an environment account connection
  - **Resource types (\*required):** [environment-account-connection\*](#list_proton-resource-environment-account-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironmentTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentTemplate.html)  **
  - **Description:** Grants permission to update an environment template
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironmentTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentTemplateMajorVersion.html)  **
  - **Description:** Grants permission to update an environment template major version. DEPRECATED - use UpdateEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironmentTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentTemplateMinorVersion.html)  **
  - **Description:** Grants permission to update an environment template minor version. DEPRECATED - use UpdateEnvironmentTemplateVersion instead
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironmentTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentTemplateVersion.html)  **
  - **Description:** Grants permission to update an environment template version
  - **Resource types (\*required):** [environment-template\*](#list_proton-resource-environment-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateService](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateService.html)  **
  - **Description:** Grants permission to update a service
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [UpdateServiceInstance](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceInstance.html)  **
  - **Description:** Grants permission to update a service instance
  - **Resource types (\*required):** [service-instance\*](#list_proton-resource-service-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [UpdateServicePipeline](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServicePipeline.html)  **
  - **Description:** Grants permission to update a service pipeline
  - **Resource types (\*required):** [service\*](#list_proton-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)<br />[proton:ServiceTemplate](#list_proton-proton_ServiceTemplate)
  - **Access level:** Write

- **   [UpdateServiceSyncBlocker](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceSyncBlocker.html)  **
  - **Description:** Grants permission to update a service sync blocker
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateServiceSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceSyncConfig.html)  **
  - **Description:** Grants permission to update a service sync config
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateServiceTemplate](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceTemplate.html)  **
  - **Description:** Grants permission to update a service template
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceTemplateMajorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceTemplateMajorVersion.html)  **
  - **Description:** Grants permission to update a service template major version. DEPRECATED - use UpdateServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceTemplateMinorVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceTemplateMinorVersion.html)  **
  - **Description:** Grants permission to create a service template minor version. DEPRECATED - use UpdateServiceTemplateVersion instead
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceTemplateVersion](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceTemplateVersion.html)  **
  - **Description:** Grants permission to update a service template version
  - **Resource types (\*required):** [service-template\*](#list_proton-resource-service-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTemplateSyncConfig](https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateTemplateSyncConfig.html)  **
  - **Description:** Grants permission to update a TemplateSyncConfig
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Proton
<a name="list_proton-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [component](https://docs.aws.amazon.com/proton/latest/adminguide/ag-components.html)  | arn:${Partition}:proton:${Region}:${Account}:component/${Id} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [deployment](https://docs.aws.amazon.com/proton/latest/adminguide/ag-deployments.html)  | arn:${Partition}:proton:${Region}:${Account}:deployment/${Id} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [environment](https://docs.aws.amazon.com/proton/latest/adminguide/ag-environments.html)  | arn:${Partition}:proton:${Region}:${Account}:environment/${Name} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [environment-account-connection](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-account-connections.html)  | arn:${Partition}:proton:${Region}:${Account}:environment-account-connection/${Id} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [environment-template](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:environment-template/${Name} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [environment-template-major-version](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:environment-template/${TemplateName}:${MajorVersionId} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [environment-template-minor-version](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:environment-template/${TemplateName}:${MajorVersionId}.${MinorVersionId} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [environment-template-version](https://docs.aws.amazon.com/proton/latest/adminguide/ag-env-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:environment-template/${TemplateName}:${MajorVersion}.${MinorVersion} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [repository](https://docs.aws.amazon.com/proton/latest/adminguide/ag-repositories.html)  | arn:${Partition}:proton:${Region}:${Account}:repository/${Provider}:${Name} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/proton/latest/adminguide/ag-services.html)  | arn:${Partition}:proton:${Region}:${Account}:service/${Name} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [service-instance](https://docs.aws.amazon.com/proton/latest/adminguide/ag-services.html)  | arn:${Partition}:proton:${Region}:${Account}:service/${ServiceName}/service-instance/${Name} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [service-template](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:service-template/${Name} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [service-template-major-version](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:service-template/${TemplateName}:${MajorVersionId} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [service-template-minor-version](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:service-template/${TemplateName}:${MajorVersionId}.${MinorVersionId} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 
|  [service-template-version](https://docs.aws.amazon.com/proton/latest/adminguide/managing-svc-templates.html)  | arn:${Partition}:proton:${Region}:${Account}:service-template/${TemplateName}:${MajorVersion}.${MinorVersion} | [aws:ResourceTag/${TagKey}](#list_proton-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Proton
<a name="list_proton-policy-keys"></a>

AWS Proton defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 
|   [proton:EnvironmentTemplate](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by specified environment template related to resource | String | 
|   [proton:ServiceTemplate](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by specified service template related to resource | String | 