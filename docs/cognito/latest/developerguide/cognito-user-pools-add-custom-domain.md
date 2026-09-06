

# Using your own domain for managed login
<a name="cognito-user-pools-add-custom-domain"></a>

After you set up an app client, you can configure your user pool with a custom domain for the domain services of [managed login](cognito-user-pools-managed-login.md). With a custom domain, users can sign in to your application using your own web address instead the default `amazoncognito.com` [prefix domain](cognito-user-pools-assign-domain-prefix.md). Custom domains improve user trust in your application with a familiar domain name, especially when the root domain matches the domain that hosts your application. Custom domains can improve compliance with organizational security requirements.

A custom domain has some prerequisites, including a user pool, an app client, and a web domain that you own. Custom domains also require an SSL certificate for the custom domain, managed with AWS Certificate Manager (ACM) in US East (N. Virginia). Amazon Cognito creates a Amazon CloudFront distribution, secured in transit with your ACM certificate. Because you own the domain, you must create a DNS record that directs traffic to the CloudFront distribution for your custom domain.

After these elements are ready, you can add the custom domain to your user pool through the Amazon Cognito console or API. This involves specifying the domain name and SSL certificate, and then updating your DNS configuration with the provided alias target. After making these changes, you can verify that the sign-in page is accessible at your custom domain.

The lowest-effort way to create a custom domain is with a public hosted zone in Amazon Route 53. The Amazon Cognito console can create the right DNS records in a few steps. Before you begin, consider [creating a Route 53 hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) for a domain or subdomain that you own.

**Topics**
+ [Adding a custom domain to a user pool](#cognito-user-pools-add-custom-domain-adding)
+ [Prerequisites](#cognito-user-pools-add-custom-domain-prereq)
+ [Step 1: Enter your custom domain name](#cognito-user-pools-add-custom-domain-console-step-1)
+ [Step 2: Add an alias target and subdomain](#cognito-user-pools-add-custom-domain-console-step-2)
+ [Step 3: Verify your sign-in page](#cognito-user-pools-add-custom-domain-console-step-3)
+ [Changing the SSL certificate for your custom domain](#cognito-user-pools-add-custom-domain-changing-certificate)
+ [Setting the minimum TLS version for your custom domain](#cognito-user-pools-add-custom-domain-tls)

## Adding a custom domain to a user pool
<a name="cognito-user-pools-add-custom-domain-adding"></a>

To add a custom domain to your user pool, you specify the domain name in the Amazon Cognito console, and you provide a certificate you manage with [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/) (ACM). After you add your domain, Amazon Cognito provides an alias target, which you add to your DNS configuration.

## Prerequisites
<a name="cognito-user-pools-add-custom-domain-prereq"></a>

Before you begin, you need:
+ A user pool with an app client. For more information, see [Getting started with user pools](getting-started-user-pools.md).
+ A web domain that you own. Its *parent domain* must have a valid DNS **A record**. You can assign any value to this record. The parent may be the root of the domain, or a child domain that is one step up in the domain hierarchy. For example, if your custom domain is *auth.xyz.example.com*, Amazon Cognito must be able to resolve *xyz.example.com* to an IP address. To prevent accidental impact on customer infrastructure, Amazon Cognito doesn't support the use of top-level domains (TLDs) for custom domains. For more information see [Domain Names](https://tools.ietf.org/html/rfc1035).
+ The ability to create a subdomain for your custom domain. We recommend **auth** for your subdomain name. For example: {{auth.example.com}}.
**Note**  
You might need to obtain a new certificate for your custom domain's subdomain if you don't have a [wildcard certificate](https://en.wikipedia.org/wiki/Wildcard_certificate).
+ A public SSL/TLS certificate managed by ACM in US East (N. Virginia). The certificate must be in us-east-1 because the certificate will be associated with a distribution in CloudFront, a global service.
+ Browser clients that support Server Name Indication (SNI). The CloudFront distribution that Amazon Cognito assigns to custom domains requires SNI. You can't change this setting. For more information about SNI in CloudFront distributions, see [Use SNI to serve HTTPS requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-https-dedicated-ip-or-sni.html#cnames-https-sni) in the *Amazon CloudFront Developer Guide*.
+ An application that permits your user pool authorization server to add cookies to user sessions. Amazon Cognito sets several required cookies for managed login pages. These include `cognito`, `cognito-fl`, and `XSRF-TOKEN`. Although each individual cookie conforms to browser size limits, changes to your user pool configuration might cause managed login cookies to grow in size. An intermediate service like an Application Load Balancer (ALB) in front of your custom domain might enforce a maximum header size or total cookie size. If your application also sets its own cookies, your users' sessions might exceed these limits. We recommend that, to avoid size limit conflicts, your application not set cookies on the subdomain that hosts your user pool domain services.
+ Permission to update Amazon CloudFront distributions. You can do so by attaching the following IAM policy statement to a user in your AWS account:

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
           {
              "Sid": "AllowCloudFrontUpdateDistribution",
              "Effect": "Allow",
              "Action": [
                  "cloudfront:updateDistribution"
              ],
              "Resource": [
                  "*"
              ]
          }
      ]
  }
  ```

------

  For more information about authorizing actions in CloudFront, see [Using Identity-Based Policies (IAM Policies) for CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/access-control-managing-permissions.html).

  Amazon Cognito initially uses your IAM permissions to configure the CloudFront distribution, but the distribution is managed by AWS. You can't change the configuration of the CloudFront distribution that Amazon Cognito associated with your user pool. You can select the minimum TLS version for the distribution security policy when you create or update your custom domain with the Amazon Cognito API. For more information, see [Setting the minimum TLS version for your custom domain](#cognito-user-pools-add-custom-domain-tls).

## Step 1: Enter your custom domain name
<a name="cognito-user-pools-add-custom-domain-console-step-1"></a>

You can add your domain to your user pool by using the Amazon Cognito console or API.

------
#### [ Amazon Cognito console ]

**To add your domain to your user pool from the Amazon Cognito console:**

1. Navigate to the **Domain** menu under **Branding**.

1. Next to **Domain**, choose **Actions** and select **Create custom domain** or **Create Amazon Cognito domain**. If you have already configured a user pool custom domain, choose **Delete custom domain** before creating your new custom domain.

1. Next to **Domain**, choose **Actions** and select **Create custom domain**. If you have already configured a custom domain, choose **Delete custom domain** to delete the existing domain before creating your new custom domain.

1. For **Custom domain**, enter the URL of the domain you want to use with Amazon Cognito. Your domain name can include only lowercase letters, numbers, and hyphens. Do not use a hyphen for the first or last character. Use periods to separate subdomain names.

1. For **ACM certificate**, choose the SSL certificate that you want to use for your domain. Only ACM certificates in US East (N. Virginia) are eligible to use with an Amazon Cognito custom domain, regardless of the AWS Region of your user pool.

   If you don't have an available certificate, you can use ACM to provision one in US East (N. Virginia). For more information, see [Getting Started](https://docs.aws.amazon.com/acm/latest/userguide/gs.html) in the *AWS Certificate Manager User Guide*.

1. Choose a **Branding version**. Your branding version applies to all user-interactive pages at that domain. Your user pool can host either managed login or hosted UI branding for all app clients.
**Note**  
You can have a custom domain and a prefix domain, but Amazon Cognito only serves the `/.well-known/openid-configuration` endpoint for the *custom* domain.

1. Choose **Create**.

1. Amazon Cognito returns you to the **Domain** menu. A message titled **Create an alias record in your domain's DNS** is displayed. Note down the **Domain** and **Alias target** displayed in the console. They will be used in the next step to direct traffic to your custom domain.

------
#### [ API ]

The following [CreateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.html) request body creates a custom domain.

```
{
   "Domain": "auth.example.com",
   "UserPoolId": "us-east-1_EXAMPLE",
   "ManagedLoginVersion": 2,
   "CustomDomainConfig": {
    "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "SecurityPolicy": "TLS_V1_3_2025"
   }
}
```

The optional `SecurityPolicy` field sets the minimum TLS version for your custom domain. For more information, see [Setting the minimum TLS version for your custom domain](#cognito-user-pools-add-custom-domain-tls).

------

## Step 2: Add an alias target and subdomain
<a name="cognito-user-pools-add-custom-domain-console-step-2"></a>

In this step, you set up an alias through your Domain Name Server (DNS) service provider that points back to the alias target from the previous step. If you are using Amazon Route 53 for DNS address resolution, choose the section **To add an alias target and subdomain using Route 53.**

### To add an alias target and subdomain to your current DNS configuration
<a name="cognito-user-pools-add-custom-domain-console-step-2a"></a>
+ If you aren't using Route 53 for DNS address resolution, then you must use your DNS service provider's configuration tools to add the alias target from the previous step to your domain's DNS record. Your DNS provider will also need to set up the subdomain for your custom domain.

### To add an alias target and subdomain using Route 53
<a name="cognito-user-pools-add-custom-domain-console-step-2b"></a>

1. Sign in to the [Route 53 console](https://console.aws.amazon.com/route53/). If prompted, enter your AWS credentials.

1. If you don't have a public hosted zone in Route 53, create one with a root that is a parent of your custom domain. For more information, see [Creating a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in the *Amazon Route 53 Developer Guide*.

   1. Choose **Create Hosted Zone**.

   1. Enter the parent domain, for example {{auth.example.com}}, of your custom domain, for example {{myapp.auth.example.com}}, from the **Domain Name** list.

   1. Enter a **Description** for your hosted zone.

   1. Choose a hosted zone **Type** of **Public hosted zone** to allow public clients to resolve your custom domain. Choosing **Private hosted zone** is not supported.

   1. Apply **Tags** as desired.

   1. Choose **Create hosted zone**.
**Note**  
You can also create a new hosted zone for your custom domain with a delegation set in the parent hosted zone that directs queries to the subdomain hosted zone. Otherwise, create an A record. This method offers more flexibility and security with your hosted zones.For more information, see [Creating a subdomain for a domain hosted through Amazon Route 53](https://aws.amazon.com/premiumsupport/knowledge-center/create-subdomain-route-53/).

1. On the **Hosted Zones** page, choose the name of your hosted zone.

1. Add a DNS record for the parent domain of your custom domain, if you don’t already have one. Create a DNS record for the parent domain with the following properties:
   + **Record name**: Leave blank.
   + **Record type**: `A`.
   + **Alias**: Don't enable.
   + **Value**: Enter a target of your choosing. This record must resolve to *something*, but the value of the record doesn't matter to Amazon Cognito.
   + **TTL**: Set to your preferred TTL or leave as default.
   + **Routing policy**: Choose **Simple routing**.

1. Choose **Create records**. The following is an example record for the domain {{example.com}}:

   `{{example.com.}} 60 IN A {{198.51.100.1}}`
**Note**  
Amazon Cognito verifies that there is a DNS record for the parent domain of your custom domain to protect against accidental hijacking of production domains. If you do not have a DNS record for the parent domain, Amazon Cognito will return an error when you attempt to set the custom domain. A Start of Authority (SOA) record isn't a sufficient DNS record for the purposes of parent-domain verification.

1. Add another DNS record for your custom domain with the following properties:
   + **Record name**: Your custom domain prefix, for example `auth` to create a record for `auth.example.com`.
   + **Record type**: `A`.
   + **Alias**: Enable.
   + **Route traffic to**: Choose **Alias to Cloudfront distribution**. Enter the **Alias target** you recorded earlier, for example `123example.cloudfront.net`.
   + **Routing policy**: Choose **Simple routing**.

1. Choose **Create records**.
**Note**  
Your new records can take around 60 seconds to propagate to all Route 53 DNS servers. You can use the Route 53 [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) API method to verify that your changes have propagated. 

## Step 3: Verify your sign-in page
<a name="cognito-user-pools-add-custom-domain-console-step-3"></a>
+ Verify that the sign-in page is available from your custom domain.

  Sign in with your custom domain and subdomain by entering this address into your browser. This is an example URL of a custom domain {{example.com}} with the subdomain {{auth}}:

  ```
  https://{{myapp}}.{{auth}}.{{example.com}}/login?response_type=code&client_id={{<your_app_client_id>}}&redirect_uri={{<your_callback_url>}}
  ```

## Changing the SSL certificate for your custom domain
<a name="cognito-user-pools-add-custom-domain-changing-certificate"></a>

When necessary, you can use Amazon Cognito to change the certificate that you applied to your custom domain.

Usually, this is unnecessary following routine certificate renewal with ACM. When you renew your existing certificate in ACM, the ARN for your certificate remains the same, and your custom domain uses the new certificate automatically.

However, if you replace your existing certificate with a new one, ACM gives the new certificate a new ARN. To apply the new certificate to your custom domain, you must provide this ARN to Amazon Cognito.

After you provide your new certificate, Amazon Cognito requires up to 1 hour to distribute it to your custom domain.

**Before you begin**  
Before you can change your certificate in Amazon Cognito, you must add your certificate to ACM. For more information, see [Getting Started](https://docs.aws.amazon.com/acm/latest/userguide/gs.html) in the *AWS Certificate Manager User Guide*.  
When you add your certificate to ACM, you must choose US East (N. Virginia) as the AWS Region.

You can change your certificate by using the Amazon Cognito console or API.

------
#### [ AWS Management Console ]

**To renew a certificate from the Amazon Cognito console:**

1. Sign in to the AWS Management Console and open the Amazon Cognito console at [https://console.aws.amazon.com/cognito/home](https://console.aws.amazon.com/cognito/home).

1. Choose **User Pools**.

1. Choose the user pool for which you want to update the certificate.

1. Choose the **Domain** menu.

1. Choose **Actions**, **Edit ACM certificate**.

1. Select the new certificate you want to associate with your custom domain.

1. Choose **Save changes**.

------
#### [ API ]

**To renew a certificate (Amazon Cognito API)**
+ Use the [UpdateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html) action.

------

## Setting the minimum TLS version for your custom domain
<a name="cognito-user-pools-add-custom-domain-tls"></a>

When you create or update a custom domain with the Amazon Cognito console or API, you can select the minimum TLS version for the Amazon CloudFront distribution. The distribution uses this version when it communicates with clients. In the API, set the minimum TLS version in the `SecurityPolicy` field of the `CustomDomainConfig` object in a [CreateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.html) or [UpdateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html) request. The security policy defines the minimum TLS version and cipher suites that CloudFront supports when communicating with clients. For specific guidance, see [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html) in the *Amazon CloudFront Developer Guide*. You can select one of the following values.

**`TLS_V1_3_2025` (strictest)**  
A post-quantum-ready policy requiring TLS 1.3. It provides the strongest security posture and is ideal for workloads where all clients and browsers are updated to the latest versions. For more information, see [Supported protocols and ciphers for TLSv1.3\_2025](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).

**`TLS_V1_2_2021` (recommended)**  
A post-quantum-ready policy that prefers TLS 1.3 but allows fallback to TLS 1.2 to accommodate older clients. It is the recommended minimum for typical commercial-grade consumer applications. For more information, see [Supported protocols and ciphers for TLSv1.2\_2021](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).

**`TLS_V1` (strongly discouraged)**  
Permits fallback to TLS 1.0. It offers the broadest compatibility, including support for legacy clients that are more than a decade old. This compatibility comes at the expense of allowing TLS versions and cryptographic algorithms that are no longer considered safe for commercial use. For more information, see [Supported protocols and ciphers for TLSv1](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).

**Note**  
Custom domains that use managed login (branding version 2) require a minimum TLS version of `TLS_V1_2_2021` or higher. A request that sets `TLS_V1` for a managed login domain returns an `InvalidInputException` error.

You can select the minimum TLS version from the Amazon Cognito console, or with the Amazon Cognito API, the AWS Command Line Interface (AWS CLI), and the AWS SDKs.

The following [UpdateUserPoolDomain](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPoolDomain.html) request body updates the minimum TLS version of an existing custom domain.

```
{
   "Domain": "auth.example.com",
   "UserPoolId": "us-east-1_EXAMPLE",
   "ManagedLoginVersion": 2,
   "CustomDomainConfig": {
    "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "SecurityPolicy": "TLS_V1_3_2025"
   }
}
```