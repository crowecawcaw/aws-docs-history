# List certificates managed by AWS Certificate Manager

You can use the ACM console or AWS CLI to list the certificates managed by ACM. The
console can list up to 500 certificates in a page, and the CLI up to 1000.

###### To list your certificates using the console

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. Review the information in the certificate list. You can navigate through
   multiple pages of certificates using the page numbers at upper-right. Each
   certificate occupies a row with the following columns displayed by default for
   each certificate:

- **Domain name** – The fully qualified domain name
  (FQDN) for the certificate.
- **Type** – The type of certificate. Possible values
  are: **Amazon issued** | **Private** |
  **Imported**
- **Status** – Certificate status. Possible values are:
  **Pending validation** | **Issued** |
  **Inactive** | **Expired** |
  **Revoked** | **Failed** |
  **Validation timed out**
- **In use?** – Whether the ACM certificate is
  actively associated with an AWS service such as Elastic Load Balancing or CloudFront. The value can
  be **No** or **Yes**.
- **Renewal eligibility** – Whether the certificate can
  be renewed automatically by ACM when it approaches expiration. Possible values
  are: **Eligible** | **Ineligible**. For
  eligibility rules, see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md "managed-renewal.md").
  By choosing the settings icon in the upper-right corner of the console, you can
  customize the number of certificates shown on a page, specify the line-wrapping behavior
  of cell contents, and display additional information fields. The following optional
  fields are available:

- **Additional domain names** – One or more domain names
  (subject alternative names) included in the certificate.
- **Requested at** – The time when ACM requested the
  certificate.
- **Issued at** – The time when the certificate was
  issued. This information is available only for Amazon-issued certificates, not
  for imports.
- **Not before** – The time before which the certificate
  is not valid.
- **Not after** – The time after which the certificate
  is not valid.
- **Revoked at** – For revoked certificates, the time of
  the revocation.
- **Name tag** – The value of a tag on this certificate
  called _Name_, if such a tag exists.
- **Renewal status** – Status of the requested renewal
  of a certificate. This field is displayed and has a value only when renewal was
  requested. Possible values are: **Pending automatic renewal** |
  **Pending validation** | **Success** |
  **Failure**.

###### Note

It can take up to several hours for changes to the certificate status to
become available. If a problem is encountered, a certificate request times
out after 72 hours, and the issuance or renewal process must be repeated
from the beginning.
The **Page size** preference specifies the number of certificates
returned on each console page.

For more information about the available certificate details, see [View AWS Certificate Manager certificate details](gs-acm-describe.md "gs-acm-describe.md").

**To list your certificates using the AWS CLI**

Use the [list-certificates](../../../cli/latest/reference/acm/list-certificates.md "../../../cli/latest/reference/acm/list-certificates.md")
command to list your ACM-managed certificates as shown in the following
example:

```
`$` aws acm list-certificates --max-items `10`
```

The command returns information similar to the following:

```
{
    "CertificateSummaryList": [
        {
            "CertificateArn": "arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID`",
            "DomainName": "example.com"
		"SubjectAlternativeNameSummaries": [
                "example.com",
                "other.example.com"
            ],
            "HasAdditionalSubjectAlternativeNames": false,
            "Status": "ISSUED",
            "Type": "IMPORTED",
            "KeyAlgorithm": "RSA-2048",
            "KeyUsages": [
                "DIGITAL_SIGNATURE",
                "KEY_ENCIPHERMENT"
            ],
            "ExtendedKeyUsages": [
                "NONE"
            ],
            "InUse": false,
            "RenewalEligibility": "INELIGIBLE",
            "NotBefore": "2022-06-14T23:42:49+00:00",
            "NotAfter": "2032-06-11T23:42:49+00:00",
            "CreatedAt": "2022-08-25T19:28:05.531000+00:00",
            "ImportedAt": "2022-08-25T19:28:05.544000+00:00"
        },...
    ]
}
```

By default, only certificates with **keyTypes**
`RSA_1024` or `RSA_2048` and with at least one specified domain
are returned. To see other certificates that you control, such as domainless
certificates or certificates using a different algorithm or bit size, provide the
`--includes` parameter as shown in the following example. The parameter
allows you to specify a member of the [Filters](../APIReference/API_Filters.md "../APIReference/API_Filters.md") structure.

```
`$` aws acm list-certificates --max-items `10` --includes keyTypes=`RSA_4096`
```
