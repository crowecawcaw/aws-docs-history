

# Actions, resources, and condition keys for AWS Service - Oracle Database@AWS
<a name="list_odb"></a>

AWS Service - Oracle Database@AWS (service prefix: `odb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/odb/latest/UserGuide/what-is-odb.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/odb/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/odb/latest/UserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/odb/odb.json) for this service.

**Topics**
+ [API operations defined by AWS Service - Oracle Database@AWS](#list_odb-operations)
+ [Actions defined by AWS Service - Oracle Database@AWS](#list_odb-actions-as-permissions)
+ [Permission-only actions for AWS Service - Oracle Database@AWS](#list_odb-permission-only-actions)
+ [Resource types defined by AWS Service - Oracle Database@AWS](#list_odb-resources-for-iam-policies)
+ [Condition keys for AWS Service - Oracle Database@AWS](#list_odb-policy-keys)

## API operations defined by AWS Service - Oracle Database@AWS
<a name="list_odb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_odb-actions-as-permissions).




- **   AcceptMarketplaceRegistration  **
  - **IAM action:**  [odb:AcceptMarketplaceRegistration](#list_odb-action-AcceptMarketplaceRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateIamRoleToResource  **
  - **IAM action:**  [odb:AssociateIamRoleToResource](#list_odb-action-AssociateIamRoleToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** odb.amazonaws.com / **Access level:** Write

- **   CreateAutonomousDatabase  **
  - **IAM action:**  [odb:CreateAutonomousDatabase](#list_odb-action-CreateAutonomousDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAutonomousDatabaseBackup  **
  - **IAM action:**  [odb:CreateAutonomousDatabaseBackup](#list_odb-action-CreateAutonomousDatabaseBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAutonomousDatabaseWallet  **
  - **IAM action:**  [odb:CreateAutonomousDatabaseWallet](#list_odb-action-CreateAutonomousDatabaseWallet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** odb.amazonaws.com / **Access level:** Write

- **   CreateCloudAutonomousVmCluster  **
  - **IAM action:**  [odb:CreateCloudAutonomousVmCluster](#list_odb-action-CreateCloudAutonomousVmCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCloudExadataInfrastructure  **
  - **IAM action:**  [odb:CreateCloudExadataInfrastructure](#list_odb-action-CreateCloudExadataInfrastructure)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCloudVmCluster  **
  - **IAM action:**  [odb:CreateCloudVmCluster](#list_odb-action-CreateCloudVmCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:CreateDbNode](#list_odb-action-CreateDbNode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateExascaleDbStorageVault  **
  - **IAM action:**  [odb:CreateExascaleDbStorageVault](#list_odb-action-CreateExascaleDbStorageVault)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOdbNetwork  **
  - **IAM action:**  [odb:CreateOdbNetwork](#list_odb-action-CreateOdbNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOdbPeeringConnection  **
  - **IAM action:**  [odb:CreateOdbPeeringConnection](#list_odb-action-CreateOdbPeeringConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAutonomousDatabase  **
  - **IAM action:**  [odb:DeleteAutonomousDatabase](#list_odb-action-DeleteAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAutonomousDatabaseBackup  **
  - **IAM action:**  [odb:DeleteAutonomousDatabaseBackup](#list_odb-action-DeleteAutonomousDatabaseBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudAutonomousVmCluster  **
  - **IAM action:**  [odb:DeleteCloudAutonomousVmCluster](#list_odb-action-DeleteCloudAutonomousVmCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudExadataInfrastructure  **
  - **IAM action:**  [odb:DeleteCloudExadataInfrastructure](#list_odb-action-DeleteCloudExadataInfrastructure) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudVmCluster  **
  - **IAM action:**  [odb:DeleteCloudVmCluster](#list_odb-action-DeleteCloudVmCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [odb:DeleteDbNode](#list_odb-action-DeleteDbNode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteExascaleDbStorageVault  **
  - **IAM action:**  [odb:DeleteExascaleDbStorageVault](#list_odb-action-DeleteExascaleDbStorageVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOdbNetwork  **
  - **IAM action:**  [odb:DeleteOdbNetwork](#list_odb-action-DeleteOdbNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOdbPeeringConnection  **
  - **IAM action:**  [odb:DeleteOdbPeeringConnection](#list_odb-action-DeleteOdbPeeringConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateIamRoleFromResource  **
  - **IAM action:**  [odb:DisassociateIamRoleFromResource](#list_odb-action-DisassociateIamRoleFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateVirtualMachinesFromExadbVmCluster  **
  - **IAM action:**  [odb:DisassociateVirtualMachinesFromExadbVmCluster](#list_odb-action-DisassociateVirtualMachinesFromExadbVmCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FailoverAutonomousDatabase  **
  - **IAM action:**  [odb:FailoverAutonomousDatabase](#list_odb-action-FailoverAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAutonomousDatabase  **
  - **IAM action:**  [odb:GetAutonomousDatabase](#list_odb-action-GetAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutonomousDatabaseBackup  **
  - **IAM action:**  [odb:GetAutonomousDatabaseBackup](#list_odb-action-GetAutonomousDatabaseBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutonomousDatabaseWalletDetails  **
  - **IAM action:**  [odb:GetAutonomousDatabaseWalletDetails](#list_odb-action-GetAutonomousDatabaseWalletDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudAutonomousVmCluster  **
  - **IAM action:**  [odb:GetCloudAutonomousVmCluster](#list_odb-action-GetCloudAutonomousVmCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudExadataInfrastructure  **
  - **IAM action:**  [odb:GetCloudExadataInfrastructure](#list_odb-action-GetCloudExadataInfrastructure) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudExadataInfrastructureUnallocatedResources  **
  - **IAM action:**  [odb:GetCloudExadataInfrastructureUnallocatedResources](#list_odb-action-GetCloudExadataInfrastructureUnallocatedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudVmCluster  **
  - **IAM action:**  [odb:GetCloudVmCluster](#list_odb-action-GetCloudVmCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDbNode  **
  - **IAM action:**  [odb:GetDbNode](#list_odb-action-GetDbNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDbServer  **
  - **IAM action:**  [odb:GetDbServer](#list_odb-action-GetDbServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExadbVmCluster  **
  - **IAM action:**  [odb:GetExadbVmCluster](#list_odb-action-GetExadbVmCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExascaleDbStorageVault  **
  - **IAM action:**  [odb:GetExascaleDbStorageVault](#list_odb-action-GetExascaleDbStorageVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOciOnboardingStatus  **
  - **IAM action:**  [odb:GetOciOnboardingStatus](#list_odb-action-GetOciOnboardingStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOdbNetwork  **
  - **IAM action:**  [odb:GetOdbNetwork](#list_odb-action-GetOdbNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOdbPeeringConnection  **
  - **IAM action:**  [odb:GetOdbPeeringConnection](#list_odb-action-GetOdbPeeringConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitializeService  **
  - **IAM action:**  [odb:InitializeService](#list_odb-action-InitializeService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAutonomousDatabaseBackups  **
  - **IAM action:**  [odb:ListAutonomousDatabaseBackups](#list_odb-action-ListAutonomousDatabaseBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutonomousDatabaseCharacterSets  **
  - **IAM action:**  [odb:ListAutonomousDatabaseCharacterSets](#list_odb-action-ListAutonomousDatabaseCharacterSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutonomousDatabaseClones  **
  - **IAM action:**  [odb:ListAutonomousDatabaseClones](#list_odb-action-ListAutonomousDatabaseClones) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutonomousDatabasePeers  **
  - **IAM action:**  [odb:ListAutonomousDatabasePeers](#list_odb-action-ListAutonomousDatabasePeers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutonomousDatabaseVersions  **
  - **IAM action:**  [odb:ListAutonomousDatabaseVersions](#list_odb-action-ListAutonomousDatabaseVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutonomousDatabases  **
  - **IAM action:**  [odb:ListAutonomousDatabases](#list_odb-action-ListAutonomousDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutonomousVirtualMachines  **
  - **IAM action:**  [odb:ListAutonomousVirtualMachines](#list_odb-action-ListAutonomousVirtualMachines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudAutonomousVmClusters  **
  - **IAM action:**  [odb:ListCloudAutonomousVmClusters](#list_odb-action-ListCloudAutonomousVmClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudExadataInfrastructures  **
  - **IAM action:**  [odb:ListCloudExadataInfrastructures](#list_odb-action-ListCloudExadataInfrastructures) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudVmClusters  **
  - **IAM action:**  [odb:ListCloudVmClusters](#list_odb-action-ListCloudVmClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDbNodes  **
  - **IAM action:**  [odb:ListDbNodes](#list_odb-action-ListDbNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDbServers  **
  - **IAM action:**  [odb:ListDbServers](#list_odb-action-ListDbServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDbSystemShapes  **
  - **IAM action:**  [odb:ListDbSystemShapes](#list_odb-action-ListDbSystemShapes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExadbVmClusters  **
  - **IAM action:**  [odb:ListExadbVmClusters](#list_odb-action-ListExadbVmClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExascaleDbStorageVaults  **
  - **IAM action:**  [odb:ListExascaleDbStorageVaults](#list_odb-action-ListExascaleDbStorageVaults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlexComponents  **
  - **IAM action:**  [odb:ListFlexComponents](#list_odb-action-ListFlexComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGiMinorVersions  **
  - **IAM action:**  [odb:ListGiMinorVersions](#list_odb-action-ListGiMinorVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGiVersions  **
  - **IAM action:**  [odb:ListGiVersions](#list_odb-action-ListGiVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOdbNetworks  **
  - **IAM action:**  [odb:ListOdbNetworks](#list_odb-action-ListOdbNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOdbPeeringConnections  **
  - **IAM action:**  [odb:ListOdbPeeringConnections](#list_odb-action-ListOdbPeeringConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSystemVersions  **
  - **IAM action:**  [odb:ListSystemVersions](#list_odb-action-ListSystemVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [odb:ListTagsForResource](#list_odb-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RebootAutonomousDatabase  **
  - **IAM action:**  [odb:RebootAutonomousDatabase](#list_odb-action-RebootAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootDbNode  **
  - **IAM action:**  [odb:RebootDbNode](#list_odb-action-RebootDbNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreAutonomousDatabase  **
  - **IAM action:**  [odb:RestoreAutonomousDatabase](#list_odb-action-RestoreAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ShrinkAutonomousDatabase  **
  - **IAM action:**  [odb:ShrinkAutonomousDatabase](#list_odb-action-ShrinkAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutonomousDatabase  **
  - **IAM action:**  [odb:StartAutonomousDatabase](#list_odb-action-StartAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDbNode  **
  - **IAM action:**  [odb:StartDbNode](#list_odb-action-StartDbNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAutonomousDatabase  **
  - **IAM action:**  [odb:StopAutonomousDatabase](#list_odb-action-StopAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDbNode  **
  - **IAM action:**  [odb:StopDbNode](#list_odb-action-StopDbNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SwitchoverAutonomousDatabase  **
  - **IAM action:**  [odb:SwitchoverAutonomousDatabase](#list_odb-action-SwitchoverAutonomousDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [odb:TagResource](#list_odb-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [odb:UntagResource](#list_odb-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAutonomousDatabase  **
  - **IAM action:**  [odb:UpdateAutonomousDatabase](#list_odb-action-UpdateAutonomousDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** odb.amazonaws.com / **Access level:** Write

- **   UpdateAutonomousDatabaseBackup  **
  - **IAM action:**  [odb:UpdateAutonomousDatabaseBackup](#list_odb-action-UpdateAutonomousDatabaseBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCloudExadataInfrastructure  **
  - **IAM action:**  [odb:UpdateCloudExadataInfrastructure](#list_odb-action-UpdateCloudExadataInfrastructure) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExadbVmCluster  **
  - **IAM action:**  [odb:UpdateExadbVmCluster](#list_odb-action-UpdateExadbVmCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExascaleDbStorageVault  **
  - **IAM action:**  [odb:UpdateExascaleDbStorageVault](#list_odb-action-UpdateExascaleDbStorageVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOdbNetwork  **
  - **IAM action:**  [odb:UpdateOdbNetwork](#list_odb-action-UpdateOdbNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOdbPeeringConnection  **
  - **IAM action:**  [odb:UpdateOdbPeeringConnection](#list_odb-action-UpdateOdbPeeringConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Service - Oracle Database@AWS
<a name="list_odb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptMarketplaceRegistration](https://docs.aws.amazon.com/odb/latest/APIReference/API_AcceptMarketplaceRegistration.html)  **
  - **Description:** Grants permission to register the Amazon Web Services Marketplace token for your Amazon Web Services account to activate your Oracle Database@Amazon Web Services subscription
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateIamRoleToResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_AssociateIamRoleToResource.html)  **
  - **Description:** Grants permission to associate an AWS Identity and Access Management (IAM) service role with a specified resource to enable AWS service integration
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-vm-cluster](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateVirtualMachinesToExadbVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_AssociateVirtualMachinesToExadbVmCluster.html)  **
  - **Description:** Grants permission to associate virtual machines to a specified Exadb VM cluster
  - **Resource types (\*required):** [exadb-vm-cluster\*](#list_odb-resource-exadb-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateAutonomousDatabase.html)  **
  - **Description:** Grants permission to create an Autonomous Database
  - **Resource types (\*required):** [odb-network](#list_odb-resource-odb-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAutonomousDatabaseBackup](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateAutonomousDatabaseBackup.html)  **
  - **Description:** Grants permission to create a backup of the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAutonomousDatabaseWallet](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateAutonomousDatabaseWallet.html)  **
  - **Description:** Grants permission to create a wallet for the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudAutonomousVmCluster.html)  **
  - **Description:** Grants permission to create an Autonomous VM cluster in the specified Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudExadataInfrastructure.html)  **
  - **Description:** Grants permission to create an Exadata infrastructure
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudVmCluster.html)  **
  - **Description:** Grants permission to create a VM cluster on the specified Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExadbVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateExadbVmCluster.html)  **
  - **Description:** Grants permission to create an Exadb VM cluster in the specified Exascale DB storage vault
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExascaleDbStorageVault](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateExascaleDbStorageVault.html)  **
  - **Description:** Grants permission to create an Exascale DB storage vault
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateOdbNetwork.html)  **
  - **Description:** Grants permission to create an ODB network
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateOdbPeeringConnection.html)  **
  - **Description:** Grants permission to create an ODB Peering Connection
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteAutonomousDatabase.html)  **
  - **Description:** Grants permission to delete the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAutonomousDatabaseBackup](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteAutonomousDatabaseBackup.html)  **
  - **Description:** Grants permission to delete the specified Autonomous Database backup
  - **Resource types (\*required):** [autonomous-database-backup\*](#list_odb-resource-autonomous-database-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteCloudAutonomousVmCluster.html)  **
  - **Description:** Grants permission to Deletes an Autonomous VM cluster
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster\*](#list_odb-resource-cloud-autonomous-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteCloudExadataInfrastructure.html)  **
  - **Description:** Grants permission to delete a specified Exadata infrastructure. Before you use this operation, make sure to delete all of the VM clusters that are hosted on this Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteCloudVmCluster.html)  **
  - **Description:** Grants permission to delete a specified VM cluster
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExadbVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteExadbVmCluster.html)  **
  - **Description:** Grants permission to delete a specified Exadb VM cluster
  - **Resource types (\*required):** [exadb-vm-cluster\*](#list_odb-resource-exadb-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExascaleDbStorageVault](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteExascaleDbStorageVault.html)  **
  - **Description:** Grants permission to delete a specified Exascale DB storage vault
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteOdbNetwork.html)  **
  - **Description:** Grants permission to delete the specified ODB network
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_DeleteOdbPeeringConnection.html)  **
  - **Description:** Grants permission to delete the specified ODB Peering Connection. When you delete an ODB peering connection, the underlying VPC peering connection is also deleted
  - **Resource types (\*required):** [odb-peering-connection\*](#list_odb-resource-odb-peering-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateIamRoleFromResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_DisassociateIamRoleFromResource.html)  **
  - **Description:** Grants permission to disassociate an AWS Identity and Access Management (IAM) service role from a specified resource to disable AWS service integration
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-vm-cluster](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateVirtualMachinesFromExadbVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_DisassociateVirtualMachinesFromExadbVmCluster.html)  **
  - **Description:** Grants permission to disassociate virtual machines from a specified Exadb VM cluster
  - **Resource types (\*required):** [exadb-vm-cluster\*](#list_odb-resource-exadb-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [FailoverAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_FailoverAutonomousDatabase.html)  **
  - **Description:** Grants permission to fail over the specified Autonomous Database to a standby peer database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetAutonomousDatabase.html)  **
  - **Description:** Grants permission to get information about a specific Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutonomousDatabaseBackup](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetAutonomousDatabaseBackup.html)  **
  - **Description:** Grants permission to get information about a specific Autonomous Database backup
  - **Resource types (\*required):** [autonomous-database-backup\*](#list_odb-resource-autonomous-database-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutonomousDatabaseWalletDetails](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetAutonomousDatabaseWalletDetails.html)  **
  - **Description:** Grants permission to get the wallet details for the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudAutonomousVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudAutonomousVmCluster.html)  **
  - **Description:** Grants permission to get information about a specific Autonomous VM cluster
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster\*](#list_odb-resource-cloud-autonomous-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudExadataInfrastructure.html)  **
  - **Description:** Grants permission to get information about the specified Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudExadataInfrastructureUnallocatedResources](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudExadataInfrastructureUnallocatedResources.html)  **
  - **Description:** Grants permission to retrieve information about unallocated resources in a specified Cloud Exadata Infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudVmCluster.html)  **
  - **Description:** Grants permission to get information about the specified VM cluster
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetDbNode.html)  **
  - **Description:** Grants permission to get information about the specified DB node
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-node\*](#list_odb-resource-db-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDbServer](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetDbServer.html)  **
  - **Description:** Grants permission to get information about the specified database server
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExadbVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetExadbVmCluster.html)  **
  - **Description:** Grants permission to get information about a specified Exadb VM cluster
  - **Resource types (\*required):** [exadb-vm-cluster\*](#list_odb-resource-exadb-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExascaleDbStorageVault](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetExascaleDbStorageVault.html)  **
  - **Description:** Grants permission to get information about a specified Exascale DB storage vault
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOciOnboardingStatus](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOciOnboardingStatus.html)  **
  - **Description:** Grants permission to get the tenancy activation link and onboarding status for your Amazon Web Services account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOdbNetwork.html)  **
  - **Description:** Grants permission to get information about the specified ODB network
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_GetOdbPeeringConnection.html)  **
  - **Description:** Grants permission to get information about the specified ODB Peering connection
  - **Resource types (\*required):** [odb-peering-connection\*](#list_odb-resource-odb-peering-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InitializeService](https://docs.aws.amazon.com/odb/latest/APIReference/API_InitializeService.html)  **
  - **Description:** Grants permission to initialize the ODB service for the first time in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListAutonomousDatabaseBackups](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseBackups.html)  **
  - **Description:** Grants permission to list information about the backups of the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAutonomousDatabaseCharacterSets](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseCharacterSets.html)  **
  - **Description:** Grants permission to list information about the character sets that are available for Autonomous Databases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutonomousDatabaseClones](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseClones.html)  **
  - **Description:** Grants permission to list all clones of the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAutonomousDatabasePeers](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabasePeers.html)  **
  - **Description:** Grants permission to list all peer databases of the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAutonomousDatabaseVersions](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseVersions.html)  **
  - **Description:** Grants permission to list information about the Oracle Database software versions that are available for Autonomous Databases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutonomousDatabases](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabases.html)  **
  - **Description:** Grants permission to list information about the Autonomous Databases owned by your Amazon Web Services account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutonomousVirtualMachines](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousVirtualMachines.html)  **
  - **Description:** Grants permission to list all Autonomous VMs in an Autonomous VM cluster
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster](#list_odb-resource-cloud-autonomous-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCloudAutonomousVmClusters](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudAutonomousVmClusters.html)  **
  - **Description:** Grants permission to list all Autonomous VM clusters in a specified Cloud Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCloudExadataInfrastructures](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudExadataInfrastructures.html)  **
  - **Description:** Grants permission to list information about the Exadata infrastructures owned by your Amazon Web Services account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCloudVmClusters](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudVmClusters.html)  **
  - **Description:** Grants permission to list information about the VM clusters owned by your Amazon Web Services account or only the ones on the specified Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDbNodes](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbNodes.html)  **
  - **Description:** Grants permission to list information about the DB nodes for the specified VM cluster
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDbServers](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbServers.html)  **
  - **Description:** Grants permission to list information about the database servers that belong to the specified Exadata infrastructure
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDbSystemShapes](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListDbSystemShapes.html)  **
  - **Description:** Grants permission to list information about the shapes that are available for an Exadata infrastructure
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExadbVmClusters](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListExadbVmClusters.html)  **
  - **Description:** Grants permission to list information about the Exadb VM clusters owned by your Amazon Web Services account or only the ones in the specified Exascale DB storage vault
  - **Resource types (\*required):** [exascale-db-storage-vault](#list_odb-resource-exascale-db-storage-vault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExascaleDbStorageVaults](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListExascaleDbStorageVaults.html)  **
  - **Description:** Grants permission to list information about the Exascale DB storage vaults owned by your Amazon Web Services account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFlexComponents](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListFlexComponents.html)  **
  - **Description:** Grants permission to list information about the flex components that are available for a DB system shape
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGiMinorVersions](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListGiMinorVersions.html)  **
  - **Description:** Grants permission to list information about the minor versions of Oracle Grid Infrastructure (GI) software that are available for a VM cluster for the specified GI version and shape
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGiVersions](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListGiVersions.html)  **
  - **Description:** Grants permission to list information about Oracle Grid Infrastructure (GI) software versions that are available for a VM cluster for the specified shape
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOdbNetworks](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListOdbNetworks.html)  **
  - **Description:** Grants permission to list information about the ODB networks owned by your Amazon Web Services account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOdbPeeringConnections](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListOdbPeeringConnections.html)  **
  - **Description:** Grants permission to list all ODB peering connections or those associated with a specific ODB network
  - **Resource types (\*required):** [odb-network](#list_odb-resource-odb-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSystemVersions](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListSystemVersions.html)  **
  - **Description:** Grants permission to list information about the system versions that are available for a VM cluster for the specified giVersion and shape
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list information about the tags applied to this resource
  - **Resource types (\*required):** [autonomous-database](#list_odb-resource-autonomous-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [autonomous-database-backup](#list_odb-resource-autonomous-database-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-exadata-infrastructure](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-vm-cluster](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-node](#list_odb-resource-db-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [exadb-vm-cluster](#list_odb-resource-exadb-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [exascale-db-storage-vault](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [odb-network](#list_odb-resource-odb-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [odb-peering-connection](#list_odb-resource-odb-peering-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RebootAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_RebootAutonomousDatabase.html)  **
  - **Description:** Grants permission to reboot the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RebootDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_RebootDbNode.html)  **
  - **Description:** Grants permission to reboot the specified DB node in a VM cluster
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-node\*](#list_odb-resource-db-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_RestoreAutonomousDatabase.html)  **
  - **Description:** Grants permission to restore the specified Autonomous Database to a point in time
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ShrinkAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_ShrinkAutonomousDatabase.html)  **
  - **Description:** Grants permission to shrink the storage of the specified Autonomous Database to reclaim unused space
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_StartAutonomousDatabase.html)  **
  - **Description:** Grants permission to start the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_StartDbNode.html)  **
  - **Description:** Grants permission to start the specified DB node in a VM cluster
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-node\*](#list_odb-resource-db-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_StopAutonomousDatabase.html)  **
  - **Description:** Grants permission to stop the specified Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDbNode](https://docs.aws.amazon.com/odb/latest/APIReference/API_StopDbNode.html)  **
  - **Description:** Grants permission to stop the specified DB node in a VM cluster
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [db-node\*](#list_odb-resource-db-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SwitchoverAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_SwitchoverAutonomousDatabase.html)  **
  - **Description:** Grants permission to switch over the specified Autonomous Database to a standby peer database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to apply tags to the specified resource
  - **Resource types (\*required):** [autonomous-database](#list_odb-resource-autonomous-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [autonomous-database-backup](#list_odb-resource-autonomous-database-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [cloud-exadata-infrastructure](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [cloud-vm-cluster](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [db-node](#list_odb-resource-db-node) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [exadb-vm-cluster](#list_odb-resource-exadb-vm-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [exascale-db-storage-vault](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-network](#list_odb-resource-odb-network) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-peering-connection](#list_odb-resource-odb-peering-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_odb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/odb/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified resource
  - **Resource types (\*required):** [autonomous-database](#list_odb-resource-autonomous-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [autonomous-database-backup](#list_odb-resource-autonomous-database-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [cloud-exadata-infrastructure](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [cloud-vm-cluster](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [db-node](#list_odb-resource-db-node) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [exadb-vm-cluster](#list_odb-resource-exadb-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [exascale-db-storage-vault](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-network](#list_odb-resource-odb-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Resource types (\*required):** [odb-peering-connection](#list_odb-resource-odb-peering-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_odb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAutonomousDatabase](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateAutonomousDatabase.html)  **
  - **Description:** Grants permission to update the properties of an Autonomous Database
  - **Resource types (\*required):** [autonomous-database\*](#list_odb-resource-autonomous-database)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutonomousDatabaseBackup](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateAutonomousDatabaseBackup.html)  **
  - **Description:** Grants permission to update the properties of an Autonomous Database backup
  - **Resource types (\*required):** [autonomous-database-backup\*](#list_odb-resource-autonomous-database-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCloudExadataInfrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateCloudExadataInfrastructure.html)  **
  - **Description:** Grants permission to update the properties of an Exadata infrastructure resource
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExadbVmCluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateExadbVmCluster.html)  **
  - **Description:** Grants permission to update properties of a specified Exadb VM cluster
  - **Resource types (\*required):** [exadb-vm-cluster\*](#list_odb-resource-exadb-vm-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExascaleDbStorageVault](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateExascaleDbStorageVault.html)  **
  - **Description:** Grants permission to update properties of a specified Exascale DB storage vault
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOdbNetwork](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateOdbNetwork.html)  **
  - **Description:** Grants permission to update properties of a specified ODB network
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOdbPeeringConnection](https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateOdbPeeringConnection.html)  **
  - **Description:** Grants permission to update properties of a specified ODB Peering Connection
  - **Resource types (\*required):** [odb-peering-connection\*](#list_odb-resource-odb-peering-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Service - Oracle Database@AWS
<a name="list_odb-permission-only-actions"></a>

The following actions are defined by AWS Service - Oracle Database@AWS but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateDbNode](API_CreateDbNode.html)  **
  - **Description:** Grants permission to create a DB Node
  - **Resource types (\*required):** [db-node\*](#list_odb-resource-db-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGrantShare](API_CreateGrantShare.html)  **
  - **Description:** Grants permission to create an ODB Grant Share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOutboundIntegration](API_CreateOutboundIntegration.html)  **
  - **Description:** Grants permission to create an Outbound Integration
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster\*](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDbNode](API_DeleteDbNode.html)  **
  - **Description:** Grants permission to delete a DB Node
  - **Resource types (\*required):** [db-node\*](#list_odb-resource-db-node)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGrantShare](API_DeleteGrantShare.html)  **
  - **Description:** Grants permission to delete an ODB Grant Share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetResourcePolicy](API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get a resource policy
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to update a resource policy
  - **Resource types (\*required):** [cloud-exadata-infrastructure\*](#list_odb-resource-cloud-exadata-infrastructure) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [exascale-db-storage-vault\*](#list_odb-resource-exascale-db-storage-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [odb-network\*](#list_odb-resource-odb-network) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGrantShare](API_UpdateGrantShare.html)  **
  - **Description:** Grants permission to update an ODB Grant Share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOutboundIntegration](API_UpdateOutboundIntegration.html)  **
  - **Description:** Grants permission to update an Outbound Integration
  - **Resource types (\*required):** [cloud-autonomous-vm-cluster\*](#list_odb-resource-cloud-autonomous-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cloud-vm-cluster\*](#list_odb-resource-cloud-vm-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Service - Oracle Database@AWS
<a name="list_odb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [autonomous-database](https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabase.html)  | arn:${Partition}:odb:${Region}:${Account}:autonomous-database/${AutonomousDatabaseId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [autonomous-database-backup](https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabaseBackup.html)  | arn:${Partition}:odb:${Region}:${Account}:autonomous-database-backup/${AutonomousDatabaseBackupId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [cloud-autonomous-vm-cluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudAutonomousVmCluster.html)  | arn:${Partition}:odb:${Region}:${Account}:cloud-autonomous-vm-cluster/${CloudAutonomousVmClusterId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [cloud-exadata-infrastructure](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudExadataInfrastructure.html)  | arn:${Partition}:odb:${Region}:${Account}:cloud-exadata-infrastructure/${CloudExadataInfrastructureId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [cloud-vm-cluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_CloudVmCluster.html)  | arn:${Partition}:odb:${Region}:${Account}:cloud-vm-cluster/${CloudVmClusterId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [db-node](https://docs.aws.amazon.com/odb/latest/APIReference/API_DbNode.html)  | arn:${Partition}:odb:${Region}:${Account}:db-node/${DbNodeId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [exadb-vm-cluster](https://docs.aws.amazon.com/odb/latest/APIReference/API_ExadbVmCluster.html)  | arn:${Partition}:odb:${Region}:${Account}:exadb-vm-cluster/${ExadbVmClusterId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [exascale-db-storage-vault](https://docs.aws.amazon.com/odb/latest/APIReference/API_ExascaleDbStorageVault.html)  | arn:${Partition}:odb:${Region}:${Account}:exascale-db-storage-vault/${ExascaleDbStorageVaultId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [odb-network](https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbNetwork.html)  | arn:${Partition}:odb:${Region}:${Account}:odb-network/${OdbNetworkId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 
|  [odb-peering-connection](https://docs.aws.amazon.com/odb/latest/APIReference/API_OdbPeeringConnection.html)  | arn:${Partition}:odb:${Region}:${Account}:odb-peering-connection/${OdbPeeringConnectionId} | [aws:ResourceTag/${TagKey}](#list_odb-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Service - Oracle Database@AWS
<a name="list_odb-policy-keys"></a>

AWS Service - Oracle Database@AWS defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 