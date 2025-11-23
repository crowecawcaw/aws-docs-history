# SSL certificates for your Application Load Balancer

When you create a secure listener for your Application Load Balancer, you must deploy at least one
certificate on the load balancer. The load balancer requires X.509 certificates
(SSL/TLS server certificates). Certificates are a digital form of identification
issued by a certificate authority (CA). A certificate contains identification
information, a validity period, a public key, a serial number, and the digital
signature of the issuer.

When you create a certificate for use with your load balancer, you must specify a
domain name. The domain name on the certificate must match the custom domain name
record so that we can verify the TLS connection. If they do not match, the traffic
is not encrypted.

You must specify a fully qualified domain name (FQDN) for your certificate, such as
`www.example.com` or an apex domain name such as `example.com`.
You can also use an asterisk (\*) as a wild card to protect several site names in the
same domain. When you request a wild-card certificate, the asterisk (\*) must be in the
leftmost position of the domain name and can protect only one subdomain level. For
instance, `*.example.com` protects `corp.example.com`, and
`images.example.com`, but it cannot protect `test.login.example.com`.
Also note that `*.example.com` protects only the subdomains of
`example.com`, it does not protect the bare or apex domain (`example.com`).
The wild-card name appears in the **Subject** field and in the
**Subject Alternative Name** extension of the certificate. For more
information about public certificates, see [Request a public certificate](../../../acm/latest/userguide/acm-public-certificates.md "../../../acm/latest/userguide/acm-public-certificates.md") in the _AWS Certificate Manager User Guide_.

We recommend that you create certificates for your load balancer using [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/"). ACM
supports RSA certificates with 2048, 3072, and 4096-bit key lengths, and all ECDSA
certificates. ACM integrates with ELB so that you can deploy the certificate on
your load balancer. For more information, see the [AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md").

Alternatively, you can use SSL/TLS tools to create a certificate signing request
(CSR), then get the CSR signed by a CA to produce a certificate, then import the
certificate into ACM or upload the certificate to AWS Identity and Access Management (IAM). For more
information about importing certificates into ACM, see [Importing certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the
_AWS Certificate Manager User Guide_. For more information about uploading
certificates to IAM, see [Working with server
certificates](../../../IAM/latest/UserGuide/id_credentials_server-certs.md "../../../IAM/latest/UserGuide/id_credentials_server-certs.md") in the _IAM User Guide_.

## Default certificate

When you create an HTTPS listener, you must specify exactly one certificate.
This certificate is known as the _default certificate_. You
can replace the default certificate after you create the HTTPS listener. For
more information, see [Replace the default certificate](listener-update-certificates.md#replace-default-certificate "listener-update-certificates.md#replace-default-certificate").

If you specify additional certificates in a [certificate list](#sni-certificate-list "#sni-certificate-list"), the default
certificate is used only if a client connects without using the Server Name
Indication (SNI) protocol to specify a hostname or if there are no matching
certificates in the certificate list.

If you do not specify additional certificates but need to host multiple secure
applications through a single load balancer, you can use a wildcard certificate
or add a Subject Alternative Name (SAN) for each additional domain to your
certificate.

## Certificate list

After you create an HTTPS listener, you can add certificates to the certificate
list. If you created the listener using the AWS Management Console, we added the default
certificate to the certificate list for you. Otherwise, the certificate list is
empty. Using a certificate list enables the load balancer to support multiple domains
on the same port and provide a different certificate for each domain. For more
information, see [Add certificates to the certificate list](listener-update-certificates.md#add-certificates "listener-update-certificates.md#add-certificates").

The load balancer uses a smart certificate selection algorithm with support
for SNI. If the hostname provided by a client matches a single certificate in
the certificate list, the load balancer selects this certificate. If a hostname
provided by a client matches multiple certificates in the certificate list, the
load balancer selects the best certificate that the client can support.
Certificate selection is based on the following criteria in the following
order:

- Public key algorithm (prefer ECDSA over RSA)
- Expiration (prefer not expired)
- Hashing algorithm (prefer SHA over MD5). If there are multiple SHA certificates,
  prefer the highest SHA number.
- Key length (prefer the largest)
- Validity period

The load balancer access log entries indicate the hostname specified by the
client and the certificate presented to the client. For more information, see
[Access log entries](load-balancer-access-logs.md#access-log-entry-format "load-balancer-access-logs.md#access-log-entry-format").

## Certificate renewal

Each certificate comes with a validity period. You must ensure that you renew
or replace each certificate for your load balancer before its validity period
ends. This includes the default certificate and certificates in a certificate
list. Renewing or replacing a certificate does not affect in-flight requests
that were received by the load balancer node and are pending routing to a
healthy target. After a certificate is renewed, new requests use the renewed
certificate. After a certificate is replaced, new requests use the new
certificate.

You can manage certificate renewal and replacement as follows:

- Certificates provided by AWS Certificate Manager and deployed on your load balancer
  can be renewed automatically. ACM attempts to renew certificates
  before they expire. For more information, see [Managed renewal](../../../acm/latest/userguide/managed-renewal.md "../../../acm/latest/userguide/managed-renewal.md") in the
  _AWS Certificate Manager User Guide_.
- If you imported a certificate into ACM, you must monitor the
  expiration date of the certificate and renew it before it expires. For
  more information, see [Importing certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the
  _AWS Certificate Manager User Guide_.
- If you imported a certificate into IAM, you must create a new
  certificate, import the new certificate to ACM or IAM, add the new
  certificate to your load balancer, and remove the expired certificate
  from your load balancer.
