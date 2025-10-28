# Best practice 3.1 – Privacy by Design

Privacy by Design is an approach in system engineering that
takes privacy into account throughout the whole engineering
process. It especially focuses on systems or applications
that capture and process personal data.

There is an increased focus on ensuring that personal data
is processed lawfully, fairly, and in a transparent manner
in relation to the data subject. Another concern is that the
data processing is adequate, relevant, and limited in
relation to the purpose for which the information is used.

## Suggestion 3.1.1 – Data minimization

Organizations should only receive, process, and store information that is relevant for the task rather than processing all information when only a portion of the file is required. For example, if a client provided a full extract of all information from their source system containing sensitive personal information, and if a portion of the file is deemed irrelevant in meeting the overall project requirements, the remainder of the file should not be stored or processed.

Data minimization coincides with data access controls in that applying data minimization rules can be implemented using data access controls. A suggestion is to create and maintain a data access matrix aligned with your data classification catalogs. This helps ensure that the correct groups of people have access to the right data. As most compliant frameworks encourage evidence that rules have been applied, a data access matrix can demonstrate to auditors that your organization has gone through the proper thought process to determine who can access what information.

Data minimization can be applied at the point of capture. It can also be applied at the point of access by presenting a restricted data model or implementing role-based access controls (RBAC). For more information on controlling data access, see [4 – Implement data access control](design-principle-4.md "design-principle-4.md").

Test and user acceptance test (UAT) environments, as well
as training model datasets, must have a restricted dataset
and not contain any personal information. If the structure
of the data model must remain the same as production, then
consider anonymizing or masking information to meet your
data minimization requirements.

It is common practice to create test and development
environments using a backup of production and restore to
the respective development or test environment. If this is
the case, anonymization of personally identifiable
information (PII) and other sensitive information must
occur using inbuilt logic or services such as AWS Glue DataBrew to obfuscate the information.

For more details, refer to the following documentation:

- Amazon Redshift RBAC -
  [Amazon Redshift role-based access control](../../../redshift/latest/dg/t_Roles.md "../../../redshift/latest/dg/t_Roles.md")s
- AWS Lake Formation RBAC -
  [Lake Formation role-based access controls](../../../lake-formation/latest/dg/access-control-overview.md "../../../lake-formation/latest/dg/access-control-overview.md")
- Amazon Athena RBAC -
  [Amazon Athena fine-grained access controls](../../../athena/latest/ug/fine-grained-access-to-glue-resources.md "../../../athena/latest/ug/fine-grained-access-to-glue-resources.md")
- AWS Glue DataBrew -
  [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/ "https://aws.amazon.com/glue/features/databrew/") Visual Data Preparation

## Suggestion 3.1.2 – Anonymization, pseudonymization, and tokenization

Anonymization, pseudonymization, or tokenisation refers to the method of either rendering data anonymous or encoding data in such a manner that the data is no longer identifiable

### Suggestion 3.1.2.1 – Anonymization

**Anonymization is defined as the process of turning data into a
form that does not identify individuals and where identification is not likely to take
place.**

This results in changing personal data into data that is no longer personal. An
important factor in this process is that the anonymization must be irreversible. The
anonymized value should be supported by the current field data type, have similar
length, and retain some characteristics of the original value. For example, if a Vehicle
Registration Number such as `OU51 SMR` was being anonymized, the result would
look similar to `BB88 9AA`.

Organizations need the ability to anonymize full datasets as well as single records.
Single record anonymization functionality can help deliver right to erasure and meet
data retention requirements. In this case, full batch anonymization is typically used
when obfuscating development and UAT environments.

The function to anonymize information should support the flexibility to anonymize
certain fields, but not all.

Operational databases, reporting databases, and analytical data marts should all be
considered for anonymization, although reports and analytical cubes should never
typically contain PII information regardless.

Audit the reason why information was anonymized, for example, data portability, or
data retention removal. The time, date, and user ID of when and who the anonymization
process has affected should be recorded in an audit table.

For more details, see AWS Big Data Blog: [Anonymize and manage data in your data lake with Amazon Athena and AWS Lake Formation](https://aws.amazon.com/blogs/big-data/anonymize-and-manage-data-in-your-data-lake-with-amazon-athena-and-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/anonymize-and-manage-data-in-your-data-lake-with-amazon-athena-and-aws-lake-formation/")

### Suggestion 3.1.2.2 –

Pseudonymization

**Pseudonymized data is not the same as anonymized data.**

When data has been pseudonymized, it still retains a level of detail in the target
data that allows tracking back of the data to its original state. With anonymized data,
the level of detail is reduced rendering a reverse compilation impossible.
Pseudonymization is the processing of personal data in such a way that the data can only
be attributed to a specific data subject by using additional information. To
pseudonymize a dataset, the additional information must be kept separately and subject
to technical and organizational measures to ensure non-attribution to an identified or
identifiable person.

In summary, pseudonymized data is a privacy-enhancing technique where directly
identifying data, such as IP addresses and contact information, are held separately and
securely from processed data to ensure non-attribution. Similar to anonymization,
referential integrity must not be affected. Therefore, both of the following are
required: an audit trail of the pseudonymization process, and a pseudonymization
function that supports both single item and batch processing.

For more detail, see [Amazon Redshift Data Masking](../../../redshift/latest/dg/t_ddm.md "../../../redshift/latest/dg/t_ddm.md").

### Suggestion 3.1.2.3 –

Tokenization

_Tokenization_, when applied to data security, is
the process of substituting a sensitive data element with a non-sensitive equivalent.
This is referred to as a token, which has no extrinsic or exploitable meaning or value.
The token is a reference that maps back to the sensitive data through a tokenization
system. Tokenization is typically used in finance to tokenize the payment account number
(PAN).

For more details, refer to the following information:

- AWS Blog – [AWS Glue DataBrew detection data masking transformations](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-glue-databrew-detection-data-masking-transformations/ "https://aws.amazon.com/about-aws/whats-new/2021/11/aws-glue-databrew-detection-data-masking-transformations/")
- AWS Blog - [Data Tokenization with Amazon Redshift and Protegrity](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/ "https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/")

## Suggestion 3.1.3 – Rights of the individual, citizen, or subject

Your organization should consider the process to address
the rights of the individual, citizen, or subject for
their respective regional regulation.

### Suggestion 3.1.3.1 – Subject Access

Request (SAR)

This particular right is for an individual to request
information from the data controller, that is, how their
personal data is being processed. If an individual’s
information is being processed, the personal data and
associated metadata must be provided to that individual.

If the individual’s information is stored in a database, then an automated process, such as a stored procedure or User-Defined Function (UDF), should be developed to answer the Subject Access Request (SAR). There will, however, be situations when the individual’s information is stored in Amazon S3. If the information is stored in Amazon S3, the proposed solution to identify which S3 object contains the respective information is to build a lookup table in a database containing the reference number, individual contact details, and the S3 object location. This approach allows your organization to ingest the information into Amazon EMR, infer the schema using Apache Spark, and extract the information required to fulfill the request. Alternatively, your organization must process all S3 objects to identify the information to fulfill the request.

If your regional regulations require that your organization handle a right to data portability request, then the SAR logic can double up to support that as well.

For more details, see Apache Spark Documentation -
[Inferring
the Schema Using Reflection](https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#:~:text=Inferring%20the%20Schema%20Using%20Reflection,-Scala&text=The%20Scala%20interface%20for%20Spark,the%20names%20of%20the%20columns. "https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#:~:text=Inferring%20the%20Schema%20Using%20Reflection,-Scala&text=The%20Scala%20interface%20for%20Spark,the%20names%20of%20the%20columns.")

### Suggestion 3.1.3.2

– Right to be forgotten or erasure

Individuals have the right to erasure (the right to be forgotten), where an
individual can request that all of their personal data is erased by the data controller
organization. In some countries, there are instances where the data controller can
refuse to comply with a right to erasure request, such as where the data is used for
financial governance.

The right to erasure does not strictly mean that the individual’s information must
be deleted. Instead, it can be permanently masked so that the personal data is no longer
in the clear and the update is irreversible.

The organization must consider all data repositories when responding to a SAR as an
individual’s information can reside in back up and source system databases. All these
records must have the individual’s information removed or anonymized.

If there are concerns about the impact of database referential integrity being
affected by removing the individual’s information, then you can consider anonymization
of the specific data attributes for the given individual. There are benefits to
anonymization, such as being able to maintain an audit history of what actions have been
performed against the individual by referencing a system ID. The same steps that are
performed in production environments must also be run in UAT, development, OLTP, and
back up repositories.

The schedule of running the procedure in the other environments depends on the
refresh schedules of those other environments.
