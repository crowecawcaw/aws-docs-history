

# Receiving query results
<a name="receive-results"></a>

**Note**  
The **Results destination in Amazon S3** can't be within the same S3 bucket as any data source.

The results of the query are located in the **Results settings defaults** section of the **Analysis** tab in the AWS Clean Rooms console.

**To receive query results**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Receive results**.

1. To receive the query results directly from AWS Clean Rooms, on the **Analysis** tab, under **Analyses**, select **All queries** from the dropdown, and then under the **Protected query ID** column, select the query.

1. On the **Query details** page, under **Results**, do one of the following:


<table>
<thead>
  <tr><th>If you want to…</th><th>Then choose…</th></tr>
</thead>
<tbody>
  <tr><td>Copy the results.</td><td><b>Copy</b></td></tr>
  <tr><td>Download the results.</td><td><b>Download</b> By default, the downloaded ﬁle’s name is the corresponding <code>Query id</code> that was displayed when the query was run in AWS Clean Rooms. </td></tr>
  <tr><td>View the results in Amazon S3.</td><td><b>View in Amazon S3</b>The Amazon S3 console opens in a separate tab.</td></tr>
</tbody>
</table>


1. If you're using encrypted data, you can now [decrypt](glossary.md#glossary-decryption) the data tables.

   For more information, see [Decrypting data tables with the C3R encryption client](decrypt-data.md).