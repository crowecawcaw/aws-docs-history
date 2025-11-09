AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container generate pipeline command

When you run the **generate pipeline** command, it generates the artifacts
that you need to create a CI/CD pipeline with CodePipeline, Jenkins, or Microsoft Azure DevOps services.
Your application pipeline settings and deployment artifacts determine the artifacts that you
create.

###### Note

For Windows applications, App2Container chooses the base image for your application container
and Amazon ECS cluster, based on the worker machine or application server OS where you run
the containerization command. Windows application containers running on Amazon EKS use
Windows Server Core 2019 for the base image.

You have two options for creating your pipeline:

- You can use the `--deploy` option to create your pipeline directly.
- You can review and customize pipeline artifacts, and then create your pipeline,
  with the AWS CLI or the AWS Management Console for CodePipeline. You can also create your pipeline in the
  native environments for Jenkins or Microsoft Azure DevOps pipelines.
  When the **generate pipeline** command generates artifacts and creates
  CI/CD pipelines, it accesses AWS resources, even if your application integrates with an
  external pipeline tool or service. App2Container needs administrator access to run the command with
  the `--deploy` option. For information on how to set up AWS Identity and Access Management (IAM) users
  for App2Container, see [Identity and access management in App2Container](iam-a2c.md "iam-a2c.md").

The **generate pipeline** command uses the
`pipeline.json` file that App2Container generates when you run the [generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md")
command. You can edit the `pipeline.json` file to specify your container
repository and target environments for Amazon ECS, Amazon EKS, or App Runner. For more information on how to
configure the `pipeline.json` file, see [Configuring container pipelines](config-pipeline.md "config-pipeline.md").

###### Note

If the command fails, an error message is displayed in the console, followed by
additional messaging to help you troubleshoot.

When you ran the **init** command, if you chose to automatically
upload logs to App2Container support if an error occurs, App2Container notifies you of the
success of the automatic upload of your application support bundle.

Otherwise, App2Container messaging directs you to upload application artifacts by
running the [upload-support-bundle](cmd-upload-support-bundle.md "cmd-upload-support-bundle.md") command for additional support.

## Syntax

```
app2container generate pipeline --application-id `id` [--deploy] [--profile `admin-profile`] [--help]
```

## Parameters and options

###### Parameters

**--application-id `id`**

The application ID _(required)_. After you run the [inventory](cmd-inventory.md "cmd-inventory.md") command, you can find the application ID in the `inventory.json`
file in one of the following locations:

- Linux: `/root/inventory.json`
- Windows: `C:\Users\Administrator\AppData\Local\.app2container-config\inventory.json`

**--profile `admin-profile`**

Use this option to specify a _named profile_ to run this
command. For more information about named profiles in AWS, see
[Named profiles](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")
in the AWS Command Line Interface User Guide

###### Options

**--deploy**

Use this option to create your CI/CD pipeline directly.

###### Note

When you use the `--deploy` option to create your CI/CD
pipeline directly, we recommend that you use the `--profile`
option to specify a _named profile_ that has elevated
permissions.

**--help**

Displays the command help.

## Output

You have two options for creating your CI/CD pipeline using the
**generate pipeline** command.

- You can use the `--deploy` option to create your pipeline directly.
- You can review and customize pipeline artifacts, and then create your pipeline,
  with the AWS CLI or the AWS Management Console for CodePipeline. You can also create your pipeline in
  the native environments for Jenkins or Microsoft Azure DevOps pipelines.

When you run the **generate pipeline** command, App2Container generates the
following artifacts and performs the following tasks.

CodePipeline

###### Generates pipeline artifacts for customization

- Generates CI/CD artifacts **generate pipeline
  `--application-id `id``**
  - Checks for AWS and Docker prerequisites
  - Creates a CodeCommit repository, if one doesn't already exist
  - Generates a buildspec file
  - Generates CloudFormation templates for a two-step pipeline to commit and
    build your application

###### Creates pipeline directly with deploy option

- When you run this command with the `--deploy` option, App2Container uses the same process to validate and
  customize your pipeline resources as it does when you deploy manually. Then it uses the settings from the files that it
  generated to create the pipeline for you: **generate pipeline
  `--application-id `id``
`--deploy`
`--profile
 `admin-profile``**

      + Performs all steps to validate and customize pipeline resources
      + Creates the CloudFormation stack for your pipeline

Jenkins

###### Generates pipeline artifacts for customization

- Generates CI/CD artifacts **generate pipeline
  `--application-id `id``**
  - Checks for AWS and Docker prerequisites
  - Creates a CodeCommit repository, if one doesn't exist already
  - Generates the following files for your pipeline definition:
    the `Jenkinsfile`, and the
    `config.xml` file that you can use with the
    Jenkins REST API
  - If your application runs on Amazon EKS, App2Container generates a CloudFormation template
    for a two-step pipeline to commit and build your application

###### Creates pipeline directly with deploy option

- When you run this command with the `--deploy` option, App2Container uses the same process to validate and
  customize your pipeline resources as it does when you deploy manually. App2Container then creates the pipeline for you with
  the settings from the files that it generates: **generate pipeline
  `--application-id `id`` `--deploy` `--profile 
`admin-profile``**
  - Performs all steps to validate and customize pipeline resources
  - Creates the pipeline in Jenkins, and starts the pipeline build

Azure DevOps

###### Generate pipeline artifacts for customization

- Generates CI/CD artifacts: **generate pipeline `--application-id `id``**
  - Checks for AWS, Microsoft Azure DevOps, and Docker prerequisites
  - Creates the Azure Repos Git repository, if it doesn't already exist
  - Commits updated files to the Azure Repos Git repository
  - Generates the following files for your pipeline definition:
    `main.yaml`, `build.yaml`,
    `release.yaml`, `pre-req.sh` (Linux) or
    `pre-req.ps1` (Windows), and
    `install-pre-req.sh`

###### Creates pipeline directly with deploy option

- When you run this command with the `--deploy` option, App2Container uses the same process to validate and
  customize your pipeline resources as it does when you deploy manually. Then it uses the settings from the files that it generated
  to create the pipeline for you: **generate pipeline `--application-id `id``
`--deploy` `--profile `admin-profile``**.

      + Performs all steps to validate and customize pipeline resources
      + Uses the configuration in `pipeline.json` to create an Azure DevOps
       pipeline, and initiate an Azure DevOps pipeline build

## Examples

To see examples of how to use the **generate pipeline** command, choose
your target environment.

CodePipeline
**Linux:**

The following Linux example shows the **generate pipeline** command with the
`--application-id` parameter that you use to create CodeCommit pipeline resources for your application.

````
`$` `sudo app2container generate pipeline --application-id `java-tomcat-9e8e4799```√ Created CodeCommit repository
√ Generated buildspec file(s)
√ Generated CloudFormation templates
√ Committed files to CodeCommit repository
Pipeline resource template generation successful for application java-tomcat-9e8e4799

You're all set to use AWS CloudFormation to manage your pipeline stack.

Next Steps:
1. Edit the CloudFormation template as necessary.
2. Create a pipeline stack using the AWS CLI or the AWS Console. AWS CLI command:

aws cloudformation deploy --template-file /root/app2container/java-tomcat-9e8e4799/Artifacts/Pipeline/CodePipeline/ecs-pipeline-master.yml --capabilities CAPABILITY_NAMED_IAM --stack-name app2container-java-tomcat-9e8e4799-ecs-pipeline-stack`
````

The following Linux example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a CodeCommit pipeline for your application.

````
`$` `sudo app2container generate pipeline `--deploy` --application-id `java-tomcat-9e8e4799```√ Generated buildspec file(s)
√ Generated CloudFormation templates
√ Committed files to CodeCommit repository
√ Initiated CloudFormation stack creation. This may take a few minutes. Please visit the AWS CloudFormation Console to track progress.
√ Deployed pipeline through CloudFormation
Pipeline deployment successful for application --application-id `java-tomcat-9e8e4799`

Successfully created AWS CodePipeline stack 'app2container---application-id `java-tomcat-9e8e4799`-ecs-pipeline-stack' for application. Check the AWS CloudFormation Console for additional details.`
````

The following Linux example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a pipeline for an application that runs on AWS App Runner.

````
`$` `sudo app2container generate pipeline `--deploy` --application-id `java-tomcat-9e8e4799```√ Created CodeCommit repository
√ Generated buildspec file(s)
√ Generated CloudFormation templates
√ Committed files to CodeCommit repository
√ Initiated CloudFormation stack creation. This may take a few minutes. To track progress, open the AWS CloudFormation console.
√ Deployed pipeline through CloudFormation
Pipeline deployment successful for application java-tomcat-9e8e4799

Successfully created AWS CodePipeline stack 'a2c---application-id `java-tomcat-9e8e4799`-ecs-pipeline-stack' for application. Check the AWS CloudFormation Console for additional details.`
````

**Windows:**

The following Tools for Windows PowerShell example shows the **generate pipeline** command with the
`--application-id` parameter that you use to create CodeCommit pipeline resources for your application.

````
`PS>` `app2container generate pipeline --application-id `iis-smarts-51d2dbf8```√ Created CodeCommit repository
√ Generated buildspec file(s)
√ Generated CloudFormation templates
√ Committed files to CodeCommit repository
Pipeline resource template generation successful for application --application-id `iis-smarts-51d2dbf8`

You're all set to use AWS CloudFormation to manage your pipeline stack.

Next Steps:
1. Edit the CloudFormation template as necessary.
2. Create a pipeline stack using the AWS CLI or the AWS Console. AWS CLI command:

aws cloudformation deploy --template-file C:\Users\Administrator\AppData\Local\app2container\--application-id `iis-smarts-51d2dbf8`\Artifacts\Pipeline\CodePipeline\ecs-pipeline-master.yml --capabilities CAPABILITY_NAMED_IAM --stack-name app2container---application-id `iis-smarts-51d2dbf8`-652becbe-ecs-pipeline-stack`
````

The following Tools for Windows PowerShell example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a CodeCommit pipeline for your application.

````
`PS>` `app2container generate pipeline `--deploy` --application-id `iis-smarts-51d2dbf8```√ Generated buildspec file(s)
√ Generated CloudFormation templates
√ Committed files to CodeCommit repository
√ Initiated CloudFormation stack creation. This may take a few minutes. Please visit the AWS CloudFormation Console to track progress.
√ Deployed pipeline through CloudFormation
Pipeline deployment successful for application --application-id `iis-smarts-51d2dbf8`

Successfully created AWS CodePipeline stack 'app2container---application-id `iis-smarts-51d2dbf8`-ecs-pipeline-stack' for application. Check the AWS CloudFormation Console for additional details.`
````

Jenkins
**Linux:**

The following Linux example shows the **generate pipeline** command with the
`--application-id` parameter that you use to create Jenkins pipeline resources for your application.

````
`$` `sudo app2container generate pipeline --application-id `java-tomcat-9e8e4799```√ Discovered existing CodeCommit repository
√ Generated Jenkins pipeline configuration file
√ Generated Jenkinsfile
√ Committed files to source repository
Pipeline resource template generation successful for application java-tomcat-9e8e4799

You're all set to use Jenkins to manage your pipeline.

Next Steps:
1. Edit the Jenkinsfile as necessary.
2. Create a Jenkins Pipeline using the Jenkins REST API or the Jenkins Dashboard. Jenkins API command:

 curl -k -XPOST https://ec2-`1-234-567-890.<Region>`.compute.amazonaws.com:8443/createItem?name=a2c-java-tomcat-9e8e4799-eks-pipeline-stack -u a2c:1164afa1fe791a4c86fd3117d7bc5d93e2 --data-binary @/home/ubuntu/app2container/java-tomcat-9e8e4799/Artifacts/Pipeline/Jenkins/config.xml -H "Content-Type:text/xml"`
````

The following Linux example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a Jenkins pipeline for your application.

````
`$` `sudo app2container generate pipeline `--deploy` --application-id `java-tomcat-9e8e4799```√ Discovered existing CodeCommit repository
√ Generated Jenkins pipeline configuration file
√ Generated Jenkinsfile
√ Committed files to source repository
√ Initiated Jenkins pipeline creation
√ Deployed pipeline through Jenkins
Pipeline deployment successful for application java-tomcat-9e8e4799

Successfully created Jenkins Pipeline 'a2c-java-tomcat-9e8e4799-eks-pipeline' for application. Started a build of the pipeline.
Build link: https://ec2-`1-234-567-890.<Region>`.compute.amazonaws.com:8443/job/a2c-java-tomcat-9e8e4799-eks-pipeline/1`
````

**Windows:**

The following Tools for Windows PowerShell example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a Jenkins pipeline for your application.

````
`PS>` `app2container generate pipeline `--deploy` --application-id `iis-smarts-51d2dbf8```√ Validated Jenkins Nodes and Labels
√ Generated Jenkins pipeline configuration file
√ Generated Jenkinsfile
√ Committed files to source repository
√ Initiated Jenkins pipeline creation
√ Deployed pipeline through Jenkins
Pipeline deployment successful for application iis-smarts-51d2dbf8

Successfully created Jenkins Pipeline 'iis-smarts-51d2dbf8-eks-pipeline' for application. Started a build of the pipeline.
Build link: https://ec2-`1-234-567-890.<Region>`.compute.amazonaws.com:8443/job/iis-smarts-51d2dbf8-eks-pipeline/1`
````

Azure DevOps
**Linux:**

The following Linux example shows the **generate pipeline** command with the
`--application-id` parameter that you use to create Microsoft Azure DevOps pipeline resources for your application.

````
`$` `sudo app2container generate pipeline --application-id `java-tomcat-9e8e4799```✔ Discovered existing Azure repository
✔ Discovered existing Azure branch
✔ Generated pre-requisite installation scripts
✔ Generated pipeline definition files
✔ Committed artifacts to Microsoft Azure DevOps repository
Pipeline resource template generation successful for application java-tomcat-9e8e4799

You're all set to use pipeline definition files in /root/app2container/java-tomcat-9e8e4799/Artifacts/Pipeline/AzureDevOps to create your Azure DevOps pipeline.

Next Steps:
1. Edit the pipeline definition files as necessary.
2. Created a new Azure git repository at https://dev.azure.com/`a2c-azure-org`/`a2c-project`/_git/a2c-java-tomcat-9e8e4799
3. Go to your Microsoft Azure DevOps web console https://dev.azure.com/`a2c-azure-org`/`a2c-project`/_build and click on "New Pipeline".
4. For Repositories select "Azure Repos Git" and select the repo with name a2c-java-tomcat-9e8e4799
5. For "Configure your pipeline" step choose "Existing Azure Pipelines YAML file"
6. In the options for "branch" select main and for "path" select /pipeline.yaml
7. Click "continue" and then click "Run"`
````

The following Linux example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a Microsoft Azure DevOps pipeline for your application.

````
`$` `sudo app2container generate pipeline `--deploy` --application-id `java-tomcat-9e8e4799```✔ Discovered existing Azure repository
✔ Discovered existing Azure branch
✔ Generated pre-requisite installation scripts
✔ Generated pipeline definition files
✔ Committed artifacts to Microsoft Azure DevOps repository
✔ Initiated Microsoft Azure DevOps pipeline creation
✔ Deployed pipeline through Microsoft Azure DevOps
Pipeline deployment successful for application java-tomcat-9e8e4799

Successfully created and ran Microsoft Azure DevOps Pipeline 'a2c-java-tomcat-9e8e4799-pipeline' for the application, url: https://dev.azure.com/`a2c-azure-org`/`a2c-project`/_build?definitionId=152`
````

**Windows:**

The following Windows example shows the **generate pipeline** command with the
`--application-id` parameter that you use to create Microsoft Azure DevOps pipeline resources for your application.

```
`PS>` `app2container generate pipeline iis-smarts-51d2dbf8``✔ Discovered existing Azure repository
✔ Discovered existing Azure branch
✔ Generated pre-requisite installation scripts
✔ Generated pipeline definition files
✔ Committed artifacts to Microsoft Azure DevOps repository
Pipeline resource template generation successful for application iis-smarts-51d2dbf8

You're all set to use pipeline definition files in C:\Users\Administrator\AppData\Local\app2container\iis-smarts-51d2dbf8\Artifacts\Pipeline\AzureDevOps to create your Azure DevOps pipeline.

Next Steps:
1. Edit the pipeline definition files as necessary.
2. Created a new Azure git repository at https://dev.azure.com/`a2c-azure-org`/`a2c-project`/_git/a2c-iis-smarts-51d2dbf8
3. Go to your Microsoft Azure DevOps web console https://dev.azure.com/`a2c-azure-org`/`a2c-project`/_build and click on "New Pipeline".
4. For Repositories select "Azure Repos Git" and select the repo with name a2c-iis-smarts-51d2dbf8
5. For "Configure your pipeline" step choose "Existing Azure Pipelines YAML file"
6. In the options for "branch" select main and for "path" select /pipeline.yaml
7. Click "continue" and then click "Run"`
```

The following Windows example shows the **generate pipeline** command with
the `--application-id` parameter and the `--deploy` option that you use to create a Microsoft Azure DevOps pipeline for your application.

```
`PS>` `app2container generate pipeline `--deploy` iis-smarts-51d2dbf8``✔ Discovered existing Azure repository
✔ Discovered existing Azure branch
✔ Generated pre-requisite installation scripts
✔ Generated pipeline definition files
✔ Committed artifacts to Microsoft Azure DevOps repository
✔ Initiated Microsoft Azure DevOps pipeline creation
✔ Deployed pipeline through Microsoft Azure DevOps
Pipeline deployment successful for application iis-smarts-51d2dbf8

Successfully created and ran Microsoft Azure DevOps Pipeline 'a2c-iis-smarts-51d2dbf8-pipeline' for the application, url: https://dev.azure.com/`a2c-azure-org`/`a2c-project`/_build?definitionId=151`
```
