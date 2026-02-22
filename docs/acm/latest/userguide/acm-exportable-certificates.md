# AWS Certificate Manager exportable public certificates

AWS Certificate Manager exportable public certificates lets you provision, manage, and deploy [SSL/TLS certificates](acm-concepts.md#concept-sslcert "acm-concepts.md#concept-sslcert") anywhere - including Amazon EC2
instances, containers, and on-premises hosts. This feature extends ACM issued public
certificates beyond integrated AWS services, giving you centralized control over
certificates across your entire infrastructure.

## Benefits

The following outlines benefits of ACM exportable public certificates:

- _Simplified Certificate Management_: Centrally manage
  certificates for all your resources with ACM.
- _Faster Certificate Issuance_: Access and use certificates
  in less time.
- _Automated Renewals_: ACM automatically handles
  certificate renewals and notifies you when new certificates are ready for
  deployment. For more information, see [Amazon EventBridge support for ACM](supported-events.md "supported-events.md").
- _Cost Effective_: Pay only for the exportable public
  certificates you create.
- _Flexible Deployment_: Use certificates with any server or
  application that supports standard [SSL/TLS
  certificates](acm-concepts.md#concept-sslcert "acm-concepts.md#concept-sslcert").

## How ACM exportable public certificates

works

The following outlines how ACM exportable public certificates work:

1. Request an exportable certificate through ACM for your domain.
2. Validate domain ownership using DNS or email validation.
3. Export the certificate, private key, and certificate chain.
4. Deploy the certificate to your server or application.
5. ACM manages renewals and sends notifications when new certificates are
   available.

## Security considerations

The following are security considerations when using ACM exportable public certificates. For more
information, see [Data protection in AWS Certificate Manager](data-protection.md "data-protection.md").

- Protect exported private keys using secure storage and access controls.
- Use ACM's revocation feature if you suspect key compromise.
- Implement proper key rotation procedures when deploying renewed
  certificates.

## Limitations

The following are some ACM certificate limitations:

- Certificates have a 198 days validity period.
- ACM renews certificates set to expire 45 days before their expiration date.
- You must manage the deployment process for exported certificates.

## Pricing

You are subject to an additional charge for exportable public SSL/TLS certificates
that you create with AWS Certificate Manager. For the latest ACM pricing information, see the [AWS Certificate Manager Service
Pricing](https://aws.amazon.com//certificate-manager/pricing/ "https://aws.amazon.com//certificate-manager/pricing/") page on the AWS website.

## Best practices

The following are some best practices when using ACM certificates:

- Once a certificate is renewed, you should begin using it immediately.
- Test and implement automated deployment processes for renewed
  certificates.
- Monitor certificate deployments using [Amazon EventBridge metrics and alarms](supported-events.md "supported-events.md").
