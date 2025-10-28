# Use AMS SSP to provision AMS Code services in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AMS Code services capabilities directly in your AMS managed account. AMS Code services is a proprietary bundling of AWS code management services as detailed next. You can choose to deploy all of the services in
AMS with AMS Code services, or you can deploy them in AMS individually.

AMS Code services includes the following services:

- AWS CodeCommit: A fully managed [source control](https://aws.amazon.com/devops/source-control "https://aws.amazon.com/devops/source-control") service that hosts secure
  Git-based repositories. It makes it so teams can collaborate on code in a secure
  and highly scalable ecosystem. CodeCommit eliminates the need to operate your own
  source control system or worry about scaling its infrastructure. You can use
  CodeCommit to securely store anything from source code to binaries, and it works
  seamlessly with your existing Git tools. To learn more, see
  [AWS CodeCommit](https://aws.amazon.com/codecommit/ "https://aws.amazon.com/codecommit/")

To deploy this in your AMS account independently of AMS Code services, see
[Use AMS SSP to provision AWS CodeCommit in your AMS account](codecommit.md "codecommit.md").

- AWS CodeBuild: A fully managed continuous integration service that
  compiles source code, runs tests, and produces software packages that are
  ready to deploy. With CodeBuild, you don’t need to provision, manage, and scale
  your own build servers. CodeBuild scales continuously and processes multiple builds
  concurrently, so your builds are not left waiting in a queue. You can get started
  quickly by using prepackaged build environments, or you can create custom build
  environments that use your own build tools. With CodeBuild, you are charged by the
  minute for the compute resources you use. To learn more, see
  [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/")

To deploy this in your AMS account independently of AMS Code services, see
[Use AMS SSP to provision AWS CodeBuild in your AMS account](code-build.md "code-build.md").

- AWS CodeDeploy: A fully managed deployment service that automates
  software deployments to a variety of compute services such as Amazon EC2 and your
  on-premises servers. AWS CodeDeploy helps you to rapidly release new features, helps
  you avoid downtime during application deployment, and handles the complexity of
  updating your applications. You can use AWS CodeDeploy to automate software
  deployments, eliminating the need for error-prone manual operations. The service
  scales to match your deployment needs. To learn more, see
  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/")

To deploy this in your AMS account independently of AMS Code services, see
[Use AMS SSP to provision AWS CodeDeploy in your AMS account](code-deploy.md "code-deploy.md").

- AWS CodePipeline: A fully managed
  [continuous delivery](https://aws.amazon.com/devops/continuous-delivery/ "https://aws.amazon.com/devops/continuous-delivery/")
  service that helps you automate your release pipelines for fast and reliable application
  and infrastructure updates. CodePipeline automates the build, test, and deploy phases of
  your release process every time there is a code change, based on the release model
  you define. This enables you to rapidly and reliably deliver features and updates. You
  can easily integrate AWS CodePipeline with third-party services such as GitHub or with your
  own custom plugin. With AWS CodePipeline, you only pay for what you use. There are no
  upfront fees or long-term commitments. To learn more, see
  [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")

To deploy this in your AMS account independently of AMS Code services, see
[Use AMS SSP to provision AWS CodePipeline in your AMS account](code-pipeline.md "code-pipeline.md").

## AMS Code services in AWS Managed Services FAQ

**Q: How do I request access to AMS Code services in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_code_suite_console_role`. After provisioned in your account,
you must onboard the role in your federation solution. At this time AMS Operations will also deploy the `customer_codebuild_service_role`,
`customer_codedeploy_service_role`, `aws_code_pipeline_service_role` service roles in your account for CodeBuild, CodeDeploy and CodePipeline
services. If additional IAM permissions for the are required for the `customer_codebuild_service_role` are needed, submit an AMS service request.

###### Note

You can also add these services separately; for information, see
[Use AMS SSP to provision AWS CodeBuild in your AMS account](code-build.md "code-build.md"),
[Use AMS SSP to provision AWS CodeDeploy in your AMS account](code-deploy.md "code-deploy.md"), and
[Use AMS SSP to provision AWS CodePipeline in your AMS account](code-pipeline.md "code-pipeline.md"), respectively.

**Q: What are the restrictions to using AMS Code services in my AMS account?**

- AWS CodeCommit: The triggers feature on CodeCommit is disabled given the associated rights to create SNS topics. Directly authenticating against
  CodeCommit is restricted; users should authenticate with Credential Helper. Some KMS commands are also restricted: kms:Encrypt, kms:Decrypt,
  kms:ReEncrypt, kms:GenereteDataKey, kms:GenerateDataKeyWithoutPlaintext, and kms:DescribeKey.
- CodeBuild: For AWS CodeBuild console admin access, permissions are limited at the resource level; for example, CloudWatch actions are limited on
  specific resources and the `iam:PassRole` permission is controlled.
- CodeDeploy: Currently CodeDeploy supports deployments on Amazon EC2/On-premises only. Deployments on ECS and Lambda through CodeDeploy is not supported.
- CodePipeline: CodePipeline features, stages, and providers are limited to the following:
  - Deploy Stage: Amazon S3 and AWS CodeDeploy
  - Source Stage: Amazon S3, AWS CodeCommit, Bit Bucket, and GitHub
  - Build Stage: AWS CodeBuild and Jenkins
  - Approval Stage: Amazon SNS
  - Test Stage: AWS CodeBuild, Jenkins, BlazeMeter, Ghost Inspector UI Testing, Micro Focus StormRunner Load, Runscope API Monitoring
  - Invoke Stage: Step Functions and Lambda

###### Note

AMS Operations deploys the `customer_code_pipeline_lambda_policy` in your account; it must be attached with
the Lambda execution role for Lambda invoke stage. Provide the Lambda service/execution role name that you want this policy added
with. If there is no custom Lambda service/execution role, then AMS creates a new role named `customer_code_pipeline_lambda_execution_role`,
that is a copy of `customer_lambda_basic_execution_role` along with `customer_code_pipeline_lambda_policy`.

**Q: What are the prerequisites or dependencies to using AMS Code services in my AMS
account?**

- CodeCommit: If S3 buckets are encrypted with AWS KMS keys, S3
  and AWS KMS are required to use AWS CodeCommit.
- CodeBuild: If additional IAM permissions are required for the
  defined AWS CodeBuild service role, request them through an AMS service request.
- CodeDeploy: None.
- CodePipeline: None. AWS supported services—AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy—must be
  launched prior to, or along with, the launch of CodePipeline. However this is done by an AMS engineer.
