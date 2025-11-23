# Use your app outside of Amazon SageMaker Unified Studio

With Amazon Bedrock in SageMaker Unified Studio, you can export the files for an [chat agent app](create-chat-app.md "create-chat-app.md") and a [flow app](create-flows-app.md "create-flows-app.md"). This
lets you can use the app outside of Amazon SageMaker Unified Studio.

When you export an app, Amazon Bedrock in SageMaker Unified Studio exports a zip file with the AWS CloudFormation
templates and other files required by your app. To use your app, you need to deploy the CloudFormation
templates to an AWS account. The actual contents of the zip file vary on the
Amazon Bedrock in SageMaker Unified Studio components that your app uses. After uncompressing the zip file, you
deploy the contents of the zip file into your AWS account (or another AWS account, if
you prefer).

###### Important

Once you export your app, it's your responsibility to audit the app files
and make sure they are correct. You can use the CloudFormation templates as you wish.

An app can include one or more different types of Amazon Bedrock in SageMaker Unified Studio components. For example, a
chat agent app could use a guardrail or a knowledge base. When you deploy your app's
components, Amazon Bedrock in SageMaker Unified Studio only deploys the AWS infrastructure files. The data source
files for a knowledge base and the secrets for a function aren't exported, and you have to
configure them during the deployment. After deploying the app to an AWS account, you can
run the app as a Node.js app.

## App export files

Depending on the composition of your app, the zip package contains some or all of the
following files:

- **README.md** — Instructions for deploying
  and running your app.
- **function-stack-\*.json** — CloudFormation template
  that creates your function component, if any. This includes:
  - An AWS Lambda [function](../../../bedrock/latest/studio-ug/functions.md "../../../bedrock/latest/studio-ug/functions.md") for
    calling the API defined in your OpenAPI schema.
  - An AWS Secret Manager secret for storing credentials to use when
    calling your API. This secret contains an empty value, and you are
    expected to update this secret manually.

- **knowledge-base-stack-\*.json** — AWS CloudFormation
  template that creates your
  [Knowledge Base data source](../../../bedrock/latest/studio-ug/data-sources.md#data-source-document "../../../bedrock/latest/studio-ug/data-sources.md#data-source-document"), if any. This includes an
  Knowledge Base for Amazon Bedrock configured with your selected data store and
  vector store. This knowledge base will not have the data you have uploaded in to
  Amazon Bedrock in SageMaker Unified Studio, and you are expected to provide data files manually.
- **flow-stack.json** — CloudFormation template
  that creates an Amazon Bedrock flows resource.
- **guardrails-stack-\*.json** — CloudFormation template
  that creates a [guardrail](../../../bedrock/latest/studio-ug/guardrails.md "../../../bedrock/latest/studio-ug/guardrails.md") for
  Amazon Bedrock, if any.
- **agent-stack.json** — CloudFormation template that
  creates an Amazon Bedrock Agent, if any.
- **invocation-policy-\*.json** — CloudFormation template
  that creates an IAM policy with the runtime permissions that you need
  to talk to your deployed chat agent app.
- **br-studio-app-stack-\*.json** — Parent
  stack that orchestrates the deployment of all AWS CloudFormation stacks included
  in the zip package.
- **deploy-app.sh** — Helper script that you
  use to deploy your app infrastructure into your AWS account.
- **code-snippet.mjs** — Example code snippet
  that you embed in your code to invoke the app.
- **amazon-bedrock-ide-app.mjs** — Standalone
  Node.js module to quickly test your deployed app.
- **aoss-encryption-policy-\*.json** — AOSS
  encryption policy necessary to use a Knowledge Base. This encryption policy is
  automatically created when your chat agent app contains an Amazon Bedrock in SageMaker Unified Studio Knowledge
  Base.
- **provisioning-inline-policy.json** — An example of
  an AWS IAM policy that contains the permissions required to provision the chat agent app
  resources. The permissions declared in this policy file are needed when
  deploying the AWS CloudFormation stacks.

You can modify this policy to better suit your needs. You may create a new
IAM principal with these policies, or attach these policies to an existing IAM
principal in your AWS account.

- **kms-key-policy.json** — An example of an
  AWS KMS key policy that contains required permissions for encrypting your chat agent app
  resources.

You can modify this key policy to better suit your needs. You may create a new
KMS key with this policy, or attach this policy to an existing KMS key in your
AWS account.

- **api-schema\*.json** — OpenAPI schema
  files associated with your function components, if any.

###### Topics

- [Export your Amazon Bedrock app](app-export-chat-app.md "app-export-chat-app.md")
- [Deploy an exported Amazon Bedrock app](app-deploy-app.md "app-deploy-app.md")
- [Run a deployed Amazon Bedrock app](app-run-app.md "app-run-app.md")
