# View AWS Certificate Manager certificate details

You can use the ACM console or the AWS CLI to list detailed metadata about your
certificates.

###### To view certificate details in the console

1.  Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/") to display your certificates. You can
    navigate through multiple pages of certificates using the page numbers at
    upper-right.
2.  To show detailed metadata for a listed certificate, choose the Certificate ID.
    A page opens, displaying the following information:

        * **Certificate status**




        	+ **Identifier** – 32-byte hexadecimal
        	 unique identifier of the certificate
        	+ **ARN** – An Amazon Resource Name
        	 (ARN) in the form
        	 `arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID``
        	+ **Type** – Identifies the
        	 management category of an ACM certificate. Possible values
        	 are: **Amazon Issued** |
        	 **Private** |
        	 **Imported**. For more information, see [AWS Certificate Manager public certificates](gs-acm-request-public.md "gs-acm-request-public.md"), [Request a private certificate in AWS Certificate Manager](gs-acm-request-private.md "gs-acm-request-private.md"), or [Import certificates into AWS Certificate Manager](import-certificate.md "import-certificate.md").
        	+ **Status** – The certificate status.
        	 Possible values are: **Pending validation** |
        	 **Issued** | **Inactive**
        	 | **Expired** | **Revoked** |
        	 **Failed** | **Validation timed
        	 out**
        	+ **Detailed status** – Date and time
        	 when the certificate was issued or imported
        * **Domains**




        	+ **Domain** – The fully qualified
        	 domain name (FQDN) for the certificate.
        	+ **Status** – The domain validation
        	 status. Possible values are: **Pending
        	 validation** | **Revoked** |
        	 **Failed** | **Validation timed
        	 out** | **Success**
        * **Details**




        	+ **In use?** – Whether the certificate
        	 is associated with an [AWS
        	 integrated service](acm-services.md "acm-services.md") Possible values are:
        	 **Yes** | **No**
        	+ **Domain name** – The first fully
        	 qualified domain name (FQDN) for the certificate.
        	+ **Managed by** – Identifies the AWS
        	 service that manages the certificate with ACM.
        	+ **Number of additional names** –
        	 Number of domain names for which the certificate is valid
        	+ **Serial number** – 16-byte
        	 hexadecimal serial number of the certificate
        	+ **Public key info** – The
        	 cryptographic algorithm that generated the key pair
        	+ **Signature algorithm** – The
        	 cryptographic algorithm used to sign the certificate.
        	+ **Can be used with** – A list of ACM
        	 [integrated
        	 services](acm-services.md "acm-services.md") that support a certificate with these
        	 parameters
        	+ **Requested at** – Date and time of
        	 issuance request
        	+ **Issued at** – If applicable, the
        	 date and time of issuance
        	+ **Imported at** – If applicable, the
        	 date and time of import
        	+ **Not before** – The start of the
        	 validity period of the certificate
        	+ **Not after** – The expiration date
        	 and time of the certificate
        	+ **Renewal eligibility** – Possible
        	 values are: **Eligible** |
        	 **Ineligible**. For eligibility rules, see
        	 [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md "managed-renewal.md").
        	+ **Renewal status** – Status of the
        	 requested renewal of a certificate. This field is displayed and
        	 has a value only when renewal was requested. Possible values
        	 are: **Pending automatic renewal** |
        	 **Pending validation** |
        	 **Success** |
        	 **Failure**.


        	###### Note

        	It can take up to several hours for changes to the
        	 certificate status to become available. If a problem is
        	 encountered, a certificate request times out after 72 hours,
        	 and the issuance or renewal process must be repeated from
        	 the beginning.
        	+ **CA** – The ARN of the signing
        	 CA
        * **Tags**




        	+ **Key**
        	+ **Value**
        * **Validation state** – If applicable, possible
         values are:




        	+ **Pending** – Validation has been
        	 requested and has not completed.
        	+ **Validation timed out** – A requested
        	 validation timed out, but you can repeat the request.
        	+ **None** – The certificate is for a
        	 private PKI or is self-signed, and does not need validation.

    **To view certificate details using the AWS CLI**

Use the [describe-certificate](../../../cli/latest/reference/acm/describe-certificate.md "../../../cli/latest/reference/acm/describe-certificate.md") in the AWS CLI to display certificate details, as shown
in the following command:

```
`$` **aws acm describe-certificate --certificate-arn arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID`**
```

The command returns information similar to the following:

```
{
    "Certificate": {
        "CertificateArn": "arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID`",
        "Status": "EXPIRED",
        "Options": {
            "CertificateTransparencyLoggingPreference": "ENABLED"
        },
        "SubjectAlternativeNames": [
            "example.com",
            "www.example.com"
        ],
        "DomainName": "gregpe.com",
        "NotBefore": 1450137600.0,
        "RenewalEligibility": "INELIGIBLE",
        "NotAfter": 1484481600.0,
        "KeyAlgorithm": "RSA-2048",
        "InUseBy": [
            "arn:aws:cloudfront::`account`:distribution/E12KXPQHVLSYVC"
        ],
        "SignatureAlgorithm": "SHA256WITHRSA",
        "CreatedAt": 1450212224.0,
        "IssuedAt": 1450212292.0,
        "KeyUsages": [
            {
                "Name": "DIGITAL_SIGNATURE"
            },
            {
                "Name": "KEY_ENCIPHERMENT"
            }
        ],
        "Serial": "`07:71:71:f4:6b:e7:bf:63:87:e6:ad:3c:b2:0f:d0:5b`",
        "Issuer": "Amazon",
        "Type": "AMAZON_ISSUED",
        "ExtendedKeyUsages": [
            {
                "OID": "1.3.6.1.5.5.7.3.1",
                "Name": "TLS_WEB_SERVER_AUTHENTICATION"
            },
            {
                "OID": "1.3.6.1.5.5.7.3.2",
                "Name": "TLS_WEB_CLIENT_AUTHENTICATION"
            }
        ],
        "DomainValidationOptions": [
            {
                "ValidationEmails": [
                    "hostmaster@example.com",
                    "admin@example.com",
                    "postmaster@example.com",
                    "webmaster@example.com",
                    "administrator@example.com"
                ],
                "ValidationDomain": "example.com",
                "DomainName": "example.com"
            },
            {
                "ValidationEmails": [
                    "hostmaster@example.com",
                    "admin@example.com",
                    "postmaster@example.com",
                    "webmaster@example.com",
                    "administrator@example.com"
                ],
                "ValidationDomain": "www.example.com",
                "DomainName": "www.example.com"
            }
        ],
        "Subject": "CN=example.com"
    }
}
```
