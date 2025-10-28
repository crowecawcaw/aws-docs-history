# Release: Elastic Beanstalk supports retrieving secrets and configuration from AWS Secrets Manager and AWS Systems Manager on March 31, 2025

AWS Elastic Beanstalk adds support for accessing secrets and configuration from AWS Secrets Manager and AWS Systems Manager with environment variables.

**Release date:** March 31, 2025

## Changes

Elastic Beanstalk now offers the ability to reference AWS Systems Manager Parameter Store or AWS Secrets Manager secrets in environment variables.

This new integration eliminates the need for your application to make Systems Manager or Secrets Manager API calls to retrieve sensitive data, since it can access the
data natively with environment variables.

This feature is available in all commercial AWS Regions where Elastic Beanstalk is available, including AWS GovCloud (US) Regions.

For more information, see [Using Elastic Beanstalk with Secrets Manager and Systems Manager
Parameter Store](../dg/AWSHowTo.md "../dg/AWSHowTo.md") in the _AWS Elastic Beanstalk Developer Guide_.
