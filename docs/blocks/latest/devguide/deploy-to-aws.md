

# Deploy your application to AWS
<a name="deploy-to-aws"></a>

After developing and testing your application locally, you can deploy it to AWS. This page covers the one-time AWS account setup and the deployment commands.

## Setting up AWS credentials
<a name="deploy-aws-account"></a>

If you already have AWS credentials configured, skip to [Bootstrap the AWS CDK](#deploy-aws-cdk-bootstrap).

### Sign up for an AWS account
<a name="deploy-aws-sign-up"></a>

If you don’t already have an AWS account, complete the following steps to create one.

1. Open https://portal.aws.amazon.com/billing/signup.

1. Follow the online instructions.

   Part of the sign-up procedure involves receiving a phone call and entering a verification code on the phone keypad.

   When you sign up for an AWS account, an * AWS account root user* is created. The root user has access to all AWS services and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html).

### Create a user with administrative access
<a name="deploy-aws-iam"></a>

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/) as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

1. Enable IAM Identity Center.

   For more information about enabling IAM Identity Center, see [Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) in the * AWS IAM Identity Center User Guide*.

1. In IAM Identity Center, grant administrative access to a user.

   For more information about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html) in the * AWS IAM Identity Center User Guide*.
**Note**  
Administrative access is recommended for getting started and local development. For production environments, use a least-privilege IAM policy scoped to only the resources that AWS Blocks creates.

### Install and configure the AWS CLI
<a name="deploy-aws-cli"></a>

1. Install the AWS CLI version 2. For more information about installing the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Configure the AWS CLI with your credentials. For more information about configuring the AWS CLI, see [Configuring the AWS CLI to use IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

1. Verify your configuration by running the following command:

   ```
   aws sts get-caller-identity
   ```

   This command should return your account ID, user ID, and ARN.

### Bootstrap the AWS CDK
<a name="deploy-aws-cdk-bootstrap"></a>

 AWS Blocks uses the AWS CDK to deploy infrastructure. You must bootstrap your AWS account before your first deployment.

Run the following command, replacing `ACCOUNT_ID` and `REGION` with your values:

```
npx cdk bootstrap aws://ACCOUNT_ID/REGION
```

For example:

```
npx cdk bootstrap aws://123456789012/us-east-1
```

You need to bootstrap only one time per account and Region combination.

## Deploy to a sandbox
<a name="deploy-sandbox"></a>

A sandbox is a fast, ephemeral deployment for testing against real AWS services. To deploy your application to a sandbox, run the following command:

```
npm run sandbox
```

The sandbox:
+ Deploys in seconds using Lambda hot-swapping
+ Uses real AWS services (DynamoDB, API Gateway, Lambda)
+ Supports rapid iteration without full CloudFormation deployments
+ Gives each developer an isolated environment

The same code that ran locally now runs on AWS. Blocks automatically resolve to their AWS implementations. `KVStore` becomes a DynamoDB table, `AuthBasic` provisions user storage, and `ApiNamespace` creates an API Gateway endpoint backed by a Lambda function.

To remove sandbox resources, run the following command:

```
npm run sandbox:destroy
```

## Full deployment
<a name="deploy-production"></a>

For a complete deployment including hosting, run the following command:

```
npm run deploy
```

This runs a full CDK deployment, creating a CloudFormation stack with all your resources. Use this for staging, production, or branch deployments.

To remove all deployed resources, run the following command:

```
npm run destroy
```

## Next steps
<a name="deploy-next-steps"></a>
+ To configure custom domains, VPC settings, or other environment-specific infrastructure, see [The CDK layer](concepts.md#concepts-cdk-layer) in the Concepts topic.
+ To integrate AWS Blocks into an existing CDK application, see [Integrating with existing infrastructure](existing-infrastructure.md).