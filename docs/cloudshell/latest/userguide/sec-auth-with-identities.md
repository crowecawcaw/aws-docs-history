# Managing AWS CloudShell access and usage with IAM
 policies

With the access management resources that can be provided by AWS Identity and Access Management, administrators can
 grant permissions to IAM users. That way, these users can access AWS CloudShell and use the
 environment's features. Administrators can also create policies that specify at a granular
 level what actions those users can perform with the shell environment.

The quickest way for an administrator to grant access to users is through an AWS managed
 policy. An [AWS managed
 policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") is a standalone policy that's created and administered by AWS. The
 following AWS managed policy for AWS CloudShell can be attached to IAM identities:


* **AWSCloudShellFullAccess**: Grants permission to use AWS CloudShell
 with full access to all features.
The **AWSCloudShellFullAccess** policy uses the wildcard
 (\*) character to give the IAM identity (user, role, or group) full access to CloudShell
 and features. For more information on this policy, see [AWSCloudShellFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudShellFullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudShellFullAccess.html") in the *AWS Managed Policy User Guide*.

###### Note

IAM identities with the following AWS managed policies can also launch
 CloudShell. However, these policies provide extensive permissions. So, we recommend that
 you only grant these policies if they're essential for an IAM user's job role.


* [Administrator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator"): Provides IAM users with full access and allows them to
 delegate permissions to every service and resource in AWS.
* [Developer power user](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_developer-power-user "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_developer-power-user"): Enables IAM users to perform application development
 tasks and create and configure resources and services that support AWS aware
 application development.
For more information about attaching managed policies, see [Adding
 IAM identity permissions (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console") in the
 *IAM User Guide*.


## Managing allowable actions in AWS CloudShell using custom
 policies


To manage the actions that an IAM user can perform with CloudShell, create a custom
 policy that uses the CloudShellPolicy managed policy as a template. Alternatively, edit an
 inline policy that's embedded in the relevant IAM identity (user,
 group, or role).


For example, you can allow IAM users to access CloudShell, but prevent them from
 forwarding the CloudShell environment credentials that are used to log in to
 AWS Management Console.


 


###### Important

To launch AWS CloudShell from the AWS Management Console, an IAM user needs permissions for the
 following actions:


* `CreateEnvironment`

* `CreateSession`

* `GetEnvironmentStatus`

* `StartEnvironment`
If one of these actions isn't explicitly allowed by an attached policy, an IAM
 permissions error is returned when you try to launch CloudShell.




AWS CloudShell permissions| Name | Description of permission granted | Required to launch CloudShell? |
| --- | --- | --- |
| `cloudshell:CreateEnvironment` | Creates a CloudShell environment, retrieves the layout at the start of the CloudShell session, and saves the current layout from the web application in the backend. This permission only expects `*` as the value for `Resource` as outlined in [Examples of IAM policies for CloudShell](#policy-examples "#policy-examples").  | Yes |
| `cloudshell:CreateSession` | Connects to a CloudShell environment from the AWS Management Console. | Yes |
| `cloudshell:GetEnvironmentStatus` | Read the status of a CloudShell environment. | Yes |
| `cloudshell:DeleteEnvironment` | Deletes a CloudShell environment. | No |
| `cloudshell:GetFileDownloadUrls` | Generates pre-signed Amazon S3 URLs that are used to download files through CloudShell using the CloudShell web interface. This is not available for VPC environments. | No |
| `cloudshell:GetFileUploadUrls` | Generates pre-signed Amazon S3 URLs that are used to upload files through CloudShell using the CloudShell web interface. This is not available for VPC environments. | No |
| `cloudshell:DescribeEnvironments` | Describes the environments. | No |
| `cloudshell:PutCredentials` | Forwards the credentials used to log in to the AWS Management Console to CloudShell. | No |
| `cloudshell:StartEnvironment` | Starts a CloudShell environment that is stopped. | Yes |
| `cloudshell:StopEnvironment` | Stops a CloudShell environment that is running. | No |
| `cloudshell:ApproveCommand` | Approves a command sent to CloudShell from other AWS Service consoles. | No | ### Examples of IAM policies for CloudShell The following examples show how policies can be created to restrict who can access CloudShell. The examples also show the actions that can be performed in the shell environment. This following policy enforces a complete denial of access to CloudShell and its features. JSON ``` `{ "Version":"2012-10-17", "Statement": [{ "Sid": "DenyCloudShell", "Effect": "Deny", "Action": [ "cloudshell:*" ], "Resource": "*" }] }` ``` This following policy allows IAM users to access CloudShell but blocks them from generating pre-signed URLs for file upload and download. Users can still transfer files to and from the environment, using clients like `wget` for example. JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowUsingCloudshell", "Effect": "Allow", "Action": [ "cloudshell:*" ], "Resource": "*" }, { "Sid": "DenyUploadDownload", "Effect": "Deny", "Action": [ "cloudshell:GetFileDownloadUrls", "cloudshell:GetFileUploadUrls" ], "Resource": "*" }] }` ``` The following policy allows IAM users to access CloudShell. However, the policy prevents the credentials that you used to log in to AWS Management Console from being forwarded to the CloudShell environment. IAM users with this policy need to manually configure their credentials within CloudShell. JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowUsingCloudshell", "Effect": "Allow", "Action": [ "cloudshell:*" ], "Resource": "*" }, { "Sid": "DenyCredentialForwarding", "Effect": "Deny", "Action": [ "cloudshell:PutCredentials" ], "Resource": "*" }] }` ``` The following policy allows IAM users to create AWS CloudShell environments. JSON ``` `{ "Version":"2012-10-17", "Statement": [{ "Sid": "CloudShellUser", "Effect": "Allow", "Action": [ "cloudshell:CreateEnvironment", "cloudshell:CreateSession", "cloudshell:GetEnvironmentStatus", "cloudshell:StartEnvironment" ], "Resource": "*" }] }` ``` ## Required IAM permissions for creating and using CloudShell VPC environments To create and use CloudShell VPC environments, the IAM administrator must enable access to VPC specific Amazon EC2 permissions. This section lists the Amazon EC2 permissions needed to create and use VPC environments. To create VPC environments, the IAM policy assigned to your role must include the following Amazon EC2 permissions: <br>• `ec2:DescribeVpcs` <br>• `ec2:DescribeSubnets` <br>• `ec2:DescribeSecurityGroups` <br>• `ec2:DescribeDhcpOptions` <br>• `ec2:DescribeNetworkInterfaces` <br>• `ec2:CreateTags` <br>• `ec2:CreateNetworkInterface` <br>• `ec2:CreateNetworkInterfacePermission` We recommend also including: <br>• **ec2:DeleteNetworkInterface** ###### Note This permission is not mandatory, but this is required for CloudShell to clean up the ENI resource (ENIs created for CloudShell VPC environments are tagged with **ManagedByCloudShell** key) created by it. If this permission not in enabled, you must manually clean up the ENI resource after every CloudShell VPC environment use. ### IAM policy granting full CloudShell access including access to VPC The following example displays how to enable full permissions, including access to VPC, to CloudShell: JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowCloudShellOperations", "Effect": "Allow", "Action": [ "cloudshell:*" ], "Resource": "*" }, { "Sid": "AllowDescribeVPC", "Effect": "Allow", "Action": [ "ec2:DescribeDhcpOptions", "ec2:DescribeNetworkInterfaces", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:DescribeVpcs" ], "Resource": "*" }, { "Sid": "AllowCreateTagWithCloudShellKey", "Effect": "Allow", "Action": [ "ec2:CreateTags" ], "Resource": "arn:aws:ec2:*:*:network-interface/*", "Condition": { "StringEquals": { "ec2:CreateAction": "CreateNetworkInterface" }, "ForAnyValue:StringEquals": { "aws:TagKeys": "ManagedByCloudShell" } } }, { "Sid": "AllowCreateNetworkInterfaceWithSubnetsAndSG", "Effect": "Allow", "Action": [ "ec2:CreateNetworkInterface" ], "Resource": [ "arn:aws:ec2:*:*:subnet/*", "arn:aws:ec2:*:*:security-group/*" ] }, { "Sid": "AllowCreateNetworkInterfaceWithCloudShellTag", "Effect": "Allow", "Action": [ "ec2:CreateNetworkInterface" ], "Resource": "arn:aws:ec2:*:*:network-interface/*", "Condition": { "ForAnyValue:StringEquals": { "aws:TagKeys": "ManagedByCloudShell" } } }, { "Sid": "AllowCreateNetworkInterfacePermissionWithCloudShellTag", "Effect": "Allow", "Action": [ "ec2:CreateNetworkInterfacePermission" ], "Resource": "arn:aws:ec2:*:*:network-interface/*", "Condition": { "StringEquals": { "aws:ResourceTag/ManagedByCloudShell": "" } } }, { "Sid": "AllowDeleteNetworkInterfaceWithCloudShellTag", "Effect": "Allow", "Action": [ "ec2:DeleteNetworkInterface" ], "Resource": "arn:aws:ec2:*:*:network-interface/*", "Condition": { "StringEquals": { "aws:ResourceTag/ManagedByCloudShell": "" } } } ] }` ``` ### Using IAM condition keys for VPC environments You can use CloudShell-specific condition keys for VPC settings to provide additional permission controls for your VPC environments. You can also specify the subnets and security groups that the VPC environment can and can't use. CloudShell supports the following condition keys in IAM policies: <br>• `CloudShell:VpcIds` – Allow or deny one or more VPCs <br>• `CloudShell:SubnetIds` – Allow or deny one or more subnets <br>• `CloudShell:SecurityGroupIds` – Allow or deny one or more security groups ###### Note If the permissions for users with access to public CloudShell environments are modified to add restriction to the `cloudshell:createEnvironment` action, they can still access their existing public environment. However, if you want to modify an IAM policy with this restriction and disable their access to the existing public environment, you must first update the IAM policy with the restriction, and then ensure that every CloudShell user in your account manually deletes the existing public environment using the CloudShell web user interface (**Actions** → **Delete CloudShell environment**). ### Example policies with condition keys for VPC settings The following examples demonstrate how to use condition keys for VPC settings. After you create a policy statement with the desired restrictions, append the policy statement for the target user or role. #### Ensure that users create only VPC environments and deny creation of public environments To ensure that users can create only VPC environments, use the deny permission as shown in the following example: ``` { "Statement": [ { "Sid": "DenyCloudShellNonVpcEnvironments", "Action": [ "cloudshell:CreateEnvironment" ], "Effect": "Deny", "Resource": "*", "Condition": { "Null": { "cloudshell:VpcIds": "true" } } } ] } ``` #### Deny users access to specific VPCs, subnets, or security groups To deny users access to specific VPCs, use `StringEquals` to check the value of the `cloudshell:VpcIds` condition. The following example denies users access to `vpc-1` and `vpc-2`: To deny users access to specific VPCs, use `StringEquals` to check the value of the `cloudshell:SubnetIds` condition. The following example denies users access to `subnet-1` and `subnet-2`: To deny users access to specific VPCs, use `StringEquals` to check the value of the `cloudshell:SecurityGroupIds` condition. The following example denies users access to `sg-1` and `sg-2`: JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "EnforceOutOfSecurityGroups", "Action": [ "cloudshell:CreateEnvironment" ], "Effect": "Deny", "Resource": "*", "Condition": { "ForAnyValue:StringEquals": { "cloudshell:SecurityGroupIds": [ "sg-1", "sg-2" ] } } } ] }` ``` #### Allow users to create environments with specific VPC configurations To allow users access to specific VPCs, use `StringEquals` to check the value of the `cloudshell:VpcIds` condition. The following example allows users access to `vpc-1` and `vpc-2`: To allow users access to specific VPCs, use `StringEquals` to check the value of the `cloudshell:SubnetIds` condition. The following example allows users access to `subnet-1` and `subnet-2`: JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "EnforceStayInSpecificSubnets", "Action": [ "cloudshell:CreateEnvironment" ], "Effect": "Allow", "Resource": "*", "Condition": { "ForAllValues:StringEquals": { "cloudshell:SubnetIds": [ "subnet-1", "subnet-2" ] } } } ] }` ``` To allow users access to specific VPCs, use `StringEquals` to check the value of the `cloudshell:SecurityGroupIds` condition. The following example allows users access to `sg-1` and `sg-2`: JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "EnforceStayInSpecificSecurityGroup", "Action": [ "cloudshell:CreateEnvironment" ], "Effect": "Allow", "Resource": "*", "Condition": { "ForAllValues:StringEquals": { "cloudshell:SecurityGroupIds": [ "sg-1", "sg-2" ] } } } ] }` ``` ## Permissions for accessing AWS services CloudShell uses the IAM credentials that you used to sign in to the AWS Management Console. ###### Note To use the IAM credentials that you used to sign in to the AWS Management Console, you must have `cloudshell:PutCredentials` permission. This pre-authentication feature of CloudShell makes it convenient to use AWS CLI. However, an IAM user still requires explicit permissions for the AWS services that are called from the command line. For example, suppose that IAM users are required to create Amazon S3 buckets and upload files as objects to them. You can create a policy that explicitly allows those actions. The IAM console provides an interactive [visual editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start") that guides through the process of building up a JSON-formatted policy document. After the policy is created, you can attach it to relevant IAM identity (user, group, or role). For more information about attaching managed policies, see [Adding IAM identity permissions (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console") in the *IAM User Guide*. ## Permissions for accessing Amazon Q CLI features in CloudShell To use Amazon Q CLI features in CloudShell, such as inline suggestions, chat, and translate, make sure you have the required IAM permissions. If you're unable to access Amazon Q CLI features in CloudShell, contact your administrator to provide you with the necessary IAM permissions. For more information, see [Identity-based policy examples for Amazon Q Developer](https://docs.aws.amazon.com/en_us/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.html "https://docs.aws.amazon.com/en_us/amazonq/latest/qdeveloper-ug/security_iam_id-based-policy-examples.html") in the *Amazon Q Developer User Guide*.
