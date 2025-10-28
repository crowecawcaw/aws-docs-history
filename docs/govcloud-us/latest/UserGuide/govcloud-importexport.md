# AWS Snow Family in AWS GovCloud (US)

AWS Snow Family is a service for customers who want to transport terabytes or petabytes of data to and from AWS, or who want to access the storage and compute power of the AWS Cloud locally and cost effectively in places where connecting to the internet might not be an option.

## How AWS Snow Family differs for AWS GovCloud (US)

- Users can only select AWS GovCloud (US) Regions as the import or export destination Region. The
  AWS GovCloud (US) Region selection is available only when signed in to AWS GovCloud (US).
- AWS Snowball Edge Device Management service is not available.
- AWS Snow Family Large Data Migration Manager is not available.
- Amazon EKS Anywhere on Snow is not available.

## Documentation for AWS Snow Family

[AWS Snow Family documentation](https://aws.amazon.com/documentation/snowball/ "https://aws.amazon.com/documentation/snowball/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Snow Family metadata is not permitted to contain export-controlled data. This
  includes the naming and configuration data that you enter when creating and managing your
  Snow Family import or export job. For example, do not enter export-controlled data into
  user input fields describing your job, such as import job name, Amazon S3 bucket name, or Amazon SNS
  topic name. Snow Family generated metadata will not contain export-controlled data.
