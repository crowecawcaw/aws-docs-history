

# Step 4: Create Your Oracle Source Endpoint
<a name="chap-on-premoracle2aurora.steps.createoracle"></a>

While your replication instance is being created, you can specify the Oracle source endpoint using the [AWS Management Console](https://console.aws.amazon.com/). However, you can only test connectivity after the replication instance has been created, because the replication instance is used to test the connection.

To specify source or target database endpoints, do the following:

1. In the AWS DMS console, choose **Endpoints** on the navigation pane.

1. Choose **Create endpoint**. The **Create database endpoint page** appears, as shown following.  
![Create source and target DB endpoints](https://docs.aws.amazon.com/dms/latest/sbs/images/datarep-gs-wizard3.png)

1. Specify your connection information for the source Oracle database. The following table describes the source settings.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint type</b> </td><td>Choose <b>Source</b>.</td></tr>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter an identifier for your Oracle endpoint. The identifier for your endpoint must be unique within an AWS Region.</td></tr>
  <tr><td> <b>Source Engine</b> </td><td>Choose <b>oracle</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Enter an IP address that AWS DMS can use to connect to your database from the replication server.</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter the port which your database is listening for connections (the Oracle default is 1521).</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose a Secure Sockets Layer (SSL) mode if you want to enable connection encryption for this endpoint. Depending on the mode you select, you might need to provide certificate and server certificate information.</td></tr>
  <tr><td> <b>Username</b> </td><td>Enter the user name. We recommend that you create a user specific to your migration.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the user name preceding.</td></tr>
</tbody>
</table>


1. Choose the **Advanced** tab to set values for extra connection strings and the encryption key.


<table>
<thead>
  <tr><th>For This Option</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Extra connection attributes</b> </td><td>Here you can add values for extra attributes that control the behavior of your endpoint. A few of the most relevant attributes are listed here. For the full list, see the documentation. Separate multiple entries from each other by using a semi-colon (;).<br />* <b>addSupplementalLogging:</b> AWS DMS will automatically add supplemental logging if you enable this option (addSupplementalLogging=Y).<br />* <b>useLogminerReader:</b> By default AWS DMS uses Oracle LogMiner to capture change data from the logs. AWS DMS can also parse the logs using its proprietary technology. If you use Oracle 12c and need to capture changes to tables that include LOBS, set this to No (useLogminerReader=N).<br />* <b>numberDataTypeScale:</b> Oracle supports a NUMBER data type that has no precision or scale. By default, NUMBER is converted to a number with a precision of 38 and scale of 10, number(38,10). Valid values are 0—​38 or -1 for FLOAT.<br />* <b>archivedLogDestId:</b> This option specifies the destination of the archived redo logs. The value should be the same as the DEST_ID number in the $archived_log table. When working with multiple log destinations (DEST_ID), we recommend that you specify a location identifier for archived redo logs. Doing so improves performance by ensuring that the correct logs are accessed from the outset. The default value for this option is 0.</td></tr>
  <tr><td> <b> KMS key </b> </td><td>Choose the encryption key to use to encrypt replication storage and connection information. If you choose <b>(Default) aws/dms</b>, the default AWS KMS key associated with your user and region is used.</td></tr>
</tbody>
</table>


Before you save your endpoint, you can test it. To do so, select a VPC and replication instance from which to perform the test. As part of the test AWS DMS refreshes the list of schemas associated with the endpoint. (The schemas are presented as source options when creating a task using this source endpoint.)