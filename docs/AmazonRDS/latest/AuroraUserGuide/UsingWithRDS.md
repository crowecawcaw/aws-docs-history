# Using SSL/TLS to encrypt a connection to a DB cluster

You can use Secure Socket Layer (SSL) or Transport Layer
Security (TLS) from your application to encrypt a connection to a DB cluster
running Aurora MySQL or Aurora PostgreSQL.

SSL/TLS connections provide a layer of security by
encrypting data that moves between your client and DB
cluster. Optionally, your SSL/TLS connection can perform server
identity verification by validating the server certificate installed on your
database. To require server identity verification, follow this general
process:

1. Choose the **certificate authority (CA)**
   that signs the **DB server certificate,**
   for your database. For more information about certificate
   authorities, see [Certificate authorities](#UsingWithRDS.SSL.RegionCertificateAuthorities "#UsingWithRDS.SSL.RegionCertificateAuthorities")
   .
2. Download a certificate bundle to use when you are connecting to the
   database. To download a certificate bundle, see

[Certificate bundles by AWS Region](#UsingWithRDS.SSL.CertificatesAllRegions "#UsingWithRDS.SSL.CertificatesAllRegions")
.

###### Note

All certificates are only available for download using SSL/TLS
connections. 3. Connect to the database using your DB engine's process for
implementing SSL/TLS connections. Each DB engine has its own process for
implementing SSL/TLS. To learn how to implement SSL/TLS for your
database, follow the link that corresponds to your DB engine:

    * [Security with Amazon Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md")
    * [Security with Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md")

## Certificate authorities

The **certificate authority (CA)** is the
certificate that identifies the root CA at the top of the certificate chain.
The CA signs the **DB server certificate,**
which is installed on each DB instance. The DB server certificate identifies
the DB instance as a trusted server.

![Certificate authority overview](images/certificate-authority-overview.png)

Amazon RDS provides the following CAs to sign the DB server certificate for a
database.

| Certificate authority (CA) | Description                                                                                                                                                                                                                                                                                                                              | Common name (CN)                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| rds-ca-rsa2048-g1          | Uses a certificate authority with RSA 2048 private key<br>algorithm and SHA256 signing algorithm in most<br>AWS Regions.<br>In the AWS GovCloud (US) Regions, this CA uses a<br>certificate authority with RSA 2048 private key<br>algorithm and SHA384 signing algorithm.<br>This CA supports automatic server certificate<br>rotation. | Amazon RDS `region-identifier` Root CA RSA2048 G1 |
| rds-ca-rsa4096-g1          | Uses a certificate authority with RSA 4096 private key<br>algorithm and SHA384 signing algorithm. This CA supports<br>automatic server certificate rotation.                                                                                                                                                                             | Amazon RDS `region-identifier` Root CA RSA4096 G1 |
| rds-ca-ecc384-g1           | Uses a certificate authority with ECC 384 private key<br>algorithm and SHA384 signing algorithm. This CA supports<br>automatic server certificate rotation.                                                                                                                                                                              | Amazon RDS `region-identifier` Root CA ECC384 G1  |

###### Note

If you are using the AWS CLI, you can see the validities of the
certificate authorities listed above by using [describe-certificates](../../../cli/latest/reference/rds/describe-certificates.md "../../../cli/latest/reference/rds/describe-certificates.md").

These CA certificates are included in the regional and global certificate
bundle. When you use the rds-ca-rsa2048-g1,
rds-ca-rsa4096-g1, or rds-ca-ecc384-g1 CA with a database, RDS
manages the DB server certificate on the database. RDS rotates the DB server
certificate automatically before it expires.

### Setting the CA for your database

You can set the CA for a database when you perform the following
tasks:

- Create an Aurora DB cluster – You can set the CA for a
  DB instance in an Aurora cluster when you create the first DB
  instance in the DB cluster using the AWS CLI or RDS API.
  Currently, you can't set the CA for the DB instances in a DB
  cluster when you create the DB cluster using the RDS console.
  For instructions, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md")
  .
- Modify a DB instance – You can set the CA for a DB
  instance in a DB cluster by modifying it. For instructions, see
  [Modifying a DB instance in a DB cluster](Aurora.md#Aurora.Modifying.Instance "Aurora.md#Aurora.Modifying.Instance")
  .

###### Note

The default CA is set to
rds-ca-rsa2048-g1.
You can override the default CA for your AWS account by
using the [modify-certificates](../../../cli/latest/reference/rds/modify-certificates.md "../../../cli/latest/reference/rds/modify-certificates.md") command.

The available CAs depend on the DB engine and DB engine version. When
you use the AWS Management Console, you can choose the CA using the
**Certificate authority** setting, as shown in the
following image.

![Certificate authority option](images/certificate-authority.png)

The console only shows the CAs that are available for the DB engine
and DB engine version. If you're using the AWS CLI, you can set the CA for
a DB instance using the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") or [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command.

If you're using the AWS CLI, you can see the available CAs for your
account by using the [describe-certificates](../../../cli/latest/reference/rds/describe-certificates.md "../../../cli/latest/reference/rds/describe-certificates.md") command. This command also shows the
expiration date for each CA in `ValidTill` in the output. You
can find the CAs that are available for a specific DB engine and DB
engine version using the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.

The following example shows the CAs available for the default
RDS for PostgreSQL DB engine version.

```
aws rds describe-db-engine-versions --default-only --engine postgres
```

Your output is similar to the following. The available CAs are listed
in `SupportedCACertificateIdentifiers`. The output also shows
whether the DB engine version supports rotating the certificate without
restart in
`SupportsCertificateRotationWithoutRestart`.

```
{
    "DBEngineVersions": [
        {
            "Engine": "postgres",
            "MajorEngineVersion": "13",
            "EngineVersion": "13.4",
            "DBParameterGroupFamily": "postgres13",
            "DBEngineDescription": "PostgreSQL",
            "DBEngineVersionDescription": "PostgreSQL 13.4-R1",
            "ValidUpgradeTarget": [],
            "SupportsLogExportsToCloudwatchLogs": false,
            "SupportsReadReplica": true,
            "SupportedFeatureNames": [
                "Lambda"
            ],
            "Status": "available",
            "SupportsParallelQuery": false,
            "SupportsGlobalDatabases": false,
            "SupportsBabelfish": false,
            "SupportsCertificateRotationWithoutRestart": true,
            "SupportedCACertificateIdentifiers": [
                "rds-ca-rsa2048-g1",
                "rds-ca-ecc384-g1",
                "rds-ca-rsa4096-g1"
            ]
        }
    ]
}
```

### DB server certificate validities

The validity of DB server certificate depends on the DB engine and DB
engine version. If the DB engine version supports rotating the
certificate without restart, the validity of the DB server certificate
is 1 year. Otherwise the validity is 3 years.

For more information about DB server certificate rotation, see [Automatic server certificate rotation](UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-server-cert-rotation "UsingWithRDS.md#UsingWithRDS.SSL-certificate-rotation-server-cert-rotation")
.

### Viewing the CA for your DB instance

You can view the details about the CA for a database by viewing the
**Connectivity & security** tab in the console,
as in the following image.

![Certificate authority details](images/certificate-authority-details.png)

If you're using the AWS CLI, you can view the details about the CA for a
DB instance by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command.

## Download certificate bundles for Aurora

When you connect to your database with SSL or TLS, the database instance
requires a trust certificate from Amazon RDS. Select the appropriate link in the
following table to download the bundle that corresponds with the
AWS Region where you host your database.

### Certificate bundles by AWS Region

The certificate bundles for all AWS Regions and GovCloud (US)
Regions contain the following root CA certificates:

- `rds-ca-rsa2048-g1`
- `rds-ca-rsa4096-g1`
- `rds-ca-ecc384-g1`

The `rds-ca-rsa4096-g1` and `rds-ca-ecc384-g1`
certificates are not available in the following Regions:

- Asia Pacific (Mumbai)
- Asia Pacific (Melbourne)
- Canada West (Calgary)
- Europe (Zurich)
- Europe (Spain)
- Israel (Tel Aviv)

Your application trust store needs to only register the root CA certificate. Do not register the intermediate
CA certificates to your trust store as this might cause connection issues when RDS automatically rotates your DB server certificate.

###### Note

Amazon RDS Proxy and Aurora Serverless v1
use

certificates from the AWS Certificate Manager (ACM). If you're using RDS Proxy, you
don't need to download Amazon RDS certificates or update
applications that use RDS Proxy connections. For more information, see
[Using TLS/SSL with RDS Proxy](rds-proxy.md#rds-proxy-security.tls "rds-proxy.md#rds-proxy-security.tls")
.

If you're using Aurora Serverless v1, downloading
Amazon RDS certificates isn't required. For more information, see
[Using TLS/SSL with Aurora Serverless v1](aurora-serverless.md#aurora-serverless.tls "aurora-serverless.md#aurora-serverless.tls")
.

To download a certificate bundle for an AWS Region, select the link
for the AWS Region that hosts your database in the following
table.

| **AWS Region**                | **Certificate bundle<br>(PEM)**                                                                                                                                                                                           | **Certificate bundle<br>(PKCS7)**                                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Any commercial AWS Region     | [global-bundle.pem](https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem")                                                                | [global-bundle.p7b](https://truststore.pki.rds.amazonaws.com/global/global-bundle.p7b "https://truststore.pki.rds.amazonaws.com/global/global-bundle.p7b")                                                                |
| US East (N. Virginia)         | [us-east-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/us-east-1/us-east-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/us-east-1/us-east-1-bundle.pem")                                                 | [us-east-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/us-east-1/us-east-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/us-east-1/us-east-1-bundle.p7b")                                                 |
| US East (Ohio)                | [us-east-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/us-east-2/us-east-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/us-east-2/us-east-2-bundle.pem")                                                 | [us-east-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/us-east-2/us-east-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/us-east-2/us-east-2-bundle.p7b")                                                 |
| US West (N. California)       | [us-west-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/us-west-1/us-west-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/us-west-1/us-west-1-bundle.pem")                                                 | [us-west-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/us-west-1/us-west-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/us-west-1/us-west-1-bundle.p7b")                                                 |
| US West (Oregon)              | [us-west-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/us-west-2/us-west-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/us-west-2/us-west-2-bundle.pem")                                                 | [us-west-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/us-west-2/us-west-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/us-west-2/us-west-2-bundle.p7b")                                                 |
| Africa (Cape Town)            | [af-south-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/af-south-1/af-south-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/af-south-1/af-south-1-bundle.pem")                                            | [af-south-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/af-south-1/af-south-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/af-south-1/af-south-1-bundle.p7b")                                            |
| Asia Pacific (Hong Kong)      | [ap-east-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-east-1/ap-east-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-east-1/ap-east-1-bundle.pem")                                                 | [ap-east-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-east-1/ap-east-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-east-1/ap-east-1-bundle.p7b")                                                 |
| Asia Pacific (Hyderabad)      | [ap-south-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-south-2/ap-south-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-south-2/ap-south-2-bundle.pem")                                            | [ap-south-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-south-2/ap-south-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-south-2/ap-south-2-bundle.p7b")                                            |
| Asia Pacific (Jakarta)        | [ap-southeast-3-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-southeast-3/ap-southeast-3-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-southeast-3/ap-southeast-3-bundle.pem")                        | [ap-southeast-3-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-southeast-3/ap-southeast-3-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-southeast-3/ap-southeast-3-bundle.p7b")                        |
| Asia Pacific (Malaysia)       | [ap-southeast-5-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-southeast-5/ap-southeast-5-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-southeast-5/ap-southeast-5-bundle.pem")                        | [ap-southeast-5-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-southeast-5/ap-southeast-5-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-southeast-5/ap-southeast-5-bundle.p7b")                        |
| Asia Pacific (Melbourne)      | [ap-southeast-4-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-southeast-4/ap-southeast-4-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-southeast-4/ap-southeast-4-bundle.pem")                        | [ap-southeast-4-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-southeast-4/ap-southeast-4-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-southeast-4/ap-southeast-4-bundle.p7b")                        |
| Asia Pacific (Mumbai)         | [ap-south-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-south-1/ap-south-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-south-1/ap-south-1-bundle.pem")                                            | [ap-south-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-south-1/ap-south-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-south-1/ap-south-1-bundle.p7b")                                            |
| Asia Pacific (Osaka)          | [ap-northeast-3-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-northeast-3/ap-northeast-3-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-northeast-3/ap-northeast-3-bundle.pem")                        | [ap-northeast-3-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-northeast-3/ap-northeast-3-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-northeast-3/ap-northeast-3-bundle.p7b")                        |
| Asia Pacific (Thailand)       | [ap-southeast-7-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-southeast-7/ap-southeast-7-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-southeast-7/ap-southeast-7-bundle.pem")                        | [ap-southeast-7-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-southeast-7/ap-southeast-7-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-southeast-7/ap-southeast-7-bundle.p7b")                        |
| Asia Pacific (Tokyo)          | [ap-northeast-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-northeast-1/ap-northeast-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-northeast-1/ap-northeast-1-bundle.pem")                        | [ap-northeast-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-northeast-1/ap-northeast-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-northeast-1/ap-northeast-1-bundle.p7b")                        |
| Asia Pacific (Seoul)          | [ap-northeast-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-northeast-2/ap-northeast-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-northeast-2/ap-northeast-2-bundle.pem")                        | [ap-northeast-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-northeast-2/ap-northeast-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-northeast-2/ap-northeast-2-bundle.p7b")                        |
| Asia Pacific (Singapore)      | [ap-southeast-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-southeast-1/ap-southeast-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-southeast-1/ap-southeast-1-bundle.pem")                        | [ap-southeast-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-southeast-1/ap-southeast-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-southeast-1/ap-southeast-1-bundle.p7b")                        |
| Asia Pacific (Sydney)         | [ap-southeast-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/ap-southeast-2/ap-southeast-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/ap-southeast-2/ap-southeast-2-bundle.pem")                        | [ap-southeast-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ap-southeast-2/ap-southeast-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ap-southeast-2/ap-southeast-2-bundle.p7b")                        |
| Canada (Central)              | [ca-central-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/ca-central-1/ca-central-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/ca-central-1/ca-central-1-bundle.pem")                                  | [ca-central-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ca-central-1/ca-central-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ca-central-1/ca-central-1-bundle.p7b")                                  |
| Canada West (Calgary)         | [ca-west-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/ca-west-1/ca-west-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/ca-west-1/ca-west-1-bundle.pem")                                                 | [ca-west-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/ca-west-1/ca-west-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/ca-west-1/ca-west-1-bundle.p7b")                                                 |
| Europe (Frankfurt)            | [eu-central-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-central-1/eu-central-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-central-1/eu-central-1-bundle.pem")                                  | [eu-central-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-central-1/eu-central-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-central-1/eu-central-1-bundle.p7b")                                  |
| Europe (Ireland)              | [eu-west-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-west-1/eu-west-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-west-1/eu-west-1-bundle.pem")                                                 | [eu-west-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-west-1/eu-west-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-west-1/eu-west-1-bundle.p7b")                                                 |
| Europe (London)               | [eu-west-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-west-2/eu-west-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-west-2/eu-west-2-bundle.pem")                                                 | [eu-west-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-west-2/eu-west-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-west-2/eu-west-2-bundle.p7b")                                                 |
| Europe (Milan)                | [eu-south-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-south-1/eu-south-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-south-1/eu-south-1-bundle.pem")                                            | [eu-south-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-south-1/eu-south-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-south-1/eu-south-1-bundle.p7b")                                            |
| Europe (Paris)                | [eu-west-3-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-west-3/eu-west-3-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-west-3/eu-west-3-bundle.pem")                                                 | [eu-west-3-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-west-3/eu-west-3-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-west-3/eu-west-3-bundle.p7b")                                                 |
| Europe (Spain)                | [eu-south-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-south-2/eu-south-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-south-2/eu-south-2-bundle.pem")                                            | [eu-south-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-south-2/eu-south-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-south-2/eu-south-2-bundle.p7b")                                            |
| Europe (Stockholm)            | [eu-north-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-north-1/eu-north-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-north-1/eu-north-1-bundle.pem")                                            | [eu-north-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-north-1/eu-north-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-north-1/eu-north-1-bundle.p7b")                                            |
| Europe (Zurich)               | [eu-central-2-bundle.pem](https://truststore.pki.rds.amazonaws.com/eu-central-2/eu-central-2-bundle.pem "https://truststore.pki.rds.amazonaws.com/eu-central-2/eu-central-2-bundle.pem")                                  | [eu-central-2-bundle.p7b](https://truststore.pki.rds.amazonaws.com/eu-central-2/eu-central-2-bundle.p7b "https://truststore.pki.rds.amazonaws.com/eu-central-2/eu-central-2-bundle.p7b")                                  |
| Israel (Tel Aviv)             | [il-central-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/il-central-1/il-central-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/il-central-1/il-central-1-bundle.pem")                                  | [il-central-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/il-central-1/il-central-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/il-central-1/il-central-1-bundle.p7b")                                  |
| Mexico (Central)              | [mx-central-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/mx-central-1/mx-central-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/mx-central-1/mx-central-1-bundle.pem")                                  | [mx-central-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/mx-central-1/mx-central-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/mx-central-1/mx-central-1-bundle.p7b")                                  |
| Middle East (Bahrain)         | [me-south-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/me-south-1/me-south-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/me-south-1/me-south-1-bundle.pem")                                            | [me-south-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/me-south-1/me-south-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/me-south-1/me-south-1-bundle.p7b")                                            |
| Middle East (UAE)             | [me-central-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/me-central-1/me-central-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/me-central-1/me-central-1-bundle.pem")                                  | [me-central-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/me-central-1/me-central-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/me-central-1/me-central-1-bundle.p7b")                                  |
| South America (São Paulo)     | [sa-east-1-bundle.pem](https://truststore.pki.rds.amazonaws.com/sa-east-1/sa-east-1-bundle.pem "https://truststore.pki.rds.amazonaws.com/sa-east-1/sa-east-1-bundle.pem")                                                 | [sa-east-1-bundle.p7b](https://truststore.pki.rds.amazonaws.com/sa-east-1/sa-east-1-bundle.p7b "https://truststore.pki.rds.amazonaws.com/sa-east-1/sa-east-1-bundle.p7b")                                                 |
| Any AWS GovCloud (US) Regions | [global-bundle.pem](https://truststore.pki.us-gov-west-1.rds.amazonaws.com/global/global-bundle.pem "https://truststore.pki.us-gov-west-1.rds.amazonaws.com/global/global-bundle.pem")                                    | [global-bundle.p7b](https://truststore.pki.us-gov-west-1.rds.amazonaws.com/global/global-bundle.p7b "https://truststore.pki.us-gov-west-1.rds.amazonaws.com/global/global-bundle.p7b")                                    |
| AWS GovCloud (US-East)        | [us-gov-east-1-bundle.pem](https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-east-1/us-gov-east-1-bundle.pem "https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-east-1/us-gov-east-1-bundle.pem") | [us-gov-east-1-bundle.p7b](https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-east-1/us-gov-east-1-bundle.p7b "https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-east-1/us-gov-east-1-bundle.p7b") |
| AWS GovCloud (US-West)        | [us-gov-west-1-bundle.pem](https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-west-1/us-gov-west-1-bundle.pem "https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-west-1/us-gov-west-1-bundle.pem") | [us-gov-west-1-bundle.p7b](https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-west-1/us-gov-west-1-bundle.p7b "https://truststore.pki.us-gov-west-1.rds.amazonaws.com/us-gov-west-1/us-gov-west-1-bundle.p7b") |

### Viewing the contents of your CA certificate

To check the contents of your CA certificate bundle, use the following
command:

```
keytool -printcert -v -file global-bundle.pem
```
