We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Creating an Amazon ML Datasource from Data in

Amazon Redshift

If you have data stored in Amazon Redshift, you can use the **Create Datasource**
wizard in the Amazon Machine Learning (Amazon ML) console to create a datasource object. When you create a
datasource from Amazon Redshift data, you specify the cluster that contains your data and the SQL query
to retrieve your data. Amazon ML executes the query by invoking the Amazon Redshift `Unload`
command on the cluster. Amazon ML stores the results in the Amazon Simple Storage Service (Amazon S3) location of your choice,
and then uses the data stored in Amazon S3 to create the datasource. The datasource, Amazon Redshift cluster,
and S3 bucket must all be in the same region.

###### Note

Amazon ML doesn't support creating datasources from Amazon Redshift clusters in private VPCs. The
cluster must have a public IP address.

###### Topics

- [Required Parameters for the Create Datasource
  Wizard](redshift-parameters.md "redshift-parameters.md")
- [Creating a Datasource with Amazon Redshift
  Data (Console)](create-datasource-from-redshift-procedure.md "create-datasource-from-redshift-procedure.md")
- [Troubleshooting Amazon Redshift Issues](troubleshooting.md "troubleshooting.md")
