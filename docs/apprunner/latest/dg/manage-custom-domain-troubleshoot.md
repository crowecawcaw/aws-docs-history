

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Custom domain names
<a name="manage-custom-domain-troubleshoot"></a>

 This section covers how you can troubleshoot and resolve various errors that you might run into while linking to a custom domain. 

**Note**  
To augment the security of your App Runner applications, the *\*.awsapprunner.com* domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/). For further security, we recommend that you use cookies with a `__Host-` prefix if you ever need to set sensitive cookies in the default domain name for your App Runner applications. This practice will help to defend your domain against cross-site request forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes) page in the Mozilla Developer Network.

## Getting Create Fail error for custom domain
<a name="create-fail-error.troubleshoot"></a>
+ Check if this error is because of an issue with the CAA records. If there are no CAA records anywhere in the DNS tree, you receive a message `fail open`, and AWS Certificate Manager issues a certificate to verify the custom domain. This allows App Runner to accept the custom domain. If you're using CAA certifications in the DNS records, make sure that at least one domain's CAA records include `amazon.com`. Otherwise, ACM fails to issue a certificate. As a result, the custom domain for App Runner fails to be created. 

  The following example uses the DNS lookup tool *DiG* to show CAA records missing a required entry. The example uses `example.com` as the custom domain. Run the following commands in the example to check the CAA records.

  ```
  ...
  ;; QUESTION SECTION:
  ;example.com.           IN  CAA
  
  ;; ANSWER SECTION:
  example.com.        7200    IN  CAA 0 iodef "mailto:hostmaster@example.com"
  example.com.        7200    IN  CAA 0 issue "letsencrypt.org"
  ...note absence of "amazon.com" in any of the above CAA records...
  ```
+ Correct the domain records and ensure that at least one CAA record includes `amazon.com`. 
+ Retry to link the custom domain with App Runner. 

For instructions on how to resolve CAA errors, see the following:
+ [Certification Authority Authorization (CAA) problems](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-caa.html) 
+ [How do I resolve CAA errors for issuing or renewing an ACM certificate?](https://aws.amazon.com/premiumsupport/knowledge-center/acm-troubleshoot-caa-errors/) 

## Getting DNS certificate validation pending error for custom domain
<a name="DNS-certificate-validation-pending.troubleshoot"></a>
+ Check if you skipped an important step in the custom domain setup. Additionally check if you incorrectly configured a DNS record using a DNS lookup tool such as *DiG*. In particular, check for the following mistakes: 
  + Any missed steps.
  + Unsupported characters such as double quotations in the DNS records.
+ Correct the mistakes. 
+ Retry to link the custom domain with App Runner. 

For instructions on how to resolve CAA validation errors, see the following.
+ [DNS Validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) 
+ [Managing custom domain names for an App Runner service](manage-custom-domains.md) 

## Basic troubleshooting commands
<a name="Basic-troubleshooting-commands.troubleshoot"></a>
+ Confirm that a service can be found. 

  ```
            aws apprunner list-services
  ```
+ Describe a service and check its status. 

  ```
            aws apprunner describe-service --service-arn
  ```
+ Check status of custom domain. 

  ```
            aws apprunner describe-custom-domains --service-arn
  ```
+ List all operations in progress. 

  ```
            aws apprunner list-operations --service-arn
  ```

## Custom domain certificate renewal
<a name="certificate-renewal.troubleshoot"></a>

When you add a custom domain to your service, App Runner provides you with a set of CNAME records that you add to your DNS server. These CNAME records include certificate records. App Runner uses AWS Certificate Manager (ACM) to verify the domain. App Runner validates these DNS records to ensure continued ownership of this domain. If you remove the CNAME records from your DNS zone, App Runner can no longer validate the DNS records, and the custom domain certificate fails to renew automatically. 

This section covers how to resolve the following custom domain certificate renewal issues:
+  [The CNAME is removed from the DNS server](#cname-removed.troubleshoot). 
+ [The certificate has expired](#certificate-expired.troubleshoot). 

### The CNAME is removed from the DNS server
<a name="cname-removed.troubleshoot"></a>
+ Retrieve your CNAME records using the [DescribeCustomDomains](https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeCustomDomains.html) API or from the **Custom Domain** settings in the App Runner console. For information about stored CNAMEs, see [CertificateValidationRecords](https://docs.aws.amazon.com/apprunner/latest/api/API_CustomDomain.html#apprunner-Type-CustomDomain-CertificateValidationRecords).
+ Add the certificate validation CNAME records to your DNS server. App Runner can then validate that you own the domain. After you add the CNAME records, it can take up to 30 minutes for the DNS records to be propagated. It can also take several hours for App Runner and ACM to retry the certificate renewal process. For instructions on how to add CNAME records, see [Manage custom domains](manage-custom-domains.md#manage-custom-domains.manage). 

### The certificate has expired
<a name="certificate-expired.troubleshoot"></a>
+ Disassociate (unlink) and then associate (link) the custom domain for your App Runner service using the App Runner console or API. App Runner creates a new certificate validation CNAME records.
+ Add the new certificate validation CNAME records to your DNS server. 

  For instructions on how to disassociate (unlink) and associate (link) the custom domain, see [Manage custom domains](manage-custom-domains.md#manage-custom-domains.manage). 

### How do I verify that the certificate was successfully renewed
<a name="status-renewal.troubleshoot"></a>

You can check the status of your certificate records to verify your certificate was successfully renewed. You can check the status of the certificates by using tools like curl.

For more information about certificate renewal, see the following links:
+  [Why is my ACM certificate marked as ineligible for renewal?](https://aws.amazon.com/premiumsupport/knowledge-center/acm-certificate-ineligible/) 
+  [Managed renewal for ACM certificates ](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) 
+ [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html)