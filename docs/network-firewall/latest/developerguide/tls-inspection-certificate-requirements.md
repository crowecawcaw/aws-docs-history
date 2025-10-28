# Using

SSL/TLS certificates with TLS inspection configurations in AWS Network Firewall

Network Firewall integrates with AWS Certificate Manager (ACM) to make it easy to manage the certificates that
you're using to decrypt and re-encrypt your firewall's SSL/TLS traffic. To get started
with TLS inspection configurations, you must first import or issue certificates to ACM, and then
associate the certificates with your TLS inspection configuration. You can configure certificates for inbound
or outbound inspection, or both. To view the maximum number of certificates that you can
use, see [AWS Network Firewall quotas](quotas.md "quotas.md"). This section discusses how to
use SSL/TLS certificates with TLS inspection configurations.

## General requirements for TLS inspection

The following are general requirements for the certificates that are used for TLS
inspection.

###### Certificate chain order

Imported SSL/TLS certificates require all of the intermediate certificates in
the certificate chain that's in the **.pem** file,
beginning with the certificate authority (CA) that signed the certificate that
you are importing. Typically, you'll find a file on the CA website that lists
intermediate and root certificates in the proper chained order. Here's an
example:

```
-----BEGIN CERTIFICATE-----
Intermediate certificate 2
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Intermediate certificate 1
-----END CERTIFICATE-----
```

###### Supported certificates

Network Firewall supports all of the algorithms and key sizes that are supported by
AWS Certificate Manager (ACM), and also supports wildcard certificates. However, Network Firewall
doesn't support using self-signed certificates for inbound inspection. Using
self-signed certificates can result in client-side errors, and using
cross-signed certificates can result in asynchronous and synchronous failures.
For information about ACM supported algorithms, key sizes, and wildcard
certificates, see [ACM certificate
characteristics](../../../acm/latest/userguide/acm-certificate.md "../../../acm/latest/userguide/acm-certificate.md") in the _AWS Certificate Manager User Guide_.

If a certificate that's associated with your TLS inspection configuration expires or is deleted, you
experience client-side errors in the traffic that Network Firewall processes. Replace
certificates that will expire soon to avoid client-side errors.

## Server certificates - Inbound SSL/TLS inspection

To configure inbound TLS inspection, you must first issue or import a certificate
in AWS Certificate Manager (ACM) for each domain that you want Network Firewall to inspect. After you
issue or import the certificates in ACM, you can associate the certificates with
your TLS inspection configuration.

For more information about working with certificates in ACM, see [Request a public certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md") or [Importing certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the _AWS Certificate Manager User Guide_.

The following requirements are specific to the server certificates that are used
for inbound inspection.

###### Certificate issuer

For server certificates for inbound inspection, Network Firewall supports the same certificate authorities (CAs) as Mozilla, except for those that issue cross-signed root certificates. If you import a certificate into ACM, use a certificate issued by a CA on the [Mozilla Included CA Certificate List](https://wiki.mozilla.org/CA/Included_Certificates "https://wiki.mozilla.org/CA/Included_Certificates"). For more information about getting and installing a certificate, refer to the documentation for your HTTP server software and to the documentation for the CA.

###### Note

Network Firewall can't validate cross-signed root certificates, such as those issued by Let's Encrypt. Usage of cross-signed certificates can cause asynchronous failures in your firewall.

###### Deleted or expired certificates

Network Firewall doesn't support the Online Certificate Status Protocol (OCSP) MustStaple TLS extension. Network Firewall also doesn't validate the expiration status of
server certificates that are associated with a TLS inspection configuration. Validate the status of
your server certificates and use a valid certificate at all times.

###### Supported certificates

You can either generate or import a server certificate in ACM.

## CA certificate - Outbound SSL/TLS inspection

To configure outbound TLS inspection, you must first import a certificate
authority (CA) certificate into AWS Certificate Manager (ACM). After you import the CA
certificate in ACM, you can associate the CA certificate with your TLS inspection configuration. Network Firewall
uses the CA certificate to generate a server certificate, which the service uses to
establish trust between the client and the server.

For more information about working with certificates in ACM, see [Importing certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the _AWS Certificate Manager User Guide_.

The following requirements are specific to CA certificates that are used for
outbound SSL/TLS inspection.

###### Supported certificates

You can use CA certificates that are imported into ACM for outbound
inspection—including private certificates—but you can't generate
intermediate CA certificates using ACM. However, we don't support TLS traffic to or from destination servers that use a server certificate signed by a private CA. In other words, we do certificate verification of downstream server certificates to allow TLS traffic where server certificates are signed by public well-known roots contained on the [Mozilla Included CA Certificate List](https://wiki.mozilla.org/CA/Included_Certificates "https://wiki.mozilla.org/CA/Included_Certificates") . We also don't support certificates issued by AWS Private Certificate Authority.

###### Revoked certificates

For outbound TLS, you can enable certificate revocation checks, which allows
Network Firewall to check revocation status with Online Certificate Status Protocol (OCSP)
and Certificate Revocation List (CRL) on behalf of clients. For more information
see [Checking certificate revocation status](#tls-inspection-check-certificate-revocation-status "#tls-inspection-check-certificate-revocation-status").

## Checking certificate revocation status

For outbound inspection, Network Firewall can check if the server or intermediate certificate that the server presents in the TLS connection has a revoked or unknown status. When you enable this option, Network Firewall checks the revocation status using the Online Certificate Status Protocol (OCSP) and Certificate Revocation List (CRL) endpoints. These endpoints
are specified in the certificate authority (CA) certificate that's downloaded from
the server in the SSL/TLS connection. Network Firewall caches the CRL and OCSP responses.

If the certificate has a revoked or unknown status, Network Firewall handles the outbound
traffic based on the actions that you set when you configure the revocation status
checks.

###### Actions

When the certificate has a revoked or unknown status, you can choose from the
following actions. These actions configure how Network Firewall processes traffic when it
determines that the certificate that's presented by the server in the SSL/TLS
connection has an unknown or revoked status.

- **Pass** – Allows the connection to continue, and pass
  subsequent packets to the stateful engine for inspection.
- **Drop** – Network Firewall closes the connection and drops subsequent packets for that connection.
- **Reject** – Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. This option is available only for TCP traffic.

Keep the following considerations in mind when turning on certificate revocation
check:

###### Caching

Network Firewall caches the revocation check status to serve responses faster than the
CRL and OCSP servers can. The cache duration depends on the revocation check
status, which improves the accuracy of the certificate revocation status
checks.

###### Latency

When you turn on certificate revocation checking for outbound TLS inspection,
expect additional latency when you initially connect to a new domain over a
firewall instance. This is specific to outbound TLS inspection only. We
recommend that you conduct your own testing using your rulesets to ensure that
the service meets your performance expectations.

###### Logging

You can get logs for certificate revocation check failures. To do this, configure TLS logging for your firewall's stateful engine.
For additional information, see [Logging for TLS inspection in AWS Network Firewall](tls-inspection-logging.md "tls-inspection-logging.md").
For information about enabling logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").

###### Unsupported features

Revocation status checking doesn't include support for the following:

- Configurations for salted or nonce OCSP responses.
- Network Firewall supports OCSP checks using a different signer key, but doesn't support CRL checks using a different signer key.
- Delegated OCSP checks.
- Delta Certificate Revocation Lists (CRLs).
- File Transfer Protocol (FTP) and Lightweight Directory Access Protocol (LDAP) CRL URLs.
- OCSP and CRL checks requiring referenced parameters from issuer certificates.
- OCSP stapling.

For information about troubleshooting issues related to certificate revocation, see [Troubleshooting TLS inspection in AWS Network Firewall](troubleshooting-tls-inspection.md "troubleshooting-tls-inspection.md").

## Creating a certificate for inbound TLS inspection with AWS Private CA

You can use AWS Private CA to create certificates for inbound TLS inspection. This procedure shows you how to create a certificate that works with Network Firewall inbound inspection.

###### Prerequisites

Before you begin, verify that you have the following:

- A certificate authority (CA) with ACTIVE status in AWS Private CA
- OpenSSL installed on your system

###### To create a certificate for inbound TLS inspection

1. Create an OpenSSL configuration file named `openssl_temp.cnf`. Use the following template and modify the values for your environment. The `req_ext` section must have `basicConstraints` enabled. Adjust the `pathlen` value based on your Public Key Infrastructure (PKI) structure.

```
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
req_extensions = req_ext

[ dn ]
C = US
ST = Your-State
L = Your-City
O = Your-Organization
OU = Your-Organizational-Unit
CN = <domain name here>

[ req_ext ]
basicConstraints = critical, CA:TRUE, pathlen:0
keyUsage = critical, digitalSignature, keyEncipherment, keyCertSign, cRLSign
extendedKeyUsage = critical, serverAuth, clientAuth
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = <DNS Name here>

```

2. Generate a private key using OpenSSL.

```
openssl genrsa -out key.pem 2048
```

3. Create a Certificate Signing Request (CSR) using your configuration file.

```
openssl req -new -sha256 -key key.pem -nodes -out req.csr -config openssl_temp.cnf
```

4. Sign the certificate with AWS Private CA. Replace the placeholder values with your actual ARN and region. Adjust the template ARN if your `pathlen` value differs.

```
aws acm-pca issue-certificate --certificate-authority-arn <pca_arn> --csr fileb://req.csr --signing-algorithm SHA256WITHRSA --validity Value=365,Type="DAYS" --template-arn arn:aws:acm-pca:::template/BlankSubordinateCACertificate_PathLen0_CSRPassthrough/V1 --region <region> --output json
```

5. Export the signed certificate from AWS Private CA. Use the certificate ARN from the previous step.

```
aws acm-pca get-certificate --certificate-arn <cert_arn_from_previous_step> --certificate-authority-arn <pca_arn> --region <region> --output json | jq -r '.Certificate, .CertificateChain'
```

6. Upload the certificate to AWS Certificate Manager (ACM). The command output provides two certificate sections in PEM format. Use the first section as the certificate body, the second section as the certificate chain, and the `key.pem` file from step 2 as the private key.

```
-----BEGIN CERTIFICATE-----
<Certificate body>
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
<Certificate chain>
-----END CERTIFICATE-----

```
