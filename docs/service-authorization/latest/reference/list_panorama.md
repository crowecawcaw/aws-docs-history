

# Actions, resources, and condition keys for AWS Panorama
<a name="list_panorama"></a>

AWS Panorama (service prefix: `panorama`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/panorama/latest/dev/panorama-welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/panorama/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/panorama/latest/dev/panorama-permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/panorama/panorama.json) for this service.

**Topics**
+ [Actions defined by AWS Panorama](#list_panorama-actions-as-permissions)
+ [Permission-only actions for AWS Panorama](#list_panorama-permission-only-actions)
+ [Resource types defined by AWS Panorama](#list_panorama-resources-for-iam-policies)
+ [Condition keys for AWS Panorama](#list_panorama-policy-keys)

## Actions defined by AWS Panorama
<a name="list_panorama-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_CreateApplicationInstance.html)  **
  - **Description:** Grants permission to create an AWS Panorama Application Instance
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_panorama-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Access level:** Write

- **   [CreateJobForDevices](https://docs.aws.amazon.com/panorama/latest/api/API_CreateJobForDevices.html)  **
  - **Description:** Grants permission to create a job for an AWS Panorama Appliance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNodeFromTemplateJob](https://docs.aws.amazon.com/panorama/latest/api/API_CreateNodeFromTemplateJob.html)  **
  - **Description:** Grants permission to create an AWS Panorama Node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePackage](https://docs.aws.amazon.com/panorama/latest/api/API_CreatePackage.html)  **
  - **Description:** Grants permission to create an AWS Panorama Package
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_panorama-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePackageImportJob](https://docs.aws.amazon.com/panorama/latest/api/API_CreatePackageImportJob.html)  **
  - **Description:** Grants permission to create an AWS Panorama Package
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDevice](https://docs.aws.amazon.com/panorama/latest/api/API_DeleteDevice.html)  **
  - **Description:** Grants permission to deregister an AWS Panorama Appliance
  - **Resource types (\*required):** [device\*](#list_panorama-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePackage](https://docs.aws.amazon.com/panorama/latest/api/API_DeletePackage.html)  **
  - **Description:** Grants permission to delete an AWS Panorama Package
  - **Resource types (\*required):** [package\*](#list_panorama-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterPackageVersion](https://docs.aws.amazon.com/panorama/latest/api/API_DeregisterPackageVersion.html)  **
  - **Description:** Grants permission to deregister an AWS Panorama package version
  - **Resource types (\*required):** [package\*](#list_panorama-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeApplicationInstance.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama application instance
  - **Resource types (\*required):** [applicationInstance\*](#list_panorama-resource-applicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApplicationInstanceDetails](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeApplicationInstanceDetails.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama application instance
  - **Resource types (\*required):** [applicationInstance\*](#list_panorama-resource-applicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDevice](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeDevice.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama Appliance
  - **Resource types (\*required):** [device\*](#list_panorama-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDeviceJob](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeDeviceJob.html)  **
  - **Description:** Grants permission to view job details for an AWS Panorama Appliance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeNode](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeNode.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama application node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeNodeFromTemplateJob](https://docs.aws.amazon.com/panorama/latest/api/API_DescribeNodeFromTemplateJob.html)  **
  - **Description:** Grants permission to view details about AWS Panorama application node
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePackage](https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackage.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama package
  - **Resource types (\*required):** [package\*](#list_panorama-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePackageImportJob](https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackageImportJob.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama package
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePackageVersion](https://docs.aws.amazon.com/panorama/latest/api/API_DescribePackageVersion.html)  **
  - **Description:** Grants permission to view details about an AWS Panorama package version
  - **Resource types (\*required):** [package\*](#list_panorama-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplicationInstanceDependencies](https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstanceDependencies.html)  **
  - **Description:** Grants permission to retrieve a list of application instance dependencies in AWS Panorama
  - **Resource types (\*required):** [applicationInstance\*](#list_panorama-resource-applicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApplicationInstanceNodeInstances](https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstanceNodeInstances.html)  **
  - **Description:** Grants permission to retrieve a list of node instances of application instances in AWS Panorama
  - **Resource types (\*required):** [applicationInstance\*](#list_panorama-resource-applicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApplicationInstances](https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstances.html)  **
  - **Description:** Grants permission to retrieve a list of application instances in AWS Panorama
  - **Resource types (\*required):** [device](#list_panorama-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDevices](https://docs.aws.amazon.com/panorama/latest/api/API_ListDevices.html)  **
  - **Description:** Grants permission to retrieve a list of appliances in AWS Panorama
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDevicesJobs](https://docs.aws.amazon.com/panorama/latest/api/API_ListDevicesJobs.html)  **
  - **Description:** Grants permission to retrieve a list of jobs for an AWS Panorama Appliance
  - **Resource types (\*required):** [device](#list_panorama-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNodeFromTemplateJobs](https://docs.aws.amazon.com/panorama/latest/api/API_ListNodeFromTemplateJobs.html)  **
  - **Description:** Grants permission to retrieve a list of Nodes for an AWS Panorama Appliance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNodes](https://docs.aws.amazon.com/panorama/latest/api/API_ListNodes.html)  **
  - **Description:** Grants permission to retrieve a list of nodes in AWS Panorama
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackageImportJobs](https://docs.aws.amazon.com/panorama/latest/api/API_ListPackageImportJobs.html)  **
  - **Description:** Grants permission to retrieve a list of packages in AWS Panorama
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPackages](https://docs.aws.amazon.com/panorama/latest/api/API_ListPackages.html)  **
  - **Description:** Grants permission to retrieve a list of packages in AWS Panorama
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/panorama/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags for a resource in AWS Panorama
  - **Resource types (\*required):** [applicationInstance](#list_panorama-resource-applicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device](#list_panorama-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [package](#list_panorama-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ProvisionDevice](https://docs.aws.amazon.com/panorama/latest/api/API_ProvisionDevice.html)  **
  - **Description:** Grants permission to register an AWS Panorama Appliance
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_panorama-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Access level:** Write

- **   [RegisterPackageVersion](https://docs.aws.amazon.com/panorama/latest/api/API_RegisterPackageVersion.html)  **
  - **Description:** Grants permission to register an AWS Panorama package version
  - **Resource types (\*required):** [package\*](#list_panorama-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveApplicationInstance](https://docs.aws.amazon.com/panorama/latest/api/API_RemoveApplicationInstance.html)  **
  - **Description:** Grants permission to remove an AWS Panorama application instance
  - **Resource types (\*required):** [applicationInstance\*](#list_panorama-resource-applicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SignalApplicationInstanceNodeInstances](https://docs.aws.amazon.com/panorama/latest/api/API_SignalApplicationInstanceNodeInstances.html)  **
  - **Description:** Grants permission to signal camera nodes in an application instance to pause or resume
  - **Resource types (\*required):** [applicationInstance\*](#list_panorama-resource-applicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/panorama/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource in AWS Panorama
  - **Resource types (\*required):** [applicationInstance](#list_panorama-resource-applicationInstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_panorama-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Resource types (\*required):** [device](#list_panorama-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_panorama-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_panorama-resource-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_panorama-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/panorama/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource in AWS Panorama
  - **Resource types (\*required):** [applicationInstance](#list_panorama-resource-applicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Resource types (\*required):** [device](#list_panorama-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_panorama-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_panorama-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDeviceMetadata](https://docs.aws.amazon.com/panorama/latest/api/API_UpdateDeviceMetadata.html)  **
  - **Description:** Grants permission to modify basic settings for an AWS Panorama Appliance
  - **Resource types (\*required):** [device\*](#list_panorama-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Panorama
<a name="list_panorama-permission-only-actions"></a>

The following actions are defined by AWS Panorama but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeSoftware](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspanorama.html)  | Grants permission to view details about a software version for the AWS Panorama Appliance |  |   | Read | 
|   [GetWebSocketURL](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awspanorama.html)  | Grants permission to generate a WebSocket endpoint for communication with AWS Panorama |  |   | Read | 

## Resource types defined by AWS Panorama
<a name="list_panorama-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [applicationInstance](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-application)  | arn:${Partition}:panorama:${Region}:${Account}:applicationInstance/${ApplicationInstanceId} | [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_) | 
|  [device](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-appliance)  | arn:${Partition}:panorama:${Region}:${Account}:device/${DeviceId} | [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_) | 
|  [package](https://docs.aws.amazon.com/panorama/latest/dev/gettingstarted-concepts.html#gettingstarted-concepts-node)  | arn:${Partition}:panorama:${Region}:${Account}:package/${PackageId} | [aws:ResourceTag/${TagKey}](#list_panorama-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Panorama
<a name="list_panorama-policy-keys"></a>

AWS Panorama defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 