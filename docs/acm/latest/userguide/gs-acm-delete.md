

# Delete certificates managed by AWS Certificate Manager
<a name="gs-acm-delete"></a>

You can use the ACM console or the AWS CLI to delete a certificate. Deleting a ticket is eventually consistent. A certificate may appear in lists for a short time after it's deleted.

**Important**  
You cannot delete an ACM certificate that is being used by another AWS service. To delete a certificate that is in use, you must first remove the certificate association. This is done using the console or CLI *for the associated service*.
You can delete only *expired* certificates issued through ACME (certificates with a `CertificateKeyPairOrigin` of `ACME`). An ACME certificate remains in your account until one year after it expires, when ACM automatically removes it.
Deleting a certificate issued by a private certificate authority (CA) has no effect on the CA. You will continue to be charged for the CA until it is deleted. For more information, see [Deleting Your Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html) in the *AWS Private Certificate Authority User Guide*.

**To delete a certificate using the console**

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/).

1. In the list of certificates, select the check box for an ACM certificate, then choose **Delete**. 
**Note**  
Depending on how you have ordered the list, a certificate you are looking for might not be immediately visible. You can click the black triangle at right to change the ordering. You can also navigate through multiple pages of certificates using the page numbers at upper-right.

**To delete a certificate using the AWS CLI**

Use the [delete-certificate](https://docs.aws.amazon.com/cli/latest/reference/acm/delete-certificate.html) command to delete a certificate, as shown in the following command:

```
$ aws acm delete-certificate --certificate-arn arn:aws:acm:{{Region}}:{{444455556666}}:certificate/{{certificate_ID}}
```