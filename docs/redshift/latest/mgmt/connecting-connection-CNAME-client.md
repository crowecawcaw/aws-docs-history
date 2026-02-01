Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to your Amazon Redshift provisioned

cluster or Amazon Redshift Serverless workgroup

To connect with a custom domain name, the following IAM permissions are required for
a provisioned cluster: `redshift:DescribeCustomDomainAssociations`. For
Amazon Redshift Serverless, you don't have to add permissions.

As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

After you complete the steps to create your CNAME and assign it to your cluster or
workgroup in the console, you can provide the custom URL in the connection properties of
your SQL client. Note that there can be a delay from DNS propagation immediately
following the creation of a CNAME record.

1. Open a SQL client. For example, you can use SQL/Workbench J. Open the
   properties for a connection, and add the custom domain name for the connection
   string. For example,
   `jdbc:redshift://mycluster.example.com:5439/dev?sslmode=verify-full`.
   In this example, `dev` specifies the default database.
2. Add the **Username** and **Password** for
   your database user.
3. Test the connection. Your ability to query database resources such as specific
   tables can vary, based on the permissions granted to the database user or
   granted to the Amazon Redshift database roles assigned.

Note that you might have to set your cluster or workgroup to be publicly
accessible to connect to it if it's in a VPC. You can change this setting in the
network properties.

###### Note

Connections to a custom domain name are supported with JDBC, ODBC, and Python
drivers.
