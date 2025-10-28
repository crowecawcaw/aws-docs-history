AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# App2Container command reference

###### Tip

To containerize your applications with a console-based experience and deploy them on
Amazon ECS on AWS Fargate, you can use the _Replatform applications to
Amazon ECS_ template on the [AWS Migration Hub Orchestrator
console](https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates "https://console.aws.amazon.com/migrationhub/orchestrator?region=us-east-1#/templates"). For more information, see [Replatform
applications to Amazon ECS](../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md "../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md") in the _AWS Migration Hub Orchestrator User
Guide_.

AWS App2Container is a command line tool that transforms supported legacy applications
running on physical servers or virtual machines into applications that run in
Docker containers on Amazon ECS, Amazon EKS, or AWS App Runner.

###### Important

Running App2Container commands on a Linux server requires elevated permissions. Prefix the command syntax
with **sudo**, or run the **sudo su** command one time when you log in before running the
commands as shown in the syntax for the commands linked below.

## Containerization phases

The containerization process has several phases.

###### Phases

- [Initialize](#init-phase "#init-phase")
- [Analyze](#analyze-phase "#analyze-phase")
- [Transform](#transform-phase "#transform-phase")
- [Deploy](#deploy-phase "#deploy-phase")

### Initialize

The **init** command performs one-time initialization tasks for App2Container. This interactive command prompts
for the information required to set up the local App2Container environment. Run this command before you run any other
App2Container commands. If you are using a worker machine to run commands remotely on application
servers, you must also run the **remote configure** command on the worker machine.

**_[init](cmd-init.md "cmd-init.md")_**

Run the **init** command to configure the AWS App2Container
workspace on your application servers and worker machines. If you are
using a worker machine, and running commands remotely, the
**init** command is only required on the worker
machine.

**_[remote configure](cmd-remote-configure.md "cmd-remote-configure.md")_**

After setting up remote access for the worker machine on your application
server (see [Enable remote access for a worker machine
(optional)](start-intro.md#setup-remote-access "start-intro.md#setup-remote-access")), run the **remote
configure** command on the worker machine to configure the
connections needed to run remote workflows on application servers. This
interactive command prompts for the required information for each application
server that you enter.

### Analyze

After you have completed setup and initialization tasks on your servers, you can
begin the analyze phase. Run the version of these commands that applies to your
server setup:

###### Run commands directly on application servers

**_[inventory](cmd-inventory.md "cmd-inventory.md")_**

Run the **inventory** command to produce an inventory
of applications that are running on your application servers, and to
assign each one a unique ID to use when you run other commands.

**_[analyze](cmd-analyze.md "cmd-analyze.md")_**

Run the **analyze** command to analyze your running
applications and to identify dependencies that are required for
containerization. This command creates the
`analysis.json` file that feeds into the
Transform phase commands.

###### Run commands remotely from a worker machine

**_[remote inventory](cmd-remote-inventory.md "cmd-remote-inventory.md")_**

Run the **remote inventory** command from your worker
machine to produce an inventory of applications that are running on your
target application server and to assign each one a unique ID to use when
you run other commands.

**_[remote analyze](cmd-remote-analyze.md "cmd-remote-analyze.md")_**

Run the **remote analyze** command from your worker
machine to analyze the applications running on your target application
server, and to identify dependencies that are required for
containerization. This command creates the
`analysis.json` file that feeds into the
Transform phase commands.

### Transform

The transform phase creates containers for your applications that have gone through analysis. Run the
version of these commands that applies to your server setup:

###### Run the extract directly on application servers, or run the remote extract from a worker machine

**_[extract](cmd-extract.md "cmd-extract.md")_**

Run the **extract** command on your application server
to generate an application archive based on the `analysis.json`
file, created by the **analyze** command. Transfer the archive to
the worker machine for the remaining steps that require the operating system
to support containers.

**_[remote extract](cmd-remote-extract.md "cmd-remote-extract.md")_**

Run the **remote extract** command from your worker
machine to generate an application archive for the applications running
on your target application server, based on the
`analysis.json` file that was created by the
**analyze** command.

###### Run all remaining commands directly on application servers or on a worker machine

**_[containerize](cmd-containerize.md "cmd-containerize.md")_**

Run the **containerize** command for the application
specified in the `--application id` parameter to do the following:

- Extract application artifacts or read from an extract
  archive for the specified application. For complex, multi-component
  Windows applications, this also applies to any additional
  applications or services that run in the same container.
- Generate Docker container artifacts, including a Dockerfile
  and container image, based on the application artifacts, and the
  application settings in the `analysis.json`
  file.
- Create the `deployment.json` file for input
  to the **generate app-deployment** command

### Deploy

The deploy phase consists of deploying an application to your target container
management environment (Amazon ECR with Amazon ECS, Amazon EKS, or AWS App Runner), and optionally creating a CI/CD
pipeline to automate future deployments.

**_[generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md")_**

###### Option 1: Generate deployment artifacts and deploy directly

Run the **generate app-deployment** command with
the `--deploy` option to generate container deployment
artifacts and to deploy them to your target environment all in one
step.

###### Option 2: Generate deployment artifacts and customize

- Run the **generate app-deployment** command without
  the deployment option to generate deployment artifacts.
- Review and customize the generated Amazon ECS, Amazon EKS, or AWS App Runner deployment artifacts.
- Deploy to your target environment using the AWS CLI or AWS console.

**_[generate pipeline](cmd-generate-pipeline.md "cmd-generate-pipeline.md") (optional)_**

###### Option 1: Generate CI/CD pipeline artifacts and deploy directly

Run the **generate pipeline** command with the
`--deploy` option to generate CI/CD pipeline
artifacts and to deploy them with AWS CodePipeline all in one step.

###### Option 2: Generate CI/CD pipeline artifacts and customize

- Run the **generate pipeline** command without
  the deployment option to generate pipeline artifacts.
- Review and customize the generated pipeline artifacts.
- Deploy to your target environment using the AWS CLI or AWS console.

## Utility commands

The following additional commands help you maintain AWS App2Container in your environment.

**[upgrade](cmd-upgrade.md "cmd-upgrade.md")**

Run the **upgrade** command to upgrade your existing
installation of App2Container. This command checks if there is a newer version
of App2Container available, and automatically upgrades if doing so will not
break backwards compatibility with previously generated container artifacts.

**[upload-support-bundle](cmd-upload-support-bundle.md "cmd-upload-support-bundle.md")**

Run the **upload-support-bundle** command for assistance
from the AWS App2Container team for troubleshooting a command failure. This
command securely uploads App2Container logs and supporting artifacts, and an
optional message for your troubleshooting request to the AWS App2Container team.
