

# Options for deploying your application with AWS SAM
<a name="deploying-options"></a>

With AWS SAM, you can deploy your application manually and automate deployments. Use the AWS SAM CLI to manually deploy your application. To automate deployment, use pipelines and a continuous integration and continuous deployment (CI/CD) system. The topics in this section provide information on both approaches.

**Topics**
+ [How to use the AWS SAM CLI to manually deploy](#serverless-sam-cli-using-package-and-deploy)
+ [Deploy with CI/CD systems and pipelines](#serverless-deploying-ci-cd)
+ [Gradual deployments](#serverless-deploying-gradual)
+ [Troubleshooting deployments using the AWS SAM CLI](#serverless-deploying-troubleshooting)
+ [Learn more](#serverless-sam-cli-using-invoke-learn)

## How to use the AWS SAM CLI to manually deploy
<a name="serverless-sam-cli-using-package-and-deploy"></a>

After you develop and test your serverless application locally, you can deploy your application using the **[sam deploy](sam-cli-command-reference-sam-deploy.md)** command.

To have AWS SAM guide you through the deployment with prompts, specify the **--guided** flag. When you specify this flag, the **sam deploy** command zips your application artifacts, uploads them either to Amazon Simple Storage Service (Amazon S3) (for .zip file archives) or to Amazon Elastic Container Registry (Amazon ECR) (for container images). The command then deploys your application to the AWS Cloud.

**Example:**

```
# Deploy an application using prompts:
sam deploy --guided
```

## Deploy with CI/CD systems and pipelines
<a name="serverless-deploying-ci-cd"></a>

AWS SAM helps you automate deployment using pipelines and a continuous integration and continuous deployment (CI/CD) system. AWS SAM can be used to create pipelines and simplify CI/CD tasks for serverless applications. Multiple CI/CD systems support AWS SAM build container images, and AWS SAM also provides a set of default pipeline templates for multiple CI/CD systems that encapsulate AWS's deployment best practices. 

For more information, see [Using CI/CD systems and pipelines to deploy with AWS SAM](deploying-cicd-overview.md).

## Gradual deployments
<a name="serverless-deploying-gradual"></a>

If you want to deploy your AWS SAM application gradually rather than all at once, you can specify deployment configurations that AWS CodeDeploy provides. For more information, see [Working with deployment configurations in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) in the *AWS CodeDeploy User Guide*.

For information about configuring your AWS SAM application to deploy gradually, see [Deploying serverless applications gradually with AWS SAM](automating-updates-to-serverless-apps.md).

## Troubleshooting deployments using the AWS SAM CLI
<a name="serverless-deploying-troubleshooting"></a>

### AWS SAM CLI error: "Security Constraints Not Satisfied"
<a name="troubleshooting-security-constraints"></a>

When running **sam deploy --guided**, you're prompted with the question `HelloWorldFunction may not have authorization defined, Is this okay? [y/N]`. If you respond to this prompt with **N** (the default response), you see the following error:

```
 
Error: Security Constraints Not Satisfied
```

The prompt is informing you that the application you're about to deploy might have an Amazon API Gateway API configured without authorization. By responding **N** to this prompt, you're saying that this is not OK.

To fix this, you have the following options:
+ Configure your application with authorization. For information about configuring authorization, see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md).
+ Respond to this question with **Y** to indicate that you're OK with deploying an application that has an API Gateway API configured without authorization.

## Learn more
<a name="serverless-sam-cli-using-invoke-learn"></a>

For hands-on examples of deploying serverless applications, see the following from *The Complete AWS SAM Workshop*:
+ [Module 3 - Deploy manually](https://s12d.com/sam-ws-en-manual-deploy) – Learn how to build, package, and deploy a serverless application using the AWS SAM CLI.
+ [Module 4 - CI/CD](https://s12d.com/sam-ws-en-cicd-deploy) – Learn how to automate the build, package, and deployment phases by creating a *continuous integration and delivery (CI/CD)* pipeline.