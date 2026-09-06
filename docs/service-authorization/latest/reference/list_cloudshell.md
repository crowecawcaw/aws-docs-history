

# Actions, resources, and condition keys for AWS CloudShell
<a name="list_cloudshell"></a>

AWS CloudShell (service prefix: `cloudshell`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudshell/cloudshell.json) for this service.

**Topics**
+ [Actions defined by AWS CloudShell](#list_cloudshell-actions-as-permissions)
+ [Permission-only actions for AWS CloudShell](#list_cloudshell-permission-only-actions)
+ [Resource types defined by AWS CloudShell](#list_cloudshell-resources-for-iam-policies)
+ [Condition keys for AWS CloudShell](#list_cloudshell-policy-keys)

## Actions defined by AWS CloudShell
<a name="list_cloudshell-actions-as-permissions"></a>

AWS CloudShell has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS CloudShell
<a name="list_cloudshell-permission-only-actions"></a>

The following actions are defined by AWS CloudShell but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ApproveCommand](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#ApproveCommand)  **
  - **Description:** Grants permission to approve a command sent by another AWS service
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateEnvironment](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#CreateEnvironment)  **
  - **Description:** Grants permissions to create a CloudShell environment
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudshell:SecurityGroupIds](#list_cloudshell-cloudshell_SecurityGroupIds)<br />[cloudshell:SubnetIds](#list_cloudshell-cloudshell_SubnetIds)<br />[cloudshell:VpcIds](#list_cloudshell-cloudshell_VpcIds)
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#CreateSession)  **
  - **Description:** Grants permissions to connect to a CloudShell environment from the AWS Management Console
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#DeleteEnvironment)  **
  - **Description:** Grants permission to delete a CloudShell environment
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeEnvironments](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#DescribeEnvironments)  **
  - **Description:** Grants permission to return descriptions of existing user's environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetEnvironmentStatus](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#GetEnvironmentStatus)  **
  - **Description:** Grants permission to read a CloudShell environment status
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFileDownloadUrls](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#GetFileDownloadUrls)  **
  - **Description:** Grants permissions to download files from a CloudShell environment
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetFileUploadUrls](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#GetFileUploadUrls)  **
  - **Description:** Grants permissions to upload files to a CloudShell environment
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutCredentials](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#PutCredentials)  **
  - **Description:** Grants permissions to forward console credentials to the environment
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartEnvironment](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#StartEnvironment)  **
  - **Description:** Grants permission to start a stopped CloudShell environment
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopEnvironment](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#StopEnvironment)  **
  - **Description:** Grants permission to stop a running CloudShell environment
  - **Resource types (\*required):** [Environment\*](#list_cloudshell-resource-Environment)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS CloudShell
<a name="list_cloudshell-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Environment](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html#Environment)  | arn:${Partition}:cloudshell:${Region}:${Account}:environment/${EnvironmentId} |   | 

## Condition keys for AWS CloudShell
<a name="list_cloudshell-policy-keys"></a>

AWS CloudShell defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [cloudshell:SecurityGroupIds](https://docs.aws.amazon.com/cloudshell/latest/userguide/aws-cloudshell-vpc-permissions-1.html#vpc-condition-keys-examples-1)  | Filters access by security group ids. Available during CreateEnvironment operation | ArrayOfString | 
|   [cloudshell:SubnetIds](https://docs.aws.amazon.com/cloudshell/latest/userguide/aws-cloudshell-vpc-permissions-1.html#vpc-condition-keys-examples-1)  | Filters access by subnet ids. Available during CreateEnvironment operation | ArrayOfString | 
|   [cloudshell:VpcIds](https://docs.aws.amazon.com/cloudshell/latest/userguide/aws-cloudshell-vpc-permissions-1.html#vpc-condition-keys-examples-1)  | Filters access by vpc ids. Available during CreateEnvironment operation | ArrayOfString | 