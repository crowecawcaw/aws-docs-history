# Manage AS2 certificates

This topic discusses how to import and manage AS2 certificates. Importing certificates
is the first step in the AS2 process for Transfer Family.

1. Import certificates
2. [Create AS2 profiles](configure-as2-profile.md "configure-as2-profile.md")
3. [Create an AS2 server](create-as2-transfer-server.md "create-as2-transfer-server.md")
4. [Create an AS2 agreement](create-as2-transfer-server.md#as2-agreements "create-as2-transfer-server.md#as2-agreements")
5. [Configure AS2 connectors](configure-as2-connector.md "configure-as2-connector.md")

## Import AS2 certificates

The Transfer Family AS2 process uses certificate keys for both encryption and signing of
transferred information. Partners can use the same key for both purposes, or a
separate key for each. If you have common encryption keys kept in escrow by a
trusted third-party so that data can be decrypted in the event of a disaster or
security breach, we recommend having separate signing keys. By using separate
signing keys (which you do not escrow), you don't compromise the non-repudiation
features of your digital signatures.

###### Note

The key length for AS2 certificates must be at least 2048 bits, and at
most 4096.

The following points detail how AS2 certificates are used during the
process.

- Inbound AS2
  - The trading partner sends their public key for the signing
    certificate, and this key is imported to the partner profile.
  - The local party sends the public key for their encryption and
    signing certificates. The partner then imports the private key or
    keys. The local party can send separate certificate keys for signing
    and encryption, or can choose to use the same key for both
    purposes.

- Outbound AS2
  - The partner sends the public key for their encryption certificate,
    and this key is imported to the partner profile.
  - The local party sends the public key for the certificate for
    signing, and imports the private key of the certificate for
    signing.
  - If you are using HTTPS, you can import a self-signed Transport
    Layer Security (TLS) certificate.

For details on how to create certificates, see [Step 1: Create certificates for AS2](as2-example-tutorial.md#as2-create-certs "as2-example-tutorial.md#as2-create-certs").

This procedure explains how to import certificates by using the Transfer Family console. If
you want to use the AWS CLI instead, see [Step 2: Import certificates as Transfer Family
certificate resources](as2-example-tutorial.md#as2-import-certs-example "as2-example-tutorial.md#as2-import-certs-example").

###### To specify an AS2-enabled certificate

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, under **AS2 Trading
   Partners**, choose **Certificates**.
3. Choose **Import certificate**.
4. In the **Certificate configuration** section, for
   **Certificate description**, enter an easily
   identifiable name for the certificate. Make sure that you can identify the
   certificate's purpose by its description. Additionally, choose the role for
   the certificate.
5. In the **Certificate usage** section, choose the purpose
   for this certificate. It can be used for encryption, signing, or
   both.

**Tip:** If you choose **Encryption
and signing** for the usage, Transfer Family creates two identical
certificates (each having their own ID): one with a usage value of
`ENCRYPTION` and one with a usage value of
`SIGNING`. 6. In the **Certificate contents** section, provide a public
certificate from a trading partner, or the public and private keys for a
local certificate.

Fill in the **Certificate contents** section with the
appropriate details.

    * If you choose **Self-signed certificate**, you do
     not provide the certificate chain.
    * Paste the certificate text and its chain into the
     **Certificate and Certificate chain**
     field.
    * If this certificate is a local certificate, paste in its private
     key.

7. Choose **Import certificate** to complete the process and
   save the details for the imported certificate.

###### Note

TLS certificates can only be imported as a partner's public certificate. If
you select **Public certificate from a partner**, and then
select **Transport Layer Security (TLS)** for the usage, you
receive a warning. Also, TLS certificates must be self-signed (that is, you must
select **Self Signed Certificate** to import a TLS
certificate).

## AS2 certificate rotation

Often, certificates are valid for a period of six months to a year. You might have
set up profiles that you want to persist for a longer duration. To facilitate this,
Transfer Family provides certificate rotation. You can specify multiple certificates for a
profile, allowing you to keep using the profile for multiple years. Transfer Family uses
certificates for signing (optional) and encryption (mandatory). You can specify a
single certificate for both purposes, if you like.

Certificate rotation is the process of replacing an old expiring certificate with
a newer certificate. The transition is a gradual one to avoid disrupting transfers
where a partner in the agreement has yet to configure a new certificate for outbound
transfers or might be sending payloads that are signed or encrypted with an old
certificate during a period when a newer certificate might also be in use. The
intermediate period where both old and new certificates are valid is referred to as
a _grace period_.

X.509 certificates have `Not Before` and `Not After` dates.
However, these parameters might not provide enough control for administrators. Transfer Family
provides `Active Date` and `Inactive Date` settings to control
which certificate is used for outbound payloads and which is accepted for inbound
payloads.

### Certificate expiration

monitoring

Transfer Family publishes a Amazon CloudWatch metric `DaysUntilExpiry` after importing
a certificate. The metric emits the number of days between the current date and
the date specified as the `InactiveDate` on the Certificate. The
metric is found under the `Transfer` AWS namespace in the CloudWatch
metrics dashboard.

This metric will always have a metric dimension for
**CertificateId** and will optionally include a
**Description** dimension if provided by the customer on
the certificate. For more information about CloudWatch metric dimensions, see
[Dimension](../../../AmazonCloudWatch/latest/APIReference/API_Dimension.md "../../../AmazonCloudWatch/latest/APIReference/API_Dimension.md") in the _CloudWatch API
Reference_.

###### Note

It can take up to a full day after importing a Certificate for Transfer Family to
emit this metric to the customer account.

You can use this metric to create CloudWatch alarms that notify you when
certificates are approaching expiration.

Outbound certificate selection uses the maximum value that is prior to the
date of the transfer as an `Inactive Date`. Inbound processes accept
certificates within the range of `Not Before` and `Not
 After` and within the range of `Active Date` and
`Inactive Date`.

### Certificate rotation example

The following table describes one possible way to configure two certificates
for a single profile.

Two certificates in rotation| Name | NOT BEFORE (controlled by certificate
authority) | ACTIVE DATE (set by Transfer Family) | INACTIVE DATE (set by Transfer Family) | NOT AFTER (set by certificate
authority) |
| --- | --- | --- | --- | --- |
| Cert1 (older certificate) | 2019-11-01 | 2020-01-01 | 2020-12-31 | 2024-01-01 |
| Cert2 (newer certificate) | 2020-11-01 | 2020-06-01 | 2021-06-01 | 2025-01-01 | Note the following: <br>• When you specify an `Active Date` and `Inactive Date` for a certificate, the range must be inside the range between `Not Before` and `Not After`. <br>• We recommend that you configure several certificates for each profile, making sure that the active date range for all the certificates combined covers the amount of time for which you want to use the profile. <br>• We recommend that you specify some grace time between when your older certificate becomes inactive and when your newer certificate becomes active. In the preceding example, the first certificate does not become inactive until 2020-12-31, while the second certificate becomes active on 2020-06-01, providing a 6-month grace period. During the period from 2020-06-01 until 2020-12-31, both certificates are active.
