# Configuring custom domain names for GraphQL and real-time APIs

With AWS AppSync, you can use custom domain names to configure a single, memorable domain
that works for both your GraphQL and real-time APIs.

In other words, you can utilize simple and memorable endpoint URLs with domain names of
your choice by creating custom domain names that you associate with the AWS AppSync APIs in
your account.

When you configure an AWS AppSync API, two endpoints are provisioned:

**AWS AppSync GraphQL endpoint:**

`https://example1234567890000.appsync-api.us-east-1.amazonaws.com/graphql`

**AWS AppSync real-time endpoint:**

`wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql`

With custom domain names, you can interact with both endpoints using a single domain. For
example, if you configure `api.example.com` as your custom domain, you can
interact with both your GraphQL and real-time endpoints using these URLs:

**AWS AppSync custom domain GraphQL endpoint:**

`https://api.example.com/graphql`

**AWS AppSync custom domain real-time
endpoint:**

`wss://api.example.com/graphql/realtime`

###### Note

AWS AppSync APIs support only TLS 1.2 and TLS 1.3 for custom domain names.

## Registering and configuring a

domain name

To set up custom domain names for your AWS AppSync APIs, you must have a registered
internet domain name. You can register an internet domain using
Amazon Route 53 domain registration or a third-party domain registrar of your choice. For more
information about Route 53, see [What is Amazon Route 53?](../../../Route53/latest/DeveloperGuide.md "../../../Route53/latest/DeveloperGuide.md") in the
_Amazon Route 53 Developer Guide_.

An API's custom domain name can be the name of a subdomain or the root domain (also
known as the "zone apex") of a registered internet domain. After you create a custom
domain name in AWS AppSync, you must create or update your DNS provider's resource record
to map to your API endpoint. Without this mapping, API requests bound for the custom
domain name cannot reach AWS AppSync.

## Creating a custom domain name in

AWS AppSync

Creating a custom domain name for an AWS AppSync API sets up an
Amazon CloudFront distribution. You must set up a DNS record to map the custom
domain name to the CloudFront distribution domain name. This mapping is required to route API
requests that are bound for the custom domain name AWS AppSync through the mapped CloudFront
distribution. You must also provide a certificate for the custom domain name.

To set up the custom domain name or to update its certificate, you must have
permission to update CloudFront distributions and describe the AWS Certificate Manager (ACM) certificate
that you plan to use. To grant these permissions, attach the following AWS Identity and Access Management (IAM)
policy statement to an IAM user, group, or role in your account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUpdateDistributionForAppSyncCustomDomainName",
 "Effect": "Allow",
 "Action": [
 "cloudfront:updateDistribution"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowDescribeCertificateForAppSyncCustomDomainName",
 "Effect": "Allow",
 "Action": "acm:DescribeCertificate",
 "Resource": "arn:aws:acm:us-east-1:111122223333:certificate/certificate-id"
 }
 ]
}`

```

AWS AppSync supports custom domain names by leveraging Server Name Indication (SNI) on
the CloudFront distribution. For more information about using custom domain names on a CloudFront
distribution, including the required certificate format and the maximum certificate key
length, see [Using HTTPS with
CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/using-https.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https.md") in the _Amazon CloudFront Developer Guide_.

To set up a custom domain name as the API's hostname, the API owner must provide a public
or imported ACM certificate in the `us-east-1` _AWS Region (US East (N. Virginia))_ that covers the custom domain name. For more information about ACM, see [What is
AWS Certificate Manager?](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md") in the _AWS Certificate Manager User Guide_.

## Wildcard custom domain names in

AWS AppSync

AWS AppSync supports wildcard custom domain names. To configure a wildcard custom domain
name, specify a wildcard character (`*`) as the first subdomain of a custom
domain. This represents all possible subdomains of the root domain. For example, the
wildcard custom domain name `*.example.com` results in subdomains such as
`a.example.com`, `b.example.com`, and
`c.example.com`. All these subdomains route to the same domain.

To use a wildcard custom domain name in AWS AppSync, you must provide a certificate
issued by ACM containing a wildcard name that can protect several sites in the same
domain. For more information, see [ACM certificate
characteristics](../../../acm/latest/userguide/acm-certificate.md "../../../acm/latest/userguide/acm-certificate.md") in the _AWS Certificate Manager User Guide_.
