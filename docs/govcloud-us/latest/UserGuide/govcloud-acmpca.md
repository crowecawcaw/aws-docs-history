# AWS Private Certificate Authority in AWS GovCloud (US)

AWS Private Certificate Authority (AWS Private CA) is a managed private CA service with which you can easily and securely
manage your CA infrastructure and your private certificates.

## How AWS Private CA differs for AWS GovCloud (US)

- Online Certificate Status Protocol (OCSP) is not supported in the
  AWS GovCloud (US) Regions.
- To connect to AWS Private CA by using the command line or API, use the following [endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md"):
  - `https://acm-pca.us-gov-west-1.amazonaws.com`
  - `https://acm-pca.us-gov-east-1.amazonaws.com`

## Documentation for AWS Private CA

[AWS Private Certificate Authority
documentation](../../../acm-pca/latest/userguide/PCAWelcome.md "../../../acm-pca/latest/userguide/PCAWelcome.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No export-controlled data may be entered, stored, or processed by AWS Private Certificate Authority.
  For example, domain names specified for certificates are not permitted to
  contain export-controlled data. For example, do not enter export-controlled data
  into the **DomainName** or
  **SubjectAlternativeNames** fields when requesting a
  certificate.
