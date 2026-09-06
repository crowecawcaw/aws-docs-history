

# AWS Private Certificate Authority in AWS GovCloud (US)
<a name="govcloud-acmpca"></a>

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

 AWS Private Certificate Authority (AWS Private CA) is a managed private CA service with which you can easily and securely manage your CA infrastructure and your private certificates.

## How AWS Private CA differs
<a name="govcloud-acmpca-diffs"></a>

The following differences apply to AWS Private CA:
+ To connect to AWS Private CA by using the command line or API, use the following [endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html):
  +  `https://acm-pca.us-gov-west-1.amazonaws.com` 
  +  `https://acm-pca.us-gov-east-1.amazonaws.com` 
+ The Amazon Resource Name (ARN) for a private certificate authority has a AWS GovCloud (US) pattern of `arn:aws-us-gov:acm-pca:<region>:<account-id>:certificate-authority/<CA-ID>` 

  You can find this ARN on the **CA details** page in the AWS Private CA console.
+ The ARN for a certificate issued by a private CA has a AWS GovCloud (US) pattern of `arn:aws-us-gov:acm-pca:<region>:<account-id>:certificate-authority/<CA-ID>/certificate/<CertificateID>` 
+ The ARNs for certificate templates used with the `IssueCertificate` API action have a AWS GovCloud (US) pattern of `arn:aws-us-gov:acm-pca:::template/<TemplateName>/V1` 

  For example, `arn:aws-us-gov:acm-pca:::template/EndEntityCertificate/V1`. For the complete list of available template names, see [Using certificate templates](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html) in the AWS Private Certificate Authority User Guide.

## Documentation
<a name="govcloud-acmpca-docs"></a>
+  [AWS Private Certificate Authority documentation](https://docs.aws.amazon.com/acm-pca/latest/userguide/PCAWelcome.html) 

## Export-controlled content
<a name="itar-boundary-3"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ No export-controlled data may be entered, stored, or processed by AWS Private Certificate Authority. For example, domain names specified for certificates are not permitted to contain export-controlled data. For example, do not enter export-controlled data into the **DomainName** or **SubjectAlternativeNames** fields when requesting a certificate.