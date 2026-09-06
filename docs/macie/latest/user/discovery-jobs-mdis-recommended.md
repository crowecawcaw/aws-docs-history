

# Managed data identifiers recommended for sensitive data discovery jobs
<a name="discovery-jobs-mdis-recommended"></a>

To optimize the results of your sensitive data discovery jobs, you can configure individual jobs to automatically use the set of managed data identifiers that we recommend for jobs. A *managed data identifier* is a set of built-in criteria and techniques that are designed to detect a specific type of sensitive data—for example, AWS secret access keys, credit card numbers, or passport numbers for a particular country or region.

The recommended set of managed data identifiers is designed to detect common categories and types of sensitive data. Based on our research, it can detect general categories and types of sensitive data while also optimizing your job results by reducing noise. As we release new managed data identifiers, we add them to this set if they're likely to further optimize your job results. Over time, we might also add or remove existing managed data identifiers from the set. If we add or remove a managed data identifier from the recommended set, we update this page to indicate the nature and timing of the change. For automatic alerts about these changes, you can subscribe to the RSS feed on the [Macie document history](doc-history.md) page.

When you create a sensitive data discovery job, you specify which managed data identifiers you want the job to use to analyze objects in Amazon Simple Storage Service (Amazon S3) buckets. To configure a job to use the recommended set of managed data identifiers, choose the *Recommended* option when you create the job. The job will then automatically use all the managed data identifiers that are in the recommended set when the job starts to run. If you configure a job to run more than once, each run will automatically use all the managed data identifiers that are in the recommended set when the run starts.

The following topics list the managed data identifiers that are currently in the recommended set, organized by sensitive data category and type. They specify the unique identifier (ID) for each managed data identifier in the set. This ID describes the type of sensitive data that a managed data identifier is designed to detect, for example: `PGP_PRIVATE_KEY` for PGP private keys and `USA_PASSPORT_NUMBER` for US passport numbers.

**Topics**
+ [Credentials](#discovery-jobs-mdis-recommended-credentials)
+ [Financial information](#discovery-jobs-mdis-recommended-financial)
+ [Personally identifiable information (PII)](#discovery-jobs-mdis-recommended-pii)
+ [Updates to the recommended set](#discovery-jobs-mdis-recommended-updates)

 For details about specific managed data identifiers or a complete list of all the managed data identifiers that Macie currently provides, see [Using managed data identifiers](managed-data-identifiers.md).

## Credentials
<a name="discovery-jobs-mdis-recommended-credentials"></a>

To detect occurrences of credentials data in S3 objects, the recommended set uses the following managed data identifiers.


| Sensitive data type | Managed data identifier ID | 
| --- | --- | 
| AWS secret access key | AWS\_CREDENTIALS | 
| HTTP Basic Authorization header | HTTP\_BASIC\_AUTH\_HEADER | 
| OpenSSH private key | OPENSSH\_PRIVATE\_KEY | 
| PGP private key | PGP\_PRIVATE\_KEY | 
| Public Key Cryptography Standard (PKCS) private key | PKCS | 
| PuTTY private key | PUTTY\_PRIVATE\_KEY | 

## Financial information
<a name="discovery-jobs-mdis-recommended-financial"></a>

To detect occurrences of financial information in S3 objects, the recommended set uses the following managed data identifiers.


| Sensitive data type | Managed data identifier ID | 
| --- | --- | 
| Credit card magnetic stripe data | CREDIT\_CARD\_MAGNETIC\_STRIPE | 
| Credit card number | CREDIT\_CARD\_NUMBER (for credit card numbers in proximity of a keyword) | 

## Personally identifiable information (PII)
<a name="discovery-jobs-mdis-recommended-pii"></a>

To detect occurrences of personally identifiable information (PII) in S3 objects, the recommended set uses the following managed data identifiers.


| Sensitive data type | Managed data identifier ID | 
| --- | --- | 
| Driver’s license identification number | CANADA\_DRIVERS\_LICENSE, DRIVERS\_LICENSE (for the US), UK\_DRIVERS\_LICENSE | 
| Electoral roll number | UK\_ELECTORAL\_ROLL\_NUMBER | 
| National identification number | FRANCE\_NATIONAL\_IDENTIFICATION\_NUMBER, GERMANY\_NATIONAL\_IDENTIFICATION\_NUMBER, ITALY\_NATIONAL\_IDENTIFICATION\_NUMBER, SPAIN\_DNI\_NUMBER | 
| National Insurance Number (NINO) | UK\_NATIONAL\_INSURANCE\_NUMBER | 
| Passport number | CANADA\_PASSPORT\_NUMBER, FRANCE\_PASSPORT\_NUMBER, GERMANY\_PASSPORT\_NUMBER, ITALY\_PASSPORT\_NUMBER, SPAIN\_PASSPORT\_NUMBER, UK\_PASSPORT\_NUMBER, USA\_PASSPORT\_NUMBER | 
| Social Insurance Number (SIN) | CANADA\_SOCIAL\_INSURANCE\_NUMBER | 
| Social Security number (SSN) | SPAIN\_SOCIAL\_SECURITY\_NUMBER, USA\_SOCIAL\_SECURITY\_NUMBER | 
| Taxpayer identification or reference number | AUSTRALIA\_TAX\_FILE\_NUMBER, BRAZIL\_CPF\_NUMBER, FRANCE\_TAX\_IDENTIFICATION\_NUMBER, GERMANY\_TAX\_IDENTIFICATION\_NUMBER, SPAIN\_NIE\_NUMBER, SPAIN\_NIF\_NUMBER, SPAIN\_TAX\_IDENTIFICATION\_NUMBER, USA\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER | 

## Updates to the recommended set
<a name="discovery-jobs-mdis-recommended-updates"></a>

The following table describes changes to the set of managed data identifiers that we recommend for sensitive data discovery jobs. For automatic alerts about these changes, subscribe to the RSS feed on the [Macie document history](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| General availability | Initial release of the recommended set. | June 27, 2023 | 