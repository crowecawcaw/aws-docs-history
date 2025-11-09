AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Set up CI/CD pipelines with AWS CodePipeline

AWS CodePipeline is a continuous delivery service that you can use tomodel, visualize, and automate
your software release process. App2Container integrates with CodePipeline to automate a consistent release
process while it gives you insights to monitor and manage your pipeline. For more
information, see [What is AWS CodePipeline?](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md") in the
_AWS CodePipeline User Guide_.

Before you run the **generate pipeline** command, review the
`pipeline.json` file that the **generate
app-deployment** command creates. Configure the parameters for your CodeCommit
pipeline as follows:

- Set the flags to enable CodePipeline deployment.
  - sourceInfo
    - CodeCommit – enabled: **true**
    - ExistingGitRepo – enabled: **false**
    - AzureRepo – enabled: **false**

  - pipelineInfo
    - CodePipeline – enabled: **true**
    - Jenkins – enabled: **false**
    - AzureDevOps – enabled: **false**

###### Important

You must set the `sourceInfo` and `pipelineInfo` flags as described or
else the pipeline integration will fail.

###### Contents

- [Validation](#integrations-codepipeline-workflow-validation "#integrations-codepipeline-workflow-validation")
- [Output](#integrations-codepipeline-workflow-output "#integrations-codepipeline-workflow-output")

## Validation

###### File validation

When you run the `generate pipeline` command, App2Container performs the following
validation to ensure that your pipeline deploys successfully:

- Checks that CodeCommit is the only source repository that you've activated in the
  `sourceInfo` section of the `pipeline.json`
  file, and that this section contains all required properties.
- Checks that CodePipeline is the only pipeline that you've activated in the
  `pipelineInfo` section of the `pipeline.json`
  file, and that this section contains all required properties.

###### Deployment validation

If you use the App2Container `generate pipeline` command with `--deploy`, the
`pipeline.json` file that App2Container creates will have the required
configuration already defined. If you don't specify the `--deploy` flag
for the command, or you use your own deployment, you must edit the
`pipeline.json` file to specify the required configuration. For more
information, see [Configuring container pipelines](config-pipeline.md "config-pipeline.md").

## Output

The `generate pipeline` command generates the following artifacts for CodePipeline
pipelines. If you don't use the `--deploy` option with the `generate
 pipeline` command, you can edit the artifacts that App2Container added to your CodeCommit
repository to create your pipeline from the CodePipeline interface (AWS CLI or AWS Management Console).

###### Note

If you run the `generate pipeline` command with the
`--deploy` option, App2Container creates the pipeline in CodePipeline, and starts
the pipeline build.

App2Container generates the following artifacts:

**`buildspec.yml` files**

Used to build the application container image and uploads it to
Amazon ECR.

**AWS CloudFormation templates**

Used to create your pipeline in CodePipeline along with other
required resources.

###### Note

If your CodeCommit repository doesn't already exist, App2Containercreates it for you.
