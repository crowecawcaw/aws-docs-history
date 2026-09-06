

# Actions, resources, and condition keys for AWS IoT Managed Integrations
<a name="list_iot-managed-integrations"></a>

AWS IoT Managed Integrations (service prefix: `iotmanagedintegrations`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iotmanagedintegrations/latest/devguide/what-is-managedintegrations.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iotmanagedintegrations/latest/devguide/what-is-managedintegrations.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotmanagedintegrations/iotmanagedintegrations.json) for this service.

**Topics**
+ [API operations defined by AWS IoT Managed Integrations](#list_iot-managed-integrations-operations)
+ [Actions defined by AWS IoT Managed Integrations](#list_iot-managed-integrations-actions-as-permissions)
+ [Resource types defined by AWS IoT Managed Integrations](#list_iot-managed-integrations-resources-for-iam-policies)
+ [Condition keys for AWS IoT Managed Integrations](#list_iot-managed-integrations-policy-keys)

## API operations defined by AWS IoT Managed Integrations
<a name="list_iot-managed-integrations-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iot-managed-integrations-actions-as-permissions).




- **   CreateAccountAssociation  **
  - **IAM action:**  [iotmanagedintegrations:CreateAccountAssociation](#list_iot-managed-integrations-action-CreateAccountAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotmanagedintegrations:TagResource](#list_iot-managed-integrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCloudConnector  **
  - **IAM action:**  [iotmanagedintegrations:CreateCloudConnector](#list_iot-managed-integrations-action-CreateCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectorDestination  **
  - **IAM action:**  [iotmanagedintegrations:CreateConnectorDestination](#list_iot-managed-integrations-action-CreateConnectorDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCredentialLocker  **
  - **IAM action:**  [iotmanagedintegrations:CreateCredentialLocker](#list_iot-managed-integrations-action-CreateCredentialLocker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotmanagedintegrations:TagResource](#list_iot-managed-integrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDestination  **
  - **IAM action:**  [iotmanagedintegrations:CreateDestination](#list_iot-managed-integrations-action-CreateDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateEventLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:CreateEventLogConfiguration](#list_iot-managed-integrations-action-CreateEventLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateManagedThing  **
  - **IAM action:**  [iotmanagedintegrations:CreateManagedThing](#list_iot-managed-integrations-action-CreateManagedThing)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotmanagedintegrations:TagResource](#list_iot-managed-integrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNotificationConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:CreateNotificationConfiguration](#list_iot-managed-integrations-action-CreateNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOtaTask  **
  - **IAM action:**  [iotmanagedintegrations:CreateOtaTask](#list_iot-managed-integrations-action-CreateOtaTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotmanagedintegrations:TagResource](#list_iot-managed-integrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOtaTaskConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:CreateOtaTaskConfiguration](#list_iot-managed-integrations-action-CreateOtaTaskConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProvisioningProfile  **
  - **IAM action:**  [iotmanagedintegrations:CreateProvisioningProfile](#list_iot-managed-integrations-action-CreateProvisioningProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotmanagedintegrations:TagResource](#list_iot-managed-integrations-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccountAssociation  **
  - **IAM action:**  [iotmanagedintegrations:DeleteAccountAssociation](#list_iot-managed-integrations-action-DeleteAccountAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudConnector  **
  - **IAM action:**  [iotmanagedintegrations:DeleteCloudConnector](#list_iot-managed-integrations-action-DeleteCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectorDestination  **
  - **IAM action:**  [iotmanagedintegrations:DeleteConnectorDestination](#list_iot-managed-integrations-action-DeleteConnectorDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCredentialLocker  **
  - **IAM action:**  [iotmanagedintegrations:DeleteCredentialLocker](#list_iot-managed-integrations-action-DeleteCredentialLocker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDestination  **
  - **IAM action:**  [iotmanagedintegrations:DeleteDestination](#list_iot-managed-integrations-action-DeleteDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:DeleteEventLogConfiguration](#list_iot-managed-integrations-action-DeleteEventLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteManagedThing  **
  - **IAM action:**  [iotmanagedintegrations:DeleteManagedThing](#list_iot-managed-integrations-action-DeleteManagedThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotificationConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:DeleteNotificationConfiguration](#list_iot-managed-integrations-action-DeleteNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOtaTask  **
  - **IAM action:**  [iotmanagedintegrations:DeleteOtaTask](#list_iot-managed-integrations-action-DeleteOtaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOtaTaskConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:DeleteOtaTaskConfiguration](#list_iot-managed-integrations-action-DeleteOtaTaskConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProvisioningProfile  **
  - **IAM action:**  [iotmanagedintegrations:DeleteProvisioningProfile](#list_iot-managed-integrations-action-DeleteProvisioningProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterAccountAssociation  **
  - **IAM action:**  [iotmanagedintegrations:DeregisterAccountAssociation](#list_iot-managed-integrations-action-DeregisterAccountAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountAssociation  **
  - **IAM action:**  [iotmanagedintegrations:GetAccountAssociation](#list_iot-managed-integrations-action-GetAccountAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudConnector  **
  - **IAM action:**  [iotmanagedintegrations:GetCloudConnector](#list_iot-managed-integrations-action-GetCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectorDestination  **
  - **IAM action:**  [iotmanagedintegrations:GetConnectorDestination](#list_iot-managed-integrations-action-GetConnectorDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCredentialLocker  **
  - **IAM action:**  [iotmanagedintegrations:GetCredentialLocker](#list_iot-managed-integrations-action-GetCredentialLocker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomEndpoint  **
  - **IAM action:**  [iotmanagedintegrations:GetCustomEndpoint](#list_iot-managed-integrations-action-GetCustomEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDefaultEncryptionConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:GetDefaultEncryptionConfiguration](#list_iot-managed-integrations-action-GetDefaultEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDestination  **
  - **IAM action:**  [iotmanagedintegrations:GetDestination](#list_iot-managed-integrations-action-GetDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeviceDiscovery  **
  - **IAM action:**  [iotmanagedintegrations:GetDeviceDiscovery](#list_iot-managed-integrations-action-GetDeviceDiscovery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:GetEventLogConfiguration](#list_iot-managed-integrations-action-GetEventLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHubConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:GetHubConfiguration](#list_iot-managed-integrations-action-GetHubConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedThing  **
  - **IAM action:**  [iotmanagedintegrations:GetManagedThing](#list_iot-managed-integrations-action-GetManagedThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedThingCapabilities  **
  - **IAM action:**  [iotmanagedintegrations:GetManagedThingCapabilities](#list_iot-managed-integrations-action-GetManagedThingCapabilities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedThingConnectivityData  **
  - **IAM action:**  [iotmanagedintegrations:GetManagedThingConnectivityData](#list_iot-managed-integrations-action-GetManagedThingConnectivityData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedThingMetaData  **
  - **IAM action:**  [iotmanagedintegrations:GetManagedThingMetaData](#list_iot-managed-integrations-action-GetManagedThingMetaData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedThingState  **
  - **IAM action:**  [iotmanagedintegrations:GetManagedThingState](#list_iot-managed-integrations-action-GetManagedThingState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotificationConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:GetNotificationConfiguration](#list_iot-managed-integrations-action-GetNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOtaTask  **
  - **IAM action:**  [iotmanagedintegrations:GetOtaTask](#list_iot-managed-integrations-action-GetOtaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOtaTaskConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:GetOtaTaskConfiguration](#list_iot-managed-integrations-action-GetOtaTaskConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProvisioningProfile  **
  - **IAM action:**  [iotmanagedintegrations:GetProvisioningProfile](#list_iot-managed-integrations-action-GetProvisioningProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRuntimeLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:GetRuntimeLogConfiguration](#list_iot-managed-integrations-action-GetRuntimeLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaVersion  **
  - **IAM action:**  [iotmanagedintegrations:GetSchemaVersion](#list_iot-managed-integrations-action-GetSchemaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountAssociations  **
  - **IAM action:**  [iotmanagedintegrations:ListAccountAssociations](#list_iot-managed-integrations-action-ListAccountAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudConnectors  **
  - **IAM action:**  [iotmanagedintegrations:ListCloudConnectors](#list_iot-managed-integrations-action-ListCloudConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectorDestinations  **
  - **IAM action:**  [iotmanagedintegrations:ListConnectorDestinations](#list_iot-managed-integrations-action-ListConnectorDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCredentialLockers  **
  - **IAM action:**  [iotmanagedintegrations:ListCredentialLockers](#list_iot-managed-integrations-action-ListCredentialLockers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDestinations  **
  - **IAM action:**  [iotmanagedintegrations:ListDestinations](#list_iot-managed-integrations-action-ListDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeviceDiscoveries  **
  - **IAM action:**  [iotmanagedintegrations:ListDeviceDiscoveries](#list_iot-managed-integrations-action-ListDeviceDiscoveries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDiscoveredDevices  **
  - **IAM action:**  [iotmanagedintegrations:ListDiscoveredDevices](#list_iot-managed-integrations-action-ListDiscoveredDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEventLogConfigurations  **
  - **IAM action:**  [iotmanagedintegrations:ListEventLogConfigurations](#list_iot-managed-integrations-action-ListEventLogConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListManagedThingAccountAssociations  **
  - **IAM action:**  [iotmanagedintegrations:ListManagedThingAccountAssociations](#list_iot-managed-integrations-action-ListManagedThingAccountAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedThingSchemas  **
  - **IAM action:**  [iotmanagedintegrations:ListManagedThingSchemas](#list_iot-managed-integrations-action-ListManagedThingSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListManagedThings  **
  - **IAM action:**  [iotmanagedintegrations:ListManagedThings](#list_iot-managed-integrations-action-ListManagedThings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotificationConfigurations  **
  - **IAM action:**  [iotmanagedintegrations:ListNotificationConfigurations](#list_iot-managed-integrations-action-ListNotificationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOtaTaskConfigurations  **
  - **IAM action:**  [iotmanagedintegrations:ListOtaTaskConfigurations](#list_iot-managed-integrations-action-ListOtaTaskConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOtaTaskExecutions  **
  - **IAM action:**  [iotmanagedintegrations:ListOtaTaskExecutions](#list_iot-managed-integrations-action-ListOtaTaskExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOtaTasks  **
  - **IAM action:**  [iotmanagedintegrations:ListOtaTasks](#list_iot-managed-integrations-action-ListOtaTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisioningProfiles  **
  - **IAM action:**  [iotmanagedintegrations:ListProvisioningProfiles](#list_iot-managed-integrations-action-ListProvisioningProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemaVersions  **
  - **IAM action:**  [iotmanagedintegrations:ListSchemaVersions](#list_iot-managed-integrations-action-ListSchemaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [iotmanagedintegrations:ListTagsForResource](#list_iot-managed-integrations-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutDefaultEncryptionConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:PutDefaultEncryptionConfiguration](#list_iot-managed-integrations-action-PutDefaultEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutHubConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:PutHubConfiguration](#list_iot-managed-integrations-action-PutHubConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRuntimeLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:PutRuntimeLogConfiguration](#list_iot-managed-integrations-action-PutRuntimeLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterAccountAssociation  **
  - **IAM action:**  [iotmanagedintegrations:RegisterAccountAssociation](#list_iot-managed-integrations-action-RegisterAccountAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterCustomEndpoint  **
  - **IAM action:**  [iotmanagedintegrations:RegisterCustomEndpoint](#list_iot-managed-integrations-action-RegisterCustomEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetRuntimeLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:ResetRuntimeLogConfiguration](#list_iot-managed-integrations-action-ResetRuntimeLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendConnectorEvent  **
  - **IAM action:**  [iotmanagedintegrations:SendConnectorEvent](#list_iot-managed-integrations-action-SendConnectorEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendManagedThingCommand  **
  - **IAM action:**  [iotmanagedintegrations:SendManagedThingCommand](#list_iot-managed-integrations-action-SendManagedThingCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAccountAssociationRefresh  **
  - **IAM action:**  [iotmanagedintegrations:StartAccountAssociationRefresh](#list_iot-managed-integrations-action-StartAccountAssociationRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDeviceDiscovery  **
  - **IAM action:**  [iotmanagedintegrations:StartDeviceDiscovery](#list_iot-managed-integrations-action-StartDeviceDiscovery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [iotmanagedintegrations:TagResource](#list_iot-managed-integrations-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [iotmanagedintegrations:UntagResource](#list_iot-managed-integrations-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountAssociation  **
  - **IAM action:**  [iotmanagedintegrations:UpdateAccountAssociation](#list_iot-managed-integrations-action-UpdateAccountAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCloudConnector  **
  - **IAM action:**  [iotmanagedintegrations:UpdateCloudConnector](#list_iot-managed-integrations-action-UpdateCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectorDestination  **
  - **IAM action:**  [iotmanagedintegrations:UpdateConnectorDestination](#list_iot-managed-integrations-action-UpdateConnectorDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDestination  **
  - **IAM action:**  [iotmanagedintegrations:UpdateDestination](#list_iot-managed-integrations-action-UpdateDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventLogConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:UpdateEventLogConfiguration](#list_iot-managed-integrations-action-UpdateEventLogConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateManagedThing  **
  - **IAM action:**  [iotmanagedintegrations:UpdateManagedThing](#list_iot-managed-integrations-action-UpdateManagedThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNotificationConfiguration  **
  - **IAM action:**  [iotmanagedintegrations:UpdateNotificationConfiguration](#list_iot-managed-integrations-action-UpdateNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOtaTask  **
  - **IAM action:**  [iotmanagedintegrations:UpdateOtaTask](#list_iot-managed-integrations-action-UpdateOtaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT Managed Integrations
<a name="list_iot-managed-integrations-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccountAssociation](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateAccountAssociation.html)  **
  - **Description:** Grants permission to create a new account association
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)<br />[iotmanagedintegrations:connectorDestinationId](#list_iot-managed-integrations-iotmanagedintegrations_connectorDestinationId)
  - **Access level:** Write

- **   [CreateCloudConnector](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateCloudConnector.html)  **
  - **Description:** Grants permission to create a new cloud connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateConnectorDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateConnectorDestination.html)  **
  - **Description:** Grants permission to create a new connector destination
  - **Resource types (\*required):** 
  - **Condition keys:** [iotmanagedintegrations:cloudConnectorId](#list_iot-managed-integrations-iotmanagedintegrations_cloudConnectorId)
  - **Access level:** Write

- **   [CreateCredentialLocker](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateCredentialLocker.html)  **
  - **Description:** Grants permission to create a product credential locker
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateDestination.html)  **
  - **Description:** Grants permission to create a new destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEventLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateEventLogConfiguration.html)  **
  - **Description:** Grants permission to create a new event configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateManagedThing](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateManagedThing.html)  **
  - **Description:** Grants permission to create a new managed thing
  - **Resource types (\*required):** [credential-locker](#list_iot-managed-integrations-resource-credential-locker)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNotificationConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateNotificationConfiguration.html)  **
  - **Description:** Grants permission to create a new notification configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOtaTask](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateOtaTask.html)  **
  - **Description:** Grants permission to create a new ota task
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOtaTaskConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateOtaTaskConfiguration.html)  **
  - **Description:** Grants permission to create a new ota task configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProvisioningProfile](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_CreateProvisioningProfile.html)  **
  - **Description:** Grants permission to create a new provisioning profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccountAssociation](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteAccountAssociation.html)  **
  - **Description:** Grants permission to delete an account association
  - **Resource types (\*required):** [account-association\*](#list_iot-managed-integrations-resource-account-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCloudConnector](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteCloudConnector.html)  **
  - **Description:** Grants permission to delete a cloud connector
  - **Resource types (\*required):** 
  - **Condition keys:** [iotmanagedintegrations:cloudConnectorId](#list_iot-managed-integrations-iotmanagedintegrations_cloudConnectorId)
  - **Access level:** Write

- **   [DeleteConnectorDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteConnectorDestination.html)  **
  - **Description:** Grants permission to delete a connector destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCredentialLocker](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteCredentialLocker.html)  **
  - **Description:** Grants permission to delete a credential locker
  - **Resource types (\*required):** [credential-locker\*](#list_iot-managed-integrations-resource-credential-locker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteDestination.html)  **
  - **Description:** Grants permission to delete destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEventLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteEventLogConfiguration.html)  **
  - **Description:** Grants permission to delete event log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteManagedThing](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteManagedThing.html)  **
  - **Description:** Grants permission to delete managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotificationConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteNotificationConfiguration.html)  **
  - **Description:** Grants permission to delete notification configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOtaTask](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteOtaTask.html)  **
  - **Description:** Grants permission to delete ota task
  - **Resource types (\*required):** [ota-task\*](#list_iot-managed-integrations-resource-ota-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOtaTaskConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteOtaTaskConfiguration.html)  **
  - **Description:** Grants permission to delete ota task configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProvisioningProfile](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeleteProvisioningProfile.html)  **
  - **Description:** Grants permission to delete provisioning profile
  - **Resource types (\*required):** [provisioning-profile\*](#list_iot-managed-integrations-resource-provisioning-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterAccountAssociation](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_DeregisterAccountAssociation.html)  **
  - **Description:** Grants permission to deregister account association
  - **Resource types (\*required):** [account-association\*](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountAssociation](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetAccountAssociation.html)  **
  - **Description:** Grants permission to get information about an account association
  - **Resource types (\*required):** [account-association\*](#list_iot-managed-integrations-resource-account-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudConnector](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetCloudConnector.html)  **
  - **Description:** Grants permission to get information about a cloud connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnectorDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetConnectorDestination.html)  **
  - **Description:** Grants permission to get information about a cloud destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCredentialLocker](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetCredentialLocker.html)  **
  - **Description:** Grants permission to get information about a credential locker
  - **Resource types (\*required):** [credential-locker\*](#list_iot-managed-integrations-resource-credential-locker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomEndpoint](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetCustomEndpoint.html)  **
  - **Description:** Grants permission to get information about a custom endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetDefaultEncryptionConfiguration.html)  **
  - **Description:** Grants permission to get information about a default encryption configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetDestination.html)  **
  - **Description:** Grants permission to get information about a destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDeviceDiscovery](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetDeviceDiscovery.html)  **
  - **Description:** Grants permission to get information about a device discovery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEventLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetEventLogConfiguration.html)  **
  - **Description:** Grants permission to get information about an event log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetHubConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetHubConfiguration.html)  **
  - **Description:** Grants permission to get information about a hub configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedThing](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetManagedThing.html)  **
  - **Description:** Grants permission to get information about a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedThingCapabilities](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetManagedThingCapabilities.html)  **
  - **Description:** Grants permission to get the capability report for a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedThingCertificate](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetManagedThingCertificate.html)  **
  - **Description:** Grants permission to get the certificate pem for a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedThingConnectivityData](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetManagedThingConnectivityData.html)  **
  - **Description:** Grants permission to get the connectivity data for a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedThingMetaData](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetManagedThingMetaData.html)  **
  - **Description:** Grants permission to get the meta data information for a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedThingState](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetManagedThingState.html)  **
  - **Description:** Grants permission to get the device state information for a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNotificationConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetNotificationConfiguration.html)  **
  - **Description:** Grants permission to get information for a notification configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOtaTask](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetOtaTask.html)  **
  - **Description:** Grants permission to get information for an ota task
  - **Resource types (\*required):** [ota-task\*](#list_iot-managed-integrations-resource-ota-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOtaTaskConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetOtaTaskConfiguration.html)  **
  - **Description:** Grants permission to get information for an ota task configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProvisioningProfile](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetProvisioningProfile.html)  **
  - **Description:** Grants permission to get information for a provisioning profile
  - **Resource types (\*required):** [provisioning-profile\*](#list_iot-managed-integrations-resource-provisioning-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRuntimeLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetRuntimeLogConfiguration.html)  **
  - **Description:** Grants permission to get information for a runtime log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSchemaVersion](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_GetSchemaVersion.html)  **
  - **Description:** Grants permission to get information for a version of a schema
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccountAssociations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListAccountAssociations.html)  **
  - **Description:** Grants permission to list information for account associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCloudConnectors](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListCloudConnectors.html)  **
  - **Description:** Grants permission to list information for cloud connectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectorDestinations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListConnectorDestinations.html)  **
  - **Description:** Grants permission to list information for connector destinations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCredentialLockers](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListCredentialLockers.html)  **
  - **Description:** Grants permission to list information for credential lockers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDestinations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListDestinations.html)  **
  - **Description:** Grants permission to list information for destinations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeviceDiscoveries](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListDeviceDiscoveries.html)  **
  - **Description:** Grants permission to list information for device discoveries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDiscoveredDevices](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListDiscoveredDevices.html)  **
  - **Description:** Grants permission to list information for device discovered in a device discoveries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEventLogConfigurations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListEventLogConfigurations.html)  **
  - **Description:** Grants permission to list information for event log configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListManagedThingAccountAssociations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListManagedThingAccountAssociations.html)  **
  - **Description:** Grants permission to list information for associations between managed thing and account associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedThingSchemas](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListManagedThingSchemas.html)  **
  - **Description:** Grants permission to list schemas associated with a managed thing
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListManagedThings](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListManagedThings.html)  **
  - **Description:** Grants permission to list information for managed things
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotificationConfigurations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListNotificationConfigurations.html)  **
  - **Description:** Grants permission to list information for notification configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOtaTaskConfigurations](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListOtaTaskConfigurations.html)  **
  - **Description:** Grants permission to list information for ota task configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOtaTaskExecutions](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListOtaTaskExecutions.html)  **
  - **Description:** Grants permission to list information for ota task executions
  - **Resource types (\*required):** [ota-task\*](#list_iot-managed-integrations-resource-ota-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListOtaTasks](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListOtaTasks.html)  **
  - **Description:** Grants permission to list information for ota tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProvisioningProfiles](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListProvisioningProfiles.html)  **
  - **Description:** Grants permission to list information for provisioning profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchemaVersions](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListSchemaVersions.html)  **
  - **Description:** Grants permission to list information for schemas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for the specified resource
  - **Resource types (\*required):** [account-association](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [credential-locker](#list_iot-managed-integrations-resource-credential-locker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managed-thing](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ota-task](#list_iot-managed-integrations-resource-ota-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [provisioning-profile](#list_iot-managed-integrations-resource-provisioning-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_PutDefaultEncryptionConfiguration.html)  **
  - **Description:** Grants permission to update the default settings for an encryption configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutHubConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_PutHubConfiguration.html)  **
  - **Description:** Grants permission to update a hub configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutRuntimeLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_PutRuntimeLogConfiguration.html)  **
  - **Description:** Grants permission to update a runtime log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterAccountAssociation](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_RegisterAccountAssociation.html)  **
  - **Description:** Grants permission to register an account association to a managed thing
  - **Resource types (\*required):** [account-association\*](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterCustomEndpoint](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_RegisterCustomEndpoint.html)  **
  - **Description:** Grants permission to register a custom endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ResetRuntimeLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_ResetRuntimeLogConfiguration.html)  **
  - **Description:** Grants permission to reset a runtime log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendConnectorEvent](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_SendConnectorEvent.html)  **
  - **Description:** Grants permission to send a connector event
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendManagedThingCommand](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_SendManagedThingCommand.html)  **
  - **Description:** Grants permission to send a command to a managed thing
  - **Resource types (\*required):** [account-association](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAccountAssociationRefresh](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_StartAccountAssociationRefresh.html)  **
  - **Description:** Grants permission to start a refresh of access tokens associated with an account association
  - **Resource types (\*required):** [account-association\*](#list_iot-managed-integrations-resource-account-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDeviceDiscovery](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_StartDeviceDiscovery.html)  **
  - **Description:** Grants permission to start a device discovery
  - **Resource types (\*required):** [account-association](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managed-thing](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags for the specified resource
  - **Resource types (\*required):** [account-association](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [credential-locker](#list_iot-managed-integrations-resource-credential-locker) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [managed-thing](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [ota-task](#list_iot-managed-integrations-resource-ota-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [provisioning-profile](#list_iot-managed-integrations-resource-provisioning-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iot-managed-integrations-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags for the specified resource
  - **Resource types (\*required):** [account-association](#list_iot-managed-integrations-resource-account-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [credential-locker](#list_iot-managed-integrations-resource-credential-locker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [managed-thing](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [ota-task](#list_iot-managed-integrations-resource-ota-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Resource types (\*required):** [provisioning-profile](#list_iot-managed-integrations-resource-provisioning-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iot-managed-integrations-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountAssociation](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateAccountAssociation.html)  **
  - **Description:** Grants permission to update an account association
  - **Resource types (\*required):** [account-association\*](#list_iot-managed-integrations-resource-account-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCloudConnector](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateCloudConnector.html)  **
  - **Description:** Grants permission to update a cloud connector
  - **Resource types (\*required):** 
  - **Condition keys:** [iotmanagedintegrations:cloudConnectorId](#list_iot-managed-integrations-iotmanagedintegrations_cloudConnectorId)
  - **Access level:** Write

- **   [UpdateConnectorDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateConnectorDestination.html)  **
  - **Description:** Grants permission to update a connector destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDestination](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateDestination.html)  **
  - **Description:** Grants permission to update a destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEventLogConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateEventLogConfiguration.html)  **
  - **Description:** Grants permission to update an event log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateManagedThing](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateManagedThing.html)  **
  - **Description:** Grants permission to update a managed thing
  - **Resource types (\*required):** [credential-locker](#list_iot-managed-integrations-resource-credential-locker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [managed-thing\*](#list_iot-managed-integrations-resource-managed-thing) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNotificationConfiguration](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateNotificationConfiguration.html)  **
  - **Description:** Grants permission to update a notification configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOtaTask](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/API_UpdateOtaTask.html)  **
  - **Description:** Grants permission to update an ota task
  - **Resource types (\*required):** [ota-task\*](#list_iot-managed-integrations-resource-ota-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT Managed Integrations
<a name="list_iot-managed-integrations-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [account-association](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/)  | arn:${Partition}:iotmanagedintegrations:${Region}:${Account}:account-association/${AccountAssociationId} | [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_) | 
|  [credential-locker](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/)  | arn:${Partition}:iotmanagedintegrations:${Region}:${Account}:credential-locker/${Identifier} | [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_) | 
|  [managed-thing](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/)  | arn:${Partition}:iotmanagedintegrations:${Region}:${Account}:managed-thing/${Identifier} | [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_) | 
|  [ota-task](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/)  | arn:${Partition}:iotmanagedintegrations:${Region}:${Account}:ota-task/${Identifier} | [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_) | 
|  [provisioning-profile](https://docs.aws.amazon.com/iotmanagedintegrations/latest/APIReference/)  | arn:${Partition}:iotmanagedintegrations:${Region}:${Account}:provisioning-profile/${Identifier} | [aws:ResourceTag/${TagKey}](#list_iot-managed-integrations-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT Managed Integrations
<a name="list_iot-managed-integrations-policy-keys"></a>

AWS IoT Managed Integrations defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 
|   [iotmanagedintegrations:cloudConnectorId](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotmanagedintegrations.html#awsiotmanagedintegrations-policy-keys)  | Filters access by the CloudConnectorId | String | 
|   [iotmanagedintegrations:connectorDestinationId](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotmanagedintegrations.html#awsiotmanagedintegrations-policy-keys)  | Filters access by the ConnectorDestinationId | String | 