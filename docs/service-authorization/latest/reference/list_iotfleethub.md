

# Actions, resources, and condition keys for AWS IoT Fleet Hub for Device Management
<a name="list_iotfleethub"></a>

AWS IoT Fleet Hub for Device Management (service prefix: `iotfleethub`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot/latest/fleethubuserguide).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Fleet_Hub.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot/latest/fleethubuserguide/aws-iot-monitor-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotfleethub/iotfleethub.json) for this service.

**Topics**
+ [Actions defined by AWS IoT Fleet Hub for Device Management](#list_iotfleethub-actions-as-permissions)
+ [Resource types defined by AWS IoT Fleet Hub for Device Management](#list_iotfleethub-resources-for-iam-policies)
+ [Condition keys for AWS IoT Fleet Hub for Device Management](#list_iotfleethub-policy-keys)

## Actions defined by AWS IoT Fleet Hub for Device Management
<a name="list_iotfleethub-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplication](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleethub-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotfleethub-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [application\*](#list_iotfleethub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApplication](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_DescribeApplication.html)  **
  - **Description:** Grants permission to describe an application
  - **Resource types (\*required):** [application\*](#list_iotfleethub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_ListApplications.html)  **
  - **Description:** Grants permission to list all applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for a resource
  - **Resource types (\*required):** [application](#list_iotfleethub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [application](#list_iotfleethub-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotfleethub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleethub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [application](#list_iotfleethub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotfleethub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application
  - **Resource types (\*required):** [application\*](#list_iotfleethub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT Fleet Hub for Device Management
<a name="list_iotfleethub-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_ApplicationSummary.html)  | arn:${Partition}:iotfleethub:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT Fleet Hub for Device Management
<a name="list_iotfleethub-policy-keys"></a>

AWS IoT Fleet Hub for Device Management defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions by the tag keys in the request | ArrayOfString | 