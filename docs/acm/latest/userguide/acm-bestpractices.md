# Best practices

Best practices are recommendations that can help you use AWS Certificate Manager (AWS Certificate Manager) more
effectively. The following best practices are based on real-world experience from
current ACM customers.

###### Topics

- [Account-level separation](#best-practices-account-separation "#best-practices-account-separation")
- [AWS CloudFormation](#best-practices-cloudformation "#best-practices-cloudformation")
- [Custom Trust Stores](#best-practices-custom-trust-stores "#best-practices-custom-trust-stores")
- [Certificate pinning](#best-practices-pinning "#best-practices-pinning")
- [Domain validation](#best-practices-validating "#best-practices-validating")
- [Adding or deleting domain names](#best-practices-add-delete "#best-practices-add-delete")
- [Domain name privacy](#best-practices-domain-name-privacy "#best-practices-domain-name-privacy")
- [Turn on AWS CloudTrail](#best-practices-ct "#best-practices-ct")

## Account-level separation

Use account-level separation in your policies to control who can access
certificates at an account level. Keep your production certificates in separate
accounts than your testing and development certificates. If you can't use
account-level separation, you can restrict access to specific roles by denying
`kms:CreateGrant` action in your policies. This limits which roles in
an account can sign certificates at a high level. For information about grants,
including grant terminology, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the
_AWS Key Management Service Developer Guide_.

If you want more granular control than restricting the use of
`kms:CreateGrant` by account, you can limit
`kms:CreateGrant` to specific certificates using [kms:EncryptionContext](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-encryption-context "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-encryption-context") condition keys. Specify `arn:aws:acm`
as the key, and the value of the ARN to restrict. The following example policy
prevents the use of a specific certificate, but allow others.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Deny",
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:aws:acm:arn": "arn:aws:acm:us-east-1:`111122223333`:certificate/b26def74-1234-4321-9876-951d4c07b197"
 }
 }
 }
 ]
}`

```

## AWS CloudFormation

With AWS CloudFormation you can create a template that describes the AWS resources that
you want to use. CloudFormation then provisions and configures those resources for you. CloudFormation
can provision resources that are supported by ACM such as Elastic Load Balancing, Amazon CloudFront, and
Amazon API Gateway. For more information, see [Managed automation with integrated services](acm-services.md "acm-services.md").

If you use CloudFormation to quickly create and delete multiple test environments, we
recommend that you do not create a separate ACM certificate for each environment.
Doing so will quickly exhaust your certificate quota. For more information, see
[Quotas](acm-limits.md "acm-limits.md"). Instead, create a
wildcard certificate that covers all of the domain names that you are using for
testing. For example, if you repeatedly create ACM certificates for domain names
that vary by only a version number, such as
`<version>``.service.example.com`,
create instead a single wildcard certificate for
`<*>``.service.example.com`.

###### Important

If you're using Amazon CloudFront distributions, note that HTTP validation doesn't
support wildcard certificates. When including wildcard certificates in your
CloudFormation templates for use with Amazon CloudFront, you must use either DNS validation or
email validation. We recommend DNS validation for automated renewal
capabilities.

Include the wildcard certificate in the template that CloudFormation uses to create your
test environment.

## Custom Trust Stores

In order to ensure connectivity to endpoints protected by ACM certificates, we
recommend the [Amazon roots](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/") be included in your custom trust store. Amazon Root
certificate authorities can represent different key types and algorithms. Starfield
Services Root Certificate Authority - G2 is an older root that is compatible with
other older trust stores and clients that can not be updated. By including all root
CAs, you'll be able to ensure maximum compatibility for your application.

## Certificate pinning

Certificate pinning, sometimes known as SSL pinning, is a process that you can use
in your application to validate a remote host by associating that host directly with
its X.509 certificate or public key instead of with a certificate hierarchy. The
application therefore uses pinning to bypass SSL/TLS certificate chain validation.
The typical SSL validation process checks signatures throughout the certificate
chain from the root certificate authority (CA) certificate through the subordinate
CA certificates, if any. It also checks the certificate for the remote host at the
bottom of the hierarchy. Your application can instead pin to the certificate for the
remote host to say that _only that_ certificate and not the root
certificate or any other in the chain is trusted. You can add the remote host's
certificate or public key to your application during development. Alternatively, the
application can add the certificate or key when it first connects to the
host.

###### Warning

We recommend that your application **not** pin an
ACM certificate. ACM performs [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md "managed-renewal.md") to automatically renew your Amazon-issued
SSL/TLS certificates before they expire. To renew a certificate, ACM generates
a new public-private key pair. If your application pins the ACM certificate
and the certificate is successfully renewed with a new public key, the
application might be unable to connect to your domain.

If you decide to pin a certificate, the following options will not hinder your
application from connecting to your domain:

- [Import your own
  certificate](import-certificate.md "import-certificate.md") into ACM and then pin your application to the
  imported certificate. ACM doesn't try to automatically renew imported
  certificates.
- If you're using a public certificate, pin your application to all
  available [Amazon root
  certificates](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/"). If you're using a private certificate, pin your
  application to the CA's root certificate.

## Domain validation

Before the Amazon certificate authority (CA) can issue a certificate for your
site, AWS Certificate Manager (ACM) must verify that you own or control all the domains that you
specified in your request. You can perform verification using either email or DNS.
For more information, see [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md") and [AWS Certificate Manager email validation](email-validation.md "email-validation.md").

## Adding or deleting domain names

You cannot add or remove domain names from an existing ACM certificate. Instead
you must request a new certificate with the revised list of domain names. For
example, if your certificate has five domain names and you want to add four more,
you must request a new certificate with all nine domain names. As with any new
certificate, you must validate ownership of all the domain names in the request,
including the names that you previously validated for the original certificate.

If you use email validation, you receive up to 8 validation email messages for
each domain, at least 1 of which must be acted upon within 72 hours. For example,
when you request a certificate with five domain names, you receive up to 40
validation messages, at least 5 of which must be acted upon within 72 hours. As the
number of domain names in the certificate request increases, so does the work
required to use email to validate domain ownership.

If you use DNS validation instead, you must write one new DNS record to the
database for the FQDN you want to validate. ACM sends you the record to create and
later queries the database to determine whether the record has been added. Adding
the record asserts that you own or control the domain. In the preceding example, if
you request a certificate with five domain names, you must create five DNS records.
We recommend that you use DNS validation when possible.

## Domain name privacy

Do not include confidential or sensitive information in public certificate
domain names. Public certificates, including ACM public certificates, are logged
to public, append-only Certificate Transparency logs. For more information, see [Certificate Transparency Logging](acm-concepts.md#concept-transparency "acm-concepts.md#concept-transparency").

## Turn on AWS CloudTrail

Turn on CloudTrail logging before you begin using ACM. CloudTrail enables you to monitor
your AWS deployments by retrieving a history of AWS API calls for your account,
including API calls made via the AWS Management Console, the AWS SDKs, the
AWS Command Line Interface, and higher-level Amazon Web Services. You can also identify which users and
accounts called the ACM APIs, the source IP address the calls were made from, and
when the calls occurred. You can integrate CloudTrail into applications using the API,
automate trail creation for your organization, check the status of your trails, and
control how administrators turn CloudTrail logging on and off. For more information, see
[Creating a
Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md"). Go to [Using CloudTrail with AWS Certificate Manager](cloudtrail.md "cloudtrail.md") to
see example trails for ACM actions.
