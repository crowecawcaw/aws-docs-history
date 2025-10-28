# Managed data identifiers recommended for sensitive data discovery jobs

To optimize the results of your sensitive data discovery jobs, you can configure individual jobs to
automatically use the set of managed data identifiers that we recommend for jobs. A _managed data identifier_ is a set of built-in criteria and techniques
that are designed to detect a specific type of sensitive data—for example, AWS secret
access keys, credit card numbers, or passport numbers for a particular country or
region.

The recommended set of managed data identifiers is designed to detect common categories and
types of sensitive data. Based on our research, it can detect general categories and types of
sensitive data while also optimizing your job results by reducing noise. As we release new managed
data identifiers, we add them to this set if they're likely to further optimize your job results.
Over time, we might also add or remove existing managed data identifiers from the set. If we add
or remove a managed data identifier from the recommended set, we update this page to indicate the
nature and timing of the change. For automatic alerts about these changes, you can subscribe to
the RSS feed on the [Macie document history](doc-history.md "doc-history.md") page.

When you create a sensitive data discovery job, you specify which managed data identifiers you want the job to
use to analyze objects in Amazon Simple Storage Service (Amazon S3) buckets. To configure a job to use the recommended set
of managed data identifiers, choose the _Recommended_ option when
you create the job. The job will then automatically use all the managed data identifiers that are
in the recommended set when the job starts to run. If you configure a job to run more than once,
each run will automatically use all the managed data identifiers that are in the recommended set
when the run starts.

The following topics list the managed data identifiers that are currently in the recommended
set, organized by sensitive data category and type. They specify the unique identifier (ID) for
each managed data identifier in the set. This ID describes the type of sensitive data that a
managed data identifier is designed to detect, for example: `PGP_PRIVATE_KEY` for PGP
private keys and `USA_PASSPORT_NUMBER` for US passport numbers.

###### Topics

- [Credentials](#discovery-jobs-mdis-recommended-credentials "#discovery-jobs-mdis-recommended-credentials")
- [Financial
  information](#discovery-jobs-mdis-recommended-financial "#discovery-jobs-mdis-recommended-financial")
- [Personally identifiable information (PII)](#discovery-jobs-mdis-recommended-pii "#discovery-jobs-mdis-recommended-pii")
- [Updates to the recommended
  set](#discovery-jobs-mdis-recommended-updates "#discovery-jobs-mdis-recommended-updates")
  For details about specific managed data identifiers or a complete list of all the managed data identifiers that Macie
  currently provides, see [Using managed data
  identifiers](managed-data-identifiers.md "managed-data-identifiers.md").

## Credentials

To detect occurrences of credentials data in S3 objects, the recommended set uses the
following managed data identifiers.

| Sensitive data type                                 | Managed data identifier ID                                                                                                                                                                                                         |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS secret access key                               | `AWS_CREDENTIALS`                                                                                                                                                                                                                  |
| HTTP Basic Authorization header                     | `HTTP_BASIC_AUTH_HEADER`                                                                                                                                                                                                           |
| OpenSSH private key                                 | `OPENSSH_PRIVATE_KEY`                                                                                                                                                                                                              |
| PGP private key                                     | `PGP_PRIVATE_KEY`                                                                                                                                                                                                                  |
| Public Key Cryptography Standard (PKCS) private key | `PKCS`                                                                                                                                                                                                                             |
| PuTTY private key                                   | `PUTTY_PRIVATE_KEY`                                                                                                                                                                                                                | ## Financial information To detect occurrences of financial information in S3 objects, the recommended set uses the following managed data identifiers.                                                                                                                                                        |
| Sensitive data type                                 | Managed data identifier ID                                                                                                                                                                                                         |
| ---                                                 | ---                                                                                                                                                                                                                                |
| Credit card magnetic stripe data                    | `CREDIT_CARD_MAGNETIC_STRIPE`                                                                                                                                                                                                      |
| Credit card number                                  | `CREDIT_CARD_NUMBER` (for credit card numbers in proximity of a keyword)                                                                                                                                                           | ## Personally identifiable information (PII) To detect occurrences of personally identifiable information (PII) in S3 objects, the recommended set uses the following managed data identifiers.                                                                                                                |
| Sensitive data type                                 | Managed data identifier ID                                                                                                                                                                                                         |
| ---                                                 | ---                                                                                                                                                                                                                                |
| Driver’s license identification number              | `CANADA_DRIVERS_LICENSE, DRIVERS_LICENSE` (for the US), `UK_DRIVERS_LICENSE`                                                                                                                                                       |
| Electoral roll number                               | `UK_ELECTORAL_ROLL_NUMBER`                                                                                                                                                                                                         |
| National identification number                      | `FRANCE_NATIONAL_IDENTIFICATION_NUMBER, GERMANY_NATIONAL_IDENTIFICATION_NUMBER, ITALY_NATIONAL_IDENTIFICATION_NUMBER, SPAIN_DNI_NUMBER`                                                                                            |
| National Insurance Number (NINO)                    | `UK_NATIONAL_INSURANCE_NUMBER`                                                                                                                                                                                                     |
| Passport number                                     | `CANADA_PASSPORT_NUMBER, FRANCE_PASSPORT_NUMBER, GERMANY_PASSPORT_NUMBER, ITALY_PASSPORT_NUMBER, SPAIN_PASSPORT_NUMBER, UK_PASSPORT_NUMBER, USA_PASSPORT_NUMBER`                                                                   |
| Social Insurance Number (SIN)                       | `CANADA_SOCIAL_INSURANCE_NUMBER`                                                                                                                                                                                                   |
| Social Security number (SSN)                        | `SPAIN_SOCIAL_SECURITY_NUMBER, USA_SOCIAL_SECURITY_NUMBER`                                                                                                                                                                         |
| Taxpayer identification or reference number         | `AUSTRALIA_TAX_FILE_NUMBER, BRAZIL_CPF_NUMBER, FRANCE_TAX_IDENTIFICATION_NUMBER, GERMANY_TAX_IDENTIFICATION_NUMBER, SPAIN_NIE_NUMBER, SPAIN_NIF_NUMBER, SPAIN_TAX_IDENTIFICATION_NUMBER, USA_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER` | ## Updates to the recommended set The following table describes changes to the set of managed data identifiers that we recommend for sensitive data discovery jobs. For automatic alerts about these changes, subscribe to the RSS feed on the [Macie document history](doc-history.md "doc-history.md") page. |
| Change                                              | Description                                                                                                                                                                                                                        | Date                                                                                                                                                                                                                                                                                                           |
| ---                                                 | ---                                                                                                                                                                                                                                | ---                                                                                                                                                                                                                                                                                                            |
| General availability                                | Initial release of the recommended set.                                                                                                                                                                                            | June 27, 2023                                                                                                                                                                                                                                                                                                  |
