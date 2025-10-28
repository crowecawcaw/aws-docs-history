# Use the Data Viewer in the Kinesis console

The Data Viewer in the Kinesis Management Console lets you view data records within the
specified shard of your data stream without having to develop a consumer application. To
use the Data Viewer, follow these steps:

1. Sign in to the AWS Management Console and open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Choose the active data stream whose records you want to view with the Data
   Viewer and then choose the **Data Viewer** tab.
3. In the **Data Viewer** tab for the selected active data
   stream, choose the shard whose records you want to view, chose the
   **Starting Position**, and then click **Get
   records**. You can set the starting position to one of the
   following values:
   - **At sequence number**: Show records from the
     position denoted by the sequence number specified in the sequence number
     field.
   - **After sequence number**: Show records right after
     the position denoted by the sequence number specified in the sequence
     number field.
   - **At timestamp**: Show records from the position
     denoted by the time stamp specified in the timestamp field.
   - **Trim horizon**: Show records at the last untrimmed
     record in the shard, which is the oldest data record in the
     shard.
   - **Latest**: Show records just after the most recent
     record in the shard, so that you always read the most recent data in the
     shard.

   The generated data records that match the specified shard ID and
   starting position are then displayed in a records table in the console.
   Maximum 50 records are displayed at a time. To view the next set of
   records, click the **Next** button.

4. Click any individual record to view that record payload in raw data or JSON
   format in a separate window.
   Note that when you click **Get records** or **Next**
   buttons in **Data Viewer**, this invokes the
   **GetRecords** API and this applies towards the
   **GetRecords** API limit of 5 transactions per second.
