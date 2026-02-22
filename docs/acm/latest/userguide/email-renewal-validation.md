# Renewal for email-validated

domains

ACM certificates are valid for 198 days. Renewing a certificate requires action by the domain owner. ACM begins sending renewal notices to the email addresses associated with the domain 45 days before expiration. The notifications contain a link that the
domain owner can click for renewal. Once all listed domains are validated,
ACM issues a renewed certificate with the same ARN.

ACM sends AWS Health events and Amazon EventBridge events if it can't automatically
validate a domain during renewal. These events are sent at 30 days, 15
days, seven days, three days, and one day prior to expiration. For more information,
see [Amazon EventBridge support for ACM](supported-events.md "supported-events.md").

For more information about validation email messages, see [AWS Certificate Manager email validation](email-validation.md "email-validation.md")

To learn how you can respond programmatically to validation email, see [Automate AWS Certificate Manager email validation](email-automation.md "email-automation.md").

## Resend validation

email

After you configure email validation for your domain when you request a
certificate (see [AWS Certificate Manager email validation](email-validation.md "email-validation.md")), you can use the AWS Certificate Manager API to
request that ACM send you a domain validation email for your certificate
renewal. You should do this in the following circumstances:

- You used email validation when initially requesting your ACM
  certificate.
- Your certificate's renewal status is **pending
  validation**. For information about determining a
  certificate's renewal status, see [Check a certificate's renewal
  status](check-certificate-renewal-status.md "check-certificate-renewal-status.md").
- You didn't receive or can't find the original domain validation email
  message that ACM sent for certificate renewal.

To send validation emails to a different domain than what you originally
configured in your certificate request, you can use the [ResendValidationEmail](../APIReference/API_ResendValidationEmail.md "../APIReference/API_ResendValidationEmail.md") operation in the ACM API, AWS CLI, or AWS
SDKs. ACM will send emails to the specified validation domain. You can access
the AWS CLI in browser by using AWS CloudShell in supported Regions.

###### To request that ACM resend the domain validation email message

(console)

1. Open the AWS Certificate Manager console at [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Choose the **Certificate ID** of the certificate that
   requires validation.
3. Choose **Resend validation email**.

###### To request that ACM resend the domain validation email (ACM

API)

Use the [ResendValidationEmail](../APIReference/API_ResendValidationEmail.md "../APIReference/API_ResendValidationEmail.md") operation in the ACM API. In doing so,
pass the ARN of the certificate, the domain that requires manual validation,
and domain where you want to receive the domain validation emails. The
following example shows how to do this with the AWS CLI. This example contains
line breaks to make it easier to read.

```
$ aws acm resend-validation-email \
	--certificate-arn arn:aws:acm:`region`:`account`:certificate/`certificate_ID` \
	--domain `subdomain.example.com` \
	--validation-domain `example.com`
```
