

# Check a certificate's renewal status
<a name="check-certificate-renewal-status"></a>

When you have attempted to renew a certificate, ACM provides a *Renewal status* information field in the certificate details. You can use the AWS Certificate Manager console, the ACM API, the AWS CLI, or the Health Dashboard to check the renewal status of an ACM certificate. If you use the console, AWS CLI, or ACM API, the renewal status can have one of the four possible status values listed below. Similar values are displayed if you use the Health Dashboard. 

**Pending automatic renewal**  
ACM is attempting to automatically validate the domain names in the certificate. For more information, see [Renewal for domains validated by DNS](dns-renewal-validation.md). No further action is required. 

**Pending validation**  
ACM couldn't automatically validate one or more domain names in the certificate. You must take action to validate these domain names or the certificate won't be renewed. If you originally used email validation for the certificate, look for an email from ACM and then follow the link in that email to perform the validation. If you used DNS validation, check to make sure your DNS record exists and that your certificate remains in use.

**Success**  
All domain names in the certificate are validated, and ACM renewed the certificate. No further action is required.

**Failed**  
One or more domain names were not validated before the certificate expired, and ACM did not renew the certificate. You can [request a new certificate](gs-acm-request-public.md).

A certificate is eligible for renewal if it is associated with another AWS service, such as Elastic Load Balancing or CloudFront, or if it has been exported since being issued or last renewed.

**Note**  
It can take up to several hours for changes to the renewal status to become available. If a problem is encountered, the renewal request times out after 72 hours, and the renewal process must be repeated from the beginning. For troubleshooting help, see [Troubleshoot certificate requests](troubleshooting-cert-requests.md).

**Topics**
+ [Check the status (console)](#check-renewal-status-console)
+ [Check the status (API)](#check-renewal-status-api)
+ [Check the status (CLI)](#check-renewal-status-cli)
+ [Check the status using Personal Health Dashboard (PHD)](#check-renewal-status-phd)

## Check the status (console)
<a name="check-renewal-status-console"></a>

 The following procedure discusses how to use the ACM console to check the renewal status of an ACM certificate. 

1. Open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home).

1. Expand a certificate to view its details.

1. Find the **Renewal status** in the **Details** section. If you don't see the status, ACM hasn't started the managed renewal process for this certificate. 

## Check the status (API)
<a name="check-renewal-status-api"></a>

 For a Java example that shows how to use the [DescribeCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) action to check the status, see [Describing a certificate](sdk-describe.md). 

## Check the status (CLI)
<a name="check-renewal-status-cli"></a>

The following example shows how to check the status of your ACM certificate renewal with the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/). 

```
aws acm describe-certificate \ 
	--certificate-arn arn:aws:acm:{{region}}:{{account}}:certificate/{{certificate_ID}}
```

In the response, note the value in the `RenewalStatus` field. If you don't see the `RenewalStatus` field, ACM hasn't started the managed renewal process for your certificate. 

## Check the status using Personal Health Dashboard (PHD)
<a name="check-renewal-status-phd"></a>

ACM attempts to automatically renew your ACM certificate 45 days prior to expiration for public certificates and 60 days prior for private certificates. If ACM cannot automatically renew your certificate, it sends certificate renewal event notices to your Health Dashboard at 45 day (for private only), 30 day, 15 day, 7 day, 3 day, and 1 day intervals from expiration to inform you that you need to take action. The Health Dashboard is part of the AWS Health service. It requires no setup and can be viewed by any user that is authenticated in your account. For more information, see [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/). 

**Note**  
ACM writes successive renewal event notices to a single event in your PHD time line. Each notice overwrites the previous one until the renewal succeeds.

**To use the Health Dashboard:**

1. Log in to the Health Dashboard at [https://phd.aws.amazon.com/phd/home\#/](https://phd.aws.amazon.com/phd/home#/).

1. Choose **Event log**.

1. For **Filter by tags or attributes**, choose **Service**.

1. Choose **Certificate Manager**.

1. Choose **Apply**.

1. For **Event category** choose **Scheduled Change**.

1. Choose **Apply**.