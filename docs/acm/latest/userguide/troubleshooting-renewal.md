

# Troubleshoot managed certificate renewal
<a name="troubleshooting-renewal"></a>

ACM tries to automatically renew your ACM certificates before they expire so that no action is required from you. Consult the following topics if you have trouble with [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md). 

## Preparing for automatic domain validation
<a name="troubleshooting-renewal-domain-validation"></a>

Before ACM can renew your certificates automatically, the following must be true:
+ Your certificate must be associated with an AWS service that is integrated with ACM. For information about the resources that ACM supports, see [Managed automation with integrated services](acm-services.md).
+ For email-validated certificates, ACM must be able to reach you at an administrator email address for each domain listed in your certificate. The email addresses that will be tried are listed in [AWS Certificate Manager email validation](email-validation.md).
+ For DNS-validated certificates, make sure that your DNS configuration contains the correct CNAME records as described in [AWS Certificate Manager DNS validation](dns-validation.md).
+ For HTTP-validated certificates, make sure that your redirects are configured as described in [AWS Certificate Manager HTTP validation](http-validation.md).

## Handling failures in managed certificate renewal
<a name="troubleshooting-automatic-renewal"></a>

As the certificate nears expiration (45 days for DNS, 45 for EMAIL and 60 days for Private), ACM attempts to renew the certificate if it meets the [eligibility criteria](managed-renewal.md). You might have to take actions for the renewal to succeed. For more information, see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md).

## Managed certificate renewal for email-validated certificates
<a name="troubleshooting-renewal-email-validation-failure"></a>

ACM certificates are valid for 198 days. Renewing a certificate requires action by the domain owner. ACM begins sending renewal notices to the email addresses associated with the domain 45 days before expiration. The notifications contain a link that the domain owner can click for renewal. Once all listed domains are validated, ACM issues a renewed certificate with the same ARN.

See [Validate with Email](email-validation.md) for instructions on identifying which domains are in the `PENDING_VALIDATION` state and repeating the validation process for those domains.

## Managed certificate renewal for DNS-validated certificates
<a name="troubleshooting-renewal-domain-validation-failure"></a>

ACM does not attempt TLS validation for DNS-validated certificates. If ACM fails to renew a certificate you validated with DNS validation, it is most likely due to missing or inaccurate CNAME records in your DNS configuration. If this occurs, ACM notifies you that the certificate could not be renewed automatically. 

**Important**  
You must insert the correct CNAME records into your DNS database. Consult your domain registrar about how to do this.

You can find the CNAME records for your domains by expanding your certificate and its domain entries in the ACM console. Refer to the figures below for details. You can also retrieve CNAME records by using the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) operation in the ACM API or the [describe-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm/describe-certificate.html) command in the ACM CLI. For more information, see [AWS Certificate Manager DNS validation](dns-validation.md).

![Select the target certificate from the console.](http://docs.aws.amazon.com/acm/latest/userguide/images/Dns-renewal-1.png)


![Expand the certificate window to find the certificate's CNAME information.](http://docs.aws.amazon.com/acm/latest/userguide/images/Dns-renewal-2.png)


If the problem persists, contact the [Support Center](https://console.aws.amazon.com/support).

## Managed certificate renewal for HTTP-validated certificates
<a name="troubleshooting-renewal-http-validation-failure"></a>

ACM attempts to renew HTTP-validated certificates automatically. If renewal fails, it's likely due to issues with the HTTP validation records. In such cases, ACM notifies you that the certificate couldn't be renewed automatically.

**Important**  
You must ensure that the content at the `RedirectFrom` location matches the content at the `RedirectTo` location for each domain in the certificate.

You can find the HTTP validation information for your domains by expanding your certificate and its domain entries in the ACM console. You can also retrieve this information using the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) operation in the ACM API or the [describe-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm/describe-certificate.html) command in the ACM CLI. For more information, see [AWS Certificate Manager HTTP validation](http-validation.md).

If the problem persists, contact the [Support Center](https://console.aws.amazon.com/support).

## Understanding renewal timing
<a name="troubleshooting-renewal-domain-async"></a>

[Managed certificate renewal in AWS Certificate Manager](managed-renewal.md) is an asynchronous process. This means that the steps don't occur in immediate succession. After all domain names in an ACM certificate have been validated, there might be a delay before ACM obtains the new certificate. An additional delay can occur between the time when ACM obtains the renewed certificate and the time when that certificate is deployed to the AWS resources that use it. Therefore, changes to the certificate status can take up to several hours to appear in the console. 