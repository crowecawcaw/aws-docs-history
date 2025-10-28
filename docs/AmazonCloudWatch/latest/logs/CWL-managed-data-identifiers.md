# CloudWatch Logs managed data identifiers for sensitive

data types

This section contains information about the types of data that you can protect using managed
data identifiers, and which countries and regions
are relevant for each of those types of data.

For some types of sensitive data, CloudWatch Logs data protection scans for keywords in the proximity of the data, and
finds a match only if it finds that keyword. If a keyword has to be in proximity of a particular type of data, the keyword typically has to be within 30 characters (inclusively) of the data.

If a keyword contains a space, CloudWatch Logs data protection automatically matches keyword
variations that are missing the space or that contain an underscore (`_`) or hyphen (`-`)
instead of the space. In some cases, CloudWatch Logs also expands or abbreviates a keyword to address
common variations of the keyword.

The following tables lists the types of credential, device, financial,
medical, and protected health information (PHI) that CloudWatch Logs can detect using managed data
identifiers. These are in addition to certain types of data that might also qualify as
personally identifiable information (PII).

**Supported identifiers that are language and region
independent**

| Identifier                        | Category    |
| --------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Address`                         | Personal    |
| `AwsSecretKey`                    | Credentials |
| `CreditCardExpiration`            | Financial   |
| `CreditCardNumber`                | Financial   |
| `CreditCardSecurityCode`          | Financial   |
| `EmailAddress`                    | Personal    |
| `IpAddress`                       | Personal    |
| `LatLong`                         | Personal    |
| `Name`                            | Personal    |
| `OpenSshPrivateKey`               | Credentials |
| `PgpPrivateKey`                   | Credentials |
| `PkcsPrivateKey`                  | Credentials |
| `PuttyPrivateKey`                 | Credentials |
| `VehicleIdentificationNumber`     | Personal    | Region-dependent data identifiers must include the identifier name, then a hyphen, and then the two-letter (ISO 3166-1 alpha-2) codes. For example, `DriversLicense-US`. **Supported identifiers that must include a two-letter country or region code** |
| Identifier                        | Category    | Countries and languages                                                                                                                                                                                                                                  |
| ---                               | ---         | ---                                                                                                                                                                                                                                                      |
| BankAccountNumber                 | Financial   | DE, ES, FR, GB, IT, US                                                                                                                                                                                                                                   |
| CepCode                           | Personal    | BR                                                                                                                                                                                                                                                       |
| Cnpj                              | Personal    | BR                                                                                                                                                                                                                                                       |
| CpfCode                           | Personal    | BR                                                                                                                                                                                                                                                       |
| DriversLicense                    | Personal    | AT, AU, BE, BG, CA, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, US                                                                                                                               |
| DrugEnforcementAgencyNumber       | Health      | US                                                                                                                                                                                                                                                       |
| ElectoralRollNumber               | Personal    | GB                                                                                                                                                                                                                                                       |
| HealthInsuranceCardNumber         | Health      | EU                                                                                                                                                                                                                                                       |
| HealthInsuranceClaimNumber        | Health      | US                                                                                                                                                                                                                                                       |
| HealthInsuranceNumber             | Health      | FR                                                                                                                                                                                                                                                       |
| HealthcareProcedureCode           | Health      | US                                                                                                                                                                                                                                                       |
| IndividualTaxIdentificationNumber | Personal    | US                                                                                                                                                                                                                                                       |
| InseeCode                         | Personal    | FR                                                                                                                                                                                                                                                       |
| MedicareBeneficiaryNumber         | Health      | US                                                                                                                                                                                                                                                       |
| NationalDrugCode                  | Health      | US                                                                                                                                                                                                                                                       |
| NationalIdentificationNumber      | Personal    | DE, ES, IT                                                                                                                                                                                                                                               |
| NationalInsuranceNumber           | Personal    | GB                                                                                                                                                                                                                                                       |
| NationalProviderId                | Health      | US                                                                                                                                                                                                                                                       |
| NhsNumber                         | Health      | GB                                                                                                                                                                                                                                                       |
| NieNumber                         | Personal    | ES                                                                                                                                                                                                                                                       |
| NifNumber                         | Personal    | ES                                                                                                                                                                                                                                                       |
| PassportNumber                    | Personal    | CA, DE, ES, FR, GB, IT, US                                                                                                                                                                                                                               |
| PermanentResidenceNumber          | Personal    | CA                                                                                                                                                                                                                                                       |
| PersonalHealthNumber              | Health      | CA                                                                                                                                                                                                                                                       |
| PhoneNumber                       | Personal    | BR, DE, ES, FR, GB, IT, US                                                                                                                                                                                                                               |
| PostalCode                        | Personal    | CA                                                                                                                                                                                                                                                       |
| RgNumber                          | Personal    | BR                                                                                                                                                                                                                                                       |
| SocialInsuranceNumber             | Personal    | CA                                                                                                                                                                                                                                                       |
| Ssn                               | Personal    | ES, US                                                                                                                                                                                                                                                   |
| TaxId                             | Personal    | DE, ES, FR, GB                                                                                                                                                                                                                                           |
| ZipCode                           | Personal    | US                                                                                                                                                                                                                                                       |
