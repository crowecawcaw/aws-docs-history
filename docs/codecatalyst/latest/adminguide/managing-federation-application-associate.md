

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Associating a space to your Identity Center application
<a name="managing-federation-application-associate"></a>

You can associate a space with your CodeCatalyst Identity Center application. You must have already competed the prerequisites for setting up identity federation in AWS Organizations and IAM Identity Center.

**To associate a space to an Identity Center application**

1. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2\#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/).

1. Choose **IAM Identity Center**. On the **IAM Identity Center** page, under **Application Enabled Spaces**, view the spaces enabled for SSO and associated with your application.
**Tip**  
Make sure you are signed in to the AWS Management Console with the AWS account that will be the specified billing account for your space. 

1. Under **Application Enabled Spaces**, choose **Connect space**. On the **Choose or create a CodeCatalyst space** page, choose the space that you want to associate with your application, or you can choose to create a new space.