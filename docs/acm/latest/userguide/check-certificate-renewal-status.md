# Check a certificate's renewal

status

When you have attempted to renew a certificate, ACM provides a _Renewal status_ information field in the certificate
details. You can use the AWS Certificate Manager console, the ACM API, the AWS CLI, or the Health Dashboard to
check the renewal status of an ACM certificate. If you use the console, AWS CLI, or
ACM API, the renewal status can have one of the four possible status values listed
below. Similar values are displayed if you use the Health Dashboard.

**Pending automatic renewal**

ACM is attempting to automatically validate the domain names in the
certificate. For more information, see [Renewal for domains validated by
DNS](dns-renewal-validation.md "dns-renewal-validation.md"). No further action is required.

**Pending validation**

ACM couldn't automatically validate one or more domain names in the
certificate. You must take action to validate these domain names or the
certificate won't be renewed. If you originally used email validation for
the certificate, look for an email from ACM and then follow the link in
that email to perform the validation. If you used DNS validation, check to
make sure your DNS record exists and that your certificate remains in
use.

**Success**

All domain names in the certificate are validated, and ACM renewed the
certificate. No further action is required.

**Failed**

One or more domain names were not validated before the certificate
expired, and ACM did not renew the certificate. You can [request a new certificate](gs-acm-request-public.md "gs-acm-request-public.md").

A certificate is eligible for renewal if it is associated with another AWS service,
such as Elastic Load Balancing or CloudFront, or if it has been exported since being issued or last
renewed.

###### Note

It can take up to several hours for changes to the renewal status to become
available. If a problem is encountered, the renewal request times out after 72
hours, and the renewal process must be repeated from the beginning. For
troubleshooting help, see [Troubleshoot certificate requests](troubleshooting-cert-requests.md "troubleshooting-cert-requests.md").

###### Topics

- [Check the status (console)](#check-renewal-status-console "#check-renewal-status-console")
- [Check the status (API)](#check-renewal-status-api "#check-renewal-status-api")
- [Check the status (CLI)](#check-renewal-status-cli "#check-renewal-status-cli")
- [Check the status using Personal Health
  Dashboard (PHD)](#check-renewal-status-phd "#check-renewal-status-phd")

## Check the status (console)

The following procedure discusses how to use the ACM console to check the
renewal status of an ACM certificate.

1. Open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Expand a certificate to view its details.
3. Find the **Renewal status** in the
   **Details** section. If you don't see the status, ACM
   hasn't started the managed renewal process for this certificate.

## Check the status (API)

For a Java example that shows how to use the [DescribeCertificate](../APIReference/API_DescribeCertificate.md "../APIReference/API_DescribeCertificate.md")
action to check the status, see [Describing a certificate](sdk-describe.md "sdk-describe.md").

## Check the status (CLI)

The following example shows how to check the status of your ACM certificate
renewal with the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").

```
aws acm describe-certificate \
	--certificate-arn arn:aws:acm:`region`:`account`:certificate/`certificate_ID`
```

In the response, note the value in the `RenewalStatus` field. If you
don't see the `RenewalStatus` field, ACM hasn't started the managed
renewal process for your certificate.

## Check the status using Personal Health

Dashboard (PHD)

ACM attempts to automatically renew your ACM certificate 45 days prior to
expiration for public certificates and 60 days prior for private certificates. If ACM cannot automatically renew your certificate, it sends
certificate renewal event notices to your Health Dashboard at 45 day (for private only), 30 day, 15 day, 7 day, 3
day, and 1 day intervals from expiration to inform you that you need to take action.
The Health Dashboard is part of the AWS Health service. It requires no setup and can be
viewed by any user that is authenticated in your account. For more information, see
[AWS Health User Guide](../../../health/latest/ug.md "../../../health/latest/ug.md").

###### Note

ACM writes successive renewal event notices to a single event in your PHD
time line. Each notice overwrites the previous one until the renewal
succeeds.

###### To use the Health Dashboard:

1. Log in to the Health Dashboard at [https://phd.aws.amazon.com/phd/home#/](https://phd.aws.amazon.com/phd/home#/ "https://phd.aws.amazon.com/phd/home#/").
2. Choose **Event log**.
3. For **Filter by tags or attributes**, choose
   **Service**.
4. Choose **Certificate Manager**.
5. Choose **Apply**.
6. For **Event category** choose **Scheduled
   Change**.
7. Choose **Apply**.
