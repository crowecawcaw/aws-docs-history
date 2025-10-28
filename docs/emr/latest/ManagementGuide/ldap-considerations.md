# Application support and considerations with LDAP

for Amazon EMR

This topic lists supported applications, supported features and unsupported features.

## Supported applications with LDAP for

Amazon EMR

###### Important

The applications listed on this page are the only applications that Amazon EMR
supports for LDAP. To ensure cluster security, you can only include
LDAP-compatible applications when you create an EMR cluster with LDAP enabled.
If you attempt to install other, unsupported applications, Amazon EMR will reject
your request for a new cluster.

The Amazon EMR releases 6.12 and higher support LDAP integration with the following
applications:

- Apache Livy
- Apache Hive through HiveServer2 (HS2)
- Trino
- Presto
- Hue

You can also install the following applications on an EMR cluster and configure
them to meet your security needs:

- Apache Spark
- Apache Hadoop

## Supported features with LDAP for

Amazon EMR

You can use the following Amazon EMR features with the LDAP integration:

###### Note

To keep LDAP credentials secure, you must use in-transit encryption to secure
the flow of data on and off the cluster. For more information about in-transit
encryption, see [Encrypt data at rest and in transit with Amazon EMR](emr-data-encryption.md "emr-data-encryption.md").

- Encryption in transit (required) and at rest
- Instance groups, instance fleets, and Spot Instances
- Reconfiguration of applications on a running cluster
- EMRFS server-side encryption (SSE)

## Unsupported features

Consider the following limitations when you use the Amazon EMR LDAP integration:

- Amazon EMR disables steps for clusters with LDAP enabled.
- Amazon EMR doesn't support runtime roles and AWS Lake Formation integrations for clusters
  with LDAP enabled.
- Amazon EMR doesn't support LDAP with StartTLS.
- Amazon EMR doesn't support high-availability mode (clusters with multiple
  primary nodes) for clusters with LDAP enabled.
- You can't rotate bind credentials or certificates for clusters with LDAP
  enabled. If any of those fields were rotated, we recommend that you start a
  new cluster with the updated bind credentials or certificates.
- You must use exact search bases with LDAP. The LDAP user and group search
  base doesn't support LDAP search filters.
