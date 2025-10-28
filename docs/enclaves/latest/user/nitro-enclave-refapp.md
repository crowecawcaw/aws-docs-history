# AWS Certificate Manager for Nitro Enclaves

AWS Certificate Manager (ACM) for Nitro Enclaves allows you to use public and private SSL/TLS certificates
with your web applications and web servers running on Amazon EC2 instances with AWS Nitro Enclaves.
SSL/TLS certificates are used to secure network communications and to establish the identity
of websites over the internet, as well as resources on private networks.

Previously, when running a web server on an EC2 instance, you would have created SSL
certificates and stored them as plaintext on your instance. With ACM for Nitro Enclaves, you
can now bind AWS Certificate Manager certificates to an enclave and use those certificates directly with
your web server, without exposing the certificates in plaintext form to the parent instance
and its users.

ACM for Nitro Enclaves removes the time-consuming and error-prone manual process of
purchasing, uploading, and renewing SSL/TLS certificates. ACM for Nitro Enclaves creates
secure private keys, distributes the certificate and its private key to your enclave, and
manages certificate renewals. With ACM for Nitro Enclaves, the certificate's private key
remains isolated in the enclave, preventing the instance, and its users, from accessing
it.

Currently, ACM for Nitro Enclaves works with [NGINX
servers](https://www.nginx.com/ "https://www.nginx.com/") and [Apache HTTP servers](https://httpd.apache.org/ "https://httpd.apache.org/")
running on Amazon EC2 instances to install the certificate and seamlessly replace expiring
certificates. Support for additional web servers will be added over time.

###### Note

ACM for Nitro Enclaves uses the standardized PKCS11 cryptographic interface between the
parent instance and the enclave. Any application that supports the PKCS11 protocol can
be adapted to use ACM for Nitro Enclaves for protecting certificates and keys.

ACM for Nitro Enclaves also includes a “helper” `p11-kit` based module for
using the PKCS11 protocol over the Nitro Enclaves vsock socket.

###### Contents

- [Pricing and billing](#acm-pricing "#acm-pricing")
- [Considerations](#acm-considerations "#acm-considerations")
- [Install ACM for Nitro Enclaves](install-acm.md "install-acm.md")
- [Update ACM for Nitro Enclaves](update-acm.md "update-acm.md")
- [Uninstall ACM for Nitro Enclaves](uninstall-acm.md "uninstall-acm.md")

## Pricing and billing

Public SSL/TLS certificates that you provision through ACM for Nitro Enclaves are
available at no additional cost. You pay only for the AWS resources that you create to
run your application, such as Amazon EC2 instances. Private certificates are available at no
additional cost per certificate when you use and pay for [ACM Private CA](https://aws.amazon.com/certificate-manager/pricing/ "https://aws.amazon.com/certificate-manager/pricing/").

## Considerations

The following considerations apply when using ACM for Nitro Enclaves:

- ACM for Nitro Enclaves only supports RSA certificates.
- ACM for Nitro Enclaves is available for Linux instances only. It is currently not
  supported on Windows instances.
- ACM for Nitro Enclaves is currently not supported in Asia Pacific (Osaka) and Asia
  Pacific (Jakarta).
