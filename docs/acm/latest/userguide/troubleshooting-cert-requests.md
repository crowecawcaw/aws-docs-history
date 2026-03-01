# Troubleshoot certificate requests

Consult the following topics if you encounter problems when requesting an ACM
certificate.

###### Topics

- [Certificate request times out](#troubleshooting-timed-out "#troubleshooting-timed-out")
- [Certificate request fails](#troubleshooting-failed "#troubleshooting-failed")

## Certificate request times out

Requests for ACM certificates time out if they are not validated within 72 hours. To
correct this condition, open the console, find the record for the certificate, click the
checkbox for it, choose **Actions**, and choose
**Delete**. Then choose **Actions** and **Request
a certificate** to begin again. For more information, see [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md") or [AWS Certificate Manager email validation](email-validation.md "email-validation.md"). We recommend that you use
DNS validation if possible.

## Certificate request fails

If your request fails ACM and you receive one of the following error messages, follow
the suggested steps to fix the problem. You cannot resubmit a failed certificate request –
after resolving the problem, submit a new request.

###### Topics

- [Error message: No Available Contacts](#failed-no-available-contacts "#failed-no-available-contacts")
- [Error message: Additional Verification Required](#failed-additional-verification-required "#failed-additional-verification-required")
- [Error message: Invalid Public Domain](#failed-invalid-domain "#failed-invalid-domain")
- [Error message: Other](#failed-other "#failed-other")

### Error message: No Available Contacts

You chose email validation when requesting a certificate, but ACM could not find an
email address to use for validating one or more of the domain names in the request. To
correct this problem, you can do one of the following:

- Ensure your domain is configured to receive email. Your domain's name server must
  have a mail exchanger record (MX record) so ACM's email servers know where to send
  the [domain validation email](email-validation.md "email-validation.md").

Accomplishing just one of the preceding tasks is enough to correct this problem; you
don't need to do both. After you correct the problem, request a new certificate.

For more information about how to ensure that you receive domain validation emails
from ACM, see [AWS Certificate Manager email validation](email-validation.md "email-validation.md") or
[Not receiving validation email](troubleshooting-email-validation.md#troubleshooting-no-mail "troubleshooting-email-validation.md#troubleshooting-no-mail"). If
you follow these steps and continue to get the **No Available Contacts**
message, then [report this to AWS](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home")
so that we can investigate it.

### Error message: Additional Verification Required

ACM requires additional information to process this certificate request. This
happens as a fraud-protection measure if your domain ranks within the [Alexa top 1000 websites](https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Alexa-Top-Sites/B07QK2XWNV "https://aws.amazon.com/marketplace/pp/Amazon-Web-Services-Alexa-Top-Sites/B07QK2XWNV"). To provide the required information, use the [Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") to contact Support. If you
don't have a support plan, post a new thread in the [ACM Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=206 "https://forums.aws.amazon.com/forum.jspa?forumID=206").

###### Note

You cannot request a certificate for Amazon-owned domain names such as those ending
in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.

### Error message: Invalid Public Domain

One or more of the domain names in the certificate request is not valid. Typically,
this is because a domain name in the request is not a valid top-level domain. Try again to
request a certificate, correcting any spelling errors or typos that were in the failed
request, and ensure that all domain names in the request are for valid top-level domains.
For example, you cannot request an ACM certificate for
`example.invalidpublicdomain` because "**invalidpublicdomain**" is not a valid top-level domain. If you continue to
receive this failure reason, contact the [Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home"). If you don't have a support plan, post a new thread in the
[ACM Discussion
Forum](https://forums.aws.amazon.com/forum.jspa?forumID=206 "https://forums.aws.amazon.com/forum.jspa?forumID=206").

### Error message: Other

Typically, this failure occurs when there is a typographical error in one or more of
the domain names in the certificate request. Try again to request a certificate,
correcting any spelling errors or typos that were in the failed request. If you continue
to receive this failure message, use the [Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") to contact Support. If you don't have a support plan, post a new
thread in the [ACM
Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=206 "https://forums.aws.amazon.com/forum.jspa?forumID=206").
