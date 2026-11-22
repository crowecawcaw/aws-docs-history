

# Using a custom proxy hostname and certificate

By default, Network Firewall gives a NAT/Proxy firewall a hostname in the format `proxy-{{id}}.nfw.{{region}}.amazonaws.com`, and manages a public ACM certificate for it. The firewall presents this certificate to clients that connect to the HTTPS listener.

You can instead give the proxy your own hostname, such as `proxy.example.com`, and an AWS Certificate Manager (ACM) certificate for that hostname. The firewall presents your certificate to clients that connect to the HTTPS listener.

You set the custom hostname and certificate when you create the firewall. You can't add, change, or remove them afterward.

**Requirements**  
The custom hostname and certificate have the following requirements:
+ The certificate must be an ACM certificate in the same account and AWS Region as the firewall. You can request a public certificate or import a certificate. For information about requesting or importing a certificate, see [Requesting a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) and [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.
+ The certificate's subject alternative names must cover the hostname, either with an exact match or with a wildcard name such as `*.example.com`. A wildcard covers exactly one label.
+ The hostname must be a fully qualified domain name of 1–253 characters with at least two labels. It can't contain a wildcard, and it can't use the `proxy-{{id}}.nfw.{{region}}.amazonaws.com` format.
+ The firewall's VPC and any VPC where you create a VPC endpoint association for the firewall can't already have a private hosted zone with exactly the same name as the hostname.
+ The certificate is used only by the HTTPS listener. You can create the firewall without an HTTPS listener, but the certificate isn't used until you add one.

**How it works**  
Network Firewall creates and manages the Route 53 private hosted zones for your custom hostname, the same as it does for the default hostname. You don't need to configure DNS in the firewall's VPC or in VPCs with VPC endpoint associations. The firewall's endpoints report the custom hostname as their DNS name.

You manage the certificate in ACM. Network Firewall picks up ACM certificate renewals automatically. While the firewall uses the certificate, you can't delete the certificate in ACM.

**Important**  
Clients must trust the certificate authority (CA) that issued the certificate. Public ACM certificates are trusted by standard trust stores. If you import a certificate, or use a certificate issued by a private CA, configure your clients to trust that CA.

For the permissions that you need to use a custom certificate, see [Permissions for a NAT/Proxy firewall](nfw-proxy-permissions.md).