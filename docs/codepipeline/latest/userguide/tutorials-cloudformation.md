# Tutorial: Create a pipeline with AWS CloudFormation

The examples provide sample templates that allow you to use AWS CloudFormation to create a pipeline
that deploys your application to your instances each time the source code changes. The sample
template creates a pipeline that you can view in AWS CodePipeline. The pipeline detects the arrival of
a saved change through Amazon CloudWatch Events.

###### Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be
used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source action.)
If the S3 artifact bucket is in a different account from the account for your pipeline, make
sure that the S3 artifact bucket is owned by AWS accounts that are safe and will be
dependable.

###### Topics

- [Example 1: Create an AWS CodeCommit pipeline
  with AWS CloudFormation](tutorials-cloudformation-codecommit.md "tutorials-cloudformation-codecommit.md")
- [Example 2: Create an Amazon S3 pipeline with
  AWS CloudFormation](tutorials-cloudformation-s3.md "tutorials-cloudformation-s3.md")
