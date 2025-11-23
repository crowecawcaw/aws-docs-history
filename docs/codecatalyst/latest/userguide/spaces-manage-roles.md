Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring IAM roles for connected accounts

You create roles in AWS Identity and Access Management (IAM) for the account that you want to add to CodeCatalyst. If
you are adding a billing account, you do not need to create roles.

In your AWS account, you must have permissions to create roles for the AWS account you
want to add to your space. For more information about IAM roles and policies, including
IAM references and example policies, see [Identity and Access Management and Amazon CodeCatalyst](security-iam.md "security-iam.md"). For more information about the trust policy and service
principals used in CodeCatalyst, see [Understanding the CodeCatalyst trust model](trust-model.md "trust-model.md").

In CodeCatalyst, you must be signed in with the Space administrator role to complete the
steps to add accounts (and the roles, if applicable) to your space.

You can add roles to your account connections by using one of the following methods.

- To create a service role that contains the permissions policy and trust policy for the
  **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role, see [CodeCatalystWorkflowDevelopmentRole-spaceName role](#spaces-manage-roles-createrole "#spaces-manage-roles-createrole").
- For an example of creating a role and adding a policy to create a project from a
  blueprint, see [Creating an IAM role and using the CodeCatalyst
  trust policy](#ipa-connect-account-createrole "#ipa-connect-account-createrole").
- For a list of sample role policies to use when creating your IAM roles, see [Grant access to project AWS resources with IAM roles](ipa-iam-roles.md "ipa-iam-roles.md").
- For
  detailed steps to create roles for workflow actions, see the workflow tutorial for that
  action as
  follows:
  - [Tutorial: Upload artifacts to Amazon S3](build-deploy.md "build-deploy.md")
  - [Tutorial: Deploy a serverless application](deploy-tut-lambda.md "deploy-tut-lambda.md")
  - [Tutorial: Deploy an application to Amazon ECS](deploy-tut-ecs.md "deploy-tut-ecs.md")
  - [Tutorial: Lint code using a GitHub
    Action](integrations-github-action-tutorial.md "integrations-github-action-tutorial.md")

###### Topics

- [CodeCatalystWorkflowDevelopmentRole-spaceName role](#spaces-manage-roles-createrole "#spaces-manage-roles-createrole")
- [AWSRoleForCodeCatalystSupport role](#w2aac25c29c18c17 "#w2aac25c29c18c17")
- [Creating an IAM role and using the CodeCatalyst
  trust policy](#ipa-connect-account-createrole "#ipa-connect-account-createrole")

## **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role

You create the developer role as a 1-click role in IAM. You must have the
**Space administrator** or **Power user** role in the
space where you want to add the account. You must also have administrative permissions
for the AWS account you want to add.

Before you start the procedure below, you must log in to the AWS Management Console with the same
account that you want to add to your CodeCatalyst space. Otherwise, the console will return
an unknown account error.

###### To create and add the CodeCatalyst **CodeCatalystWorkflowDevelopmentRole-`spaceName`**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   logged in with the same AWS account for your space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
4. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
5. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst spaces** page. You might need to log in
to access the page. 6. Choose **Create CodeCatalyst development administrator role in IAM**. This
option creates a service role that contains the permissions policy and trust policy for the
development role. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName``. For more information about the
role and role policy, see [Understanding the CodeCatalystWorkflowDevelopmentRole-spaceName service role](ipa-iam-roles.md#ipa-iam-roles-service-role "ipa-iam-roles.md#ipa-iam-roles-service-role").

###### Note

This role is only recommended for use with developer accounts and uses the
`AdministratorAccess` AWS managed policy, giving it full access to create new
policies and resources in this AWS account. 7. Choose **Create development role**. 8. On the connections page, under **IAM roles available to CodeCatalyst**, view
the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role in the list of IAM roles added to your account. 9. To return to your space, choose **Go to Amazon CodeCatalyst**.

## **AWSRoleForCodeCatalystSupport** role

You create the support role as a 1-click role in IAM. You must have the
**Space administrator** or **Power user** role in the
space where you want to add the account. You must also have administrative permissions
for the AWS account you want to add.

Before you start the procedure below, you must log in to the AWS Management Console with the same
account that you want to add to your CodeCatalyst space. Otherwise, the console will return
an unknown account error.

###### To create and add the CodeCatalyst **AWSRoleForCodeCatalystSupport**

1. Before you start in the CodeCatalyst console, open the AWS Management Console, and then make sure you are
   logged in with the same AWS account for your space.
2. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
3. Choose the link for the AWS account where you want to create the role. The
   **AWS account details** page displays.
4. Choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page opens in the
AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need to sign in
to access the page. 5. Under **CodeCatalyst space details**, choose **Add CodeCatalyst Support
role**. This option creates a service role that contains the permissions policy and
trust policy for the preview development role. The role will have a name **AWSRoleForCodeCatalystSupport**
with a unique identifier appended. For more information about the role and role policy, see
[Understanding the AWSRoleForCodeCatalystSupport service
role](ipa-iam-roles.md#ipa-iam-roles-support-role "ipa-iam-roles.md#ipa-iam-roles-support-role"). 6. On the **Add role for CodeCatalyst Support** page, leave the default selected,
and then choose **Create role**. 7. Under **IAM roles available to CodeCatalyst**, view the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role
in the list of IAM roles added to your account. 8. To return to your space, choose **Go to Amazon CodeCatalyst**.

## Creating an IAM role and using the CodeCatalyst

trust policy

IAM roles to be used in CodeCatalyst with AWS account connections must be
configured to use the trust policy provided here. Use these steps to create an IAM role
and attach a policy that allows you to create projects from blueprints in CodeCatalyst.

As an alternative, you can create a service role that contains the permissions policy
and trust policy for the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role. For more information, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**, and then choose **Create
   role**.
3. Choose **Custom trust policy**.
4. Under the **Custom trust policy** form, paste the following trust
   policy.

```

"Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
             "Principal": {
                "Service": [
                    "codecatalyst-runner.amazonaws.com",
                    "codecatalyst.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:codecatalyst:::space/spaceId/project/*"
                }
            }
        }
    ]

```

5. Choose **Next**.
6. Under **Add permissions**, search for and select a custom policy
   that you have already created in IAM.
7. Choose **Next**.
8. For **Role name**, enter a name for the role, for example:
   `codecatalyst-project-role`
9. Choose **Create role**.
10. Copy the role Amazon Resource Name (ARN). You'll need to provide this information
    when adding the role to your account connection or environment.
