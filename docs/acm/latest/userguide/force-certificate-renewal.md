

# Force certificate renewal
<a name="force-certificate-renewal"></a>

You can renew your ACM public and private certificates with the ACM console, [renew-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html) AWS CLI, or [`RenewCertificate`](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewCertificate.html) API action. You can only renew certificates that have been previously exported.

**Important**  
When you renew an ACM exportable public certificates, you're charged an additional fee. For the latest ACM pricing information, see the [AWS Certificate Manager Service Pricing](https://aws.amazon.com/certificate-manager/pricing/) page on the AWS website.

## Renew a certificate (console)
<a name="renew-certificate-console"></a>

The following procedure walks you through how you can force the renewal of an ACM public or private certificate.

1. Sign in to the AWS Management Console and open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/).

1. Choose **List certificates** and select the checkbox of the certificate you want to renew.

   1. Alternatively, you can select the certificate. In the certificate detail page, select **Renew**.

1. Choose **More actions** and then choose **Renew**.

1. A dialog box appears where you must enter **renew**and then choose **Renew**.

## Renew a certificate (AWS CLI)
<a name="renew-certificate-cli"></a>

Use the [`renew-certificate`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html) AWS CLI command or [`RenewCertificate`](https://docs.aws.amazon.com/acm/latest/APIReference/API_RenewCertificate.html) API action to renew an ACM public or private certificate. You can retrieve the certificate's ARN by calling the [`list-certificates`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html) command. The `renew-certificate` command does not return a response.

```
$ aws acm renew-certificate \
    --certificate-arn arn:aws:acm:{{us-east-1}}:{{111122223333}}:certificate/{{12345678-1234-1234-1234-123456789012}}
```