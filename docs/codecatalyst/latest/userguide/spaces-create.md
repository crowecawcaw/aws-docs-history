

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating a space
<a name="spaces-create"></a>

When you first sign up in Amazon CodeCatalyst with your AWS Builder ID, you are required to create a space. For more information, see [Set up and sign in to CodeCatalyst](setting-up-topnode.md). You can choose to create additional spaces to meet your business needs. 

**Note**  
Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

The information in this guide is provided for creating spaces in CodeCatalyst that support AWS Builder ID users. The steps to set up and administer a space that supports identity federation are provided in the *CodeCatalyst Administrator Guide*. To work with spaces that are set up for identity federation, see [Setup and administration for CodeCatalyst spaces](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/what-is.html) in the *Amazon CodeCatalyst Administrator Guide*.

To create additional spaces that support AWS Builder ID users, you must be assigned the Space administrator role.

**Note**  
When you create an additional space, you are not prompted to create a project. To learn how to create projects in a space, see [Creating a project](projects-create.md). <a name="space-create-additional"></a>

**To create another space**

1. In the AWS Management Console, make sure you are signed in with the same AWS account that you want to associate with your CodeCatalyst space.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your space.
**Tip**  
If you belong to more than one space, choose a space in the top navigation bar.

1. Choose **Create space**.

1. On the **Create a space** page, in **Space name**, enter a name for the space. You cannot change this later.
**Note**  
Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

1. In **AWS Region**, choose the Region where you want to store your space and project data. You cannot change this later.

1. In **AWS account ID**, enter the twelve-digit ID for the account you want to connect to your space.

   In **AWS account verification token**, copy the generated token ID. The token is automatically copied for you, but you might want to store it while you approve the AWS connection request.

1. Choose **Verify in AWS**.

1. The **Verify Amazon CodeCatalyst space** page opens in the AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need to sign in to access the page.

   In the AWS Management Console, make sure to choose the same AWS Region where you want to create your space.

   To directly access the page, sign in to the Amazon CodeCatalyst Spaces in the AWS Management Console at https://console.aws.amazon.com/codecatalyst/home/.

   The verification token is automatically entered in **Verification token**. A success banner shows a message that the token is a valid token.

1. Choose **Verify space**.

   An **Account verified** success message displays to show that the account has been added to the space.

1. Remain on the **Verify Amazon CodeCatalyst space** page. Choose the following link: **To add IAM roles for this space, view space details.**

   The **CodeCatalyst space details** page opens in the AWS Management Console. This is the **Amazon CodeCatalyst Spaces** page. You might need to log in to access the page.

1. Under **IAM roles available to CodeCatalyst**, choose **Add IAM role**. 

   The **Add IAM roles available to CodeCatalyst** page displays.

1. Choose **Create CodeCatalyst development administrator role in IAM**. This option creates a service role that contains the permissions policy and trust policy for the development role. 

   The developer role is an AWS IAM role that enables your CodeCatalyst workflows to access AWS resources such as Amazon S3, Lambda, and CloudFormation. The role will have a name `CodeCatalystWorkflowDevelopmentRole-{{spaceName}}` with a unique identifier appended. For more information about the role and role policy, see [Understanding the **CodeCatalystWorkflowDevelopmentRole-{{spaceName}}** service role](ipa-iam-roles.md#ipa-iam-roles-service-role).

1. Choose **Create development role**.

1. On the connection page, under **IAM roles available to CodeCatalyst**, view the developer role in the list of IAM roles added to your account.

1. Choose **Go to Amazon CodeCatalyst**.

1. On the creation page in CodeCatalyst, choose **Create space**.