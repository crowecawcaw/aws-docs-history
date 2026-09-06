

# Actions, resources, and condition keys for AWS IoT Greengrass
<a name="list_greengrass"></a>

AWS IoT Greengrass (service prefix: `greengrass`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/greengrass/v1/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/greengrass/v1/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/greengrass/v1/developerguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/greengrass/greengrass.json) for this service.

**Topics**
+ [API operations defined by AWS IoT Greengrass](#list_greengrass-operations)
+ [Actions defined by AWS IoT Greengrass](#list_greengrass-actions-as-permissions)
+ [Resource types defined by AWS IoT Greengrass](#list_greengrass-resources-for-iam-policies)
+ [Condition keys for AWS IoT Greengrass](#list_greengrass-policy-keys)

## API operations defined by AWS IoT Greengrass
<a name="list_greengrass-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_greengrass-actions-as-permissions).




- **   AssociateRoleToGroup  **
  - **IAM action:**  [greengrass:AssociateRoleToGroup](#list_greengrass-action-AssociateRoleToGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** greengrass.amazonaws.com / **Access level:** Write

- **   AssociateServiceRoleToAccount  **
  - **IAM action:**  [greengrass:AssociateServiceRoleToAccount](#list_greengrass-action-AssociateServiceRoleToAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** greengrass.amazonaws.com / **Access level:** Write

- **   CreateConnectorDefinition  **
  - **IAM action:**  [greengrass:CreateConnectorDefinition](#list_greengrass-action-CreateConnectorDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnectorDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateConnectorDefinitionVersion](#list_greengrass-action-CreateConnectorDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCoreDefinition  **
  - **IAM action:**  [greengrass:CreateCoreDefinition](#list_greengrass-action-CreateCoreDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCoreDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateCoreDefinitionVersion](#list_greengrass-action-CreateCoreDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDeployment  **
  - **IAM action:**  [greengrass:CreateDeployment](#list_greengrass-action-CreateDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDeviceDefinition  **
  - **IAM action:**  [greengrass:CreateDeviceDefinition](#list_greengrass-action-CreateDeviceDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDeviceDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateDeviceDefinitionVersion](#list_greengrass-action-CreateDeviceDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFunctionDefinition  **
  - **IAM action:**  [greengrass:CreateFunctionDefinition](#list_greengrass-action-CreateFunctionDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFunctionDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateFunctionDefinitionVersion](#list_greengrass-action-CreateFunctionDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGroup  **
  - **IAM action:**  [greengrass:CreateGroup](#list_greengrass-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGroupCertificateAuthority  **
  - **IAM action:**  [greengrass:CreateGroupCertificateAuthority](#list_greengrass-action-CreateGroupCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGroupVersion  **
  - **IAM action:**  [greengrass:CreateGroupVersion](#list_greengrass-action-CreateGroupVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLoggerDefinition  **
  - **IAM action:**  [greengrass:CreateLoggerDefinition](#list_greengrass-action-CreateLoggerDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLoggerDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateLoggerDefinitionVersion](#list_greengrass-action-CreateLoggerDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResourceDefinition  **
  - **IAM action:**  [greengrass:CreateResourceDefinition](#list_greengrass-action-CreateResourceDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateResourceDefinitionVersion](#list_greengrass-action-CreateResourceDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSoftwareUpdateJob  **
  - **IAM action:**  [greengrass:CreateSoftwareUpdateJob](#list_greengrass-action-CreateSoftwareUpdateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** greengrass.amazonaws.com / **Access level:** Write

- **   CreateSubscriptionDefinition  **
  - **IAM action:**  [greengrass:CreateSubscriptionDefinition](#list_greengrass-action-CreateSubscriptionDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSubscriptionDefinitionVersion  **
  - **IAM action:**  [greengrass:CreateSubscriptionDefinitionVersion](#list_greengrass-action-CreateSubscriptionDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectorDefinition  **
  - **IAM action:**  [greengrass:DeleteConnectorDefinition](#list_greengrass-action-DeleteConnectorDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCoreDefinition  **
  - **IAM action:**  [greengrass:DeleteCoreDefinition](#list_greengrass-action-DeleteCoreDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeviceDefinition  **
  - **IAM action:**  [greengrass:DeleteDeviceDefinition](#list_greengrass-action-DeleteDeviceDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunctionDefinition  **
  - **IAM action:**  [greengrass:DeleteFunctionDefinition](#list_greengrass-action-DeleteFunctionDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGroup  **
  - **IAM action:**  [greengrass:DeleteGroup](#list_greengrass-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLoggerDefinition  **
  - **IAM action:**  [greengrass:DeleteLoggerDefinition](#list_greengrass-action-DeleteLoggerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceDefinition  **
  - **IAM action:**  [greengrass:DeleteResourceDefinition](#list_greengrass-action-DeleteResourceDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriptionDefinition  **
  - **IAM action:**  [greengrass:DeleteSubscriptionDefinition](#list_greengrass-action-DeleteSubscriptionDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateRoleFromGroup  **
  - **IAM action:**  [greengrass:DisassociateRoleFromGroup](#list_greengrass-action-DisassociateRoleFromGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateServiceRoleFromAccount  **
  - **IAM action:**  [greengrass:DisassociateServiceRoleFromAccount](#list_greengrass-action-DisassociateServiceRoleFromAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAssociatedRole  **
  - **IAM action:**  [greengrass:GetAssociatedRole](#list_greengrass-action-GetAssociatedRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBulkDeploymentStatus  **
  - **IAM action:**  [greengrass:GetBulkDeploymentStatus](#list_greengrass-action-GetBulkDeploymentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectivityInfo  **
  - **IAM action:**  [greengrass:GetConnectivityInfo](#list_greengrass-action-GetConnectivityInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectorDefinition  **
  - **IAM action:**  [greengrass:GetConnectorDefinition](#list_greengrass-action-GetConnectorDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectorDefinitionVersion  **
  - **IAM action:**  [greengrass:GetConnectorDefinitionVersion](#list_greengrass-action-GetConnectorDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoreDefinition  **
  - **IAM action:**  [greengrass:GetCoreDefinition](#list_greengrass-action-GetCoreDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoreDefinitionVersion  **
  - **IAM action:**  [greengrass:GetCoreDefinitionVersion](#list_greengrass-action-GetCoreDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeploymentStatus  **
  - **IAM action:**  [greengrass:GetDeploymentStatus](#list_greengrass-action-GetDeploymentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeviceDefinition  **
  - **IAM action:**  [greengrass:GetDeviceDefinition](#list_greengrass-action-GetDeviceDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeviceDefinitionVersion  **
  - **IAM action:**  [greengrass:GetDeviceDefinitionVersion](#list_greengrass-action-GetDeviceDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionDefinition  **
  - **IAM action:**  [greengrass:GetFunctionDefinition](#list_greengrass-action-GetFunctionDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionDefinitionVersion  **
  - **IAM action:**  [greengrass:GetFunctionDefinitionVersion](#list_greengrass-action-GetFunctionDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **IAM action:**  [greengrass:GetGroup](#list_greengrass-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupCertificateAuthority  **
  - **IAM action:**  [greengrass:GetGroupCertificateAuthority](#list_greengrass-action-GetGroupCertificateAuthority) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupCertificateConfiguration  **
  - **IAM action:**  [greengrass:GetGroupCertificateConfiguration](#list_greengrass-action-GetGroupCertificateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupVersion  **
  - **IAM action:**  [greengrass:GetGroupVersion](#list_greengrass-action-GetGroupVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggerDefinition  **
  - **IAM action:**  [greengrass:GetLoggerDefinition](#list_greengrass-action-GetLoggerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLoggerDefinitionVersion  **
  - **IAM action:**  [greengrass:GetLoggerDefinitionVersion](#list_greengrass-action-GetLoggerDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceDefinition  **
  - **IAM action:**  [greengrass:GetResourceDefinition](#list_greengrass-action-GetResourceDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceDefinitionVersion  **
  - **IAM action:**  [greengrass:GetResourceDefinitionVersion](#list_greengrass-action-GetResourceDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceRoleForAccount  **
  - **IAM action:**  [greengrass:GetServiceRoleForAccount](#list_greengrass-action-GetServiceRoleForAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriptionDefinition  **
  - **IAM action:**  [greengrass:GetSubscriptionDefinition](#list_greengrass-action-GetSubscriptionDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriptionDefinitionVersion  **
  - **IAM action:**  [greengrass:GetSubscriptionDefinitionVersion](#list_greengrass-action-GetSubscriptionDefinitionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetThingRuntimeConfiguration  **
  - **IAM action:**  [greengrass:GetThingRuntimeConfiguration](#list_greengrass-action-GetThingRuntimeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBulkDeploymentDetailedReports  **
  - **IAM action:**  [greengrass:ListBulkDeploymentDetailedReports](#list_greengrass-action-ListBulkDeploymentDetailedReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBulkDeployments  **
  - **IAM action:**  [greengrass:ListBulkDeployments](#list_greengrass-action-ListBulkDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectorDefinitionVersions  **
  - **IAM action:**  [greengrass:ListConnectorDefinitionVersions](#list_greengrass-action-ListConnectorDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectorDefinitions  **
  - **IAM action:**  [greengrass:ListConnectorDefinitions](#list_greengrass-action-ListConnectorDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreDefinitionVersions  **
  - **IAM action:**  [greengrass:ListCoreDefinitionVersions](#list_greengrass-action-ListCoreDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreDefinitions  **
  - **IAM action:**  [greengrass:ListCoreDefinitions](#list_greengrass-action-ListCoreDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeployments  **
  - **IAM action:**  [greengrass:ListDeployments](#list_greengrass-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeviceDefinitionVersions  **
  - **IAM action:**  [greengrass:ListDeviceDefinitionVersions](#list_greengrass-action-ListDeviceDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeviceDefinitions  **
  - **IAM action:**  [greengrass:ListDeviceDefinitions](#list_greengrass-action-ListDeviceDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctionDefinitionVersions  **
  - **IAM action:**  [greengrass:ListFunctionDefinitionVersions](#list_greengrass-action-ListFunctionDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctionDefinitions  **
  - **IAM action:**  [greengrass:ListFunctionDefinitions](#list_greengrass-action-ListFunctionDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupCertificateAuthorities  **
  - **IAM action:**  [greengrass:ListGroupCertificateAuthorities](#list_greengrass-action-ListGroupCertificateAuthorities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupVersions  **
  - **IAM action:**  [greengrass:ListGroupVersions](#list_greengrass-action-ListGroupVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **IAM action:**  [greengrass:ListGroups](#list_greengrass-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLoggerDefinitionVersions  **
  - **IAM action:**  [greengrass:ListLoggerDefinitionVersions](#list_greengrass-action-ListLoggerDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLoggerDefinitions  **
  - **IAM action:**  [greengrass:ListLoggerDefinitions](#list_greengrass-action-ListLoggerDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceDefinitionVersions  **
  - **IAM action:**  [greengrass:ListResourceDefinitionVersions](#list_greengrass-action-ListResourceDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceDefinitions  **
  - **IAM action:**  [greengrass:ListResourceDefinitions](#list_greengrass-action-ListResourceDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptionDefinitionVersions  **
  - **IAM action:**  [greengrass:ListSubscriptionDefinitionVersions](#list_greengrass-action-ListSubscriptionDefinitionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptionDefinitions  **
  - **IAM action:**  [greengrass:ListSubscriptionDefinitions](#list_greengrass-action-ListSubscriptionDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [greengrass:ListTagsForResource](#list_greengrass-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResetDeployments  **
  - **IAM action:**  [greengrass:ResetDeployments](#list_greengrass-action-ResetDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBulkDeployment  **
  - **IAM action:**  [greengrass:StartBulkDeployment](#list_greengrass-action-StartBulkDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** greengrass.amazonaws.com / **Access level:** Write

- **   StopBulkDeployment  **
  - **IAM action:**  [greengrass:StopBulkDeployment](#list_greengrass-action-StopBulkDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [greengrass:TagResource](#list_greengrass-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [greengrass:UntagResource](#list_greengrass-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnectivityInfo  **
  - **IAM action:**  [greengrass:UpdateConnectivityInfo](#list_greengrass-action-UpdateConnectivityInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectorDefinition  **
  - **IAM action:**  [greengrass:UpdateConnectorDefinition](#list_greengrass-action-UpdateConnectorDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCoreDefinition  **
  - **IAM action:**  [greengrass:UpdateCoreDefinition](#list_greengrass-action-UpdateCoreDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDeviceDefinition  **
  - **IAM action:**  [greengrass:UpdateDeviceDefinition](#list_greengrass-action-UpdateDeviceDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFunctionDefinition  **
  - **IAM action:**  [greengrass:UpdateFunctionDefinition](#list_greengrass-action-UpdateFunctionDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGroup  **
  - **IAM action:**  [greengrass:UpdateGroup](#list_greengrass-action-UpdateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGroupCertificateConfiguration  **
  - **IAM action:**  [greengrass:UpdateGroupCertificateConfiguration](#list_greengrass-action-UpdateGroupCertificateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLoggerDefinition  **
  - **IAM action:**  [greengrass:UpdateLoggerDefinition](#list_greengrass-action-UpdateLoggerDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceDefinition  **
  - **IAM action:**  [greengrass:UpdateResourceDefinition](#list_greengrass-action-UpdateResourceDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriptionDefinition  **
  - **IAM action:**  [greengrass:UpdateSubscriptionDefinition](#list_greengrass-action-UpdateSubscriptionDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThingRuntimeConfiguration  **
  - **IAM action:**  [greengrass:UpdateThingRuntimeConfiguration](#list_greengrass-action-UpdateThingRuntimeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT Greengrass
<a name="list_greengrass-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateRoleToGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/associateroletogroup-put.html)  **
  - **Description:** Grants permission to associate a role with a group. The role's permissions must allow Greengrass core Lambda functions and connectors to perform actions in other AWS services
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateServiceRoleToAccount](https://docs.aws.amazon.com/greengrass/v1/apireference/associateserviceroletoaccount-put.html)  **
  - **Description:** Grants permission to associate a role with your account. AWS IoT Greengrass uses this role to access your Lambda functions and AWS IoT resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [CreateConnectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createconnectordefinition-post.html)  **
  - **Description:** Grants permission to create a connector definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createconnectordefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing connector definition
  - **Resource types (\*required):** [connectorDefinition\*](#list_greengrass-resource-connectorDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCoreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createcoredefinition-post.html)  **
  - **Description:** Grants permission to create a core definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCoreDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createcoredefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing core definition. Greengrass groups must each contain exactly one Greengrass core
  - **Resource types (\*required):** [coreDefinition\*](#list_greengrass-resource-coreDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/greengrass/v1/apireference/createdeployment-post.html)  **
  - **Description:** Grants permission to create a deployment
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createdevicedefinition-post.html)  **
  - **Description:** Grants permission to create a device definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeviceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createdevicedefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing device definition
  - **Resource types (\*required):** [deviceDefinition\*](#list_greengrass-resource-deviceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFunctionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createfunctiondefinition-post.html)  **
  - **Description:** Grants permission to create a Lambda function definition to be used in a group that contains a list of Lambda functions and their configurations
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFunctionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createfunctiondefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing Lambda function definition
  - **Resource types (\*required):** [functionDefinition\*](#list_greengrass-resource-functionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/creategroup-post.html)  **
  - **Description:** Grants permission to create a group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGroupCertificateAuthority](https://docs.aws.amazon.com/greengrass/v1/apireference/creategroupcertificateauthority-post.html)  **
  - **Description:** Grants permission to create a CA for the group, or rotate the existing CA
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGroupVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/creategroupversion-post.html)  **
  - **Description:** Grants permission to create a version of a group that has already been defined
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLoggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createloggerdefinition-post.html)  **
  - **Description:** Grants permission to create a logger definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLoggerDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createloggerdefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing logger definition
  - **Resource types (\*required):** [loggerDefinition\*](#list_greengrass-resource-loggerDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateResourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createresourcedefinition-post.html)  **
  - **Description:** Grants permission to create a resource definition that contains a list of resources to be used in a group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResourceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createresourcedefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing resource definition
  - **Resource types (\*required):** [resourceDefinition\*](#list_greengrass-resource-resourceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSoftwareUpdateJob](https://docs.aws.amazon.com/greengrass/v1/apireference/createsoftwareupdatejob-post.html)  **
  - **Description:** Grants permission to create an AWS IoT job that will trigger your Greengrass cores to update the software they are running
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSubscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/createsubscriptiondefinition-post.html)  **
  - **Description:** Grants permission to create a subscription definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubscriptionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/createsubscriptiondefinitionversion-post.html)  **
  - **Description:** Grants permission to create a version of an existing subscription definition
  - **Resource types (\*required):** [subscriptionDefinition\*](#list_greengrass-resource-subscriptionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deleteconnectordefinition-delete.html)  **
  - **Description:** Grants permission to delete a connector definition
  - **Resource types (\*required):** [connectorDefinition\*](#list_greengrass-resource-connectorDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCoreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deletecoredefinition-delete.html)  **
  - **Description:** Grants permission to delete a core definition. Deleting a definition that is currently in use in a deployment affects future deployments
  - **Resource types (\*required):** [coreDefinition\*](#list_greengrass-resource-coreDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deletedevicedefinition-delete.html)  **
  - **Description:** Grants permission to delete a device definition. Deleting a definition that is currently in use in a deployment affects future deployments
  - **Resource types (\*required):** [deviceDefinition\*](#list_greengrass-resource-deviceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFunctionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deletefunctiondefinition-delete.html)  **
  - **Description:** Grants permission to delete a Lambda function definition. Deleting a definition that is currently in use in a deployment affects future deployments
  - **Resource types (\*required):** [functionDefinition\*](#list_greengrass-resource-functionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/deletegroup-delete.html)  **
  - **Description:** Grants permission to delete a group that is not currently in use in a deployment
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deleteloggerdefinition-delete.html)  **
  - **Description:** Grants permission to delete a logger definition. Deleting a definition that is currently in use in a deployment affects future deployments
  - **Resource types (\*required):** [loggerDefinition\*](#list_greengrass-resource-loggerDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deleteresourcedefinition-delete.html)  **
  - **Description:** Grants permission to delete a resource definition
  - **Resource types (\*required):** [resourceDefinition\*](#list_greengrass-resource-resourceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSubscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/deletesubscriptiondefinition-delete.html)  **
  - **Description:** Grants permission to delete a subscription definition. Deleting a definition that is currently in use in a deployment affects future deployments
  - **Resource types (\*required):** [subscriptionDefinition\*](#list_greengrass-resource-subscriptionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateRoleFromGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/disassociaterolefromgroup-delete.html)  **
  - **Description:** Grants permission to disassociate the role from a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateServiceRoleFromAccount](https://docs.aws.amazon.com/greengrass/v1/apireference/disassociateservicerolefromaccount-delete.html)  **
  - **Description:** Grants permission to disassociate the service role from an account. Without a service role, deployments will not work
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Discover](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-discover-api.html)  **
  - **Description:** Grants permission to retrieve information required to connect to a Greengrass core
  - **Resource types (\*required):** [thing\*](#list_greengrass-resource-thing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAssociatedRole](https://docs.aws.amazon.com/greengrass/v1/apireference/getassociatedrole-get.html)  **
  - **Description:** Grants permission to retrieve the role associated with a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBulkDeploymentStatus](https://docs.aws.amazon.com/greengrass/v1/apireference/getbulkdeploymentstatus-get.html)  **
  - **Description:** Grants permission to return the status of a bulk deployment
  - **Resource types (\*required):** [bulkDeployment\*](#list_greengrass-resource-bulkDeployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectivityInfo](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectivityinfo-get.html)  **
  - **Description:** Grants permission to retrieve the connectivity information for a core
  - **Resource types (\*required):** [connectivityInfo\*](#list_greengrass-resource-connectivityInfo)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectordefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a connector definition
  - **Resource types (\*required):** [connectorDefinition\*](#list_greengrass-resource-connectorDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectordefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a connector definition version
  - **Resource types (\*required):** [connectorDefinition\*](#list_greengrass-resource-connectorDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectorDefinitionVersion\*](#list_greengrass-resource-connectorDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetCoreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getcoredefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a core definition
  - **Resource types (\*required):** [coreDefinition\*](#list_greengrass-resource-coreDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCoreDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getcoredefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a core definition version
  - **Resource types (\*required):** [coreDefinition\*](#list_greengrass-resource-coreDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [coreDefinitionVersion\*](#list_greengrass-resource-coreDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetDeploymentStatus](https://docs.aws.amazon.com/greengrass/v1/apireference/getdeploymentstatus-get.html)  **
  - **Description:** Grants permission to return the status of a deployment
  - **Resource types (\*required):** [deployment\*](#list_greengrass-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getdevicedefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a device definition
  - **Resource types (\*required):** [deviceDefinition\*](#list_greengrass-resource-deviceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getdevicedefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a device definition version
  - **Resource types (\*required):** [deviceDefinition\*](#list_greengrass-resource-deviceDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deviceDefinitionVersion\*](#list_greengrass-resource-deviceDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetFunctionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getfunctiondefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a Lambda function definition, such as its creation time and latest version
  - **Resource types (\*required):** [functionDefinition\*](#list_greengrass-resource-functionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getfunctiondefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a Lambda function definition version, such as which Lambda functions are included in the version and their configurations
  - **Resource types (\*required):** [functionDefinition\*](#list_greengrass-resource-functionDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [functionDefinitionVersion\*](#list_greengrass-resource-functionDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html)  **
  - **Description:** Grants permission to retrieve information about a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroupCertificateAuthority](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupcertificateauthority-get.html)  **
  - **Description:** Grants permission to return the public key of the CA associated with a group
  - **Resource types (\*required):** [certificateAuthority\*](#list_greengrass-resource-certificateAuthority) / **Condition keys:**  
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroupCertificateConfiguration](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupcertificateconfiguration-get.html)  **
  - **Description:** Grants permission to retrieve the current configuration for the CA used by a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroupVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a group version
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [groupVersion\*](#list_greengrass-resource-groupVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetLoggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getloggerdefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a logger definition
  - **Resource types (\*required):** [loggerDefinition\*](#list_greengrass-resource-loggerDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLoggerDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getloggerdefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a logger definition version
  - **Resource types (\*required):** [loggerDefinition\*](#list_greengrass-resource-loggerDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [loggerDefinitionVersion\*](#list_greengrass-resource-loggerDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getresourcedefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a resource definition, such as its creation time and latest version
  - **Resource types (\*required):** [resourceDefinition\*](#list_greengrass-resource-resourceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getresourcedefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a resource definition version, such as which resources are included in the version
  - **Resource types (\*required):** [resourceDefinition\*](#list_greengrass-resource-resourceDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [resourceDefinitionVersion\*](#list_greengrass-resource-resourceDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceRoleForAccount](https://docs.aws.amazon.com/greengrass/v1/apireference/getserviceroleforaccount-get.html)  **
  - **Description:** Grants permission to retrieve the service role that is attached to an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getsubscriptiondefinition-get.html)  **
  - **Description:** Grants permission to retrieve information about a subscription definition
  - **Resource types (\*required):** [subscriptionDefinition\*](#list_greengrass-resource-subscriptionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSubscriptionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getsubscriptiondefinitionversion-get.html)  **
  - **Description:** Grants permission to retrieve information about a subscription definition version
  - **Resource types (\*required):** [subscriptionDefinition\*](#list_greengrass-resource-subscriptionDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subscriptionDefinitionVersion\*](#list_greengrass-resource-subscriptionDefinitionVersion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetThingRuntimeConfiguration](https://docs.aws.amazon.com/greengrass/v1/apireference/getthingruntimeconfiguration-get.html)  **
  - **Description:** Grants permission to retrieve runtime configuration of a thing
  - **Resource types (\*required):** [thingRuntimeConfig\*](#list_greengrass-resource-thingRuntimeConfig)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListBulkDeploymentDetailedReports](https://docs.aws.amazon.com/greengrass/v1/apireference/listbulkdeploymentdetailedreports-get.html)  **
  - **Description:** Grants permission to retrieve a paginated list of the deployments that have been started in a bulk deployment operation and their current deployment status
  - **Resource types (\*required):** [bulkDeployment\*](#list_greengrass-resource-bulkDeployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBulkDeployments](https://docs.aws.amazon.com/greengrass/v1/apireference/listbulkdeployments-get.html)  **
  - **Description:** Grants permission to retrieve a list of bulk deployments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectorDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listconnectordefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a connector definition
  - **Resource types (\*required):** [connectorDefinition\*](#list_greengrass-resource-connectorDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConnectorDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listconnectordefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of connector definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCoreDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listcoredefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a core definition
  - **Resource types (\*required):** [coreDefinition\*](#list_greengrass-resource-coreDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCoreDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listcoredefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of core definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeployments](https://docs.aws.amazon.com/greengrass/v1/apireference/listdeployments-get.html)  **
  - **Description:** Grants permission to retrieve a list of all deployments for a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeviceDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listdevicedefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a device definition
  - **Resource types (\*required):** [deviceDefinition\*](#list_greengrass-resource-deviceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeviceDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listdevicedefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of device definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFunctionDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listfunctiondefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a Lambda function definition
  - **Resource types (\*required):** [functionDefinition\*](#list_greengrass-resource-functionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFunctionDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listfunctiondefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of Lambda function definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroupCertificateAuthorities](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroupcertificateauthorities-get.html)  **
  - **Description:** Grants permission to retrieve a list of current CAs for a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroupVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroupversions-get.html)  **
  - **Description:** Grants permission to list the versions of a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html)  **
  - **Description:** Grants permission to retrieve a list of groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLoggerDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listloggerdefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a logger definition
  - **Resource types (\*required):** [loggerDefinition\*](#list_greengrass-resource-loggerDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLoggerDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listloggerdefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of logger definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listresourcedefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a resource definition
  - **Resource types (\*required):** [resourceDefinition\*](#list_greengrass-resource-resourceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResourceDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listresourcedefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of resource definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptionDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listsubscriptiondefinitionversions-get.html)  **
  - **Description:** Grants permission to list the versions of a subscription definition
  - **Resource types (\*required):** [subscriptionDefinition\*](#list_greengrass-resource-subscriptionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSubscriptionDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listsubscriptiondefinitions-get.html)  **
  - **Description:** Grants permission to retrieve a list of subscription definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/greengrass/v1/apireference/listtagsforresource-get.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [bulkDeployment](#list_greengrass-resource-bulkDeployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [connectorDefinition](#list_greengrass-resource-connectorDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [coreDefinition](#list_greengrass-resource-coreDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_greengrass-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [deviceDefinition](#list_greengrass-resource-deviceDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [functionDefinition](#list_greengrass-resource-functionDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [group](#list_greengrass-resource-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [loggerDefinition](#list_greengrass-resource-loggerDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [resourceDefinition](#list_greengrass-resource-resourceDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [subscriptionDefinition](#list_greengrass-resource-subscriptionDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Read

- **   [ResetDeployments](https://docs.aws.amazon.com/greengrass/v1/apireference/resetdeployments-post.html)  **
  - **Description:** Grants permission to reset a group's deployments
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBulkDeployment](https://docs.aws.amazon.com/greengrass/v1/apireference/startbulkdeployment-post.html)  **
  - **Description:** Grants permission to deploy multiple groups in one operation
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Write

- **   [StopBulkDeployment](https://docs.aws.amazon.com/greengrass/v1/apireference/stopbulkdeployment-put.html)  **
  - **Description:** Grants permission to stop the execution of a bulk deployment
  - **Resource types (\*required):** [bulkDeployment\*](#list_greengrass-resource-bulkDeployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/greengrass/v1/apireference/tagresource-post.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [bulkDeployment](#list_greengrass-resource-bulkDeployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [connectorDefinition](#list_greengrass-resource-connectorDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [coreDefinition](#list_greengrass-resource-coreDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_greengrass-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [deviceDefinition](#list_greengrass-resource-deviceDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [functionDefinition](#list_greengrass-resource-functionDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [group](#list_greengrass-resource-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [loggerDefinition](#list_greengrass-resource-loggerDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [resourceDefinition](#list_greengrass-resource-resourceDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [subscriptionDefinition](#list_greengrass-resource-subscriptionDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrass-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/greengrass/v1/apireference/untagresource-delete.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [bulkDeployment](#list_greengrass-resource-bulkDeployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [connectorDefinition](#list_greengrass-resource-connectorDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [coreDefinition](#list_greengrass-resource-coreDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_greengrass-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [deviceDefinition](#list_greengrass-resource-deviceDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [functionDefinition](#list_greengrass-resource-functionDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [group](#list_greengrass-resource-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [loggerDefinition](#list_greengrass-resource-loggerDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [resourceDefinition](#list_greengrass-resource-resourceDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Resource types (\*required):** [subscriptionDefinition](#list_greengrass-resource-subscriptionDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrass-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnectivityInfo](https://docs.aws.amazon.com/greengrass/v1/apireference/updateconnectivityinfo-put.html)  **
  - **Description:** Grants permission to update the connectivity information for a Greengrass core. Any devices that belong to the group that has this core will receive this information in order to find the location of the core and connect to it
  - **Resource types (\*required):** [connectivityInfo\*](#list_greengrass-resource-connectivityInfo)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updateconnectordefinition-put.html)  **
  - **Description:** Grants permission to update a connector definition
  - **Resource types (\*required):** [connectorDefinition\*](#list_greengrass-resource-connectorDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCoreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updatecoredefinition-put.html)  **
  - **Description:** Grants permission to update a core definition
  - **Resource types (\*required):** [coreDefinition\*](#list_greengrass-resource-coreDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updatedevicedefinition-put.html)  **
  - **Description:** Grants permission to update a device definition
  - **Resource types (\*required):** [deviceDefinition\*](#list_greengrass-resource-deviceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFunctionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updatefunctiondefinition-put.html)  **
  - **Description:** Grants permission to update a Lambda function definition
  - **Resource types (\*required):** [functionDefinition\*](#list_greengrass-resource-functionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/updategroup-put.html)  **
  - **Description:** Grants permission to update a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGroupCertificateConfiguration](https://docs.aws.amazon.com/greengrass/v1/apireference/updategroupcertificateconfiguration-put.html)  **
  - **Description:** Grants permission to update the certificate expiry time for a group
  - **Resource types (\*required):** [group\*](#list_greengrass-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLoggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updateloggerdefinition-put.html)  **
  - **Description:** Grants permission to update a logger definition
  - **Resource types (\*required):** [loggerDefinition\*](#list_greengrass-resource-loggerDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updateresourcedefinition-put.html)  **
  - **Description:** Grants permission to update a resource definition
  - **Resource types (\*required):** [resourceDefinition\*](#list_greengrass-resource-resourceDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/updatesubscriptiondefinition-put.html)  **
  - **Description:** Grants permission to update a subscription definition
  - **Resource types (\*required):** [subscriptionDefinition\*](#list_greengrass-resource-subscriptionDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThingRuntimeConfiguration](https://docs.aws.amazon.com/greengrass/v1/apireference/updatethingruntimeconfiguration-put.html)  **
  - **Description:** Grants permission to update runtime configuration of a thing
  - **Resource types (\*required):** [thingRuntimeConfig\*](#list_greengrass-resource-thingRuntimeConfig)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS IoT Greengrass
<a name="list_greengrass-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [bulkDeployment](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/bulk/deployments/${BulkDeploymentId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [certificateAuthority](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-sec.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/groups/${GroupId}/certificateauthorities/${CertificateAuthorityId} |   | 
|  [connectivityInfo](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectivityinfo.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/things/${ThingName}/connectivityInfo |   | 
|  [connectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connector.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/connectors/${ConnectorDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [connectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-connectordefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/connectors/${ConnectorDefinitionId}/versions/${VersionId} |   | 
|  [coreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-core.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/cores/${CoreDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [coreDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-coredefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/cores/${CoreDefinitionId}/versions/${VersionId} |   | 
|  [deployment](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-createdeploymentrequest.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/groups/${GroupId}/deployments/${DeploymentId}, arn:${Partition}:greengrass:${Region}:${Account}:deployments:${DeploymentId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [deviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-device.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/devices/${DeviceDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [deviceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-devicedefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/devices/${DeviceDefinitionId}/versions/${VersionId} |   | 
|  [functionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-function.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/functions/${FunctionDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [functionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functiondefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/functions/${FunctionDefinitionId}/versions/${VersionId} |   | 
|  [group](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupinformation.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/groups/${GroupId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [groupVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-groupversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/groups/${GroupId}/versions/${VersionId} |   | 
|  [loggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-logger.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/loggers/${LoggerDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [loggerDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-loggerdefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/loggers/${LoggerDefinitionId}/versions/${VersionId} |   | 
|  [resourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resource.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/resources/${ResourceDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [resourceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-resourcedefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/resources/${ResourceDefinitionId}/versions/${VersionId} |   | 
|  [subscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscription.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/subscriptions/${SubscriptionDefinitionId} | [aws:ResourceTag/${TagKey}](#list_greengrass-aws_ResourceTag___TagKey_) | 
|  [subscriptionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-subscriptiondefinitionversion.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/definition/subscriptions/${SubscriptionDefinitionId}/versions/${VersionId} |   | 
|  [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)  | arn:${Partition}:iot:${Region}:${Account}:thing/${ThingName} |   | 
|  [thingRuntimeConfig](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/things/${ThingName}/runtimeconfig |   | 

## Condition keys for AWS IoT Greengrass
<a name="list_greengrass-policy-keys"></a>

AWS IoT Greengrass defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the mandatory tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 