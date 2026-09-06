

# Step 1: Create a database
<a name="step-1-create-a-database"></a>

You first need to create a database in Athena.

**To create an Athena database**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. If this is your first time to visit the Athena console in your current AWS Region, choose **Explore the query editor** to open the query editor. Otherwise, Athena opens in the query editor.

1. Choose **Edit Settings** to set up a query result location in Amazon S3.  
![Choose Edit settings.](http://docs.aws.amazon.com/athena/latest/ug/images/getting-started-choose-view-settings.png)

1. For **Manage settings**, do one of the following:
   + In the **Location of query result** box, enter the path to the bucket that you created in Amazon S3 for your query results. Prefix the path with `s3://`.
   + Choose **Browse S3**, choose the Amazon S3 bucket that you created for your current Region, and then choose **Choose**.  
![Specify a location in Amazon S3 to receive query results from Athena.](http://docs.aws.amazon.com/athena/latest/ug/images/getting-started-setting-results-location.png)

1. Choose **Save**.

1. Choose **Editor** to switch to the query editor.  
![Choose Editor.](http://docs.aws.amazon.com/athena/latest/ug/images/getting-started-choose-editor.png)

1. On the right of the navigation pane, you can use the Athena query editor to enter and run queries and statements.

1. To create a database named `mydatabase`, enter the following CREATE DATABASE statement.

   ```
   CREATE DATABASE mydatabase
   ```

1. Choose **Run** or press **Ctrl\+ENTER**.

1. From the **Database** list on the left, choose `mydatabase` to make it your current database.