# SSL/TLS support for MariaDB DB instances

on Amazon RDS

Amazon RDS creates an SSL/TLS certificate and installs the certificate on the DB instance
when Amazon RDS provisions the instance. These certificates are signed by a certificate
authority. The SSL/TLS certificate includes the DB instance endpoint as the Common Name
(CN) for the SSL/TLS certificate to guard against spoofing attacks.

An SSL/TLS certificate created by Amazon RDS is the trusted root entity
and should work in most cases, but might fail if your application doesn't accept
certificate chains. If your application doesn't accept certificate chains, try using an
intermediate certificate to connect to your AWS Region. For example, you must use an
intermediate certificate to connect to the AWS GovCloud (US) Regions with SSL/TLS.

For information about downloading certificates, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md"). For more information about using SSL/TLS with
MySQL, see [Updating applications to connect to
MariaDB instances using new SSL/TLS certificates](ssl-certificate-rotation-mariadb.md "ssl-certificate-rotation-mariadb.md").

Amazon RDS for MariaDB supports Transport Layer Security (TLS) versions 1.3, 1.2, 1.1, and
1.0. TLS support depends on the MariaDB minor version. The following table shows the TLS
support for MariaDB minor versions.

| TLS version | MariaDB 11.8       | MariaDB 11.4       | MariaDB 10.11      | MariaDB 10.6       | MariaDB 10.5       | MariaDB 10.4       |
| ----------- | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| TLS 1.3     | All minor versions | All minor versions | All minor versions | All minor versions | All minor versions | All minor versions |
| TLS 1.2     | All minor versions | All minor versions | All minor versions | All minor versions | All minor versions | All minor versions |
| TLS 1.1     | Not supported      | Not supported      | Not supported      | 10.6.16 and lower  | 10.5.23 and lower  | 10.4.32 and lower  |
| TLS 1.0     | Not supported      | Not supported      | Not supported      | 10.6.16 and lower  | 10.5.23 and lower  | 10.4.32 and lower  |
