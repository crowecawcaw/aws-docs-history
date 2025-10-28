Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding IAM roles to account

connections

Part of creating your account connection includes adding the IAM role or roles you
want to use with projects in your CodeCatalyst space.

###### Note

To use IAM roles with an account connection, make sure that the trust policy is
updated to use the CodeCatalyst service principal.

###### Add IAM roles to an account connection (console)

1. In the AWS Management Console, make sure you are logged in with the same account that you want to
   manage.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your CodeCatalyst space. Choose **Settings**, and then choose
   **AWS accounts**.
4. Choose the **Amazon CodeCatalyst display name** of your account connection, and
   then choose **Manage roles from AWS Management Console**.

The **Add IAM role to Amazon CodeCatalyst space** page displays. 5. Do one of the following:

    * To create a service role that contains the permissions policy and trust policy for the
     developer role, choose **Create CodeCatalyst development administrator role in
     IAM**. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName`` with a unique identifier
     appended. For more information about the role and role policy, see [Understanding the CodeCatalystWorkflowDevelopmentRole-spaceName service role](ipa-iam-roles.md#ipa-iam-roles-service-role "ipa-iam-roles.md#ipa-iam-roles-service-role").


    Choose **Create development role**.
    * To add a role that you have already created in IAM, choose **Add an existing
     IAM role**. In **Select existing IAM role**, choose the
     role from the drop-down list.


    Choose **Add role**.

The page opens in the AWS Management Console. You might need to log in to access the page. 6. In the **Amazon CodeCatalyst spaces** page navigation pane, choose
**Spaces**.

To directly access the page, sign in to the Amazon CodeCatalyst Spaces in the AWS Management Console at
https://console.aws.amazon.com/codecatalyst/home/. 7. Choose the account added for your CodeCatalyst space. The connection page is shown. 8. On the connection page, under **IAM roles available to
CodeCatalyst**, view the list of IAM roles added to your account. Choose
**Associate IAM role to CodeCatalyst**. 9. On the **Associate an IAM role** pop-up, in **Role
ARN**, enter the Amazon Resource Name (ARN) of the IAM role you want to associate
with your CodeCatalyst space.

Under **Purpose**, choose a role purpose that describes how you want to
use the role in your account connection. Specify `RUNNER` for roles that you use to
run actions in workflows. Specify `SERVICE` for roles that you use to access
another service.

You can specify more than one purpose.

###### Note

Choosing a purpose for the role ARN is required. 10. Choose **Associate an IAM role**. Repeat these steps for additional
IAM roles.
