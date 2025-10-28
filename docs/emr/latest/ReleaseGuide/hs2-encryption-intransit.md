# In-transit encryption in

HiveServer2

Starting with Amazon EMR release 6.9.0, HiveServer2 (HS2) is TLS/SSL-enabled as part of
In-transit encryption in
HiveServer2 security configuration. This affects
how you connect to HS2 running on an Amazon EMR cluster with in-transit encryption
enabled. To connect to HS2, you must modify the `TRUSTSTORE_PATH` and
`TRUSTSTORE_PASSWORD` parameter values in the JDBC URL. The following
URL is an example of a JDBC connection for HS2 with the required parameters:

```
jdbc:hive2://`HOST_NAME`:10000/default;ssl=true;sslTrustStore=`TRUSTSTORE_PATH`;trustStorePassword=`TRUSTSTORE_PASSWORD`
```

Use the appropriate instuctions for on-cluster or off-cluster HiveServer2
encryption below.

On-cluster HS2 access
If you are accessing HiveServer2 using the Beeline client after you
SSH to the primary node, then reference
`/etc/hadoop/conf/ssl-server.xml` to find the
`TRUSTSTORE_PATH` and `TRUSTSTORE_PASSWORD`
parameter values using configuration
`ssl.server.truststore.location` and
`ssl.server.truststore.password`.

The following example commands can help you retrieve these
configurations:

```
TRUSTSTORE_PATH=$(sed -n '/ssl.server.truststore.location/,+2p' /etc/hadoop/conf/ssl-server.xml | awk -F "[><]" '/value/{print $3}')
TRUSTSTORE_PASSWORD=$(sed -n '/ssl.server.truststore.password/,+2p' /etc/hadoop/conf/ssl-server.xml | awk -F "[><]" '/value/{print $3}')
```

Off-cluster HS2 access
If you are accessing HiveServer2 from a client outside the Amazon EMR
cluster. you can use one of the following approaches to get the
`TRUSTSTORE_PATH` and
`TRUSTSTORE_PASSWORD`:

- Convert the PEM file that was created during [security configuration](../ManagementGuide/emr-encryption-enable.md "../ManagementGuide/emr-encryption-enable.md") to a JKS file and use the
  same in the JDBC connection URL. For example, with openssl and
  keytool, use the following commands:

```
openssl pkcs12 -export -in trustedCertificates.pem -inkey privateKey.pem -out trustedCertificates.p12 -name "certificate"
keytool -importkeystore -srckeystore trustedCertificates.p12 -srcstoretype pkcs12 -destkeystore trustedCertificates.jks
```

- Alternatively, reference
  `/etc/hadoop/conf/ssl-server.xml` to find the
  `TRUSTSTORE_PATH` and
  `TRUSTSTORE_PASSWORD` parameter values using
  configuration `ssl.server.truststore.location` and
  `ssl.server.truststore.password`. Download the
  truststore file to the client machine and use the path on the
  client machine as the `TRUSTSTORE_PATH`.

For more information on accessing applications from a client
outside of the Amazon EMR cluster, see [Use the
Hive JDBC driver](HiveJDBCDriver.md "HiveJDBCDriver.md").
