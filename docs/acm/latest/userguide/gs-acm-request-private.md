# Request a private certificate in AWS Certificate Manager

## Request a private certificate (console)

1. Sign into the AWS Management Console and open the ACM console at
   [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").

Choose **Request a certificate**. 2. On the **Request certificate** page, choose
**Request a private certificate** and
**Next** to continue. 3. In the **Certificate authority details** section,
select the **Certificate authority** menu and choose
one of the available private CAs. If the CA is shared from another
account, the ARN is prefaced by ownership information.

Details about the CA are displayed to help you verify that you have
chosen the correct one:

    * **Owner**
    * **Type**
    * **Common name (CN)**
    * **Organization (O)**
    * **Organization unit (OU)**
    * **Country name (C)**
    * **State or province**
    * **Locality name**

4. In the **Domain names** section, type your domain
   name. You can use a fully qualified domain name (FQDN), such as
   `www.example.com`, or a bare or apex domain
   name such as `example.com`. You can also use an
   asterisk (`*`) as a wild card in the leftmost
   position to protect several site names in the same domain. For example,
   `*.example.com` protects
   `corp.example.com`, and
   `images.example.com`. The wildcard name will
   appear in the **Subject** field and in the
   **Subject Alternative Name** extension of the ACM
   certificate.

###### Note

When you request a wildcard certificate, the asterisk
(`*`) must be in the leftmost position of
the domain name and can protect only one subdomain level. For
example, `*.example.com` can protect
`login.example.com`, and
`test.example.com`, but it cannot protect
`test.login.example.com`. Also note that
`*.example.com` protects
_only_ the subdomains of
`example.com`, it does not protect the bare
or apex domain (`example.com`). To protect
both, see the next step

Optionally, choose **Add another name to this
certificate** and type the name in the text box. This is
useful for authenticating both a bare or apex domain (such as
`example.com`) and its subdomains such as
`*.example.com`). 5. In the **Key algorithm** section, choose an
algorithm.

For information to help you choose an algorithm, see the AWS blog
post [How to evaluate and use ECDSA certificates in
AWS Certificate Manager](https://aws.amazon.com/blogs/security/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/ "https://aws.amazon.com/blogs/security/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/"). 6. In the **Tags** section, you can optionally tag your
certificate. Tags are key-value pairs that serve as metadata for
identifying and organizing AWS resources. For a list of ACM tag
parameters and for instructions on how to add tags to certificates after
creation, see [Tag AWS Certificate Manager resources](tags.md "tags.md"). 7. In the **Certificate renewal permissions** section,
acknowledge the notice about certificate renewal permissions. These
permissions allow automatic renewal of private PKI certificates that you
sign with the selected CA. For more information, see [Using a Service Linked Role with
ACM](acm-slr.md "acm-slr.md"). 8. After providing all of the required information, choose
**Request**. The console returns you to the
certificate list, where you can view your new certificate.

###### Note

Depending on how you have ordered the list, a certificate you are
looking for might not be immediately visible. You can click the
black triangle at right to change the ordering. You can also navigate
through multiple pages of certificates using the page numbers at
upper-right.

## Request a private certificate (CLI)

Use the [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md") command to request a private certificate in
ACM.

###### Note

When you request a private PKI certificate signed by a CA from AWS Private CA, the
specified signing algorithm family (RSA or ECDSA) must match the algorithm
family of the CA's secret key.

```
aws acm request-certificate \
--domain-name www.example.com \
--idempotency-token 12563 \
--certificate-authority-arn arn:aws:acm-pca:`Region`:`444455556666`:\
certificate-authority/`CA_ID`
```

This command outputs the Amazon Resource Name (ARN) of your new private
certificate.

```
{
    "CertificateArn": "arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID`"
}
```

In most cases, ACM automatically attaches a service-linked role (SLR) to
your account the first time that you use a shared CA. The SLR enables automatic
renewal of end-entity certificates that you issue. To check whether the SLR is
present, you can query IAM with the following command:

```
aws iam get-role --role-name AWSServiceRoleForCertificateManager
```

If the SLR is present, the command output should resemble the
following:

```
{
   "Role":{
      "Path":"/aws-service-role/acm.amazonaws.com/",
      "RoleName":"AWSServiceRoleForCertificateManager",
      "RoleId":"AAAAAAA0000000BBBBBBB",
      "Arn":"arn:aws:iam::{account_no}:role/aws-service-role/acm.amazonaws.com/AWSServiceRoleForCertificateManager",
      "CreateDate":"2020-08-01T23:10:41Z",
      "AssumeRolePolicyDocument":{
         "Version":"2012-10-17",
         "Statement":[
            {
               "Effect":"Allow",
               "Principal":{
                  "Service":"acm.amazonaws.com"
               },
               "Action":"sts:AssumeRole"
            }
         ]
      },
      "Description":"SLR for ACM Service for accessing cross-account Private CA",
      "MaxSessionDuration":3600,
      "RoleLastUsed":{
         "LastUsedDate":"2020-08-01T23:11:04Z",
         "Region":"ap-southeast-1"
      }
   }
}
```

If the SLR is missing, see [Using a
Service Linked Role with ACM](acm-slr.md "acm-slr.md").
