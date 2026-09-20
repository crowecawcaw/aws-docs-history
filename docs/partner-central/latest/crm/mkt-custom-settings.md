

# Entering custom settings
<a name="mkt-custom-settings"></a>

After you enter the system configuration settings, you enter settings for the Amazon S3 bucket used to upload and store custom EULAs. 

1. In Salesforce, on the [Guided setup tab](use-guided-setup.md), return to the **Custom Settings** page, locate **S3 Bucket Settings**, and choose **Manage**. 

1. Choose **New**.

1. Enter values for the following settings.


<table>
<thead>
  <tr><th> <b>Setting name</b> </th><th> <b>Default value</b> </th><th> <b>Description</b> </th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>N/A </td><td> <b>Provide unique account prefix</b> The name of the Amazon S3 setting. This name should be same as the AWS account name in the AWS accounts table. </td></tr>
  <tr><td> <b>Amazon S3 Bucket Name</b> </td><td>N/A </td><td>The name of the Amazon S3 bucket that stores the custom EULA. </td></tr>
  <tr><td> <b>Amazon S3 Bucket Prefix</b> </td><td>N/A </td><td>Prefix of the Amazon S3 bucket that stores the custom EULA. </td></tr>
</tbody>
</table>


1. Choose **Save**. 

1. For each configured AWS Seller account, repeat steps 2-4 to add the Amazon S3 settings.