# Use AMS SSP to provision AWS CodePipeline in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS CodePipeline capabilities directly in your AMS managed account. AWS CodePipeline is a fully managed
[continuous delivery](https://aws.amazon.com/devops/continuous-delivery/ "https://aws.amazon.com/devops/continuous-delivery/") service that helps you
automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test,
and deploy phases of your release process every time there is a code change, based on the release model you define.
This enables you to rapidly and reliably deliver features and updates. You can easily integrate AWS CodePipeline with third-party services such as
GitHub or with your own custom plugin.
With AWS CodePipeline, you only pay for what you use. There are no upfront fees or long-term commitments.
To learn more, see [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/").

###### Note

To onboard CodeCommit, CodeBuild, CodeDeploy, and CodePipeline with a single RFC, submit the
Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change
type and request the three services: CodeBuild, CodeDeploy and CodePipeline. Then, all three roles,
`customer_codebuild_service_role`, `customer_codedeploy_service_role`,
and `aws_code_pipeline_service_role` are provisioned in your account. After provisioning in your
account, you must onboard the role in your federation solution.

CodePipeline in AMS does not support "Amazon CloudWatch Events" for Source Stage because
it needs elevated permissions
to create the service role and policy, which bypasses the least-privileges model and AMS
change management process.

## CodePipeline in AWS Managed Services FAQ

**Q: How do I request access to CodePipeline in my AMS account?**

Request access to CodePipeline by submitting a service request for the `customer_code_pipeline_console_role` in the relevant account.
After it's provisioned
in your account, you must onboard the role in your federation solution.

At this time, AMS Operations will also deploy this service role in your account:
`aws_code_pipeline_service_role_policy`.

**Q: What are the restrictions to using CodePipeline in my AMS account?**

Yes. CodePipeline features, stages, and providers are limited to the following:

1. Deploy Stage: Limited to Amazon S3, and AWS CodeDeploy
2. Source Stage: Limited to Amazon S3, AWS CodeCommit, BitBucket, and GitHub
3. Build Stage: Limited to AWS CodeBuild, and Jenkins
4. Approval Stage: Limited to Amazon SNS
5. Test Stage: Limited to AWS CodeBuild, Jenkins, BlazeMeter, Ghost Inspector UI Testing,
   Micro Focus StormRunner Load, and Runscope API Monitoring
6. Invoke Stage: Limited to Step Functions, and Lambda

###### Note

AMS Operations will deploy `customer_code_pipeline_lambda_policy` in your
account; it must be attached with the Lambda execution role for Lambda invoke stage. Please provide
the Lambda service/execution role name that you want this policy added with. If there is no custom
Lambda service/execution role, AMS will create a new role named
`customer_code_pipeline_lambda_execution_role`, which will be a copy of
`customer_lambda_basic_execution_role` along with
`customer_code_pipeline_lambda_policy`.

**Q: What are the prerequisites or dependencies to using CodePipeline in my AMS account?**

AWS supported services AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy must
be launched prior to, or along with, the launch of CodePipeline.
