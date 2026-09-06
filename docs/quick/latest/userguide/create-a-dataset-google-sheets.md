

# Creating a dataset using a Google Sheets data source
<a name="create-a-dataset-google-sheets"></a>

Google Sheets is a web-based spreadsheet application that enables users to create, edit, and collaborate on data in real time. With its comprehensive set of functions and formulas, it serves as a powerful data source for business intelligence and analytics. Users can organize, analyze, and share insights efficiently, while its seamless collaboration features make it an ideal platform for teams working on data-driven projects.

## Admin configuration in Amazon Quick
<a name="google-sheets-admin-config"></a>

Amazon Quick administrators need to perform a one-time setup to enable Google Sheets as a data source. For detailed instructions and important considerations, see [the blog](https://aws.amazon.com/blogs/business-intelligence/transform-your-google-sheets-data-into-powerful-analytics-with-amazon-quicksight/).

## Creating a dataset using a Google Sheets data source
<a name="google-sheets-create-dataset"></a>

Use the following procedure to create a dataset using a Google Sheets data source.

**To create a dataset using a Google Sheets data source**

1. From the Quick start page, choose **Datasets**.

1. On the **Datasets** page, choose **New Dataset**.

1. Choose **Google Sheets**.

1. Enter a name for the data source, and then choose **Connect**.

1. When redirected to Google's sign-in page, do the following:

   1. Enter your Google account credentials, and then choose **Next**.

   1. Review the permissions to authorize your AWS account to connect with Google Sheets, and then choose **Continue**.

1. In the **Choose your table** menu, locate your data. The menu displays all folders, subfolders, sheets, and tabs from your Google account. To display the tabs, select a sheet from the displayed list.

1. Select the tab you want to work with.

1. Choose **Edit/Preview data** to navigate to the Data preparation page. Choose **Add data** to include any additional tabs.

1. Configure the join, and then select **Publish & visualize** to analyze your Google Sheets data with Quick Sight.

**Note**  
This connector supports only SPICE functionality.
If your OAuth token expires (visible in the ingestion error report or when creating a new dataset), reauthorize by choosing **Edit** on the data source and updating it.