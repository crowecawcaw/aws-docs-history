# Create AWS Secrets Manager secrets in AWS Cloud Development Kit (AWS CDK)

To create, manage, and retrieve secrets in a CDK app, you can use the [AWS Secrets Manager Construct Library](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md"), which contains [`ResourcePolicy`](../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md"), [`RotationSchedule`](../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md"), [`Secret`](../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md"), [`SecretRotation`](../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md"), and [`SecretTargetAttachment`](../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_secretsmanager.md") constructs.

A good practice for using secrets in CDK applications is to first [create the secret by using console or the CLI](create_secret.md "create_secret.md"), and then
import the secret into your CDK application.

For examples, see:

- [Create a secret](../../../cdk/api/v2/docs/aws-cdk-lib.md#creating-json-secrets "../../../cdk/api/v2/docs/aws-cdk-lib.md#creating-json-secrets")
- [Import a secret](../../../cdk/api/v2/docs/aws-cdk-lib.md#importing-secrets "../../../cdk/api/v2/docs/aws-cdk-lib.md#importing-secrets")
- [Retrieve a secret](../../../cdk/v2/guide/get-secrets-manager-value.md "../../../cdk/v2/guide/get-secrets-manager-value.md")
- [Grant permission to use the secret](../../../cdk/api/v2/docs/aws-cdk-lib.md#grant-permission-to-use-the-secret-to-a-role "../../../cdk/api/v2/docs/aws-cdk-lib.md#grant-permission-to-use-the-secret-to-a-role")
- [Rotate a secret](../../../cdk/api/v2/docs/aws-cdk-lib.md#rotating-a-secret "../../../cdk/api/v2/docs/aws-cdk-lib.md#rotating-a-secret")
- [Rotate a database secret](../../../cdk/api/v2/docs/aws-cdk-lib.md#rotating-database-credentials "../../../cdk/api/v2/docs/aws-cdk-lib.md#rotating-database-credentials")
- [Replicate a secret to other Regions](../../../cdk/api/v2/docs/aws-cdk-lib.md#replicating-secrets "../../../cdk/api/v2/docs/aws-cdk-lib.md#replicating-secrets")
  For more information about the CDK, see the [AWS Cloud Development Kit (AWS CDK) v2 Developer Guide](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md").
