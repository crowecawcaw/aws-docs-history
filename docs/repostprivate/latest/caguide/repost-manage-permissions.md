

End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html). 

# Manage access to Support case creation and management in re:Post Private
<a name="repost-manage-permissions"></a>

You must create an AWS Identity and Access Management (IAM) role to manage access to Support case creation and management from AWS re:Post Private. This role performs the following Support actions for you:
+ [CreateCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html)
+ [AddCommunicationToCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddCommunicationToCase.html)
+ [ResolveCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_ResolveCase.html)

After you create the IAM role, attach an IAM policy to this role so that the role has the required permissions to complete these actions. You choose this role when you create your private re:Post in the re:Post Private console.

Users in your private re:Post have the same permissions that you grant to the IAM role.

**Important**  
If you change the IAM role or the IAM policy, then your changes apply to the private re:Post that you configured.

Follow these procedures to create your IAM role and policy.

**Topics**
+ [Use an AWS managed policy or create a customer managed policy](#create-iam-role-support-app)
+ [Example IAM policy](#example-repost-policy)
+ [Create an IAM role](#creating-an-iam-role-for-repost)
+ [Troubleshooting](#troubleshooting-permissions-for-support-app)

## Use an AWS managed policy or create a customer managed policy
<a name="create-iam-role-support-app"></a>

To grant your role permissions, you can use either an AWS managed policy or a customer managed policy. 

**Tip**  
If you don't want to create a policy manually, then we recommend that you use an AWS managed policy instead and skip this procedure. Managed policies automatically have the required permissions for Support. You don't need to update the policies manually. For more information, see [AWS managed policy: AWSRepostSpaceSupportOperationsPolicy](security-with-iam-managed-policy.md#support-case-manpol).

Follow this procedure to create a customer managed policy for your role. This procedure uses the JSON policy editor in the IAM console. 

**To create a customer managed policy for re:Post Private**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**. 

1. Choose **Create policy**.

1. Choose the **JSON** tab.

1. Enter your JSON, and then replace the default JSON in the editor. You can use the [example policy](#example-repost-policy).

1. Choose **Next: Tags**.

1. (Optional) You can use tags as key–value pairs to add metadata to the policy.

1. Choose **Next: Review**.

1. On the **Review policy** page, enter a **Name**, such as {{`rePostPrivateSupportPolicy`}}, and a **Description** (optional). 

1. Review the **Summary** page to see the permissions that the policy allows, and then choose **Create policy**.

This policy defines the actions that the role can take. For more information, see [Creating IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*. 

## Example IAM policy
<a name="example-repost-policy"></a>

You can attach the following example policy to your IAM role. This policy allows the role to have full permissions to all required actions for Support. After you configure a private re:Post with the role, any user in your private re:Post has the same permissions.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "RepostSpaceSupportOperations",
			"Effect": "Allow",
			"Action": [
				"support:AddAttachmentsToSet",
				"support:AddCommunicationToCase",
				"support:CreateCase",
				"support:DescribeCases",
				"support:DescribeCommunications",
				"support:ResolveCase"
			],
			"Resource": "*"
		}
	]
}
```

------

**Note**  
For a list of AWS managed policies for re:Post Private, see [AWS managed policies for AWS re:Post Private](security-with-iam-managed-policy.md).

You can update the policy to remove a permission from Support.

For descriptions for each action, see the following topics in the *Service Authorization Reference*:
+ [Actions, resources, and condition keys for AWS Support](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupport.html)
+ [Actions, resources, and condition keys for Service Quotas](https://docs.aws.amazon.com/service-authorization/latest/reference/list_servicequotas.html)
+ [Actions, resources, and condition keys for AWS Identity and Access Management](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html)

## Create an IAM role
<a name="creating-an-iam-role-for-repost"></a>

After you create the policy, you must create an IAM role, and then attach the policy to that role. You choose this role when you create a private re:Post in the re:Post Private console.

**To create a role for Support case creation and management**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose **Create role**.

1. For **Trusted entity type**, choose **Custom trust policy**. 

1. For **Custom trust policy**, enter the following:

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
   				"Service": "repostspace.amazonaws.com"
   			},
   			"Action": [
   				"sts:AssumeRole",
   				"sts:SetSourceIdentity"
   			]
   		}
   	]
   }
   ```

------

1. Choose **Next**.

1. Under **Permissions policies**, in the search bar, enter the AWS managed policy or a customer managed policy that you created, such as {{`rePostPrivateSupportPolicy`}}. Select the check box that's next to the permissions policies that you want the service to have.

1. Choose **Next**.

1. On the **Name, review, and create** page, for **Role name**, enter a name, such as {{`rePostPrivateSupportRole`}}.

1. (Optional) For **Description**, enter a description for the role.

1. Review the trust policy and permissions.

1. (Optional) You can use tags as key–value pairs to add metadata to the role. For more information about using tags in IAM, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html).

1. Choose **Create role**. You can now choose this role when you configure a private re:Post in the re:Post Private console. See [Create a new private re:Post](create-new-repost.md).

For more information, see [Creating a role for an AWS service (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the *IAM User Guide*.

## Troubleshooting
<a name="troubleshooting-permissions-for-support-app"></a>

See the following topics to manage access to re:Post Private.

**Contents**
+ [I want to restrict specific users in my private re:Post from specific actions](#restrict-repost-users)
+ [When I configure a private re:Post, I don't see the IAM role that I created](#missing-iam-role)
+ [My IAM role is missing a permission](#missing-permissions-repost)
+ [An error says that my IAM role isn't valid](#find-the-configured-iam-role)

### I want to restrict specific users in my private re:Post from specific actions
<a name="restrict-repost-users"></a>

By default, users in your private re:Post have the same permissions specified in the IAM policy that you attach to the IAM role that you create. This means that anyone in the private re:Post has read or write access to create and manage Support cases, whether or not they have an AWS account or an IAM user.

We recommend the following best practices:
+ Use an IAM policy that has the minimum required permissions to the Support. See [AWS managed policy: AWSRepostSpaceSupportOperationsPolicy](security-with-iam-managed-policy.md#support-case-manpol).

### When I configure a private re:Post, I don't see the IAM role that I created
<a name="missing-iam-role"></a>

If your IAM role doesn't appear in the **IAM role for re:Post Private;** list, this means that the role doesn't have re:Post Private as a trusted entity, or that the role was deleted. You can update the existing role, or create another one. See [Create an IAM role](#creating-an-iam-role-for-repost).

### My IAM role is missing a permission
<a name="missing-permissions-repost"></a>

The IAM role that you create for your private re:Post needs permissions to perform the actions that you want. For example, if you want your users in the private re:Post to create support cases, the role must have the `support:CreateCase` permission. re:Post Private assumes this role to perform these actions for you. 

If you receive an error about a missing permission for Support, verify that the policy attached to your role has the required permission.

See the previous [Example IAM policy](#example-repost-policy).

### An error says that my IAM role isn't valid
<a name="find-the-configured-iam-role"></a>

Verify that you chose the correct role for your private re:Post configuration.