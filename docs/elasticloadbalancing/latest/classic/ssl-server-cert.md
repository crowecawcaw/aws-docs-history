# SSL/TLS certificates for Classic Load Balancers

If you use HTTPS (SSL or TLS) for your front-end listener, you must deploy an SSL/TLS
certificate on your load balancer. The load balancer uses the certificate to terminate
the connection and then decrypt requests from clients before sending them to the
instances.

The SSL and TLS protocols use an X.509 certificate (SSL/TLS server certificate) to
authenticate both the client and the back-end application. An X.509 certificate is a
digital form of identification issued by a certificate authority (CA) and contains
identification information, a validity period, a public key, a serial number, and the
digital signature of the issuer.

You can create a certificate using AWS Certificate Manager or a tool that supports the SSL and TLS
protocols, such as OpenSSL. You will specify this certificate when you create or update
an HTTPS listener for your load balancer. When you create a certificate for use with
your load balancer, you must specify a domain name.

When you create a certificate for use with your load balancer, you must specify a
domain name. The domain name on the certificate must match the custom domain name record.
If they do not match, the traffic will not be encrypted as the TLS connection cannot be verified.

You must specify a fully qualified domain name (FQDN) for your certificate, such as
`www.example.com` or an apex domain name such as `example.com`.
You can also use an asterisk (\*) as a wild card to protect several site names in the
same domain. When you request a wild-card certificate, the asterisk (\*) must be in the
leftmost position of the domain name and can protect only one subdomain level. For
instance, `*.example.com` protects `corp.example.com`, and
`images.example.com`, but it cannot protect `test.login.example.com`.
Also note that `*.example.com` protects only the subdomains of
`example.com`, it does not protect the bare or apex domain (`example.com`).
The wild-card name will appear in the **Subject** field and in the
**Subject Alternative Name** extension of the certificate. For more
information about public certificates, see [Requesting a public certificate](../../../acm/latest/userguide/gs-acm-request-public.md#request-public-console "../../../acm/latest/userguide/gs-acm-request-public.md#request-public-console") in the _AWS Certificate Manager User Guide_.

## Create or import an SSL/TLS certificate

using AWS Certificate Manager

We recommend that you use AWS Certificate Manager (ACM) to create or import certificates for
your load balancer. ACM integrates with ELB so that you can deploy the
certificate on your load balancer. To deploy a certificate on your load balancer,
the certificate must be in the same Region as the load balancer. For more
information, see [Request a
public certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md") or [Importing certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the
_AWS Certificate Manager User Guide_.

To allow a user to deploy the certificate on your load balancer using the
AWS Management Console, you must allow access to the ACM `ListCertificates` API
action. For more information, see [Listing
certificates](../../../acm/latest/userguide/security_iam_id-based-policy-examples.md#policy-list-certificates "../../../acm/latest/userguide/security_iam_id-based-policy-examples.md#policy-list-certificates") in the _AWS Certificate Manager User Guide_.

###### Important

You cannot install certificates with 4096-bit RSA keys or EC keys on your load
balancer through integration with ACM. You must upload certificates with
4096-bit RSA keys or EC keys to IAM in order to use them with your load
balancer.

## Import an SSL/TLS certificate using IAM

If you are not using ACM, you can use SSL/TLS tools, such as OpenSSL, to create
a certificate signing request (CSR), get the CSR signed by a CA to produce a
certificate, and upload the certificate to IAM. For more information, see
[Working with server
certificates](../../../IAM/latest/UserGuide/id_credentials_server-certs.md "../../../IAM/latest/UserGuide/id_credentials_server-certs.md") in the _IAM User Guide_.
