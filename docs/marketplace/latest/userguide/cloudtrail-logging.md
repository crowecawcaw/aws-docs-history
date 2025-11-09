# Logging AWS Marketplace API calls with

AWS CloudTrail

AWS Marketplace is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in AWS Marketplace. CloudTrail captures API calls for AWS Marketplace as
events. The calls captured include calls from the AWS Marketplace console and code calls to the
AWS Marketplace API operations.

CloudTrail is enabled on your AWS account when you create the account. When supported event
activity occurs in AWS Marketplace, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and
download recent events in your account.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management user credentials.
- Whether the request was made with temporary security credentials for a role or a
  federated user.
- Whether the request was made by another AWS service.
  For more information on the different CloudTrail log entries and to see examples, see [Logging for the AWS Marketplace API](../APIReference/logging.md "../APIReference/logging.md")
  in the _AWS Marketplace API Reference_.
