# Using encrypted content keys with DRM

For the most secure DRM encryption solution, use encrypted content keys in addition to
encrypted content. To use encrypted content keys, you must import suitable certificates into
AWS Certificate Manager (ACM), and then prepare them for use with AWS Elemental MediaConvert. For information about
ACM, see the [AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md").

Run AWS Certificate Manager in the same Region as you run AWS Elemental MediaConvert.

###### To prepare a certificate for DRM content key encryption

1. Obtain a 2048 RSA, SHA-512-signed certificate.
2. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
3. Import the certificate into ACM according to the instructions at [Importing certificates into AWS Certificate Manager](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md"). Note the resulting certificate ARN because you will need it
   later.

For use in DRM encryption, your certificate must have a status of
**Issued** in ACM. 4. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert/](https://console.aws.amazon.com/mediaconvert/ "https://console.aws.amazon.com/mediaconvert/"). 5. In the navigation pane, under **Certificates**, enter your
certificate ARN, and then choose **Associate certificate**.
**To find certificates that are associated with
AWS Elemental MediaConvert**

In the ACM console, list and display your certificates to find the ones that you have
associated with MediaConvert. In the **Details** section of the
certificate's description, you can see the MediaConvert association and retrieve the
certificate ARN. For more information, see [List
ACM–managed certificates](../../../acm/latest/userguide/gs-acm-list.md "../../../acm/latest/userguide/gs-acm-list.md") and [Describe ACM certificates](../../../acm/latest/userguide/gs-acm-describe.md "../../../acm/latest/userguide/gs-acm-describe.md").

**To use a certificate in AWS Elemental MediaConvert**

When you use DRM encryption, provide one of your associated certificate ARNs in the
SPEKE encryption parameters. This enables content key encryption. You can use the same
certificate ARN for multiple jobs. For information, see [Container and DRM system support with
SPEKE](encryption-choosing-speke-version.md "encryption-choosing-speke-version.md").

**To renew a certificate**

To renew a certificate that you have associated with AWS Elemental MediaConvert, reimport it in
AWS Certificate Manager. The certificate renews without any disruption of its use in MediaConvert.

**To delete a certificate**

To delete a certificate from AWS Certificate Manager, you must first dissociate it from any other
service. To dissociate a certificate from AWS Elemental MediaConvert, copy its certificate ARN from
ACM, navigate to the MediaConvert **Certificates** pane, enter the
certificate ARN, and then choose **Dissociate certificate**.
