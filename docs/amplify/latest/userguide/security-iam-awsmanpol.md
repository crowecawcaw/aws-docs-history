

# AWS managed policies for AWS Amplify
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AdministratorAccess-Amplify
<a name="security-iam-awsmanpol-AdministratorAccess-Amplify"></a>

You can attach the `AdministratorAccess-Amplify` policy to your IAM identities. Amplify also attaches this policy to a service role that allows Amplify to perform actions on your behalf.

When you deploy a backend in the Amplify console, you must create an `Amplify-Backend Deployment` service role that Amplify uses to create and manage AWS resources. IAM attaches the `AdministratorAccess-Amplify` managed policy to the `Amplify-Backend Deployment` service role.

This policy grants account administrative permissions while explicitly allowing direct access to resources that Amplify applications require to create and manage backends.

**Permissions details**

This policy provides access to multiple AWS services, including IAM actions. These actions allow identities with this policy to use AWS Identity and Access Management to create other identities with any permissions. This allows permissions escalation and this policy should be considered as powerful as the `AdministratorAccess` policy.

This policy grants the `iam:PassRole` action permission for all resources. This is required to support Amazon Cognito user pools configuration.

To view the permissions for this policy, see [AdministratorAccess-Amplify](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess-Amplify.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmplifyBackendDeployFullAccess
<a name="security-iam-awsmanpol-AmplifyBackendDeployFullAccess"></a>

You can attach the `AmplifyBackendDeployFullAccess` policy to your IAM identities.

This policy grants Amplify full access permissions to deploy Amplify backend resources using the AWS Cloud Development Kit (AWS CDK). Permissions are deferred to the AWS CDK roles that have the necessary `AdministratorAccess` policy permissions.

**Permissions details**

This policy includes permissions to do the following .
+ `Amplify`– Retrieve metadata about deployed applications.
+ `CloudFormation`– Create, update, and delete Amplify managed stacks.
+ `SSM`– Create, update, and delete Amplify managed SSM Parameter Store `String` and `SecureString` parameters.
+ `AWS AppSync`– Update and retrieve AWS AppSync schema, resolver and function resources. The purpose is to support the Gen 2 sandbox hotswapping functionality.
+ `Lambda`– Update and retrieve the configuration for Amplify managed functions. The purpose is to support the Gen 2 sandbox hotswapping functionality.

  Retrieve a Lambda function's tags. The purpose is to support Lambda functions defined by customers.
+ `Amazon S3`– Retrieve Amplify deployment assets.
+ `AWS Security Token Service`– Enables the AWS Cloud Development Kit (AWS CDK) CLI to assume the deployment role.
+ `Amazon RDS`– Read metadata of DB instances, clusters, and proxies.
+ `Amazon EC2`– Read the availability zone information for a subnet.
+ `CloudWatch Logs`– Retrieve the logs for a customer's Lambda function. The purpose is to allow an Amplify cloud development sandbox environment to stream a Lambda function's logs to a customer's terminal.

To view the permissions for this policy, see [AmplifyBackendDeployFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmplifyBackendDeployFullAccess.html) in the *AWS Managed Policy Reference*.

## Amplify updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Amplify since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history for AWS Amplify](document-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add read access to the `logs:FilterLogEvents` resource to allow Amplify to stream logs from functions where a custom log group was created. This is an extension of the existing ability to stream a Lambda function's logs. | November 14, 2024 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add read access to the `lambda:ListTags` and `logs:FilterLogEvents` resources to support Lambda functions defined by customers. These permissions allow an Amplify cloud development sandbox environment to stream a Lambda function's logs to a customer's terminal.  | July 18, 2024 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add read access to the `arn:aws:ssm:*:*:parameter/cdk-bootstrap/*` resource to allow Amplify to detect the CDK bootstrap version in a customer's account. | May 31, 2024 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add a new `AmplifyDiscoverRDSVpcConfig` policy statement with Amazon RDS and Amazon EC2 read-only permissions scoped by both resource and account conditions. These permissions support the Amplify Gen 2 `npx amplify generate schema-from-database` command that allows customers to generate Typescript data schema from an existing SQL database.<br />Add the `rds:DescribeDBProxies`, `rds:DescribeDBInstances`, `rds:DescribeDBClusters`, `rds:DescribeDBSubnetGroups`, and `ec2:DescribeSubnets` permissions. The `npx amplify generate schema-from-database` command requires these permissions to check whether a specified DB host is hosted in Amazon RDS and auto-generate the Amazon VPC configuration required to provision the other resources required to set up an AWS AppSync API backed by a SQL database. | April 17, 2024 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add the `cloudformation:DeleteStack` policy action to support stack deletion when the `DeleteBranch` API is called.<br />Add the `lambda:GetFunction` policy action to support hotswapping functions.<br />Add the `lambda:UpdateFunctionConfiguration` policy action to support updates to the Lambda function. | April 5, 2024 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add the `cloudformation:TagResource` and `cloudformation:UnTagResource` permissions to support calls to CloudFormation APIs. | April 4, 2024 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add the `lambda:InvokeFunction` policy action to support AWS Cloud Development Kit (AWS CDK) hotswapping. The AWS CDK makes direct calls to a Lambda function to perform Amazon S3 asset hotswapping.<br />Add the `lambda:UpdateFunctionCode` policy action to support hotswapping functions. | January 02, 2024 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add policy actions to support the `UpdateApiKey` operation. This is required to enable a successful app deployment after exiting and restarting the sandbox without deleting resources. | November 17, 2023 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – Update to an existing policy | Add the `amplify:GetBackendEnvironment` permission to support Amplify app deployment. | November 6, 2023 | 
| [AmplifyBackendDeployFullAccess](#security-iam-awsmanpol-AmplifyBackendDeployFullAccess) – New policy | Amplify added a new policy with the minimum permissions required to deploy Amplify backend resources. | October 8, 2023 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add the ecr:DescribeRepositories permission that is required by the Amplify Command Line Interface (CLI). | June 1, 2023 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add a policy action to support removing tags from an AWS AppSync resource.<br />Add a policy action to support the Amazon Polly resource.<br />Add a policy action to support updating the OpenSearch domain configuration.<br />Add a policy action to support removing tags from an AWS Identity and Access Management role.<br />Add a policy action to support removing tags from an Amazon DynamoDB resource.<br />Add the `cloudfront:GetCloudFrontOriginAccessIdentity` and `cloudfront:GetCloudFrontOriginAccessIdentityConfig` permissions to the `CLISDKCalls` statement block to support the Amplify publish and hosting workflows.<br />Add the `s3:PutBucketPublicAccessBlock` permission to the `CLIManageviaCFNPolicy` statement block to allow the AWS CLI to support the Amazon S3 security best practice of enabling the Amazon S3 Block Public Access feature on internal buckets.<br />Add the `cloudformation:DescribeStacks` permission to the `CLISDKCalls` statement block to support retrieving customers’ CloudFormation stacks on retries in the Amplify backend processor to avoid duplicating executions if a stack is updating.<br />Add the `cloudformation:ListStacks` permission to the `CLICloudformationPolicy` statement block. This permission is required to fully support the CloudFormation DescribeStacks action. | February 24, 2023 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add policy actions to allow the Amplify server-side rendering feature to push application metrics to CloudWatch in a customer's AWS account. | August 30, 2022 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add policy actions to block public access to the Amplify deployment Amazon S3 bucket. | April 27, 2022 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add an action to allow customers to delete their server-side rendered (SSR) apps. This also allows the corresponding CloudFront distribution to be deleted successfully.<br />Add an action to allow customers to specify a different Lambda function to handle events from an existing event source using the Amplify CLI. With these changes, AWS Lambda will be able to perform the [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateEventSourceMapping.html) action. | April 17, 2022 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add a policy action to enable Amplify UI Builder actions on all resources. | December 2, 2021 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add policy actions to support the Amazon Cognito authentication feature that uses social identity providers.<br />Add a policy action to support Lambda layers.<br />Add a policy action to support the Amplify Storage category. | November 8, 2021 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Add Amazon Lex actions to support the Amplify Interactions category.<br />Add Amazon Rekognition actions to support the Amplify Predictions category.<br />Add an Amazon Cognito action to support MFA configuration on Amazon Cognito user pools.<br />Add CloudFormation actions to support CloudFormation StackSets.<br />Add Amazon Location Service actions to support the Amplify Geo category.<br />Add a Lambda action to support Lambda layers in Amplify.<br />Add CloudWatch Logs actions to support CloudWatch Events.<br />Add Amazon S3 actions to support the Amplify Storage category.<br />Add policy actions to support server-side rendered (SSR) apps. | September 27, 2021 | 
| [AdministratorAccess-Amplify](#security-iam-awsmanpol-AdministratorAccess-Amplify) – Update to an existing policy | Consolidate all Amplify actions into a single `amplify:*` action.<br />Add an Amazon S3 action to support encrypting customer Amazon S3 buckets.<br />Add IAM permission boundary actions to support Amplify apps that have permission boundaries enabled.<br />Add Amazon SNS actions to support viewing origination phone numbers, and viewing, creating, verifying, and deleting destination phone numbers.<br />Amplify Studio: Add Amazon Cognito, AWS Lambda, IAM, and CloudFormation policy actions to enable managing backends in the Amplify console and Amplify Studio.<br />Add an AWS Systems Manager (SSM) policy statement to manage Amplify environment secrets.<br />Add an CloudFormation `ListResources` action to support Lambda layers for Amplify apps. | July 28, 2021 | 
| Amplify started tracking changes | Amplify started tracking changes for its AWS managed policies. | July 28, 2021 | 