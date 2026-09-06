

# Actions, resources, and condition keys for AWS Cloud9
<a name="list_cloud9"></a>

AWS Cloud9 (service prefix: `cloud9`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloud9/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloud9/cloud9.json) for this service.

**Topics**
+ [API operations defined by AWS Cloud9](#list_cloud9-operations)
+ [Actions defined by AWS Cloud9](#list_cloud9-actions-as-permissions)
+ [Permission-only actions for AWS Cloud9](#list_cloud9-permission-only-actions)
+ [Resource types defined by AWS Cloud9](#list_cloud9-resources-for-iam-policies)
+ [Condition keys for AWS Cloud9](#list_cloud9-policy-keys)

## API operations defined by AWS Cloud9
<a name="list_cloud9-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloud9-actions-as-permissions).




- **   CreateEnvironmentEC2  **
  - **IAM action:**  [cloud9:CreateEnvironmentEC2](#list_cloud9-action-CreateEnvironmentEC2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloud9:TagResource](#list_cloud9-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEnvironmentMembership  **
  - **IAM action:**  [cloud9:CreateEnvironmentMembership](#list_cloud9-action-CreateEnvironmentMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [cloud9:DeleteEnvironment](#list_cloud9-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironmentMembership  **
  - **IAM action:**  [cloud9:DeleteEnvironmentMembership](#list_cloud9-action-DeleteEnvironmentMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeEnvironmentMemberships  **
  - **IAM action:**  [cloud9:DescribeEnvironmentMemberships](#list_cloud9-action-DescribeEnvironmentMemberships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEnvironmentStatus  **
  - **IAM action:**  [cloud9:DescribeEnvironmentStatus](#list_cloud9-action-DescribeEnvironmentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEnvironments  **
  - **IAM action:**  [cloud9:DescribeEnvironments](#list_cloud9-action-DescribeEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEnvironments  **
  - **IAM action:**  [cloud9:ListEnvironments](#list_cloud9-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [cloud9:ListTagsForResource](#list_cloud9-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [cloud9:TagResource](#list_cloud9-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cloud9:UntagResource](#list_cloud9-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEnvironment  **
  - **IAM action:**  [cloud9:UpdateEnvironment](#list_cloud9-action-UpdateEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironmentMembership  **
  - **IAM action:**  [cloud9:UpdateEnvironmentMembership](#list_cloud9-action-UpdateEnvironmentMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Cloud9
<a name="list_cloud9-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateEnvironmentEC2](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentEC2.html)  **
  - **Description:** Grants permission to create an AWS Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then hosts the environment on the instance
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloud9-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloud9-aws_TagKeys)<br />[cloud9:EnvironmentName](#list_cloud9-cloud9_EnvironmentName)<br />[cloud9:InstanceType](#list_cloud9-cloud9_InstanceType)<br />[cloud9:OwnerArn](#list_cloud9-cloud9_OwnerArn)<br />[cloud9:SubnetId](#list_cloud9-cloud9_SubnetId)<br />[cloud9:UserArn](#list_cloud9-cloud9_UserArn)
  - **Access level:** Write

- **   [CreateEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentMembership.html)  **
  - **Description:** Grants permission to add an environment member to an AWS Cloud9 development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)<br />[cloud9:EnvironmentId](#list_cloud9-cloud9_EnvironmentId)<br />[cloud9:Permissions](#list_cloud9-cloud9_Permissions)<br />[cloud9:UserArn](#list_cloud9-cloud9_UserArn)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an AWS Cloud9 development environment. If the environment is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance, also terminates the instance
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DeleteEnvironmentMembership.html)  **
  - **Description:** Grants permission to delete an environment member from an AWS Cloud9 development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)<br />[cloud9:EnvironmentId](#list_cloud9-cloud9_EnvironmentId)<br />[cloud9:UserArn](#list_cloud9-cloud9_UserArn)
  - **Access level:** Write

- **   [DescribeEnvironmentMemberships](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironmentMemberships.html)  **
  - **Description:** Grants permission to get information about environment members for an AWS Cloud9 development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)<br />[cloud9:EnvironmentId](#list_cloud9-cloud9_EnvironmentId)<br />[cloud9:UserArn](#list_cloud9-cloud9_UserArn)
  - **Access level:** Read

- **   [DescribeEnvironmentStatus](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironmentStatus.html)  **
  - **Description:** Grants permission to get status information for an AWS Cloud9 development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEnvironments](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironments.html)  **
  - **Description:** Grants permission to get information about AWS Cloud9 development environments
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEnvironments](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to get a list of AWS Cloud9 development environment identifiers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a cloud9 environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a cloud9 environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloud9-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloud9-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a cloud9 environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloud9-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to change the settings of an existing AWS Cloud9 development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UpdateEnvironmentMembership.html)  **
  - **Description:** Grants permission to change the settings of an existing environment member for an AWS Cloud9 development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)<br />[cloud9:EnvironmentId](#list_cloud9-cloud9_EnvironmentId)<br />[cloud9:Permissions](#list_cloud9-cloud9_Permissions)<br />[cloud9:UserArn](#list_cloud9-cloud9_UserArn)
  - **Access level:** Write



## Permission-only actions for AWS Cloud9
<a name="list_cloud9-permission-only-actions"></a>

The following actions are defined by AWS Cloud9 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ActivateEC2Remote](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to start the Amazon EC2 instance that your AWS Cloud9 IDE connects to
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironmentSSH](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to create an AWS Cloud9 SSH development environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloud9-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloud9-aws_TagKeys)<br />[cloud9:EnvironmentName](#list_cloud9-cloud9_EnvironmentName)<br />[cloud9:OwnerArn](#list_cloud9-cloud9_OwnerArn)
  - **Access level:** Write

- **   [CreateEnvironmentToken](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to create an authentication token that allows a connection between the AWS Cloud9 IDE and the user's environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEC2Remote](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get details about the connection to the EC2 development environment, including host, user, and port
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSSHRemote](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get details about the connection to the SSH development environment, including host, user, and port
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentConfig](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get configuration information that's used to initialize the AWS Cloud9 IDE
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentSettings](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get the AWS Cloud9 IDE settings for a specified development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMembershipSettings](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get the AWS Cloud9 IDE settings for a specified environment member
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMigrationExperiences](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get the migration experience for a cloud9 user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserPublicKey](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get the user's public SSH key, which is used by AWS Cloud9 to connect to SSH development environments
  - **Resource types (\*required):** 
  - **Condition keys:** [cloud9:UserArn](#list_cloud9-cloud9_UserArn)
  - **Access level:** Read

- **   [GetUserSettings](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to get the AWS Cloud9 IDE settings for a specified user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ModifyTemporaryCredentialsOnEnvironmentEC2](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to set AWS managed temporary credentials on the Amazon EC2 instance that's used by the AWS Cloud9 integrated development environment (IDE)
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironmentSettings](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to update the AWS Cloud9 IDE settings for a specified development environment
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMembershipSettings](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to update the AWS Cloud9 IDE settings for a specified environment member
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSSHRemote](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to update details about the connection to the SSH development environment, including host, user, and port
  - **Resource types (\*required):** [environment\*](#list_cloud9-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserSettings](https://docs.aws.amazon.com/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-ref-matrix)  **
  - **Description:** Grants permission to update IDE-specific settings of an AWS Cloud9 user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Cloud9
<a name="list_cloud9-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [environment](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-environment)  | arn:${Partition}:cloud9:${Region}:${Account}:environment:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cloud9-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Cloud9
<a name="list_cloud9-policy-keys"></a>

AWS Cloud9 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [cloud9:EnvironmentId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_EnvironmentId)  | Filters access by the AWS Cloud9 environment ID | String | 
|   [cloud9:EnvironmentName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_EnvironmentName)  | Filters access by the AWS Cloud9 environment name | String | 
|   [cloud9:InstanceType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_InstanceType)  | Filters access by the instance type of the AWS Cloud9 environment's Amazon EC2 instance | String | 
|   [cloud9:OwnerArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_OwnerArn)  | Filters access by the owner ARN specified | ARN | 
|   [cloud9:Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_Permissions)  | Filters access by the type of AWS Cloud9 permissions | String | 
|   [cloud9:SubnetId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_SubnetId)  | Filters access by the subnet ID that the AWS Cloud9 environment will be created in | String | 
|   [cloud9:UserArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscloud9.html##awscloud9-cloud9_UserArn)  | Filters access by the user ARN specified | ARN | 