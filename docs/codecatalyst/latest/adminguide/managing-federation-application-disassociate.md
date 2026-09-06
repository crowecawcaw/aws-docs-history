

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Disassociating an Identity Center application from a space
<a name="managing-federation-application-disassociate"></a>

You can disassociate the Identity Center application that is associated with your CodeCatalyst space. You can reassociate the Identity Center application later, or you can associate the Identity Center application to another space.

**Note**  
If you delete the identity store in IAM Identity Center, then the Identity Center application is automatically disassociated from the CodeCatalyst space.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose **IAM Identity Center**. On the **IAM Identity Center** page, under **Application Enabled Spaces**, view the spaces enabled for SSO and associated with your application.
**Tip**  
Make sure you are signed in to the AWS Management Console with the AWS account that will be the specified billing account for your space. 

1. Under **Application Enabled Spaces**, choose the space that you want to disassociate from your application. Choose **Disassociate space from application**.

1. Enter the confirmation for disassociating the application, and then choose **Disassociate**.
**Important**  
This action will remove all SSO users as members in the CodeCatalyst space.

   The Identity Center application will be available to be reassociated with this space or another space when needed.