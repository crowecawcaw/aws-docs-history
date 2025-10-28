# Important reference notes for AWS SAM

This section contains important notes and announcements for AWS Serverless Application Model (AWS SAM).

###### Topics

- [Important notes for 2023](#important-notes-2023 "#important-notes-2023")

## Important notes for 2023

### October 2023

#### AWS SAM CLI discontinuing support for Python 3.7

_Published on 2023-10-20_

Python 3.7 received end-of-life status in June of 2023. The AWS SAM CLI will
discontinue support for Python 3.7 on October 24, 2023. For more information, see the
[announcement](https://github.com/aws/aws-sam-cli/issues/5889 "https://github.com/aws/aws-sam-cli/issues/5889") at the
_aws-sam-cli GitHub repository_.

This change impacts the following users:

- If you use Python 3.7 and install the AWS SAM CLI through
  `pip`.
- If you use the `aws-sam-cli` as a library and build your application with
  Python 3.7.

If you install and manage the AWS SAM CLI through another method, you are not affected.

For impacted users, we recommend that you upgrade your development environment to
Python 3.8 or newer.

This change does not affect support for the Python 3.7 AWS Lambda runtime environment. For
more information, see [Runtime deprecation policy](../../../lambda/latest/dg/lambda-runtimes.md#runtime-support-policy "../../../lambda/latest/dg/lambda-runtimes.md#runtime-support-policy")
in the _AWS Lambda Developer Guide_.
