# Using managed data

identifiers in Amazon SNS

## What are managed data

identifiers?

Amazon SNS managed data identifiers are designed to detect a specific type of sensitive data,
such as credit card numbers, AWS secret access keys, or passport numbers for a particular
country or region. When you create a data protection policy, you can configure Amazon SNS to use
these identifiers to analyze messages going through the topic, and take actions when they are
detected.

Amazon SNS can detect the following categories of sensitive data by using managed data
identifiers:

- Credentials, such as private keys or AWS secret access keys
- Device identifiers, such as IP address or MAC address
- Financial information, such as credit card numbers
- Health information, for PHI such as health insurance or medical identification
  numbers
- Personal information, for PII such as driver’s licenses or social security
  numbers

Within each category, Amazon SNS can detect multiple types of sensitive data. The topics in
this section list and describe each type and any relevant requirements for detecting it. For
each type, they also indicate the unique identifier (ID) for the managed data identifier
that's designed to detect the data. When you create a data protection policy, you can use this
ID to include the managed data identifier for message data protection to detect.

### Keyword requirements

To detect certain types of sensitive data, Amazon SNS scans for keywords in proximity of the
data. If this is the case for a particular type of data, a subsequent topic in this section
indicates specific keyword requirements for that data.

Keywords aren’t case sensitive. In addition, if a keyword contains a space, Amazon SNS
automatically matches keyword variations that don’t contain the space, or contain an
underscore (\_) or a hyphen (-) instead of the space. In certain cases, Amazon SNS also expands or
abbreviates a keyword to address common variations of the keyword.

### Amazon SNS managed data identifiers for sensitive

data types

The following table lists and describes the types of credential, device, financial,
medical, and personal health information (PHI) that Amazon SNS can detect using managed data
identifiers. These are in addition to certain types of data that might also qualify as
personally identifiable information (PII).

Region-dependent data identifiers require the identifier name with a dash, and the two
letter (ISO 3166-1 alpha-2) codes. For example, DriversLicense-US.

| Identifier                        | Category  | Countries/Languages                                                                                                           |
| --------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| BankAccountNumber                 | Financial | DE, ES, FR, GB, IT                                                                                                            |
| CepCode                           | Personal  | BR                                                                                                                            |
| Cnpj                              | Personal  | BR                                                                                                                            |
| CpfCode                           | Personal  | BR                                                                                                                            |
| DriversLicense                    | Personal  | AT, AU, BE, BG, CA, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT,<br>LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, US |
| DrugEnforcementAgencyNumber       | Health    | US                                                                                                                            |
| ElectoralRollNumber               | Personal  | GB                                                                                                                            |
| HealthInsuranceCardNumber         | Health    | EU                                                                                                                            |
| HealthInsuranceClaimNumber        | Health    | US                                                                                                                            |
| HealthInsuranceNumber             | Health    | FR                                                                                                                            |
| HealthcareProcedureCode           | Health    | US                                                                                                                            |
| IndividualTaxIdentificationNumber | Personal  | US                                                                                                                            |
| InseeCode                         | Personal  | FR                                                                                                                            |
| MedicareBeneficiaryNumber         | Health    | US                                                                                                                            |
| NationalDrugCode                  | Health    | US                                                                                                                            |
| NationalIdentificationNumber      | Personal  | DE, ES, IT                                                                                                                    |
| NationalInsuranceNumber           | Personal  | GB                                                                                                                            |
| NationalProviderId                | Health    | US                                                                                                                            |
| NhsNumber                         | Health    | GB                                                                                                                            |
| NieNumber                         | Personal  | ES                                                                                                                            |
| NifNumber                         | Personal  | ES                                                                                                                            |
| PassportNumber                    | Personal  | CA, DE, ES, FR, GB, IT, US                                                                                                    |
| PermanentResidenceNumber          | Personal  | CA                                                                                                                            |
| PersonalHealthNumber              | Health    | CA                                                                                                                            |
| PhoneNumber                       | Personal  | BR, DE, ES, FR, GB, IT, US                                                                                                    |
| PostalCode                        | Personal  | CA                                                                                                                            |
| RgNumber                          | Personal  | BR                                                                                                                            |
| SocialInsuranceNumber             | Personal  | CA                                                                                                                            |
| Ssn                               | Personal  | ES, US                                                                                                                        |
| TaxId                             | Personal  | DE, ES, FR, GB                                                                                                                |
| ZipCode                           | Personal  | US                                                                                                                            |

**Supported Identifiers that are language/region
independent**

| Identifier                  | Category    |
| --------------------------- | ----------- |
| Address                     | Personal    |
| AwsSecretKey                | Credentials |
| CreditCardExpiration        | Financial   |
| CreditCardNumber            | Financial   |
| CreditCardSecurityCode      | Financial   |
| EmailAddress                | Personal    |
| IpAddress                   | Personal    |
| LatLong                     | Personal    |
| Name                        | Personal    |
| OpenSshPrivateKey           | Credentials |
| PgpPrivateKey               | Credentials |
| PkcsPrivateKey              | Credentials |
| PuttyPrivateKey             | Credentials |
| VehicleIdentificationNumber | Personal    |
