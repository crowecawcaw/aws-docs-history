# Delete certificates managed by AWS Certificate Manager

You can use the ACM console or the AWS CLI to delete a certificate. Deleting a ticket
is eventually consistent. A certificate may appear in lists for a short time after it's
deleted.

###### Important

- You cannot delete an ACM certificate that is being used by another AWS
  service. To delete a certificate that is in use, you must first remove the
  certificate association. This is done using the console or CLI _for the associated service_.
- Deleting a certificate issued by a private certificate authority (CA) has
  no effect on the CA. You will continue to be charged for the CA until it is
  deleted. For more information, see [Deleting Your Private CA](../../../privateca/latest/userguide/PCADeleteCA.md "../../../privateca/latest/userguide/PCADeleteCA.md") in the _AWS Private Certificate Authority User Guide_.

###### To delete a certificate using the console

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. In the list of certificates, select the check box for an ACM certificate,
   then choose **Delete**.

###### Note

Depending on how you have ordered the list, a certificate you are
looking for might not be immediately visible. You can click the
black triangle at right to change the ordering. You can also navigate
through multiple pages of certificates using the page numbers at
upper-right.
**To delete a certificate using the AWS CLI**

Use the [delete-certificate](../../../cli/latest/reference/acm/delete-certificate.md "../../../cli/latest/reference/acm/delete-certificate.md") command to delete a certificate, as shown in the
following command:

```
`$` **aws acm delete-certificate --certificate-arn arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID`**
```
