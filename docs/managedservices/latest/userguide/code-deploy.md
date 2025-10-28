# Use AMS SSP to provision AWS CodeDeploy in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS CodeDeploy capabilities directly in your AMS managed account. AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute
services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers.
AWS CodeDeploy helps you to rapidly release new features, helps you avoid downtime during application deployment,
and handles the complexity of updating your applications.
You can use AWS CodeDeploy to automate software deployments, eliminating the need for error-prone manual operations.
The service scales to match your deployment needs.
To learn more, see [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/").

###### Note

To onboard CodeCommit, CodeBuild, CodeDeploy, and CodePipeline with a single RFC, submit the
Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change
type and request the three services: CodeBuild, CodeDeploy and CodePipeline. Then, all three roles,
`customer_codebuild_service_role`, `customer_codedeploy_service_role`,
and `aws_code_pipeline_service_role` are provisioned in your account. After provisioning in your
account, you must onboard the role in your federation solution.

## CodeDeploy in AWS Managed Services FAQ

**Q: How do I request access to CodeDeploy in my AMS account?**

Request access to CodeDeploy by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles to your account:
`customer_codedeploy_console_role` and `customer_codedeploy_service_role`. After it's provisioned in
your account, you must onboard the `customer_codedeploy_console_role` role in your federation solution.

**Q: What are the restrictions to using CodeDeploy in my AMS account?**

Currently we are only supporting Compute Platform as — Amazon EC2/On-premises. Blue/Green Deployments are not supported.

**Q: What are the prerequisites or dependencies to using CodeDeploy in my AMS account?**

There are no prerequisites or dependencies to use CodeDeploy in your AMS account.
