AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Configuring container pipelines

This topic contains information about the files that you use to configure continuous
integration and deployment (CI/CD) pipelines for your application container with
CodePipeline, Jenkins, or Microsoft Azure DevOps.

###### Pipeline configuration files

- [pipeline.json file](#config-pipeline-json "#config-pipeline-json")

## pipeline.json file

When you run the **[generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md")** command, App2Container creates
a `pipeline.json` file for the application that the
`--application-id` parameter specifies. The **generate
pipeline** command uses this file, along with others, to generate pipeline
deployment artifacts. Before you run the **generate pipeline** command,
you can configure any of the fields in this file to customize your application container
pipeline.

###### Important

The `pipeline.json` file includes sections for all of the types
of pipelines that you can configure. This includes CodePipeline, Jenkins, and Microsoft Azure DevOps.

Configure exactly one source repository, and one type of pipeline. In each section, set one
Boolean value `enabled` flag to `true`, and all others to `false`. For Jenkins pipelines, you can choose to use either a
CodeCommit repository, or an existing Git repository.

CodePipeline

- sourceInfo
  - CodeCommit – enabled: **true**
  - ExistingGitRepo – enabled: **false**
  - AzureRepo – enabled: **false**

- pipelineInfo
  - CodePipeline – enabled: **true**
  - Jenkins – enabled: **false**
  - AzureDevOps – enabled: **false**

Jenkins

- sourceInfo
  - CodeCommit – enabled: **false**
  - ExistingGitRepo – enabled: **true**
  - AzureRepo – enabled: **false**

- pipelineInfo
  - CodePipeline – enabled: **false**
  - Jenkins – enabled: **true**
  - AzureDevOps – enabled: **false**

Microsoft Azure DevOps

- sourceInfo
  - CodeCommit – enabled: **false**
  - ExistingGitRepo – enabled: **false**
  - AzureRepo – enabled: **true**

- pipelineInfo
  - CodePipeline – enabled: **false**
  - Jenkins – enabled: **false**
  - AzureDevOps – enabled: **true**

App2Container enables CodeCommit as the source repository, and CodePipeline as the pipeline by default.

The application `pipeline.json` file includes the following
content. While all fields are configurable, the `a2CTemplateVersion` field
should not be changed. For key/value pairs that do not apply to your pipeline, set
string values to an empty string, numeric values to zero, and Boolean values to
false.

- imageInfo (object) – Contains parameters needed for
  Amazon ECR configuration.
  - image (string, required) – The full repository
    name of the application container image to store in Amazon ECR. _Must be in the
    format <application ID>.<repository name>:<tag>._

- sourceInfo (object) – Contains JSON objects
  for pipeline source repository configuration for CodePipeline or Jenkins pipelines. CodePipeline uses
  CodeCommit for its source repository, while Jenkins uses Git.
  - CodeCommit (object) – Contains parameters
    needed for AWS CodeCommit configuration.
    - enabled (Boolean, required) –
      A flag that indicates if you are targeting CodeCommit as the source repository
      for your pipeline.
    - repositoryName (string, required) –
      The name of the CodeCommit repository to use or create.
    - branch (string, required) – The name
      of the code branch in the CodeCommit repository to commit to.

  - ExistingGitRepo (object) – Contains
    parameters needed for Git repository configuration.
    - enabled (Boolean, required) –
      A flag that indicates if you are targeting Git as the source repository
      for your pipeline.
    - repositoryUri (string, required) –
      The URI of the Git repository to use for your pipeline. SSH access
      is required.
    - branch (string, required) – The
      name of the code branch in the Git repository to commit to.
    - sshKeyArn (string, required) – The
      ARN of the secret in Secrets Manager that is used to store the user name and SSH key
      for Git authentication from the Jenkins server.

  - AzureRepo (object) – Contains
    parameters to specify the Azure Repos Git repository where App2Container
    uploads pipeline artifacts for your application.
    - enabled (Boolean, required) – A flag
      that indicates if you want to use an Azure Repos Git repository
      as the source repository for an Azure DevOps pipeline that you
      create.
    - repositoryName (string, required) –
      The name of the Azure Repos Git repository that you want to use
      or create.
    - branch (string, required) – The name
      of the code branch in the Azure Repos Git repository where App2Container commits
      pipeline resources.

- releaseInfo (object) – Contains JSON
  objects with parameters needed to create a pipeline for your target deployment
  environments.
  - ECS | EKS | AppRunner (object) – Contains
    JSON objects representing the environments to target for deployment. The
    key name specifies the container management service that you are
    targeting for your application container pipeline. _Key must be
    "ECS", "EKS", or "AppRunner". At least one of the pipeline environments must be
    enabled._
    - beta (object) –
      - clusterName (string, required\*) –
        The name of the Amazon ECS or Amazon EKS cluster to set up in the AWS CloudFormation stack.
      - serviceName (string, required\*) –
        The name of the Amazon ECS service to set up in the AWS CloudFormation stack.

      _\* Applies only to Amazon ECS pipelines._
      - enabled (Boolean, required) – A
        flag indicating whether a beta environment should be configured.

    ###### Note

    Beta environments are not supported for App Runner.
    - prod (object) –
      - clusterName (string, required\*) –
        The name of the Amazon ECS or Amazon EKS cluster to set up in the AWS CloudFormation stack.

      _\* Does not apply to App Runner._
      - serviceName (string, required\*) –
        The name of the Amazon ECS service to set up in the AWS CloudFormation stack.

      _\* Applies only to Amazon ECS pipelines._
      - enabled (Boolean, required) – A
        flag indicating whether a prod environment should be configured.

- pipelineInfo (object) – Contains JSON
  objects with parameters needed to access and configure your target pipeline
  environments.
  - CodePipeline (object) – Contains parameters
    needed for CodePipeline configuration.
    - enabled (Boolean, required) –
      A flag that indicates if you are targeting CodePipeline for your pipeline.

  - Jenkins (object) – Contains parameters
    needed for Jenkins pipeline access and configuration.
    - enabled (Boolean, required) –
      A flag that indicates if you are targeting Jenkins for your pipeline.
    - jenkinsServerUrl (string, required) – The
      URL of the Jenkins server. The URL requires HTTPS protocol for
      secure access.
    - nodeLabels (array of strings, required) –
      A list of the labels that must be attached to the Jenkins agent node
      that runs the pipeline. All labels specified must be present on the
      agent node for it to run.
    - apiTokenArn (string, required) – The
      ARN of the secret in Secrets Manager that is used to authenticate to the Jenkins server.
    - repoSshCredentialId (string, required) –
      The ID that you create on the Jenkins server that the Jenkins
      agent node uses for SSH access to the Git repository.
      For more information about SSH credentials on
      Jenkins, see the [Using
      credentials](https://www.jenkins.io/doc/book/using/using-credentials/ "https://www.jenkins.io/doc/book/using/using-credentials/") chapter in the Jenkins _User Handbook_,
      available online..
    - awsCredentialId (string, required) – The
      AWS profile on the Jenkins server that is used to access AWS resources
      from the Jenkins agent node when the pipeline runs.

  - AzureDevOps (object) – Contains parameters
    that you need to access and configure your Azure DevOps pipeline.
    - enabled (Boolean, required) – A flag that
      indicates if you want App2Container to use Azure DevOps to set up your
      CI/CD pipeline.
    - organizationName (string, required) –
      The name of the organization that you set up under your Microsoft Azure account
      for Azure DevOps.
    - projectName (string, required) –
      The name of the project that you set up under your Microsoft Azure account for
      Azure DevOps.
    - serviceCredName (string, required) – The
      name of the service credentials that Azure DevOps uses to connect to AWS.
    - agentPoolName (string, required) – The
      name of the agent pool with the Microsoft-hosted agents that your pipeline uses to
      build and deploy updated container images for your application.
    - personalAccessTokenARN (string, required) – The
      ARN that identifies the Secrets Manager secret where you store your Microsoft Azure Personal Access Token (PAT).

###### Examples

The following example shows a `pipeline.json` file that uses the
CodePipeline environment as the pipeline for an IIS application that runs on Windows. The
application runs in a beta environment, and there is no prod environment configured
yet.

```
{
    "a2CTemplateVersion": "3.1",
    "imageInfo": {
        "image": "123456789012.dkr.ecr.us-west-1.amazonaws.com/iis-smarts-51d2dbf8:latest"
    },
    "sourceInfo": {
        "CodeCommit": {
            "repositoryName": "app2container-iis-smarts-51d2dbf8-ecs",
            "branch": "master"
        }
    },
    "releaseInfo": {
        "ECS": {
            "beta": {
                "clusterName": "a2c-iis-smarts-51d2dbf8-ECS-Cluster",
                "serviceName": "a2c-iis-smarts-51d2dbf8-ECS-LBWebAppStack-1EB23FI45ZYXW-Service-1mnoPQRS2Tu3",
                "enabled": true
            },
            "prod": {
                "clusterName": "",
                "serviceName": "",
                "enabled": false
            }
        }
    }
}
```

The following example shows a `pipeline.json` file that uses the
Jenkins environment as the pipeline for an IIS application that runs on Windows.

```
{
    "a2CTemplateVersion": "1.0",
    "imageInfo": {
        "image": "123456789012.dkr.ecr.us-west-1.amazonaws.com/iis-smarts-51d2dbf8:latest"
    },
    "sourceInfo": {
        "CodeCommit": {
            "enabled": false,
            "repositoryName": "",
            "branch": ""
        },
        "ExistingGitRepo": {
            "enabled": true,
            "repositoryUri": "git@ec2-12-34-567-890.us-west-1.compute.amazonaws.com/~/windows.git",
            "branch": "master",
            "sshKeyArn": "arn:aws:secretsmanager:us-east-1:123456789075:secret:test-We6XCm"
        }
    },
    "releaseInfo": {
        "ECS": {
            "beta": {
                "clusterName": "a2c-iis-smarts-51d2dbf8-ECS-Cluster",
                "serviceName": "a2c-iis-smarts-51d2dbf8-ECS-LBWebAppStack-1EB23FI45ZYXW-Service-1mnoPQRS2Tu3",
                "enabled": true
            },
            "prod": {
                "clusterName": "",
                "serviceName": "",
                "enabled": false
            }
        }
    },
    "resourceTags": [
        {
            "key": "example-key",
            "value": "example-value"
        }
    ],
    "pipelineInfo": {
        "CodePipeline": {
            "enabled": false
        },
        "Jenkins": {
            "enabled": true,
            "jenkinsServerUrl": "https://ec2-3-101-121-107.us-west-1.compute.amazonaws.com",
             "nodeLabels": [
                "windows2019",
                "beta"
            ],
            "apiTokenArn": "arn:aws:secretsmanager:us-east-1:123456789076:secret:test-We6XCm",
            "repoSshCredentialId": "12345678-90a1-23bc-de45-f67a123bc45d",
            "awsCredentialId": "beta-tester"
        }
    }
}
```

The following example shows a `pipeline.json` file that uses
Microsoft Azure DevOps as the pipeline for a Java application that runs on Linux.

```
{
 	"a2CTemplateVersion": "1.0",
 	"imageInfo": {
 		"image": "459632601910.dkr.ecr.us-west-1.amazonaws.com/java-tomcat-9e8e4799:latest"
 	},
 	"sourceInfo": {
 		"CodeCommit": {
 			"enabled": false,
 			"repositoryName": "a2c-java-tomcat-9e8e4799-ecs",
 			"branch": "master"
 		},
 		"ExistingGitRepo": {
 			"enabled": false,
 			"repositoryUri": "",
 			"branch": "",
 			"sshKeyArn": ""
 		},
 		"AzureRepo": {
 			"enabled": true,
 			"repositoryName": "a2c-java-tomcat-9e8e4799",
 			"branch": "main"
 		}
 	},
 	"releaseInfo": {
 		"ECS": {
 			"beta": {
 				"clusterName": "a2c-java-tomcat-9e8e4799-ECS-Cluster",
 				"serviceName": "a2c-java-tomcat-9e8e4799-ECS-JavaStack-1AB23CD45ZYXW-Service-1abcPQRS2Tu3",
 				"enabled": true
 			},
 			"prod": {
 				"clusterName": "",
 				"serviceName": "",
 				"enabled": false
 			}
 		}
 	},
 	"resourceTags": [{
 		"key": "example-key",
 		"value": "example-value"
 	}],
 	"pipelineInfo": {
 		"CodePipeline": {
 			"enabled": false
 		},
 		"Jenkins": {
 			"enabled": false,
 			"jenkinsServerUrl": "",

 			"nodeLabels": [],
 			"apiTokenArn": "",
 			"repoSshCredentialId": "",
 			"awsCredentialId": ""
 		},
 		"AzureDevOps": {
 			"enabled": true,
 			"organizationName": "App2Container",
 			"projectName": "a2c-java-tomcat-9e8e4799-project",
 			"serviceCredName": "azure-devops-to-aws-creds",
 			"agentPoolName": "Azure Pipelines",
 			"personalAccessTokenARN": "arn:aws:secretsmanager:us-east-1:12345678:secret:APP2CONTAINER-PAT"
 		}
 	}
 }
```
