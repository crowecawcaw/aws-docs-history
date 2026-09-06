

# Actions, resources, and condition keys for AWS Storage Gateway
<a name="list_storagegateway"></a>

AWS Storage Gateway (service prefix: `storagegateway`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/storagegateway/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/storagegateway/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/storagegateway/latest/userguide/UsingIAMWithStorageGateway.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/storagegateway/storagegateway.json) for this service.

**Topics**
+ [API operations defined by AWS Storage Gateway](#list_storagegateway-operations)
+ [Actions defined by AWS Storage Gateway](#list_storagegateway-actions-as-permissions)
+ [Resource types defined by AWS Storage Gateway](#list_storagegateway-resources-for-iam-policies)
+ [Condition keys for AWS Storage Gateway](#list_storagegateway-policy-keys)

## API operations defined by AWS Storage Gateway
<a name="list_storagegateway-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_storagegateway-actions-as-permissions).




- **   ActivateGateway  **
  - **IAM action:**  [storagegateway:ActivateGateway](#list_storagegateway-action-ActivateGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   AddCache  **
  - **IAM action:**  [storagegateway:AddCache](#list_storagegateway-action-AddCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTagsToResource  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AddUploadBuffer  **
  - **IAM action:**  [storagegateway:AddUploadBuffer](#list_storagegateway-action-AddUploadBuffer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddWorkingStorage  **
  - **IAM action:**  [storagegateway:AddWorkingStorage](#list_storagegateway-action-AddWorkingStorage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssignTapePool  **
  - **IAM action:**  [storagegateway:AssignTapePool](#list_storagegateway-action-AssignTapePool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [storagegateway:BypassGovernanceRetention](#list_storagegateway-action-BypassGovernanceRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AssociateFileSystem  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:AssociateFileSystem](#list_storagegateway-action-AssociateFileSystem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AttachVolume  **
  - **IAM action:**  [storagegateway:AttachVolume](#list_storagegateway-action-AttachVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelArchival  **
  - **IAM action:**  [storagegateway:CancelArchival](#list_storagegateway-action-CancelArchival) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelCacheReport  **
  - **IAM action:**  [storagegateway:CancelCacheReport](#list_storagegateway-action-CancelCacheReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelRetrieval  **
  - **IAM action:**  [storagegateway:CancelRetrieval](#list_storagegateway-action-CancelRetrieval) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCachediSCSIVolume  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateCachediSCSIVolume](#list_storagegateway-action-CreateCachediSCSIVolume)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateNFSFileShare  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateNFSFileShare](#list_storagegateway-action-CreateNFSFileShare)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSMBFileShare  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateSMBFileShare](#list_storagegateway-action-CreateSMBFileShare)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSnapshot  **
  - **IAM action:**  [storagegateway:CreateSnapshot](#list_storagegateway-action-CreateSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSnapshotFromVolumeRecoveryPoint  **
  - **IAM action:**  [storagegateway:CreateSnapshotFromVolumeRecoveryPoint](#list_storagegateway-action-CreateSnapshotFromVolumeRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStorediSCSIVolume  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateStorediSCSIVolume](#list_storagegateway-action-CreateStorediSCSIVolume)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTapePool  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateTapePool](#list_storagegateway-action-CreateTapePool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTapeWithBarcode  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateTapeWithBarcode](#list_storagegateway-action-CreateTapeWithBarcode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTapes  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:CreateTapes](#list_storagegateway-action-CreateTapes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAutomaticTapeCreationPolicy  **
  - **IAM action:**  [storagegateway:DeleteAutomaticTapeCreationPolicy](#list_storagegateway-action-DeleteAutomaticTapeCreationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBandwidthRateLimit  **
  - **IAM action:**  [storagegateway:DeleteBandwidthRateLimit](#list_storagegateway-action-DeleteBandwidthRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCacheReport  **
  - **IAM action:**  [storagegateway:DeleteCacheReport](#list_storagegateway-action-DeleteCacheReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChapCredentials  **
  - **IAM action:**  [storagegateway:DeleteChapCredentials](#list_storagegateway-action-DeleteChapCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFileShare  **
  - **IAM action:**  [storagegateway:DeleteFileShare](#list_storagegateway-action-DeleteFileShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGateway  **
  - **IAM action:**  [storagegateway:DeleteGateway](#list_storagegateway-action-DeleteGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSnapshotSchedule  **
  - **IAM action:**  [storagegateway:DeleteSnapshotSchedule](#list_storagegateway-action-DeleteSnapshotSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTape  **
  - **IAM action:**  [storagegateway:DeleteTape](#list_storagegateway-action-DeleteTape) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTapeArchive  **
  - **IAM action:**  [storagegateway:BypassGovernanceRetention](#list_storagegateway-action-BypassGovernanceRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [storagegateway:DeleteTapeArchive](#list_storagegateway-action-DeleteTapeArchive)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteTapePool  **
  - **IAM action:**  [storagegateway:DeleteTapePool](#list_storagegateway-action-DeleteTapePool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVolume  **
  - **IAM action:**  [storagegateway:DeleteVolume](#list_storagegateway-action-DeleteVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAvailabilityMonitorTest  **
  - **IAM action:**  [storagegateway:DescribeAvailabilityMonitorTest](#list_storagegateway-action-DescribeAvailabilityMonitorTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBandwidthRateLimit  **
  - **IAM action:**  [storagegateway:DescribeBandwidthRateLimit](#list_storagegateway-action-DescribeBandwidthRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBandwidthRateLimitSchedule  **
  - **IAM action:**  [storagegateway:DescribeBandwidthRateLimitSchedule](#list_storagegateway-action-DescribeBandwidthRateLimitSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCache  **
  - **IAM action:**  [storagegateway:DescribeCache](#list_storagegateway-action-DescribeCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCacheReport  **
  - **IAM action:**  [storagegateway:DescribeCacheReport](#list_storagegateway-action-DescribeCacheReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCachediSCSIVolumes  **
  - **IAM action:**  [storagegateway:DescribeCachediSCSIVolumes](#list_storagegateway-action-DescribeCachediSCSIVolumes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChapCredentials  **
  - **IAM action:**  [storagegateway:DescribeChapCredentials](#list_storagegateway-action-DescribeChapCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFileSystemAssociations  **
  - **IAM action:**  [storagegateway:DescribeFileSystemAssociations](#list_storagegateway-action-DescribeFileSystemAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGatewayInformation  **
  - **IAM action:**  [storagegateway:DescribeGatewayInformation](#list_storagegateway-action-DescribeGatewayInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMaintenanceStartTime  **
  - **IAM action:**  [storagegateway:DescribeMaintenanceStartTime](#list_storagegateway-action-DescribeMaintenanceStartTime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNFSFileShares  **
  - **IAM action:**  [storagegateway:DescribeNFSFileShares](#list_storagegateway-action-DescribeNFSFileShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSMBFileShares  **
  - **IAM action:**  [storagegateway:DescribeSMBFileShares](#list_storagegateway-action-DescribeSMBFileShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSMBSettings  **
  - **IAM action:**  [storagegateway:DescribeSMBSettings](#list_storagegateway-action-DescribeSMBSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshotSchedule  **
  - **IAM action:**  [storagegateway:DescribeSnapshotSchedule](#list_storagegateway-action-DescribeSnapshotSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStorediSCSIVolumes  **
  - **IAM action:**  [storagegateway:DescribeStorediSCSIVolumes](#list_storagegateway-action-DescribeStorediSCSIVolumes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTapeArchives  **
  - **IAM action:**  [storagegateway:DescribeTapeArchives](#list_storagegateway-action-DescribeTapeArchives) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTapeRecoveryPoints  **
  - **IAM action:**  [storagegateway:DescribeTapeRecoveryPoints](#list_storagegateway-action-DescribeTapeRecoveryPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTapes  **
  - **IAM action:**  [storagegateway:DescribeTapes](#list_storagegateway-action-DescribeTapes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUploadBuffer  **
  - **IAM action:**  [storagegateway:DescribeUploadBuffer](#list_storagegateway-action-DescribeUploadBuffer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVTLDevices  **
  - **IAM action:**  [storagegateway:DescribeVTLDevices](#list_storagegateway-action-DescribeVTLDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkingStorage  **
  - **IAM action:**  [storagegateway:DescribeWorkingStorage](#list_storagegateway-action-DescribeWorkingStorage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachVolume  **
  - **IAM action:**  [storagegateway:DetachVolume](#list_storagegateway-action-DetachVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableGateway  **
  - **IAM action:**  [storagegateway:DisableGateway](#list_storagegateway-action-DisableGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFileSystem  **
  - **IAM action:**  [storagegateway:DisassociateFileSystem](#list_storagegateway-action-DisassociateFileSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EvictFilesFailingUpload  **
  - **IAM action:**  [storagegateway:EvictFilesFailingUpload](#list_storagegateway-action-EvictFilesFailingUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   JoinDomain  **
  - **IAM action:**  [storagegateway:JoinDomain](#list_storagegateway-action-JoinDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAutomaticTapeCreationPolicies  **
  - **IAM action:**  [storagegateway:ListAutomaticTapeCreationPolicies](#list_storagegateway-action-ListAutomaticTapeCreationPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCacheReports  **
  - **IAM action:**  [storagegateway:ListCacheReports](#list_storagegateway-action-ListCacheReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFileShares  **
  - **IAM action:**  [storagegateway:ListFileShares](#list_storagegateway-action-ListFileShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFileSystemAssociations  **
  - **IAM action:**  [storagegateway:ListFileSystemAssociations](#list_storagegateway-action-ListFileSystemAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGateways  **
  - **IAM action:**  [storagegateway:ListGateways](#list_storagegateway-action-ListGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLocalDisks  **
  - **IAM action:**  [storagegateway:ListLocalDisks](#list_storagegateway-action-ListLocalDisks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [storagegateway:ListTagsForResource](#list_storagegateway-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTapePools  **
  - **IAM action:**  [storagegateway:ListTapePools](#list_storagegateway-action-ListTapePools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTapes  **
  - **IAM action:**  [storagegateway:ListTapes](#list_storagegateway-action-ListTapes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVolumeInitiators  **
  - **IAM action:**  [storagegateway:ListVolumeInitiators](#list_storagegateway-action-ListVolumeInitiators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVolumeRecoveryPoints  **
  - **IAM action:**  [storagegateway:ListVolumeRecoveryPoints](#list_storagegateway-action-ListVolumeRecoveryPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVolumes  **
  - **IAM action:**  [storagegateway:ListVolumes](#list_storagegateway-action-ListVolumes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   NotifyWhenUploaded  **
  - **IAM action:**  [storagegateway:NotifyWhenUploaded](#list_storagegateway-action-NotifyWhenUploaded) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RefreshCache  **
  - **IAM action:**  [storagegateway:RefreshCache](#list_storagegateway-action-RefreshCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **IAM action:**  [storagegateway:RemoveTagsFromResource](#list_storagegateway-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetCache  **
  - **IAM action:**  [storagegateway:ResetCache](#list_storagegateway-action-ResetCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetrieveTapeArchive  **
  - **IAM action:**  [storagegateway:RetrieveTapeArchive](#list_storagegateway-action-RetrieveTapeArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetrieveTapeRecoveryPoint  **
  - **IAM action:**  [storagegateway:RetrieveTapeRecoveryPoint](#list_storagegateway-action-RetrieveTapeRecoveryPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetLocalConsolePassword  **
  - **IAM action:**  [storagegateway:SetLocalConsolePassword](#list_storagegateway-action-SetLocalConsolePassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetSMBGuestPassword  **
  - **IAM action:**  [storagegateway:SetSMBGuestPassword](#list_storagegateway-action-SetSMBGuestPassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ShutdownGateway  **
  - **IAM action:**  [storagegateway:ShutdownGateway](#list_storagegateway-action-ShutdownGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAvailabilityMonitorTest  **
  - **IAM action:**  [storagegateway:StartAvailabilityMonitorTest](#list_storagegateway-action-StartAvailabilityMonitorTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCacheReport  **
  - **IAM action:**  [storagegateway:AddTagsToResource](#list_storagegateway-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [storagegateway:StartCacheReport](#list_storagegateway-action-StartCacheReport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartGateway  **
  - **IAM action:**  [storagegateway:StartGateway](#list_storagegateway-action-StartGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAutomaticTapeCreationPolicy  **
  - **IAM action:**  [storagegateway:UpdateAutomaticTapeCreationPolicy](#list_storagegateway-action-UpdateAutomaticTapeCreationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBandwidthRateLimit  **
  - **IAM action:**  [storagegateway:UpdateBandwidthRateLimit](#list_storagegateway-action-UpdateBandwidthRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBandwidthRateLimitSchedule  **
  - **IAM action:**  [storagegateway:UpdateBandwidthRateLimitSchedule](#list_storagegateway-action-UpdateBandwidthRateLimitSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChapCredentials  **
  - **IAM action:**  [storagegateway:UpdateChapCredentials](#list_storagegateway-action-UpdateChapCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFileSystemAssociation  **
  - **IAM action:**  [storagegateway:UpdateFileSystemAssociation](#list_storagegateway-action-UpdateFileSystemAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGatewayInformation  **
  - **IAM action:**  [storagegateway:UpdateGatewayInformation](#list_storagegateway-action-UpdateGatewayInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGatewaySoftwareNow  **
  - **IAM action:**  [storagegateway:UpdateGatewaySoftwareNow](#list_storagegateway-action-UpdateGatewaySoftwareNow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMaintenanceStartTime  **
  - **IAM action:**  [storagegateway:UpdateMaintenanceStartTime](#list_storagegateway-action-UpdateMaintenanceStartTime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNFSFileShare  **
  - **IAM action:**  [storagegateway:UpdateNFSFileShare](#list_storagegateway-action-UpdateNFSFileShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSMBFileShare  **
  - **IAM action:**  [storagegateway:UpdateSMBFileShare](#list_storagegateway-action-UpdateSMBFileShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSMBFileShareVisibility  **
  - **IAM action:**  [storagegateway:UpdateSMBFileShareVisibility](#list_storagegateway-action-UpdateSMBFileShareVisibility) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSMBLocalGroups  **
  - **IAM action:**  [storagegateway:UpdateSMBLocalGroups](#list_storagegateway-action-UpdateSMBLocalGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSMBSecurityStrategy  **
  - **IAM action:**  [storagegateway:UpdateSMBSecurityStrategy](#list_storagegateway-action-UpdateSMBSecurityStrategy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSnapshotSchedule  **
  - **IAM action:**  [storagegateway:UpdateSnapshotSchedule](#list_storagegateway-action-UpdateSnapshotSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVTLDeviceType  **
  - **IAM action:**  [storagegateway:UpdateVTLDeviceType](#list_storagegateway-action-UpdateVTLDeviceType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Storage Gateway
<a name="list_storagegateway-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateGateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ActivateGateway.html)  **
  - **Description:** Grants permission to activate the gateway you previously deployed on your host
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [AddCache](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AddCache.html)  **
  - **Description:** Grants permission to configure one or more gateway local disks as cache for a cached-volume gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddTagsToResource](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AddTagsToResource.html)  **
  - **Description:** Grants permission to add one or more tags to the specified resource
  - **Resource types (\*required):** [cache-report](#list_storagegateway-resource-cache-report) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [fs-association](#list_storagegateway-resource-fs-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [gateway](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [share](#list_storagegateway-resource-share) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [tape](#list_storagegateway-resource-tape) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [tapepool](#list_storagegateway-resource-tapepool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [volume](#list_storagegateway-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [AddUploadBuffer](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AddUploadBuffer.html)  **
  - **Description:** Grants permission to configure one or more gateway local disks as upload buffer for a specified gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddWorkingStorage](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AddWorkingStorage.html)  **
  - **Description:** Grants permission to configure one or more gateway local disks as working storage for a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssignTapePool](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AssignTapePool.html)  **
  - **Description:** Grants permission to move a tape to the target pool specified
  - **Resource types (\*required):** [tape\*](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tapepool\*](#list_storagegateway-resource-tapepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateFileSystem](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AssociateFileSystem.html)  **
  - **Description:** Grants permission to associate an Amazon FSx file system with the Amazon FSx file gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [AttachVolume](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_AttachVolume.html)  **
  - **Description:** Grants permission to connect a volume to an iSCSI connection and then attaches the volume to the specified gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BypassGovernanceRetention](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingCustomTapePool.html#TapeRetentionLock)  **
  - **Description:** Grants permission to allow the governance retention lock on a pool to be bypassed
  - **Resource types (\*required):** [tapepool\*](#list_storagegateway-resource-tapepool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelArchival](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CancelArchival.html)  **
  - **Description:** Grants permission to cancel archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tape\*](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelCacheReport](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CancelCacheReport.html)  **
  - **Description:** Grants permission to cancel a cache report
  - **Resource types (\*required):** [cache-report\*](#list_storagegateway-resource-cache-report)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelRetrieval](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CancelRetrieval.html)  **
  - **Description:** Grants permission to cancel retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tape\*](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCachediSCSIVolume](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateCachediSCSIVolume.html)  **
  - **Description:** Grants permission to create a cached volume on a specified cached gateway. This operation is supported only for the gateway-cached volume architecture
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNFSFileShare](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateNFSFileShare.html)  **
  - **Description:** Grants permission to create a NFS file share on an existing file gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSMBFileShare](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateSMBFileShare.html)  **
  - **Description:** Grants permission to create a SMB file share on an existing file gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to initiate a snapshot of a volume
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSnapshotFromVolumeRecoveryPoint](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateSnapshotFromVolumeRecoveryPoint.html)  **
  - **Description:** Grants permission to initiate a snapshot of a gateway from a volume recovery point
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStorediSCSIVolume](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateStorediSCSIVolume.html)  **
  - **Description:** Grants permission to create a volume on a specified gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTapePool](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateTapePool.html)  **
  - **Description:** Grants permission to create a tape pool
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTapeWithBarcode](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateTapeWithBarcode.html)  **
  - **Description:** Grants permission to create a virtual tape by using your own barcode
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [tapepool\*](#list_storagegateway-resource-tapepool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTapes](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateTapes.html)  **
  - **Description:** Grants permission to create one or more virtual tapes. You write data to the virtual tapes and then archive the tapes
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [tapepool\*](#list_storagegateway-resource-tapepool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAutomaticTapeCreationPolicy](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteAutomaticTapeCreationPolicy.html)  **
  - **Description:** Grants permission to delete the automatic tape creation policy configured on a gateway-VTL
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBandwidthRateLimit](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteBandwidthRateLimit.html)  **
  - **Description:** Grants permission to delete the bandwidth rate limits of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCacheReport](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteCacheReport.html)  **
  - **Description:** Grants permission to delete the metadata associated with a cache report
  - **Resource types (\*required):** [cache-report\*](#list_storagegateway-resource-cache-report)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChapCredentials](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteChapCredentials.html)  **
  - **Description:** Grants permission to delete Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair
  - **Resource types (\*required):** [target\*](#list_storagegateway-resource-target)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileShare](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteFileShare.html)  **
  - **Description:** Grants permission to delete a file share from a file gateway
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteGateway.html)  **
  - **Description:** Grants permission to delete a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshotSchedule](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteSnapshotSchedule.html)  **
  - **Description:** Grants permission to delete a snapshot of a volume
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTape](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteTape.html)  **
  - **Description:** Grants permission to delete the specified virtual tape
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tape\*](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTapeArchive](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteTapeArchive.html)  **
  - **Description:** Grants permission to delete the specified virtual tape from the virtual tape shelf (VTS)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTapePool](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteTapePool.html)  **
  - **Description:** Grants permission to delete the specified tape pool
  - **Resource types (\*required):** [tapepool\*](#list_storagegateway-resource-tapepool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVolume](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteVolume.html)  **
  - **Description:** Grants permission to delete the specified gateway volume that you previously created using the CreateCachediSCSIVolume or CreateStorediSCSIVolume API
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAvailabilityMonitorTest](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeAvailabilityMonitorTest.html)  **
  - **Description:** Grants permission to get the information about the most recent high availability monitoring test that was performed on the gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBandwidthRateLimit](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeBandwidthRateLimit.html)  **
  - **Description:** Grants permission to get the bandwidth rate limits of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBandwidthRateLimitSchedule](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeBandwidthRateLimitSchedule.html)  **
  - **Description:** Grants permission to get the bandwidth rate limit schedule of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCache](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeCache.html)  **
  - **Description:** Grants permission to get information about the cache of a gateway. This operation is supported only for the gateway-cached volume architecture
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCacheReport](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeCacheReport.html)  **
  - **Description:** Grants permission to get a description of a cache report
  - **Resource types (\*required):** [cache-report\*](#list_storagegateway-resource-cache-report)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCachediSCSIVolumes](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeCachediSCSIVolumes.html)  **
  - **Description:** Grants permission to get a description of the gateway volumes specified in the request. This operation is supported only for the gateway-cached volume architecture
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeChapCredentials](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeChapCredentials.html)  **
  - **Description:** Grants permission to get an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair
  - **Resource types (\*required):** [target\*](#list_storagegateway-resource-target)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFileSystemAssociations](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeFileSystemAssociations.html)  **
  - **Description:** Grants permission to get a description for one or more file system associations
  - **Resource types (\*required):** [fs-association\*](#list_storagegateway-resource-fs-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGatewayInformation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeGatewayInformation.html)  **
  - **Description:** Grants permission to get metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not)
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMaintenanceStartTime](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeMaintenanceStartTime.html)  **
  - **Description:** Grants permission to get your gateway's weekly maintenance start time including the day and time of the week
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNFSFileShares](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeNFSFileShares.html)  **
  - **Description:** Grants permission to get a description for one or more file shares from a file gateway
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSMBFileShares](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeSMBFileShares.html)  **
  - **Description:** Grants permission to get a description for one or more file shares from a file gateway
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSMBSettings](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeSMBSettings.html)  **
  - **Description:** Grants permission to get a description of a Server Message Block (SMB) file share settings from a file gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSnapshotSchedule](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeSnapshotSchedule.html)  **
  - **Description:** Grants permission to describe the snapshot schedule for the specified gateway volume
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStorediSCSIVolumes](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeStorediSCSIVolumes.html)  **
  - **Description:** Grants permission to get the description of the gateway volumes specified in the request
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTapeArchives](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeTapeArchives.html)  **
  - **Description:** Grants permission to get a description of specified virtual tapes in the virtual tape shelf (VTS)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTapeRecoveryPoints](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeTapeRecoveryPoints.html)  **
  - **Description:** Grants permission to get a list of virtual tape recovery points that are available for the specified gateway-VTL
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTapes](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeTapes.html)  **
  - **Description:** Grants permission to get a description of the specified Amazon Resource Name (ARN) of virtual tapes
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUploadBuffer](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeUploadBuffer.html)  **
  - **Description:** Grants permission to get information about the upload buffer of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVTLDevices](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeVTLDevices.html)  **
  - **Description:** Grants permission to get a description of virtual tape library (VTL) devices for the specified gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkingStorage](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeWorkingStorage.html)  **
  - **Description:** Grants permission to get information about the working storage of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetachVolume](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DetachVolume.html)  **
  - **Description:** Grants permission to disconnect a volume from an iSCSI connection and then detaches the volume from the specified gateway
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableGateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DisableGateway.html)  **
  - **Description:** Grants permission to disable a gateway when the gateway is no longer functioning
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateFileSystem](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DisassociateFileSystem.html)  **
  - **Description:** Grants permission to disassociate an Amazon FSx file system from an Amazon FSx file gateway
  - **Resource types (\*required):** [fs-association\*](#list_storagegateway-resource-fs-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EvictFilesFailingUpload](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_EvictFilesFailingUpload.html)  **
  - **Description:** Grants permission to clean a share's cache of file entries that are failing upload to Amazon S3
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [JoinDomain](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_JoinDomain.html)  **
  - **Description:** Grants permission to enable you to join an Active Directory Domain
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAutomaticTapeCreationPolicies](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListAutomaticTapeCreationPolicies.html)  **
  - **Description:** Grants permission to list the automatic tape creation policies configured on the specified gateway-VTL or all gateway-VTLs owned by your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCacheReports](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListCacheReports.html)  **
  - **Description:** Grants permission to get a list of the cache reports owned by your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFileShares](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListFileShares.html)  **
  - **Description:** Grants permission to get a list of the file shares for a specific file gateway, or the list of file shares owned by your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFileSystemAssociations](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListFileSystemAssociations.html)  **
  - **Description:** Grants permission to get a list of the file system associations for the specified gateway
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGateways](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListGateways.html)  **
  - **Description:** Grants permission to list gateways owned by an AWS account in a region specified in the request. The returned list is ordered by gateway Amazon Resource Name (ARN)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLocalDisks](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListLocalDisks.html)  **
  - **Description:** Grants permission to get a list of the gateway's local disks
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get the tags that have been added to the specified resource
  - **Resource types (\*required):** [gateway](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [share](#list_storagegateway-resource-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tape](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [volume](#list_storagegateway-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTapePools](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListTapePools.html)  **
  - **Description:** Grants permission to list tape pools owned by your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTapes](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListTapes.html)  **
  - **Description:** Grants permission to list virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVolumeInitiators](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListVolumeInitiators.html)  **
  - **Description:** Grants permission to list iSCSI initiators that are connected to a volume
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVolumeRecoveryPoints](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListVolumeRecoveryPoints.html)  **
  - **Description:** Grants permission to list the recovery points for a specified gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVolumes](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListVolumes.html)  **
  - **Description:** Grants permission to list the iSCSI stored volumes of a gateway
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [NotifyWhenUploaded](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_NotifyWhenUploaded.html)  **
  - **Description:** Grants permission to send you a notification through CloudWatch Events when all files written to your NFS file share have been uploaded to Amazon S3
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RefreshCache](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html)  **
  - **Description:** Grants permission to refresh the cache for the specified file share
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveTagsFromResource](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RemoveTagsFromResource.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified resource
  - **Resource types (\*required):** [cache-report](#list_storagegateway-resource-cache-report) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [fs-association](#list_storagegateway-resource-fs-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [gateway](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [share](#list_storagegateway-resource-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [tape](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [tapepool](#list_storagegateway-resource-tapepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Resource types (\*required):** [volume](#list_storagegateway-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ResetCache](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ResetCache.html)  **
  - **Description:** Grants permission to reset all cache disks that have encountered a error and makes the disks available for reconfiguration as cache storage
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetrieveTapeArchive](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RetrieveTapeArchive.html)  **
  - **Description:** Grants permission to retrieve an archived virtual tape from the virtual tape shelf (VTS) to a gateway-VTL
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tape\*](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetrieveTapeRecoveryPoint](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RetrieveTapeRecoveryPoint.html)  **
  - **Description:** Grants permission to retrieve the recovery point for the specified virtual tape
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tape\*](#list_storagegateway-resource-tape) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetLocalConsolePassword](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_SetLocalConsolePassword.html)  **
  - **Description:** Grants permission to set the password for your VM local console
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetSMBGuestPassword](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_SetSMBGuestPassword.html)  **
  - **Description:** Grants permission to set the password for SMB Guest user
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ShutdownGateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ShutdownGateway.html)  **
  - **Description:** Grants permission to shut down a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAvailabilityMonitorTest](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_StartAvailabilityMonitorTest.html)  **
  - **Description:** Grants permission to start a test that verifies that the specified gateway is configured for High Availability monitoring in your host environment
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCacheReport](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_StartCacheReport.html)  **
  - **Description:** Grants permission to start a cache report for an existing file share
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [StartGateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_StartGateway.html)  **
  - **Description:** Grants permission to start a gateway that you previously shut down
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutomaticTapeCreationPolicy](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateAutomaticTapeCreationPolicy.html)  **
  - **Description:** Grants permission to update the automatic tape creation policy configured on a gateway-VTL
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [tapepool\*](#list_storagegateway-resource-tapepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBandwidthRateLimit](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateBandwidthRateLimit.html)  **
  - **Description:** Grants permission to update the bandwidth rate limits of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBandwidthRateLimitSchedule](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateBandwidthRateLimitSchedule.html)  **
  - **Description:** Grants permission to update the bandwidth rate limit schedule of a gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChapCredentials](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateChapCredentials.html)  **
  - **Description:** Grants permission to update the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target
  - **Resource types (\*required):** [target\*](#list_storagegateway-resource-target)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFileSystemAssociation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateFileSystemAssociation.html)  **
  - **Description:** Grants permission to update a file system association
  - **Resource types (\*required):** [fs-association\*](#list_storagegateway-resource-fs-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewayInformation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateGatewayInformation.html)  **
  - **Description:** Grants permission to update a gateway's metadata, which includes the gateway's name and time zone
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewaySoftwareNow](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateGatewaySoftwareNow.html)  **
  - **Description:** Grants permission to update the gateway virtual machine (VM) software
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMaintenanceStartTime](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateMaintenanceStartTime.html)  **
  - **Description:** Grants permission to update a gateway's weekly maintenance start time information, including day and time of the week. The maintenance time is the time in your gateway's time zone
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNFSFileShare](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateNFSFileShare.html)  **
  - **Description:** Grants permission to update a NFS file share
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSMBFileShare](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateSMBFileShare.html)  **
  - **Description:** Grants permission to update a SMB file share
  - **Resource types (\*required):** [share\*](#list_storagegateway-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSMBFileShareVisibility](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateSMBFileShareVisibility.html)  **
  - **Description:** Grants permission to update whether the shares on a gateway are visible in a net view or browse list
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSMBLocalGroups](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateSMBLocalGroups.html)  **
  - **Description:** Grants permission to update the list of Active Directory users and groups that have special permissions for SMB file shares on the gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSMBSecurityStrategy](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateSMBSecurityStrategy.html)  **
  - **Description:** Grants permission to update the SMB security strategy on a file gateway
  - **Resource types (\*required):** [gateway\*](#list_storagegateway-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSnapshotSchedule](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateSnapshotSchedule.html)  **
  - **Description:** Grants permission to update a snapshot schedule configured for a gateway volume
  - **Resource types (\*required):** [volume\*](#list_storagegateway-resource-volume)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_storagegateway-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_storagegateway-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateVTLDeviceType](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_UpdateVTLDeviceType.html)  **
  - **Description:** Grants permission to update the type of medium changer in a gateway-VTL
  - **Resource types (\*required):** [device\*](#list_storagegateway-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Storage Gateway
<a name="list_storagegateway-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cache-report](https://docs.aws.amazon.com/filegateway/latest/files3/cache-report.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:share/${ShareId}/cache-report/${CacheReportId} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [device](https://docs.aws.amazon.com/storagegateway/latest/userguide/resource_vtl-devices.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:gateway/${GatewayId}/device/${Vtldevice} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [fs-association](https://docs.aws.amazon.com/filegateway/latest/filefsxw/attach-fsxw-filesystem.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:fs-association/${FsaId} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:gateway/${GatewayId} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [share](https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateFileShare.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:share/${ShareId} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [tape](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#storage-gateway-vtl-concepts)  | arn:${Partition}:storagegateway:${Region}:${Account}:tape/${TapeBarcode} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [tapepool](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingCustomTapePool.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:tapepool/${PoolId} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [target](https://docs.aws.amazon.com/storagegateway/latest/userguide/GettingStartedCreateVolumes.html)  | arn:${Partition}:storagegateway:${Region}:${Account}:gateway/${GatewayId}/target/${IscsiTarget} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 
|  [volume](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#volume-gateway-concepts)  | arn:${Partition}:storagegateway:${Region}:${Account}:gateway/${GatewayId}/volume/${VolumeId} | [aws:ResourceTag/${TagKey}](#list_storagegateway-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Storage Gateway
<a name="list_storagegateway-policy-keys"></a>

AWS Storage Gateway defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 