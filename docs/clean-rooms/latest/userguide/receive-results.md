# Receiving query results

###### Note

If you are using the Spark analytics engine, the **Results destination in
Amazon S3** can't be within the same S3 bucket as any data source.

The results of the query are located in the **Results settings defaults**
section of the **Analysis** tab in the AWS Clean Rooms console.

###### To receive query results

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you haven't yet done so).
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration that has **Your member abilities** status of
   **Receive results**.
4. To receive the query results directly from AWS Clean Rooms, on the **Analysis**
   tab, under **Analyses**, select **All queries** from the
   dropdown, and then under the **Protected query ID** column, select the
   query.
5. On the **Query details** page, under **Results**, do
   one of the following:

| If you want to…                | Then choose…                                                                                                                                        |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Copy the results.              | **Copy**                                                                                                                                            |
| Download the results.          | **Download**NoteBy default, the downloaded ﬁle’s name is the corresponding `Query id` that was displayed when the query was run in AWS Clean Rooms. |
| View the results in Amazon S3. | **View in Amazon S3**The Amazon S3 console opens in a separate tab.                                                                                 | 6. If you're using encrypted data, you can now [decrypt](glossary.md#glossary-decryption "glossary.md#glossary-decryption") the data tables. For more information, see [Decrypting data tables with the C3R encryption client](decrypt-data.md "decrypt-data.md"). |
