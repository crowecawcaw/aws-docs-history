Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Creating additional spaces that support AWS Builder ID

users

###### Note

This topic describes how to create spaces that support users who sign in to CodeCatalyst with a
AWS Builder ID. To create spaces that support users who are managed as part of SSO users and groups, see [Administering spaces that support identity
federation](managing-federation-space.md "managing-federation-space.md").

When you first sign up in Amazon CodeCatalyst, you are required to create a space. You
can choose to create additional spaces to meet your business needs.

###### Note

Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

To create additional spaces, you must be assigned the Space administrator role.

###### Note

When you create an additional space, you are not prompted to create a project. .

###### To create another space

1. In the AWS Management Console, make sure you are signed in with the same AWS account that you want
   to associate with your CodeCatalyst space.
2. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
3. Navigate to your space.

###### Tip

If you belong to more than one space, choose a space in the top navigation
bar. 4. Choose **Create space**. 5. On the **Create a space** page, in **Space
name**, enter a name for the space. You cannot change this later.

###### Note

Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces. 6. In **AWS Region**, choose the Region where you want to store your
space and project data. You cannot change this later. 7. In **AWS account ID**, enter the twelve-digit ID for the account you
want to connect to your space.

In **AWS account verification token**, copy the generated token ID.
The token is automatically copied for you, but you might want to store it while you approve
the AWS connection request. 8. Choose **Verify in AWS**. 9. The **Verify Amazon CodeCatalyst space** page opens in the AWS Management Console. This
is the **Amazon CodeCatalyst Spaces** page. You might need to sign in to access the
page.

In the AWS Management Console, make sure to choose the same AWS Region where you want to create
your space.

To directly access the page, sign in to the Amazon CodeCatalyst Spaces in the AWS Management Console at
https://console.aws.amazon.com/codecatalyst/home/.

The verification token is automatically entered in **Verification
token**. A success banner shows a message that the token is a valid token. 10. Choose **Verify space**.

An **Account verified** success message displays to show
that the account has been added to the space. 11. Remain on the **Verify Amazon CodeCatalyst space** page. Choose the
following link: **To enable the Standard tier or add IAM roles this space,
view space details.**

The **CodeCatalyst space details** page opens in the AWS Management Console. This is
the **Amazon CodeCatalyst Spaces** page. You might need to log in to access the
page. 12. Under **IAM roles available to CodeCatalyst**, choose **Add IAM
role**.

The **Add IAM roles available to CodeCatalyst** page displays. 13. Choose **Create CodeCatalyst development administrator role in IAM**. This
option creates a service role that contains the permissions policy and trust policy for the
development role.

The developer role is an AWS IAM role that enables your CodeCatalyst workflows to access
AWS resources such as Amazon S3, Lambda, and AWS CloudFormation. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName``
with a unique identifier appended. 14. Choose **Create development role**. 15. On the connection page, under **IAM roles available to
CodeCatalyst**, view the developer role in the list of IAM roles added to your
account. 16. Choose **Go to Amazon CodeCatalyst**. 17. On the creation page in CodeCatalyst, choose **Create space**.
