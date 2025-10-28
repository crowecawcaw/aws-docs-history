# Create a query output

location

If you do not already have a query output location set up in Amazon S3, perform the
following prerequisite steps to do so.

###### To create a query output location

1. Using the same AWS Region and account that you are using for Athena, follow
   the steps (for example, by using the Amazon S3 console) to [create a bucket in Amazon S3](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") to
   hold your Athena query results. You will configure this bucket to be your query
   output location.
2. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
3. If this is your first time to visit the Athena console in this AWS Region,
   choose **Explore the query editor** to open the query editor.
   Otherwise, Athena opens in the query editor.
4. Choose **Edit Settings** to set up a query result location in
   Amazon S3.

![Choose Edit settings.](images/getting-started-choose-view-settings.png) 5. For **Manage settings**, do one of the following:

    * In the **Location of query result** box, enter the
     path to the bucket that you created in Amazon S3 for your query results.
     Prefix the path with `s3://`.
    * Choose **Browse S3**, choose the Amazon S3 bucket that you
     created for your current Region, and then choose
     **Choose**.

![Specify a location in Amazon S3 to receive query results from Athena.](images/getting-started-setting-results-location.png) 6. Choose **Save**. 7. Choose **Editor** to switch to the query editor.

![Choose Editor.](images/getting-started-choose-editor.png)
