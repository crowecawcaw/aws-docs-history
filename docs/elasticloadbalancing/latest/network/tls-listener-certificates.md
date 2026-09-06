

# Server certificates for your Network Load Balancer
<a name="tls-listener-certificates"></a>

When you create a secure listener for your Network Load Balancer, you must deploy at least one certificate on the load balancer. The load balancer requires X.509 certificates (server certificate). Certificates are a digital form of identification issued by a certificate authority (CA). A certificate contains identification information, a validity period, a public key, a serial number, and the digital signature of the issuer.

When you create a certificate for use with your load balancer, you must specify a domain name. The domain name on the certificate must match the custom domain name record so that we can verify the TLS connection. If they do not match, the traffic is not encrypted.

You must specify a fully qualified domain name (FQDN) for your certificate, such as `www.example.com` or an apex domain name such as `example.com`. You can also use an asterisk (\*) as a wild card to protect several site names in the same domain. When you request a wild-card certificate, the asterisk (\*) must be in the leftmost position of the domain name and can protect only one subdomain level. For instance, `*.example.com` protects `corp.example.com`, and `images.example.com`, but it cannot protect `test.login.example.com`. Also note that `*.example.com` protects only the subdomains of `example.com`, it does not protect the bare or apex domain (`example.com`). The wild-card name appears in the **Subject** field and in the **Subject Alternative Name** extension of the certificate. For more information about public certificates, see [Requesting a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html#request-public-console) in the *AWS Certificate Manager User Guide*.

We recommend that you create certificates for your load balancers using [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/). ACM integrates with Elastic Load Balancing so that you can deploy the certificate on your load balancer. For more information, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/).

Alternatively, you can use TLS tools to create a certificate signing request (CSR), then get the CSR signed by a CA to produce a certificate, then import the certificate into ACM or upload the certificate to AWS Identity and Access Management (IAM). For more information, see [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide* or [Working with server certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) in the *IAM User Guide*.

## Supported key algorithms
<a name="supported-key-algorithms"></a>
+ RSA 1024-bit
+ RSA 2048-bit
+ RSA 3072-bit
+ ECDSA 256-bit
+ ECDSA 384-bit
+ ECDSA 521-bit

If you import a certificate into AWS Identity and Access Management (IAM) and attach it to an NLB TLS listener, the certificate key size and algorithm are not validated at the time of attachment. Validation occurs asynchronously after the certificate is associated with the listener. If the certificate uses an unsupported key size (for example, RSA 4096-bit), the listener will enter a non-functional state and you will receive a notification via AWS Personal Health Dashboard (PHD).

Note that if your listener has a previously working certificate configured, traffic may continue to be served by that certificate while the unsupported certificate is rejected. The PHD notification will indicate that the listener is configured with an unsupported certificate but does not confirm whether traffic is still being served by a prior certificate.

To avoid this, verify the key size of your certificate before importing it into IAM. For RSA certificates, the maximum supported key size for NLB TLS listeners is 3072-bit.

If you use AWS Certificate Manager (ACM) to provision or import certificates, unsupported key sizes are rejected at the time of attachment, providing immediate feedback.

## Default certificate
<a name="default-certificate"></a>

When you create a TLS listener, you must specify at least one certificate. This certificate is known as the *default certificate*. You can replace the default certificate after you create the TLS listener. For more information, see [Replace the default certificate](listener-update-certificates.md#replace-default-certificate).

If you specify additional certificates in a [certificate list](#sni-certificate-list), the default certificate is used only if a client connects without using the Server Name Indication (SNI) protocol to specify a hostname or if there are no matching certificates in the certificate list.

If you do not specify additional certificates but need to host multiple secure applications through a single load balancer, you can use a wildcard certificate or add a Subject Alternative Name (SAN) for each additional domain to your certificate.

## Certificate list
<a name="sni-certificate-list"></a>

After you create a TLS listener, it has a default certificate and an empty certificate list. You can optionally add certificates to the certificate list for the listener. Using a certificate list enables the load balancer to support multiple domains on the same port and provide a different certificate for each domain. For more information, see [Add certificates to the certificate list](listener-update-certificates.md#add-certificates).

The load balancer uses a smart certificate selection algorithm with support for SNI. If the hostname provided by a client matches a single certificate in the certificate list, the load balancer selects this certificate. If a hostname provided by a client matches multiple certificates in the certificate list, the load balancer selects the best certificate that the client can support. Certificate selection is based on the following criteria in the following order:
+ Public key algorithm (prefer ECDSA over RSA)
+ Hashing algorithm (prefer SHA over MD5)
+ Key length (prefer the largest)
+ Validity period

The load balancer access log entries indicate the hostname specified by the client and the certificate presented to the client. For more information, see [Access log entries](load-balancer-access-logs.md#access-log-entry-format).

## Certificate renewal
<a name="ssl-certificate-renewal"></a>

Each certificate comes with a validity period. You must ensure that you renew or replace each certificate for your load balancer before its validity period ends. This includes the default certificate and certificates in a certificate list. Renewing or replacing a certificate does not affect in-flight requests that were received by the load balancer node and are pending routing to a healthy target. After a certificate is renewed, new requests use the renewed certificate. After a certificate is replaced, new requests use the new certificate.

You can manage certificate renewal and replacement as follows:
+ Certificates provided by AWS Certificate Manager and deployed on your load balancer can be renewed automatically. ACM attempts to renew certificates before they expire. For more information, see [Managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) in the *AWS Certificate Manager User Guide*.
+ If you imported a certificate into ACM, you must monitor the expiration date of the certificate and renew it before it expires. For more information, see [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.
+ If you imported a certificate into IAM, you must create a new certificate, import the new certificate to ACM or IAM, add the new certificate to your load balancer, and remove the expired certificate from your load balancer.