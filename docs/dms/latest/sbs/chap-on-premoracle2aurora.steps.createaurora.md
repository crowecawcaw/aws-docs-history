

# Step 5: Create Your Aurora MySQL Target Endpoint
<a name="chap-on-premoracle2aurora.steps.createaurora"></a>

Next, you can provide information for the target Amazon Aurora MySQL database by specifying the target endpoint settings.

To specify a target database endpoint, do the following:

1. In the AWS DMS console, choose **Endpoints** on the navigation pane.

1. Choose **Create endpoint**. The **Create endpoint** appears, as shown following.

1. Specify your connection information for the target Aurora MySQL database. The following table describes the target settings.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint type</b> </td><td>Choose <b>Target endpoint</b>.</td></tr>
  <tr><td> <b>Endpoint identifier</b> </td><td>Enter an identifier for your Aurora MySQL endpoint. The identifier for your endpoint must be unique within an AWS Region.</td></tr>
  <tr><td> <b>Target engine</b> </td><td>Choose <b>Amazon Aurora MySQL</b>.</td></tr>
  <tr><td> <b>Access to endpoint database</b> </td><td>Choose <b>Provide access information manually</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Enter the writer endpoint for your Aurora MySQL instance. The writer endpoint is the primary instance.</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter the port assigned to the instance.</td></tr>
  <tr><td> <b>Secure Socket Layer (SSL) mode</b> </td><td>Choose an SSL mode if you want to enable connection encryption for this endpoint. Depending on the mode you select, you might need to provide certificate and server certificate information.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter the user name for the user you are using for the migration. We recommend that you create a user specific to your migration.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the user name preceding.</td></tr>
</tbody>
</table>


1. Define additional specific settings for your endpoints using wizard or editor in **Endpoint settings**.

1. Choose the encryption key to use to encrypt replication storage and connection information in **KMS key**. If you choose **(Default) aws/dms**, the default AWS Key Management Service (AWS KMS) key associated with your user and region is used.

1. Add tags to organize your DMS resources in **Tags**. You can use tags to manage your IAM roles and policies, and track your DMS costs.

Prior to saving your endpoint, you have an opportunity to test it in **Test endpoint connection (optional)**. To do so you’ll need to choose a VPC and replication instance from which to perform the test.