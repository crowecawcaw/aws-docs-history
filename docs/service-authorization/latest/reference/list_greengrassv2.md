

# Actions, resources, and condition keys for AWS IoT Greengrass V2
<a name="list_greengrassv2"></a>

AWS IoT Greengrass V2 (service prefix: `greengrass`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/greengrass/v2/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/greengrass/v2/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/greengrass/v2/developerguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/greengrass/greengrass.json) for this service.

**Topics**
+ [API operations defined by AWS IoT Greengrass V2](#list_greengrassv2-operations)
+ [Actions defined by AWS IoT Greengrass V2](#list_greengrassv2-actions-as-permissions)
+ [Resource types defined by AWS IoT Greengrass V2](#list_greengrassv2-resources-for-iam-policies)
+ [Condition keys for AWS IoT Greengrass V2](#list_greengrassv2-policy-keys)

## API operations defined by AWS IoT Greengrass V2
<a name="list_greengrassv2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_greengrassv2-actions-as-permissions).




- **   AssociateServiceRoleToAccount  **
  - **IAM action:**  [greengrass:AssociateServiceRoleToAccount](#list_greengrassv2-action-AssociateServiceRoleToAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** greengrass.amazonaws.com / **Access level:** Write

- **   BatchAssociateClientDeviceWithCoreDevice  **
  - **IAM action:**  [greengrass:BatchAssociateClientDeviceWithCoreDevice](#list_greengrassv2-action-BatchAssociateClientDeviceWithCoreDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateClientDeviceFromCoreDevice  **
  - **IAM action:**  [greengrass:BatchDisassociateClientDeviceFromCoreDevice](#list_greengrassv2-action-BatchDisassociateClientDeviceFromCoreDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDeployment  **
  - **IAM action:**  [greengrass:CancelDeployment](#list_greengrassv2-action-CancelDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateComponentVersion  **
  - **IAM action:**  [greengrass:CreateComponentVersion](#list_greengrassv2-action-CreateComponentVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrassv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDeployment  **
  - **IAM action:**  [greengrass:CreateDeployment](#list_greengrassv2-action-CreateDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [greengrass:TagResource](#list_greengrassv2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteComponent  **
  - **IAM action:**  [greengrass:DeleteComponent](#list_greengrassv2-action-DeleteComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCoreDevice  **
  - **IAM action:**  [greengrass:DeleteCoreDevice](#list_greengrassv2-action-DeleteCoreDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeployment  **
  - **IAM action:**  [greengrass:DeleteDeployment](#list_greengrassv2-action-DeleteDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeComponent  **
  - **IAM action:**  [greengrass:DescribeComponent](#list_greengrassv2-action-DescribeComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateServiceRoleFromAccount  **
  - **IAM action:**  [greengrass:DisassociateServiceRoleFromAccount](#list_greengrassv2-action-DisassociateServiceRoleFromAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetComponent  **
  - **IAM action:**  [greengrass:GetComponent](#list_greengrassv2-action-GetComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComponentVersionArtifact  **
  - **IAM action:**  [greengrass:GetComponentVersionArtifact](#list_greengrassv2-action-GetComponentVersionArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectivityInfo  **
  - **IAM action:**  [greengrass:GetConnectivityInfo](#list_greengrassv2-action-GetConnectivityInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoreDevice  **
  - **IAM action:**  [greengrass:GetCoreDevice](#list_greengrassv2-action-GetCoreDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployment  **
  - **IAM action:**  [greengrass:GetDeployment](#list_greengrassv2-action-GetDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceRoleForAccount  **
  - **IAM action:**  [greengrass:GetServiceRoleForAccount](#list_greengrassv2-action-GetServiceRoleForAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListClientDevicesAssociatedWithCoreDevice  **
  - **IAM action:**  [greengrass:ListClientDevicesAssociatedWithCoreDevice](#list_greengrassv2-action-ListClientDevicesAssociatedWithCoreDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponentVersions  **
  - **IAM action:**  [greengrass:ListComponentVersions](#list_greengrassv2-action-ListComponentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponents  **
  - **IAM action:**  [greengrass:ListComponents](#list_greengrassv2-action-ListComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoreDevices  **
  - **IAM action:**  [greengrass:ListCoreDevices](#list_greengrassv2-action-ListCoreDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeployments  **
  - **IAM action:**  [greengrass:ListDeployments](#list_greengrassv2-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEffectiveDeployments  **
  - **IAM action:**  [greengrass:ListEffectiveDeployments](#list_greengrassv2-action-ListEffectiveDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstalledComponents  **
  - **IAM action:**  [greengrass:ListInstalledComponents](#list_greengrassv2-action-ListInstalledComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [greengrass:ListTagsForResource](#list_greengrassv2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [greengrass:TagResource](#list_greengrassv2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [greengrass:UntagResource](#list_greengrassv2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnectivityInfo  **
  - **IAM action:**  [greengrass:UpdateConnectivityInfo](#list_greengrassv2-action-UpdateConnectivityInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT Greengrass V2
<a name="list_greengrassv2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateServiceRoleToAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_AssociateServiceRoleToAccount.html)  **
  - **Description:** Grants permission to associate a role with your account. AWS IoT Greengrass uses this role to access your Lambda functions and AWS IoT resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [BatchAssociateClientDeviceWithCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_BatchAssociateClientDeviceWithCoreDevice.html)  **
  - **Description:** Grants permission to associate a list of client devices with a core device
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateClientDeviceFromCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_BatchDisassociateClientDeviceFromCoreDevice.html)  **
  - **Description:** Grants permission to disassociate a list of client devices from a core device
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CancelDeployment.html)  **
  - **Description:** Grants permission to cancel a deployment
  - **Resource types (\*required):** [deployment\*](#list_greengrassv2-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateComponentVersion](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateComponentVersion.html)  **
  - **Description:** Grants permission to create a component
  - **Resource types (\*required):** [component\*](#list_greengrassv2-resource-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html)  **
  - **Description:** Grants permission to create a deployment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteComponent.html)  **
  - **Description:** Grants permission to delete a component
  - **Resource types (\*required):** [componentVersion\*](#list_greengrassv2-resource-componentVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteCoreDevice.html)  **
  - **Description:** Grants permission to delete a AWS IoT Greengrass core device, which is an AWS IoT thing. This operation removes the core device from the list of core devices. This operation doesn't delete the AWS IoT thing
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeleteDeployment.html)  **
  - **Description:** Grants permission to delete a deployment. To delete an active deployment, it needs to be cancelled first
  - **Resource types (\*required):** [deployment\*](#list_greengrassv2-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DescribeComponent.html)  **
  - **Description:** Grants permission to retrieve metadata for a version of a component
  - **Resource types (\*required):** [componentVersion\*](#list_greengrassv2-resource-componentVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateServiceRoleFromAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DisassociateServiceRoleFromAccount.html)  **
  - **Description:** Grants permission to disassociate the service role from an account. Without a service role, deployments will not work
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html)  **
  - **Description:** Grants permission to get the recipe for a version of a component
  - **Resource types (\*required):** [componentVersion\*](#list_greengrassv2-resource-componentVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComponentVersionArtifact](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponentVersionArtifact.html)  **
  - **Description:** Grants permission to get the pre-signed URL to download a public component artifact
  - **Resource types (\*required):** [componentVersion\*](#list_greengrassv2-resource-componentVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetConnectivityInfo.html)  **
  - **Description:** Grants permission to retrieve the connectivity information for a Greengrass core device
  - **Resource types (\*required):** [connectivityInfo\*](#list_greengrassv2-resource-connectivityInfo)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetCoreDevice.html)  **
  - **Description:** Grants permission to retrieves metadata for a AWS IoT Greengrass core device
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to get a deployment
  - **Resource types (\*required):** [deployment\*](#list_greengrassv2-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceRoleForAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetServiceRoleForAccount.html)  **
  - **Description:** Grants permission to retrieve the service role that is attached to an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListClientDevicesAssociatedWithCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListClientDevicesAssociatedWithCoreDevice.html)  **
  - **Description:** Grants permission to retrieve a paginated list of client devices associated to a AWS IoT Greengrass core device
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComponentVersions](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListComponentVersions.html)  **
  - **Description:** Grants permission to retrieve a paginated list of all versions for a component
  - **Resource types (\*required):** [component\*](#list_greengrassv2-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComponents](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListComponents.html)  **
  - **Description:** Grants permission to retrieve a paginated list of component summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCoreDevices](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListCoreDevices.html)  **
  - **Description:** Grants permission to retrieve a paginated list of AWS IoT Greengrass core devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListDeployments.html)  **
  - **Description:** Grants permission to retrieves a paginated list of deployments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEffectiveDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListEffectiveDeployments.html)  **
  - **Description:** Grants permission to retrieves a paginated list of deployment jobs that AWS IoT Greengrass sends to AWS IoT Greengrass core devices
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInstalledComponents](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListInstalledComponents.html)  **
  - **Description:** Grants permission to retrieve a paginated list of the components that a AWS IoT Greengrass core device runs
  - **Resource types (\*required):** [coreDevice\*](#list_greengrassv2-resource-coreDevice)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [component](#list_greengrassv2-resource-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [componentVersion](#list_greengrassv2-resource-componentVersion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [coreDevice](#list_greengrassv2-resource-coreDevice) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_greengrassv2-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Access level:** Read

- **   [ResolveComponentCandidates](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolveComponentCandidates.html)  **
  - **Description:** Grants permission to list components that meet the component, version, and platform requirements of a deployment
  - **Resource types (\*required):** [componentVersion\*](#list_greengrassv2-resource-componentVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [component](#list_greengrassv2-resource-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [componentVersion](#list_greengrassv2-resource-componentVersion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [coreDevice](#list_greengrassv2-resource-coreDevice) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_greengrassv2-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_greengrassv2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [component](#list_greengrassv2-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [componentVersion](#list_greengrassv2-resource-componentVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [coreDevice](#list_greengrassv2-resource-coreDevice) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_greengrassv2-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_greengrassv2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_UpdateConnectivityInfo.html)  **
  - **Description:** Grants permission to update the connectivity information for a Greengrass core. Any devices that belong to the group that has this core will receive this information in order to find the location of the core and connect to it
  - **Resource types (\*required):** [connectivityInfo\*](#list_greengrassv2-resource-connectivityInfo)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS IoT Greengrass V2
<a name="list_greengrassv2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [component](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html)  | arn:${Partition}:greengrass:${Region}:${Account}:components:${ComponentName} | [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_) | 
|  [componentVersion](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html)  | arn:${Partition}:greengrass:${Region}:${Account}:components:${ComponentName}:versions:${ComponentVersion} | [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_) | 
|  [connectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ConnectivityInfo.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/things/${ThingName}/connectivityInfo |   | 
|  [coreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CoreDevice.html)  | arn:${Partition}:greengrass:${Region}:${Account}:coreDevices:${CoreDeviceThingName} | [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_) | 
|  [deployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Deployment.html)  | arn:${Partition}:greengrass:${Region}:${Account}:/greengrass/groups/${GroupId}/deployments/${DeploymentId}, arn:${Partition}:greengrass:${Region}:${Account}:deployments:${DeploymentId} | [aws:ResourceTag/${TagKey}](#list_greengrassv2-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT Greengrass V2
<a name="list_greengrassv2-policy-keys"></a>

AWS IoT Greengrass V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by checking tag key/value pairs included in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by checking tag key/value pairs associated with a specific resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by checking tag keys passed in the request | ArrayOfString | 