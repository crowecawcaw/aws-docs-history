

# Step 2: Set Up IAM Permissions
<a name="getting-started-iam-permissions"></a>

Next, you must create an AWS Identity and Access Management (IAM) policy that gives users a basic set of permissions (e.g., to create an Amazon IVS channel, get streaming information, and auto-record-to-S3) and assign that policy to users. You can either assign the permissions when creating a [new user](#iam-permissions-new-user) or add permissions to an [existing user](#iam-permissions-existing-user). Both procedures are given below.

For more information (for example, to learn about IAM users and policies, how to attach a policy to a user, and how to constrain what users can do with Amazon IVS), see:
+ [Creating an IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#Using_CreateUser_console) in the *IAM User Guide*
+ The information in [Amazon IVS Security](security.md) on IAM and "Managed Policies for IVS." 
+ For record-to-S3 functionality: [Using Service-Linked Roles](security-service-linked-roles.md) and [Auto-Record to Amazon S3](record-to-s3.md) in the *Amazon IVS User Guide*

You can either use an existing AWS managed policy for Amazon IVS or create a new policy that customizes the permissions you want to grant to a set of users, groups, or roles. Both approaches are described below.

## Use an Existing Policy for IVS Permissions
<a name="iam-permissions-existing-policy"></a>

In most cases, you will want to use an AWS managed policy for Amazon IVS. They are described fully in the [Managed Policies for IVS](security-iam-awsmanpol.md) section of *IVS Security*.
+ Use the `IVSReadOnlyAccess` AWS managed policy to give your application developers access to all IVS Get and List API operations (for both low-latency and real-time streaming).
+ Use the `IVSFullAccess` AWS managed policy to give your application developers access to all IVS API operations (for both low-latency and real-time streaming).

## Optional: Create a Custom Policy for Amazon IVS Permissions
<a name="iam-permissions-new-policy"></a>

Follow these steps:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**, then choose **Create policy**. A** Specify permissions** window opens..

1. In the **Specify permissions** window, choose the **JSON** tab, and copy and paste the following IVS policy to the **Policy editor** text area. (The policy does not include all Amazon IVS actions. You can add/delete (Allow/Deny) operation access permissions as needed. See [IVS Low-Latency Streaming API Reference](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/Welcome.html) for details on IVS operations.)

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
         {
            "Effect": "Allow",
            "Action": [
               "ivs:CreateChannel",
               "ivs:CreateRecordingConfiguration",
               "ivs:GetChannel",
               "ivs:GetRecordingConfiguration",
               "ivs:GetStream",
               "ivs:GetStreamKey",
               "ivs:GetStreamSession",
               "ivs:ListChannels",
               "ivs:ListRecordingConfigurations",
               "ivs:ListStreamKeys",
               "ivs:ListStreams",
               "ivs:ListStreamSessions"
             ],
             "Resource": "*"
         },
         {
            "Effect": "Allow",
            "Action": [
               "cloudwatch:DescribeAlarms",
               "cloudwatch:GetMetricData",
               "s3:CreateBucket",
               "s3:GetBucketLocation",
               "s3:ListAllMyBuckets",
               "servicequotas:ListAWSDefaultServiceQuotas",
               "servicequotas:ListRequestedServiceQuotaChangeHistoryByQuota",
               "servicequotas:ListServiceQuotas",
               "servicequotas:ListServices",
               "servicequotas:ListTagsForResource"
            ],
            "Resource": "*"
         },
         {
            "Effect": "Allow",
            "Action": [
               "iam:AttachRolePolicy",
               "iam:CreateServiceLinkedRole",
               "iam:PutRolePolicy"
            ],
            "Resource": 
   "arn:aws:iam::*:role/aws-service-role/ivs.amazonaws.com/AWSServiceRoleForIVSRecordToS3*"
         }
      ]
   }
   ```

------

1. Still in the **Specify permissions** window, choose **Next** (scroll to the bottom of the window to see this). A **Review and create** window opens. 

1. On the **Review and create** window, enter a **Policy name** and optionally add a **Description**. Make a note of the policy name, as you will need it when creating users (below). Choose **Create policy** (at the bottom of the window).

1. You are returned to the IAM console window, where you should see a banner confirming that your new policy was created.

## Create a New User and Add Permissions
<a name="iam-permissions-new-user"></a>

### IAM User Access Keys
<a name="iam-permissions-new-user-access-keys"></a>

IAM Access keys consist of an access key ID and a secret access key. They are used to sign programmatic requests that you make to AWS. If you don't have access keys, you can create them from the AWS Management Console. As a best practice, do not create root-user access keys.

*The only time that you can view or download a secret access key is when you create access keys. You cannot recover them later.* However, you can create new access keys at any time; you must have permissions to perform the required IAM actions.

Always store access keys securely. Never share them with third parties (even if an inquiry seems to come from Amazon). For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.

### Procedure
<a name="iam-permissions-new-user-procedure"></a>

Follow these steps:

1. In the navigation pane, choose **Users**, then choose **Create user**. A **Specify user details** window opens. 

1. In the **Specify user details** window:

   1. Under **User details**, type the new **User name** to be created.

   1. Check **Provide user access to the AWS Management Console**.

   1. When prompted, select **I want to create an IAM user**.

   1. Under **Console password**, select **Autogenerated password**.

   1. Check **Users must create a new password at next sign-in**.

   1. Choose **Next**. A **Set permissions** window opens.

1. Under **Set permissions**, select **Attach policies directly**. A **Permissions policies** window opens.

1. In the search box, enter an IVS policy name (either an AWS managed policy or your previously created custom policy). When it is found, check the box to select the policy.

1. Choose **Next** (at the bottom of the window). A **Review and create** window opens.

1. On the **Review and create** window, confirm that all user details are correct, then choose **Create user** (at the bottom of the window).

1. The **Retrieve password** window opens, containing your **Console sign-in details**. *Save this information securely for future reference*. When you are done, choose **Return to users list**.

## Add Permissions to an Existing User
<a name="iam-permissions-existing-user"></a>

Follow these steps:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users**, then choose an existing user name to be updated. (Choose the name by clicking on it; do not check the selection box.)

1. On the **Summary** page, on the **Permissions** tab, choose **Add permissions**. An **Add permissions** window opens.

1. Select **Attach existing policies directly**. A **Permissions policies** window opens.

1. In the search box, enter an IVS policy name (either an AWS managed policy or your previously created custom policy). When the policy is found, check the box to select the policy.

1. Choose **Next** (at the bottom of the window). A **Review** window opens.

1. On the **Review** window, select **Add permissions** (at the bottom of the window).

1. On the **Summary** page, confirm that the IVS policy was added.