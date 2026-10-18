

# Creating a Lambda Web Function
<a name="web-functions-create"></a>

To deploy an app with Lambda Web Functions, you create a Web Function with a revision and an endpoint to receive traffic. The console and the `aws lambda-web deploy` command can create the Web Function, its first revision, and its first endpoint. Revisions are immutable snapshots of your code and configuration. An endpoint routes requests to an active revision. For more information about these resources, see [Core concepts](web-functions-how-it-works.md). This topic shows how to create them using the Lambda console and the AWS CLI.

## Prerequisites
<a name="web-functions-create-prereqs"></a>

Before you begin, make sure you have the following:
+ An AWS account. To create one, see [Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html) in the *AWS Account Management Reference Guide*.
+ Permissions to manage Web Functions, to pass the execution role to Lambda (`iam:PassRole`), and to create or use the supporting Amazon S3 and IAM resources.

The console creates or reuses the resources that your Web Function needs, including an execution role and an Amazon S3 bucket for your code.

To follow the AWS CLI procedure, you also need:
+ AWS CLI version 2, in a release that includes the `aws lambda-web` commands. To check, run `aws lambda-web help`. If you installed the AWS CLI using an official installer or install script, run `aws update` to update to the latest version. Otherwise, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ AWS credentials and an AWS Region configured for the AWS CLI.
+ For `aws lambda-web deploy`, permission to call `sts:GetCallerIdentity`, `s3:ListBucket` on the deployment bucket, and `s3:PutObject`, `s3:GetObject`, and `s3:GetObjectVersion` on its objects.
+ If `aws lambda-web deploy` creates the default resources, permission to call `iam:GetRole`, `iam:CreateRole`, `iam:PutRolePolicy`, `s3:CreateBucket`, `s3:PutBucketPolicy`, and `s3:PutBucketVersioning`.
+ (Optional) Node.js 24 or later for local development. To install Node.js, see [Download Node.js](https://nodejs.org/en/download/) on the Node.js website.

## Creating a Web Function (console)
<a name="web-functions-create-console"></a>

Use the Lambda console to create a Web Function, its first revision, and its first endpoint to receive traffic.

**To create a Web Function and endpoint (console)**

1. Open the Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. In the navigation pane, choose **Web Functions**.

1. Choose **Create Web Function**.

1. Under **Basic information**, do the following:

   1. For **Function name**, enter a name for your Web Function.

   1. For **Runtime**, keep the default runtime.

   1. For **Code source**, keep **Hello World template** to start from a preconfigured example application. To deploy your own code instead, choose **Upload ZIP file** or **Amazon S3**.

1. Under **Endpoint configuration**, do the following:

   1. For **Endpoint name**, enter a name for the endpoint.

   1. For **Type**, keep **Home-Region**. A Home-Region endpoint runs in a single Region, which makes it the simplest configuration for your first Web Function. For multi-Region options, see [Lambda Web Function endpoints](web-functions-endpoints.md).
**Note**  
You can't change the endpoint type after creation.

   1. For **Authentication type**, choose **Application-managed authentication**. With this option, Lambda forwards all requests to your app, so your app handles authentication. To restrict access instead, choose **IAM authentication**, which requires callers to sign requests. Requests to `HomeRegion` and `PerRegion` endpoints use AWS Signature Version 4 (SigV4). Requests to `MultiRegion` endpoints use Signature Version 4a (SigV4a). For more information, see [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md).

   1. For **Auto deployment**, keep **Latest revision**. With this mode, Lambda automatically routes all traffic to each new revision after it becomes **Active**. For manual traffic control with revision weights, choose **Disabled**. For more information, see [Deployment patterns](web-functions-deployment.md).

1. (Optional) Expand **Additional configurations** to override the default settings. By default, Lambda creates an execution role with permission to upload logs to Amazon CloudWatch, and an Amazon S3 bucket in your account to store your code. In this section you can instead choose an existing IAM role or your own Amazon S3 bucket, and you can also configure encryption with a customer managed key, the maximum concurrency per environment, environment variables, and tags.

1. Choose **Create Web Function**.

When you choose **Create Web Function**, Lambda creates the Web Function resource together with its first revision, and it creates the endpoint at the same time. The revision starts in the **Pending** state while Lambda downloads your code and prepares a code artifact from it, and then transitions to **Active**. The endpoint also starts in the **Pending** state. The Web Function, its revision, and its endpoint each progress through these states independently. For more information about revisions and lifecycle states, see [Core concepts](web-functions-how-it-works.md).

The endpoint starts serving traffic when it reaches **Active** and there is an **Active** revision for it to route to. To find the endpoint's domain name, on the function detail page, choose the **Endpoints** tab, and then choose the endpoint. To serve the app on your own domain, put an Amazon CloudFront distribution in front of the endpoint. For more information about endpoint types and domain names, see [Lambda Web Function endpoints](web-functions-endpoints.md).

To confirm that your app is serving traffic, send a request to the domain name. Because you chose **Application-managed authentication**, you can send a plain request without signing it.

```
curl https://{{your-endpoint-domain-name}}/
```

A successful response means your Web Function is receiving traffic and your app is serving requests.

## Creating a Web Function (AWS CLI)
<a name="web-functions-create-cli"></a>

Create and deploy a Web Function from your terminal. The starter command generates a small Node.js HTTP server, deploys it, and returns an HTTPS endpoint URL.

### Deploy and test your Web Function
<a name="web-functions-create-cli-deploy"></a>

**To deploy and test a starter Web Function**

1. Run the following command:

   ```
   aws lambda-web deploy --name my-web-app --hello-world
   ```

   `--hello-world` writes the starter files to `./my-web-app`, creating the directory if it does not exist. The starter contains `server.ts`, a TypeScript HTTP server, and `package.json`, `README.md`, and `AGENTS.md`.

1. When the deployment is complete, copy the endpoint URL from the output. The URL looks similar to the following:

   ```
   https://bcdfghjklmnpqrst.b7t.lambda-web.us-east-1.on.aws
   ```

1. Send a request to the endpoint URL that you copied in the previous step. Replace {{endpoint-url}} with that URL:

   ```
   curl {{endpoint-url}}
   ```

   The starter returns a response similar to the following:

   ```
   {"message":"Hello from Lambda Web!","path":"/"}
   ```

By default, the starter endpoint accepts requests without authentication. To require IAM authorization, add `--auth-type IamAuth`. For information about controlling access to your endpoint, see [Lambda Web Function endpoint access control](web-functions-endpoint-access-control.md).

### What the command creates
<a name="web-functions-create-cli-resources"></a>

On the first deployment, the command:
+ Creates or reuses an Amazon S3 bucket with versioning enabled for deployment packages.
+ Creates or reuses an IAM execution role with Amazon CloudWatch Logs permissions.
+ Creates the Web Function and its first revision.
+ Creates a `HomeRegion` endpoint named `dev` and waits for it to become `Active`. To use a different name, add `--endpoint-name`.

A Web Function contains immutable revisions of your code and configuration. On later deployments, the command creates another revision. The `dev` endpoint uses `LatestRevision` mode and serves the revision after it becomes active.

### Deploy a change
<a name="web-functions-create-cli-change"></a>

After you edit the starter application, run:

```
aws lambda-web deploy \
  --name my-web-app \
  --code ./my-web-app
```

Running this command uploads your updated package, creates a revision, and waits for the revision to become `Active`. The `dev` endpoint has `autoDeploymentMode` set to `LatestRevision` and serves the revision automatically. Its URL remains the same.

To deploy your own app instead of the starter, pass its directory to `--code`. Your server must listen on the host and port in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. By default, the runtime loads `index.js` at the root of the deployment package. To use a different entry file, set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable. Lambda does not verify that your server starts listening when it creates the revision. As a result, the revision and endpoint can show `Active` even if requests fail. For more information, see [Lambda Web Function runtimes](web-functions-runtimes.md).

### Use existing AWS resources
<a name="web-functions-create-cli-existing-resources"></a>

If you already manage an Amazon S3 bucket or IAM execution role, use the following command to reuse those resources instead of creating defaults. The bucket must have versioning enabled and a bucket policy that grants the Lambda service principal (`lambda.amazonaws.com`) `s3:GetObject` and `s3:GetObjectVersion`. The command does not change the configuration of a bucket that you specify. For bucket requirements, see [Bucket policy for Lambda](web-functions-code-s3.md#web-functions-code-s3-bucket-policy). Replace the example resource values with your own.

```
aws lambda-web deploy \
  --name my-web-app \
  --code ./my-web-app \
  --bucket-name amzn-s3-demo-bucket \
  --execution-role-arn arn:aws:iam::111122223333:role/my-web-app-execution-role
```

The execution role must allow Lambda to assume it and must grant the permissions that your application needs. For more information, see [Execution role](web-functions-permissions.md#web-functions-permissions-execution-role).

You can omit either resource option to let `deploy` create defaults. When `deploy` creates a Web Function without `--hello-world`, or adds an endpoint, it asks you to press Enter to confirm. In a script or CI/CD pipeline, add `--create` to confirm without a prompt.

### Use the API commands directly
<a name="web-functions-create-cli-api"></a>

The `deploy` command uploads your code to Amazon S3 and creates the Web Function, revision, and endpoint for you. To control each step yourself, use the AWS CLI commands that map to the API operations, such as `create-web-function`, `create-web-function-revision`, and `update-web-function-endpoint`. In the following commands, replace each user input placeholder with your own information.

**To create a Web Function with the API commands (AWS CLI)**

1. Create a .zip deployment package from your app directory, with your entry file at the root of the package. Upload the package to an Amazon S3 bucket that meets the requirements in [Prerequisites](web-functions-code-s3.md#web-functions-code-s3-requirements). The following commands create the package and use the AWS CLI to upload it.

   ```
   cd {{my-app}}
   zip -r ../my-app.zip .
   aws s3 cp ../my-app.zip s3://{{amzn-s3-demo-bucket}}/my-app.zip
   ```

1. Use the following AWS CLI command to create the Web Function with its first revision and endpoint. In `revisionConfig`, `buildConfig` specifies the code location and runtime, and `serviceConfig` specifies the execution role. The `endpointConfig` property defines the endpoint.

   ```
   aws lambda-web create-web-function \
       --function-name {{my-web-app}} \
       --revision-config '{
         "buildConfig": {
           "codeConfig": {
             "s3Object": { "bucket": "{{amzn-s3-demo-bucket}}", "key": "my-app.zip" }
           },
           "runtimeConfig": { "runtime": "nodejs24.x" }
         },
         "serviceConfig": {
           "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-app-execution-role}}"
         }
       }' \
       --endpoint-config '{
         "endpointName": "{{my-endpoint}}",
         "endpointType": "HomeRegion",
         "authType": "ApplicationManaged",
         "autoDeploymentMode": "LatestRevision"
       }'
   ```

   The `autoDeploymentMode` property is optional. If you omit it, the default is `Disabled`, and the endpoint doesn't route traffic to new revisions automatically. Note the `revisionId` of the revision in the response.

1. Wait until the revision is `Active`. Replace {{rev-abc12}} with the revision ID from the previous step.

   ```
   aws lambda-web wait web-function-revision-active \
       --function-name {{my-web-app}} \
       --revision-id {{rev-abc12}}
   ```

1. Get the endpoint's details.

   ```
   aws lambda-web get-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{my-endpoint}}
   ```

   When the endpoint's `state` is `Active`, send requests to its `domainName`. The response looks like the following excerpt.

   ```
   {
       "endpointName": "my-endpoint",
       "endpointType": "HomeRegion",
       "domainName": "bcdfghjklmnpqrst.b7t.lambda-web.us-east-1.on.aws",
       "authType": "ApplicationManaged",
       "autoDeploymentMode": "LatestRevision",
       "state": "Active",
       "updateStatus": "Successful"
   }
   ```

**To deploy a change with the API commands (AWS CLI)**
+ Upload a new package and create a revision. A revision is a complete snapshot, so pass the full `buildConfig` and `serviceConfig` each time.

  ```
  aws s3 cp ../my-app.zip s3://{{amzn-s3-demo-bucket}}/my-app.zip
  aws lambda-web create-web-function-revision \
      --function-name {{my-web-app}} \
      --build-config '{
        "codeConfig": {
          "s3Object": { "bucket": "{{amzn-s3-demo-bucket}}", "key": "my-app.zip" }
        },
        "runtimeConfig": { "runtime": "nodejs24.x" }
      }' \
      --service-config '{
        "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-app-execution-role}}"
      }'
  ```

  Because the endpoint has `autoDeploymentMode` set to `LatestRevision`, it routes all traffic to the new revision after the revision becomes `Active`. If you set `autoDeploymentMode` to `Disabled`, you route traffic with `update-web-function-endpoint` and revision weights instead. For more information, see [Deployment patterns](web-functions-deployment.md).

## Clean up
<a name="web-functions-create-cleanup"></a>

When you no longer need the Web Function, delete it:

```
aws lambda-web delete-web-function --function-name my-web-app
```

This command also deletes the Web Function's endpoints and revisions. It does not delete the resources that `deploy` created or used: the IAM execution role (`awscli-lambdaweb-my-web-app` by default), the deployment packages under `lambda-web/my-web-app/` in the Amazon S3 bucket (`awscli-lambdaweb-{{account-id}}-{{region}}-an` by default), including noncurrent object versions, or the Amazon CloudWatch Logs log groups for the Web Function. Delete those resources separately only if you no longer need them. The managed Amazon S3 bucket can be shared by other deployments in the same AWS account and Region.