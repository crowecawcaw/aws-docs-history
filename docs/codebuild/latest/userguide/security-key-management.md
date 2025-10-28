# Key management

You can protect your content from unauthorized use through encryption. Store your
encryption keys in AWS Secrets Manager, and then give the CodeBuild service role associated with the
build project permission to obtain the encryption keys from your Secrets Manager account. For
more information, see [Encrypt build outputs using a customer managed key](setting-up-kms.md "setting-up-kms.md"),
[Create a build project in AWS CodeBuild](create-project.md "create-project.md"), [Run AWS CodeBuild builds manually](run-build.md "run-build.md"), and [Tutorial: Storing and
retrieving a secret](../../../secretsmanager/latest/userguide/tutorials_basic.md "../../../secretsmanager/latest/userguide/tutorials_basic.md").

Use the `CODEBUILD_KMS_KEY_ID` environment variable in a build command to
obtain the AWS KMS key identifier. For more information, see [Environment variables in build
environments](build-env-ref-env-vars.md "build-env-ref-env-vars.md").

You can use Secrets Manager to protect credentials to a private registry that stores a
Docker image used for your runtime environment. For more information, see [Private registry with AWS Secrets Manager sample for CodeBuild](sample-private-registry.md "sample-private-registry.md").
