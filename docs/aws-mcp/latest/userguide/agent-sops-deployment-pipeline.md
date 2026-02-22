# Set up CodePipeline

This SOP creates a CI/CD pipeline using AWS CodePipeline. The pipeline automatically builds, tests, and deploys your application when changes are pushed to a source repository branch.

For prerequisites and security information, see [AWS Deployment SOPs](agent-sops-deployment.md "agent-sops-deployment.md").

## Requirements

Your application must already be configured as a CDK application with existing infrastructure code. This SOP works best after deploying with [Frontend applications](agent-sops-deployment-frontend.md "agent-sops-deployment-frontend.md") or [Supabase applications](agent-sops-deployment-supabase.md "agent-sops-deployment-supabase.md").

###### Important

This SOP requires you to manually approve an AWS CodeConnections resource in your web browser. You need permissions to install and configure the connection in your repository or organization.

## Example prompt

To set up a pipeline, prompt your coding agent with the following: `Set up a pipeline for my application`.

## Steps your coding agent takes

Your coding agent commits changes after each significant step to the `deploy-to-aws` branch.

1. Scans the project to detect existing CDK infrastructure, stacks, and application configuration
2. Identifies available quality checks (linting, unit tests) and verifies they pass locally
3. Presents a detection summary and asks you to confirm the configuration
4. Creates an AWS CodeConnections resource to connect AWS to your source repository
5. Creates production secrets in [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"), if your application uses Lambda functions
6. Generates CDK infrastructure code for the pipeline
7. Deploys the pipeline stack through [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
8. Prompts you to authorize the connection in the AWS console
9. Verifies the pipeline triggers and runs successfully
10. Records pipeline configuration and deployment details in your repository

## Manual steps

During Step 8, you must complete authorization in the AWS console:

1. Open the [AWS CodeConnections console](https://console.aws.amazon.com/codesuite/settings/connections "https://console.aws.amazon.com/codesuite/settings/connections")
2. Find the pending connection for your application
3. Choose **Update pending connection**
4. Authorize and install the connector for your repository

## How it works

Your coding agent verifies your application has existing CDK infrastructure code. The agent then generates a pipeline stack using the CDK Pipelines module (`aws-cdk-lib/pipelines`). The pipeline is self-mutating. When you push changes to pipeline infrastructure code, the pipeline automatically updates itself.

The pipeline uses AWS CodeConnections to authenticate with your source repository. When changes are pushed to the configured branch, the pipeline executes the following stages:

1. _Source_ — Pulls source code from your repository through the CodeConnections resource
2. _Build (Synth)_ — Installs dependencies, runs quality checks, builds the application, and synthesizes CloudFormation templates using CDK
3. _Update pipeline_ — Self-mutation stage that updates the pipeline if its own infrastructure code changed
4. _Assets_ — Publishes file and Docker image assets required by the stacks
5. _Deploy_ — Deploys your application stacks to a production environment

The pipeline initially triggers on the `deploy-to-aws` branch. You can reconfigure the pipeline to trigger on `main` or another branch. To reconfigure, update the `branchName` context variable in the CDK configuration.

Quality checks are included only if they pass locally during setup. End-to-end tests are not included in the pipeline. The pipeline uses Secretlint to scan for exposed secrets in your codebase during each build. As part of the [AWS Shared Responsibility Model](data-protection.md "data-protection.md"), you should rotate exposed secrets immediately.

If your application includes Lambda functions, the SOP creates a separate production secret in AWS Secrets Manager (`{AppName}/prod/secrets`) and deploys both Lambda and frontend stacks through the pipeline.

The SOP prompts your coding agent to apply security best practices. Always review the generated pipeline configuration before deploying.

## Troubleshooting

For troubleshooting issues, you can contact [AWS Support](https://console.aws.amazon.com/support/home/ "https://console.aws.amazon.com/support/home/") or post your question on [re:Post](https://repost.aws/ "https://repost.aws/") and tag it to the AWS MCP Server to ask the community.
