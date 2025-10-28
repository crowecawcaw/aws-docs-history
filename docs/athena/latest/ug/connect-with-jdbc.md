# Connect to Amazon Athena with JDBC

Amazon Athena offers two JDBC drivers, versions 2.x and 3.x. The Athena JDBC 3.x driver is the
new generation driver offering better performance and compatibility. The JDBC 3.x driver
supports reading query results directly from Amazon S3, which improves the performance of
applications that consume large query results. The new driver also has fewer third-party
dependencies, which makes integration with BI tools and custom applications easier. In most
cases, you can use the new driver with no or minimal changes to existing
configuration.

- To download the JDBC 3.x driver, see [Athena JDBC 3.x driver](jdbc-v3-driver.md "jdbc-v3-driver.md").
- To download the JDBC 2.x driver, see [Athena JDBC 2.x driver](jdbc-v2.md "jdbc-v2.md").

###### Topics

- [Athena JDBC 3.x driver](jdbc-v3-driver.md "jdbc-v3-driver.md")
- [Athena JDBC 2.x driver](jdbc-v2.md "jdbc-v2.md")
