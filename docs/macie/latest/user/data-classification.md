# Discovering sensitive data with Macie

With Amazon Macie, you can automate discovery, logging, and reporting of sensitive data in
your Amazon Simple Storage Service (Amazon S3) data estate. You can do this in two ways: by configuring Macie to
perform automated sensitive data discovery, and by creating and running sensitive data discovery jobs.

Automated sensitive data discovery provides broad visibility into where sensitive data might reside in your
Amazon S3 data estate. With this option, Macie evaluates your S3 bucket inventory on a daily
basis and uses sampling techniques to identify and select representative S3 objects from
your buckets. Macie then retrieves and analyzes the selected objects, inspecting them for
sensitive data. For more information, see [Performing automated sensitive data
discovery](discovery-asdd.md "discovery-asdd.md").

Sensitive data discovery jobs provide deeper, more targeted analysis. With this option,
you define the breadth and depth of the analysis—specific S3 buckets that you select
or buckets that match specific criteria. You can also refine the scope of the analysis by
choosing options such as custom criteria that derive from properties of S3 objects. In
addition, you can configure a job to run only once for on-demand analysis and assessment, or
on a recurring basis for periodic analysis, assessment, and monitoring. For more
information, see [Running sensitive data discovery
jobs](discovery-jobs.md "discovery-jobs.md").

With either option, automated sensitive data discovery or sensitive data discovery jobs, you can configure Macie to analyze S3
objects by using managed data identifiers that it provides, custom data identifiers that you
define, or a combination of the two. You can also fine tune the analysis with allow lists.
When you configure settings for automated sensitive data discovery or a sensitive data discovery job, you specify which to use:

- **Managed data identifiers**
  – These are built-in criteria and techniques that are designed to detect
  specific types of sensitive data. For example, they can detect credit card numbers,
  AWS secret access keys, and passport numbers for particular countries and regions.
  They can detect a large and growing list of sensitive data types for many countries
  and regions. This includes multiple types of personally identifiable information
  (PII), financial information, and credentials data. For more information, see [Using managed data
  identifiers](managed-data-identifiers.md "managed-data-identifiers.md").
- **Custom data identifiers** – These are custom
  criteria that you define to detect sensitive data. Each custom data identifier
  specifies a regular expression (_regex_) that
  defines a text pattern to match and, optionally, character sequences and a proximity
  rule that refine the results. You can use them to detect sensitive data that
  reflects your particular scenarios, intellectual property, or proprietary
  data—for example, employee IDs, customer account numbers, or internal data
  classifications. For more information, see [Building custom data
  identifiers](custom-data-identifiers.md "custom-data-identifiers.md").
- **Allow lists** – These specify text and text
  patterns that you want Macie to ignore. You can use them to specify sensitive data
  exceptions for your particular scenarios or environment—for example, public
  names or phone numbers for your organization, or sample data that your organization
  uses for testing. If Macie finds text that matches an entry or pattern in an allow
  list, Macie doesn’t report that occurrence of text. This is the case even if the
  text matches the criteria of a managed or custom data identifier. For more
  information, see [Defining sensitive data exceptions with allow
  lists](allow-lists.md "allow-lists.md").
  When Macie analyzes an S3 object, Macie retrieves the latest version of the object from
  Amazon S3, and then inspects the object's contents for sensitive data. Macie can analyze an
  object if the following is true:

- The object uses a supported file or storage format and it's stored in an S3
  general purpose bucket using a supported storage class. For more information, see
  [Supported storage classes and
  formats](discovery-supported-storage.md "discovery-supported-storage.md").
- If the object is encrypted, it’s encrypted with a key that Macie can access and is
  allowed to use. For more information, see [Analyzing encrypted S3
  objects](discovery-supported-encryption-types.md "discovery-supported-encryption-types.md").
- If the object is stored in a bucket that has a restrictive bucket policy, the
  policy allows Macie to access objects in the bucket. For more information, see [Allowing Macie to access S3
  buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").
  To help you meet and maintain compliance with your data security and privacy requirements,
  Macie produces records of the sensitive data that it finds and the analysis that it
  performs—_sensitive data findings_ and _sensitive data discovery results_. A _sensitive data finding_ is a detailed report of sensitive data that Macie
  found in an S3 object. A _sensitive data discovery result_
  is a record that logs details about the analysis of an object. Each type of record adheres
  to a standardized schema, which can help you query, monitor, and process them by using other
  applications, services, and systems as necessary.

###### Tip

Although Macie is optimized for Amazon S3, you can use it to discover sensitive data in
resources that you currently store elsewhere. You can do this by moving the data to Amazon S3
temporarily or permanently. For example, export Amazon Relational Database Service or Amazon Aurora snapshots to Amazon S3
in Apache Parquet format. Or export an Amazon DynamoDB table to Amazon S3. You can then create a
job to analyze the data in Amazon S3.

###### Topics

- [Using managed data
  identifiers](managed-data-identifiers.md "managed-data-identifiers.md")
- [Building custom data
  identifiers](custom-data-identifiers.md "custom-data-identifiers.md")
- [Defining sensitive data exceptions with allow
  lists](allow-lists.md "allow-lists.md")
- [Performing automated sensitive data
  discovery](discovery-asdd.md "discovery-asdd.md")
- [Running sensitive data discovery
  jobs](discovery-jobs.md "discovery-jobs.md")
- [Analyzing encrypted S3
  objects](discovery-supported-encryption-types.md "discovery-supported-encryption-types.md")
- [Storing and retaining
  sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md")
- [Supported storage classes and
  formats](discovery-supported-storage.md "discovery-supported-storage.md")
