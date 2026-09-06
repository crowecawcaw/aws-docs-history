

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Using ACL Analyzer in Amazon Q
<a name="acl-analyzer"></a>

The ACL (Access Control List) Analyzer is a troubleshooting tool that helps you verify and diagnose document access permissions in your Amazon Q applications. When users report issues accessing specific documents, you can use this tool to quickly determine whether a user has the necessary permissions and understand why access might be granted or denied. The tool provides detailed information about user memberships, group associations, and the specific access control rules affecting document accessibility. This makes it particularly useful for administrators who need to validate access controls or investigate permission-related issues.

## Prerequisites
<a name="acl-analyzer-prerequisites"></a>
+ An AWS account with appropriate permissions for Amazon Q Business
+ Access to the Amazon Q Business service in the AWS Console

## Getting Started with ACL Analyzer
<a name="acl-analyzer-getting-started"></a>

**To access Amazon Q Business**

1. Sign in to the AWS Management Console.

1. Open the Amazon Q Business console.

**To select or create an application:**

1. In the navigation pane, choose **Applications**.

1. Do one of the following:
   + Choose an existing application from the list.
   + Create a new application.
**Note**  
The application you select or create will be used as the context for checking document access permissions.

**To configure user access**

1. On the application details page, choose **Manage access and subscriptions**.

1. Choose the **Users** tab.

1. Choose **Add groups and users**.

1. Do one of the following:

1. 

   1. To add new users:

      Choose **Add new users**.

   1. Enter the required user information.

   1. Choose **Done**.

1. 

   1.  To assign existing users: 

      Choose **Assign existing users**.

   1. Search for and select the desired user.

   1. Choose **Assign**.

## Configuring Data Sources
<a name="acl-analyzer-configure-data-sources"></a>

**To configure a new data source**

1. On the application details page, choose **Add data source**.

1. Select your desired data source type from the available options.

1. Follow the configuration prompts specific to your selected data source type.

1. Configure the ACL settings for your data source. For detailed instructions, see:
   + [Setting up data sources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-connector.html)
   + [Managing user access](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-user-management.html)

**To use an existing data source**

1. On the application details page, choose **Data sources**.

1. From the list of data sources, select the data source you want to use.

## Using the ACL Analyzer Tool
<a name="acl-analyzer-using-acl-analyzer"></a>

**To check document access permissions**

1. On the data source details page, choose the **Troubleshooting tools** tab.

1. Locate the **ACL Analyzer** section.

1. Enter the following required information:
   + For **Document ID**, enter the unique identifier of the document you want to check.
**Note**  
The Document ID must conform to the pattern specified in the API documentation.
   + For **User ID**, enter the ID of the user whose access you want to verify, typically this is an email address.

1. Choose **Check access**.

### Understanding the Results
<a name="acl-analyzer-understanding-results"></a>

After running the ACL Analyzer check, you'll see results in three main sections:

#### Access Status
<a name="acl-analyzer-access-status"></a>

The system displays one of the following status messages:
+ A success message indicating "**User has access**" when access is granted.
+ An error message indicating "**User doesn't have access**" when access is denied.

#### User Membership Table
<a name="acl-analyzer-user-membership"></a>

This table provides the following information:
+ All user aliases associated with the checked user ID.
+ User or group mapping information.
+ Source configurations for each membership. Datasource level ACL applies only to the datasource and index level ACL applies to the entire index/application.

#### Access Control List (ACL) Table
<a name="acl-analyzer-acl-table"></a>

This table shows:
+ The allowlist of Users/Groups with access to the specified document, as defined by documentId.