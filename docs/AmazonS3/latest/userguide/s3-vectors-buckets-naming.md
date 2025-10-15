# Vector bucket naming rules

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Vector bucket names must follow specific naming conventions to ensure uniqueness
 within an AWS Region. Amazon S3 enforces the following bucket naming requirements, and you
 can't create a vector bucket if these rules aren't followed. Additionally, there are
 best practices that, while not enforced, help prevent conflicts when working with vector
 buckets programmatically or through the console.


## Vector bucket naming requirements


When creating vector buckets, you must follow these requirements:



* Vector bucket names must be unique in the same AWS account for each
 AWS Region.
* Vector bucket names must be between 3 and 63 characters long.
* Vector bucket names can consist only of lowercase letters (a-z), numbers
 (0-9), and hyphens (-).
* Vector bucket names must begin and end with a letter or number.

## Best practices for naming


We recommend following these best practices when naming your vector
 buckets:



* Use descriptive names that reflect the purpose of your vector data (for
 example, product-recommendations, document-embeddings).
* Avoid using sensitive information in bucket names as they may appear in
 logs and URLs.
* Keep names concise but meaningful for easier management and
 identification.

These naming conventions ensure that your vector buckets can be reliably accessed
 through the AWS Management Console, Amazon S3 REST API, the AWS CLI, and AWS
 SDKs.
