# Encryption in transit

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

It is best practice to encrypt all network communications between software components. [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security "https://en.wikipedia.org/wiki/Transport_Layer_Security") is an
industry-standard protocol used for encrypting communications between two networked applications. Using TLS reduces the possibility of the communications being intercepted or
modified in transit.

TLS makes use of [X.509 certificates](https://en.wikipedia.org/wiki/X.509 "https://en.wikipedia.org/wiki/X.509") to make and validate claims of identity between the endpoints of a TLS communication channel. The X.509
standard defines a specific format of digital certificate that can be used for identification and message encryption.

Where possible, the RFDK supports the ability to use TLS for communication between software components of the render farm.

## Where does RFDK use TLS and certificates?

RFDK uses X.509 certificates to secure communications between the following constructs:

**Deadline Clients and the Deadline Render Queue’s Load Balancer**

The Render Queue must be provided a certificate that can be used to establish a TLS connection with any Deadline Client that connects to it. The Render Queue deploys an
Application Load Balancer (ALB) and configures it to present the supplied certificate during the TLS handshake from incoming client connections. RFDK constructs will configure
Deadline Clients to trust the certificate chain when connecting them to a Render Queue.

**Deadline Render Queue’s Load Balancer and the Deadline Remote Connection Server**

The Remote Connection Server (RCS) is encapsulated by the Render Queue construct. It is the service that sits behind the ALB that is set up by the Render Queue. During
instantiation, the Render Queue generates a self-signed certificate using [X509CertificatePem](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md")
and [X509CertificatePkcs12](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") that the RCS is configured to use for communication between itself
and the ALB.

**Deadline Remote Connection Server and the database**

The Deadline Remote Connection Server (RCS) communicates directly with a MongoDB-compatible database. These communications are encrypted by default when this database is
an [Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/") or a MongoDB created by the RFDK’s
[MongoDbInstance](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") construct.

**MongoDB**

The MongoDB Construct requires that a certificate be provided as input to it, for it to use as its own proof of identity for the clients that need to connect to it. It requires
that this certificate be in the [IX509CertificatePem](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") format.

## RFDK’s built-in certificate management

RFDK provides constructs that can be used to work with X509 certificates. This includes:

- [X509CertificatePem](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") - A construct that generates and stores the following in AWS Secrets
  Manager Secrets:

      + A X.509 certificate in the PEM format
      + A private key in PEM format
      + A passphrase for the private key
      + An optional trust-chain in PEM format

- [X509CertificatePkcs12](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") - A construct that converts the outputs of
  [X509CertificatePem](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") into a single PKCS #12 archive.
- [ImportedAcmCertificate](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") - A construct that imports a PEM certificate into
  AWS Certificate Manager. This Construct implements CDK’s [ICertificate](../../../cdk/api/latest/docs/@aws-cdk_aws-certificatemanager.md "../../../cdk/api/latest/docs/@aws-cdk_aws-certificatemanager.md")
  interface so that the certificates can be used by other CDK Constructs that require this interface, such as the Deadline Render Queue construct.

If you are using the RFDK’s built-in certificate constructs, then it is recommended that a self-signed certificate be created by your RFDK application to act as a Certificate
Authority (CA), and then used to sign any other certificates that components of the RFDK application require. This root certificate should only be used to sign
other certificates, and access to its private key must be tightly controlled. The certificate should not be configured to be used as the identity for a server or service.

###### Warning

The built-in certificate management does not currently support a method to rotate certificates. The X.509 certificates it creates are configured to
**expire after 1095 days (3 years)**. After this period, TLS connections between components using these certificates will no longer work and they will need to be
redeployed with new certificates.

Here is an example snippet from a CDK application that uses the [X509CertificatePem](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md"),
the [X509CertificatePkcs12](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md"), and the
[ImportedAcmCertificate](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md"):

Python

```
class CertStack(cdk.Stack):
  def __init__(scope, id, props):
    # Generate a root CA and then use it to sign another identity certificate
    signing_cert = rfdk.X509CertificatePem(self, "RootPem",
      subject={ "cn": "server.internal" },
    );
    server_cert = rfdk.X509CertificatePem(self, "ServerPem",
      subject={ "cn": "name.server.internal" },
      signing_certificate=signing_cert
    );

    # Convert the identity certificate PEM into PKCS#12
    rfdk.X509CertificatePkcs12(self, "Pkcs",
      source_certificate=server_cert
    );

    // Import the identity certificate into ACM
    rfdk.ImportedAcmCertificate(this, "AcmCert2",
      cert=server_cert.cert,
      cert_chain=server_cert.certChain,
      key=server_cert.key,
      passphrase=server_cert.passphrase
    );

```

TypeScript

```
class CertStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props: StackProps) {
    // Generate a root CA and then use it to sign another identity certificate
    const signingCert = new X509CertificatePem(this, 'RootPem', {
      subject: { cn: 'server.internal' },
    });
    const serverCert = new X509CertificatePem(this, 'ServerPem', {
      subject: { cn: 'name.server.internal' },
      signingCertificate: signingCert,
    });

    // Convert the identity certificate PEM into PKCS#12
    new X509CertificatePkcs12(this, 'Pkcs', {
      sourceCertificate: serverCert,
    });

    // Import the identity certificate into ACM
    new ImportedAcmCertificate(this, 'AcmCert2', {
      cert: serverCert.cert,
      certChain: serverCert.certChain,
      key: serverCert.key,
      passphrase: serverCert.passphrase,
    });
  }
}

```

## Alternatives to RFDK’s built-in certificate management

### Manual certificates

An alternative method of creating and using certificates is similar to the method built into RFDK. Rather than using the
[X509CertificatePem](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") Construct to generate certificates, they could
be generated using any other public key infrastructure. Once a certificate is created, it can be imported into AWS Secrets Manager Secrets in the same
format that the [ImportedAcmCertificate](../../api/latest/docs/aws-rfdk.md "../../api/latest/docs/aws-rfdk.md") Construct takes as input.

### Private Certificate Manager certificates

It is possible to create a private certificate in AWS Certificate Manager (ACM) that can be used. To do this, you will need to use AWS Certificate Manager
Private Certificate Authority (ACM PCA) to create a certificate authority that can then be used to sign a certificate in ACM. Be aware that the ACM PCA costs
can be significant and should be considered before taking this approach. Visit the [Certificate Manager Pricing](https://aws.amazon.com/certificate-manager/pricing/ "https://aws.amazon.com/certificate-manager/pricing/")
for more information.

A benefit of using this method is that the entire management of a certificate is handled for you, you do not have to worry about rotating certificates before they
expire or making sure you’re storing your certificates in a secure way. The main trade-offs are the cost and the additional work of having to set them up outside
of your CDK application. The CDK does not currently support this workflow with ACM PCA.

An ACM Certificate in CDK does not expose the certificate chain, so when using these private certificates from ACM, the certificate chain will need to be migrated
to a Secret for RFDK to distribute to clients of the certificate holder. There are a few ways to do this, so instructions specific to each option can be found in
the following sections. Once you have your ACM Certificate and your Secret containing the certificate chain created, they can be imported into CDK using
[`Secret.fromSecretArn(scope, id, secretArn)`](../../../cdk/api/latest/docs/@aws-cdk_aws-secretsmanager.md#static-from-wbr-secret-wbr-arnscope-id-secretarn "../../../cdk/api/latest/docs/@aws-cdk_aws-secretsmanager.md#static-from-wbr-secret-wbr-arnscope-id-secretarn")
and [`Certificate.fromCertificateArn(scope, id, certificateArn)`](../../../cdk/api/latest/docs/@aws-cdk_aws-certificatemanager.md#static-from-wbr-certificate-wbr-arnscope-id-certificatearn "../../../cdk/api/latest/docs/@aws-cdk_aws-certificatemanager.md#static-from-wbr-certificate-wbr-arnscope-id-certificatearn").
The following example demonstrates how these methods can be used when setting the properties of your RenderQueue during its creation:

Python

```

  acm_cert = aws_cdk.aws_certificatemanager.Certificate.from_certificate_arn(this, 'RqCert', [certificate_arn])
  acm_cert_chain = aws_cdk.aws_secretsmanager.Secret.from_secret_arn(this, 'RqCertChain', [secret_arn])
  traffic_encryption = aws_rfdk.deadline.RenderQueueTrafficEncryptionProps(
    external_tls = aws_rfdk.deadline.RenderQueueExternalTLSProps(
      acm_certificate = acm_cert,
      acm_certificate_chain = acm_cert_chain,
    )
  )

```

TypeScript

```

  trafficEncryption: {
    externalTLS: {
      acmCertificate: AcmCertificate.fromCertificateArn(
        this,
        'RqCert',
        [certificateArn],
      ),
      acmCertificateChain: Secret.fromSecretArn(
        this,
        'RqCertChain',
        [secretArn],
      ),
    },
  },

```

Until the CDK supports this workflow, these are the alternative methods that can be used for the creation of this private certificate:

###### Manually create the resources using the AWS Console

To use the AWS Console to create the resources required for using a private ACM Certificate you’ll first need to create a private CA by opening Certificate Manager
in the AWS Console, selecting Private CA on the sidebar, and then pressing the Create CA button and following the steps to create a new root CA. Visit the
[ACM PCA User Guide](../../../acm-pca/latest/userguide/PcaCreateCa.md "../../../acm-pca/latest/userguide/PcaCreateCa.md") for more detailed instructions. After creating your private CA, you can
then navigate back to Certificate Manager and press the Request a Certificate button. Then you can select "Request a private certificate" and in the next step there
will be a drop-down menu to select a CA where you can see your private CA listed. Follow the remaining steps, using a domain name such as **renderqueue.server.internal**.
This domain name should match the fully qualified domain name of the RenderQueue, which is the combination of the hostname set as a property of the RenderQueue and
the zone name set as a property of the PrivateHostedZone it’s in. More details can be found on the
[ACM User Guide](../../../acm/latest/userguide/gs-acm-request-private.md "../../../acm/latest/userguide/gs-acm-request-private.md"). Note the ARN of the Certificate after it has been created.

Once your private certificate is created, you’ll need to get the certificate chain into AWS Secrets Manager. This can also be done directly in the console, since private
certificates can be displayed there by using the export feature. Simply select the Certificate from the Certificate Manager console, click on the Actions menu, and
select "Export (private certificates only)". You’ll be asked to create a password for the private key. Don’t worry too much about the password here since we don’t
need to export the private key right now and it can be re-entered if you ever do the export process again. After submitting the password, you will see the
certificate chain on the next page and it can be copied into the plain text of a Secret. Note the ARN of the Secret after it has been created.

###### Use the AWS CLI

To accomplish this, you can use [`acm-pca create-certificate-authority`](../../../cli/latest/reference/acm-pca/create-certificate-authority.md "../../../cli/latest/reference/acm-pca/create-certificate-authority.md")
to create your private CA and then [`acm-pca issue-certificate`](../../../cli/latest/reference/acm-pca/issue-certificate.md "../../../cli/latest/reference/acm-pca/issue-certificate.md") to create the
private certificate. After creating the certificate, you can use [`acm get-certificate`](../../../cli/latest/reference/acm/get-certificate.md "../../../cli/latest/reference/acm/get-certificate.md")
to retrieve the certificate chain and then [`secrets-manager create-secret`](../../../cli/latest/reference/secretsmanager/create-secret.md "../../../cli/latest/reference/secretsmanager/create-secret.md")
to save that certificate chain as a Secret.

###### Use the AWS SDK

You can write either a custom resource or some separate stand-alone app using the AWS SDK. If you would like to use the AWS SDK for this, you can follow the instructions
for the AWS CLI. Each page of the CLI reference has a link titled "See also: AWS API Documentation" that will take you to the API documentation. There you will be able
to find the generic API information as well as links to all the language specific SDK’s.
