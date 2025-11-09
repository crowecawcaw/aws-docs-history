# Severity scoring for Macie findings

When Amazon Macie generates a policy or sensitive data finding, it automatically assigns a
severity to the finding. A finding's severity reflects the principal characteristics of the
finding, which can help you assess and prioritize the finding. A finding's severity doesn't
imply or otherwise indicate the criticality or importance that an affected resource might
have for your organization.

For policy findings, severity is based on the nature of a potential issue with the security
or privacy of an Amazon Simple Storage Service (Amazon S3) general purpose bucket. For sensitive data findings,
severity is based on the nature and number of occurrences of sensitive data that Macie
detected in an S3 object.

In Macie, a finding's severity is represented in two ways.

Severity level

This is a qualitative representation of severity. Severity levels range from
_Low_, for least severe, to
_High_, for most severe.

Severity levels appear directly on the Amazon Macie console. They're also available in JSON
representations of findings on the Macie console, from the Amazon Macie API, and in
sensitive data discovery results that correlate to sensitive data findings. Severity
levels are also included in finding events that Macie publishes to Amazon EventBridge and
findings that Macie publishes to AWS Security Hub.

Severity score

This is a numerical representation of severity. Severity scores range from
_1_ through _3_
and map directly to severity levels:

| Severity score | Severity level |
| -------------- | -------------- |
| 1              | Low            |
| 2              | Medium         |
| 3              | High           |

Severity scores don't appear directly on the Amazon Macie console. However, they're available
in JSON representations of findings on the Macie console, from the Amazon Macie API, and
in sensitive data discovery results that correlate to sensitive data findings.
Severity scores are also included in finding events that Macie publishes to Amazon EventBridge.
They aren't included in findings that Macie publishes to AWS Security Hub.

The topics in this section indicate how Macie determines the severity of policy findings
and sensitive data findings.

###### Topics

- [Severity scoring for policy findings](#findings-severity-policy "#findings-severity-policy")
- [Severity scoring for sensitive data
  findings](#findings-severity-mdis "#findings-severity-mdis")

## Severity scoring for policy findings

The severity of a policy finding is based on the nature of a potential issue with the
security or privacy of an S3 general purpose bucket. The following table lists the
severity levels that Amazon Macie assigns to each type of policy finding. For a description
of each type, see [Types of findings](findings-types.md "findings-types.md").

| Finding type                                | Severity level |
| ------------------------------------------- | -------------- |
| Policy:IAMUser/S3BlockPublicAccessDisabled  | High           |
| Policy:IAMUser/S3BucketEncryptionDisabled   | Low            |
| Policy:IAMUser/S3BucketPublic               | High           |
| Policy:IAMUser/S3BucketReplicatedExternally | High           |
| Policy:IAMUser/S3BucketSharedExternally     | High           |
| Policy:IAMUser/S3BucketSharedWithCloudFront | Medium         |

The severity of a policy finding doesn't change based on the number of occurrences of
the finding.

## Severity scoring for sensitive data

findings

The severity of a sensitive data finding is based on the nature and number of occurrences of
sensitive data that Amazon Macie detected in an S3 object. The following topics indicate
how Macie determines the severity of each type of sensitive data finding:

- [SensitiveData:S3Object/Credentials](#findings-severity-credentials "#findings-severity-credentials")
- [SensitiveData:S3Object/CustomIdentifier](#findings-severity-cdis "#findings-severity-cdis")
- [SensitiveData:S3Object/Financial](#findings-severity-financial "#findings-severity-financial")
- [SensitiveData:S3Object/Personal](#findings-severity-personal "#findings-severity-personal")
- [SensitiveData:S3Object/Multiple](#findings-severity-multiple "#findings-severity-multiple")

For details about the types of sensitive data that Macie can detect and report in sensitive
data findings, see [Using managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md") and [Building custom data
identifiers](custom-data-identifiers.md "custom-data-identifiers.md").

### SensitiveData:S3Object/Credentials

A **SensitiveData:S3Object/Credentials** finding indicates that Macie
detected sensitive credentials data in an S3 object. For this type of finding, Macie
determines severity based on the type and number of occurrences of the credentials
data that Macie detected in the object.

The following table indicates the severity levels that Macie assigns to findings that
report occurrences of credentials data in an S3 object.

| Sensitive data type                                 | 1 occurrence | 2–99 occurrences | 100 or more occurrences |
| --------------------------------------------------- | ------------ | ---------------- | ----------------------- |
| AWS secret access key                               | High         | High             | High                    |
| Google Cloud API key                                | High         | High             | High                    |
| HTTP Basic Authorization header                     | High         | High             | High                    |
| JSON Web Token (JWT)                                | High         | High             | High                    |
| OpenSSH private key                                 | High         | High             | High                    |
| PGP private key                                     | High         | High             | High                    |
| Public-Key Cryptography Standard (PKCS) private key | High         | High             | High                    |
| PuTTY private key                                   | High         | High             | High                    |
| Stripe API key                                      | High         | High             | High                    |

### SensitiveData:S3Object/CustomIdentifier

A **SensitiveData:S3Object/CustomIdentifier** finding indicates that
an S3 object contains text that matches the detection criteria of one or more custom
data identifiers. The object might contain more than one type of sensitive data.

By default, Macie assigns the **Medium** severity level to this type of
finding. If the affected S3 object contains at least one occurrence of text that
matches the detection criteria of at least one custom data identifier, Macie
automatically assigns the **Medium** severity level to the finding.
The severity of the finding doesn't change based on the number of occurrences of
text that match a custom data identifier's criteria.

However, the severity of this type of finding can vary if you defined custom severity
settings for a custom data identifier that produced the finding. If this is the case,
Macie determines severity as follows:

- If the S3 object contains text that matches the detection criteria of only one
  custom data identifier, Macie determines the finding's severity based on the
  severity settings for that identifier.
- If the S3 object contains text that matches the detection criteria of more than
  one custom data identifier, Macie determines the finding's severity by evaluating
  the severity settings for each custom data identifier, determining which of those
  settings produces the highest severity, and then assigning that highest severity
  to the finding.

To review the severity settings for a custom data identifier, you can use the Amazon Macie
console or the Amazon Macie API. To review the settings on the console, choose
**Custom data identifiers** in the navigation pane, and then
choose the name of the custom data identifier. The **Severity**
section shows the settings. To retrieve the settings programmatically, use the
[GetCustomDataIdentifier](../APIReference/custom-data-identifiers-id.md "../APIReference/custom-data-identifiers-id.md") operation or, if you're using the AWS Command Line Interface,
run the [get-custom-data-identifier](../../../cli/latest/reference/macie2/get-custom-data-identifier.md "../../../cli/latest/reference/macie2/get-custom-data-identifier.md") command. To learn about the settings, see
[Configuration options for custom data identifiers](cdis-options.md "cdis-options.md").

### SensitiveData:S3Object/Financial

A **SensitiveData:S3Object/Financial** finding indicates that Macie
detected sensitive financial information in an S3 object. For this type of finding,
Macie determines severity based on the type and number of occurrences of the
financial information that Macie detected in the object.

The following table indicates the severity levels that Macie assigns to findings that
report occurrences of financial information in an S3 object.

| Sensitive data type              | 1 occurrence | 2–99 occurrences | 100 or more occurrences |
| -------------------------------- | ------------ | ---------------- | ----------------------- |
| Bank account number 1            | High         | High             | High                    |
| Credit card expiration date      | Low          | Medium           | High                    |
| Credit card magnetic stripe data | High         | High             | High                    |
| Credit card number 2             | High         | High             | High                    |
| Credit card verification code    | Medium       | High             | High                    |

1. Severity levels are the same for any type of bank account number—a
   Basic Bank Account Number (BBAN), an International Bank Account Number
   (IBAN), or a Canadian or US bank account number.
2. Severity levels are the same for credit card numbers that are or aren't in
   proximity of a keyword.

If a finding reports multiple types of financial information in an S3 object, Macie
determines the finding's severity by calculating the severity for each type of
financial information that Macie detected, determining which type produces the
highest severity, and assigning that highest severity to the finding. For example,
if Macie detects 10 credit card expiration dates (**Medium**
severity level) and 10 credit card numbers (**High** severity
level) in an object, Macie assigns the **High** severity level to
the finding.

### SensitiveData:S3Object/Personal

A **SensitiveData:S3Object/Personal** finding indicates that Macie detected sensitive personal information in an S3 object. The information can be personal health information (PHI), personally identifiable information (PII), or a combination of the two. For this type of finding, Macie determines severity based on the type and number of occurrences of the personal information that Macie detected in the object.

The following table indicates the severity levels that Macie assigns to sensitive data findings that report occurrences of PHI in an S3 object.

| Sensitive data type                                    | 1 occurrence | 2–99 occurrences | 100 or more occurrences |
| ------------------------------------------------------ | ------------ | ---------------- | ----------------------- |
| Drug Enforcement Agency (DEA) Registration Number      | High         | High             | High                    |
| Health Insurance Claim Number (HICN)                   | High         | High             | High                    |
| Health insurance or medical identification number      | High         | High             | High                    |
| Healthcare Common Procedure Coding System (HCPCS) code | High         | High             | High                    |
| National Drug Code (NDC)                               | High         | High             | High                    |
| National Provider Identifier (NPI)                     | High         | High             | High                    |
| Unique device identifier (UDI)                         | Low          | Medium           | High                    |

The following table indicates the severity levels that Macie assigns to sensitive data findings that report occurrences of PII in an S3 object.

| Sensitive data type                            | 1 occurrence | 2–99 occurrences | 100 or more occurrences |
| ---------------------------------------------- | ------------ | ---------------- | ----------------------- |
| Birth date                                     | Low          | Medium           | High                    |
| Driver’s license identification number         | Low          | Medium           | High                    |
| Electoral roll number                          | High         | High             | High                    |
| Full name                                      | Low          | Medium           | High                    |
| Global Positioning System (GPS) coordinates    | Low          | Medium           | Medium                  |
| HTTP cookie                                    | Low          | Medium           | High                    |
| Mailing address                                | Low          | Medium           | High                    |
| National identification number                 | High         | High             | High                    |
| National Insurance Number (NINO)               | High         | High             | High                    |
| Passport number                                | Medium       | High             | High                    |
| Permanent residence number                     | High         | High             | High                    |
| Phone number                                   | Low          | Medium           | High                    |
| Public transportation card number              | Medium       | Medium           | High                    |
| Social Insurance Number (SIN)                  | High         | High             | High                    |
| Social Security number (SSN)                   | High         | High             | High                    |
| Taxpayer identification or reference number \* | High         | High             | High                    |
| Vehicle identification number (VIN)            | Low          | Low              | Medium                  |

\* Exceptions are: CUIT numbers for organizations in Argentina (`ARGENTINA_ORGANIZATION_TAX_IDENTIFICATION_NUMBER`), NIT numbers for organizations in Colombia (`COLOMBIA_ORGANIZATION_NIT_NUMBER`), and RFC numbers for organizations in Mexico (`MEXICO_ORGANIZATION_RFC_NUMBER`). For those types, the severity levels are: **Medium** for 1–99 occurrences, and **High** for 100 or more occurrences.

If a finding reports multiple types of PHI, PII, or both PHI and PII in an object, Macie determines the finding's severity by calculating the severity for each type, determining which type produces the highest severity, and assigning that highest severity to the finding.

For example, if Macie detects 10 full names (**Medium** severity level) and 5 passport numbers (**High** severity level) in an object, Macie assigns the **High** severity level to the finding. Similarly, if Macie detects 10 full names (**Medium** severity level) and 10 health insurance identification numbers (**High** severity level) in an object, Macie assigns the **High** severity level to the finding.

### SensitiveData:S3Object/Multiple

A **SensitiveData:S3Object/Multiple** finding indicates that Macie
detected multiple categories of sensitive data in an S3 object. The sensitive data
can be any combination of credentials data, financial information, personal
information, or text that matches the detection criteria of one or more custom data
identifiers.

For this type of finding, Macie determines severity by calculating the severity for each
type of sensitive data that Macie detected (as indicated in the preceding topics),
determining which type produces the highest severity, and assigning that highest
severity to the finding.

For example, if Macie detects 10 full names (**Medium** severity level)
and 10 AWS secret access keys (**High** severity level) in an
object, Macie assigns the **High** severity level to the
finding.
