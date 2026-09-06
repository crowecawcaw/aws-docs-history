

# Get started with uploading and querying data in Amazon SageMaker Unified Studio
<a name="upload-query"></a>

You can use the query editor to perform analysis using SQL. The query editor tool provides a place to write and run queries, view results, and share your work with your team.

## Prerequisites
<a name="start-querying-prerequisites"></a>

Before you get started with the query editor, access Amazon SageMaker and create a project with the **SQL analytics** or **All Capabilities** project profile. For more information, see [Setting up Amazon SageMaker](setting-up.md).

Download the file [sales-data.zip](samples/sales-data.zip).

## Query sample data using Amazon Athena in Amazon SageMaker
<a name="start-querying-upload-data"></a>

1. Navigate to Amazon SageMaker Unified Studio using the URL from the Amazon SageMaker management console and log in using your SSO or AWS credentials.

1. Use the top center menu of the Amazon SageMaker home page to navigate to the project you want to use to query data.

1. Expand the **Build** menu in the top navigation bar, then choose **Query editor**.

1. In the left data explorer navigation, choose the three-dot action menu next to a database and choose **Create table**.

1. Upload the sales-data.csv file from the prerequisites section.

1. Choose **Next**.

1. Choose **Create table**.

1. Refresh the Data explorer navigation pane and navigate to the sales-data table in the explorer.

1. Choose the three-dot action menu next to the table, then choose **Preview data**. A SQL command to select the first 10 rows from the table runs, and the results are then displayed in the query editor window.  
![Three-dot action menu under the sales-data dropdown.](http://docs.aws.amazon.com/next-generation-sagemaker/latest/userguide/images/screenshot-menu.png)