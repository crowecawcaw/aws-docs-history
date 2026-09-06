

# Actions, resources, and condition keys for AWS Snow Device Management
<a name="list_snow-device-management"></a>

AWS Snow Device Management (service prefix: `snow-device-management`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-commands).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/snow-device-management/snow-device-management.json) for this service.

**Topics**
+ [API operations defined by AWS Snow Device Management](#list_snow-device-management-operations)
+ [Actions defined by AWS Snow Device Management](#list_snow-device-management-actions-as-permissions)
+ [Resource types defined by AWS Snow Device Management](#list_snow-device-management-resources-for-iam-policies)
+ [Condition keys for AWS Snow Device Management](#list_snow-device-management-policy-keys)

## API operations defined by AWS Snow Device Management
<a name="list_snow-device-management-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_snow-device-management-actions-as-permissions).




- **   CancelTask  **
  - **IAM action:**  [snow-device-management:CancelTask](#list_snow-device-management-action-CancelTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTask  **
  - **IAM action:**  [snow-device-management:CreateTask](#list_snow-device-management-action-CreateTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [snow-device-management:TagResource](#list_snow-device-management-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DescribeDevice  **
  - **IAM action:**  [snow-device-management:DescribeDevice](#list_snow-device-management-action-DescribeDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDeviceEc2Instances  **
  - **IAM action:**  [snow-device-management:DescribeDeviceEc2Instances](#list_snow-device-management-action-DescribeDeviceEc2Instances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExecution  **
  - **IAM action:**  [snow-device-management:DescribeExecution](#list_snow-device-management-action-DescribeExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTask  **
  - **IAM action:**  [snow-device-management:DescribeTask](#list_snow-device-management-action-DescribeTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeviceResources  **
  - **IAM action:**  [snow-device-management:ListDeviceResources](#list_snow-device-management-action-ListDeviceResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDevices  **
  - **IAM action:**  [snow-device-management:ListDevices](#list_snow-device-management-action-ListDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExecutions  **
  - **IAM action:**  [snow-device-management:ListExecutions](#list_snow-device-management-action-ListExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [snow-device-management:ListTagsForResource](#list_snow-device-management-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTasks  **
  - **IAM action:**  [snow-device-management:ListTasks](#list_snow-device-management-action-ListTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [snow-device-management:TagResource](#list_snow-device-management-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [snow-device-management:UntagResource](#list_snow-device-management-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Snow Device Management
<a name="list_snow-device-management-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelTask](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-cancel-task)  **
  - **Description:** Grants permission to cancel tasks on remote devices
  - **Resource types (\*required):** [task\*](#list_snow-device-management-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTask](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-create-task)  **
  - **Description:** Grants permission to create tasks on remote devices
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_snow-device-management-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_snow-device-management-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeDevice](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-describe-device)  **
  - **Description:** Grants permission to describe a remotely-managed device
  - **Resource types (\*required):** [managed-device\*](#list_snow-device-management-resource-managed-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDeviceEc2Instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-describe-ec2-instances)  **
  - **Description:** Grants permission to describe a remotely-managed device's EC2 instances
  - **Resource types (\*required):** [managed-device\*](#list_snow-device-management-resource-managed-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExecution](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-describe-execution)  **
  - **Description:** Grants permission to describe task executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTask](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-describe-task)  **
  - **Description:** Grants permission to describe a task
  - **Resource types (\*required):** [task\*](#list_snow-device-management-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeviceResources](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-list-device-resources)  **
  - **Description:** Grants permission to list a remotely-managed device's resources
  - **Resource types (\*required):** [managed-device\*](#list_snow-device-management-resource-managed-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDevices](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-list-devices)  **
  - **Description:** Grants permission to list remotely-managed devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExecutions](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-list-executions)  **
  - **Description:** Grants permission to list task executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-list-tags-for-resource)  **
  - **Description:** Grants permission to list the tags for a resource (device or task)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_snow-device-management-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_snow-device-management-aws_TagKeys)
  - **Access level:** Read

- **   [ListTasks](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-list-tasks)  **
  - **Description:** Grants permission to list tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-tag-resource)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [managed-device](#list_snow-device-management-resource-managed-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_snow-device-management-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_snow-device-management-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_snow-device-management-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_snow-device-management-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_snow-device-management-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html#sdm-cli-untag-resources)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [managed-device](#list_snow-device-management-resource-managed-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_snow-device-management-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_snow-device-management-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_snow-device-management-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Snow Device Management
<a name="list_snow-device-management-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [managed-device](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html)  | arn:${Partition}:snow-device-management:${Region}:${Account}:managed-device/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_) | 
|  [task](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html)  | arn:${Partition}:snow-device-management:${Region}:${Account}:task/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_snow-device-management-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Snow Device Management
<a name="list_snow-device-management-policy-keys"></a>

AWS Snow Device Management defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 