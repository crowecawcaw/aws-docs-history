

# Search certificates managed by AWS Certificate Manager
<a name="gs-acm-list"></a>

With the ACM console or AWS CLI, you can search for certificates in your account. The [SearchCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_SearchCertificates.html) operation provides advanced filtering capabilities. You can filter certificates by ARN, X.509 attributes, and ACM specific properties like certificate status, type and renewal eligibility. You can also combine filters with AND, OR, and NOT logical operators.

**Note**  
The [ListCertificates](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html) operation still exists for basic listing with limited filtering options such as key type, key usage, certificate status, and certificate key pair origin.

You can filter certificates using the following categories:
+ **Certificate ARN** – Filter by the Amazon Resource Name of the certificate.
+ **X.509 attributes** – Filter by subject common name, subject alternative name, extended key usage, key usage, key algorithm, serial number, expiration date range (NotAfter), or validity start date range (NotBefore). Date range filters are inclusive of both the start and end dates. For example, to find all certificates for a specific domain, use the common name and DNS filters together with an OR operator.
+ **ACM metadata** – Filter by status, type, in-use, exported, export option, managed-by, validation method, renewal status, renewal eligibility, certificate key pair origin, ACME endpoint, or ACME account.

The certificate key pair origin filter accepts the values `AWS_MANAGED`, `CUSTOMER_PROVIDED`, and `ACME`. Certificates issued through ACME are returned only when you set the certificate key pair origin filter to `ACME`.

String filters support the CONTAINS and EQUALS comparison operators. You can combine multiple filters using AND, OR, and NOT logical operators.

You can sort results by the following fields:
+ `CREATED_AT`
+ `NOT_AFTER`
+ `STATUS`
+ `RENEWAL_STATUS`
+ `EXPORTED`
+ `IN_USE`
+ `NOT_BEFORE`
+ `KEY_ALGORITHM`
+ `TYPE`
+ `CERTIFICATE_ARN`
+ `COMMON_NAME`
+ `REVOKED_AT`
+ `RENEWAL_ELIGIBILITY`
+ `ISSUED_AT`
+ `MANAGED_BY`
+ `EXPORT_OPTION`
+ `VALIDATION_METHOD`
+ `IMPORTED_AT`

Sort order can be `ASCENDING` or `DESCENDING`.

Results are paginated. The `MaxResults` parameter defaults to 100 and accepts a maximum value of 500. Use the `NextToken` parameter to retrieve additional pages of results.

**To search your certificates using the console**

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/).

1. Use the property filter bar to search and filter certificates. You can filter by properties such as common name, status, type, key algorithm, and more. Combine filters with AND or OR operators to narrow your results.

1. Review the information in the certificate list. You can navigate through multiple pages of certificates by using the page numbers. Each certificate occupies a row. The following columns are displayed by default:
+ **Domain name** – The fully qualified domain name (FQDN) for the certificate.
+ **Type** – The type of certificate. Possible values are: **Amazon issued** \| **Private** \| **Imported**
+ **Status** – Certificate status. Possible values are: **Pending validation** \| **Issued** \| **Inactive** \| **Expired** \| **Revoked** \| **Failed** \| **Validation timed out**
+ **In use?** – Whether the ACM certificate is actively associated with an AWS service such as Elastic Load Balancing or CloudFront. The value can be **No** or **Yes**.
+ **Renewal eligibility** – Whether the certificate can be renewed automatically by ACM when it approaches expiration. Possible values are: **Eligible** \| **Ineligible**. For eligibility rules, see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md).

To customize the certificate list display, choose the settings icon. You can change the number of certificates shown on a page, specify the line-wrapping behavior of cell contents, and display additional information fields. The following optional fields are available:
+ **Additional domain names** – One or more domain names (subject alternative names) included in the certificate.
+ **Requested at** – The time when ACM requested the certificate.
+ **Issued at** – The time when the certificate was issued. This information is available only for Amazon-issued certificates, not for imports.
+ **Not before** – The time before which the certificate is not valid.
+ **Not after** – The time after which the certificate is not valid.
+ **Revoked at** – For revoked certificates, the time of the revocation. 
+ **Name tag** – The value of a tag on this certificate called *Name*, if such a tag exists.
+ **Renewal status** – Status of the requested renewal of a certificate. This field is displayed and has a value only when renewal was requested. Possible values are: **Pending automatic renewal** \| **Pending validation** \| **Success** \| **Failure**.
**Note**  
It can take up to several hours for changes to the certificate status to become available. If a problem is encountered, a certificate request times out after 72 hours, and the issuance or renewal process must be repeated from the beginning.

The **Page size** preference specifies the number of certificates returned on each console page.

For more information about the available certificate details, see [View AWS Certificate Manager certificate details](gs-acm-describe.md).

**To search your certificates using the AWS CLI**
+ Use the [search-certificates](https://docs.aws.amazon.com/cli/latest/reference/acm/search-certificates.html) command to search for ACM-managed certificates. The following example filters for certificates with a status of `ISSUED`:

  ```
  $ aws acm search-certificates \
      --filter-statement '{"Filter": {"AcmCertificateMetadataFilter": {"Status": "ISSUED"}}}' \
      --max-results 10
  ```

The command returns information similar to the following:

```
{
    "Results": [
        {
            "CertificateArn": "arn:aws:acm:{{Region}}:{{444455556666}}:certificate/{{certificate_ID}}",
            "X509Attributes": {
                "Issuer": {
                    "CommonName": "Example CA",
                    "Country": "US",
                    "Organization": "Example Corp"
                },
                "Subject": {
                    "CommonName": "example.com"
                },
                "SubjectAlternativeNames": [
                    {
                        "DnsName": "example.com"
                    },
                    {
                        "DnsName": "www.example.com"
                    }
                ],
                "ExtendedKeyUsages": [
                    "TLS_WEB_SERVER_AUTHENTICATION",
                    "TLS_WEB_CLIENT_AUTHENTICATION"
                ],
                "KeyAlgorithm": "RSA_2048",
                "KeyUsages": [
                    "DIGITAL_SIGNATURE",
                    "KEY_ENCIPHERMENT"
                ],
                "SerialNumber": "{{serial_number}}",
                "NotAfter": "2025-02-14T23:59:59+00:00",
                "NotBefore": "2024-01-15T00:00:00+00:00"
            },
            "CertificateMetadata": {
                "AcmCertificateMetadata": {
                    "CreatedAt": "2024-01-15T12:00:00+00:00",
                    "IssuedAt": "2024-01-15T12:05:00+00:00",
                    "Exported": false,
                    "InUse": true,
                    "RenewalEligibility": "ELIGIBLE",
                    "Status": "ISSUED",
                    "Type": "AMAZON_ISSUED",
                    "ValidationMethod": "DNS",
                    "CertificateKeyPairOrigin": "AWS_MANAGED"
                }
            }
        }
    ],
    "NextToken": "{{nextToken}}"
}
```