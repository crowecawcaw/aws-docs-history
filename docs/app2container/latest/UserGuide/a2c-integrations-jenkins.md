AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Set up CI/CD pipelines with Jenkins

Jenkins is an open source automation server that which supports building, deploying, and
automating your application with the help of Jenkins Pipeline. Jenkins Pipeline is a suite
of plugins that supports implementing and integrating continuous delivery pipelines into
Jenkins. These plugins can be used to integrate with AWS App2Container to automate deployments for
your applications. App2Container can help configure a Jenkins pipeline in your existing Jenkins
environment.

For more information about using Jenkins, see the [User Handbook overview](https://www.jenkins.io/doc/book/getting-started/ "https://www.jenkins.io/doc/book/getting-started/")
on the Jenkins website.

## Prerequisites

To configure Jenkins pipeline integration for your application container from App2Container,
your application must meet the following criteria.

- A fully functional Jenkins server with the following plugins installed:
  - [Pipeline](https://plugins.jenkins.io/workflow-aggregator/ "https://plugins.jenkins.io/workflow-aggregator/")
  - [Pipeline: AWS Steps](https://plugins.jenkins.io/pipeline-aws/ "https://plugins.jenkins.io/pipeline-aws/")
  - [Git](https://plugins.jenkins.io/git/ "https://plugins.jenkins.io/git/")

- One or more agent nodes, running Linux or Windows must be configured on the
  Jenkins server.

###### Note

The application container platform must match the platform of the agent
node. For example, a Java application that runs on Linux, must use a Linux
agent node for Jenkins. A .NET application that runs on Windows, must use
a Windows agent node.

- Agent nodes must have the following tools installed:
  - **AWS command line tool**
    – To install the AWS CLI or Tools for Windows PowerShell on the agent nodes,
    [follow the
    same steps](a2c-setup.md#setup-aws-profile "a2c-setup.md#setup-aws-profile") that you used to set up your application servers
    and worker machines, except that you do not need to set up an AWS
    profile on the agent node. Agent nodes use the AWS profile that is
    configured on the Jenkins server.
  - **Docker** – The Docker engine
    installation varies by the operating system platform for the server or
    instance where you install it. For more information about the variations,
    see [Install the Docker engine](start-intro.md#setup-install-docker "start-intro.md#setup-install-docker").
  - **Git** – For more information, see the [1.5 Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git") chapter in the
    _Pro Git_ guide, available free to read
    online.

- Agent nodes must be able to connect to AWS and run commands using the AWS CLI.
- The Jenkins server must have access to an existing Git repository for pipeline source.
  The following credentials and resources are required for pipeline builds:
  - Credentials created on the Jenkins server that are used to
    access the Git repository from the Jenkins agent node through SSH. The ID of
    the Jenkins credentials is required in `pipeline.json`
    configuration. For more information about SSH credentials on
    Jenkins, see the [Using
    credentials](https://www.jenkins.io/doc/book/using/using-credentials/ "https://www.jenkins.io/doc/book/using/using-credentials/") chapter in the Jenkins _User Handbook_,
    available online.
  - An AWS profile on the Jenkins server that is used to
    access AWS resources from the Jenkins agent node when the pipeline runs.

- Credentials for App2Container to integrate with Jenkins resources must be created
  and stored in AWS Secrets Manager. For more information, see [Create secrets for Jenkins pipelines](manage-secrets.md#jenkins-secrets "manage-secrets.md#jenkins-secrets")
- The application server or worker machine where the App2Container **generate
  pipeline** command runs must be able to connect to the Git source
  repository and Jenkins server, using the secrets stored in Secrets Manager.

For more information about installing and configuring a Jenkins server,
see the [Installing
Jenkins](https://www.jenkins.io/doc/book/installing/ "https://www.jenkins.io/doc/book/installing/") chapter in the Jenkins _User Handbook_,
available online. The [Jenkins User
Documentation](https://www.jenkins.io/doc/ "https://www.jenkins.io/doc/") also includes tutorials and other reference materials.

## Jenkins integration for App2Container workflow

The process for setting up Jenkins pipelines to refresh components for your
application container integrates smoothly with the App2Container workflow. Applications
follow all the standard steps through deployment. Jenkins integration happens in
the pipeline step.

1. Before you run the **generate pipeline** command, review the
   `pipeline.json` file that was created by the
   **generate app-deployment** command. Configure the parameters
   for your Jenkins pipeline as follows:
   - Set the flags to enable Jenkins deployment.
     - sourceInfo
       - CodeCommit – enabled: **false**
       - ExistingGitRepo – enabled: **true**
       - AzureRepo – enabled: **false**

     - pipelineInfo
       - CodePipeline – enabled: **false**
       - Jenkins – enabled: **true**
       - AzureDevOps – enabled: **false**

   - In the `ExistingGitRepo` object, set the following parameters:
     - repositoryUri (string, required) –
       The URI of the Git repository to use for your pipeline. SSH access
       is required.
     - branch (string, required) – The
       name of the code branch in the Git repository to commit to.
     - sshKeyArn (string, required) – The
       ARN of the secret in Secrets Manager that is used to store the user name and SSH key
       for Git authentication from the Jenkins server.

   - In the `pipelineInfo` section `Jenkins` object, set the following parameters:
     - jenkinsServerUrl (string, required) –
       The URL of the Jenkins server. HTTPS is required for secure access.
     - nodeLabels (array of strings, required) –
       A list of the labels that must be attached to the Jenkins agent node
       that runs the pipeline. All labels specified must be present on the
       agent node for it to run.
     - apiTokenArn (string, required) – The
       ARN of the secret in Secrets Manager that is used to authenticate to the Jenkins server.
     - repoSshCredentialId (string, required) – The ID
       of the credential that you create on the Jenkins server, which
       is used to access the Git repository from the Jenkins agent node
       through SSH. For more information about SSH credentials on
       Jenkins, see the [Using
       credentials](https://www.jenkins.io/doc/book/using/using-credentials/ "https://www.jenkins.io/doc/book/using/using-credentials/") chapter in the Jenkins _User Handbook_,
       available online.
     - awsCredentialId (string, required) – The
       AWS profile on the Jenkins server that is used to access AWS resources
       from the Jenkins agent node when the pipeline runs.

2. When you run the **generate pipeline** command, App2Container validates the
   properties in the `pipeline.json` file, and verifies that initial
   deployment to your container management service has been completed, and that your
   application is active.

The **generate pipeline** command generates the following artifacts
for Jenkins pipelines:

    * Jenkinsfile – App2Container uses the
     Declarative Pipeline syntax to produce the `Jenkinsfile`.
     The file contains the steps and stages (code, build, release, etc.) for the
     Jenkins pipeline. For more information about Jenkins pipeline syntax, see
     [Pipeline
     Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/ "https://www.jenkins.io/doc/book/pipeline/syntax/") on the Jenkins website.


    If you are not using the `--deploy` option with the
     **generate pipeline** command, you can customize the
     `Jenkinsfile`, and then use it to create your pipeline
     using the Jenkins user interface.
    * A `config.xml` file
     – If you are not using the `--deploy` option with the
     **generate pipeline** command, you can use the
     `config.xml` file, along with the
     `Jenkinsfile` to create your pipeline using
     the Jenkins REST API (JenkinsAPI). For more information, see the online
     documentation site: [JenkinsAPI](https://jenkinsapi.readthedocs.io/en/latest/ "https://jenkinsapi.readthedocs.io/en/latest/").
    * Amazon EKS CloudFormation template (for
     Amazon EKS deployment only) – If your application is deploying to Amazon EKS,
     the **generate pipeline** command generates a
     CloudFormation template to create a two-step pipeline. For more information
     about Amazon EKS deployments, see [Deploy application containers to Amazon EKS with AWS App2Container](a2c-integrations-eks.md "a2c-integrations-eks.md")

###### Note

If you are using CodeCommit as your source repository, App2Container creates an SSH key
for the IAM user that is running the command. It provides that SSH key to
the Jenkins server, so that Jenkins can access files in CodeCommit when it runs
the pipeline.

If you run the **generate pipeline** command with the
`--deploy` option, App2Container creates the pipeline in Jenkins, and starts
the pipeline build.
