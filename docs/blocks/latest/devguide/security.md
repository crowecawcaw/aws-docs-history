

# Security in AWS Blocks
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+  **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](http://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Blocks, see [AWS Services in Scope by Compliance Program](http://aws.amazon.com/compliance/services-in-scope/).
+  **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using AWS Blocks.

## How AWS Blocks manages permissions
<a name="security-permissions"></a>

 AWS Blocks automatically configures IAM permissions for the resources your application uses. When you instantiate a Block, the framework grants your Lambda function the minimum permissions required to interact with that resource.

For example:
+  `KVStore` grants `dynamodb:GetItem`, `dynamodb:PutItem`, `dynamodb:DeleteItem`, and `dynamodb:Query` on the specific table.
+  `FileBucket` grants `s3:GetObject` and `s3:PutObject` on the specific bucket.
+  `Database` grants `rds-data:ExecuteStatement` on the specific Aurora cluster.

You don’t need to write IAM policies manually for Block resources. However, if you add custom CDK resources in the CDK layer, you are responsible for configuring their permissions.

## Authentication
<a name="security-authentication"></a>

 AWS Blocks provides authentication Blocks that handle user identity:

 **AuthBasic**   
Stores user credentials in DynamoDB with bcrypt-hashed passwords. Issues JWT tokens for session management. Suitable for prototypes and internal tools.

 **AuthCognito**   
Integrates with Amazon Cognito for production-grade authentication. Supports social sign-in (Google, Apple, Facebook), SAML, OIDC federation, multi-factor authentication (MFA), and account recovery flows.

 **Best practices:** 
+ Use `AuthCognito` for production applications.
+ Always call `auth.requireAuth(context)` server-side in every API method that accesses user data. Never trust client-side authentication alone.
+ Scope data access by user ID to prevent unauthorized cross-user access.

## Data protection
<a name="security-data-protection"></a>

 AWS Blocks uses the following data protection mechanisms by default:

 **Encryption at rest**   
All data stored by Blocks is encrypted at rest using AWS-managed keys:  
+  `KVStore` and `DistributedTable`: DynamoDB encryption with AWS-owned keys
+  `FileBucket`: S3 server-side encryption (SSE-S3)
+  `Database`: Aurora storage encryption with AWS KMS

 **Encryption in transit**   
All communication between your application and AWS services uses TLS. API Gateway endpoints use HTTPS exclusively.

 **Local development**   
During local development, data is stored unencrypted in the `.bb-data/` directory on your machine. This directory should be added to `.gitignore` (which AWS Blocks does by default) and should not contain production data.

## Network security
<a name="security-network"></a>

By default, AWS Blocks deploys your API behind Amazon API Gateway, which provides:
+ HTTPS-only endpoints (HTTP is not supported)
+ DDoS protection via AWS Shield Standard
+ Request throttling and rate limiting

For additional network isolation, you can configure your Lambda function to run inside a VPC using the CDK layer:

```
// aws-blocks/index.cdk.ts
import * as ec2 from 'aws-cdk-lib/aws-ec2';

const vpc = new ec2.Vpc(stack, 'AppVpc');
stack.handler.connections.allowToAnyIpv4(ec2.Port.tcp(443));
```

## API protection
<a name="security-api-protection"></a>

 **Input validation**   
Always validate inputs in your API methods. AWS Blocks does not perform automatic input validation. Your API methods receive whatever the client sends.  

```
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createItem(title: string) {
    if (!title || title.length > 200) {
      throw new Error('Title must be 1-200 characters');
    }
    // ...
  },
}));
```

 **Rate limiting**   
API Gateway provides default throttling (10,000 requests per second per account per Region). For stricter limits, configure throttling in the CDK layer.

 **CORS**   
 AWS Blocks configures CORS headers automatically for your frontend origin. In production, restrict CORS to your specific domain.

## Managing secrets
<a name="security-secrets"></a>

Don’t hardcode secrets (API keys, database passwords, third-party tokens) in your source code. Use environment variables injected through the CDK layer:

```
// aws-blocks/index.cdk.ts
import * as ssm from 'aws-cdk-lib/aws-ssm';

const apiKey = ssm.StringParameter.valueForStringParameter(stack, '/my-app/api-key');
stack.handler.addEnvironment('EXTERNAL_API_KEY', apiKey);
```

```
// aws-blocks/index.ts - access at runtime
const apiKey = process.env.EXTERNAL_API_KEY;
```

For sensitive secrets, use AWS Secrets Manager instead of SSM Parameter Store.

## Least privilege for deployment
<a name="security-least-privilege"></a>

The IAM user or role that deploys your AWS Blocks application needs permissions to create and manage the underlying resources (Lambda, DynamoDB, API Gateway, CloudFormation, etc.). We recommend:
+ Use a dedicated deployment role with scoped permissions.
+ Don’t deploy with your personal administrator credentials in production.
+ Use CI/CD pipelines with OIDC-based authentication (no long-lived access keys).