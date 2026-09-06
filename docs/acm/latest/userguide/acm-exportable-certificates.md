

# AWS Certificate Manager exportable public certificates
<a name="acm-exportable-certificates"></a>

AWS Certificate Manager exportable public certificates lets you provision, manage, and deploy [SSL/TLS certificates](acm-concepts.md#concept-sslcert) anywhere - including Amazon EC2 instances, containers, and on-premises hosts. This feature extends ACM issued public certificates beyond integrated AWS services, giving you centralized control over certificates across your entire infrastructure.

## Benefits
<a name="acm-exportable-certificates-benefits"></a>

The following outlines benefits of ACM exportable public certificates:
+ *Simplified Certificate Management*: Centrally manage certificates for all your resources with ACM.
+ *Faster Certificate Issuance*: Access and use certificates in less time.
+ *Automated Renewals*: ACM automatically handles certificate renewals and notifies you when new certificates are ready for deployment. For more information, see [Amazon EventBridge support for ACM](supported-events.md).
+ *Cost Effective*: Pay only for the exportable public certificates you create.
+ *Flexible Deployment*: Use certificates with any server or application that supports standard [SSL/TLS certificates](acm-concepts.md#concept-sslcert).

## How ACM exportable public certificates works
<a name="acm-exportable-certificates-how-it-works"></a>

The following outlines how ACM exportable public certificates work:

1. Request an exportable certificate through ACM for your domain.

1. Validate domain ownership using DNS or email validation.

1. Export the certificate, private key, and certificate chain.

1. Deploy the certificate to your server or application.

1. ACM manages renewals and sends notifications when new certificates are available.

## Security considerations
<a name="acm-exportable-certificates-security"></a>

The following are security considerations when using ACM exportable public certificates. For more information, see [Data protection in AWS Certificate Manager](data-protection.md).
+ Protect exported private keys using secure storage and access controls.
+ Use ACM's revocation feature if you suspect key compromise.
+ Implement proper key rotation procedures when deploying renewed certificates.

## Limitations
<a name="acm-exportable-certificates-limitations"></a>

The following are some ACM certificate limitations:
+ Certificates have a 198 days validity period.
+ ACM renews certificates set to expire 45 days before their expiration date.
+ You must manage the deployment process for exported certificates.

## Pricing
<a name="acm-exportable-certificates-pricing"></a>

You are subject to an additional charge for exportable public SSL/TLS certificates that you create with AWS Certificate Manager. For the latest ACM pricing information, see the [AWS Certificate Manager Service Pricing](https://aws.amazon.com/certificate-manager/pricing/) page on the AWS website.

## Best practices
<a name="acm-exportable-certificates-best-practices"></a>

The following are some best practices when using ACM certificates:
+ Once a certificate is renewed, you should begin using it immediately.
+ Test and implement automated deployment processes for renewed certificates.
+ Monitor certificate deployments using [Amazon EventBridge metrics and alarms](supported-events.md).