# Use AMS SSP to provision AWS CodeBuild in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS CodeBuild capabilities directly in your AMS managed account. AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.
With CodeBuild, you don’t need to provision, manage, and scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently,
so your builds are not left waiting in a queue. You can get started quickly by using prepackaged build environments, or you can create custom build environments
that use your own build tools. With CodeBuild, you are charged by the minute for the compute resources you use.
To learn more, see [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/").

###### Note

To onboard CodeCommit, CodeBuild, CodeDeploy, and CodePipeline with a single RFC, submit the
Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change
type and request the three services: CodeBuild, CodeDeploy and CodePipeline. Then, all three roles,
`customer_codebuild_service_role`, `customer_codedeploy_service_role`,
and `aws_code_pipeline_service_role` are provisioned in your account. After provisioning in your
account, you must onboard the role in your federation solution.

## CodeBuild in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS CodeBuild in my AMS account?**

Utilization of AWS CodeBuild in your AMS account is a two-step
process:

1. Provision the `CodeBuild Service Role` for build process to coordinate with AWS
   S3 buckets, Amazon CloudWatch and Log groups
2. Request access to the CodeBuild console

You can request that both be set up in your AMS account by submitting an
RFC with the Management | AWS service | Self-provisioned service | Add
change type (ct-1w8z66n899dct). After it's provisioned in your account, you
must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS CodeBuild in my AMS account?**

For AWS CodeBuild console administrator access, permissions are limited at
resource level; for example, CloudWatch actions are limited on specific
resources and the `iam:PassRole` permission is controlled.

**Q: What are the prerequisites or dependencies to using CodeBuild in my AMS account?**

If additional IAM permissions are required for the defined AWS CodeBuild service role, request them through
an AMS service request.
