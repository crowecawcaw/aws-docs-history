# Retrieving sensitive data samples with Macie

findings

To verify the nature of sensitive data that Amazon Macie reports in findings, you can
optionally configure and use Macie to retrieve and reveal samples of sensitive data reported
by individual findings. This includes sensitive data that Macie detects using [managed data identifiers](managed-data-identifiers.md "managed-data-identifiers.md"), and data that
matches the criteria of [custom data
identifiers](custom-data-identifiers.md "custom-data-identifiers.md"). The samples can help you tailor your investigation of an affected
Amazon Simple Storage Service (Amazon S3) object and bucket.

If you retrieve and reveal sensitive data samples for a finding, Macie performs the
following general tasks:

1. Verifies that the finding specifies the location of individual occurrences of
   sensitive data and the location of a corresponding [sensitive data discovery
   result](discovery-results-repository-s3.md "discovery-results-repository-s3.md").
2. Evaluates the corresponding sensitive data discovery result, checking the validity
   of the metadata for the affected S3 object and the location data for occurrences of
   sensitive data in the object.
3. By using data in the sensitive data discovery result, locates the first
   1–10 occurrences of sensitive data reported by the finding, and extracts the
   first 1–128 characters of each occurrence from the affected S3 object. If the
   finding reports multiple types of sensitive data, Macie does this for up to 100
   types.
4. Encrypts the extracted data with an AWS Key Management Service (AWS KMS) key that you specify.
5. Temporarily stores the encrypted data in a cache and displays the data for you to
   review. The data is encrypted at all times, both in transit and at rest.
6. Soon after extraction and encryption, permanently deletes the data from the cache
   unless additional retention is temporarily required to resolve an operational
   issue.
   If you choose to retrieve and reveal sensitive data samples for a finding again, Macie
   repeats these tasks to locate, extract, encrypt, store, and ultimately delete the
   samples.

Macie doesn't use the [Macie service-linked
role](service-linked-roles.md "service-linked-roles.md") for your account to perform these tasks. Instead, you use your AWS Identity and Access Management
(IAM) identity or allow Macie to assume an IAM role in your account. You can retrieve
and reveal sensitive data samples for a finding if you or the role is allowed to access the
requisite resources and data, and perform the requisite actions. All the requisite actions
are [logged in AWS CloudTrail](macie-cloudtrail.md "macie-cloudtrail.md").

###### Important

We recommend that you restrict access to this functionality by using [custom IAM policies](security-iam.md "security-iam.md"). For additional access control,
we recommend that you also create a dedicated AWS KMS key for encryption of sensitive
data samples that are retrieved, and restrict use of the key to only those principals
who must be allowed to retrieve and reveal sensitive data samples.

For recommendations and examples of policies that you might use to control access to
this functionality, see the following blog post on the _AWS
Security Blog_: [How
to use Amazon Macie to preview sensitive data in S3 buckets](https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/ "https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/").

The topics in this section explain how to configure and use Macie to retrieve and reveal
sensitive data samples for findings. You can perform these tasks in all the AWS Regions
where Macie is currently available except the Asia Pacific (Osaka) and
Israel (Tel Aviv) Regions.

###### Topics

- [Configuration options for
  retrieving samples](findings-retrieve-sd-options.md "findings-retrieve-sd-options.md")
- [Configuring Macie to retrieve
  samples](findings-retrieve-sd-configure.md "findings-retrieve-sd-configure.md")
- [Retrieving samples](findings-retrieve-sd-proc.md "findings-retrieve-sd-proc.md")
