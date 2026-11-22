

# Create an IAM role for Amazon EVS administrators

Create an IAM role with a permissions policy that allows Amazon Elastic VMware Service operations, so that your administrators use temporary credentials instead of long-term keys. You can use the IAM console or the AWS CLI.

Administrators assume the role by calling the AWS Security Token Service (AWS STS) `AssumeRole` API operation, which returns temporary security credentials. For more information, see [Create a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the * AWS Identity and Access Management User Guide*.

**Note**  
Amazon EVS does not support the use of an instance profile to pass an IAM role to an EC2 instance.

## Before you begin
<a name="setup-iam-role-prereqs"></a>

Make sure that the following are true.
+ You’re signed in as an IAM principal that has permission to create IAM policies and roles and to attach policies to roles (`iam:CreatePolicy`, `iam:CreateRole`, and `iam:AttachRolePolicy`).
+ You’ve chosen the permissions for the policy. For an example policy for creating and managing an environment, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md). For all Amazon EVS actions, resources, and condition keys, see [Actions, resources, and condition keys for Amazon Elastic VMware Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_evs.html) in the *Service Authorization Reference*.
+ You know the AWS account ID of the account whose users assume the role.
+ Your IAM principal also has the `iam:CreateServiceLinkedRole` permission, so that Amazon EVS can create its service-linked role the first time that you create an environment. For more information, see [Using service-linked roles for Amazon EVS](using-service-linked-roles.md).

## Create the policy and the role
<a name="setup-iam-role-steps"></a>

You can create the policy and the role in the IAM console or with the AWS CLI. Choose the tab for the method that you use.

**Example**  

1. Open the [IAM console](https://console.aws.amazon.com/iam), choose **Policies** in the navigation pane, and then choose **Create policy**.

1. In the policy editor, enter a permissions policy that allows Amazon EVS operations.

1. Choose **Next**. Under **Policy name**, enter a name that identifies the policy, and review the permissions that the policy defines.

1. (Optional) Add tags to help identify, organize, or search for the policy, and then choose **Create policy**.

1. In the navigation pane, choose **Roles**, and then choose **Create role**.

1. For **Trusted entity type**, choose ** AWS account **.

1. Under **An AWS account **, specify the account whose users will perform Amazon EVS actions, and then choose **Next**.

1. On the **Add permissions** page, select the permissions policy that you created, and then choose **Next**.

1. Under **Role name**, enter a name that identifies the role.

1. Review the trust policy and confirm that the correct AWS account is listed as the principal.

1. (Optional) Add tags, and then choose **Create role**.

1. Verify the result. Choose the role, and confirm that the **Permissions** tab lists your policy and the **Trust relationships** tab lists the trusted account.

1. Copy the following contents to a trust policy JSON file. For the principal ARN, replace the example AWS account ID and `service-user` name with your own AWS account ID and IAM user name.

   ```json
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::123456789012:user/service-user" 
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

1. Create the role. Replace `evs-environment-role-trust-policy.json` with your trust policy file name.

   ```bash
   aws iam create-role \
     --role-name myAmazonEVSEnvironmentRole \
     --assume-role-policy-document file://evs-environment-role-trust-policy.json
   ```

1. Save your permissions policy to a JSON file, for example `evs-admin-policy.json`, and create the policy.

   ```bash
   POLICY_ARN=$(aws iam create-policy \
     --policy-name myAmazonEVSAdminPolicy \
     --policy-document file://evs-admin-policy.json \
     --query Policy.Arn \
     --output text)
   ```

   The command saves the policy ARN that `create-policy` returns in `POLICY_ARN`, so the next step uses the correct ARN in every partition.

1. Attach the policy to the role.

   ```bash
   aws iam attach-role-policy \
     --policy-arn $POLICY_ARN \
     --role-name myAmazonEVSEnvironmentRole
   ```

1. Verify that the policy is attached to the role.

   ```bash
   aws iam list-attached-role-policies \
     --role-name myAmazonEVSEnvironmentRole
   ```

   The response lists `myAmazonEVSAdminPolicy` under `AttachedPolicies`.

You have created an IAM role that your administrators can assume to work with Amazon EVS.

To troubleshoot access errors, see [Troubleshoot Amazon EVS identity and access](security-iam-troubleshoot.md).

Next, build the network for your environment. See [Build the network foundation](network-foundation.md).