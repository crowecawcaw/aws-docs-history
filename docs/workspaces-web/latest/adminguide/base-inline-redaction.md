# Base inline redaction in Amazon WorkSpaces Secure Browser

Inline data redaction has support for built-in patterns (such as social security numbers
and credit card numbers), which you can find listed under **Base inline
redaction**. Choose the data type(s) from the drop-down menu, and specify the
replacement value for each data type. All data types follow the default configuration
enforcement pattern above, but you can choose to override the confidence level, and fine-tune
the domain enforcement pattern for each data type.

To enter an alternative value from the default configuration, choose **Confidence
level override**. For example, with the default configuration set to Medium, you might
notice during testing that one of your data types is not being redacted reliably. You can set
the override to Low to increase the chance of redaction, without adjusting the logic used for
your other data types.

To fine-tune the way redaction is applied across URLs without changing the default
configuration, apply **URL enforcement overrides**. For example, you can set
use URL overrides to enforce email address redaction in your customer relationship management
system, without breaking user access to email addresses in the company directory website or web
based email.

The following is a list of data types and their corresponding built-in pattern IDs:

| builtInPatternId       | Data type                                       |
| ---------------------- | ----------------------------------------------- |
| awsAccessKey:          | AWS Access Key                                  |
| awsSecretKey:          | AWS Secret Key                                  |
| cardNumbers:           | Credit Card Numbers                             |
| crypto:                | Cryptocurrency Addresses                        |
| cusipNum:              | CUSIP Number                                    |
| date:                  | Date                                            |
| deaNum:                | US DEA Numbers                                  |
| dob:                   | Date of Birth                                   |
| driversLicense:        | US Driver’s Licenses                            |
| emailAddress:          | Email Address                                   |
| ein:                   | US Employer Identification Number               |
| expDate:               | Credit Card Expiration Date                     |
| healthInsuranceNum:    | Medicare Health Insurance Claim Number          |
| hipaaCode:             | HIPAA ICD-10 Code                               |
| indivTaxId:            | US Individual Tax Id                            |
| ipAddr:                | IP Address                                      |
| isin:                  | International Securities Identification Numbers |
| jwt:                   | JSON Web Token                                  |
| locationCoord:         | Location Coordinates                            |
| macAddr:               | MAC Address                                     |
| medicareBeneficiaryId: | Medicare Beneficiary Number                     |
| npi:                   | National Provider Identification Number         |
| ndc:                   | National Drug Codes (NDC)                       |
| passportNum:           | US Passport Number                              |
| phoneNum:              | Phone Number                                    |
| routingNumber:         | ABA Routing Number                              |
| ssn:                   | US Social Security Number                       |
| swiftCode:             | SWIFT Code                                      |
| time:                  | Time                                            |
| vin:                   | US Vehicle Identification Number                |
