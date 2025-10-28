Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to an Amazon Redshift data

warehouse using SQL client tools

You can connect to Amazon Redshift data warehouses from SQL client tools over Java Database
Connectivity (JDBC), Python, and Open Database Connectivity (ODBC) connections. Amazon Redshift
doesn't provide or install any SQL client tools or libraries. To use these tools or
libraries to work with data in your data warehouses, install them on your client computer or
Amazon EC2 instance. You can use most SQL client tools that support JDBC, Python, or ODBC
drivers.

Use the list of sections at the end of this topic to help you walk through the process of
configuring your client computer or Amazon EC2 instance to use a JDBC, Python, or ODBC
connection. The topics also discuss related security options for the client connection to
the server. Additionally, find information about setting up and connecting from SQL client
tools, such as [Amazon Redshift RSQL](rsql-query-tool.md "rsql-query-tool.md"). You can try these tools if
you don't yet have a business intelligence tool to use. You can also use this section
to learn about connecting to your data . Finally, if you encounter issues when attempting to
connect to your data warehouse, you can review the troubleshooting information to identify
solutions.

## Recommendations for

connecting with client tools

If you connect to your Redshift cluster using an IP address, it can result in
additional downtime when there is an outage or a connection loss and the cluster is
brought online in a new Availability Zone (AZ). However, if you still want your
application to connect to Redshift using an IP address, use the private IP address
attached to the cluster's virtual-private-cloud (VPC) endpoint. You can find this in the
cluster details in **Network and security**, under the
**Properties** tab.

###### Note

If your application uses the IP address of the leader node to access the Redshift
cluster, the recommended best practice is to change it to use the cluster endpoint
URL. For more information, see [Configuring connections in
Amazon Redshift](configuring-connections.md "configuring-connections.md").

###### Topics

- [Configuring connections in Amazon Redshift](configuring-connections.md "configuring-connections.md")
- [Configuring security options for
  connections](connecting-ssl-support.md "connecting-ssl-support.md")
- [Connecting from client tools and
  code](connecting-via-client-tools.md "connecting-via-client-tools.md")
- [Using an authentication
  profile to connect to Amazon Redshift](connecting-with-authentication-profiles.md "connecting-with-authentication-profiles.md")
- [Troubleshooting connection issues in
  Amazon Redshift](troubleshooting-connections.md "troubleshooting-connections.md")
