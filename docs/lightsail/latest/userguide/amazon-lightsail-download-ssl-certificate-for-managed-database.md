# Download an

SSL/TLS certificate for secure app connectivity to Lightsail databases

You can use Secure Socket Layer (SSL) or Transport Layer Security (TLS) from your
application to encrypt a connection to a managed database in Amazon Lightsail running MySQL, or
PostgreSQL. Each DB engine has its own process for implementing SSL/TLS. For more information,
see [Using SSL to connect
to your MySQL database](amazon-lightsail-connecting-to-mysql-database-using-ssl.md "amazon-lightsail-connecting-to-mysql-database-using-ssl.md") or [Using SSL to connect to
your PostgreSQL database](amazon-lightsail-connecting-to-postgres-database-using-ssl.md "amazon-lightsail-connecting-to-postgres-database-using-ssl.md").

###### Note

The certificates available for download are labeled for Amazon Relational Database Service (Amazon RDS), but also work
for managed databases in Lightsail.

## Certificate bundles for all AWS Regions

To get a certificate bundle that contains both the intermediate and root certificates for
all AWS Regions, or if your application is on Microsoft Windows and requires a PKCS7 file,
see [Certificate bundles for all AWS Regions](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesAllRegions "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.CertificatesAllRegions") in the Amazon Relational Database Service User Guide.

This root certificate is a trusted root entity and should work in most cases. However, it
might fail if your application doesn't accept certificate chains. If your application doesn't
accept certificate chains, continue to the next section of this document.

## Certificate bundles for specific

AWS Regions

To get a certificate bundle that contains both the intermediate and root certificates for
a specific AWS Region, see [Certificate bundles for specific AWS Regions](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.RegionCertificates "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md#UsingWithRDS.SSL.RegionCertificates") in the Amazon Relational Database Service User Guide.
