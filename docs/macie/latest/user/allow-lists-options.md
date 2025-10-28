# Configuration options and requirements for allow

lists

In Amazon Macie, you can use allow lists to specify text or text patterns that you want Macie to
ignore when it inspects Amazon Simple Storage Service (Amazon S3) objects for sensitive data. Macie provides options for two
types of allow lists, predefined text and regular expressions.

A list of predefined text is helpful if you want Macie to ignore specific words, phrases, and
other kinds of character sequences that you don't consider sensitive. Examples are: the names of
public representatives for your organization, specific phone numbers, or specific sample data that
your organization uses for testing. If Macie finds text that matches the criteria of a managed or
custom data identifier and the text also matches an entry in an allow list, Macie doesn't report
that occurrence of text in sensitive data findings, statistics, and other types of results.

A regular expression (_regex_) is helpful if you want Macie to ignore text
that varies or is likely to change while also adhering to a common pattern. The regex specifies a
text pattern to ignore. Examples are: public phone numbers for your organization, email addresses
for your organization's domain, or patterned sample data that your organization uses for testing.
If Macie finds text that matches the criteria of a managed or custom data identifier and the text
also matches a regex pattern in an allow list, Macie doesn't report that occurrence of text in
sensitive data findings, statistics, and other types of results.

You can create and use both types of allow lists in all the AWS Regions where Macie is
currently available except the Asia Pacific (Osaka) Region. As you create and manage allow lists, keep the
following options and requirements in mind. Also note that list entries and regex patterns for
mailing addresses aren't supported.

###### Topics

- [Options and requirements for lists of predefined
  text](allow-lists-options.md#allow-lists-options-s3list "allow-lists-options.md#allow-lists-options-s3list")
  - [Syntax requirements](allow-lists-options.md#allow-lists-options-s3list-syntax "allow-lists-options.md#allow-lists-options-s3list-syntax")
  - [Storage requirements](allow-lists-options.md#allow-lists-options-s3list-storage "allow-lists-options.md#allow-lists-options-s3list-storage")
  - [Encryption/Decryption
    requirements](allow-lists-options.md#allow-lists-options-s3list-encryption "allow-lists-options.md#allow-lists-options-s3list-encryption")
  - [Design considerations and
    recommendations](allow-lists-options.md#allow-lists-options-s3list-notes "allow-lists-options.md#allow-lists-options-s3list-notes")

- [Options and requirements for regular
  expressions](allow-lists-options.md#allow-lists-options-regex "allow-lists-options.md#allow-lists-options-regex")
  - [Syntax support and recommendations](allow-lists-options.md#allow-lists-options-regex-syntax "allow-lists-options.md#allow-lists-options-regex-syntax")
  - [Examples](allow-lists-options.md#allow-lists-options-regex-examples "allow-lists-options.md#allow-lists-options-regex-examples")

## Options and requirements for lists of predefined

text

For this type of allow list, you provide a line-delimited plaintext file that lists specific
character sequences to ignore. The list entries are typically words, phrases, and other kinds of
character sequences that you don’t consider sensitive, aren’t likely to change, and don’t
necessarily adhere to a specific pattern. If you use this type of list, Amazon Macie doesn't report
occurrences of text that exactly match an entry in the list. Macie treats each list entry as a
string literal value.

To use this type of allow list, start by creating the list in a text editor and saving it as
a plaintext file. Then upload the list to an S3 general purpose bucket. Also ensure that the
storage and encryption settings for the bucket and the object allow Macie to retrieve and decrypt
the list. Then [create and configure settings for the
list](allow-lists-create.md "allow-lists-create.md") in Macie.

After you configure the settings in Macie, we recommend that you test the allow list with a
small, representative set of data for your account or organization. To test a list, you can [create a one-time job](discovery-jobs-create.md "discovery-jobs-create.md"). Configure the job to use the list
in addition to the managed and custom data identifiers that you typically use to analyze data.
You can then review the job's results—sensitive data findings, sensitive data discovery
results, or both. If the job's results differ from what you expect, you can change and test the
list until the results are what you expect.

After you finish configuring and testing an allow list, you can create and configure
additional jobs to use it, or add it to your settings for automated sensitive data discovery. When those jobs start to
run or the next automated discovery analysis cycle starts, Macie retrieves the latest version of the list from
Amazon S3 and stores it in temporary memory. Macie then uses this temporary copy of the list when it
inspects S3 objects for sensitive data. When a job finishes running or the analysis cycle is
complete, Macie permanently deletes its copy of the list from memory. The list doesn't persist in
Macie. Only the list's settings persist in Macie.

###### Important

Because lists of predefined text don't persist in Macie, it's important to [check the status of your allow lists](allow-lists-status-check.md "allow-lists-status-check.md") periodically. If
Macie can’t retrieve or parse a list that you configured a job or automated discovery to use, Macie doesn’t
use the list. This might produce unexpected results, such as sensitive data findings for text
that you specified in the list.

###### Topics

- [Syntax requirements](#allow-lists-options-s3list-syntax "#allow-lists-options-s3list-syntax")
- [Storage requirements](#allow-lists-options-s3list-storage "#allow-lists-options-s3list-storage")
- [Encryption/Decryption
  requirements](#allow-lists-options-s3list-encryption "#allow-lists-options-s3list-encryption")
- [Design considerations and
  recommendations](#allow-lists-options-s3list-notes "#allow-lists-options-s3list-notes")

### Syntax requirements

When you create this type of allow list, note the following requirements for the list's
file:

- The list must be stored as a plaintext (`text/plain`) file, such as a .txt,
  .text, or .plain file.
- The list must use line breaks to separate individual entries. For example:

```
Akua Mansa
John Doe
Martha Rivera
425-555-0100
425-555-0101
425-555-0102
```

Macie treats each line as a single, distinct entry in the list. The file can also contain
blank lines to improve readability. Macie skips blank lines when it parses the file.

- Each entry can contain 1–90 UTF–8 characters.
- Each entry must be a complete, exact match for the text to ignore. Macie doesn't support
  use of wildcard characters or partial values for entries. Macie treats each entry as a string
  literal value. Matches aren't case sensitive.
- The file can contain 1–100,000 entries.
- The total storage size of the file can't exceed 35 MB.

### Storage requirements

As you add and manage allow lists in Amazon S3, note the following storage requirements and
recommendations:

- **Regional support** – An allow list must be stored
  in a bucket that's in the same AWS Region as your Macie account. Macie can’t access an allow
  list if it’s stored in a different Region.
- **Bucket ownership** – An allow list must be stored
  in a bucket that's owned by your AWS account. If you want other accounts to use the same
  allow list, consider creating an Amazon S3 replication rule to replicate the list to buckets that
  are owned by those accounts. For information about replicating S3 objects, see [Replicating
  objects](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") in the _Amazon Simple Storage Service User Guide_.

In addition, your AWS Identity and Access Management (IAM) identity must have read access to the bucket and
object that store the list. Otherwise, you won't be allowed to create or update the list's
settings or check the list's status by using Macie.

- **Storage types and classes** – An allow list must be
  stored in a general purpose bucket, not a directory bucket. In addition, it must be stored
  using one of the following storage classes: Reduced Redundancy (RRS), S3 Glacier Instant Retrieval, S3 Intelligent-Tiering, S3 One Zone-IA, S3 Standard, or S3 Standard-IA.
- **Bucket policies** – If you store an allow list in a
  bucket that has a restrictive bucket policy, ensure that the policy allows Macie to retrieve
  the list. To do this, you can add a condition for the Macie service-linked role to the bucket
  policy. For more information, see [Allowing Macie to access S3
  buckets and objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md").

Also ensure that the policy allows your IAM identity to have read access to the bucket.
Otherwise, you won't be allowed to create or update the list's settings or check the list's
status by using Macie.

- **Object paths** – If you store more than one allow
  list in Amazon S3, the object path for each list must be unique. In other words, each allow list
  must be stored separately in its own S3 object.
- **Versioning** – When you add an allow list to a
  bucket, we recommend that you also enable versioning for the bucket. You can then use date and
  time values to correlate versions of the list with the results of sensitive data discovery
  jobs and automated sensitive data discovery cycles that use the list. This can help with data privacy and protection
  audits or investigations that you perform.
- **Object Lock** – To prevent an allow list from being
  deleted or overwritten for a certain amount of time or indefinitely, you can enable Object
  Lock for the bucket that stores the list. Enabling this setting doesn’t prevent Macie from
  accessing the list. For information about this setting, see [Locking objects with Object Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") in the
  _Amazon Simple Storage Service User Guide_.

### Encryption/Decryption

requirements

If you encrypt an allow list in Amazon S3, the permissions policy for the [Macie service-linked role](service-linked-roles.md "service-linked-roles.md") typically grants Macie the
permissions that it needs to decrypt the list. However, this depends on the type of encryption
that’s used:

- If a list is encrypted using server-side encryption with an Amazon S3 managed key (SSE-S3),
  Macie can decrypt the list. The service-linked role for your Macie account grants Macie the
  permissions that it needs.
- If a list is encrypted using server-side encryption with an AWS managed AWS KMS key
  (DSSE-KMS or SSE-KMS), Macie can decrypt the list. The service-linked role for your Macie
  account grants Macie the permissions that it needs.
- If a list is encrypted using server-side encryption with a customer managed
  AWS KMS key (DSSE-KMS or SSE-KMS), Macie can decrypt the list only if you allow Macie to
  use the key. To learn how to do this, see [Allowing Macie to
  use a customer managed AWS KMS key](discovery-supported-encryption-types.md#discovery-supported-encryption-cmk-configuration "discovery-supported-encryption-types.md#discovery-supported-encryption-cmk-configuration").

###### Note

You can encrypt a list with a customer managed AWS KMS key in an external key store.
However, the key might then be slower and less reliable than a key that’s managed entirely
within AWS KMS. If latency or an availability issue prevents Macie from decrypting the list,
Macie doesn’t use the list when it analyzes S3 objects. This might produce unexpected
results, such as sensitive data findings for text that you specified in the list. To reduce
this risk, consider storing the list in an S3 bucket that’s configured to use the key as an
S3 Bucket Key.

For information about using KMS keys in external key stores, see [External key
stores](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md") in the _AWS Key Management Service Developer Guide_. For
information about using S3 Bucket Keys, see [Reducing the cost of SSE-KMS with Amazon S3
Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") in the _Amazon Simple Storage Service User Guide_.

- If a list is encrypted using server-side encryption with a customer-provided key (SSE-C)
  or client-side encryption, Macie can’t decrypt the list. Consider using SSE-S3, DSSE-KMS, or
  SSE-KMS encryption instead.

If a list is encrypted with an AWS managed KMS key or a customer managed KMS key,
your AWS Identity and Access Management (IAM) identity must also be allowed to use the key. Otherwise, you won't be
allowed to create or update the list's settings or check the list's status by using Macie. To
learn how to check or change the permissions for a KMS key, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

For detailed information about encryption options for Amazon S3 data, see [Protecting data with
encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the _Amazon Simple Storage Service User Guide_.

### Design considerations and

recommendations

In general, Macie treats each entry in an allow list as a string literal value. That is to
say, Macie ignores each occurrence of text that exactly matches a complete entry in an allow
list. Matches aren't case sensitive.

However, Macie uses the entries as part of a larger data extraction and analysis framework.
The framework includes machine learning and pattern matching functions that factor dimensions
such as grammatical and syntactical variations and, in many cases, keyword proximity. The
framework also factors an S3 object’s file type or storage format. Therefore, keep the following
considerations and recommendations in mind as you add and manage the entries in an allow
list.

Prepare for different file types and storage
formats

For unstructured data, such as text in an Adobe Portable Document Format (.pdf) file,
Macie ignores text that exactly matches a complete entry in an allow list, including text
that spans multiple lines or pages.

For structured data, such as columnar data in a CSV file or record-based data in a JSON
file, Macie ignores text that exactly matches a complete entry in an allow list if all the
text is stored in a single field, cell, or array. This requirement doesn’t apply to
structured data that’s stored in an otherwise unstructured file, such as a table in a .pdf
file.

For example, consider the following content in a CSV file:

```
Name,Account ID
Akua Mansa,111111111111
John Doe,222222222222
```

If `Akua Mansa` and `John Doe` are entries in an allow list, Macie
ignores those names in the CSV file. The complete text of each list entry is stored in a
single `Name` field.

Conversely, consider a CSV file that contains the following columns and fields:

```
First Name,Last Name,Account ID
Akua,Mansa,111111111111
John,Doe,222222222222
```

If `Akua Mansa` and `John Doe` are entries in an allow list, Macie
doesn’t ignore those names in the CSV file. None of the fields in the CSV file contain the
complete text of an entry in the allow list.

Include common variations

Add entries for common variations of numeric data, proper nouns, terms, and alphanumeric
character sequences. For example, if you add names or phrases that contain only one space
between words, also add variations that include two spaces between words. Similarly, add
words and phrases that do and don’t contain special characters, and consider including common
syntactical and semantic variations.

For the US phone number _425-555-0100_, for example,
you might add these entries to an allow list:

```
425-555-0100
425.555.0100
(425) 555-0100
+1-425-555-0100
```

For the date _February 1, 2022_ in a multinational
context, you might add entries that include common syntactical variations for English and
French, including variations that do and don't include special characters:

```
February 1, 2022
1 février 2022
1 fevrier 2022
Feb 01, 2022
1 fév 2022
1 fev 2022
02/01/2022
01/02/2022
```

For names of people, include entries for various forms of a name that you don't consider
sensitive. For example, include: the first name followed by the last name; the last name
followed by the first name, the first and last name separated by one space; the first and
last name separated by two spaces; and nicknames.

For the name _Martha Rivera_, for example, you might
add:

```
Martha Rivera
Martha  Rivera
Rivera, Martha
Rivera,  Martha
Rivera Martha
Rivera  Martha
```

If you want to ignore variations of a specific name that contains many parts, create an
allow list that uses a regular expression instead. For example, for the name _Dr. Martha Lyda Rivera, PhD_, you might use the following regular
expression: `^(Dr. )?Martha\s(Lyda|L\.)?\s?Rivera,?( PhD)?$`.

## Options and requirements for regular

expressions

For this type of allow list, you specify a regular expression (_regex_) that defines a text pattern to ignore. For example, you might specify the
pattern for your organization's public phone numbers, email addresses for your organization’s
domain, or patterned sample data that your organization uses for testing. The regex defines a
common pattern for a specific kind of data that you don’t consider sensitive. If you use this
type of allow list, Amazon Macie doesn't report occurrences of text that completely match the
specified pattern. Unlike an allow list that specifies predefined text to ignore, you create and
store the regex and all other list settings in Macie.

When you create or update this type of allow list, you can test the list’s regex with sample
data before you save the list. We recommend that you do this with multiple sets of sample data.
If you create a regex that’s too general, Macie might ignore occurrences of text that you
consider sensitive. If a regex is too specific, Macie might not ignore occurrences of text that
you don’t consider sensitive. To protect against malformed or long-running expressions, Macie
also compiles and tests the regex against a collection of sample text automatically, and notifies
you of issues to address.

For additional testing, we recommend that you also test the list’s regex with a small,
representative set of data for your account or organization. To do this, you can [create a one-time job](discovery-jobs-create.md "discovery-jobs-create.md"). Configure the job to use the list
in addition to the managed and custom data identifiers that you typically use to analyze data.
You can then review the job's results—sensitive data findings, sensitive data discovery
results, or both. If the job's results differ from what you expect, you can change and test the
regex until the results are what you expect.

After you configure and test an allow list, you can create and configure additional jobs to
use it, or add it to your settings for automated sensitive data discovery. When those job run or Macie performs automated discovery,
Macie uses the latest version of the list's regex to analyze data.

###### Topics

- [Syntax support and recommendations](#allow-lists-options-regex-syntax "#allow-lists-options-regex-syntax")
- [Examples](#allow-lists-options-regex-examples "#allow-lists-options-regex-examples")

### Syntax support and recommendations

An allow list can specify a regular expression (_regex_)
that contains as many as 512 characters. Macie supports a subset of the regex pattern syntax
provided by the [Perl Compatible Regular Expressions (PCRE)
library](https://www.pcre.org/ "https://www.pcre.org/"). Of the constructs provided by the PCRE library, Macie doesn’t support the
following pattern elements:

- Backreferences
- Capturing groups
- Conditional patterns
- Embedded code
- Global pattern flags, such as `/i`, `/m`, and
  `/x`
- Recursive patterns
- Positive and negative look-behind and look-ahead zero-width assertions, such as
  `?=`, `?!`, `?<=`, and `?<!`

To create effective regex patterns for allow lists, note the following tips and
recommendations:

- **Anchors** – Use anchors (`^` or
  `$`) only if you expect the pattern to appear at the beginning or end of a file,
  not the beginning or end of a line.
- **Bounded repeats** – For performance reasons, Macie
  limits the size of bounded repeat groups. For example, `\d{100,1000}` won’t compile
  in Macie. To approximate this functionality, you can use an open-ended repeat such as
  `\d{100,}`.
- **Case insensitivity** – To make parts of a pattern
  case insensitive, you can use the `(?i)` construct instead of the `/i`
  flag.
- **Performance** – There’s no need to optimize prefixes
  or alternations manually. For example, changing `/hello|hi|hey/` to
  `/h(?:ello|i|ey)/` won’t improve performance.
- **Wildcards** – For performance reasons, Macie limits
  the number of repeated wildcards. For example, `a*b*a*` won’t compile in
  Macie.
- **Alternation** – To specify more than one pattern in a
  single allow list, you can use the alternation operator (`|`) to concatenate the
  patterns. If you do this, Macie uses OR logic to combine the patterns and form a new pattern.
  For example, if you specify `(apple|orange)`, Macie recognizes both _apple_ and _orange_ as a match and
  ignores occurrences of both words. If you concatenate patterns, be sure to limit the overall
  length of the concatenated expression to 512 or fewer characters.

Finally, when you develop the regex, design it to accommodate different file types and
storage formats. Macie uses the regex as part of a larger data extraction and analysis
framework. The framework factors an S3 object’s file type or storage format. For structured
data, such as columnar data in a CSV file or record-based data in a JSON file, Macie ignores
text that completely matches the pattern only if all the text is stored in a single field, cell,
or array. This requirement doesn’t apply to structured data that’s stored in an otherwise
unstructured file, such as a table in an Adobe Portable Document Format (.pdf) file. For
unstructured data, such as text in a .pdf file, Macie ignores text that completely matches the
pattern, including text that spans multiple lines or pages.

### Examples

The following examples demonstrate valid regex patterns for some common scenarios.

Email addresses

If you use a custom data identifier to detect email addresses, you can ignore email
addresses that you don't consider sensitive, such as email addresses for your
organization.

To ignore email addresses for a particular second-level and top-level domain, you can
use this pattern:

`[a-zA-Z0-9_.+\\-]+@`example`\.`com``

Where `example` is the name of the second-level domain and
`com` is the top-level domain. In this case, Macie matches and
ignores addresses such as *johndoe@example.com* and
*john.doe@example.com*.

To ignore email addresses for a particular domain in any generic top-level domain
(gTLD), such as _.com_ or _.gov_, you can use this pattern:

`[a-zA-Z0-9_.+\\-]+@`example`\.[a-zA-Z]{2,}`

Where `example` is the name of the domain. In this case, Macie
matches and ignores addresses such as *johndoe@example.com*,
*john.doe@example.gov*, and *johndoe@example.edu*.

To ignore email addresses for a particular domain in any one country code top-level
domain (ccTLD), such as _.ca_ for Canada or _.au_ for Australia, you can use this pattern:

`[a-zA-Z0-9_.+\\-]+@`example`\.(`ca`|`au`)`

Where `example` is the name of the domain and
`ca` and `au` are specific ccTLDs to
ignore. In this case, Macie matches and ignores addresses such as *johndoe@example.ca* and *john.doe@example.au*.

To ignore email addresses that are for a particular domain and gTLD and include third-
and fourth-level domains, you can use this pattern:

`[a-zA-Z0-9_.+\\-]+@([a-zA-Z0-9-]+\.)?[a-zA-Z0-9-]+\.`example`\.`com``

Where `example` is the name of the domain and
`com` is the gTLD. In this case, Macie matches and ignores
addresses such as *johndoe@www.example.com* and *john.doe@www.team.example.com*.

Phone numbers

Macie provides managed data identifiers that can detect phone numbers for several
countries and regions. To ignore certain phone numbers, such as toll-free numbers or public
phone numbers for your organization, you can use patterns such as the following.

To ignore toll-free, US phone numbers that use the _800_ area code and are formatted as _(800)
###-####_:

`^\(?800\)?[ -]?\d{3}[ -]?\d{4}$`

To ignore toll-free, US phone numbers that use the _888_ area code and are formatted as _(888)
###-####_:

`^\(?888\)?[ -]?\d{3}[ -]?\d{4}$`

To ignore 10-digit, French phone numbers that include the _33_ country code and are formatted as _+33 ## ## ## ## ##_:

`^\+33 \d( \d\d){4}$`

To ignore US and Canadian phone numbers that use particular area and exchange codes,
don’t include a country code, and are formatted as _(###)
###-####_:

`^\(?`123`\)?[ -]?`555`[
 -]?\d{4}$`

Where `123` is the area code and `555`
is the exchange code.

To ignore US and Canadian phone numbers that use particular area and exchange codes,
include a country code, and are formatted as _+1 (###)
###-####_:

`^\+1\(?`123`\)?[ -]?`555`[
 -]?\d{4}$`

Where `123` is the area code and `555`
is the exchange code.
