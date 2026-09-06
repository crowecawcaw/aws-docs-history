

# Actions, resources, and condition keys for AWS Device Farm
<a name="list_devicefarm"></a>

AWS Device Farm (service prefix: `devicefarm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/devicefarm/latest/developerguide/permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/devicefarm/devicefarm.json) for this service.

**Topics**
+ [API operations defined by AWS Device Farm](#list_devicefarm-operations)
+ [Actions defined by AWS Device Farm](#list_devicefarm-actions-as-permissions)
+ [Resource types defined by AWS Device Farm](#list_devicefarm-resources-for-iam-policies)
+ [Condition keys for AWS Device Farm](#list_devicefarm-policy-keys)

## API operations defined by AWS Device Farm
<a name="list_devicefarm-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_devicefarm-actions-as-permissions).




- **   CreateDevicePool  **
  - **IAM action:**  [devicefarm:CreateDevicePool](#list_devicefarm-action-CreateDevicePool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInstanceProfile  **
  - **IAM action:**  [devicefarm:CreateInstanceProfile](#list_devicefarm-action-CreateInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNetworkProfile  **
  - **IAM action:**  [devicefarm:CreateNetworkProfile](#list_devicefarm-action-CreateNetworkProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProject  **
  - **IAM action:**  [devicefarm:CreateProject](#list_devicefarm-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** devicefarm.amazonaws.com / **Access level:** Write

- **   CreateRemoteAccessSession  **
  - **IAM action:**  [devicefarm:CreateRemoteAccessSession](#list_devicefarm-action-CreateRemoteAccessSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTestGridProject  **
  - **IAM action:**  [devicefarm:CreateTestGridProject](#list_devicefarm-action-CreateTestGridProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTestGridUrl  **
  - **IAM action:**  [devicefarm:CreateTestGridUrl](#list_devicefarm-action-CreateTestGridUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUpload  **
  - **IAM action:**  [devicefarm:CreateUpload](#list_devicefarm-action-CreateUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVPCEConfiguration  **
  - **IAM action:**  [devicefarm:CreateVPCEConfiguration](#list_devicefarm-action-CreateVPCEConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDevicePool  **
  - **IAM action:**  [devicefarm:DeleteDevicePool](#list_devicefarm-action-DeleteDevicePool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstanceProfile  **
  - **IAM action:**  [devicefarm:DeleteInstanceProfile](#list_devicefarm-action-DeleteInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNetworkProfile  **
  - **IAM action:**  [devicefarm:DeleteNetworkProfile](#list_devicefarm-action-DeleteNetworkProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **IAM action:**  [devicefarm:DeleteProject](#list_devicefarm-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRemoteAccessSession  **
  - **IAM action:**  [devicefarm:DeleteRemoteAccessSession](#list_devicefarm-action-DeleteRemoteAccessSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRun  **
  - **IAM action:**  [devicefarm:DeleteRun](#list_devicefarm-action-DeleteRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTestGridProject  **
  - **IAM action:**  [devicefarm:DeleteTestGridProject](#list_devicefarm-action-DeleteTestGridProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUpload  **
  - **IAM action:**  [devicefarm:DeleteUpload](#list_devicefarm-action-DeleteUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVPCEConfiguration  **
  - **IAM action:**  [devicefarm:DeleteVPCEConfiguration](#list_devicefarm-action-DeleteVPCEConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountSettings  **
  - **IAM action:**  [devicefarm:GetAccountSettings](#list_devicefarm-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevice  **
  - **IAM action:**  [devicefarm:GetDevice](#list_devicefarm-action-GetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeviceInstance  **
  - **IAM action:**  [devicefarm:GetDeviceInstance](#list_devicefarm-action-GetDeviceInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevicePool  **
  - **IAM action:**  [devicefarm:GetDevicePool](#list_devicefarm-action-GetDevicePool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevicePoolCompatibility  **
  - **IAM action:**  [devicefarm:GetDevicePoolCompatibility](#list_devicefarm-action-GetDevicePoolCompatibility) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstanceProfile  **
  - **IAM action:**  [devicefarm:GetInstanceProfile](#list_devicefarm-action-GetInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [devicefarm:GetJob](#list_devicefarm-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkProfile  **
  - **IAM action:**  [devicefarm:GetNetworkProfile](#list_devicefarm-action-GetNetworkProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOfferingStatus  **
  - **IAM action:**  [devicefarm:GetOfferingStatus](#list_devicefarm-action-GetOfferingStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProject  **
  - **IAM action:**  [devicefarm:GetProject](#list_devicefarm-action-GetProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRemoteAccessSession  **
  - **IAM action:**  [devicefarm:GetRemoteAccessSession](#list_devicefarm-action-GetRemoteAccessSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRun  **
  - **IAM action:**  [devicefarm:GetRun](#list_devicefarm-action-GetRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSuite  **
  - **IAM action:**  [devicefarm:GetSuite](#list_devicefarm-action-GetSuite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTest  **
  - **IAM action:**  [devicefarm:GetTest](#list_devicefarm-action-GetTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTestGridProject  **
  - **IAM action:**  [devicefarm:GetTestGridProject](#list_devicefarm-action-GetTestGridProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTestGridSession  **
  - **IAM action:**  [devicefarm:GetTestGridSession](#list_devicefarm-action-GetTestGridSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUpload  **
  - **IAM action:**  [devicefarm:GetUpload](#list_devicefarm-action-GetUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVPCEConfiguration  **
  - **IAM action:**  [devicefarm:GetVPCEConfiguration](#list_devicefarm-action-GetVPCEConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InstallToRemoteAccessSession  **
  - **IAM action:**  [devicefarm:InstallToRemoteAccessSession](#list_devicefarm-action-InstallToRemoteAccessSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListArtifacts  **
  - **IAM action:**  [devicefarm:ListArtifacts](#list_devicefarm-action-ListArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeviceInstances  **
  - **IAM action:**  [devicefarm:ListDeviceInstances](#list_devicefarm-action-ListDeviceInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDevicePools  **
  - **IAM action:**  [devicefarm:ListDevicePools](#list_devicefarm-action-ListDevicePools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDevices  **
  - **IAM action:**  [devicefarm:ListDevices](#list_devicefarm-action-ListDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstanceProfiles  **
  - **IAM action:**  [devicefarm:ListInstanceProfiles](#list_devicefarm-action-ListInstanceProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [devicefarm:ListJobs](#list_devicefarm-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkProfiles  **
  - **IAM action:**  [devicefarm:ListNetworkProfiles](#list_devicefarm-action-ListNetworkProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOfferingPromotions  **
  - **IAM action:**  [devicefarm:ListOfferingPromotions](#list_devicefarm-action-ListOfferingPromotions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOfferingTransactions  **
  - **IAM action:**  [devicefarm:ListOfferingTransactions](#list_devicefarm-action-ListOfferingTransactions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOfferings  **
  - **IAM action:**  [devicefarm:ListOfferings](#list_devicefarm-action-ListOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjects  **
  - **IAM action:**  [devicefarm:ListProjects](#list_devicefarm-action-ListProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRemoteAccessSessions  **
  - **IAM action:**  [devicefarm:ListRemoteAccessSessions](#list_devicefarm-action-ListRemoteAccessSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuns  **
  - **IAM action:**  [devicefarm:ListRuns](#list_devicefarm-action-ListRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSamples  **
  - **IAM action:**  [devicefarm:ListSamples](#list_devicefarm-action-ListSamples) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSuites  **
  - **IAM action:**  [devicefarm:ListSuites](#list_devicefarm-action-ListSuites) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [devicefarm:ListTagsForResource](#list_devicefarm-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTestGridProjects  **
  - **IAM action:**  [devicefarm:ListTestGridProjects](#list_devicefarm-action-ListTestGridProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTestGridSessionActions  **
  - **IAM action:**  [devicefarm:ListTestGridSessionActions](#list_devicefarm-action-ListTestGridSessionActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTestGridSessionArtifacts  **
  - **IAM action:**  [devicefarm:ListTestGridSessionArtifacts](#list_devicefarm-action-ListTestGridSessionArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTestGridSessions  **
  - **IAM action:**  [devicefarm:ListTestGridSessions](#list_devicefarm-action-ListTestGridSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTests  **
  - **IAM action:**  [devicefarm:ListTests](#list_devicefarm-action-ListTests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUniqueProblems  **
  - **IAM action:**  [devicefarm:ListUniqueProblems](#list_devicefarm-action-ListUniqueProblems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUploads  **
  - **IAM action:**  [devicefarm:ListUploads](#list_devicefarm-action-ListUploads) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVPCEConfigurations  **
  - **IAM action:**  [devicefarm:ListVPCEConfigurations](#list_devicefarm-action-ListVPCEConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PurchaseOffering  **
  - **IAM action:**  [devicefarm:PurchaseOffering](#list_devicefarm-action-PurchaseOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RenewOffering  **
  - **IAM action:**  [devicefarm:RenewOffering](#list_devicefarm-action-RenewOffering) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ScheduleRun  **
  - **IAM action:**  [devicefarm:ScheduleRun](#list_devicefarm-action-ScheduleRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** devicefarm.amazonaws.com / **Access level:** Write

- **   StopJob  **
  - **IAM action:**  [devicefarm:StopJob](#list_devicefarm-action-StopJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRemoteAccessSession  **
  - **IAM action:**  [devicefarm:StopRemoteAccessSession](#list_devicefarm-action-StopRemoteAccessSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRun  **
  - **IAM action:**  [devicefarm:StopRun](#list_devicefarm-action-StopRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [devicefarm:TagResource](#list_devicefarm-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [devicefarm:UntagResource](#list_devicefarm-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDeviceInstance  **
  - **IAM action:**  [devicefarm:UpdateDeviceInstance](#list_devicefarm-action-UpdateDeviceInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDevicePool  **
  - **IAM action:**  [devicefarm:UpdateDevicePool](#list_devicefarm-action-UpdateDevicePool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInstanceProfile  **
  - **IAM action:**  [devicefarm:UpdateInstanceProfile](#list_devicefarm-action-UpdateInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetworkProfile  **
  - **IAM action:**  [devicefarm:UpdateNetworkProfile](#list_devicefarm-action-UpdateNetworkProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProject  **
  - **IAM action:**  [devicefarm:UpdateProject](#list_devicefarm-action-UpdateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** devicefarm.amazonaws.com / **Access level:** Write

- **   UpdateTestGridProject  **
  - **IAM action:**  [devicefarm:UpdateTestGridProject](#list_devicefarm-action-UpdateTestGridProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUpload  **
  - **IAM action:**  [devicefarm:UpdateUpload](#list_devicefarm-action-UpdateUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVPCEConfiguration  **
  - **IAM action:**  [devicefarm:UpdateVPCEConfiguration](#list_devicefarm-action-UpdateVPCEConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Device Farm
<a name="list_devicefarm-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDevicePool](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateDevicePool.html)  **
  - **Description:** Grants permission to create a device pool within a project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInstanceProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateInstanceProfile.html)  **
  - **Description:** Grants permission to create a device instance profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNetworkProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateNetworkProfile.html)  **
  - **Description:** Grants permission to create a network profile within a project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a project for mobile testing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRemoteAccessSession](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateRemoteAccessSession.html)  **
  - **Description:** Grants permission to start a remote access session to a device instance
  - **Resource types (\*required):** [device\*](#list_devicefarm-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deviceinstance](#list_devicefarm-resource-deviceinstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [upload](#list_devicefarm-resource-upload) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateTestGridProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateTestGridProject.html)  **
  - **Description:** Grants permission to create a project for desktop testing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTestGridUrl](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateTestGridUrl.html)  **
  - **Description:** Grants permission to generate a new pre-signed url used to access our test grid service
  - **Resource types (\*required):** [testgrid-project\*](#list_devicefarm-resource-testgrid-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUpload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateUpload.html)  **
  - **Description:** Grants permission to upload a new file or app within a project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVPCEConfiguration](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateVPCEConfiguration.html)  **
  - **Description:** Grants permission to create an Amazon Virtual Private Cloud (VPC) endpoint configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDevicePool](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteDevicePool.html)  **
  - **Description:** Grants permission to delete a user-generated device pool
  - **Resource types (\*required):** [devicepool\*](#list_devicefarm-resource-devicepool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInstanceProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteInstanceProfile.html)  **
  - **Description:** Grants permission to delete a user-generated instance profile
  - **Resource types (\*required):** [instanceprofile\*](#list_devicefarm-resource-instanceprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetworkProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/DeleteNetworkProfile.html)  **
  - **Description:** Grants permission to delete a user-generated network profile
  - **Resource types (\*required):** [networkprofile\*](#list_devicefarm-resource-networkprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a mobile testing project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRemoteAccessSession](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteRemoteAccessSession.html)  **
  - **Description:** Grants permission to delete a completed remote access session and its results
  - **Resource types (\*required):** [session\*](#list_devicefarm-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteRun.html)  **
  - **Description:** Grants permission to delete a run
  - **Resource types (\*required):** [run\*](#list_devicefarm-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTestGridProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteTestGridProject.html)  **
  - **Description:** Grants permission to delete a desktop testing project
  - **Resource types (\*required):** [testgrid-project\*](#list_devicefarm-resource-testgrid-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUpload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteUpload.html)  **
  - **Description:** Grants permission to delete a user-uploaded file
  - **Resource types (\*required):** [upload\*](#list_devicefarm-resource-upload)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVPCEConfiguration](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeleteVPCEConfiguration.html)  **
  - **Description:** Grants permission to delete an Amazon Virtual Private Cloud (VPC) endpoint configuration
  - **Resource types (\*required):** [vpceconfiguration\*](#list_devicefarm-resource-vpceconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to retrieve the number of unmetered iOS and/or unmetered Android devices purchased by the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDevice](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetDevice.html)  **
  - **Description:** Grants permission to retrieve the information of a unique device type
  - **Resource types (\*required):** [device\*](#list_devicefarm-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceInstance](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetDeviceInstance.html)  **
  - **Description:** Grants permission to retireve the information of a device instance
  - **Resource types (\*required):** [deviceinstance\*](#list_devicefarm-resource-deviceinstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDevicePool](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetDevicePool.html)  **
  - **Description:** Grants permission to retireve the information of a device pool
  - **Resource types (\*required):** [devicepool\*](#list_devicefarm-resource-devicepool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDevicePoolCompatibility](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetDevicePoolCompatibility.html)  **
  - **Description:** Grants permission to retrieve information about the compatibility of a test and/or app with a device pool
  - **Resource types (\*required):** [devicepool\*](#list_devicefarm-resource-devicepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [upload](#list_devicefarm-resource-upload) / **Condition keys:**  
  - **Access level:** Read

- **   [GetInstanceProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetInstanceProfile.html)  **
  - **Description:** Grants permission to retireve the information of an instance profile
  - **Resource types (\*required):** [instanceprofile\*](#list_devicefarm-resource-instanceprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetJob.html)  **
  - **Description:** Grants permission to retireve the information of a job
  - **Resource types (\*required):** [job\*](#list_devicefarm-resource-job)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNetworkProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetNetworkProfile.html)  **
  - **Description:** Grants permission to retireve the information of a network profile
  - **Resource types (\*required):** [networkprofile\*](#list_devicefarm-resource-networkprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOfferingStatus](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetOfferingStatus.html)  **
  - **Description:** Grants permission to retrieve the current status and future status of all offerings purchased by an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetProject.html)  **
  - **Description:** Grants permission to retrieve information about a mobile testing project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRemoteAccessSession](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRemoteAccessSession.html)  **
  - **Description:** Grants permission to retireve the link to a currently running remote access session
  - **Resource types (\*required):** [session\*](#list_devicefarm-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetRun.html)  **
  - **Description:** Grants permission to retireve the information of a run
  - **Resource types (\*required):** [run\*](#list_devicefarm-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSuite](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetSuite.html)  **
  - **Description:** Grants permission to retireve the information of a testing suite
  - **Resource types (\*required):** [suite\*](#list_devicefarm-resource-suite)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTest](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetTest.html)  **
  - **Description:** Grants permission to retireve the information of a test case
  - **Resource types (\*required):** [test\*](#list_devicefarm-resource-test)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTestGridProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetTestGridProject.html)  **
  - **Description:** Grants permission to retrieve information about a desktop testing project
  - **Resource types (\*required):** [testgrid-project\*](#list_devicefarm-resource-testgrid-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestGridSession](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetTestGridSession.html)  **
  - **Description:** Grants permission to retireve the information of a test grid session
  - **Resource types (\*required):** [testgrid-project](#list_devicefarm-resource-testgrid-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [testgrid-session](#list_devicefarm-resource-testgrid-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUpload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetUpload.html)  **
  - **Description:** Grants permission to retireve the information of an uploaded file
  - **Resource types (\*required):** [upload\*](#list_devicefarm-resource-upload)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVPCEConfiguration](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetVPCEConfiguration.html)  **
  - **Description:** Grants permission to retireve the information of an Amazon Virtual Private Cloud (VPC) endpoint configuration
  - **Resource types (\*required):** [vpceconfiguration\*](#list_devicefarm-resource-vpceconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InstallToRemoteAccessSession](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstallToRemoteAccessSession.html)  **
  - **Description:** Grants permission to install an application to a device in a remote access session
  - **Resource types (\*required):** [session\*](#list_devicefarm-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [upload\*](#list_devicefarm-resource-upload) / **Condition keys:**  
  - **Access level:** Write

- **   [ListArtifacts](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html)  **
  - **Description:** Grants permission to list the artifacts in a project
  - **Resource types (\*required):** [job](#list_devicefarm-resource-job) / **Condition keys:**  
  - **Resource types (\*required):** [run](#list_devicefarm-resource-run) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [suite](#list_devicefarm-resource-suite) / **Condition keys:**  
  - **Resource types (\*required):** [test](#list_devicefarm-resource-test) / **Condition keys:**  
  - **Access level:** List

- **   [ListDeviceInstances](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDeviceInstances.html)  **
  - **Description:** Grants permission to list the information of device instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDevicePools](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDevicePools.html)  **
  - **Description:** Grants permission to list the information of device pools
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDevices](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDevices.html)  **
  - **Description:** Grants permission to list the information of unique device types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInstanceProfiles](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListInstanceProfiles.html)  **
  - **Description:** Grants permission to list the information of device instance profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListJobs.html)  **
  - **Description:** Grants permission to list the information of jobs within a run
  - **Resource types (\*required):** [run\*](#list_devicefarm-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkProfiles](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListNetworkProfiles.html)  **
  - **Description:** Grants permission to list the information of network profiles within a project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOfferingPromotions](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListOfferingPromotions.html)  **
  - **Description:** Grants permission to list the offering promotions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOfferingTransactions](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListOfferingTransactions.html)  **
  - **Description:** Grants permission to list all of the historical purchases, renewals, and system renewal transactions for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOfferings](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListOfferings.html)  **
  - **Description:** Grants permission to list the products or offerings that the user can manage through the API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list the information of mobile testing projects for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRemoteAccessSessions](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListRemoteAccessSessions.html)  **
  - **Description:** Grants permission to list the information of currently running remote access sessions
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRuns](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListRuns.html)  **
  - **Description:** Grants permission to list the information of runs within a project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSamples](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListSamples.html)  **
  - **Description:** Grants permission to list the information of samples within a project
  - **Resource types (\*required):** [job\*](#list_devicefarm-resource-job)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSuites](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListSuites.html)  **
  - **Description:** Grants permission to list the information of testing suites within a job
  - **Resource types (\*required):** [job\*](#list_devicefarm-resource-job)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags of a resource
  - **Resource types (\*required):** [device](#list_devicefarm-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deviceinstance](#list_devicefarm-resource-deviceinstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [devicepool](#list_devicefarm-resource-devicepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [instanceprofile](#list_devicefarm-resource-instanceprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [networkprofile](#list_devicefarm-resource-networkprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_devicefarm-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [run](#list_devicefarm-resource-run) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [session](#list_devicefarm-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [testgrid-project](#list_devicefarm-resource-testgrid-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [testgrid-session](#list_devicefarm-resource-testgrid-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vpceconfiguration](#list_devicefarm-resource-vpceconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTestGridProjects](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridProjects.html)  **
  - **Description:** Grants permission to list the information of desktop testing projects for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTestGridSessionActions](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionActions.html)  **
  - **Description:** Grants permission to list the session actions performed during a test grid session
  - **Resource types (\*required):** [testgrid-session\*](#list_devicefarm-resource-testgrid-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTestGridSessionArtifacts](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionArtifacts.html)  **
  - **Description:** Grants permission to list the artifacts generated by a test grid session
  - **Resource types (\*required):** [testgrid-session\*](#list_devicefarm-resource-testgrid-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTestGridSessions](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessions.html)  **
  - **Description:** Grants permission to list the sessions within a test grid project
  - **Resource types (\*required):** [testgrid-project\*](#list_devicefarm-resource-testgrid-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTests](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTests.html)  **
  - **Description:** Grants permission to list the information of tests within a testing suite
  - **Resource types (\*required):** [suite\*](#list_devicefarm-resource-suite)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUniqueProblems](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListUniqueProblems.html)  **
  - **Description:** Grants permission to list the information of unique problems within a run
  - **Resource types (\*required):** [run\*](#list_devicefarm-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUploads](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListUploads.html)  **
  - **Description:** Grants permission to list the information of uploads within a project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVPCEConfigurations](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListVPCEConfigurations.html)  **
  - **Description:** Grants permission to list the information of Amazon Virtual Private Cloud (VPC) endpoint configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PurchaseOffering](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_PurchaseOffering.html)  **
  - **Description:** Grants permission to purchase offerings for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RenewOffering](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RenewOffering.html)  **
  - **Description:** Grants permission to set the quantity of devices to renew for an offering
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ScheduleRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRun.html)  **
  - **Description:** Grants permission to schedule a run / **Resource types (\*required):** [devicepool](#list_devicefarm-resource-devicepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) / **Access level:** Write
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [upload](#list_devicefarm-resource-upload) / **Condition keys:**  
  - **Description:** **SCENARIO: **Device Pool as filter / **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)<br />[devicepool\*](#list_devicefarm-resource-devicepool)<br />[upload](#list_devicefarm-resource-upload) / **Condition keys:**  / **Access level:** 
  - **Description:** **SCENARIO: **Device Selection Configuration as filter / **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)<br />[upload](#list_devicefarm-resource-upload) / **Condition keys:**  / **Access level:** 

- **   [StopJob](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_StopJob.html)  **
  - **Description:** Grants permission to terminate a running job
  - **Resource types (\*required):** [job\*](#list_devicefarm-resource-job)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopRemoteAccessSession](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_StopRemoteAccessSession.html)  **
  - **Description:** Grants permission to terminate a running remote access session
  - **Resource types (\*required):** [session\*](#list_devicefarm-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_StopRun.html)  **
  - **Description:** Grants permission to terminate a running test run
  - **Resource types (\*required):** [run\*](#list_devicefarm-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [device](#list_devicefarm-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [deviceinstance](#list_devicefarm-resource-deviceinstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [devicepool](#list_devicefarm-resource-devicepool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [instanceprofile](#list_devicefarm-resource-instanceprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [networkprofile](#list_devicefarm-resource-networkprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_devicefarm-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [run](#list_devicefarm-resource-run) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [session](#list_devicefarm-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [testgrid-project](#list_devicefarm-resource-testgrid-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [testgrid-session](#list_devicefarm-resource-testgrid-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [vpceconfiguration](#list_devicefarm-resource-vpceconfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devicefarm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [device](#list_devicefarm-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [deviceinstance](#list_devicefarm-resource-deviceinstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [devicepool](#list_devicefarm-resource-devicepool) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [instanceprofile](#list_devicefarm-resource-instanceprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [networkprofile](#list_devicefarm-resource-networkprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_devicefarm-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [run](#list_devicefarm-resource-run) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [session](#list_devicefarm-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [testgrid-project](#list_devicefarm-resource-testgrid-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [testgrid-session](#list_devicefarm-resource-testgrid-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Resource types (\*required):** [vpceconfiguration](#list_devicefarm-resource-vpceconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devicefarm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDeviceInstance](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateDeviceInstance.html)  **
  - **Description:** Grants permission to modify an existing device instance
  - **Resource types (\*required):** [deviceinstance\*](#list_devicefarm-resource-deviceinstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [instanceprofile](#list_devicefarm-resource-instanceprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDevicePool](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateDevicePool.html)  **
  - **Description:** Grants permission to modify an existing device pool
  - **Resource types (\*required):** [devicepool\*](#list_devicefarm-resource-devicepool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInstanceProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateInstanceProfile.html)  **
  - **Description:** Grants permission to modify an existing instance profile
  - **Resource types (\*required):** [instanceprofile\*](#list_devicefarm-resource-instanceprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkProfile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateNetworkProfile.html)  **
  - **Description:** Grants permission to modify an existing network profile
  - **Resource types (\*required):** [networkprofile\*](#list_devicefarm-resource-networkprofile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to modify an existing mobile testing project
  - **Resource types (\*required):** [project\*](#list_devicefarm-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTestGridProject](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateTestGridProject.html)  **
  - **Description:** Grants permission to modify an existing desktop testing project
  - **Resource types (\*required):** [testgrid-project\*](#list_devicefarm-resource-testgrid-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUpload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateUpload.html)  **
  - **Description:** Grants permission to modify an existing upload
  - **Resource types (\*required):** [upload\*](#list_devicefarm-resource-upload)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateVPCEConfiguration](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateVPCEConfiguration.html)  **
  - **Description:** Grants permission to modify an existing Amazon Virtual Private Cloud (VPC) endpoint configuration
  - **Resource types (\*required):** [vpceconfiguration\*](#list_devicefarm-resource-vpceconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Device Farm
<a name="list_devicefarm-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [artifact](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Artifact.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:artifact:${ResourceId} |   | 
|  [device](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Device.html)  | arn:${Partition}:devicefarm:${Region}::device:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [deviceinstance](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceInstance.html)  | arn:${Partition}:devicefarm:${Region}::deviceinstance:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [devicepool](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DevicePool.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:devicepool:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [instanceprofile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstanceProfile.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:instanceprofile:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [job](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Job.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:job:${ResourceId} |   | 
|  [networkprofile](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_NetworkProfile.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:networkprofile:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Project.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:project:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [run](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Run.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:run:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [sample](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Sample.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:sample:${ResourceId} |   | 
|  [session](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RemoteAccessSession.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:session:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [suite](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Suite.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:suite:${ResourceId} |   | 
|  [test](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Test.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:test:${ResourceId} |   | 
|  [testgrid-project](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridProject.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:testgrid-project:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [testgrid-session](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridSession.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:testgrid-session:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 
|  [upload](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Upload.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:upload:${ResourceId} |   | 
|  [vpceconfiguration](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_VPCEConfiguration.html)  | arn:${Partition}:devicefarm:${Region}:${Account}:vpceconfiguration:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_devicefarm-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Device Farm
<a name="list_devicefarm-policy-keys"></a>

AWS Device Farm defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag-value assoicated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of mandatory tags in the request | ArrayOfString | 