

# Actions, resources, and condition keys for AWS Backup Gateway
<a name="list_backup-gateway"></a>

AWS Backup Gateway (service prefix: `backup-gateway`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-considerations.html#authentication) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/backup-gateway/backup-gateway.json) for this service.

**Topics**
+ [API operations defined by AWS Backup Gateway](#list_backup-gateway-operations)
+ [Actions defined by AWS Backup Gateway](#list_backup-gateway-actions-as-permissions)
+ [Resource types defined by AWS Backup Gateway](#list_backup-gateway-resources-for-iam-policies)
+ [Condition keys for AWS Backup Gateway](#list_backup-gateway-policy-keys)

## API operations defined by AWS Backup Gateway
<a name="list_backup-gateway-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_backup-gateway-actions-as-permissions).




- **   AssociateGatewayToServer  **
  - **IAM action:**  [backup-gateway:AssociateGatewayToServer](#list_backup-gateway-action-AssociateGatewayToServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGateway  **
  - **IAM action:**  [backup-gateway:CreateGateway](#list_backup-gateway-action-CreateGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup-gateway:TagResource](#list_backup-gateway-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteGateway  **
  - **IAM action:**  [backup-gateway:DeleteGateway](#list_backup-gateway-action-DeleteGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHypervisor  **
  - **IAM action:**  [backup-gateway:DeleteHypervisor](#list_backup-gateway-action-DeleteHypervisor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateGatewayFromServer  **
  - **IAM action:**  [backup-gateway:DisassociateGatewayFromServer](#list_backup-gateway-action-DisassociateGatewayFromServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBandwidthRateLimitSchedule  **
  - **IAM action:**  [backup-gateway:GetBandwidthRateLimitSchedule](#list_backup-gateway-action-GetBandwidthRateLimitSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGateway  **
  - **IAM action:**  [backup-gateway:GetGateway](#list_backup-gateway-action-GetGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHypervisor  **
  - **IAM action:**  [backup-gateway:GetHypervisor](#list_backup-gateway-action-GetHypervisor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHypervisorPropertyMappings  **
  - **IAM action:**  [backup-gateway:GetHypervisorPropertyMappings](#list_backup-gateway-action-GetHypervisorPropertyMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVirtualMachine  **
  - **IAM action:**  [backup-gateway:GetVirtualMachine](#list_backup-gateway-action-GetVirtualMachine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportHypervisorConfiguration  **
  - **IAM action:**  [backup-gateway:ImportHypervisorConfiguration](#list_backup-gateway-action-ImportHypervisorConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [backup-gateway:TagResource](#list_backup-gateway-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListGateways  **
  - **IAM action:**  [backup-gateway:ListGateways](#list_backup-gateway-action-ListGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListHypervisors  **
  - **IAM action:**  [backup-gateway:ListHypervisors](#list_backup-gateway-action-ListHypervisors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [backup-gateway:ListTagsForResource](#list_backup-gateway-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVirtualMachines  **
  - **IAM action:**  [backup-gateway:ListVirtualMachines](#list_backup-gateway-action-ListVirtualMachines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutBandwidthRateLimitSchedule  **
  - **IAM action:**  [backup-gateway:PutBandwidthRateLimitSchedule](#list_backup-gateway-action-PutBandwidthRateLimitSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutHypervisorPropertyMappings  **
  - **IAM action:**  [backup-gateway:PutHypervisorPropertyMappings](#list_backup-gateway-action-PutHypervisorPropertyMappings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup-gateway.amazonaws.com / **Access level:** Write

- **   PutMaintenanceStartTime  **
  - **IAM action:**  [backup-gateway:PutMaintenanceStartTime](#list_backup-gateway-action-PutMaintenanceStartTime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartVirtualMachinesMetadataSync  **
  - **IAM action:**  [backup-gateway:StartVirtualMachinesMetadataSync](#list_backup-gateway-action-StartVirtualMachinesMetadataSync)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** backup-gateway.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [backup-gateway:TagResource](#list_backup-gateway-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestHypervisorConfiguration  **
  - **IAM action:**  [backup-gateway:TestHypervisorConfiguration](#list_backup-gateway-action-TestHypervisorConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [backup-gateway:UntagResource](#list_backup-gateway-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateGatewayInformation  **
  - **IAM action:**  [backup-gateway:UpdateGatewayInformation](#list_backup-gateway-action-UpdateGatewayInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGatewaySoftwareNow  **
  - **IAM action:**  [backup-gateway:UpdateGatewaySoftwareNow](#list_backup-gateway-action-UpdateGatewaySoftwareNow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHypervisor  **
  - **IAM action:**  [backup-gateway:UpdateHypervisor](#list_backup-gateway-action-UpdateHypervisor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Backup Gateway
<a name="list_backup-gateway-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateGatewayToServer](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_AssociateGatewayToServer.html)  **
  - **Description:** Grants permission to AssociateGatewayToServer
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartBackupJob.html)  **
  - **Description:** Grants permission to Backup
  - **Resource types (\*required):** [virtualmachine\*](#list_backup-gateway-resource-virtualmachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_CreateGateway.html)  **
  - **Description:** Grants permission to to CreateGateway
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-gateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_DeleteGateway.html)  **
  - **Description:** Grants permission to DeleteGateway
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_DeleteHypervisor.html)  **
  - **Description:** Grants permission to DeleteHypervisor
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateGatewayFromServer](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_DisassociateGatewayFromServer.html)  **
  - **Description:** Grants permission to DisassociateGatewayFromServer
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBandwidthRateLimitSchedule](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetBandwidthRateLimitSchedule.html)  **
  - **Description:** Grants permission to GetBandwidthRateLimitSchedule
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetGateway.html)  **
  - **Description:** Grants permission to GetGateway
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetHypervisor.html)  **
  - **Description:** Grants permission to GetHypervisor
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHypervisorPropertyMappings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetHypervisorPropertyMappings.html)  **
  - **Description:** Grants permission to GetHypervisorPropertyMappings
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVirtualMachine](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_GetVirtualMachine.html)  **
  - **Description:** Grants permission to GetVirtualMachine
  - **Resource types (\*required):** [virtualmachine\*](#list_backup-gateway-resource-virtualmachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportHypervisorConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ImportHypervisorConfiguration.html)  **
  - **Description:** Grants permission to ImportHypervisorConfiguration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-gateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Access level:** Write

- **   [ListGateways](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html)  **
  - **Description:** Grants permission to ListGateways
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListHypervisors](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListHypervisors.html)  **
  - **Description:** Grants permission to ListHypervisors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListTagsForResource.html)  **
  - **Description:** Grants permission to ListTagsForResource
  - **Resource types (\*required):** [gateway](#list_backup-gateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hypervisor](#list_backup-gateway-resource-hypervisor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [virtualmachine](#list_backup-gateway-resource-virtualmachine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVirtualMachines](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListVirtualMachines.html)  **
  - **Description:** Grants permission to ListVirtualMachines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutBandwidthRateLimitSchedule](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_PutBandwidthRateLimitSchedule.html)  **
  - **Description:** Grants permission to PutBandwidthRateLimitSchedule
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutHypervisorPropertyMappings](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_PutHypervisorPropertyMappings.html)  **
  - **Description:** Grants permission to PutHypervisorPropertyMappings
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutMaintenanceStartTime](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_PutMaintenanceStartTime.html)  **
  - **Description:** Grants permission to PutMaintenanceStartTime
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Restore](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_StartRestoreJob.html)  **
  - **Description:** Grants permission to Restore
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartVirtualMachinesMetadataSync](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_StartVirtualMachinesMetadataSync.html)  **
  - **Description:** Grants permission to StartVirtualMachinesMetadataSync
  - **Resource types (\*required):** [hypervisor\*](#list_backup-gateway-resource-hypervisor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_TagResource.html)  **
  - **Description:** Grants permission to TagResource
  - **Resource types (\*required):** [gateway](#list_backup-gateway-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-gateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Resource types (\*required):** [hypervisor](#list_backup-gateway-resource-hypervisor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-gateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Resource types (\*required):** [virtualmachine](#list_backup-gateway-resource-virtualmachine) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_backup-gateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestHypervisorConfiguration](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_TestHypervisorConfiguration.html)  **
  - **Description:** Grants permission to TestHypervisorConfiguration
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UntagResource.html)  **
  - **Description:** Grants permission to UntagResource
  - **Resource types (\*required):** [gateway](#list_backup-gateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Resource types (\*required):** [hypervisor](#list_backup-gateway-resource-hypervisor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Resource types (\*required):** [virtualmachine](#list_backup-gateway-resource-virtualmachine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_backup-gateway-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateGatewayInformation](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UpdateGatewayInformation.html)  **
  - **Description:** Grants permission to UpdateGatewayInformation
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewaySoftwareNow](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UpdateGatewaySoftwareNow.html)  **
  - **Description:** Grants permission to UpdateGatewaySoftwareNow
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_UpdateHypervisor.html)  **
  - **Description:** Grants permission to UpdateHypervisor
  - **Resource types (\*required):** [gateway\*](#list_backup-gateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Backup Gateway
<a name="list_backup-gateway-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Gateway.html)  | arn:${Partition}:backup-gateway:${Region}:${Account}:gateway/${GatewayId} | [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_) | 
|  [hypervisor](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_Hypervisor.html)  | arn:${Partition}:backup-gateway:${Region}:${Account}:hypervisor/${HypervisorId} | [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_) | 
|  [virtualmachine](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_VirtualMachine.html)  | arn:${Partition}:backup-gateway:${Region}:${Account}:vm/${VirtualmachineId} | [aws:ResourceTag/${TagKey}](#list_backup-gateway-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Backup Gateway
<a name="list_backup-gateway-policy-keys"></a>

AWS Backup Gateway defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 