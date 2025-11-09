# Security Hub controls for Amazon CloudFront

These AWS Security Hub controls evaluate the Amazon CloudFront service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [CloudFront.1] CloudFront distributions should have a default

root object configured

**Related requirements:** NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16), PCI DSS v4.0.1/2.2.6

**Category:** Protect > Secure access management >
Resources not publicly accessible

**Severity:** High

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-default-root-object-configured](../../../config/latest/developerguide/cloudfront-default-root-object-configured.md "../../../config/latest/developerguide/cloudfront-default-root-object-configured.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon CloudFront distribution with S3 origins is configured to return a specific object that is the default root object.
The control fails if the CloudFront distribution uses S3 origins and doesn't have a default root object configured.
This control doesn't apply to CloudFront distributions that use custom origins.

A user might sometimes request the distribution's root URL instead of an object in the
distribution. When this happens, specifying a default root object can help you to avoid
exposing the contents of your web distribution.

### Remediation

To configure a default root object for a CloudFront distribution, see [How to specify a default root object](../../../AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.md#DefaultRootObjectHowToDefine "../../../AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.md#DefaultRootObjectHowToDefine") in the _Amazon CloudFront Developer Guide_.

## [CloudFront.3] CloudFront distributions should require

encryption in transit

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-viewer-policy-https](../../../config/latest/developerguide/cloudfront-viewer-policy-https.md "../../../config/latest/developerguide/cloudfront-viewer-policy-https.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon CloudFront distribution requires viewers to use HTTPS
directly or whether it uses redirection. The control fails if
`ViewerProtocolPolicy` is set to `allow-all` for
`defaultCacheBehavior` or for `cacheBehaviors`.

HTTPS (TLS) can be used to help prevent potential attackers from using
person-in-the-middle or similar attacks to eavesdrop on or manipulate network traffic.
Only encrypted connections over HTTPS (TLS) should be allowed. Encrypting data in
transit can affect performance. You should test your application with this feature to
understand the performance profile and the impact of TLS.

### Remediation

To encrypt a CloudFront distribution in transit, see [Requiring HTTPS for communication between viewers and CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md") in the
_Amazon CloudFront Developer Guide_.

## [CloudFront.4] CloudFront distributions should have origin

failover configured

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High
availability

**Severity:** Low

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-origin-failover-enabled](../../../config/latest/developerguide/cloudfront-origin-failover-enabled.md "../../../config/latest/developerguide/cloudfront-origin-failover-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon CloudFront distribution is configured with an origin
group that has two or more origins.

CloudFront origin failover can increase availability. Origin failover automatically
redirects traffic to a secondary origin if the primary origin is unavailable or if it
returns specific HTTP response status codes.

### Remediation

To configure origin failover for a CloudFront distribution, see [Creating an origin group](../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md#concept_origin_groups.creating "../../../AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.md#concept_origin_groups.creating") in the _Amazon CloudFront Developer Guide_.

## [CloudFront.5] CloudFront distributions should have logging

enabled

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5
AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5
AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8),
NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-accesslogs-enabled](../../../config/latest/developerguide/cloudfront-accesslogs-enabled.md "../../../config/latest/developerguide/cloudfront-accesslogs-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether server access logging is enabled on CloudFront distributions.
The control fails if access logging is not enabled for a distribution. This control only
evaluates whether standard logging (legacy) is enabled for a distribution.

CloudFront access logs provide detailed information about every user request that CloudFront
receives. Each log contains information such as the date and time the request was
received, the IP address of the viewer that made the request, the source of the request,
and the port number of the request from the viewer. These logs are useful for
applications such as security and access audits and forensics investigation. For more
information about analyzing access logs, see [Query Amazon CloudFront logs](../../../athena/latest/ug/cloudfront-logs.md "../../../athena/latest/ug/cloudfront-logs.md") in the
_Amazon Athena User Guide_.

### Remediation

To configure standard logging (legacy) for a CloudFront distribution, see [Configure standard logging (legacy)](../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging-legacy-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging-legacy-s3.md") in the _Amazon CloudFront Developer Guide_.

## [CloudFront.6] CloudFront distributions should have WAF

enabled

**Related requirements:** NIST.800-53.r5 AC-4(21),
PCI DSS v4.0.1/6.4.2

**Category:** Protect > Protective services

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-associated-with-waf](../../../config/latest/developerguide/cloudfront-associated-with-waf.md "../../../config/latest/developerguide/cloudfront-associated-with-waf.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether CloudFront distributions are associated with either AWS WAF
Classic or AWS WAF web ACLs. The control fails if the distribution is not associated with
a web ACL.

AWS WAF is a web application firewall that helps protect web applications and APIs
from attacks. It allows you to configure a set of rules, called a web access control
list (web ACL), that allow, block, or count web requests based on customizable web
security rules and conditions that you define. Ensure your CloudFront distribution is
associated with an AWS WAF web ACL to help protect it from malicious attacks.

### Remediation

To associate an AWS WAF web ACL with a CloudFront distribution, see [Using
AWS WAF to control access to your content](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.md") in the _Amazon CloudFront Developer Guide_.

## [CloudFront.7] CloudFront distributions should use custom

SSL/TLS certificates

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), NIST.800-171.r2 3.13.15

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-custom-ssl-certificate](../../../config/latest/developerguide/cloudfront-custom-ssl-certificate.md "../../../config/latest/developerguide/cloudfront-custom-ssl-certificate.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether CloudFront distributions are using the default SSL/TLS
certificate CloudFront provides. This control passes if the CloudFront distribution uses a custom
SSL/TLS certificate. This control fails if the CloudFront distribution uses the default
SSL/TLS certificate.

Custom SSL/TLS allow your users to access content by using alternate domain names.
You can store custom certificates in AWS Certificate Manager (recommended), or
in IAM.

### Remediation

To add an alternate domain name for a CloudFront distribution using a custom SSL/TLS
certificate, see [Adding an
alternate domain name](../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md#CreatingCNAME "../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md#CreatingCNAME") in the _Amazon CloudFront Developer Guide_.

## [CloudFront.8] CloudFront distributions should use SNI to serve

HTTPS requests

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2

**Category:** Protect > Secure network
configuration

**Severity:** Low

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-sni-enabled](../../../config/latest/developerguide/cloudfront-sni-enabled.md "../../../config/latest/developerguide/cloudfront-sni-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon CloudFront distributions are using a custom SSL/TLS certificate
and are configured to use SNI to serve HTTPS requests. This control fails if a custom
SSL/TLS certificate is associated but the SSL/TLS support method is a dedicated IP
address.

Server Name Indication (SNI) is an extension to the TLS protocol that is supported by
browsers and clients released after 2010. If you configure CloudFront to serve HTTPS requests
using SNI, CloudFront associates your alternate domain name with an IP address for each edge
location. When a viewer submits an HTTPS request for your content, DNS routes the
request to the IP address for the correct edge location. The IP address to your domain
name is determined during the SSL/TLS handshake negotiation; the IP address isn't
dedicated to your distribution.

### Remediation

To configure a CloudFront distribution to use SNI to serve HTTPS requests, see [Using SNI to Serve HTTPS Requests (works for Most Clients)](../../../AmazonCloudFront/latest/DeveloperGuide/cnames-https-dedicated-ip-or-sni.md#cnames-https-sni "../../../AmazonCloudFront/latest/DeveloperGuide/cnames-https-dedicated-ip-or-sni.md#cnames-https-sni") in the CloudFront
Developer Guide. For information about custom SSL certificates, see [Requirements for using SSL/TLS certificates with CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.md "../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.md").

## [CloudFront.9] CloudFront distributions should encrypt traffic

to custom origins

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-traffic-to-origin-encrypted](../../../config/latest/developerguide/cloudfront-traffic-to-origin-encrypted.md "../../../config/latest/developerguide/cloudfront-traffic-to-origin-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon CloudFront distributions are encrypting traffic to custom
origins. This control fails for a CloudFront distribution whose origin protocol policy allows
'http-only'. This control also fails if the distribution's origin protocol policy is
'match-viewer' while the viewer protocol policy is 'allow-all'.

HTTPS (TLS) can be used to help prevent eavesdropping or manipulation of network
traffic. Only encrypted connections over HTTPS (TLS) should be allowed.

### Remediation

To update the Origin Protocol Policy to require encryption for a CloudFront connection,
see [Requiring HTTPS for communication between CloudFront and your custom origin](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.md")
in the _Amazon CloudFront Developer Guide_.

## [CloudFront.10] CloudFront distributions should not use

deprecated SSL protocols between edge locations and custom origins

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5
SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.15,
PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-no-deprecated-ssl-protocols](../../../config/latest/developerguide/cloudfront-no-deprecated-ssl-protocols.md "../../../config/latest/developerguide/cloudfront-no-deprecated-ssl-protocols.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon CloudFront distributions are using deprecated SSL protocols for
HTTPS communication between CloudFront edge locations and your custom origins. This control
fails if a CloudFront distribution has a `CustomOriginConfig` where
`OriginSslProtocols` includes `SSLv3`.

In 2015, the Internet Engineering Task Force (IETF) officially announced that SSL 3.0
should be deprecated due to the protocol being insufficiently secure. It is recommended
that you use TLSv1.2 or later for HTTPS communication to your custom origins.

### Remediation

To update the Origin SSL Protocols for a CloudFront distribution, see [Requiring HTTPS for communication between CloudFront and your custom origin](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.md")
in the _Amazon CloudFront Developer Guide_.

## [CloudFront.12] CloudFront distributions should not point to

non-existent S3 origins

**Related requirements:** NIST.800-53.r5 CM-2,
NIST.800-53.r5 CM-2(2), PCI DSS v4.0.1/2.2.6

**Category:** Identify > Resource configuration

**Severity:** High

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-s3-origin-non-existent-bucket](../../../config/latest/developerguide/cloudfront-s3-origin-non-existent-bucket.md "../../../config/latest/developerguide/cloudfront-s3-origin-non-existent-bucket.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon CloudFront distributions are pointing to non-existent Amazon S3
origins. The control fails for a CloudFront distribution if the origin is configured to point
to a non-existent bucket. This control only applies to CloudFront distributions where an S3
bucket without static website hosting is the S3 origin.

When a CloudFront distribution in your account is configured to point to a non-existent
bucket, a malicious third party can create the referenced bucket and serve their own
content through your distribution. We recommend checking all origins regardless of
routing behavior to ensure that your distributions are pointing to appropriate origins.

### Remediation

To modify a CloudFront distribution to point to a new origin, see [Updating a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.md "../../../AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.md") in the
_Amazon CloudFront Developer Guide_.

## [CloudFront.13] CloudFront distributions should use origin

access control

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-s3-origin-access-control-enabled](../../../config/latest/developerguide/cloudfront-s3-origin-access-control-enabled.md "../../../config/latest/developerguide/cloudfront-s3-origin-access-control-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon CloudFront distribution with an Amazon S3 origin has origin
access control (OAC) configured. The control fails if OAC isn't configured for the CloudFront
distribution.

When using an S3 bucket as an origin for your CloudFront distribution, you can enable OAC.
This permits access to the content in the bucket only through the specified CloudFront
distribution, and prohibits access directly from the bucket or another distribution.
Although CloudFront supports Origin Access Identity (OAI), OAC offers additional
functionality, and distributions using OAI can migrate to OAC. While OAI provides a
secure way to access S3 origins, it has limitations, such as lack of support for
granular policy configurations and for HTTP/HTTPS requests that use the POST method in
AWS Regions that require AWS Signature Version 4 (SigV4). OAI also doesn't support
encryption with AWS Key Management Service. OAC is based on an AWS best practice of using IAM service
principals to authenticate with S3 origins.

### Remediation

To configure OAC for a CloudFront distribution with S3 origins, see [Restricting access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the
_Amazon CloudFront Developer Guide_.

## [CloudFront.14] CloudFront distributions should be

tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**`tagged-cloudfront-distribution`
(custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an Amazon CloudFront distribution has tags with the specific keys
defined in the parameter `requiredTagKeys`. The control fails if the
distribution doesn’t have any tag keys or if it doesn’t have all the keys specified in
the parameter `requiredTagKeys`. If the parameter
`requiredTagKeys` isn't provided, the control only checks for the
existence of a tag key and fails if the distribution isn't tagged with any key. System
tags, which are automatically applied and begin with `aws:`, are
ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an
optional value. You can create tags to categorize resources by purpose, owner,
environment, or other criteria. Tags can help you identify, organize, search for, and
filter resources. Tagging also helps you track accountable resource owners for actions
and notifications. When you use tagging, you can implement attribute-based access
control (ABAC) as an authorization strategy, which defines permissions based on tags.
You can attach tags to IAM entities (users or roles) and to AWS resources. You can
create a single ABAC policy or a separate set of policies for your IAM principals. You
can design these ABAC policies to allow operations when the principal's tag matches the
resource tag. For more information, see [What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or
sensitive information in tags. Tags are accessible to many AWS services, including
AWS Billing. For more tagging best practices, see [Tagging your
AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _AWS General Reference_.

### Remediation

To add tags to a CloudFront distribution, see [Tagging Amazon CloudFront
distributions](../../../AmazonCloudFront/latest/DeveloperGuide/tagging.md "../../../AmazonCloudFront/latest/DeveloperGuide/tagging.md") in the _Amazon CloudFront Developer Guide_.

## [CloudFront.15] CloudFront distributions should use the

recommended TLS security policy

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-ssl-policy-check](../../../config/latest/developerguide/cloudfront-ssl-policy-check.md "../../../config/latest/developerguide/cloudfront-ssl-policy-check.md")

**Schedule type:** Change triggered

**Parameters:**
`securityPolicies`: `TLSv1.2_2021,TLSv1.2_2025,TLSv1.3_2025` (not customizable)

This control checks whether an Amazon CloudFront distribution is configured to use a
recommended TLS security policy. The control fails if the CloudFront distribution is not
configured to use a recommended TLS security policy.

If you configure an Amazon CloudFront distribution to require viewers to use HTTPS to access
content, you have to choose a security policy and specify the minimum SSL/TLS protocol
version to use. This determines which protocol version CloudFront uses to communicate with
viewers, and the ciphers that CloudFront uses to encrypt the communications. We recommend
using the latest security policy that CloudFront provides. This ensures that CloudFront uses the
latest cipher suites to encrypt data in transit between a viewer and a CloudFront
distribution.

###### Note

This control generates findings only for CloudFront distributions that are configured to
use custom SSL certificates and are not configured to support legacy clients.

### Remediation

For information about configuring the security policy for a CloudFront distribution, see
[Update
a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.md "../../../AmazonCloudFront/latest/DeveloperGuide/HowToUpdateDistribution.md") in the _Amazon CloudFront Developer
Guide_. When you configure the security policy for a distribution,
choose the latest security policy.

## [CloudFront.16] CloudFront distributions should use origin

access control for Lambda function URL origins

**Category:** Protect > Secure access management > Access control

**Severity:** Medium

**Resource type:**
`AWS::CloudFront::Distribution`

**AWS Config rule:**
[cloudfront-origin-lambda-url-oac-enabled](../../../config/latest/developerguide/cloudfront-origin-lambda-url-oac-enabled.md "../../../config/latest/developerguide/cloudfront-origin-lambda-url-oac-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon CloudFront distribution with an AWS Lambda function URL as
an origin has origin access control (OAC) enabled. The control fails if the CloudFront
distribution has a Lambda function URL as an origin and OAC isn't enabled.

An AWS Lambda function URL is a dedicated HTTPS endpoint for a Lambda function. If a
Lambda function URL is the origin for a CloudFront distribution, the function URL must be
publicly accessible. Therefore, as a security best practice, you should create an OAC
and add it to the Lambda function URL in a distribution. OAC uses IAM service
principals to authenticate requests between CloudFront and the function URL. It also supports
the use of resource-based policies to allow invocation of a function only if a request
is on behalf of a CloudFront distribution specified in the policy.

### Remediation

For information about configuring OAC for an Amazon CloudFront distribution that uses a
Lambda function URL as an origin, see [Restrict access to an AWS Lambda function URL origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-lambda.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-lambda.md") in the _Amazon CloudFront Developer Guide_.
