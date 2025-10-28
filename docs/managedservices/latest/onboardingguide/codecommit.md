# Use AMS SSP to provision AWS CodeCommit in your AMS account

###### Note

AWS has closed new customer access to AWS CodeCommit, effective July 25, 2024. AWS CodeCommit existing customers can continue to use the service as normal. AWS continues to invest in
security, availability, and performance improvements for AWS CodeCommit, but we do not plan to introduce new features.

To migrate AWS CodeCommit Git repositories to other Git providers, reach out to your cloud architect (CA) for guidance. For more information on migrating your Git repositories, see
[How to migrate your AWS CodeCommit repository to another Git provider](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/ "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/").

Use AMS Self-Service Provisioning (SSP) mode to access AWS CodeCommit capabilities directly in your AMS managed account. AWS CodeCommit is a fully managed
[source control](https://aws.amazon.com/devops/source-control/ "https://aws.amazon.com/devops/source-control/") service that hosts secure Git-based repositories. It helps teams to
collaborate on code in a secure and highly scalable ecosystem. CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure.
You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools. To learn more, see
[AWS CodeCommit](https://aws.amazon.com/codecommit/ "https://aws.amazon.com/codecommit/").

###### Note

To onboard CodeCommit, CodeBuild, CodeDeploy, and CodePipeline with a single RFC, submit the Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change
type and request the three services: CodeBuild, CodeDeploy and CodePipeline. Then, all three roles, `customer_codebuild_service_role`, `customer_codedeploy_service_role`,
and `aws_code_pipeline_service_role` are provisioned in your account. After provisioning in your account, you must onboard the role in your federation solution.

## CodeCommit in AWS Managed Services FAQ

**Q: How do I request access to CodeCommit in my AMS account?**

AWS CodeCommit console and data access roles can be requested through the
submission of two AWS Service RFCs, console access, and data access:

- Request access to AWS CodeCommit by submitting an RFC with the Management | AWS service |
  Self-provisioned service | Add (ct-1w8z66n899dct) change type. This
  RFC provisions the following IAM role to your account:
  `customer_codecommit_console_role`. After it's
  provisioned in your account, you must onboard the role in your
  federation solution.

Data access (such as Training and Entity Lists) require separate CTs for each data source specifying the S3 data source (mandatory), output bucket
(mandatory) and KMS (optional). There are no limitations to AWS CodeCommit job creation as long as all data sources have been granted access roles. To request
data access, submit an RFC with the Management | Other | Other | Create (ct-1e1xtak34nx76).

**Q: What are the restrictions to using AWS CodeCommit in my AMS account?**

Triggers feature on CodeCommit are disabled given the associated rights to create SNS topics. Directly
authenticating against CodeCommit is restricted, users should authenticate
with Credential Helper. Some KMS commands are also restricted: `kms:Encrypt`,
`kms:Decrypt`, `kms:ReEncrypt`, `kms:GenereteDataKey`,
`kms:GenerateDataKeyWithoutPlaintext`, and `kms:DescribeKey`.

**Q: What are the prerequisites or dependencies to using AWS CodeCommit in my AMS account?**

If S3 buckets are encrypted with KMS keys, S3 and KMS are required to use
AWS CodeCommit.
