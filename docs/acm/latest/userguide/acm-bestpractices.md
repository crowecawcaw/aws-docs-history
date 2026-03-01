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
- [Opting out of certificate transparency logging](#best-practices-transparency "#best-practices-transparency")
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
Amazon API Gateway. For more information, see [Services integrated with ACM](acm-services.md "acm-services.md").

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

## Opting out of certificate transparency logging

###### Important

Regardless of the actions you take to opt out of certificate transparency
logging, your certificate might still be logged by any client or individual that
has access to the public or private endpoint to which you bind the certificate.
However, the certificate won't contain a signed certificate time stamp (SCT).
Only the issuing CA can embed an SCT in a certificate.

As of April 30 2018, Google Chrome no longer trusts public SSL/TLS certificates
that are not recorded in a certificate transparency log. Therefore, beginning April
24 2018, the Amazon CA began publishing all new certificates and renewals to at
least two public logs. Once a certificate has been logged, it cannot be removed. For
more information, see [Certificate Transparency Logging](acm-concepts.md#concept-transparency "acm-concepts.md#concept-transparency").

Logging is performed automatically when you request a certificate or when a
certificate is renewed, but you can choose to opt out. Common reasons for doing so
include concerns about security and privacy. For example, logging internal host
domain names gives potential attackers information about internal networks that
would otherwise not be public. In addition, logging could leak the names of new or
unreleased products and websites.

To opt out of transparency logging when you are requesting a certificate, use the
`options` parameter of the [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md")
AWS CLI command or the [RequestCertificate](../APIReference/API_RequestCertificate.md "../APIReference/API_RequestCertificate.md") API operation. If your certificate was issued before
April 24, 2018, and you want to make sure that it is not logged during renewal, you
can use the [update-certificate-options](../../../cli/latest/reference/acm/update-certificate-options.md "../../../cli/latest/reference/acm/update-certificate-options.md") command or the [UpdateCertificateOptions](../APIReference/API_UpdateCertificateOptions.md "../APIReference/API_UpdateCertificateOptions.md") API operation to opt out.

###### Limitations

- You cannot use the console to enable or disable transparency logging.
- You cannot change logging status after a certificate enters its renewal
  period, typically 45 days before certificate expiry for public certificates. No error message is
  generated if a status change fails.

Once a certificate has been logged, it cannot be removed from the log. Opting out
at that point will have no effect. If you opt out of logging when you request a
certificate and then choose later to opt back in, your certificate will not be
logged until it is renewed. If you want the certificate to be logged immediately, we
recommend that you issue a new one.

The following example shows you how to use the [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md")
command to disable certificate transparency when you request a new certificate.

```
aws acm request-certificate \
--domain-name `www.example.com` \
--validation-method DNS \
--options CertificateTransparencyLoggingPreference=DISABLED \
```

The preceding command outputs the ARN of your new certificate.

```
{
    "CertificateArn": "arn:aws:acm:`region`:`account`:certificate/`certificate_ID`"
}
```

If you already have a certificate, and you don't want it to be logged when it is
renewed, use the [update-certificate-options](../../../cli/latest/reference/acm/update-certificate-options.md "../../../cli/latest/reference/acm/update-certificate-options.md") command. This command does not return a
value.

```
aws acm update-certificate-options \
--certificate-arn arn:aws:acm:`region`:`account`:\
certificate/`certificate_ID` \
--options CertificateTransparencyLoggingPreference=DISABLED
```

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
