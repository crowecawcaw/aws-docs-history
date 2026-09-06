# Encrypting client connections with SSL/TLS to MariaDB DB instances on Amazon RDS

Secure Sockets Layer (SSL) is an industry-standard protocol for securing network
connections between client and server. After SSL version 3.0, the name was changed to
Transport Layer Security (TLS). Amazon RDS supports SSL/TLS encryption for MariaDB DB instances.
Using SSL/TLS, you can encrypt a connection between your application client and your MariaDB
DB instance. SSL/TLS support is available in all AWS Regions.

With Amazon RDS, you can secure data in transit by encrypting client connections to MariaDB DB
instances with SSL/TLS, requiring SSL/TLS for all connections to a MariaDB DB instance, and
connecting from the MySQL command-line client with SSL/TLS (encrypted). The following
sections provide guidance on configuring and using SSL/TLS encryption for MariaDB DB
instances on Amazon RDS.

###### Topics

- [SSL/TLS support for MariaDB DB instances on Amazon RDS](MariaDB.Concepts.SSLSupport.md "MariaDB.Concepts.SSLSupport.md")
- [Requiring SSL/TLS for specific user accounts to a MariaDB DB instance on Amazon RDS](MariaDB-ssl-connections.require-ssl-users.md "MariaDB-ssl-connections.require-ssl-users.md")
- [Requiring SSL/TLS for all connections to a MariaDB DB instance on Amazon RDS](mariadb-ssl-connections.require-ssl.md "mariadb-ssl-connections.require-ssl.md")
- [Connecting to your MariaDB DB instance on Amazon RDS with SSL/TLS from the MySQL command-line client (encrypted)](USER_ConnectToMariaDBInstanceSSL.CLI.md "USER_ConnectToMariaDBInstanceSSL.CLI.md")
