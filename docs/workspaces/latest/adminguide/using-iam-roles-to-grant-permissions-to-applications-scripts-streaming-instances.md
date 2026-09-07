

# Access to WorkSpaces and scripts on streaming instances
<a name="using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances"></a>

Applications and scripts that run on WorkSpaces streaming instances must include AWS credentials in their AWS API requests. You can create an IAM role to manage these credentials. An IAM role specifies a set of permissions that you can use to access AWS resources. This role is not uniquely associated with one person, however. Instead, it can be assumed by anyone that needs it.

You can apply an IAM role to a WorkSpaces streaming instance. When the streaming instance switches to (assumes) the role, the role provides temporary security credentials. Your application or scripts use these credentials to perform API actions and management tasks on the streaming instance. WorkSpaces manages the temporary credential switch for you.

**Topics**
+ [Best Practices for Using IAM Roles With WorkSpaces Streaming Instances](#best-practices-for-using-iam-role-with-streaming-instances)
+ [Configuring an Existing IAM Role to Use With WorkSpaces Streaming Instances](#configuring-existing-iam-role-to-use-with-streaming-instances)
+ [How to Create an IAM Role to Use With WorkSpaces Streaming Instances](#how-to-create-iam-role-to-use-with-streaming-instances)
+ [How to Use the IAM Role With WorkSpaces Streaming Instances](#how-to-use-iam-role-with-streaming-instances)

## Best Practices for Using IAM Roles With WorkSpaces Streaming Instances
<a name="best-practices-for-using-iam-role-with-streaming-instances"></a>

When you use IAM roles with WorkSpaces streaming instances, we recommend that you follow these practices:
+ Limit the permissions that you grant to AWS API actions and resources.

  Follow least privilege principles when you create and attach IAM policies to the IAM roles associated with WorkSpaces streaming instances. When you use an application or script that requires access to AWS API actions or resources, determine the specific actions and resources that are required. Then, create policies that allow the application or script to perform only those actions. For more information, see [Grant Least Privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.
+ Create an IAM role for each WorkSpaces resource.

  Creating a unique IAM role for each WorkSpaces resource is a practice that follows least privilege principles. Doing so also lets you modify permissions for a resource without affecting other resources.
+ Limit where the credentials can be used.

  IAM policies let you define the conditions under which your IAM role can be used to access a resource. For example, you can include conditions to specify a range of IP addresses that requests can come from. Doing so prevents the credentials from being used outside of your environment. For more information, see [Use Policy Conditions for Extra Security](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#use-policy-conditions) in the *IAM User Guide*.

## Configuring an Existing IAM Role to Use With WorkSpaces Streaming Instances
<a name="configuring-existing-iam-role-to-use-with-streaming-instances"></a>

This topic describes how to configure an existing IAM role so that you can use it with WorkSpaces .

**Prerequisites**

The IAM role that you want to use with WorkSpaces must meet the following prerequisites:
+ The IAM role must be in the same Amazon Web Services account as the WorkSpaces streaming instance.
+ The IAM role cannot be a service role.
+ The trust relationship policy that is attached to the IAM role must include the WorkSpaces service as the principal. A *principal* is an entity in AWS that can perform actions and access resources. The policy must also include the `sts:AssumeRole` action. This policy configuration defines WorkSpaces as a trusted entity.

  
+ If you are applying the IAM role to WorkSpaces, the WorkSpaces must run a version of the WorkSpaces agent released on or after September 3, 2019. If you are applying the IAM role to WorkSpaces, the WorkSpaces must use an image that uses a version of the agent released on or after the same date. 

**To enable the WorkSpaces service principal to assume an existing IAM role**

To perform the following steps, you must sign into the account as an IAM user who has the permissions required to list and update IAM roles. If you don't have the required permissions, ask your Amazon Web Services account administrator either to perform these steps in your account or to grant you the required permissions.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**. 

1. In the list of roles in your account, choose the name of the role that you want to modify.

1. Choose the **Trust relationships** tab, and then choose **Edit trust relationship**.

1. Under **Policy Document**, verify that the trust relationship policy includes the `sts:AssumeRole` action for the `workspaces.amazonaws.com` service principal:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": [
             "workspaces.amazonaws.com"
           ]
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

------

1. When you are finished editing your trust policy, choose **Update Trust Policy** to save your changes. 

1. The IAM role that you selected will display in the WorkSpaces console. This role grants permissions to applications and scripts to perform API actions and management tasks on streaming instances.

## How to Create an IAM Role to Use With WorkSpaces Streaming Instances
<a name="how-to-create-iam-role-to-use-with-streaming-instances"></a>

This topic describes how to create a new IAM role so that you can use it with WorkSpaces

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose **Create role**.

1. For **Select type of trusted entity**, choose **AWS service**.

1. From the list of AWS services, choose **WorkSpaces**.

1. Under **Select your use case**, **WorkSpaces — Allows WorkSpaces instances to call AWS services on your behalf** is already selected. Choose **Next: Permissions**.

1. If possible, select the policy to use for the permissions policy or choose **Create policy** to open a new browser tab and create a new policy from scratch. For more information, see step 4 in the procedure [Creating IAM Policies (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-start) in the *IAM User Guide*.

   After you create the policy, close that tab and return to your original tab. Select the check box next to the permissions policies that you want WorkSpaces to have.

1. (Optional) Set a permissions boundary. This is an advanced feature that is available for service roles, but not service-linked roles. For more information, see [Permissions Boundaries for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.

1. Choose **Next: Tags**. You can optionally attach tags as key-value pairs. For more information, see [Tagging IAM Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Choose **Next: Review**.

1. For **Role name**, type a role name that is unique within your Amazon Web Services account. Because other AWS resources might reference the role, you can't edit the name of the role after it has been created.

1. For **Role description**, keep the default role description or type a new one.

1. Review the role, and then choose **Create role**.

## How to Use the IAM Role With WorkSpaces Streaming Instances
<a name="how-to-use-iam-role-with-streaming-instances"></a>

After you create an IAM role, you can apply it to WorkSpaces when you launch WorkSpaces. You can also apply an IAM role to existing WorkSpaces.

When you apply an IAM role to WorkSpaces, WorkSpaces retrieves temporary credentials and creates the **workspaces\_machine\_role** credential profile on the instance. The temporary credentials are valid for 1 hour, and new credentials retrieved every hour. The previous credentials do not expire, so you can use them for as long as they are valid. You can use the credential profile to call AWS services programmatically by using the AWS Command Line Interface (AWS CLI), AWS Tools for PowerShell, or the AWS SDK with the language of your choice.

When you make the API calls, specify **workspaces\_machine\_role** as the credential profile. Otherwise, the operation fails due to insufficient permissions.

WorkSpaces assumes the specified role while the streaming instance is provisioned. Because WorkSpaces uses the elastic network interface that is attached to your VPC for AWS API calls, your application or script must wait for the elastic network interface to become available before making AWS API calls. If API calls are made before the elastic network interface is available, the calls fail.

The following examples show how you can use the **workspaces\_machine\_role** credential profile to describe streaming instances (EC2 instances) and to create the Boto client. Boto is the Amazon Web Services (AWS) SDK for Python. 

**Describe Streaming Instances (EC2 instances) by Using the AWS CLI**

```
aws ec2 describe-instances --region us-east-1 --profile workspaces_machine_role
```

**Describe Streaming Instances (EC2 instances) by Using AWS Tools for PowerShell**

You must use AWS Tools for PowerShell version 3.3.563.1 or later, with the Amazon Web Services SDK for .NET version 3.3.103.22 or later. You can download the AWS Tools for Windows installer, which includes AWS Tools for PowerShell and the Amazon Web Services SDK for .NET, from the [AWS Tools for PowerShell](https://aws.amazon.com/powershell/) website.

```
Get-EC2Instance -Region us-east-1 -ProfileName workspaces_machine_role
```

**Creating the Boto Client by Using the AWS SDK for Python**

```
session = boto3.Session(profile_name=workspaces_machine_role')
```