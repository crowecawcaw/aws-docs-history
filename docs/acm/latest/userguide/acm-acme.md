# ACME certificate automation

AWS Certificate Manager (ACM) supports the Automated Certificate Management Environment (ACME) protocol, an
industry-standard method for automating certificate issuance and lifecycle management. With
ACME certificate automation, you can issue publicly trusted certificates for
workloads running on customer-managed infrastructure such as on-premises servers, Kubernetes
clusters, and hybrid environments.

###### Topics

- [What is ACME?](#acm-acme-what-is "#acm-acme-what-is")
- [How ACME works with ACM](#acm-acme-how-it-works "#acm-acme-how-it-works")
- [ACME certificate characteristics](#acm-acme-characteristics "#acm-acme-characteristics")
- [Working with ACME-issued certificates](#acm-acme-working-with "#acm-acme-working-with")
- [When to use ACME vs. RequestCertificate](#acm-acme-when-to-use "#acm-acme-when-to-use")
- [ACME persona model](#acm-acme-personas "#acm-acme-personas")
- [End-to-end workflow](#acm-acme-workflow "#acm-acme-workflow")
- [ACME endpoints](acm-acme-endpoints.md "acm-acme-endpoints.md")
- [ACME domain validation](acm-acme-domain-validation.md "acm-acme-domain-validation.md")
- [External account bindings](acm-acme-eab.md "acm-acme-eab.md")
- [Issuing certificates through ACME](acm-acme-issuance.md "acm-acme-issuance.md")

## What is ACME?

ACME is an internet protocol defined in RFC 8555 that automates certificate
issuance through machine-to-machine communication. Instead of manual certificate
requests, ACME clients communicate directly with an ACME server to
request and obtain certificates automatically.

ACME clients such as Certbot and cert-manager are widely available and
integrate with many application platforms. These clients handle the entire certificate
lifecycle, including initial issuance and renewal before expiration.

## How ACME works with ACM

ACM provides a managed ACME server that you access through ACME
endpoints. The architecture separates into two planes:

- **Control plane:** PKI administrators use
  ACM APIs to create ACME endpoints, configure domain validations, and
  generate external account binding (EAB) credentials.
- **Data plane:** ACME clients
  interact with the ACME protocol endpoint to register accounts and
  request certificates for domains that the administrator has already
  validated.

Unlike a typical public ACME service, where the client proves domain ownership
each time it requests a certificate, the ACM ACME server uses domains that an
administrator approves in advance. This separates the administrator who controls which
domains an endpoint can issue for from the application owners who request certificates.
For more information, see [ACME domain validation](acm-acme-domain-validation.md "acm-acme-domain-validation.md").

Certificates issued through ACME receive standard ACM ARNs and appear in
your ACM certificate inventory.

## ACME certificate characteristics

Certificates issued through ACME are publicly trusted ACM certificates.
They share the same trust chain, key algorithms, and certificate transparency logging
as other ACM public certificates. For information about the
characteristics that apply to all ACM public certificates, see [AWS Certificate Manager public certificate characteristics and limitations](acm-certificate-characteristics.md "acm-certificate-characteristics.md").

The following sections describe where ACME certificates differ from other
ACM public certificates.

### Revocation

Revoked end-entity certificates use OCSP and CRLs to verify and publish
revocation information. Some customer firewalls might need additional rules to
allow these mechanisms.

Use these URL wildcard patterns to identify revocation traffic:

- **OCSP**

`http://*.amazontrust.com`

- **CRL**

`http://*.amazontrust.com/*`

If more restrictive rules are needed, see the [Amazon Trust Services website](https://www.amazontrust.com/repository/crl-and-ocsp-endpoints "https://www.amazontrust.com/repository/crl-and-ocsp-endpoints").

### Certificate validity period

The validity period for ACME-issued certificates is 45 days, which is shorter
than the validity period for other ACM public certificates. This shorter validity is
offset by the fact that ACME clients renew certificates automatically. Using
short-lived certificates also positions you for upcoming industry changes, because public
certificate maximum validity periods are mandated to reduce over time and will be no
longer than 47 days by early 2029.

## Working with ACME-issued certificates

The following operational behaviors and constraints apply to ACME-issued
certificates as ACM resources:

- **Private key:** The private key is generated
  and held by the ACME client. ACM never sees the private key.
- **AWS integrated services:**
  ACME-issued certificates cannot be bound to [Managed automation with integrated services](acm-services.md "acm-services.md") such as Elastic Load Balancing, CloudFront,
  or API Gateway. Use the certificate on your managed infrastructure where the
  ACME client holds the private key.
- **Renewal:** The ACME client requests a
  new certificate before the existing one expires. ACM managed renewal does not
  apply.
- **Revocation:** Revocation is initiated by the
  ACME client through the ACME endpoint's `revoke-cert`
  URL.
- **Deletion:** You can delete expired ACME-issued certificates by calling `DeleteCertificate`. ACM automatically removes ACME-issued certificates one year after expiration.
- **Key pair origin:**
  `CertificateKeyPairOrigin` is `ACME` on
  `DescribeCertificate`, `ListCertificates`, and
  `SearchCertificates` responses.
- **Unsupported ACM APIs:**
  `ExportCertificate`, `RevokeCertificate`,
  `RenewCertificate`, and
  `ResendValidationEmail` are not supported for ACME-issued
  certificates. Lifecycle is managed by the ACME client.

## When to use ACME vs. RequestCertificate

Use the following guidance to determine which certificate issuance method fits your
use case.

**Use RequestCertificate when:**

- You need certificates for AWS integrated services (Elastic Load Balancing, CloudFront,
  API Gateway).
- You want ACM to manage the private key.
- You want ACM managed renewal.

**Use ACME when:**

- You want to use industry-standard ACME clients (Certbot,
  cert-manager).
- You need certificates for customer-managed infrastructure (on-premises,
  Kubernetes, hybrid).
- You need automated certificate lifecycle without AWS SDK
  dependencies.
- You must keep the private key on your own systems. For example, you might
  terminate TLS directly on your servers, or you might need to satisfy compliance
  or regulatory requirements that the private key never be held by a third
  party.

## ACME persona model

ACME certificate automation involves two roles:

PKI administrator

Creates and manages ACME endpoints, configures domain
validations, creates external account bindings, controls which domains can
issue certificates, sets up IAM roles, and monitors certificate issuance
through CloudWatch metrics and the ACM console.

Application owner

Receives EAB credentials from the administrator, uses an ACME
client to request certificates, and manages certificate renewal on their
systems.

## End-to-end workflow

The following steps describe the complete setup and usage flow for ACME
certificate automation:

1. The PKI administrator creates an ACME endpoint and receives an
   endpoint URL.
2. The administrator creates domain validations to pre-approve domains and
   provisions the required CNAME records.
3. The administrator creates external account bindings to generate credentials
   for ACME clients.
4. The administrator distributes EAB credentials to application owners.
5. The application owner configures an ACME client with the EAB
   credentials, registers an account, and requests certificates.
6. Issued certificates appear in ACM with standard ARNs.
7. The PKI administrator monitors issuance success and failure through CloudWatch
   metrics and the ACM console's certificates dashboard. For more information,
   see [Supported CloudWatch metrics](cloudwatch-metrics.md "cloudwatch-metrics.md").
