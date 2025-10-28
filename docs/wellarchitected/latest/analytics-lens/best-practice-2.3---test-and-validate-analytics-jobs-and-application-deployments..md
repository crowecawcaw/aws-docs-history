# Best practice 2.3 – Test and validate analytics jobs and application deployments

Before making changes in production environments, use
standard and repeatable automated tests to validate
performance and accuracy of results.

## Suggestion 2.3.1 – Establish separate staging environments to test changes before going live

Use separate environments, such as development, test, and
production, to allow feature development to be introduced
without disrupting production systems. Test changes for
accuracy and performance before changes are deployed into
the production environment.

## Suggestion 2.3.2 – Automate the deployment and testing when infrastructure and

applications changes are introduced

The deployment of data pipelines and data infrastructure changes should be an automated process. When code is checked into version control, a CI/CD process should run tests and apply the changes to the staging environment, and once tested and confirmed correct, it should be deployed to the production environment.

You can use the AWS CodePipeline service to define a CI/CD process.

For more details refer to the following information:

- AWS Perspective Guidance:
  [Deploy
  an AWS Glue job with an AWS CodePipeline CI/CD
  pipeline](../../../prescriptive-guidance/latest/patterns/deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline.md "../../../prescriptive-guidance/latest/patterns/deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline.md")
- AWS DevOps Blog:
  [How
  to unit test and deploy AWS Glue jobs using AWS CodePipeline](https://aws.amazon.com/blogs/devops/how-to-unit-test-and-deploy-aws-glue-jobs-using-aws-codepipeline/ "https://aws.amazon.com/blogs/devops/how-to-unit-test-and-deploy-aws-glue-jobs-using-aws-codepipeline/")
- AWS DevOps Blog: [10 ways to build applications faster with Amazon CodeWhisperer](https://aws.amazon.com/blogs/devops/10-ways-to-build-applications-faster-with-amazon-codewhisperer/ "https://aws.amazon.com/blogs/devops/10-ways-to-build-applications-faster-with-amazon-codewhisperer/")
