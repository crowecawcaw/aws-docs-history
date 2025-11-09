# Using a Cassandra client driver to access

Amazon Keyspaces programmatically

You can use many third-party, open-source Cassandra drivers to connect to Amazon Keyspaces.
Amazon Keyspaces is compatible with Cassandra drivers that support Apache Cassandra version
3.11.2. These are the drivers and latest versions that we’ve tested and recommend to use with Amazon Keyspaces:

- `Java v3.3`
- `Java v4.17`
- `Python Cassandra-driver 3.29.1`
- `Node.js cassandra driver -v 4.7.2`
- `GO using GOCQL v1.6`
- `.NET CassandraCSharpDriver -v 3.20.1`
  For more information about
  Cassandra drivers, see [Apache
  Cassandra Client drivers](http://cassandra.apache.org/doc/latest/getting_started/drivers.html "http://cassandra.apache.org/doc/latest/getting_started/drivers.html").

###### Note

To help you get started, you can view and download end-to-end code examples that establish
connections to Amazon Keyspaces with popular drivers. See [Amazon Keyspaces
examples](https://github.com/aws-samples/amazon-keyspaces-examples "https://github.com/aws-samples/amazon-keyspaces-examples") on GitHub.

The tutorials in this chapter include a simple CQL query to confirm that the connection
to Amazon Keyspaces has been successfully established. To learn how to work with keyspaces and tables
after you connect to an Amazon Keyspaces endpoint, see [CQL language reference for Amazon Keyspaces (for Apache Cassandra)](cql.md "cql.md"). For a step-by-step tutorial that shows how to
connect to Amazon Keyspaces from an Amazon VPC endpoint, see [Tutorial: Connect to Amazon Keyspaces using an interface VPC
endpoint](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md").

###### Topics

- [Using a Cassandra Java client driver to
  access Amazon Keyspaces programmatically](using_java_driver.md "using_java_driver.md")
- [Using a Cassandra Python client driver to
  access Amazon Keyspaces programmatically](using_python_driver.md "using_python_driver.md")
- [Using a Cassandra Node.js client driver to
  access Amazon Keyspaces programmatically](using_nodejs_driver.md "using_nodejs_driver.md")
- [Using a Cassandra .NET Core client driver to
  access Amazon Keyspaces programmatically](using_dotnetcore_driver.md "using_dotnetcore_driver.md")
- [Using a Cassandra Go client driver to
  access Amazon Keyspaces programmatically](using_go_driver.md "using_go_driver.md")
- [Using a Cassandra Perl client driver to
  access Amazon Keyspaces programmatically](using_perl_driver.md "using_perl_driver.md")
