

# Actions, resources, and condition keys for AWS IoT Wireless
<a name="list_iotwireless"></a>

AWS IoT Wireless (service prefix: `iotwireless`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot-wireless/latest/apireference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot/latest/developerguide/iot-authorization.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotwireless/iotwireless.json) for this service.

**Topics**
+ [API operations defined by AWS IoT Wireless](#list_iotwireless-operations)
+ [Actions defined by AWS IoT Wireless](#list_iotwireless-actions-as-permissions)
+ [Resource types defined by AWS IoT Wireless](#list_iotwireless-resources-for-iam-policies)
+ [Condition keys for AWS IoT Wireless](#list_iotwireless-policy-keys)

## API operations defined by AWS IoT Wireless
<a name="list_iotwireless-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iotwireless-actions-as-permissions).




- **   AssociateAwsAccountWithPartnerAccount  **
  - **IAM action:**  [iotwireless:AssociateAwsAccountWithPartnerAccount](#list_iotwireless-action-AssociateAwsAccountWithPartnerAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AssociateMulticastGroupWithFuotaTask  **
  - **IAM action:**  [iotwireless:AssociateMulticastGroupWithFuotaTask](#list_iotwireless-action-AssociateMulticastGroupWithFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateWirelessDeviceWithFuotaTask  **
  - **IAM action:**  [iotwireless:AssociateWirelessDeviceWithFuotaTask](#list_iotwireless-action-AssociateWirelessDeviceWithFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateWirelessDeviceWithMulticastGroup  **
  - **IAM action:**  [iotwireless:AssociateWirelessDeviceWithMulticastGroup](#list_iotwireless-action-AssociateWirelessDeviceWithMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateWirelessDeviceWithThing  **
  - **IAM action:**  [iotwireless:AssociateWirelessDeviceWithThing](#list_iotwireless-action-AssociateWirelessDeviceWithThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateWirelessGatewayWithCertificate  **
  - **IAM action:**  [iotwireless:AssociateWirelessGatewayWithCertificate](#list_iotwireless-action-AssociateWirelessGatewayWithCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateWirelessGatewayWithThing  **
  - **IAM action:**  [iotwireless:AssociateWirelessGatewayWithThing](#list_iotwireless-action-AssociateWirelessGatewayWithThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMulticastGroupSession  **
  - **IAM action:**  [iotwireless:CancelMulticastGroupSession](#list_iotwireless-action-CancelMulticastGroupSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDestination  **
  - **IAM action:**  [iotwireless:CreateDestination](#list_iotwireless-action-CreateDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotwireless.amazonaws.com / **Access level:** Write

- **   CreateDeviceProfile  **
  - **IAM action:**  [iotwireless:CreateDeviceProfile](#list_iotwireless-action-CreateDeviceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFuotaTask  **
  - **IAM action:**  [iotwireless:CreateFuotaTask](#list_iotwireless-action-CreateFuotaTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotwireless.amazonaws.com / **Access level:** Write

- **   CreateMulticastGroup  **
  - **IAM action:**  [iotwireless:CreateMulticastGroup](#list_iotwireless-action-CreateMulticastGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNetworkAnalyzerConfiguration  **
  - **IAM action:**  [iotwireless:CreateNetworkAnalyzerConfiguration](#list_iotwireless-action-CreateNetworkAnalyzerConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceProfile  **
  - **IAM action:**  [iotwireless:CreateServiceProfile](#list_iotwireless-action-CreateServiceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWirelessDevice  **
  - **IAM action:**  [iotwireless:CreateWirelessDevice](#list_iotwireless-action-CreateWirelessDevice)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWirelessGateway  **
  - **IAM action:**  [iotwireless:CreateWirelessGateway](#list_iotwireless-action-CreateWirelessGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWirelessGatewayTask  **
  - **IAM action:**  [iotwireless:CreateWirelessGatewayTask](#list_iotwireless-action-CreateWirelessGatewayTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWirelessGatewayTaskDefinition  **
  - **IAM action:**  [iotwireless:CreateWirelessGatewayTaskDefinition](#list_iotwireless-action-CreateWirelessGatewayTaskDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotwireless.amazonaws.com / **Access level:** Write

- **   DeleteDestination  **
  - **IAM action:**  [iotwireless:DeleteDestination](#list_iotwireless-action-DeleteDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeviceProfile  **
  - **IAM action:**  [iotwireless:DeleteDeviceProfile](#list_iotwireless-action-DeleteDeviceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFuotaTask  **
  - **IAM action:**  [iotwireless:DeleteFuotaTask](#list_iotwireless-action-DeleteFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMulticastGroup  **
  - **IAM action:**  [iotwireless:DeleteMulticastGroup](#list_iotwireless-action-DeleteMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNetworkAnalyzerConfiguration  **
  - **IAM action:**  [iotwireless:DeleteNetworkAnalyzerConfiguration](#list_iotwireless-action-DeleteNetworkAnalyzerConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueuedMessages  **
  - **IAM action:**  [iotwireless:DeleteQueuedMessages](#list_iotwireless-action-DeleteQueuedMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceProfile  **
  - **IAM action:**  [iotwireless:DeleteServiceProfile](#list_iotwireless-action-DeleteServiceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWirelessDevice  **
  - **IAM action:**  [iotwireless:DeleteWirelessDevice](#list_iotwireless-action-DeleteWirelessDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWirelessDeviceImportTask  **
  - **IAM action:**  [iotwireless:DeleteWirelessDeviceImportTask](#list_iotwireless-action-DeleteWirelessDeviceImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWirelessGateway  **
  - **IAM action:**  [iotwireless:DeleteWirelessGateway](#list_iotwireless-action-DeleteWirelessGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWirelessGatewayTask  **
  - **IAM action:**  [iotwireless:DeleteWirelessGatewayTask](#list_iotwireless-action-DeleteWirelessGatewayTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWirelessGatewayTaskDefinition  **
  - **IAM action:**  [iotwireless:DeleteWirelessGatewayTaskDefinition](#list_iotwireless-action-DeleteWirelessGatewayTaskDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterWirelessDevice  **
  - **IAM action:**  [iotwireless:DeregisterWirelessDevice](#list_iotwireless-action-DeregisterWirelessDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAwsAccountFromPartnerAccount  **
  - **IAM action:**  [iotwireless:DisassociateAwsAccountFromPartnerAccount](#list_iotwireless-action-DisassociateAwsAccountFromPartnerAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMulticastGroupFromFuotaTask  **
  - **IAM action:**  [iotwireless:DisassociateMulticastGroupFromFuotaTask](#list_iotwireless-action-DisassociateMulticastGroupFromFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWirelessDeviceFromFuotaTask  **
  - **IAM action:**  [iotwireless:DisassociateWirelessDeviceFromFuotaTask](#list_iotwireless-action-DisassociateWirelessDeviceFromFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWirelessDeviceFromMulticastGroup  **
  - **IAM action:**  [iotwireless:DisassociateWirelessDeviceFromMulticastGroup](#list_iotwireless-action-DisassociateWirelessDeviceFromMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWirelessDeviceFromThing  **
  - **IAM action:**  [iotwireless:DisassociateWirelessDeviceFromThing](#list_iotwireless-action-DisassociateWirelessDeviceFromThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWirelessGatewayFromCertificate  **
  - **IAM action:**  [iotwireless:DisassociateWirelessGatewayFromCertificate](#list_iotwireless-action-DisassociateWirelessGatewayFromCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWirelessGatewayFromThing  **
  - **IAM action:**  [iotwireless:DisassociateWirelessGatewayFromThing](#list_iotwireless-action-DisassociateWirelessGatewayFromThing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDestination  **
  - **IAM action:**  [iotwireless:GetDestination](#list_iotwireless-action-GetDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeviceProfile  **
  - **IAM action:**  [iotwireless:GetDeviceProfile](#list_iotwireless-action-GetDeviceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventConfigurationByResourceTypes  **
  - **IAM action:**  [iotwireless:GetEventConfigurationByResourceTypes](#list_iotwireless-action-GetEventConfigurationByResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFuotaTask  **
  - **IAM action:**  [iotwireless:GetFuotaTask](#list_iotwireless-action-GetFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLogLevelsByResourceTypes  **
  - **IAM action:**  [iotwireless:GetLogLevelsByResourceTypes](#list_iotwireless-action-GetLogLevelsByResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetricConfiguration  **
  - **IAM action:**  [iotwireless:GetMetricConfiguration](#list_iotwireless-action-GetMetricConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMetrics  **
  - **IAM action:**  [iotwireless:GetMetrics](#list_iotwireless-action-GetMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMulticastGroup  **
  - **IAM action:**  [iotwireless:GetMulticastGroup](#list_iotwireless-action-GetMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMulticastGroupSession  **
  - **IAM action:**  [iotwireless:GetMulticastGroupSession](#list_iotwireless-action-GetMulticastGroupSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkAnalyzerConfiguration  **
  - **IAM action:**  [iotwireless:GetNetworkAnalyzerConfiguration](#list_iotwireless-action-GetNetworkAnalyzerConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPartnerAccount  **
  - **IAM action:**  [iotwireless:GetPartnerAccount](#list_iotwireless-action-GetPartnerAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPosition  **
  - **IAM action:**  [iotwireless:GetPosition](#list_iotwireless-action-GetPosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPositionConfiguration  **
  - **IAM action:**  [iotwireless:GetPositionConfiguration](#list_iotwireless-action-GetPositionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPositionEstimate  **
  - **IAM action:**  [iotwireless:GetPositionEstimate](#list_iotwireless-action-GetPositionEstimate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceEventConfiguration  **
  - **IAM action:**  [iotwireless:GetResourceEventConfiguration](#list_iotwireless-action-GetResourceEventConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceLogLevel  **
  - **IAM action:**  [iotwireless:GetResourceLogLevel](#list_iotwireless-action-GetResourceLogLevel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePosition  **
  - **IAM action:**  [iotwireless:GetResourcePosition](#list_iotwireless-action-GetResourcePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceEndpoint  **
  - **IAM action:**  [iotwireless:GetServiceEndpoint](#list_iotwireless-action-GetServiceEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceProfile  **
  - **IAM action:**  [iotwireless:GetServiceProfile](#list_iotwireless-action-GetServiceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessDevice  **
  - **IAM action:**  [iotwireless:GetWirelessDevice](#list_iotwireless-action-GetWirelessDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessDeviceImportTask  **
  - **IAM action:**  [iotwireless:GetWirelessDeviceImportTask](#list_iotwireless-action-GetWirelessDeviceImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessDeviceStatistics  **
  - **IAM action:**  [iotwireless:GetWirelessDeviceStatistics](#list_iotwireless-action-GetWirelessDeviceStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessGateway  **
  - **IAM action:**  [iotwireless:GetWirelessGateway](#list_iotwireless-action-GetWirelessGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessGatewayCertificate  **
  - **IAM action:**  [iotwireless:GetWirelessGatewayCertificate](#list_iotwireless-action-GetWirelessGatewayCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessGatewayFirmwareInformation  **
  - **IAM action:**  [iotwireless:GetWirelessGatewayFirmwareInformation](#list_iotwireless-action-GetWirelessGatewayFirmwareInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessGatewayStatistics  **
  - **IAM action:**  [iotwireless:GetWirelessGatewayStatistics](#list_iotwireless-action-GetWirelessGatewayStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessGatewayTask  **
  - **IAM action:**  [iotwireless:GetWirelessGatewayTask](#list_iotwireless-action-GetWirelessGatewayTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWirelessGatewayTaskDefinition  **
  - **IAM action:**  [iotwireless:GetWirelessGatewayTaskDefinition](#list_iotwireless-action-GetWirelessGatewayTaskDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDestinations  **
  - **IAM action:**  [iotwireless:ListDestinations](#list_iotwireless-action-ListDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeviceProfiles  **
  - **IAM action:**  [iotwireless:ListDeviceProfiles](#list_iotwireless-action-ListDeviceProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDevicesForWirelessDeviceImportTask  **
  - **IAM action:**  [iotwireless:ListDevicesForWirelessDeviceImportTask](#list_iotwireless-action-ListDevicesForWirelessDeviceImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEventConfigurations  **
  - **IAM action:**  [iotwireless:ListEventConfigurations](#list_iotwireless-action-ListEventConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFuotaTasks  **
  - **IAM action:**  [iotwireless:ListFuotaTasks](#list_iotwireless-action-ListFuotaTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMulticastGroups  **
  - **IAM action:**  [iotwireless:ListMulticastGroups](#list_iotwireless-action-ListMulticastGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMulticastGroupsByFuotaTask  **
  - **IAM action:**  [iotwireless:ListMulticastGroupsByFuotaTask](#list_iotwireless-action-ListMulticastGroupsByFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNetworkAnalyzerConfigurations  **
  - **IAM action:**  [iotwireless:ListNetworkAnalyzerConfigurations](#list_iotwireless-action-ListNetworkAnalyzerConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPartnerAccounts  **
  - **IAM action:**  [iotwireless:ListPartnerAccounts](#list_iotwireless-action-ListPartnerAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPositionConfigurations  **
  - **IAM action:**  [iotwireless:ListPositionConfigurations](#list_iotwireless-action-ListPositionConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListQueuedMessages  **
  - **IAM action:**  [iotwireless:ListQueuedMessages](#list_iotwireless-action-ListQueuedMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceProfiles  **
  - **IAM action:**  [iotwireless:ListServiceProfiles](#list_iotwireless-action-ListServiceProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [iotwireless:ListTagsForResource](#list_iotwireless-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWirelessDeviceImportTasks  **
  - **IAM action:**  [iotwireless:ListWirelessDeviceImportTasks](#list_iotwireless-action-ListWirelessDeviceImportTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWirelessDevices  **
  - **IAM action:**  [iotwireless:ListWirelessDevices](#list_iotwireless-action-ListWirelessDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWirelessGatewayTaskDefinitions  **
  - **IAM action:**  [iotwireless:ListWirelessGatewayTaskDefinitions](#list_iotwireless-action-ListWirelessGatewayTaskDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWirelessGateways  **
  - **IAM action:**  [iotwireless:ListWirelessGateways](#list_iotwireless-action-ListWirelessGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutPositionConfiguration  **
  - **IAM action:**  [iotwireless:PutPositionConfiguration](#list_iotwireless-action-PutPositionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourceLogLevel  **
  - **IAM action:**  [iotwireless:PutResourceLogLevel](#list_iotwireless-action-PutResourceLogLevel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetAllResourceLogLevels  **
  - **IAM action:**  [iotwireless:ResetAllResourceLogLevels](#list_iotwireless-action-ResetAllResourceLogLevels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetResourceLogLevel  **
  - **IAM action:**  [iotwireless:ResetResourceLogLevel](#list_iotwireless-action-ResetResourceLogLevel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendDataToMulticastGroup  **
  - **IAM action:**  [iotwireless:SendDataToMulticastGroup](#list_iotwireless-action-SendDataToMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendDataToWirelessDevice  **
  - **IAM action:**  [iotwireless:SendDataToWirelessDevice](#list_iotwireless-action-SendDataToWirelessDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBulkAssociateWirelessDeviceWithMulticastGroup  **
  - **IAM action:**  [iotwireless:StartBulkAssociateWirelessDeviceWithMulticastGroup](#list_iotwireless-action-StartBulkAssociateWirelessDeviceWithMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBulkDisassociateWirelessDeviceFromMulticastGroup  **
  - **IAM action:**  [iotwireless:StartBulkDisassociateWirelessDeviceFromMulticastGroup](#list_iotwireless-action-StartBulkDisassociateWirelessDeviceFromMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFuotaTask  **
  - **IAM action:**  [iotwireless:StartFuotaTask](#list_iotwireless-action-StartFuotaTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMulticastGroupSession  **
  - **IAM action:**  [iotwireless:StartMulticastGroupSession](#list_iotwireless-action-StartMulticastGroupSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSingleWirelessDeviceImportTask  **
  - **IAM action:**  [iotwireless:StartSingleWirelessDeviceImportTask](#list_iotwireless-action-StartSingleWirelessDeviceImportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartWirelessDeviceImportTask  **
  - **IAM action:**  [iotwireless:StartWirelessDeviceImportTask](#list_iotwireless-action-StartWirelessDeviceImportTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotwireless.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [iotwireless:TagResource](#list_iotwireless-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestWirelessDevice  **
  - **IAM action:**  [iotwireless:TestWirelessDevice](#list_iotwireless-action-TestWirelessDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [iotwireless:UntagResource](#list_iotwireless-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDestination  **
  - **IAM action:**  [iotwireless:UpdateDestination](#list_iotwireless-action-UpdateDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotwireless.amazonaws.com / **Access level:** Write

- **   UpdateEventConfigurationByResourceTypes  **
  - **IAM action:**  [iotwireless:UpdateEventConfigurationByResourceTypes](#list_iotwireless-action-UpdateEventConfigurationByResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFuotaTask  **
  - **IAM action:**  [iotwireless:UpdateFuotaTask](#list_iotwireless-action-UpdateFuotaTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotwireless.amazonaws.com / **Access level:** Write

- **   UpdateLogLevelsByResourceTypes  **
  - **IAM action:**  [iotwireless:UpdateLogLevelsByResourceTypes](#list_iotwireless-action-UpdateLogLevelsByResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMetricConfiguration  **
  - **IAM action:**  [iotwireless:UpdateMetricConfiguration](#list_iotwireless-action-UpdateMetricConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMulticastGroup  **
  - **IAM action:**  [iotwireless:UpdateMulticastGroup](#list_iotwireless-action-UpdateMulticastGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetworkAnalyzerConfiguration  **
  - **IAM action:**  [iotwireless:UpdateNetworkAnalyzerConfiguration](#list_iotwireless-action-UpdateNetworkAnalyzerConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePartnerAccount  **
  - **IAM action:**  [iotwireless:UpdatePartnerAccount](#list_iotwireless-action-UpdatePartnerAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePosition  **
  - **IAM action:**  [iotwireless:UpdatePosition](#list_iotwireless-action-UpdatePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceEventConfiguration  **
  - **IAM action:**  [iotwireless:UpdateResourceEventConfiguration](#list_iotwireless-action-UpdateResourceEventConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourcePosition  **
  - **IAM action:**  [iotwireless:UpdateResourcePosition](#list_iotwireless-action-UpdateResourcePosition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWirelessDevice  **
  - **IAM action:**  [iotwireless:UpdateWirelessDevice](#list_iotwireless-action-UpdateWirelessDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWirelessDeviceImportTask  **
  - **IAM action:**  [iotwireless:UpdateWirelessDeviceImportTask](#list_iotwireless-action-UpdateWirelessDeviceImportTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWirelessGateway  **
  - **IAM action:**  [iotwireless:UpdateWirelessGateway](#list_iotwireless-action-UpdateWirelessGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT Wireless
<a name="list_iotwireless-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAwsAccountWithPartnerAccount](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateAwsAccountWithPartnerAccount.html)  **
  - **Description:** Grants permission to link partner accounts with AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [AssociateMulticastGroupWithFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateMulticastGroupWithFuotaTask.html)  **
  - **Description:** Grants permission to associate the MulticastGroup with FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWirelessDeviceWithFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessDeviceWithFuotaTask.html)  **
  - **Description:** Grants permission to associate the wireless device with FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWirelessDeviceWithMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessDeviceWithMulticastGroup.html)  **
  - **Description:** Grants permission to associate the WirelessDevice with MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWirelessDeviceWithThing](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessDeviceWithThing.html)  **
  - **Description:** Grants permission to associate the wireless device with AWS IoT thing for a given wirelessDeviceId
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iotwireless-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [AssociateWirelessGatewayWithCertificate](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessGatewayWithCertificate.html)  **
  - **Description:** Grants permission to associate a WirelessGateway with the IoT Core Identity certificate
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cert\*](#list_iotwireless-resource-cert) / **Condition keys:**  
  - **Access level:** Write

- **   [AssociateWirelessGatewayWithThing](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessGatewayWithThing.html)  **
  - **Description:** Grants permission to associate the wireless gateway with AWS IoT thing for a given wirelessGatewayId
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iotwireless-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [CancelMulticastGroupSession](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CancelMulticastGroupSession.html)  **
  - **Description:** Grants permission to cancel the MulticastGroup session
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDestination](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDestination.html)  **
  - **Description:** Grants permission to create a Destination resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeviceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDeviceProfile.html)  **
  - **Description:** Grants permission to create a DeviceProfile resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateFuotaTask.html)  **
  - **Description:** Grants permission to create a FuotaTask resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateMulticastGroup.html)  **
  - **Description:** Grants permission to create a MulticastGroup resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNetworkAnalyzerConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateNetworkAnalyzerConfiguration.html)  **
  - **Description:** Grants permission to create a NetworkAnalyzerConfiguration resource
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateServiceProfile.html)  **
  - **Description:** Grants permission to create a ServiceProfile resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessDevice.html)  **
  - **Description:** Grants permission to create a WirelessDevice resource with given Destination
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [DeviceProfile](#list_iotwireless-resource-DeviceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [ServiceProfile](#list_iotwireless-resource-ServiceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWirelessGateway](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGateway.html)  **
  - **Description:** Grants permission to create a WirelessGateway resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWirelessGatewayTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGatewayTask.html)  **
  - **Description:** Grants permission to create a task for a given WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWirelessGatewayTaskDefinition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGatewayTaskDefinition.html)  **
  - **Description:** Grants permission to create a WirelessGateway task definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDestination](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteDestination.html)  **
  - **Description:** Grants permission to delete a Destination
  - **Resource types (\*required):** [Destination\*](#list_iotwireless-resource-Destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeviceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteDeviceProfile.html)  **
  - **Description:** Grants permission to delete a DeviceProfile
  - **Resource types (\*required):** [DeviceProfile\*](#list_iotwireless-resource-DeviceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteFuotaTask.html)  **
  - **Description:** Grants permission to delete the FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteMulticastGroup.html)  **
  - **Description:** Grants permission to delete the MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetworkAnalyzerConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteNetworkAnalyzerConfiguration.html)  **
  - **Description:** Grants permission to delete the NetworkAnalyzerConfiguration
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration\*](#list_iotwireless-resource-NetworkAnalyzerConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQueuedMessages](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteQueuedMessages.html)  **
  - **Description:** Grants permission to delete QueuedMessages
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteServiceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteServiceProfile.html)  **
  - **Description:** Grants permission to delete a ServiceProfile
  - **Resource types (\*required):** [ServiceProfile\*](#list_iotwireless-resource-ServiceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessDevice.html)  **
  - **Description:** Grants permission to delete a WirelessDevice
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWirelessDeviceImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessDeviceImportTask.html)  **
  - **Description:** Grants permission to delete the wireless device import task
  - **Resource types (\*required):** [ImportTask\*](#list_iotwireless-resource-ImportTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWirelessGateway](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessGateway.html)  **
  - **Description:** Grants permission to delete a WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWirelessGatewayTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessGatewayTask.html)  **
  - **Description:** Grants permission to delete task for a given WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWirelessGatewayTaskDefinition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessGatewayTaskDefinition.html)  **
  - **Description:** Grants permission to delete a WirelessGateway task definition
  - **Resource types (\*required):** [WirelessGatewayTaskDefinition\*](#list_iotwireless-resource-WirelessGatewayTaskDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeregisterWirelessDevice.html)  **
  - **Description:** Grants permission to deregister wireless device
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateAwsAccountFromPartnerAccount](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateAwsAccountFromPartnerAccount.html)  **
  - **Description:** Grants permission to disassociate an AWS account from a partner account
  - **Resource types (\*required):** [SidewalkAccount\*](#list_iotwireless-resource-SidewalkAccount)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateMulticastGroupFromFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateMulticastGroupFromFuotaTask.html)  **
  - **Description:** Grants permission to disassociate the MulticastGroup from FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWirelessDeviceFromFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessDeviceFromFuotaTask.html)  **
  - **Description:** Grants permission to disassociate the wireless device from FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWirelessDeviceFromMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessDeviceFromMulticastGroup.html)  **
  - **Description:** Grants permission to disassociate the wireless device from MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWirelessDeviceFromThing](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessDeviceFromThing.html)  **
  - **Description:** Grants permission to disassociate a wireless device from a AWS IoT thing
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iotwireless-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateWirelessGatewayFromCertificate](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessGatewayFromCertificate.html)  **
  - **Description:** Grants permission to disassociate a WirelessGateway from a IoT Core Identity certificate
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cert\*](#list_iotwireless-resource-cert) / **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateWirelessGatewayFromThing](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessGatewayFromThing.html)  **
  - **Description:** Grants permission to disassociate a WirelessGateway from a IoT Core thing
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thing\*](#list_iotwireless-resource-thing) / **Condition keys:**  
  - **Access level:** Write

- **   [GetDestination](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDestination.html)  **
  - **Description:** Grants permission to get the Destination
  - **Resource types (\*required):** [Destination\*](#list_iotwireless-resource-Destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDeviceProfile.html)  **
  - **Description:** Grants permission to get the DeviceProfile
  - **Resource types (\*required):** [DeviceProfile\*](#list_iotwireless-resource-DeviceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventConfigurationByResourceTypes](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetEventConfigurationByResourceTypes.html)  **
  - **Description:** Grants permission to get event configuration by resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetFuotaTask.html)  **
  - **Description:** Grants permission to get the FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLogLevelsByResourceTypes](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetLogLevelsByResourceTypes.html)  **
  - **Description:** Grants permission to get log levels by resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMetricConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetMetricConfiguration.html)  **
  - **Description:** Grants permission to get metric configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMetrics](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetMetrics.html)  **
  - **Description:** Grants permission to get metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetMulticastGroup.html)  **
  - **Description:** Grants permission to get the MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMulticastGroupSession](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetMulticastGroupSession.html)  **
  - **Description:** Grants permission to get the MulticastGroup session
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkAnalyzerConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetNetworkAnalyzerConfiguration.html)  **
  - **Description:** Grants permission to get the NetworkAnalyzerConfiguration
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration\*](#list_iotwireless-resource-NetworkAnalyzerConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPartnerAccount](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPartnerAccount.html)  **
  - **Description:** Grants permission to get the associated PartnerAccount
  - **Resource types (\*required):** [SidewalkAccount\*](#list_iotwireless-resource-SidewalkAccount)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPosition.html)  **
  - **Description:** Grants permission to get position for a given resource
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPositionConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPositionConfiguration.html)  **
  - **Description:** Grants permission to get position configuration for a given resource
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPositionEstimate](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetPositionEstimate.html)  **
  - **Description:** Grants permission to get position estimate
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceEventConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourceEventConfiguration.html)  **
  - **Description:** Grants permission to get an event configuration for an identifier
  - **Resource types (\*required):** [SidewalkAccount](#list_iotwireless-resource-SidewalkAccount) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceLogLevel](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourceLogLevel.html)  **
  - **Description:** Grants permission to get resource log level
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html)  **
  - **Description:** Grants permission to get position for a given resource
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceEndpoint](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetServiceEndpoint.html)  **
  - **Description:** Grants permission to retrieve the customer account specific endpoint for CUPS protocol connection or LoRaWAN Network Server (LNS) protocol connection, and optionally server trust certificate in PEM format
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServiceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetServiceProfile.html)  **
  - **Description:** Grants permission to get the ServiceProfile
  - **Resource types (\*required):** [ServiceProfile\*](#list_iotwireless-resource-ServiceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDevice.html)  **
  - **Description:** Grants permission to get the WirelessDevice
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessDeviceImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDeviceImportTask.html)  **
  - **Description:** Grants permission to get the wireless device import task
  - **Resource types (\*required):** [ImportTask\*](#list_iotwireless-resource-ImportTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessDeviceStatistics](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDeviceStatistics.html)  **
  - **Description:** Grants permission to get statistics info for a given WirelessDevice
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessGateway](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGateway.html)  **
  - **Description:** Grants permission to get the WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessGatewayCertificate](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayCertificate.html)  **
  - **Description:** Grants permission to get the IoT Core Identity certificate id associated with the WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessGatewayFirmwareInformation](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayFirmwareInformation.html)  **
  - **Description:** Grants permission to get Current firmware version and other information for the WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessGatewayStatistics](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayStatistics.html)  **
  - **Description:** Grants permission to get statistics info for a given WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessGatewayTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayTask.html)  **
  - **Description:** Grants permission to get the task for a given WirelessGateway
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWirelessGatewayTaskDefinition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessGatewayTaskDefinition.html)  **
  - **Description:** Grants permission to get the given WirelessGateway task definition
  - **Resource types (\*required):** [WirelessGatewayTaskDefinition\*](#list_iotwireless-resource-WirelessGatewayTaskDefinition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDestinations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDestinations.html)  **
  - **Description:** Grants permission to list information of available Destinations based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDeviceProfiles](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDeviceProfiles.html)  **
  - **Description:** Grants permission to list information of available DeviceProfiles based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDevicesForWirelessDeviceImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDevicesForWirelessDeviceImportTask.html)  **
  - **Description:** Grants permission to list information of devices by wireless device import task based on the AWS account
  - **Resource types (\*required):** [ImportTask\*](#list_iotwireless-resource-ImportTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEventConfigurations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListEventConfigurations.html)  **
  - **Description:** Grants permission to list information of available event configurations based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFuotaTasks](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListFuotaTasks.html)  **
  - **Description:** Grants permission to list information of available FuotaTasks based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListMulticastGroups](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListMulticastGroups.html)  **
  - **Description:** Grants permission to list information of available MulticastGroups based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListMulticastGroupsByFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListMulticastGroupsByFuotaTask.html)  **
  - **Description:** Grants permission to list information of available MulticastGroups by FuotaTask based on the AWS account
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListNetworkAnalyzerConfigurations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListNetworkAnalyzerConfigurations.html)  **
  - **Description:** Grants permission to list information of available NetworkAnalyzerConfigurations based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPartnerAccounts](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListPartnerAccounts.html)  **
  - **Description:** Grants permission to list the available partner accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPositionConfigurations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListPositionConfigurations.html)  **
  - **Description:** Grants permission to list information of available position configurations based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListQueuedMessages](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListQueuedMessages.html)  **
  - **Description:** Grants permission to list the Queued Messages
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServiceProfiles](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListServiceProfiles.html)  **
  - **Description:** Grants permission to list information of available ServiceProfiles based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for a given resource
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DeviceProfile](#list_iotwireless-resource-DeviceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [FuotaTask](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ImportTask](#list_iotwireless-resource-ImportTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MulticastGroup](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration](#list_iotwireless-resource-NetworkAnalyzerConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ServiceProfile](#list_iotwireless-resource-ServiceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SidewalkAccount](#list_iotwireless-resource-SidewalkAccount) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGatewayTaskDefinition](#list_iotwireless-resource-WirelessGatewayTaskDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWirelessDeviceImportTasks](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDeviceImportTasks.html)  **
  - **Description:** Grants permission to list wireless device import tasks information of based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListWirelessDevices](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDevices.html)  **
  - **Description:** Grants permission to list information of available WirelessDevices based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListWirelessGatewayTaskDefinitions](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessGatewayTaskDefinitions.html)  **
  - **Description:** Grants permission to list information of available WirelessGateway task definitions based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListWirelessGateways](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessGateways.html)  **
  - **Description:** Grants permission to list information of available WirelessGateways based on the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutPositionConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_PutPositionConfiguration.html)  **
  - **Description:** Grants permission to put position configuration for a given resource
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourceLogLevel](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_PutResourceLogLevel.html)  **
  - **Description:** Grants permission to put resource log level
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetAllResourceLogLevels](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ResetAllResourceLogLevels.html)  **
  - **Description:** Grants permission to reset all resource log levels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ResetResourceLogLevel](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ResetResourceLogLevel.html)  **
  - **Description:** Grants permission to reset resource log level
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDataToMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SendDataToMulticastGroup.html)  **
  - **Description:** Grants permission to send data to the MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDataToWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SendDataToWirelessDevice.html)  **
  - **Description:** Grants permission to send the decrypted application data frame to the target device
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBulkAssociateWirelessDeviceWithMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartBulkAssociateWirelessDeviceWithMulticastGroup.html)  **
  - **Description:** Grants permission to associate the WirelessDevices with MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBulkDisassociateWirelessDeviceFromMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartBulkDisassociateWirelessDeviceFromMulticastGroup.html)  **
  - **Description:** Grants permission to bulk disassociate the WirelessDevices from MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartFuotaTask.html)  **
  - **Description:** Grants permission to start the FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMulticastGroupSession](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartMulticastGroupSession.html)  **
  - **Description:** Grants permission to start the MulticastGroup session
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNetworkAnalyzerStream](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-network-analyzer-api.html)  **
  - **Description:** Grants permission to start NetworkAnalyzer stream
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration\*](#list_iotwireless-resource-NetworkAnalyzerConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSingleWirelessDeviceImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartSingleWirelessDeviceImportTask.html)  **
  - **Description:** Grants permission to start the single wireless device import task
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [StartWirelessDeviceImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartWirelessDeviceImportTask.html)  **
  - **Description:** Grants permission to start the wireless device import task
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [ImportTask\*](#list_iotwireless-resource-ImportTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a given resource
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [DeviceProfile](#list_iotwireless-resource-DeviceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [FuotaTask](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [ImportTask](#list_iotwireless-resource-ImportTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [MulticastGroup](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration](#list_iotwireless-resource-NetworkAnalyzerConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [ServiceProfile](#list_iotwireless-resource-ServiceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [SidewalkAccount](#list_iotwireless-resource-SidewalkAccount) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessGatewayTaskDefinition](#list_iotwireless-resource-WirelessGatewayTaskDefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotwireless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TestWirelessDevice.html)  **
  - **Description:** Grants permission to simulate a provisioned device to send an uplink data with payload of 'Hello'
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the given tags from the resource
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [DeviceProfile](#list_iotwireless-resource-DeviceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [FuotaTask](#list_iotwireless-resource-FuotaTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [ImportTask](#list_iotwireless-resource-ImportTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [MulticastGroup](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration](#list_iotwireless-resource-NetworkAnalyzerConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [ServiceProfile](#list_iotwireless-resource-ServiceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [SidewalkAccount](#list_iotwireless-resource-SidewalkAccount) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Resource types (\*required):** [WirelessGatewayTaskDefinition](#list_iotwireless-resource-WirelessGatewayTaskDefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotwireless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDestination](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateDestination.html)  **
  - **Description:** Grants permission to update a Destination resource
  - **Resource types (\*required):** [Destination\*](#list_iotwireless-resource-Destination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventConfigurationByResourceTypes](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateEventConfigurationByResourceTypes.html)  **
  - **Description:** Grants permission to update event configuration by resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateFuotaTask.html)  **
  - **Description:** Grants permission to update the FuotaTask
  - **Resource types (\*required):** [FuotaTask\*](#list_iotwireless-resource-FuotaTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLogLevelsByResourceTypes](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateLogLevelsByResourceTypes.html)  **
  - **Description:** Grants permission to update log levels by resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMetricConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateMetricConfiguration.html)  **
  - **Description:** Grants permission to update metric configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateMulticastGroup.html)  **
  - **Description:** Grants permission to update the MulticastGroup
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkAnalyzerConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateNetworkAnalyzerConfiguration.html)  **
  - **Description:** Grants permission to update the NetworkAnalyzerConfiguration
  - **Resource types (\*required):** [MulticastGroup\*](#list_iotwireless-resource-MulticastGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NetworkAnalyzerConfiguration\*](#list_iotwireless-resource-NetworkAnalyzerConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePartnerAccount](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdatePartnerAccount.html)  **
  - **Description:** Grants permission to update a partner account
  - **Resource types (\*required):** [SidewalkAccount\*](#list_iotwireless-resource-SidewalkAccount)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdatePosition.html)  **
  - **Description:** Grants permission to update position for a given resource
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResourceEventConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourceEventConfiguration.html)  **
  - **Description:** Grants permission to update an event configuration for an identifier
  - **Resource types (\*required):** [SidewalkAccount](#list_iotwireless-resource-SidewalkAccount) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResourcePosition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html)  **
  - **Description:** Grants permission to update position for a given resource
  - **Resource types (\*required):** [WirelessDevice](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessGateway](#list_iotwireless-resource-WirelessGateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessDevice.html)  **
  - **Description:** Grants permission to update a WirelessDevice resource
  - **Resource types (\*required):** [Destination](#list_iotwireless-resource-Destination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DeviceProfile](#list_iotwireless-resource-DeviceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ServiceProfile](#list_iotwireless-resource-ServiceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WirelessDevice\*](#list_iotwireless-resource-WirelessDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWirelessDeviceImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessDeviceImportTask.html)  **
  - **Description:** Grants permission to update a wireless device import task
  - **Resource types (\*required):** [ImportTask\*](#list_iotwireless-resource-ImportTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWirelessGateway](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessGateway.html)  **
  - **Description:** Grants permission to update a WirelessGateway resource
  - **Resource types (\*required):** [WirelessGateway\*](#list_iotwireless-resource-WirelessGateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT Wireless
<a name="list_iotwireless-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Destination](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDestination.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:Destination/${DestinationName} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [DeviceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDeviceProfile.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:DeviceProfile/${DeviceProfileId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [FuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateFuotaTask.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:FuotaTask/${FuotaTaskId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [ImportTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartWirelessDeviceImportTask.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:ImportTask/${ImportTaskId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [MulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateMulticastGroup.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:MulticastGroup/${MulticastGroupId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [NetworkAnalyzerConfiguration](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateNetworkAnalyzerConfiguration.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:NetworkAnalyzerConfiguration/${NetworkAnalyzerConfigurationName} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [ServiceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateServiceProfile.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:ServiceProfile/${ServiceProfileId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [SidewalkAccount](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateAwsAccountWithPartnerAccount.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:SidewalkAccount/${SidewalkAccountId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [WirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessDevice.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:WirelessDevice/${WirelessDeviceId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [WirelessGateway](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGateway.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:WirelessGateway/${WirelessGatewayId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [WirelessGatewayTaskDefinition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGatewayTaskDefinition.html)  | arn:${Partition}:iotwireless:${Region}:${Account}:WirelessGatewayTaskDefinition/${WirelessGatewayTaskDefinitionId} | [aws:ResourceTag/${TagKey}](#list_iotwireless-aws_ResourceTag___TagKey_) | 
|  [cert](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html)  | arn:${Partition}:iot:${Region}:${Account}:cert/${Certificate} |   | 
|  [thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)  | arn:${Partition}:iot:${Region}:${Account}:thing/${ThingName} |   | 

## Condition keys for AWS IoT Wireless
<a name="list_iotwireless-policy-keys"></a>

AWS IoT Wireless defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key that is present in the request that the user makes to IoT Wireless | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key component of a tag attached to an IoT Wireless resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the list of all the tag key names associated with the resource in the request | ArrayOfString | 
|   [iotwireless:DestinationName](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotwireless.html)  | Filters access by destination name associated with the IoT Wireless resource | String | 
|   [iotwireless:DeviceProfileId](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotwireless.html)  | Filters access by device profile id associated with the IoT Wireless resource | String | 
|   [iotwireless:ServiceProfileId](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotwireless.html)  | Filters access by service profile id associated with the IoT Wireless resource | String | 