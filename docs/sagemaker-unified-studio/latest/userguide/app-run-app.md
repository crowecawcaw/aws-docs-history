# Run a deployed Amazon Bedrock app

The following instructions show you the steps you take to run a deployed Amazon Bedrock in SageMaker Unified Studio chat agent app.

###### Topics

- [Prerequisites for running a chat agent app](#app-run-app-prerequisites "#app-run-app-prerequisites")
- [Run the app](#app-deploy-app-run "#app-deploy-app-run")

## Prerequisites for running a chat agent app

Before you can run an app that you have exported, you must first do the following:

###### To prepare for running an app

1. Download and install Node.js. For more information, see [Download
   Node.js](https://nodejs.org/en/download/package-manager "https://nodejs.org/en/download/package-manager").
2. At the command prompt, install third-party Node.js libraries by running the following commands:

```
npm install minimist
npm install aws-sdk
npm install @aws-sdk/credential-providers
npm install @aws-sdk/client-bedrock-agent-runtime
npm install @aws-sdk/client-bedrock-runtime
```

For a flow app you also need the following

```
npm install @aws-sdk/client-bedrock-agent
```

3. Create or update an IAM role in which you want to run the app. For the policy,
   use the policy created by `deployApp.sh` when you exported the app. The policy name
   is `BRStudioExportedAppInvocationRolePolicy-`exportProjectId``.
   The policy is declared in invocation-policy-\*.json.
   For more information, see [Creating roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").

## Run the app

To run your app, you need an IAM role with with permissions to invoke Amazon Bedrock
resources. When you deploy the app, the AWS CloudFormation stack deployed through
`deployApp.sh` script provisions a suitable policy in your AWS account (declared in `invocation-policy-*.json`).

###### To run the app

1. Switch to the IAM role that you created in step 3 of [Prerequisites for running a chat agent app](#app-run-app-prerequisites "#app-run-app-prerequisites").
2. Run the app by entering the command you noted in step 3 of [Deploy the exported app](app-deploy-app.md#app-deploy-app-deploy "app-deploy-app.md#app-deploy-app-deploy").
