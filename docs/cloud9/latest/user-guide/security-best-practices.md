AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Security best practices for AWS Cloud9

The following best practices are general guidelines and don’t represent a complete security
solution. Because these best practices might not be appropriate or sufficient for your
environment, treat them as helpful considerations instead of prescriptions.

###### Some security best practices for AWS Cloud9

- Store your code securely in a version control system, for example, [AWS CodeCommit](../../../codecommit/latest/userguide.md "../../../codecommit/latest/userguide.md").
- For your AWS Cloud9 EC2 development environments, configure and use [Amazon Elastic Block Store](../../../ebs/latest/userguide/what-is-ebs.md "../../../ebs/latest/userguide/what-is-ebs.md") encrypted
  volumes.
- For your EC2 environments, use [tags](tags.md "tags.md") to control access to your AWS Cloud9
  resources.
- For your shared AWS Cloud9 development environments, follow the [best practices](share-environment-best-practices.md "share-environment-best-practices.md") for them.
