# Giving Amazon Personalize permission to access your resources

To give Amazon Personalize permission to access your resources, you create an IAM policy that provides Amazon Personalize full access to
your Amazon Personalize resources. Or you can use the AWS managed `AmazonPersonalizeFullAccess` policy.
`AmazonPersonalizeFullAccess` provides more permissions than are necessary. We recommend creating a new IAM
policy that only grants the necessary permissions. For more information about managed policies, see [AWS managed policies](security_iam_id-based-policy-examples.md#using-managed-policies "security_iam_id-based-policy-examples.md#using-managed-policies").

After you create a policy, you create an IAM role for Amazon Personalize and attach the new policy to
it.

###### Topics

- [Creating a new IAM policy for Amazon Personalize](#create-role-policy "#create-role-policy")
- [Creating an IAM role for Amazon Personalize](#set-up-create-role-with-permissions "#set-up-create-role-with-permissions")

## Creating a new IAM policy for Amazon Personalize

Create an IAM policy that provides Amazon Personalize full access to your Amazon Personalize resources.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "personalize:*"
            ],
            "Resource": "*"
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.

## Creating an IAM role for Amazon Personalize

To use Amazon Personalize, you must create an AWS Identity and Access Management service role for Amazon Personalize.

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.
After you
create a service role for Amazon Personalize, grant the role additional permissions listed in [Additional service role permissions](#additional-service-role-permissions "#additional-service-role-permissions")
as necessary.

###### To create the service role for Personalize (IAM console)

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose **Roles**, and
    then choose **Create role**.
3.  For **Trusted entity type**, choose **AWS service**.
4.  For **Service or use case**, choose **Personalize**, and then choose the **Personalize** use case.
5.  Choose **Next**.
6.  Chose the policy that you created in the previous procedure.
7.  (Optional) Set a [permissions
    boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
    not service-linked roles.

        1. Open the **Set permissions boundary** section, and then choose
        **Use a permissions boundary to control the maximum role permissions**.


        IAM includes a list of the AWS managed and customer-managed policies in your account.
        2. Select the policy to use for the permissions boundary.

8.  Choose **Next**.
9.  Enter a role name or a role name suffix to help you identify the purpose of the role.

###### Important

When you name a role, note the following:

    * Role names must be unique within your AWS account, and can't be made unique by case.


    For example, don't create roles named both `PRODROLE` and
     `prodrole`. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
    * You can't edit the name of the role after it's created because other entities might reference the role.

10. (Optional) For **Description**, enter a description for the role.
11. (Optional) To edit
    the use cases and permissions for the role, in the **Step 1: Select trusted
    entities** or **Step 2: Add permissions** sections, choose **Edit**.
12. (Optional) To help identify, organize, or search for the role, add tags as key-value pairs. For more
    information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
13. Review the role, and then choose **Create role**.

After you create a role for Amazon Personalize, you are ready to grant it [access to your Amazon S3 bucket](granting-personalize-s3-access.md "granting-personalize-s3-access.md") and [any AWS KMS keys](granting-personalize-key-access.md "granting-personalize-key-access.md").

### Additional service role permissions

After you create the role and grant it permissions to access your resources in Amazon Personalize, do the following:

1. Modify your Amazon Personalize service role's trust policy so it prevents the [confused deputy problem](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").
   For a trust relationship policy example, see [Cross-service confused deputy
   prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"). For information modifying a role's trust policy, see [Modifying a role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md").
2. If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
   permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").
