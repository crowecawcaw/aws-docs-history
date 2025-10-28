# Receiving job results

###### Note

If you are using the Spark analytics engine, the **Results destination in
Amazon S3** can't be within the same S3 bucket as any data source.

The results of the job are located in the **Results settings defaults**
section of the **Analysis** tab in the AWS Clean Rooms console.

###### To receive job results

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you haven't yet done so).
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration that has **Your member abilities** status of
   **Receive results**.
4. To receive the job results directly from AWS Clean Rooms, on the **Analysis**
   tab, under **Analyses**, select **All jobs** from the
   dropdown, and then under the **Protected job ID** column, select the
   job.
5. On the **Job details** page, under **Results**, copy
   the Job ID.

Go back to the **Analysis** tab and expand the **Result
settings defaults**.

Under **Results destination**, select the link to view the results in
Amazon S3.

The Amazon S3 console opens in a separate tab.

In Amazon S3, paste the Job ID in the Search bar and press enter.

The folder containing the results appears. Select the folder to view the job
results.
