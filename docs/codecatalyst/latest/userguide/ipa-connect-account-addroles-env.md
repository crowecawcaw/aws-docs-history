Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding the account connection and

IAM roles to your deploy environment

To access AWS resources, such as Amazon ECS or AWS Lambda resources for deployments,
CodeCatalyst build and deploy actions require IAM roles with permissions to access those
resources. With the **Space administrator** or
**Power user** role, you can connect your CodeCatalyst account to
the AWS account where your resources are created. You then add the IAM
role to your account connection. For deploy actions, you must then add the IAM role to
a
CodeCatalyst environment.

You must add the IAM roles that you want to use with deployment environments in your
projects. Adding the roles to the account connection does not add the roles and the
connection to the project deploy environments. To add your account connection and IAM
roles to your deploy environment, make sure that the account connection and roles are
created as detailed in [Step 4: Add IAM roles to your
connection](ipa-connect-account-create.md#ipa-connect-account-linkedroles "ipa-connect-account-create.md#ipa-connect-account-linkedroles").

Then, use the **Environments** page in the CodeCatalyst console
to add your account connection and IAM role to a deploy environment in a
project.

###### Note

You only add an IAM role to an environment if the IAM role is used for a
CodeCatalyst action that requires an IAM role. All workﬂow actions that require IAM
roles, including build actions, must use a CodeCatalyst environment.

To add your account connection and IAM roles to your deploy environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate
   to the project with the deployment environment where you want to add the account
   connection and IAM roles.
3. Expand **CI/CD**, and then choose
   **Environments**.
4. Choose your environment, and then the additional tabs display.
5. Choose the **AWS account connections** tab. Under
   **Connection name**, the accounts that have been added to
   the environment, if any, are listed.
6. Choose **Associate AWS account**. The **Associate
   AWS account with <environment_name>** page displays.
7. Under **Connection**, choose the name of the account
   connection with the IAM roles that you want to add. Choose
   **Associate**.
