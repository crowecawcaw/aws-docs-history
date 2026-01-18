# Encrypting client connections with SSL/TLS to MySQL

DB instances on Amazon RDS

Secure Sockets Layer (SSL) is an industry-standard protocol for securing network
connections between client and server. After SSL version 3.0, the name was changed to
Transport Layer Security (TLS). Amazon RDS supports SSL/TLS encryption for MySQL DB instances.
Using SSL/TLS, you can encrypt a connection between your application client and your MySQL
DB instance. SSL/TLS support is available in all AWS Regions for MySQL.

With Amazon RDS, you can secure data in transit by encrypting client connections to MySQL DB
instances with SSL/TLS, requiring SSL/TLS for all connections to a MySQL DB instance, and
connecting from the MySQL command-line client with SSL/TLS (encrypted). The following
sections provide guidance on configuring and utilizing SSL/TLS encryption for MySQL DB
instances on Amazon RDS.

###### Topics

- [SSL/TLS support for MySQL DB instances on
  Amazon RDS](MySQL.Concepts.md "MySQL.Concepts.md")
- [Requiring SSL/TLS for
  specific user accounts to a MySQL DB instance on Amazon RDS](mysql-ssl-connections.md "mysql-ssl-connections.md")
- [Requiring SSL/TLS for all
  connections to a MySQL DB instance on Amazon RDS](mysql-ssl-connections.md "mysql-ssl-connections.md")
- [Connecting to your MySQL DB instance on
  Amazon RDS with SSL/TLS from the MySQL command-line client (encrypted)](USER_ConnectToInstanceSSL.md "USER_ConnectToInstanceSSL.md")
