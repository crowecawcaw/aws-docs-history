

# Granting permissions for using AWS Resource Groups and Tag Editor
<a name="gettingstarted-prereqs-permissions-howto"></a>

To add a policy for using AWS Resource Groups and Tag Editor to a user, do the following.

1. Open the [IAM console](https://console.aws.amazon.com/iam).

1. In the navigation pane, choose **Users**.

1. Find the user to whom you want to grant AWS Resource Groups and Tag Editor permissions. Choose the user's name to open the user properties page.

1. Choose **Add permissions**.

1. Choose **Attach existing policies directly**.

1. Choose **Create policy**.

1. On the **JSON** tab, paste the following policy statement.

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
           "resource-groups:*",
           "cloudformation:DescribeStacks",
           "cloudformation:ListStackResources",
           "tag:GetResources",
           "tag:TagResources",
           "tag:UntagResources",
           "tag:getTagKeys",
           "tag:getTagValues",
           "resource-explorer:*"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

------
**Note**  
This example policy statement grants permissions only for AWS Resource Groups and Tag Editor actions. It does not allow access to AWS Systems Manager tasks in the AWS Resource Groups console. For example, this policy does not grant permissions for you to use Systems Manager Automation commands. To perform Systems Manager tasks on resource groups, you must have Systems Manager permissions attached to your policy (such as `ssm:*`). For more information about granting access to Systems Manager, see [Configuring access to Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-access.html) in the *AWS Systems Manager User Guide*.

1. Choose **Review policy**.

1. Give the new policy a name and description. (for example, `AWSResourceGroupsQueryAPIAccess`).

1. Choose **Create policy**.

1. Now that the policy is saved in IAM, you can attach it to other users. For more information about how to add a policy to a user, see [Adding permissions by attaching policies directly to the user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#by-direct-attach-policy) in the *IAM User Guide*.