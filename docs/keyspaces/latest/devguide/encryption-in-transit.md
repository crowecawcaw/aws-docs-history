# Encryption in transit in Amazon Keyspaces

Amazon Keyspaces only accepts secure connections using Transport Layer Security (TLS). Encryption in transit provides an additional layer of data protection
by encrypting your data as it travels to and from Amazon Keyspaces.
Organizational policies, industry or government regulations, and compliance
requirements often require the use of encryption in transit to increase the data security of your
applications when they transmit data over the network.

To learn how to encrypt `cqlsh` connections to Amazon Keyspaces using TLS, see [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls"). To learn how to use TLS encryption with client drivers,
see [Using a Cassandra client driver to access
Amazon Keyspaces programmatically](programmatic.md "programmatic.md").
