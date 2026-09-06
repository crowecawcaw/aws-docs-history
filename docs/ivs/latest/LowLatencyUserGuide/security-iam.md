

# Identity and Access Management in IVS
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an account administrator securely control access to AWS resources. Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies. IAM account administrators control who can be authenticated (signed in) and authorized (have permissions) to use Amazon IVS resources. IAM is a feature of your AWS account offered at no additional charge.

**Important**: For comprehensive information, see the [AWS IAM product page](https://aws.amazon.com/iam/), [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/), and [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html). Throughout this section, we also provide links to specific sections of the *IAM User Guide*. You should be familiar with this material before proceeding.

## Audience
<a name="security-iam-audience"></a>

How you use IAM differs, depending on the work you do in Amazon IVS:
+ **Service user** – If you use the Amazon IVS service to do your job, your administrator provides you with the credentials and permissions that you need. As you use more Amazon IVS features to do your work, you might need additional permissions. Understanding how access is managed can help you request the right permissions from your administrator. If you cannot access a feature in Amazon IVS, see [Troubleshooting](#security-iam-troubleshooting).
+ **Service administrator** – If you're in charge of Amazon IVS resources at your company, you probably have full access to Amazon IVS. It's your job to determine which Amazon IVS features and resources your employees should access. You must then submit requests to your IAM administrator, to change the permissions of your service users. Review the information on this page to understand basic IAM concepts. To learn more about how your company can use IAM with Amazon IVS, see [How Amazon IVS Works with IAM](#security-iam-how-ivs-works).
+ **IAM administrator** – If you're an IAM administrator, you can write policies to manage access to Amazon IVS. To view example Amazon IVS identity-based policies that you can use in IAM, see [Identity-Based Policy Examples](#security-iam-policy-examples). 

## How Amazon IVS Works with IAM
<a name="security-iam-how-ivs-works"></a>

Before you can make Amazon IVS API requests, you must create one or more IAM *identities* (users, groups, and roles) and IAM *policies*, then attach policies to identities. It takes up to a few minutes for the permissions to propagate; until then, API requests are rejected.

For a high-level view of how Amazon IVS works with IAM, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identities
<a name="security-iam-identities"></a>

You can create IAM identities to provide authentication for people and processes in your AWS account. IAM groups are collections of IAM users that you can manage as a unit. See [Identities (Users, Groups, and Roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.

## Policies
<a name="security-iam-policies"></a>

See these sections in the *IAM User Guide*:
+ [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) — All about policies.
+ [Actions, Resources, and Condition Keys for Amazon IVS](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninteractivevideoservice.html)
+ [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) 
+ [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) — All the elements that you can use in a JSON policy.

By default, IAM users and roles don't have permission to create or modify Amazon IVS resources (even to change their own passwords). They also cannot perform tasks using the AWS console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources that they need.

IAM policies define permissions for an action regardless of the method that is used to perform the operation. For example, suppose that you have a policy that allows the `iam:GetRole` action. A user with that policy can get role information from the AWS Management Console, the AWS CLI, or the AWS API.

Policies are JSON permissions-policy documents made up of *elements*. Amazon IVS supports three elements:
+ **Actions** — Policy actions for Amazon IVS use the `ivs` prefix before the action. For example, to grant someone permission to create an Amazon IVS channel with the Amazon IVS `CreateChannel` API method, you include the `ivs:CreateChannel` action in the policy for that person. Policy statements must include either an `Action` or `NotAction` element.
+ **Resources** — The Amazon IVS channel resource has the following [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) format:

  ```
  arn:aws:ivs:${Region}:${Account}:channel/${channelId}
  ```

  For example, to specify the `VgNkEJgOVX9N` channel in your statement, use this ARN:

  ```
  "Resource": "arn:aws:ivs:us-west-2:123456789012:channel/VgNkEJgOVX9N"
  ```

  Some Amazon IVS actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (`*`):

  ```
  "Resource":"*"
  ```
+ **Conditions** — Amazon IVS supports some global condition keys: `aws:RequestTag`, `aws:TagKeys`, and `aws:ResourceTag`.

You can use variables as placeholders in a policy. For example, you can grant an IAM user permission to access a resource only if it is tagged with the user’s IAM username. See [Variables and Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*.

Amazon IVS provides AWS managed policies that can be used to grant a preconfigured set of permissions to identities (read only or full access). You can choose to use managed policies instead of the identity-based policies shown below. For details, see [Managed Policies for Amazon IVS](security-iam-awsmanpol.md).

## Authorization Based on Amazon IVS Tags
<a name="security-iam-authorization"></a>

You can attach tags to Amazon IVS resources or pass tags in a request to Amazon IVS. To control access based on tags, you provide tag information in the condition element of a policy using the `aws:ResourceTag/key-name`, `aws:RequestTag/key-name`, or `aws:TagKeys` condition keys. For more information about tagging Amazon IVS resources, see “Tagging” in the [IVS Low-Latency Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/Welcome.html), [IVS Real-Time Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/Welcome.html), and [IVS Chat API Reference](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/Welcome.html). 

For an example, see [View Amazon IVS Channels Based on Tags](#security-iam-policy-examples-tags).

## Roles
<a name="security-iam-roles"></a>

See [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) and [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.

An IAM *role* is an entity within your AWS account that has specific permissions.

Amazon IVS supports using *temporary security credentials*. You can use temporary credentials to sign in with federation, assume an IAM role, or assume a cross-account role. You obtain temporary security credentials by calling [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) API operations such as `AssumeRole` or `GetFederationToken`.

## Privileged and Unprivileged Access
<a name="security-iam-privileged-access"></a>

API resources have privileged access. Unprivileged playback access can be set up through private channels; see [Setting Up Private Channels](private-channels.md).

## Best Practices for Policies
<a name="security-iam-policy-best-practices"></a>

See [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

Identity-based policies are very powerful. They determine whether someone can create, access, or delete Amazon IVS resources in your account. These actions can incur costs for your AWS account. Follow these recommendations:
+ **Grant least privilege** — When you create custom policies, grant only the permissions required to perform a task. Start with a minimum set of permissions and grant more permissions as needed. Doing so is more secure than starting with permissions that are too lenient, then trying to tighten them later. Specifically, reserve `ivs:*` for admin access; do not use it in applications.
+ **Enable multi-factor authentication (MFA) for sensitive operations** — For extra security, require IAM users to use MFA to access sensitive resources or API operations.
+ **Use policy conditions for extra security** — To the extent practical, define the conditions under which your identity-based policies allow access to a resource. For example, you can write conditions to specify a range of allowable IP addresses from which a request must come. You also can write conditions to allow requests only within a specified date or time range, or to require the use of SSL or MFA.

## Identity-Based Policy Examples
<a name="security-iam-policy-examples"></a>

### Use the Amazon IVS Console
<a name="security-iam-policy-examples-console"></a>

To access the Amazon IVS console, you must have a minimum set of permissions which allow you to list and view details about the Amazon IVS resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console will not function as intended for identities with that policy. To ensure access to the Amazon IVS console, attach the following policy to the identities (see [Adding and Removing IAM Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*).

The parts of the following policy provide access to:
+ All Amazon IVS API operations
+ Your Amazon IVS [service quotas](service-quotas.md)
+ Amazon S3 endpoints needed for IVS auto-record-to-S3 functionality (low-latency-streaming) and IVS composite-recording functionality (real-time streaming).
+ Auto-record-to-S3 service-linked-role creation
+ Amazon Cloudwatch to get metrics for your live-stream session

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Action": "ivs:*",
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "servicequotas:ListServiceQuotas"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "s3:CreateBucket",
        "s3:DeleteBucketPolicy",
        "s3:GetBucketLocation",
        "s3:GetBucketPolicy",
        "s3:ListAllMyBuckets",
        "s3:PutBucketPolicy"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "iam:AttachRolePolicy",
        "iam:CreateServiceLinkedRole",
        "iam:PutRolePolicy"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:iam::*:role/aws-service-role/ivs.amazonaws.com/AWSServiceRoleForIVSRecordToS3*"
    },
    {
      "Action": [
        "cloudwatch:GetMetricData"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "lambda:AddPermission",
        "lambda:ListFunctions"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

------

### Allow Users to View Their Own Permissions
<a name="security-iam-policy-examples-permissions"></a>

This example shows a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the AWS console or programmatically using the AWS CLI or AWS API.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Sid": "ViewOwnUserInfo",
         "Effect": "Allow",
         "Action": [
            "iam:GetUserPolicy",
            "iam:ListGroupsForUser",
            "iam:ListAttachedUserPolicies",
            "iam:ListUserPolicies",
            "iam:GetUser"
         ],
         "Resource": [
            "arn:aws:iam:*:*:user/${aws:username}"
         ]
      },
      {
         "Sid": "NavigateInConsole",
         "Effect": "Allow",
         "Action": [
            "iam:GetGroupPolicy",
            "iam:GetPolicyVersion",
            "iam:GetPolicy",
            "iam:ListAttachedGroupPolicies",
            "iam:ListGroupPolicies",
            "iam:ListPolicyVersions",
            "iam:ListPolicies",
            "iam:ListUsers"
         ],
         "Resource": "*"
      }
   ]
}
```

------

### Access an Amazon IVS Channel
<a name="security-iam-policy-examples-channel"></a>

Here, you want to grant an IAM user in your AWS account access to one of your Amazon IVS channels, `VgNkEJgOVX9N`. You also want to allow the user to stop the stream (`ivs:StopStream`), add metadata (`ivs:PutMetadata`), and update the channel (`ivs:UpdateChannel`). The policy also grants permissions required by the Amazon IVS console: `ivs:ListChannels`, `ivs:ListStreams`, `ivs:GetChannel`, and `ivs:GetStream`.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"ListChannelsInConsole",
         "Effect":"Allow",
         "Action":[
            "ivs:ListChannels",
            "ivs:ListStreams"

         ],
         "Resource":"arn:aws:ivs:*:*:channel/*"
      },
      {
         "Sid":"ViewSpecificChannelInfo",
         "Effect":"Allow",
         "Action":[
            "ivs:GetChannel",
            "ivs:GetStream"
         ],
         "Resource":"arn:aws:ivs:*:*:channel/VgNkEJgOVX9N"
      },
      {
         "Sid":"ManageChannel",
         "Effect":"Allow",
         "Action":[
            "ivs:StopStream",
            "ivs:PutMetadata",
            "ivs:UpdateChannel"
         ],
         "Resource":"arn:aws:ivs:*:*:channel/VgNkEJgOVX9N" 
      }
   ]
}
```

------

### View Amazon IVS Channels Based on Tags
<a name="security-iam-policy-examples-tags"></a>

You can use conditions in your identity-based policy to control access to Amazon IVS resources based on tags. This example shows a policy that allows viewing a channel. This policy also grants the permissions necessary to complete this action on the Amazon IVS console.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement": [
      {
         "Sid": "ListWidgetsInConsole",
         "Effect": "Allow",
         "Action": "ivs:ListChannels",
         "Resource": "arn:aws:ivs:*:*:channel/*"
      },
      {
         "Sid": "ViewChannelIfOwner",
         "Effect": "Allow",
         "Action": "ivs:GetChannel",
         "Resource": "arn:aws:ivs:*:*:channel/*",
         "Condition": {
            "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
         }
      }
   ]
}
```

------

You can attach this policy to the IAM users in your account. However, permission is granted only if the channel is tagged with that user's username as an owner. If a user named richard-roe tries to view an Amazon IVS channel, the channel must be tagged `Owner=richard-roe` or `owner=richard-roe`; otherwise he is denied access. (The condition tag key `Owner` matches both `Owner` and `owner` because condition-key names are not case sensitive.)

## Troubleshooting
<a name="security-iam-troubleshooting"></a>

Use the following information to help diagnose and fix common issues that you might encounter when working with Amazon IVS and IAM.
+ **I am not authorized to perform an action in Amazon IVS.** 

  The following example error occurs when the mateojackson IAM user tries to use the AWS console to view details about a channel but does not have `ivs:GetChannel` permission.

  ```
  User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: ivs:GetChannel on resource: arn:aws:ivs:us-west-2:123456789012:channel/VgNkEJgOVX9N
  ```

  In this case, Mateo asks his administrator to update his policies to allow him to access the `arn:aws:ivs:us-west-2:123456789012:channel/VgNkEJgOVX9N` resource using the `ivs:GetChannel` action.
+ **I want to view my access keys**.

  After you create your IAM user access keys, you can view your access key ID at any time. However, you can't view your secret access key again. If you lose your secret key, you must create a new access key pair. Access keys have two parts:
  + An access key ID (for example, `AKIAIOSFODNN7EXAMPLE`)
  + A secret access key (for example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`)

  As with a username and password, you must use both the access key ID and the secret access key together to authenticate your requests. Manage your access keys as securely as you do your user name and password.

  ***Important: Do not give your access keys to a third party, even to help [find your canonical user ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindingCanonicalId). Doing so might give someone permanent access to your account.***

  When you create an access key pair, you are prompted to save the access key ID and secret access key in a secure location. The secret access key is available only when you create it. If you lose your secret access key, you must add new access keys to your IAM user.

  You can have at most two access keys. If you already have two, you must delete one key pair before creating a new one. See [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.
+ **I'm an administrator and want to allow others to access Amazon IVS.**

  To allow others to access Amazon IVS, you must create an IAM entity (user or role) for the person or application that needs access. The person or application will use the credentials for that entity to access AWS. You must then attach a policy to the entity that grants the correct permissions in Amazon IVS.

  To get started, see [Creating Your First IAM Delegated User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in the *IAM User Guide*.
+ **I want to allow people outside my AWS account to access my Amazon IVS resources.**

  You can create a role that users in other accounts or people outside your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources. For related information, see these sections of the *IAM User Guide*:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/security-iam.html)