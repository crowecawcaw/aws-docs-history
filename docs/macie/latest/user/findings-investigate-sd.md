# Investigating sensitive data with Macie findings

When you run sensitive data discovery jobs or Amazon Macie performs automated sensitive data discovery, Macie captures details about
the location of each occurrence of sensitive data that it finds in Amazon Simple Storage Service (Amazon S3) objects. This
includes sensitive data that Macie detects using [managed
data identifiers](managed-data-identifiers.md "managed-data-identifiers.md"), and data that matches the criteria of [custom data identifiers](custom-data-identifiers.md "custom-data-identifiers.md") that you configure a job or
Macie to use.

With sensitive data findings, you can review these details for as many as 15 occurrences of
sensitive data that Macie finds in individual S3 objects. The details provide insight into the
breadth of the categories and types of sensitive data that specific S3 buckets and objects might
contain. They can help you locate individual occurrences of sensitive data in objects, and
determine whether to perform a deeper investigation of specific buckets and objects.

For additional insight, you can optionally configure and use Macie to retrieve samples of
sensitive data that Macie reports in individual findings. The samples can help you verify the
nature of the sensitive data that Macie found. They can also help you tailor your investigation of
an affected S3 bucket and object. If you choose to retrieve sensitive data samples for a finding,
Macie uses data in the finding to locate 1-10 occurrences of each type of sensitive data reported
by the finding. Macie then extracts those occurrences of sensitive data from the affected object
and displays the data for you to review.

If an S3 object contains many occurrences of sensitive data, a finding can also help you
navigate to the corresponding sensitive data discovery result. Unlike a sensitive data finding, a
sensitive data discovery result provides detailed location data for as many as 1,000 occurrences
of each type of sensitive data that Macie finds in an object. Macie uses the same schema for
location data in sensitive data findings and sensitive data discovery results. To learn more about
sensitive data discovery results, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

The topics in this section explain how to locate and optionally retrieve occurrences of
sensitive data reported by sensitive data findings. They also explain the schema that Macie uses
to report the location of individual occurrences of sensitive data that Macie finds.

###### Topics

- [Locating sensitive data](findings-locate-sd.md "findings-locate-sd.md")
- [Retrieving sensitive data
  samples](findings-retrieve-sd.md "findings-retrieve-sd.md")
- [Schema for sensitive data
  locations](findings-locate-sd-schema.md "findings-locate-sd-schema.md")
