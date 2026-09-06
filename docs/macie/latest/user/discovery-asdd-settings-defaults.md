

# Default settings for automated sensitive data discovery
<a name="discovery-asdd-settings-defaults"></a>

If automated sensitive data discovery is enabled, Amazon Macie automatically selects and analyzes sample objects from all the Amazon Simple Storage Service (Amazon S3) general purpose buckets for your account. If you're the Macie administrator for an organization, by default this includes S3 buckets that your member accounts own. 

If you're a Macie administrator or you have a standalone Macie account, you can refine the scope of the analyses by excluding specific S3 buckets from automated sensitive data discovery. You can do this in two ways: by changing the settings for your account, and by changing the settings for individual buckets. As a Macie administrator, you can also enable or disable automated sensitive data discovery for individual accounts in your organization.

By default, Macie analyzes S3 objects by using only the set of managed data identifiers that we recommend for automated sensitive data discovery. Macie doesn't use any custom data identifiers or allow lists that you defined. If you're a Macie administrator or you have a standalone Macie account, you can customize the analyses by configuring Macie to use specific managed data identifiers, custom data identifiers, and allow lists. You can do this by changing the settings for your account. 

For information about changing your settings, see [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md).

**Topics**
+ [Default managed data identifiers](#discovery-asdd-settings-defaults-mdis)
+ [Updates to the default settings](#discovery-asdd-mdis-default-updates)

## Default managed data identifiers for automated sensitive data discovery
<a name="discovery-asdd-settings-defaults-mdis"></a>

By default, Amazon Macie analyzes S3 objects by using only the set of managed data identifiers that we recommend for automated sensitive data discovery. This default set of managed data identifiers is designed to detect common categories and types of sensitive data. Based on our research, it can detect general categories and types of sensitive data while also optimizing your results by reducing noise.

The default set is dynamic. As we release new managed data identifiers, we add them to the default set if they're likely to further optimize your automated sensitive data discovery results. Over time, we might also add or remove existing managed data identifiers from the set. Removal of a managed data identifier doesn't affect existing sensitive data discovery statistics and details for your S3 buckets. For example, if we remove the managed data identifier for a type of sensitive data that Macie previously detected in a bucket, Macie continues to report those detections. If we add or remove a managed data identifier from the default set, we update this page to indicate the nature and timing of the change. For automatic alerts about these changes, you can subscribe to the RSS feed on the [Macie document history](doc-history.md) page.

The following topics list the managed data identifiers that are currently in the default set, organized by sensitive data category and type. They specify the unique identifier (ID) for each managed data identifier in the set. This ID describes the type of sensitive data that a managed data identifier is designed to detect, for example: `PGP_PRIVATE_KEY` for PGP private keys and `USA_PASSPORT_NUMBER` for US passport numbers. If you change your settings for automated sensitive data discovery, you can use this ID to explicitly exclude a managed data identifier from subsequent analyses.

**Topics**
+ [Credentials](#discovery-asdd-settings-defaults-mdis-credentials)
+ [Financial information](#discovery-asdd-settings-defaults-mdis-financial)
+ [Personally identifiable information (PII)](#discovery-asdd-settings-defaults-mdis-pii)

 For details about specific managed data identifiers or a complete list of all the managed data identifiers that Macie currently provides, see [Using managed data identifiers](managed-data-identifiers.md).

### Credentials
<a name="discovery-asdd-settings-defaults-mdis-credentials"></a>

To detect occurrences of credentials data in S3 objects, Macie uses the following managed data identifiers by default.


| Sensitive data type | Managed data identifier ID | 
| --- | --- | 
| AWS secret access key | AWS\_CREDENTIALS | 
| HTTP Basic Authorization header | HTTP\_BASIC\_AUTH\_HEADER | 
| OpenSSH private key | OPENSSH\_PRIVATE\_KEY | 
| PGP private key | PGP\_PRIVATE\_KEY | 
| Public Key Cryptography Standard (PKCS) private key | PKCS | 
| PuTTY private key | PUTTY\_PRIVATE\_KEY | 

### Financial information
<a name="discovery-asdd-settings-defaults-mdis-financial"></a>

To detect occurrences of financial information in S3 objects, Macie uses the following managed data identifiers by default.


| Sensitive data type | Managed data identifier ID | 
| --- | --- | 
| Credit card magnetic stripe data | CREDIT\_CARD\_MAGNETIC\_STRIPE | 
| Credit card number | CREDIT\_CARD\_NUMBER (for credit card numbers in proximity of a keyword) | 

### Personally identifiable information (PII)
<a name="discovery-asdd-settings-defaults-mdis-pii"></a>

To detect occurrences of personally identifiable information (PII) in S3 objects, Macie uses the following managed data identifiers by default.


| Sensitive data type | Managed data identifier ID | 
| --- | --- | 
| Driver’s license identification number | CANADA\_DRIVERS\_LICENSE, DRIVERS\_LICENSE (for the US),  UK\_DRIVERS\_LICENSE | 
| Electoral roll number | UK\_ELECTORAL\_ROLL\_NUMBER | 
| National identification number | FRANCE\_NATIONAL\_IDENTIFICATION\_NUMBER, GERMANY\_NATIONAL\_IDENTIFICATION\_NUMBER, ITALY\_NATIONAL\_IDENTIFICATION\_NUMBER, SPAIN\_DNI\_NUMBER | 
| National Insurance Number (NINO) | UK\_NATIONAL\_INSURANCE\_NUMBER | 
| Passport number | CANADA\_PASSPORT\_NUMBER, FRANCE\_PASSPORT\_NUMBER, GERMANY\_PASSPORT\_NUMBER, ITALY\_PASSPORT\_NUMBER, SPAIN\_PASSPORT\_NUMBER, UK\_PASSPORT\_NUMBER, USA\_PASSPORT\_NUMBER | 
| Social Insurance Number (SIN) | CANADA\_SOCIAL\_INSURANCE\_NUMBER | 
| Social Security number (SSN) | SPAIN\_SOCIAL\_SECURITY\_NUMBER, USA\_SOCIAL\_SECURITY\_NUMBER | 
| Taxpayer identification or reference number | AUSTRALIA\_TAX\_FILE\_NUMBER, BRAZIL\_CPF\_NUMBER, FRANCE\_TAX\_IDENTIFICATION\_NUMBER, GERMANY\_TAX\_IDENTIFICATION\_NUMBER, SPAIN\_NIE\_NUMBER, SPAIN\_NIF\_NUMBER, SPAIN\_TAX\_IDENTIFICATION\_NUMBER, USA\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER | 

## Updates to the default settings for automated sensitive data discovery
<a name="discovery-asdd-mdis-default-updates"></a>

The following table describes changes to the settings that Amazon Macie uses by default for automated sensitive data discovery. For automatic alerts about these changes, subscribe to the RSS feed on the [Macie document history](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| Implemented a new, dynamic set of default managed data identifiers | New automated sensitive data discovery configurations are now based on a dynamic [default set of managed data identifiers](#discovery-asdd-settings-defaults-mdis). If you enable automated sensitive data discovery for the first time on or after this date, your configuration is based on the dynamic set.<br />If you enabled automated sensitive data discovery for the first time before this date, your configuration is based on a different set of managed data identifiers. For more information, see the notes after this table. | August 2, 2023 | 
| General availability | Initial release of automated sensitive data discovery. | November 28, 2022 | 

If you initially enabled automated sensitive data discovery prior to August 2, 2023, your configuration isn't based on the dynamic set of default managed data identifiers. Instead, it's based on a static set of managed data identifiers that we defined for the initial release of automated sensitive data discovery, as listed in the table below.

To determine when you initially enabled automated sensitive data discovery you can use the Amazon Macie console: choose **Automated sensitive data discovery** in the navigation pane, and then refer to the enabled date in the **Status** section. You can also do this programmatically: use the [GetAutomatedDiscoveryConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-configuration.html) operation of the Amazon Macie API and refer to the value for the `firstEnabledAt` field. If the date is prior to August 2, 2023, and you want to start using the dynamic set of default managed data identifiers, contact AWS Support for assistance.

The following table lists all the managed data identifiers that are in the static set. The table is sorted first by sensitive data category and then by sensitive data type. For details about specific managed data identifiers, see [Using managed data identifiers](managed-data-identifiers.md).


| Sensitive data category | Sensitive data type | Managed data identifier ID | 
| --- | --- | --- | 
| Credentials | AWS secret access key | AWS\_CREDENTIALS | 
| Credentials | HTTP Basic Authorization header | HTTP\_BASIC\_AUTH\_HEADER | 
| Credentials | OpenSSH private key | OPENSSH\_PRIVATE\_KEY | 
| Credentials | PGP private key | PGP\_PRIVATE\_KEY | 
| Credentials | Public Key Cryptography Standard (PKCS) private key | PKCS | 
| Credentials | PuTTY private key | PUTTY\_PRIVATE\_KEY | 
| Financial information | Bank account number | BANK\_ACCOUNT\_NUMBER (for Canadian and US bank account numbers), FRANCE\_BANK\_ACCOUNT\_NUMBER, GERMANY\_BANK\_ACCOUNT\_NUMBER, ITALY\_BANK\_ACCOUNT\_NUMBER, SPAIN\_BANK\_ACCOUNT\_NUMBER, UK\_BANK\_ACCOUNT\_NUMBER | 
| Financial information | Credit card expiration date | CREDIT\_CARD\_EXPIRATION | 
| Financial information | Credit card magnetic stripe data | CREDIT\_CARD\_MAGNETIC\_STRIPE | 
| Financial information | Credit card number | CREDIT\_CARD\_NUMBER (for credit card numbers in proximity of a keyword) | 
| Financial information | Credit card verification code | CREDIT\_CARD\_SECURITY\_CODE | 
| Personal information: Personal health information (PHI) | Drug Enforcement Agency (DEA) Registration Number | US\_DRUG\_ENFORCEMENT\_AGENCY\_NUMBER | 
| Personal information: PHI | Health Insurance Claim Number (HICN) | USA\_HEALTH\_INSURANCE\_CLAIM\_NUMBER | 
| Personal information: PHI | Health insurance or medical identification number | CANADA\_HEALTH\_NUMBER, EUROPEAN\_HEALTH\_INSURANCE\_CARD\_NUMBER, FINLAND\_EUROPEAN\_HEALTH\_INSURANCE\_NUMBER, FRANCE\_HEALTH\_INSURANCE\_NUMBER, UK\_NHS\_NUMBER, USA\_MEDICARE\_BENEFICIARY\_IDENTIFIER | 
| Personal information: PHI | Healthcare Common Procedure Coding System (HCPCS) code | USA\_HEALTHCARE\_PROCEDURE\_CODE | 
| Personal information: PHI | National Drug Code (NDC) | USA\_NATIONAL\_DRUG\_CODE | 
| Personal information: PHI | National Provider Identifier (NPI) | USA\_NATIONAL\_PROVIDER\_IDENTIFIER | 
| Personal information: PHI | Unique device identifier (UDI) | MEDICAL\_DEVICE\_UDI | 
| Personal information: Personally identifiable information (PII) | Birth date | DATE\_OF\_BIRTH | 
| Personal information: PII | Driver’s license identification number | AUSTRALIA\_DRIVERS\_LICENSE, AUSTRIA\_DRIVERS\_LICENSE, BELGIUM\_DRIVERS\_LICENSE, BULGARIA\_DRIVERS\_LICENSE, CANADA\_DRIVERS\_LICENSE, CROATIA\_DRIVERS\_LICENSE, CYPRUS\_DRIVERS\_LICENSE, CZECHIA\_DRIVERS\_LICENSE, DENMARK\_DRIVERS\_LICENSE, DRIVERS\_LICENSE (for the US), ESTONIA\_DRIVERS\_LICENSE, FINLAND\_DRIVERS\_LICENSE, FRANCE\_DRIVERS\_LICENSE, GERMANY\_DRIVERS\_LICENSE, GREECE\_DRIVERS\_LICENSE, HUNGARY\_DRIVERS\_LICENSE, IRELAND\_DRIVERS\_LICENSE, ITALY\_DRIVERS\_LICENSE, LATVIA\_DRIVERS\_LICENSE, LITHUANIA\_DRIVERS\_LICENSE, LUXEMBOURG\_DRIVERS\_LICENSE, MALTA\_DRIVERS\_LICENSE, NETHERLANDS\_DRIVERS\_LICENSE, POLAND\_DRIVERS\_LICENSE, PORTUGAL\_DRIVERS\_LICENSE, ROMANIA\_DRIVERS\_LICENSE, SLOVAKIA\_DRIVERS\_LICENSE, SLOVENIA\_DRIVERS\_LICENSE, SPAIN\_DRIVERS\_LICENSE, SWEDEN\_DRIVERS\_LICENSE, UK\_DRIVERS\_LICENSE | 
| Personal information: PII | Electoral roll number | UK\_ELECTORAL\_ROLL\_NUMBER | 
| Personal information: PII | Full name | NAME | 
| Personal information: PII | Global Positioning System (GPS) coordinates | LATITUDE\_LONGITUDE | 
| Personal information: PII | Mailing address | ADDRESS, BRAZIL\_CEP\_CODE | 
| Personal information: PII | National identification number | BRAZIL\_RG\_NUMBER, FRANCE\_NATIONAL\_IDENTIFICATION\_NUMBER, GERMANY\_NATIONAL\_IDENTIFICATION\_NUMBER, ITALY\_NATIONAL\_IDENTIFICATION\_NUMBER, SPAIN\_DNI\_NUMBER | 
| Personal information: PII | National Insurance Number (NINO) | UK\_NATIONAL\_INSURANCE\_NUMBER | 
| Personal information: PII | Passport number | CANADA\_PASSPORT\_NUMBER, FRANCE\_PASSPORT\_NUMBER, GERMANY\_PASSPORT\_NUMBER, ITALY\_PASSPORT\_NUMBER, SPAIN\_PASSPORT\_NUMBER, UK\_PASSPORT\_NUMBER, USA\_PASSPORT\_NUMBER | 
| Personal information: PII | Permanent residence number | CANADA\_NATIONAL\_IDENTIFICATION\_NUMBER | 
| Personal information: PII | Phone number | BRAZIL\_PHONE\_NUMBER, FRANCE\_PHONE\_NUMBER, GERMANY\_PHONE\_NUMBER, ITALY\_PHONE\_NUMBER, PHONE\_NUMBER (for Canada and the US), SPAIN\_PHONE\_NUMBER, UK\_PHONE\_NUMBER | 
| Personal information: PII | Social Insurance Number (SIN) | CANADA\_SOCIAL\_INSURANCE\_NUMBER | 
| Personal information: PII | Social Security number (SSN) | SPAIN\_SOCIAL\_SECURITY\_NUMBER, USA\_SOCIAL\_SECURITY\_NUMBER | 
| Personal information: PII | Taxpayer identification or reference number | AUSTRALIA\_TAX\_FILE\_NUMBER, BRAZIL\_CNPJ\_NUMBER, BRAZIL\_CPF\_NUMBER, FRANCE\_TAX\_IDENTIFICATION\_NUMBER, GERMANY\_TAX\_IDENTIFICATION\_NUMBER, SPAIN\_NIE\_NUMBER, SPAIN\_NIF\_NUMBER, SPAIN\_TAX\_IDENTIFICATION\_NUMBER, UK\_TAX\_IDENTIFICATION\_NUMBER, USA\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER | 
| Personal information: PII | Vehicle identification number (VIN) | VEHICLE\_IDENTIFICATION\_NUMBER | 