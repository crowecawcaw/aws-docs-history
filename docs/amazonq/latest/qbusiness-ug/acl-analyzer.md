# Using ACL Analyzer in Amazon Q

The ACL (Access Control List) Analyzer is a troubleshooting tool that helps you verify and diagnose document access permissions in your
Amazon Q applications. When users report issues accessing specific documents, you can use this tool to quickly determine
whether a user has the necessary permissions and understand why access might be granted or denied. The tool provides detailed
information about user memberships, group associations, and the specific access control rules affecting document accessibility.
This makes it particularly useful for administrators who need to validate access controls or investigate permission-related issues.

## Prerequisites

- An AWS account with appropriate permissions for Amazon Q Business
- Access to the Amazon Q Business service in the AWS Console

## Getting Started with ACL Analyzer

###### To access Amazon Q Business

1. Sign in to the AWS Management Console.
2. Open the Amazon Q Business console.

###### To select or create an application:

1. In the navigation pane, choose **Applications**.
2. Do one of the following:
   - Choose an existing application from the list.
   - Create a new application.

###### Note

The application you select or create will be used as the context for checking document access permissions.

###### To configure user access

1. On the application details page, choose **Manage access and subscriptions**.
2. Choose the **Users** tab.
3. Choose **Add groups and users**.
4. Do one of the following:
5. 1. To add new users:

   Choose **Add new users**. 2. Enter the required user information. 3. Choose **Done**.

6. 1. To assign existing users:

   Choose **Assign existing users**. 2. Search for and select the desired user. 3. Choose **Assign**.

## Configuring Data Sources

###### To configure a new data source

1. On the application details page, choose **Add data source**.
2. Select your desired data source type from the available options.
3. Follow the configuration prompts specific to your selected data source type.
4. Configure the ACL settings for your data source. For detailed instructions, see:
   - [Setting up data sources](s3-connector.md "s3-connector.md")
   - [Managing user access](s3-user-management.md "s3-user-management.md")

###### To use an existing data source

1. On the application details page, choose **Data sources**.
2. From the list of data sources, select the data source you want to use.

## Using the ACL Analyzer Tool

###### To check document access permissions

1. On the data source details page, choose the **Troubleshooting tools** tab.
2. Locate the **ACL Analyzer** section.
3. Enter the following required information:
   - For **Document ID**, enter the unique identifier of the document you want to check.

   ###### Note

   The Document ID must conform to the pattern specified in the API documentation.
   - For **User ID**, enter the ID of the user whose
     access you want to verify, typically this is an email address.

4. Choose **Check access**.

### Understanding the Results

After running the ACL Analyzer check, you'll see results in three main sections:

#### Access Status

The system displays one of the following status messages:

- A success message indicating "**User has access**"
  when access is granted.
- An error message indicating "**User doesn't have
  access**" when access is denied.

#### User Membership Table

This table provides the following information:

- All user aliases associated with the checked user ID.
- User or group mapping information.
- Source configurations for each membership. Datasource level
  ACL applies only to the datasource and index level ACL applies to the
  entire index/application.

#### Access Control List (ACL) Table

This table shows:

- The allowlist of Users/Groups with access to the specified document,
  as defined by documentId.
