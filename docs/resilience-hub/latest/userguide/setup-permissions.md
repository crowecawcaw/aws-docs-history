# Setup permissions

AWS Resilience Hub allows you to configure the necessary permissions for **Primary
account** and **Secondary account** to discover and assess the
resources. However, you must run the procedure separately to configure permissions for each
account.

###### To configure IAM roles and IAM permissions

1. To select an existing IAM role that will be used for accessing resources in the current
   account, select an IAM role from the **Select an IAM role** dropdown
   list.

###### Note

For a cross account setup, if you do not specify the Amazon Resource Names (ARNs) of the
IAM role in the **Enter an IAM role ARN** box, AWS Resilience Hub will use the
IAM role you have selected from the **Select an IAM role** dropdown list
for all the accounts.

If there are no existing IAM roles attached to your account, you can create an IAM
role by using one of the following options:

    * **AWS IAM console** – If you choose this option, you must
     complete the procedure in **To create your AWS Resilience Hub role in the IAM
     console**.
    * **AWS CLI** – If you choose this option, you must complete
     all the steps in **AWS CLI**.
    * **CloudFormation template** – If you choose this option, depending
     on which account type (**Primary account** or **Secondary
     account**), you must create the roles using the appropriate AWS CloudFormation
     template.

2. Choose the right arrow to expand **Add IAM role(s) from a cross account -
   Optional** section.
3. To select IAM roles from a cross account, enter the ARNs of the IAM role in
   **Enter an IAM role ARN** box. Ensure that the ARNs of the IAM roles you
   are entering does not belong to the current account.
4. If you want to use current IAM user to discover your application resources, choose the
   right arrow to expand **Use the current IAM user permissions** section and
   select **I understand that I must manually configure permissions to enable the
   required functionality within AWS Resilience Hub**.

If you select this option, some of the AWS Resilience Hub features (such as drift notification)
may not function as expected and the inputs you have provided for creating a new application will be ignored.

## Next

[Configure the application configuration
parameters](app-config-param.md "app-config-param.md")
