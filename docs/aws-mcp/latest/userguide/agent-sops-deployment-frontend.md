# Frontend applications

This SOP analyzes your frontend application and generates AWS CDK infrastructure code. The SOP then deploys the infrastructure to AWS. After deployment, the SOP provides a shareable URL for your website.

For prerequisites and security information, see [AWS Deployment SOPs](agent-sops-deployment.md "agent-sops-deployment.md").

## Supported application types

- Single-page applications (SPAs): React, Vue, Angular, SvelteKit
- Static site generators (SSGs): Next.js (static export), Nuxt 2/3, Gatsby, Hugo, Jekyll, Docusaurus, Astro, Eleventy
- Static websites

###### Note

Applications that require server-side rendering (SSR) are not supported by this SOP. If your application uses SSR, consider deploying with [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md"), [Amazon ECS](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md"), or [AWS App Runner](../../../apprunner/latest/dg/what-is-apprunner.md "../../../apprunner/latest/dg/what-is-apprunner.md").

## Example prompt

To start a deployment, prompt your coding agent: `Deploy my application`.

## Steps your coding agent takes

Your coding agent commits changes after each significant step to a new `deploy-to-aws` branch.

1. Scans the project to detect the framework, build configuration, and output directory
2. Validates prerequisites (AWS credentials, package manager, CDK CLI)
3. Creates a new branch (`deploy-to-aws`)
4. Generates CDK infrastructure code for Amazon S3 and Amazon CloudFront
5. Builds your application and deploys infrastructure through [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
6. Validates the deployment and provides a URL for your application
7. Records deployment details, and follow-up instructions, in your repository in `AGENTS.md` and `DEPLOYMENT.md`

## How it works

Your coding agent analyzes your application to determine the framework, build output directory, and routing strategy. Based on this analysis, the agent generates CDK infrastructure code using the [CloudFrontToS3](../../../solutions/latest/constructs/aws_cloudfront_s3.md "../../../solutions/latest/constructs/aws_cloudfront_s3.md") AWS Solutions Construct.

The generated infrastructure creates an Amazon S3 bucket to store your compiled application. It also creates an Amazon CloudFront distribution to serve the application globally. CloudFront is configured with Origin Access Control (OAC) so that Amazon S3 is accessed only through the AWS internal network, keeping the bucket private.

Your coding agent determines the correct CloudFront routing configuration based on your framework:

- Single-page applications use CloudFront error responses to redirect navigation requests to `index.html`
- Static site generators use CloudFront Functions to rewrite URLs. Depending on your framework's trailing slash configuration, requests are rewritten to either `/path/index.html` or `/path.html`

A personal preview stack is provisioned using CloudFormation with the naming pattern `{AppName}Frontend-preview-{username}`. Preview environments use non-production defaults. These defaults include `DESTROY` removal policies and short log retention. Production environments use `RETAIN` removal policies and longer retention periods.

The SOP prompts your coding agent to apply security best practices. These practices include private S3 buckets, Content Security Policy (CSP) headers, HTTPS enforcement, and managed security response headers. Always review the generated configuration before deploying to production environments.

For production environments with CI/CD, see [Set up CodePipeline](agent-sops-deployment-pipeline.md "agent-sops-deployment-pipeline.md").

## Troubleshooting

###### Application type not supported

Verify that all prerequisites are met. If your application meets the prerequisites but is reported as unsupported, prompt your coding agent to attempt the deployment. Minor adjustments may be sufficient.

For any other troubleshooting issues, you can contact [AWS Support](https://console.aws.amazon.com/support/home/ "https://console.aws.amazon.com/support/home/") or post your question on [re:Post](https://repost.aws/ "https://repost.aws/") and tag it to the AWS MCP Server to ask the community.
