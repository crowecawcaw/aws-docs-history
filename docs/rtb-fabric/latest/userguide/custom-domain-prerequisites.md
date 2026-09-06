

# Prerequisites
<a name="custom-domain-prerequisites"></a>

Before you configure inbound external links with custom domains, verify that you meet the following prerequisites. For general setup requirements, see Setting up AWS RTB Fabric.

## Domain ownership
<a name="prereq-domain-ownership"></a>

You must own the domain that you want to use as a custom ingress endpoint. You need the ability to create and modify DNS records for the domain.

If the domain is registered with a third-party registrar, verify that you can create CNAME records either through the registrar's DNS management interface or through a DNS service such as Amazon Route 53.

## ACM certificate (HTTPS only)
<a name="prereq-acm-certificate"></a>

If you use HTTPS for your custom domain, you must have an AWS Certificate Manager (ACM) certificate that covers each custom domain you plan to use. You can either import an existing certificate or request a new one through ACM. If you use HTTP only, skip this prerequisite and the Certificate permissions prerequisite.

The certificate must meet the following requirements:
+ The certificate must be in **ISSUED** status in ACM. Certificates in other states (such as `PENDING_VALIDATION`) cannot be associated with a gateway.
+ The certificate's common name (CN) or subject alternative names (SANs) must include the custom domain hostname (exact or wildcard).
+ The certificate must be in the same AWS Region as the RTB Fabric gateway that will use it.
+ If you use a wildcard certificate (for example, `*.example.com`), it covers all single-level subdomains of that domain.

**Note**  
Each custom domain requires a certificate. If you use multiple custom domains that are not covered by a single wildcard certificate, you need a separate certificate for each domain.

When you associate the certificate with the gateway, RTB Fabric uses the CN and SANs for SNI-based certificate selection.

## RTB Fabric external gateway
<a name="prereq-gateway"></a>

You must have an existing RTB Fabric external responder gateway in each region where you want to receive custom domain traffic. Inbound external links with custom domains require an external gateway — standard (internal) gateways do not support certificate association or routing rules. The gateway must be in an active state.

If you need to accept both HTTP and HTTPS traffic, configure the gateway with a listener configuration that includes both protocols. See [Listener configuration](custom-domain-concepts.md#custom-domain-concept-listener-config).

If you serve traffic in multiple regions, you need an external gateway in each region. Each regional gateway is configured independently with its own certificates, routing rules, and listener configuration.

## Certificate permissions (HTTPS only)
<a name="prereq-certificate-permissions"></a>

When you associate an ACM certificate with your gateway using the `AssociateCertificate` API, RTB Fabric calls ACM on your behalf using forward access sessions (FAS) to establish a certificate relation. To enable this, you must add the following ACM permissions to the IAM identity (user or role) that you use to call `AssociateCertificate` API:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "ACMCertificatePermissions",
            "Effect": "Allow",
            "Action": [
                "acm:DescribeCertificate",
                "acm:CreateCertificateRelation"
            ],
            "Resource": "{{CERTIFICATE_ARN}}"
        }
    ]
}
```

Replace {{CERTIFICATE\_ARN}} with the ARN of your ACM certificate (for example, `arn:aws:acm:us-east-1:{{ACCOUNT_ID}}:certificate/abcd1234-5678-90ef-ghij-klmnopqrstuv`).

If you use HTTP only, skip this prerequisite.

## DNS access
<a name="prereq-dns-access"></a>

You must have the ability to create CNAME records for your custom domain. The CNAME record points your custom domain to the regional RTB Fabric gateway endpoint.

If you use Amazon Route 53, you can create the CNAME record in the hosted zone for your domain. If you use an external DNS provider, create the CNAME record through your provider's management interface.

Before creating the CNAME, verify the following:
+ You have the regional gateway endpoint hostname for each region you plan to use.
+ Your routing rules are configured and returning the expected `linkId`. Use the `/resolve-link` endpoint to test your URLs before updating DNS.
+ Your DNS provider supports CNAME records at the hostname level you need. CNAME records cannot be created at the zone apex (for example, `example.com` without a subdomain) per DNS specifications (RFC 1034). If your bid endpoint uses a zone apex hostname, use an ALIAS record in Route 53 or restructure to a subdomain-based endpoint.
+ If you plan to use weighted, latency-based, or geolocation routing for gradual migration, your DNS provider supports those record types.

**Warning**  
Creating the CNAME record immediately begins routing live traffic to RTB Fabric. Ensure that your routing rules, link configuration, and TLS certificates (if using HTTPS) are fully configured and tested before updating DNS. See Getting started with inbound external links with custom domains for the recommended setup sequence.