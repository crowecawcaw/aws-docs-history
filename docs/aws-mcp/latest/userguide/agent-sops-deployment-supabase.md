# Supabase applications

This SOP deploys applications that use Supabase (such as Lovable.dev and Bolt.new) to AWS. The SOP migrates Supabase Edge Functions to AWS Lambda and [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md"). It stores secrets in [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") and hosts the frontend on [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") and [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md"). After deployment, the SOP provides a shareable URL for your application.

For prerequisites and security information, see [AWS Deployment SOPs](agent-sops-deployment.md "agent-sops-deployment.md").

###### Important

This SOP keeps your database, authentication, and storage in Supabase. You can use an existing project or create a new one. Hosting, Edge Functions, and secrets management migrate to AWS. To fully migrate to AWS, you must manually move your Supabase data.

## Supported application types

- Applications with environment-based Supabase configuration (`supabase/config.toml`):
  - Single-page applications (SPAs): React, Vue, Angular, SvelteKit
  - Static site generators (SSGs): Next.js (static export), Nuxt 2/3, Gatsby, Hugo, Jekyll, Docusaurus, Astro, Eleventy

## Example prompt

To start a deployment, prompt your coding agent: `Deploy my application`.

## Steps your coding agent takes

Your coding agent commits changes after each significant step to a new `deploy-to-aws` branch.

1. Scans the project to detect the framework, build configuration, and Supabase setup
2. Validates prerequisites (AWS credentials, Supabase CLI, package manager, CDK CLI)
3. Creates a new branch (`deploy-to-aws`)
4. Analyzes Supabase Edge Functions, database configuration, and required secrets
5. Configures the Supabase project — uses your existing project or creates a new one under your existing subscription
6. Migrates Supabase Edge Functions (Deno, TypeScript) to AWS Lambda (Node.js, TypeScript)
7. Converts AI or LLM functions to [Amazon Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md"), if detected. This uses `InvokeModel` or `InvokeModelWithResponseStream` as needed
8. Updates all Edge Function references in your application code to use new API endpoints
9. Stores application secrets in AWS Secrets Manager
10. Generates CDK infrastructure code for Lambda, API Gateway, Amazon S3, and Amazon CloudFront
11. Deploys infrastructure through [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
12. Validates each migrated function through the deployed API
13. Provides a URL for your application
14. Records deployment details in your repository

## How it works

Your coding agent analyzes your application to identify Supabase Edge Functions, database configuration, and required secrets. The SOP can create a new Supabase project if needed. The new project is created under your existing subscription, and the SOP pushes database migrations to it.

Each Supabase Edge Function is migrated from Deno/TypeScript to Node.js/TypeScript. The migrated function is deployed as an AWS Lambda function fronted by Amazon API Gateway. The SOP uses [NodejsFunction](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md") with esbuild to bundle each function. If your application uses AI or LLM features, those functions are converted to use Amazon Bedrock. Application secrets, including Supabase credentials, are stored in AWS Secrets Manager. Lambda functions access these secrets at runtime.

For the frontend, the SOP generates the same Amazon S3 and Amazon CloudFront infrastructure as a [frontend deployment](agent-sops-deployment-frontend.md "agent-sops-deployment-frontend.md"). The SOP adds an additional CloudFront behavior that proxies `/api/*` requests to API Gateway. This routing approach avoids cross-origin issues and presents a single domain to your users. All Supabase Edge Function references in your application code are updated to use the new `/api/*` endpoints.

After deployment, the SOP updates Supabase authentication redirect URLs to include the CloudFront domain, so authentication flows work correctly with the new hosting.

The SOP prompts your coding agent to apply security best practices to all generated resources. Always review the generated configuration before deploying to production environments.

For production environments with CI/CD, see [Set up CodePipeline](agent-sops-deployment-pipeline.md "agent-sops-deployment-pipeline.md").

###### Services used

Amazon CloudFront, Amazon S3, AWS Lambda, Amazon API Gateway, AWS Secrets Manager, AWS CloudFormation, AWS IAM, and optionally Amazon Bedrock.

## Troubleshooting

###### Application type not supported

Verify that all prerequisites are met. If your application meets the prerequisites but is reported as unsupported, prompt your coding agent to attempt the deployment. Minor adjustments may be sufficient.

For any other troubleshooting issues, you can contact [AWS Support](https://console.aws.amazon.com/support/home/ "https://console.aws.amazon.com/support/home/") or post your question on [re:Post](https://repost.aws/ "https://repost.aws/") and tag it to the AWS MCP Server to ask the community.
