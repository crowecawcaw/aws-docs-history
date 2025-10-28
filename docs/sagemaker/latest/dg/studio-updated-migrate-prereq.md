# Complete prerequisites to migrate the

Studio experience

Migration of the default experience from Studio Classic to Studio is managed by the
administrator of the existing domain. If you do not have permissions to set Studio as
the default experience for the existing domain, contact your administrator. To migrate your
default experience, you must have administrator permissions or at least have permissions to
update the existing domain, AWS Identity and Access Management (IAM), and Amazon Simple Storage Service (Amazon S3). Complete the following
prerequisites before migrating an existing domain from Studio Classic to Studio.

- The AWS Identity and Access Management role used to complete migration must have a policy attached with at least the
  following permissions. For information about creating an IAM policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

###### Note

The release of Studio includes updates to the AWS managed policies. For
more information, see [SageMaker AI Updates to AWS Managed
Policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

    + Phase 1 required permissions:




    	- `iam:CreateServiceLinkedRole`
    	- `iam:PassRole`
    	- `sagemaker:DescribeDomain`
    	- `sagemaker:UpdateDomain`
    	- `sagemaker:CreateDomain`
    	- `sagemaker:CreateUserProfile`
    	- `sagemaker:ListApps`
    	- `sagemaker:AddTags`
    	- `sagemaker:DeleteApp`
    	- `sagemaker:DeleteSpace`
    	- `sagemaker:UpdateSpace`
    	- `sagemaker:DeleteUserProfile`
    	- `sagemaker:DeleteDomain`
    	- `s3:PutBucketCORS`
    + Phase 2 required permissions (Optional, only if using lifecycle
     configuration scripts):


    No additional permissions needed. If the existing domain has lifecycle
     configurations and custom images, the admin will already have the required
     permissions.
    + Phase 3 using custom Amazon Elastic File System required permissions (Optional, only if
     transfering data):




    	- `efs:CreateFileSystem`
    	- `efs:CreateMountTarget`
    	- `efs:DescribeFileSystems`
    	- `efs:DescribeMountTargets`
    	- `efs:DescribeMountTargetSecurityGroups`
    	- `efs:ModifyMountTargetSecurityGroups`
    	- `ec2:DescribeSubnets`
    	- `ec2:DescribeSecurityGroups`
    	- `ec2:DescribeNetworkInterfaceAttribute`
    	- `ec2:DescribeNetworkInterfaces`
    	- `ec2:AuthorizeSecurityGroupEgress`
    	- `ec2:AuthorizeSecurityGroupIngress`
    	- `ec2:CreateNetworkInterface`
    	- `ec2:CreateNetworkInterfacePermission`
    	- `ec2:RevokeSecurityGroupIngress`
    	- `ec2:RevokeSecurityGroupEgress`
    	- `ec2:DeleteSecurityGroup`
    	- `datasync:CreateLocationEfs`
    	- `datasync:CreateTask`
    	- `datasync:StartTaskExecution`
    	- `datasync:DeleteTask`
    	- `datasync:DeleteLocation`
    	- `sagemaker:ListUserProfiles`
    	- `sagemaker:DescribeUserProfile`
    	- `sagemaker:UpdateDomain`
    	- `sagemaker:UpdateUserProfile`
    + Phase 3 using Amazon Simple Storage Service required permissions (Optional, only if transfering
     data):




    	- `iam:CreateRole`
    	- `iam:GetRole`
    	- `iam:AttachRolePolicy`
    	- `iam:DetachRolePolicy`
    	- `iam:DeleteRole`
    	- `efs:DescribeFileSystems`
    	- `efs:DescribeMountTargets`
    	- `efs:DescribeMountTargetSecurityGroups`
    	- `ec2:DescribeSubnets`
    	- `ec2:CreateSecurityGroup`
    	- `ec2:DescribeSecurityGroups`
    	- `ec2:DescribeNetworkInterfaces`
    	- `ec2:CreateNetworkInterface`
    	- `ec2:CreateNetworkInterfacePermission`
    	- `ec2:DetachNetworkInterfaces`
    	- `ec2:DeleteNetworkInterface`
    	- `ec2:DeleteNetworkInterfacePermission`
    	- `ec2:CreateTags`
    	- `ec2:AuthorizeSecurityGroupEgress`
    	- `ec2:AuthorizeSecurityGroupIngress`
    	- `ec2:RevokeSecurityGroupIngress`
    	- `ec2:RevokeSecurityGroupEgress`
    	- `ec2:DeleteSecurityGroup`
    	- `datasync:CreateLocationEfs`
    	- `datasync:CreateLocationS3`
    	- `datasync:CreateTask`
    	- `datasync:StartTaskExecution`
    	- `datasync:DescribeTaskExecution`
    	- `datasync:DeleteTask`
    	- `datasync:DeleteLocation`
    	- `sagemaker:CreateStudioLifecycleConfig`
    	- `sagemaker:UpdateDomain`
    	- `s3:ListBucket`
    	- `s3:GetObject`

- Access to AWS services from a terminal environment on either:
  - Your local machine using the AWS CLI version `2.13+`. Use the following
    command to verify the AWS CLI version.

  ```
  aws --version
  ```

  - AWS CloudShell. For more information, see [What is AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md")

- From your local machine or AWS CloudShell, run the following command
  and provide your AWS credentials. For information about AWS credentials, see
  [Understanding and getting your AWS credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md").

```
aws configure
```

- Verify that the lightweight JSON processor, jq, is installed in the
  terminal environment. jq is required to parse AWS CLI responses.

```
jq --version
```

If jq is not installed, install it using one of the following
commands:

    + ```
    sudo apt-get install -y jq
    ```
    + ```
    sudo yum install -y jq
    ```
